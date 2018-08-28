
.. _add-aws-mobile-user-data-storage:

#######################################################
Add User File Storage to Your Mobile App with Amazon S3
#######################################################


.. meta::
   :description: Integrating user file storage


.. _overview:

Overview
==============

.. container:: option

   Android - Java
      .. _android-java:

      Enable your app to store and retrieve user files from cloud storage with the permissions model that suits your purpose. The CLI deploys and configures cloud storage buckets using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ (|S3|).

   Android - Kotlin
      .. _android-kotlin:

      Enable your app to store and retrieve user files from cloud storage with the permissions model that suits your purpose. The CLI deploys and configures cloud storage buckets using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ (|S3|).

   iOS - Swift
      .. _ios-swift:

      Enable your app to store and retrieve user files from cloud storage with the permissions model that suits your purpose. The CLI deploys and configures cloud storage buckets using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ (|S3|).

.. _setup-your-backend-user-file-storage:

Set Up Your Backend
===================


#. Complete the :ref:`Get Started <add-aws-mobile-sdk>` steps before you proceed.

#. In a terminal window, navigate to the root of your app files and add the storage category to your app. The CLI will prompt you for configuration parameters.

     .. code-block:: none

        $ cd ./ROOT_OF_YOUR_APP_FILES
        $ amplify storage add

#.  Choose Content as your storage service.

     .. code-block:: none

        ❯ Content (Images, audio, video, etc.)

#. Provide names when prompted by the CLI project. The CLI displays a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

   .. code-block:: none

      $ amplify status
      | Category  | Resource name   | Operation | Provider plugin   |
      | --------- | --------------- | --------- | ----------------- |
      | Storage   | sabc0123de      | Create    | awscloudformation |

#. To create your backend AWS resources run:

     .. code-block:: none

        amplify push

   Use the steps in the next section to connect your app to your backend.

.. _add-aws-mobile-user-data-storage-app:

Connect to Your Backend
=======================

