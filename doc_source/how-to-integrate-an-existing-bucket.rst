
.. _how-to-integrate-an-existing-bucket:

#####################################
How to Integrate Your Existing Bucket
#####################################

.. _native-integrate-exisitng-bucket:

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-user-data-storage>` to install the SDK and integrate Amazon S3.

*Or, use the contents of this page if your app will integrate existing AWS services.*



The following steps  include:

    * Set up short-lived credentials for accessing your AWS resources using a `Cognito Identity Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html>`__.

    * Create an AWS Mobile configuration file that ties your app code to your bucket.


Set Up Your Backend
===================

If you already have a Cognito Identity Pool and have its unauthenticated IAM role set up with read/write permissions on the S3 bucket, you can skip to :ref:`get-your-bucket-name`.

Create or Import the Amazon Cognito Identity Pool
--------------------------------------------------

#. Go to `Amazon Cognito Console <https://console.aws.amazon.com/cognito>`__ and choose :guilabel:`Manage Federated Identities`.

#. Choose :guilabel:`Create new Identity pool` on the top left of the console.

#. Type a name for the Identity pool, select :guilabel:`Enable access to unauthenticated identities` under the :guilabel:`Unauthenticated Identities` section, and then choose :guilabel:`Create pool` on the bottom right.

#. Expand the :guilabel:`View Details` section to see the two roles that are to be created to enable access to your bucket. Copy and keep the Unauthenticated role name, in the form of :code:`Cognito_<IdentityPoolName>Unauth_Role`, for use in a following configuration step. Choose  :guilabel:`Allow` on the bottom right.

#. In the code snippet labeled :guilabel:`Get AWSCredentials` displayed by the console, copy the Identity Pool ID and the Region for use in a following configuration step.

Set Up the Required Amazon IAM Permissions
-------------------------------------------

#. Go to `Amazon IAM Console <https://console.aws.amazon.com/iam/home>`__ and choose :guilabel:`Roles`.

#. Choose the unauthenticated role whose name you copied in a previous step.

#. Choose :guilabel:`Attach Policy`, select the :code:`AmazonS3FullAccess` policy, and then choose :guilabel:`Attach Policy` to attach it to the role.

.. list-table::
   :widths: 1 6

   * - **Note**

     - The :code:`AmazonS3FullAccess` policy will grant users in the identity pool full access to all buckets and operations in |S3|. In a real app, you should restrict users to only have access to the specific resources they need. For more information, see :ref:`Amazon S3 Security Considerations <s3-security>`.

.. _get-your-bucket-name:

Get Your Bucket Name and ID
---------------------------

#. Go to `Amazon S3 Console <https://console.aws.amazon.com/s3/home>`__ and select the bucket you want to integrate.

#. Copy and keep the bucket name value from the breadcrumb at the top of the console for use later.

#. Copy and keep the bucket's region for use later.

.. _how-to-storage-connect-to-your-backend:

Connect to Your Backend
=======================

Create the awsconfiguration.json File
-------------------------------------

#. Create a file with name :file:`awsconfiguration.json` with the following contents:

    .. code-block:: json

      {
          "Version": "1.0",
          "CredentialsProvider": {
              "CognitoIdentity": {
                  "Default": {
                      "PoolId": "COGNITO-IDENTITY-POOL-ID",
                      "Region": "COGNITO-IDENTITY-POOL-REGION"
                  }
              }
          },
          "IdentityManager" : {
            "Default" : { }
          },
          "S3TransferUtility": {
              "Default": {
                  "Bucket": "S3-BUCKET-NAME",
                  "Region": "S3-REGION"
              }
          }
      }

#. Make the following changes to the configuration file.

    * Replace the :code:`COGNITO-IDENTITY-POOL-ID` with the identity pool ID.

    * Replace the :code:`COGNITO-IDENTITY-POOL-REGION` with the Region the identity pool was created in.

    * Replace the :code:`S3-BUCKET-NAME` with the name of your bucket.

    * Replace the :code:`S3-REGION` with the Region your bucket was created in.


