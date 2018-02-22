.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-transfer-files-with-transfer-utility:

######################################################
Transfer Files and Data Using TransferUtility and |S3|
######################################################

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-user-data-storage>` to install the SDK and integrate Amazon S3.

*Or, use the contents of this page if your app will integrate existing AWS services.*




This page explains how to implement upload and download functionality and a number of additional storage use cases.

The examples on this page assume you have added the the AWS Mobile SDK to your mobile app. To create a new cloud storage backend for your app, see :ref:`Add User Data Storage <add-aws-mobile-user-data-storage>`.


.. _how-to-transfer-utility-add-aws-user-data-storage-upload:

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

.. _how-to-transfer-utility-add-aws-user-data-storage-download:

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


.. _native-track-progress-and-completion-of-a-transfer:

Track Transfer Progress
=======================

.. container:: option

    Android-Java
        With the :code:`TransferUtility`, the download() and upload() methods return a :code:`TransferObserver` object. This object gives access to:

        #.  The state, as an :code:`enum`
        #.  The total bytes currently transferred
        #.  The total bytes remaining to transfer, to aid in calculating progress bars
        #.  A unique ID that you can use to keep track of distinct transfers

        Given the transfer ID, the :code:`TransferObserver` object can be retrieved from anywhere in your app, even if the app was terminated during a transfer. It also lets you create a :code:`TransferListener`, which will be updated on state or progress change, as well as when an error occurs.

        To get the progress of a transfer, call :code:`setTransferListener()` on your :code:`TransferObserver`. This requires you to implement :code:`onStateChanged`, :code:`onProgressChanged`, and :code:`onError`. For example:

        You can also query for :code:`TransferObservers` with either the :code:`getTransfersWithType(transferType)` or :code:`getTransfersWithTypeAndState(transferType, transferState)` method. You can use :code:`TransferObservers` to determine what transfers are underway, what are paused and handle the transfers as necessary.

        .. code-block:: java

            TransferObserver transferObserver = download(MY_BUCKET, OBJECT_KEY, MY_FILE);
            transferObserver.setTransferListener(new TransferListener(){

                @Override
                public void onStateChanged(int id, TransferState state) {
                    // do something
                }

                @Override
                public void onProgressChanged(int id, long bytesCurrent, long bytesTotal) {
                    int percentage = (int) (bytesCurrent/bytesTotal * 100);
                    //Display percentage transfered to user
                }

                @Override
                public void onError(int id, Exception ex) {
                    // do something
                }
            });

        The transfer ID can be retrieved from the :code:`TransferObserver` object that is returned from upload or download function.

        .. code-block:: java

            // Gets id of the transfer.
            int transferId = transferObserver.getId();

    iOS - Swift
        Implement progress and completion actions for transfers by passing a :code:`progressBlock` and :code:`completionHandler` blocks to the call to :code:`AWSS3TransferUtility` that initiates the transfer.

        The following example of initiating a data upload, shows how progress and completion handling is typically done for all transfers. The :code:`AWSS3TransferUtilityUploadExpression` and :code:`AWSS3TransferUtilityDownloadExpression` contains the :code:`progressBlock` that gives you the progress of the transfer which you can use to update the progress bar.

        .. code-block:: swift

            // For example, create a progress bar
            let progressView: UIProgressView! = UIProgressView()
            progressView.progress = 0.0;

            let data = Data() // The data to upload

            let expression = AWSS3TransferUtilityUploadExpression()
            expression.progressBlock = {(task, progress) in DispatchQueue.main.async(execute: {
                    // Update a progress bar.
                    progressView.progress = Float(progress.fractionCompleted)
                })
            }

            let completionHandler: AWSS3TransferUtilityUploadCompletionHandlerBlock = { (task, error) -> Void in DispatchQueue.main.async(execute: {
                    if let error = error {
                        NSLog("Failed with error: \(error)")
                    }
                    else if(self.progressView.progress != 1.0) {
                        NSLog("Error: Failed.")
                    } else {
                        NSLog("Success.")
                    }
                })
            }

            var refUploadTask: AWSS3TransferUtilityTask?
            let transferUtility = AWSS3TransferUtility.default()
            transferUtility.uploadData(data,
                       bucket: "S3BucketName",
                       key: "S3UploadKeyName",
                       contentType: "text/plain",
                       expression: expression,
                       completionHandler: completionHandler).continueWith { (task) -> AnyObject! in
                            if let error = task.error {
                                print("Error: \(error.localizedDescription)")
                            }

                            if let uploadTask = task.result {
                                // Do something with uploadTask.
                                // The uploadTask can be used to pause/resume/cancel the operation, retrieve task specific information
                                refUploadTask = uploadTask
                            }

                            return nil;
                        }

.. _native-pause-a-transfer:

Pause a Transfer
================

.. container:: option

    Android-Java
        Transfers can be paused using the :code:`pause(transferId)` method. If your app is terminated, crashes, or loses Internet connectivity, transfers are automatically paused.

        The :code:`transferId` can be retrieved from the :code:`TransferObserver` object as described in :ref:`native-track-progress-and-completion-of-a-transfer`.

        To pause a single transfer:

        .. code-block:: java

            transferUtility.pause(idOfTransferToBePaused);

        To pause all uploads:

        .. code-block:: java

            transferUtility.pauseAllWithType(TransferType.UPLOAD);

        To pause all downloads:

        .. code-block:: java

            transferUtility.pauseAllWithType(TransferType.DOWNLOAD);

        To pause all transfers of any type:

        .. code-block:: java

            transferUtility.pauseAllWithType(TransferType.ANY);

    iOS - Swift
        To pause or suspend a transfer, retain references to :code:`AWSS3TransferUtilityUploadTask` or :code:`AWSS3TransferUtilityDownloadTask` .

        As described in the previous section :ref:`native-track-progress-and-completion-of-a-transfer`, the variable :code:`refUploadTask` is a reference to the :code:`UploadTask` object that is retrieved from the :code:`continueWith` block of an upload operation that is invoked through :code:`transferUtiity.uploadData`.

        To pause a transfer, use the :code:`suspend` method:

        .. code-block:: swift

            refUploadTask.suspend()

.. _native-resume-a-transfer:

Resume a Transfer
=======================

.. container:: option

    Android-Java
        In the case of a loss in network connectivity, transfers will automatically resume when network connectivity is restored. If the app crashed or was terminated by the operating system, transfers can be resumed with the :code:`resume(transferId)` method.

        The :code:`transferId` can be retrieved from the :code:`TransferObserver` object as described in :ref:`native-track-progress-and-completion-of-a-transfer`.

        To resume a single transfer:

        .. code-block:: java

            transferUtility.resume(idOfTransferToBeResumed);

    iOS - Swift
        To resume an upload or a download operation, retain references to :code:`AWSS3TransferUtilityUploadTask` or :code:`AWSS3TransferUtilityDownloadTask`.

        As described in the previous section :ref:`native-track-progress-and-completion-of-a-transfer`, the variable :code:`refUploadTask` is a reference to the :code:`UploadTask` object that is retrieved from the :code:`continueWith` block of an upload operation that is invoked through :code:`transferUtiity.uploadData`.

        To resume a transfer, use the :code:`resume` method:

        .. code-block:: swift

            refUploadTask.resume()

.. _native-cancel-a-transfer:

Cancel a Transfer
=================

.. container:: option

    Android-Java
        To cancel an upload, call cancel() or cancelAllWithType() on the :code:`TransferUtility` object.

        The :code:`transferId` can be retrieved from the :code:`TransferObserver` object as described in :ref:`native-track-progress-and-completion-of-a-transfer`.

        To cancel a single transfer, use:

        .. code-block:: java

            transferUtility.cancel(idToBeCancelled);

        To cancel all transfers of a certain type, use:

        .. code-block:: java

            transferUtility.cancelAllWithType(TransferType.DOWNLOAD);

    iOS - Swift
        To cancel an upload or a download operation, retain references to :code:`AWSS3TransferUtilityUploadTask` (for upload oepration) and :code:`AWSS3TransferUtilityDownloadTask` (for download operation).

        As described in the previous section :ref:`native-track-progress-and-completion-of-a-transfer`, the variable :code:`refUploadTask` is a reference to the :code:`UploadTask` object that is retrieved from the :code:`continueWith` block of an upload operation that is invoked through :code:`transferUtiity.uploadData`.

        To cancel a transfer, use the :code:`cancel` method:

        .. code-block:: swift

           refUploadTask.cancel()


.. _native-background-transfers:

Background Transfers
====================

The SDK supports uploading to and downloading from Amazon S3 while your app is running in the background.

.. container:: option

    Android-Java
       No additional work is needed to use this feature. As long as your app is present in the background a transfer that is in progress will continue.

    iOS - Swift
        **Configure the Application Delegate**

        The :code:`TransferUtility` for iOS uses the iOS background transfer feature to continue data transfers even when your app moves to the background. Call the following method in the :code:`- application:handleEventsForBackgroundURLSession: completionHandler:` of your application delegate.
        When the app moves the foreground, the delegate enables iOS to notify TransferUtility that a transfer has completed.

        .. code-block:: swift

            func application(_ application: UIApplication, handleEventsForBackgroundURLSession identifier: String, completionHandler: @escaping () -> Void) {
                // Store the completion handler.
                AWSS3TransferUtility.interceptApplication(application, handleEventsForBackgroundURLSession: identifier, completionHandler: completionHandler)
            }

        **Manage a Transfer with the App in the Foreground**

        To manage transfers for an app that has moved from the background to the foregroud, retain references to :code:`AWSS3TransferUtilityUploadTask` and :code:`AWSS3TransferUtilityDownloadTask`. Call suspend, resume, or cancel methods on those task references. The following example shows how to suspend a transfer when the app is about to be terminated.

        .. code-block:: swift

            transferUtility.uploadFile(fileURL,
                    bucket: S3BucketName,
                    key: S3UploadKeyName,
                    contentType: "image/png",
                    expression: nil,
                    completionHandler: nil).continueWith {
                        (task) -> AnyObject! in if let error = task.error {
                            print("Error: \(error.localizedDescription)")
                        }

                        if let uploadTask = task.result {
                            uploadTask.suspend()
                        }

                        return nil;
                    }

        **Manage a Transfer when a Suspended App Returns to the Foreground**

        When an app that has initiated a transfer becomes suspended and then returns to the foreground, the transfer may still be in progress or may have completed. In both cases, use the following code to reestablish the progress and completion handler blocks of the app.

        This code example is for downloading a file but the same pattern can be used for upload:

        You can get a reference to the :code:`AWSS3TransferUtilityUploadTask` and :code:`AWSS3TransferUtilityDownloadTask` objects from the task.result in continueWith block when you initiate the upload and download respectively. These tasks have a property called taskIdentifier, which uniquely identifies the transfer task object within the :code:`AWSS3TransferUtility`. Your app should persist the identifier through closure and relaunch, so that you can uniquely identify the task objects when the app comes back into the foreground.

        .. code-block:: swift

            let transferUtility = AWSS3TransferUtility.default()

            var uploadProgressBlock: AWSS3TransferUtilityProgressBlock? = {(task: AWSS3TransferUtilityTask, progress: Progress) in
                DispatchQueue.main.async {
                    // Handle progress feedback, e.g. update progress bar
                }
            }
            var downloadProgressBlock: AWSS3TransferUtilityProgressBlock? = {
                (task: AWSS3TransferUtilityTask, progress: Progress) in DispatchQueue.main.async {
                    // Handle progress feedback, e.g. update progress bar
                }
            }
            var completionBlockUpload:AWSS3TransferUtilityUploadCompletionHandlerBlock? = {
                (task, error) in DispatchQueue.main.async {
                    // perform some action on completed upload operation
                }
            }
            var completionBlockDownload:AWSS3TransferUtilityDownloadCompletionHandlerBlock? = {
                (task, url, data, error) in DispatchQueue.main.async {
                    // perform some action on completed download operation
                }
            }

            transferUtility.enumerateToAssignBlocks(forUploadTask: {
                (task, progress, completion) -> Void in

                    let progressPointer = AutoreleasingUnsafeMutablePointer<AWSS3TransferUtilityProgressBlock?>(& uploadProgressBlock)

                    let completionPointer = AutoreleasingUnsafeMutablePointer<AWSS3TransferUtilityUploadCompletionHandlerBlock?>(&completionBlockUpload)

                    // Reassign your progress feedback
                    progress?.pointee = progressPointer.pointee

                    // Reassign your completion handler.
                    completion?.pointee = completionPointer.pointee

            }, downloadTask: {
                (task, progress, completion) -> Void in

                    let progressPointer = AutoreleasingUnsafeMutablePointer<AWSS3TransferUtilityProgressBlock?>(&downloadProgressBlock)

                    let completionPointer = AutoreleasingUnsafeMutablePointer<AWSS3TransferUtilityDownloadCompletionHandlerBlock?>(&completionBlockDownload)

                    // Reassign your progress feedback
                    progress?.pointee = progressPointer.pointee

                    // Reassign your completion handler.
                    completion?.pointee = completionPointer.pointee
            })

             if let downloadTask = task.result {
                // Do something with downloadTask.
            }


.. _native-advanced-transfers:

Advanced Transfer Methods
=========================

.. contents::
   :local:
   :depth: 1

.. _native-object-metadta:

Transfer with Object Metadata
-----------------------------

.. container:: option

    Android-Java
        To upload a file with metadata, use the :code:`ObjectMetadata` object. Create a :code:`ObjectMetadata` object and add in the metadata headers and pass it to the upload function.

        .. code-block:: java

            import com.amazonaws.services.s3.model.ObjectMetadata;

            ObjectMetadata myObjectMetadata = new ObjectMetadata();

            //create a map to store user metadata
            Map<String, String> userMetadata = new HashMap<String,String>();
            userMetadata.put("myKey","myVal");

            //call setUserMetadata on our ObjectMetadata object, passing it our map
            myObjectMetadata.setUserMetadata(userMetadata);

        Then, upload an object along with its metadata:

        .. code-block:: java

            TransferObserver observer = transferUtility.upload(
              MY_BUCKET,        /* The bucket to upload to */
              OBJECT_KEY,       /* The key for the uploaded object */
              MY_FILE,          /* The file where the data to upload exists */
              myObjectMetadata  /* The ObjectMetadata associated with the object*/
            );

        To download the meta, use the S3 :code:`getObjectMetadata` method. For more information, see the `API Reference <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3Client.html#getObjectMetadata%28com.amazonaws.services.s3.model.GetObjectMetadataRequest%29>`__.

    iOS - Swift
        :code:`AWSS3TransferUtilityUploadExpression` contains the method `setValue:forRequestHeader <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSS3TransferUtilityExpression.html#//api/name/setValue:forRequestParameter:>`__ where you can pass in metadata to Amazon S3.
        This example demonstrates passing in the Server-side Encryption Algorithm as a request header in uploading data to S3.

        .. code-block:: swift

            let data: Data = Data() // The data to upload

            let uploadExpression = AWSS3TransferUtilityUploadExpression()
            uploadExpression.setValue("AES256", forRequestHeader: "x-amz-server-side-encryption-customer-algorithm")
            uploadExpression.progressBlock = {(task, progress) in DispatchQueue.main.async(execute: {
                    // Do something e.g. Update a progress bar.
                })
            }

            let transferUtility = AWSS3TransferUtility.default()

            transferUtility.uploadData(data,
                        bucket: "S3BucketName",
                        key: "S3UploadKeyName",
                        contentType: "text/plain",
                        expression: uploadExpression,
                        completionHandler: nil).continueWith { (task) -> AnyObject! in
                            if let error = task.error {
                                print("Error: \(error.localizedDescription)")
                            }

                            return nil;
                        }

