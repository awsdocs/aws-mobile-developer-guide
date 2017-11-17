.. _add-aws-mobile-user-data-storage:

########################################
Add User Data Storage to Your Mobile App
########################################


.. meta::
   :description: Integrating user data storage


.. _add-aws-user-data-storage-overview:

User Data Storage
=================


Enable your app to store and retrieve user files from cloud storage with the permissions model that
suits your purpose. |AMH|  :ref:`user-data-storage` deploys and configures cloud storage buckets
using `Amazon Simple Storage Service <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`_ (|S3|).

The User Data Storage feature also uses `Amazon Cognito Sync <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/add-aws-mobile-user-data-storage.html>`_. This service enables your app to sync key/name
pair app data, like user profiles, to the cloud and other devices.


.. _add-aws-user-data-storage-backend-setup:

Set Up Your Backend
===================


#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the
   integration steps on this page.

#. Use |AMHlong| to deploy your backend.


   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a project name, and then choose :guilabel:`Create project` or select a previously created project.

   #. Choose the :guilabel:`User Data Storage` tile to enable the feature.

#. Download your updated |AMH| project configuration file and replace it in your project (see :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` for more information).  Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app.

.. _add-aws-mobile-user-data-storage-app:

Add The SDK to Your App
=======================

Make sure to complete the :ref:`add-aws-mobile-user-sign-in-backend-setup` steps before
using the integration steps on this page.

**To add User Data Storage to your app**

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml
               :emphasize-lines: 1,7

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

                  <!- . . . ->

               </application>

         #. :file:`app/build.gradle` must contain:

            .. code-block:: none
               :emphasize-lines: 2-3

               dependencies{
                  compile 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  compile 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

         #. For each Activity where you make calls to perform database operations, import the
            following APIs.

            .. code-block:: none
               :emphasize-lines: 1-2

               import com.amazonaws.mobile.config.AWSConfiguration;
               import com.amazonaws.mobileconnectors.s3.transferutility.*;


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

               .. code-block:: swift

                  platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                     pod 'AWSS3', '~> 2.6.6'   # For file transfers
                     pod 'AWSCognito', '~> 2.6.6'   #For data sync
                     # other pods

                  end

               Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |S3| APIs must use the following import statements:

            .. code-block:: none

               import AWSCore
               import AWSS3

      #. Add your backend service configuration to the app.

         From the location where your |AMH| configuration file was downloaded in a previous step,
         drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file
         in your Xcode project.

         Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.



.. _add-aws-user-data-storage-upload:

Upload a File to User Store
===========================


.. container:: option

   Android - Java
     The following example shows how to upload a file to an |S3| bucket.

       .. code-block:: java
         :emphasize-lines: 1-6, 9-53

            import java.io.File;

            import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
            import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;

            public class YourActivity extends Activity {
                public void uploadData() {

                TransferUtility transferUtility =
                      TransferUtility.builder()
                            .context(getApplicationContext())
                            .awsConfiguration(awsConfig)
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
                   public void onProgressChanged(
                      int id, long bytesCurrent, long bytesTotal) {
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

             let data : Data  // Data to be uploaded

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

Download a File from User Store
===============================


.. container:: option

   Android - Java
     The following example shows how to download a file from an |S3| bucket.

       .. code-block:: java
         :emphasize-lines: 1-6, 9-44

          import java.io.File;

          import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
          import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
          import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
          import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;

          public class YourActivity extends Activity {
               public void downloadData() {

                TransferUtility transferUtility =
                      TransferUtility.builder()
                            .context(getApplicationContext())
                            .awsConfiguration(AWSMobileClient.getInstance().getConfiguration())
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




