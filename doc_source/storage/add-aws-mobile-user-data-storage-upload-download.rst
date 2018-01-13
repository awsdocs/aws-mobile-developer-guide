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