.. _native-access-control-list:

Transfer with Access Control List
---------------------------------

.. container:: option

    Android-Java
        To upload a file with Access Control List, use the :code:`CannedAccessControlList` object. The `CannedAccessControlList <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/services/s3/model/CannedAccessControlList.html>`__ specifies the constants defining a canned access control list. For example, if you use `CannedAccessControlList.PublicRead <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/services/s3/model/CannedAccessControlList.html#PublicRead>`__ , this specifies the owner is granted :code:`Permission.FullControl` and the :code:`GroupGrantee.AllUsers` group grantee is granted Permission.Read access.

        Then, upload an object along with its ACL:

        .. code-block:: java

            TransferObserver observer = transferUtility.upload(
              MY_BUCKET,                          /* The bucket to upload to */
              OBJECT_KEY,                         /* The key for the uploaded object */
              MY_FILE,                            /* The file where the data to upload exists */
              CannedAccessControlList.PublicRead  /* Specify PublicRead ACL for the object in the bucket. */
            );

    iOS - Swift
        To upload a file and specify permissions for it, you can use predefined grants, also known as canned ACLs. The following code shows you how to setup a file with publicRead access using the AWSS3 client.


        .. code-block:: swift

            //Create a AWSS3PutObjectRequest object and setup the content, bucketname, key on it.
            //use the .acl method to specify the ACL for the file
            let s3: AWSS3 = AWSS3.default()

            let putObjectRequest: AWSS3PutObjectRequest! = AWSS3PutObjectRequest()
            let content = "testObjectData"
            putObjectRequest.acl = AWSS3ObjectCannedACL.publicRead
            putObjectRequest.bucket = "bucket name"
            putObjectRequest.key = "file name"
            putObjectRequest.body = content
            putObjectRequest.contentLength = content.count as NSNumber
            putObjectRequest.contentType = "text/plain";

            s3.putObject(putObjectRequest, completionHandler: { (putObjectOutput:AWSS3PutObjectOutput? , error: Error? ) in
                if let output = putObjectOutput {
                    print (output)
                }

                if let error = error {
                    print (error)
                }
            })


