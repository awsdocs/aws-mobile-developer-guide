.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-user-data-storage:

#######################################################
Add User File Storage to Your Mobile App with Amazon S3
#######################################################


.. meta::
   :description: Integrating user file storage


.. _overview:

Overview
==============

Enable your app to store and retrieve user files from cloud storage with the permissions model that
suits your purpose. Mobile Hub  :ref:`user-data-storage` deploys and configures cloud storage buckets
using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ (|S3|).


.. _setup-your-backend:

Set Up Your Backend
===================


#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before your proceed.

   If you want to integrate an |S3| bucket that you have already configured, go to :ref:`Integrate an Existing Bucket <how-to-integrate-an-existing-bucket>`.

#. Enable :guilabel:`User File Storage`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User File Storage` tile to enable the feature.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the User File Storage documentation below to connect to your backend.

.. _add-aws-mobile-user-data-storage-app:

Connect to Your Backend
=======================

Make sure to complete the :ref:`add-aws-mobile-user-sign-in-backend-setup` steps before
using the integration steps on this page.

**To add User File Storage to your app**

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle` (Module:app):

            .. code-block:: none

               dependencies {
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app

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

   iOS - Swift
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`Podfile` that you configure to install the AWS Mobile SDK:

            .. code-block:: swift

               platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                     pod 'AWSS3', '~> 2.6.13'   # For file transfers
                     pod 'AWSCognito', '~> 2.6.13'   #For data sync

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
    then create the :code:`TransferUtility` object. :code:`AWSMobileClient` expects an activity context for resuming an authenticated session and creating the credentials provider.

    The following example shows using the :code:`TransferUtility` in the context of an Activity.
    If you are creating :code:`TransferUtility` from an application context, you can construct the :code:`AWSCredentialsProvider` and pass it into :code:`TransferUtility` to use in forming the :code:`AWSConfiguration` object. :code:`TransferUtility` will check the size of file being uploaded and will automatically switch over to using multi-part uploads if the file size exceeds 5 MB.

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

.. _add-aws-user-data-storage-download:

Download a File
===============

.. container:: option

   Android - Java
    To download a file from an Amazon S3 bucket, use :code:`AWSMobileClient`
    to get the :code:`AWSConfigurationand` :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.
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

* Looking for Amazon Cognito Sync? If you are a new user, use `AWS AppSync <https://aws.amazon.com/appsync/>`__ instead. AppSync is a new service for synchronizing application data across devices. Like Cognito Sync, AppSync enables synchronization of a user's own data, such as game state or app preferences. AppSync extends these capabilities by allowing multiple users to synchronize and collaborate in real-time on shared data, such as a virtual meeting space or chatroom. `Start building with AWS AppSync now <https://aws.amazon.com/appsync/>`__