Add the awsconfiguration.json File to Your App
-----------------------------------------------

.. container:: option

    Android - Java
      In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

          .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
             :scale: 100
             :alt: Image of creating a raw directory in Android Studio.

          .. only:: pdf

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 50

          .. only:: kindle

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 75

      Drag the :file:`awsconfiguration.json` you created into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

    Android - Kotlin
      In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

          .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
             :scale: 100
             :alt: Image of creating a raw directory in Android Studio.

          .. only:: pdf

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 50

          .. only:: kindle

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 75

      Drag the :file:`awsconfiguration.json` you created into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

    iOS - Swift
      Drag the :file:`awsconfiguration.json` into the Xcode Project Navigator folder containing :file:`Info.plist`. Choose :guilabel:`Copy items` and :guilabel:`Create groups` in the options dialog.


Add the SDK to Your App
-----------------------

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none

               dependencies {
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app

         #. Add the following to :file:`AndroidManifest.xml`:

            .. code-block:: xml

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

                  <!- . . . ->

               </application>

         #. For each Activity where you make calls to perform user file storage operations, import the
            following packages.

            .. code-block:: none

               import com.amazonaws.mobile.config.AWSConfiguration;
               import com.amazonaws.mobileconnectors.s3.transferutility.*;

         #. Add the following code to the :code:`onCreate` method of your main or startup activity. This establishes a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

            .. code-block:: java

              import com.amazonaws.mobile.client.AWSMobileClient;

              public class YourMainActivity extends Activity {
               @Override
               protected void onCreate(Bundle savedInstanceState) {
                   super.onCreate(savedInstanceState);

                   AWSMobileClient.getInstance().initialize(this).execute();
                }
              }

   Android - Kotlin
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none
               :emphasize-lines: 1-3

               dependencies {
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app

         #. Add the following to :file:`AndroidManifest.xml`:

            .. code-block:: xml
               :emphasize-lines: 1,7

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

                  <!- . . . ->

               </application>

         #. For each Activity where you make calls to perform user file storage operations, import the
            following packages.

            .. code-block:: none
               :emphasize-lines: 1-2

               import com.amazonaws.mobile.config.AWSConfiguration;
               import com.amazonaws.mobileconnectors.s3.transferutility.*;

         #. Add the following code to the :code:`onCreate` method of your main or startup activity. This will establish a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

            .. code-block:: java

              import com.amazonaws.mobile.client.AWSMobileClient;

              class MainActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                  super.onCreate(savedInstanceState)
                  AWSMobileClient.getInstance().initialize(this).execute()
                }
              }

   iOS - Swift
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`Podfile` that you configure to install the AWS Mobile SDK:

            .. code-block:: swift

               platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                     pod 'AWSMobileClient', '~> 2.6.13'  # For AWSMobileClient
                     pod 'AWSS3', '~> 2.6.13'            # For file transfers
                     pod 'AWSCognito', '~> 2.6.13'       # For data sync

                     # other pods

                  end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you might need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Add the following imports to the classes that perform user file storage operations:

            .. code-block:: none

               import AWSCore
               import AWSS3

         #. Add the following code to your AppDelegate to establish a run-time connection with AWS Mobile.

            .. code-block:: swift

                import UIKit
                import AWSCore
                import AWSMobileClient

                @UIApplicationMain
                class AppDelegate: UIResponder, UIApplicationDelegate {


                    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                        //Instantiate AWSMobileClient to establish AWS user credentials
                        return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)
                    }
                }



Implement Storage Operations
============================

After your backend is set up and connected to your app, use the following steps to upload and download a file using the SDK's transfer utility.

.. _native-how-to-integrate-add-aws-user-data-storage-upload:

Upload a File
--------------

