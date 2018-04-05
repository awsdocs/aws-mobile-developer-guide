.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

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

To configure a new Amazon S3 bucket, see .

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

Set up the required Amazon IAM permissions
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

#. Copy and keep the bucket name value from the breadcrumb at the top of the console, for use in a following step.

#. Copy and keep the bucket's region, for use in a following step.

.. _how-to-storage-connect-to-your-backend:

Connect to Your Backend
=======================

Create the awsconfiguration.json file
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
          "Default" : {

          }
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

    * Replace the :code:`COGNITO-IDENTITY-POOL-REGION` with the region the identity pool was created in.

    * Replace the :code:`S3-BUCKET-NAME` with the name of your bucket.

    * Replace the :code:`S3-REGION` with the region your bucket was created in.


Add the awsconfiguration.json file to your app
-----------------------------------------------

.. container:: option

    Android - Java
      Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown menu.

          .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
             :scale: 100
             :alt: Image of selecting a Raw Android Resource Directory in Android Studio.

          .. only:: pdf

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 50

          .. only:: kindle

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 75

      Drag the :file:`awsconfiguration.json` you created into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

    iOS - Swift
      Drag the :file:`awsconfiguration.json` into the folder containing your :file:`Info.plist` file in your Xcode project. Choose :guilabel:`Copy items` and :guilabel:`Create groups` in the options dialog.


    iOS - Swift
      Place the :file:`awsconfiguration.json` into the folder containing your :file:`Info.plist` file in your Xcode project. Choose :guilabel:`Copy items` and :guilabel:`Create groups` in the options dialog.


Add the SDK to your App
-----------------------

.. container:: option

   Android - Java
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

         #. For each Activity where you make calls to perform user data storage operations, import the
            following packages.

            .. code-block:: none
               :emphasize-lines: 1-2

               import com.amazonaws.mobile.config.AWSConfiguration;
               import com.amazonaws.mobileconnectors.s3.transferutility.*;

         #. Add the following code to the :code:`onCreate` method of your main or startup activity. This will establish a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

            .. code-block:: java

              import com.amazonaws.mobile.client.AWSMobileClient;

              public class YourMainActivity extends Activity {
               @Override
               protected void onCreate(Bundle savedInstanceState) {
                   super.onCreate(savedInstanceState);

                   AWSMobileClient.getInstance().initialize(this).execute();
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

         #. Add the following imports to the classes that perform user data storage operations:

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

Once your backend is setup and connected to your app, use the following steps to upload and download a file using the SDK's transfer utility.

.. _native-how-to-integrate-add-aws-user-data-storage-upload:

Upload a File
--------------

.. container:: option

   Android - Java
    To upload a file to an Amazon S3 bucket, use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider`,
    then create the :code:`TransferUtility` object. :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the credentials provider.

    The following example shows using the :code:`TransferUtility `in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and
    pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object.. The :code:`TransferUtility` will check
    the size of file being uploaded and will automatically switch over to using multi-part uploads if the file size exceeds 5 MB.

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

                    Log.d("YourActivity", "Bytes Transferrred: " + uploadObserver.getBytesTransferred());
                    Log.d("YourActivity", "Bytes Total: " + uploadObserver.getBytesTotal());
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
    to get the :code:`AWSConfigurationand` :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
    :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the :cdoe:`AWSCredentialsProvider`.

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

                    Log.d("YourActivity", "Bytes Transferrred: " + downloadObserver.getBytesTransferred());
                    Log.d("YourActivity", "Bytes Total: " + downloadObserver.getBytesTotal());
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