Use the following steps to connect add file storage backend services to your app.

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows.

         #. Add the following to :file:`app/build.gradle` (Module:app):

            .. code-block:: none

               dependencies {
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app.

         #. Add the following to :file:`AndroidManifest.xml`:

            .. code-block:: xml

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- Other manifest / application items . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

               </application>

         #. For each Activity where you make calls to perform user file storage operations, import the
            following packages.

            .. code-block:: none

               import com.amazonaws.mobileconnectors.s3.transferutility.*;

   Android - Kotlin
      Set up AWS Mobile SDK components as follows.

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none

               apply plugin: 'kotlin-android'

               apply plugin: 'kotlin-android-extensions'

               dependencies {
                  implementation"org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app

         #. Add the following to :file:`AndroidManifest.xml`:

            .. code-block:: xml
               :emphasize-lines: 1,7

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- Other manifest / application items . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

               </application>

         #. For each Activity where you make calls to perform user file storage operations, import the
            following packages.

            .. code-block:: none

               import com.amazonaws.mobileconnectors.s3.transferutility.*;

   iOS - Swift
      Set up AWS Mobile SDK components as follows.

         #. Add the following to :file:`Podfile` that you configure to install the AWS Mobile SDK:

            .. code-block:: swift

               platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                     pod 'AWSS3', '~> 2.6.13'   # For file transfers

                     # other pods . . .

                  end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Add the following imports to the classes that perform user file storage operations:

            .. code-block:: none

               import AWSCore
               import AWSS3

         #. Add the following code to your AppDelegate to establish a run-time connection with AWS Mobile.

            .. code-block:: swift

               import UIKit
               import AWSMobileClient

               @UIApplicationMain
               class AppDelegate: UIResponder, UIApplicationDelegate {

                func application(_ application: UIApplication,
                    didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                        return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)
                }
               }



.. _add-aws-user-data-storage-upload:

Upload a File
=============

.. container:: option

   Android - Java
    To upload a file to an Amazon S3 bucket, use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider`,
    and then create the :code:`TransferUtility` object. :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the credentials provider.

    The following example shows how to use the :code:`TransferUtility` in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object. :code:`TransferUtility` checks the size of the file being uploaded and automatically switches over to using multi-part uploads if the file size exceeds 5 MB.

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

                public void uploadWithTransferUtility() {

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

    The following example shows how to use the :code:`TransferUtility` in the context of an Activity.

    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object. :code:`TransferUtility` checks the size of the file being uploaded and automatically switches over to using multi-part uploads if the file size exceeds 5 MB.

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

            class YourActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)

                    AWSMobileClient.getInstance().initialize(this).execute()
                    uploadWithTransferUtility()
                }

                fun uploadWithTransferUtility() {
                    val transferUtility = TransferUtility.builder()
                        .context(this.applicationContext)
                        .awsConfiguration(AWSMobileClient.getInstance().configuration)
                        .s3Client(AmazonS3Client(AWSMobileClient.getInstance().credentialsProvider))
                        .build()

                    val uploadObserver = transferUtility.upload("s3folder/s3key.txt", File("/path/to/localfile.txt"))

                    // Attach a listener to the observer
                    uploadObserver.setTransferListener(object : TransferListener {
                        override fun onStateChanged(id: Int, state: TransferState) {
                            if (state == TransferState.COMPLETED) {
                                // Handle a completed upload
                            }
                        }

                        override fun onProgressChanged(id: Int, current: Long, total: Long) {
                            val done = (((current.toDouble() / total) * 100.0).toInt())
                            Log.d(LOG_TAG, "UPLOAD - - ID: $id, percent done = $done")
                        }

                        override fun onError(id: Int, ex: Exception) {
                            Log.d(LOG_TAG, "UPLOAD ERROR - - ID: $id - - EX: ${ex.message.toString()}")
                        }
                    })

                    // If you prefer to long-poll for updates
                    if (uploadObserver.state == TransferState.COMPLETED) {
                        /* Handle completion */
                    }

                    val bytesTransferred = uploadObserver.bytesTransferred
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

.. _add-aws-user-data-storage-download:

Download a File
===============

.. container:: option

   Android - Java
    To download a file from an Amazon S3 bucket, use :code:`AWSMobileClient`
    to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
    :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the :code:`AWSCredentialsProvider`.

    The following example shows how to use the :code:`TransferUtility` in the context of an Activity.
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

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    AWSMobileClient.getInstance().initialize(this).execute();
                    downloadWithTransferUtility();
                }

                private void downloadWithTransferUtility() {

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

                                Log.d(LOG_TAG, "   ID:" + id + "   bytesCurrent: " + bytesCurrent + "   bytesTotal: " + bytesTotal + " " + percentDone + "%");
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

                    Log.d(LOG_TAG, "Bytes Transferred: " + downloadObserver.getBytesTransferred());
                    Log.d(LOG_TAG, "Bytes Total: " + downloadObserver.getBytesTotal());
                }
            }

   Android - Kotlin
    To download a file from an Amazon S3 bucket, use :code:`AWSMobileClient`
    to get the :code:`AWSConfiguration` and  :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
    :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the :code:`AWSCredentialsProvider`.

    The following example shows how to use the :code:`TransferUtility` in the context of an Activity.
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

            class YourActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)
                    setContentView(R.layout.activity_your)

                    AWSMobileClient.getInstance().initialize(this).execute()
                    donwloadWithTransferUtility()
                }

                private fun downloadWithTransferUtility() {
                    val transferUtility = TransferUtility.builder()
                        .context(applicationContext)
                        .awsConfiguration(AWSMobileClient.getInstance().configuration)
                        .s3Client(AmazonS3Client(AWSMobileClient.getInstance().credentialsProvider))
                        .build()

                    val downloadObserver = transferUtility.download(
                        "s3folder/s3key.txt",
                        File("/path/to/file/localfile.txt"))

                    // Attach a listener to get state updates
                    downloadObserver.setTransferListener(object : TransferListener {
                        override fun onStateChanged(id: Int, state: TransferState) {
                            if (state == TransferState.COMPLETED) {
                                // Handle a completed upload.
                            }
                        }

                        override fun onProgressChanged(id: Int, current: Long, total: Long) {
                            try {
                                val done = (((current.toDouble() / total) * 100.0).toInt()) //as Int
                                Log.d(LOG_TAG, "DOWNLOAD - - ID: $id, percent done = $done")
                            }
                            catch (e: Exception) {
                                Log.e(LOG_TAG, "Trouble calculating progress percent", e)
                            }
                        }

                        override fun onError(id: Int, ex: Exception) {
                            Log.d(LOG_TAG, "DOWNLOAD ERROR - - ID: $id - - EX: ${ex.message.toString()}")
                        }
                    })

                    // If you prefer to poll for the data, instead of attaching a
                    // listener, check for the state and progress in the observer.
                    if (downloadObserver.state == TransferState.COMPLETED) {
                        // Handle a completed upload.
                    }

                    Log.d(LOG_TAG, "Bytes Transferred: ${downloadObserver.bytesTransferred}");
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

* For more information about TransferUtility capabilities, see :ref:`how-to-transfer-files-with-transfer-utility`.

* For sample apps that demonstrate TransferUtility capabilities, see `Android S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-android-samples/tree/master/S3TransferUtilitySample>`__ and `iOS S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferUtility-Sample>`__.

* Looking for Amazon Cognito Sync? If you are a new user, use `AWS AppSync <https://aws.amazon.com/appsync/>`__ instead. AppSync is a new service for synchronizing application data across devices. Like Cognito Sync, AppSync enables synchronization of a user's own data, such as game state or app preferences. AppSync extends these capabilities by allowing multiple users to synchronize and collaborate in real time on shared data, such as a virtual meeting space or chat room. `Start building with AWS AppSync now <https://aws.amazon.com/appsync/>`__