.. container:: option

   Android - Java
    To upload a file to an Amazon S3 bucket, use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider`,
    then create the :code:`TransferUtility` object. :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the credentials provider.

    The following example shows using the :code:`TransferUtility `in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and
    pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object.. The :code:`TransferUtility` checks
    the size of file being uploaded and automatically uses multi-part uploads if the file size exceeds 5 MB.

       .. code-block:: java

            import android.app.Activity;
            import android.util.Log;

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;
            import com.amazonaws.services.s3.AmazonS3Client;

            import java.io.File;

            public class YourActivity extends Activity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    AWSMobileClient.getInstance().initialize(this).execute();
                    uploadWithTransferUtility();
                }

                private void uploadWithTransferUtility() {

                    TransferUtility transferUtility =
                        TransferUtility.builder()
                            .context(getApplicationContext())
                            .awsConfiguration(AWSMobileClient.getInstance().getConfiguration())
                            .s3Client(new AmazonS3Client(AWSMobileClient.getInstance().getCredentialsProvider()))
                            .build();

                    TransferObserver uploadObserver =
                        transferUtility.upload(
                            "s3Folder/s3Key.txt",
                            new File("/path/to/file/localFile.txt"));

                    // Attach a listener to the observer to get state update and progress notifications
                    uploadObserver.setTransferListener(new TransferListener() {

                        @Override
                        public void onStateChanged(int id, TransferState state) {
                            if (TransferState.COMPLETED == state) {
                                // Handle a completed upload.
                            }
                        }

                        @Override
                        public void onProgressChanged(int id, long bytesCurrent, long bytesTotal) {
                            float percentDonef = ((float) bytesCurrent / (float) bytesTotal) * 100;
                            int percentDone = (int)percentDonef;

                            Log.d("YourActivity", "ID:" + id + " bytesCurrent: " + bytesCurrent
                                    + " bytesTotal: " + bytesTotal + " " + percentDone + "%");
                        }

                        @Override
                        public void onError(int id, Exception ex) {
                            // Handle errors
                        }

                    });

                    // If you prefer to poll for the data, instead of attaching a
                    // listener, check for the state and progress in the observer.
                    if (TransferState.COMPLETED == uploadObserver.getState()) {
                        // Handle a completed upload.
                    }

                    Log.d("YourActivity", "Bytes Transferred: " + uploadObserver.getBytesTransferred());
                    Log.d("YourActivity", "Bytes Total: " + uploadObserver.getBytesTotal());
                }
            }

   Android - Kotlin
    To upload a file to an Amazon S3 bucket, use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider`,
    then create the :code:`TransferUtility` object. :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the credentials provider.

    The following example shows using the :code:`TransferUtility `in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and
    pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object.. The :code:`TransferUtility` will check
    the size of file being uploaded and will automatically switch over to using multi-part uploads if the file size exceeds 5 MB.

       .. code-block:: kotlin

            import android.os.Bundle
            import android.support.v7.app.AppCompatActivity
            import android.util.Log
            import com.amazonaws.AmazonServiceException
            import com.amazonaws.mobile.client.AWSMobileClient
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferState
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility
            import com.amazonaws.services.s3.AmazonS3Client
            import kotlinx.android.synthetic.main.activity_main.*
            import java.io.File;


            import java.io.File;

            class MainActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate()
                    AWSMobileClient.getInstance().initialize(this).execute()
                    uploadWithTransferUtility(
                        "s3Folder/s3Key.txt"
                        File("/path/to/file/localfile.txt")
                    )
                }

                private fun uploadWithTransferUtility(remote: String, local: File) {
                    val transferUtility = TransferUtility.builder()
                            .context(this.applicationContext)
                            .awsConfiguration(AWSMobileClient.getInstance().configuration)
                            .s3Client(AmazonS3Client(AWSMobileClient.getInstance().credentialsProvider))
                            .build()

                    val uploadObserver = transferUtility.upload(remote, local)

                    uploadObserver.transferListener = object : TransferListener() {
                        override fun onStateChanged(id: Int, state: TransferState) {
                            if (state == TransferState.COMPLETED) {
                                // Handle a completed upload
                            }
                        }

                        override fun onProgressChanged(id: Int, current: Long, total: Long) {
                            val done = (((current.toDouble() / total) * 100.0).toInt())
                            Log.d(TAG, "ID: $id, percent done = $done")
                        }

                        override fun onError(id: Int, ex: Exception) {
                            // Handle errors
                        }
                    }

                    // If you prefer to poll for the data, instead of attaching a
                    // listener, check for the state and progress in the observer.
                    if (uploadObserver.state == TransferState.COMPLETED) {
                        // Handle a completed upload.
                    }
                }
            }

   iOS - Swift
     The following example shows how to upload a file to an |S3| bucket.

       .. code-block:: swift

          func uploadData() {

             let data: Data = Data() // Data to be uploaded

             let expression = AWSS3TransferUtilityUploadExpression()
                expression.progressBlock = {(task, progress) in
                   DispatchQueue.main.async(execute: {
                     // Do something e.g. Update a progress bar.
                  })
             }

             var completionHandler: AWSS3TransferUtilityUploadCompletionHandlerBlock?
             completionHandler = { (task, error) -> Void in
                DispatchQueue.main.async(execute: {
                   // Do something e.g. Alert a user for transfer completion.
                   // On failed uploads, `error` contains the error object.
                })
             }

             let transferUtility = AWSS3TransferUtility.default()

             transferUtility.uploadData(data,
                  bucket: "YourBucket",
                  key: "YourFileName",
                  contentType: "text/plain",
                  expression: expression,
                  completionHandler: completionHandler).continueWith {
                     (task) -> AnyObject! in
                         if let error = task.error {
                            print("Error: \(error.localizedDescription)")
                         }

                         if let _ = task.result {
                            // Do something with uploadTask.
                         }
                         return nil;
                 }
          }

