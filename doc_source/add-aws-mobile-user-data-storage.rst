.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-user-data-storage:

#######################################################
Add User Data Storage to Your Mobile App with Amazon S3
#######################################################


.. meta::
   :description: Integrating user data storage


.. _overview:

Overview
==============


Enable your app to store and retrieve user files from cloud storage with the permissions model that
suits your purpose. |AMH|  :ref:`user-data-storage` deploys and configures cloud storage buckets
using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`_ (|S3|).

The User Data Storage feature also uses `Amazon Cognito Sync <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/add-aws-mobile-user-data-storage.html>`_. This service enables your app to sync key/name
pair app data, like user profiles, to the cloud and other devices.


.. _setup-your-backend:

Set Up Your Backend
===================


#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before your proceed.

   If you want to integrate an |S3| bucket that you have already configured, go to :ref:`Integrate an Existing Bucket <how-to-integrate-an-existing-bucket>`.

#. Enable :guilabel:`User Data Storage`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`_ and choose the :guilabel:`User Data Storage` tile to enable the feature.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the User Data Storage documentation below to connect to your backend.

.. _add-aws-mobile-user-data-storage-app:

Connect to your backend
=======================

Make sure to complete the :ref:`add-aws-mobile-user-sign-in-backend-setup` steps before
using the integration steps on this page.

**To add User Data Storage to your app**

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none
               :emphasize-lines: 2-3

               dependencies {
                  compile 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  compile 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
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

                     pod 'AWSS3', '~> 2.6.6'   # For file transfers
                     pod 'AWSCognito', '~> 2.6.6'   #For data sync
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
               import AWSMobileClient

               @UIApplicationMain
               class AppDelegate: UIResponder, UIApplicationDelegate {

                 func application(_ application: UIApplication,
                       didFinishLaunchingWithOptions launchOptions:

                       [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                           return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)
                 }
               }



.. _add-aws-user-data-storage-upload:

Upload a File
=============

.. container:: option

   Android - Java
     The following example shows how to upload a file to an |S3| bucket.

     Use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider`, then create the :code:`TransferUtility` object.

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

                public void uploadData() {

                  // Initialize AWSMobileClient if not initialized upon the app startup.
                  // AWSMobileClient.getInstance().initialize(this).execute();

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

                  uploadObserver.setTransferListener(new TransferListener() {

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

                  // If your upload does not trigger the onStateChanged method inside your
                  // TransferListener, you can directly check the transfer state as shown here.
                  if (TransferState.COMPLETED == uploadObserver.getState()) {
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

.. _add-aws-user-data-storage-download:

Download a File
===============

.. container:: option

   Android - Java
     The following example shows how to download a file from an |S3| bucket. We use :code:`AWSMobileClient` to get the :code:`AWSConfiguration` and :code:`AWSCredentialsProvider` to create the :code:`TransferUtility` object.

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

               public void downloadData() {

                  // Initialize AWSMobileClient if not initialized upon the app startup.
                  // AWSMobileClient.getInstance().initialize(this).execute();

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


.. _add-aws-user-data-storage-sync:

Save User Profile Data
======================


The following shows how to load user settings and access those settings using |COG| Sync.

.. container:: option

   Android - Java
     .. code-block:: java
       :emphasize-lines: 1-42

        import java.util.List;

        import com.amazonaws.auth.CognitoCachingCredentialsProvider;

        import com.amazonaws.mobileconnectors.cognito.CognitoSyncManager;
        import com.amazonaws.mobileconnectors.cognito.Dataset;
        import com.amazonaws.mobileconnectors.cognito.exceptions.DataStorageException;
        import com.amazonaws.auth.CognitoCachingCredentialsProvider;

        public void saveProfileData() {

           CognitoSyncManager manager =
              new CognitoSyncManager(getApplicationContext(), (CognitoCachingCredentialsProvider)AWSMobileClient.getInstance().getCredentialsProvider(),
                        AWSMobileClient.getInstance().getConfiguration());

           Dataset dataset = manager.openOrCreateDataset("myDataset");
           dataset.put("myKey", "myValue");

           // synchronize dataset with the Cloud
           dataset.synchronize(new Dataset.SyncCallback() {
              public void onSuccess(Dataset dataset, List list) {

              }

              public boolean onConflict(Dataset dataset, List list) {
                 return false;
              }

              public boolean onDatasetDeleted(Dataset dataset, String list) {
                 return true;
              }

              public boolean onDatasetsMerged(Dataset dataset, List list) {
                 return true;
              }

              public void onFailure(DataStorageException exception) {

              }
           });
        }


   iOS - Swift
     .. code-block:: swift
       :emphasize-lines: 0

        import AWSCore
        import AWSCognito


        func loadSettings() {
           let syncClient: AWSCognito = AWSCognito.default()
           let userSettings: AWSCognitoDataset = syncClient.openOrCreateDataset("user_settings")

           userSettings.synchronize().continueWith { (task: AWSTask<AnyObject>) -> Any? in
              if let error = task.error as NSError? {
                 print("loadSettings error: \(error.localizedDescription)")
                 return nil;
              }
              let titleTextColorString = userSettings.string(forKey: "titleTextColorStringKey")
              let titleBarColorString = userSettings.string(forKey: "titleBarColorStringKey")
              let backgroundColorString = userSettings.string(forKey: "backgroundColorStringKey")
              return nil;
           }
        }


Next Steps
==========

* For further information about TransferUtility capabilities, see :ref:`how-to-transfer-files-with-transfer-utility`.

* For sample apps that demonstrate TransferUtility capabilities, see `Android S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-android-samples/tree/master/S3TransferUtilitySample>`_ and `iOS S3 TransferUtility Sample <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferUtility-Sample>`_.