.. _native-more-transfer-examples:

More Transfer Examples
======================

.. contents::
   :local:
   :depth: 1

This section provides descriptions and abbreviated examples of the aspects of each type of transfer that are unique. For information about typical code surrounding the following snippets see :ref:`native-track-progress-and-completion-of-a-transfer`.

Downloading to a File
---------------------

The following code shows how to download an |S3| Object to a local file.

.. container:: option

    Android-Java
        .. code-block:: java

            TransferObserver downloadObserver =
                transferUtility.download(
                      "s3Folder/s3Key.txt",
                      new File("/path/to/file/localFile.txt"));

            downloadObserver.setTransferListener(new TransferListener() {

                 @Override
                 public void onStateChanged(int id, TransferState state) {
                    if (TransferState.COMPLETED == state) {
                       // Handle a completed download.
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

    iOS-Swift
        .. code-block:: swift

            let fileURL = // The file URL of the download destination.

            let transferUtility = AWSS3TransferUtility.default()
            transferUtility.download(
                    to: fileURL
                    bucket: S3BucketName,
                    key: S3DownloadKeyName,
                    expression: expression,
                    completionHandler: completionHandler).continueWith {
                        (task) -> AnyObject! in if let error = task.error {
                            print("Error: \(error.localizedDescription)")
                        }

                        if let _ = task.result {
                            // Do something with downloadTask.
                        }
                        return nil;
                    }

Uploading Binary Data to a File
-------------------------------

.. container:: option

    Android-Java
        Use the following code to upload binary data to a file in |S3|.

        .. code-block:: java

            TransferObserver uploadObserver =
                    transferUtility.upload(
                          "s3Folder/s3Key.bin",
                          new File("/path/to/file/localFile.bin"));

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

    iOS-Swift
        To upload a binary data to a file, you have to make sure to set the appropriate content type in the uploadData method of the TransferUtility. In the example below, we are uploading a PNG image to S3.

        .. code-block:: swift

            let data: Data = Data() // The data to upload

            let transferUtility = AWSS3TransferUtility.default()
            transferUtility.uploadData(data,
                        bucket: S3BucketName,
                        key: S3UploadKeyName,
                        contentType: "image/png",
                        expression: expression,
                        completionHandler: completionHandler).continueWith { (task) -> AnyObject! in
                            if let error = task.error {
                                print("Error: \(error.localizedDescription)")
                            }

                            if let _ = task.result {
                                // Do something with uploadTask.
                            }

                            return nil;
                        }

Downloading Binary Data to a File
---------------------------------

The following code shows how to download a binary file.

.. container:: option

    Android-Java
        .. code-block:: java

            TransferObserver downloadObserver =
                transferUtility.download(
                      "s3Folder/s3Key.bin",
                      new File("/path/to/file/localFile.bin"));

            downloadObserver.setTransferListener(new TransferListener() {

                 @Override
                 public void onStateChanged(int id, TransferState state) {
                    if (TransferState.COMPLETED == state) {
                       // Handle a completed download.
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

    iOS-Swift
        .. code-block:: swift

            let fileURL = // The file URL of the download destination
            let transferUtility = AWSS3TransferUtility.default()
            transferUtility.downloadData(
                    fromBucket: S3BucketName,
                    key: S3DownloadKeyName,
                    expression: expression,
                    completionHandler: completionHandler).continueWith {
                        (task) -> AnyObject! in if let error = task.error {
                            print("Error: \(error.localizedDescription)")
                        }

                        if let _ = task.result {
                            // Do something with downloadTask.
                        }

                        return nil;
                    }

Limitations
===========

.. container:: option

    Android-Java
        If you expect your app to perform transfers that take longer than 50 minutes, use `AmazonS3Client <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3Client.html>`__ instead of `TransferUtility <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobileconnectors/s3/transferutility/TransferUtility.html>`__.

        :code:`TransferUtility` generates Amazon S3 pre-signed URLs to use for background data transfer. Using |COG| Identity, you receive AWS temporary credentials. The credentials are valid for up to 60 minutes. Generated |S3| pre-signed URLs cannot last longer than that time. Because of this limitation, the Amazon S3 Transfer Utility enforces 50 minute transfer timeouts, leaving a 10 minute buffer before AWS temporary credentials are regenerated. After **50 minutes**, you receive a transfer failure.

    iOS-Swift
        If you expect your app to perform transfers that take longer than 50 minutes, use `AWSS3 <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSS3.html>`__ instead of `AWSS3TransferUtility <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSS3TransferUtility.html>`__.

        :code:`AWSS3TransferUtility` generates Amazon S3 pre-signed URLs to use for background data transfer. Using Amazon Cognito Identity, you receive AWS temporary credentials. The credentials are valid for up to 60 minutes. At the same time, generated S3 pre-signed URLs cannot last longer than that time. Because of this limitation, the AWSS3TransferUtility enforces **50 minutes** transfer timeout, leaving a 10 minute buffer before AWS temporary credentials are regenerated. After 50 minutes, you receive a transfer failure.