.. _native-how-to-integrate-add-aws-user-data-storage-download:

Download a File
----------------

.. container:: option

   Android - Java
    To download a file from an Amazon S3 bucket, use :code:`AWSMobileClient`
    to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
    :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the :code:`AWSCredentialsProvider`.

    The following example shows using the :code:`TransferUtility` in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and
    pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object.

      .. code-block:: java

            import android.app.Activity;
            import android.util.Log;

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;
            import com.amazonaws.services.s3.AmazonS3Client;

            import java.io.File;

            public class YourActivity extends Activity {

                public void dowloadData() {
                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                        @Override
                        public void onComplete() {
                            downloadWithTransferUtility();
                        }
                    }).execute();
                }

                public void downloadWithTransferUtility() {

                    TransferUtility transferUtility =
                        TransferUtility.builder()
                                .context(getApplicationContext())
                                .awsConfiguration(AWSMobileClient.getInstance().getConfiguration())
                                .s3Client(new AmazonS3Client(AWSMobileClient.getInstance().getCredentialsProvider()))
                                .build();

                    TransferObserver downloadObserver =
                        transferUtility.download(
                                "s3Folder/s3Key.txt",
                                new File("/path/to/file/localFile.txt"));

                    // Attach a listener to the observer to get state update and progress notifications
                    downloadObserver.setTransferListener(new TransferListener() {

                        @Override
                        public void onStateChanged(int id, TransferState state) {
                            if (TransferState.COMPLETED == state) {
                                // Handle a completed upload.
                            }
                        }

                        @Override
                        public void onProgressChanged(int id, long bytesCurrent, long bytesTotal) {
                                float percentDonef = ((float)bytesCurrent/(float)bytesTotal) * 100;
                                int percentDone = (int)percentDonef;

                                Log.d("MainActivity", "   ID:" + id + "   bytesCurrent: " + bytesCurrent + "   bytesTotal: " + bytesTotal + " " + percentDone + "%");
                        }

                        @Override
                        public void onError(int id, Exception ex) {
                            // Handle errors
                        }

                    });

                    // If you prefer to poll for the data, instead of attaching a
                    // listener, check for the state and progress in the observer.
                    if (TransferState.COMPLETED == downloadObserver.getState()) {
                        // Handle a completed upload.
                    }

                    Log.d("YourActivity", "Bytes Transferred: " + downloadObserver.getBytesTransferred());
                    Log.d("YourActivity", "Bytes Total: " + downloadObserver.getBytesTotal());
                }
            }

   Android - Kotlin
    To download a file from an Amazon S3 bucket, use :code:`AWSMobileClient`
    to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
    :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the :code:`AWSCredentialsProvider`.

    The following example shows using the :code:`TransferUtility` in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and
    pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object.

      .. code-block:: kotlin

            import android.app.Activity;
            import android.util.Log;

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;
            import com.amazonaws.services.s3.AmazonS3Client;

            import java.io.File;

            class MainActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate()
                    AWSMobileClient.getInstance().initialize(this).execute()
                    downloadWithTransferUtility(
                        "s3Folder/s3Key.txt"
                        File("/path/to/file/localfile.txt")
                    )
                }

                private fun downloadWithTransferUtility(remote: String, local: File) {
                    val transferUtility = TransferUtility.builder()
                            .context(getApplicationContext)
                            .awsConfiguration(AWSMobileClient.getInstance().configuration)
                            .s3Client(AmazonS3Client(AWSMobileClient.getInstance().credentialsProvider))
                            .build()

                    val downloadObserver = transferUtility.download(remote, local)

                    downloadObserver.transferListener = object : TransferListener() {
                        override fun onStateChanged(id: Int, state: TransferState) {
                            if (state == TransferState.COMPLETED) {
                                // Handle a completed upload
                            }
                        }

                    override fun onProgressChanged(id: Int, current: Long, total: Long) {
                        try {
                            val done = (((current.toDouble() / total) * 100.0).toInt()) //as Int
                            Log.d("downloadObserver", "DOWNLOAD - - ID: $id, percent done = $done")
                        }
                        catch (e: Exception) {
                            // Handle errors
                        }
                    }

                        override fun onError(id: Int, ex: Exception) {
                            // Handle errors
                        }
                    }

                    // If you prefer to poll for the data, instead of attaching a
                    // listener, check for the state and progress in the observer.
                    if (downloadObserver.state == TransferState.COMPLETED) {
                        // Handle a completed upload.
                    }
                }
            }

   iOS - Swift
     The following example shows how to download a file from an |S3| bucket.

       .. code-block:: swift

          func downloadData() {
             let expression = AWSS3TransferUtilityDownloadExpression()
             expression.progressBlock = {(task, progress) in DispatchQueue.main.async(execute: {
                // Do something e.g. Update a progress bar.
                })
             }

             var completionHandler: AWSS3TransferUtilityDownloadCompletionHandlerBlock?
             completionHandler = { (task, URL, data, error) -> Void in
                DispatchQueue.main.async(execute: {
                // Do something e.g. Alert a user for transfer completion.
                // On failed downloads, `error` contains the error object.
                })
             }

             let transferUtility = AWSS3TransferUtility.default()
             transferUtility.downloadData(
                   fromBucket: "YourBucket",
                   key: "YourFileName",
                   expression: expression,
                   completionHandler: completionHandler
                   ).continueWith {
                      (task) -> AnyObject! in if let error = task.error {
                         print("Error: \(error.localizedDescription)")
                      }

                      if let _ = task.result {
                        // Do something with downloadTask.

                      }
                      return nil;
                  }
          }


Next Steps
==========

* For further information about TransferUtility capabilities, see :ref:`how-to-transfer-files-with-transfer-utility`.

* For sample apps that demonstrate TransferUtility capabilities, see `Android S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-android-samples/tree/master/S3TransferUtilitySample>`__ and `iOS S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferUtility-Sample>`__.
