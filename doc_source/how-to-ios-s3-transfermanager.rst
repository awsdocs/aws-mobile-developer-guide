.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _s3transfermanager:

######################################
iOS: Amazon S3 TransferManager for iOS
######################################

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-user-data-storage>` to install the SDK and integrate Amazon S3.

*Or, use the contents of this page if your app will integrate existing AWS services.*



.. contents::
   :local:
   :depth: 1

:guilabel:`Amazon Simple Storage Service (S3)`

`Amazon Simple Storage Service (S3) <http://aws.amazon.com/s3/>`_ provides secure,
durable, highly-scalable object storage in the cloud. Using the AWS Mobile SDK for iOS, you can
directly access Amazon S3 from your mobile app. For information about Amazon S3 regional availability,
see  `AWS Service Region Availability <http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`_.

:guilabel:`TransferManager Features`

Amazon S3 TransferManager class makes it easy   to upload files to and download files from Amazon S3
while optimizing for performance and reliability. It hides the complexity of transferring
files behind a simple API.

Whenever possible, uploads are broken into multiple pieces, so that several pieces are sent in
parallel to provide better throughput. This approach enables more robust transfers, since an I/O error
in an individual piece result in the SDK retransmitting only the faulty piece, not the
entire transfer. ``TransferManager`` provides simple APIs to pause, resume, and cancel file transfers.

The following sections provide a step-by-step guide for getting started with Amazon S3 using the ``TransferManager``.

You can also try out the
`Amazon S3 sample <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferManager-Sample>`_ available in the AWSLabs GitHub repository.

.. admonition:: Should I Use ``TransferManager`` or ``TransferUtility``?

    To choose which API best suits your needs, see :ref:`manager-or-utility`.


Setup
-----

To set your project up to use the ``TransferManager`` class, take the steps below.

1. Setup the SDK, Credentials and Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Follow the steps in `How to Integrate Your Existing Bucket <https://docs.aws.amazon.com/aws-mobile/latest/developerguide/how-to-integrate-an-existing-bucket.html`_ to install the AWS Mobile SDK for iOS and configure
    AWS credentials and permissions.

2. Import the SDK Amazon S3 APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Add the following import statements to your Xcode project.

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    import AWSS3


            iOS - Objective-C
                .. code-block:: objc

                    #import <AWSS3/AWSS3.h>

3. Create the ``TransferManager`` Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Add the following code to create an `AWSS3TransferManager` client.

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    let transferManager = AWSS3TransferManager.default()


            iOS - Objective-C
                .. code-block:: objc

                    AWSS3TransferManager *transferManager = [AWSS3TransferManager defaultS3TransferManager];

    The `AWSS3TransferManager` class is an entry point to this SDK's high-level Amazon S3 APIs.

Transfer an Object
~~~~~~~~~~~~~~~~~~

In this section:

.. contents::
   :local:
   :depth: 1

Downloading a file from and uploading a file to a bucket, use the same coding pattern. An important
difference is that `download:` does not succeed until the download is complete, blocking any flow that
depends on that success. Upload returns immediately and can therefore be safely called on the
main thread.

The steps to call ``TransferManager`` for a transfer are as follows.

1. Create an ``AWSS3TransferManagerDownloadRequest``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The following code illustrates the three actions needed to create a download request:

        - Create a destination/source location for the file. In this example, this is
          called ``downloadingFileURL`` / ``uploadingFileURL``.

        - Construct a request object using ``AWSS3TransferManagerDownloadRequest``.

        - Set three properties of the request object: the bucket name; the key (the name of
          the object in the bucket); and the download destination / upload source
          ``downloadingFileURL`` / ``uploadingFileURL``.

        :guilabel:`Download`

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    let downloadingFileURL = URL(fileURLWithPath: NSTemporaryDirectory()).appendingPathComponent("myImage.jpg")

                    let downloadRequest = AWSS3TransferManagerDownloadRequest()

                    downloadRequest.bucket = "myBucket"
                    downloadRequest.key = "myImage.jpg"
                    downloadRequest.downloadingFileURL = downloadingFileURL


            iOS - Objective-C
                .. code-block:: objc

                    NSString *downloadingFilePath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"myImage.jpg"];
                    NSURL *downloadingFileURL = [NSURL fileURLWithPath:downloadingFilePath];

                    AWSS3TransferManagerDownloadRequest *downloadRequest = [AWSS3TransferManagerDownloadRequest new];

                    downloadRequest.bucket = @"myBucket";
                    downloadRequest.key = @"myImage.jpg";
                    downloadRequest.downloadingFileURL = downloadingFileURL;


        :guilabel:`Upload`

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    let uploadingFileURL = URL(fileURLWithPath: "your/file/path/myTestFile.txt")

                    let uploadRequest = AWSS3TransferManagerUploadRequest()

                    uploadRequest.bucket = "myBucket"
                    uploadRequest.key = "myTestFile.txt"
                    uploadRequest.body = uploadingFileURL


            iOS - Objective-C
                .. code-block:: objc

                    NSURL *uploadingFileURL = [NSURL fileURLWithPath: @"your/file/path/myTestFile.txt"];

                    AWSS3TransferManagerUploadRequest *uploadRequest = [AWSS3TransferManagerUploadRequest new];

                    uploadRequest.bucket = @"myBucket";
                    uploadRequest.key = @"myTestFile.txt";
                    uploadRequest.body = uploadingFileURL;


2. Pass the Request to the `download:` Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Use the following code to pass the request to the `download:` / `upload:" method of the
    ``TransferManager`` client. The methods are asynchronous and returns an `AWSTask` object. Use a
    `continueWith` block to handle the method result.  For more information about `AWSTask`,
    see :ref:`Working with Asynchronous Tasks <aws-aysnchronous-tasks-for-ios>`.

        :guilabel:`Download`

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    transferManager.download(downloadRequest).continueWith(executor: AWSExecutor.mainThread(), block: { (task:AWSTask<AnyObject>) -> Any? in

                        if let error = task.error as? NSError {
                            if error.domain == AWSS3TransferManagerErrorDomain, let code = AWSS3TransferManagerErrorType(rawValue: error.code) {
                                switch code {
                                case .cancelled, .paused:
                                    break
                                default:
                                    print("Error downloading: \(downloadRequest.key) Error: \(error)")
                                }
                            } else {
                                print("Error downloading: \(downloadRequest.key) Error: \(error)")
                            }
                            return nil
                        }
                        print("Download complete for: \(downloadRequest.key)")
                        let downloadOutput = task.result
                        return nil
                    })


            iOS - Objective-C
                .. code-block:: objc

                    [[transferManager download:downloadRequest ] continueWithExecutor:[AWSExecutor mainThreadExecutor]
                        withBlock:^id(AWSTask *task) {
                        if (task.error){
                            if ([task.error.domain isEqualToString:AWSS3TransferManagerErrorDomain]) {
                                switch (task.error.code) {
                                    case AWSS3TransferManagerErrorCancelled:
                                    case AWSS3TransferManagerErrorPaused:
                                    break;

                                    default:
                                        NSLog(@"Error: %@", task.error);
                                        break;
                                }

                            } else {
                                NSLog(@"Error: %@", task.error);
                            }
                        }

                        if (task.result) {
                            AWSS3TransferManagerDownloadOutput *downloadOutput = task.result;
                        }
                        return nil;
                    }];

        :guilabel:`Upload`

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    transferManager.upload(uploadRequest).continueWith(executor: AWSExecutor.mainThread(), block: { (task:AWSTask<AnyObject>) -> Any? in

                        if let error = task.error as? NSError {
                            if error.domain == AWSS3TransferManagerErrorDomain, let code = AWSS3TransferManagerErrorType(rawValue: error.code) {
                                switch code {
                                case .cancelled, .paused:
                                    break
                                default:
                                    print("Error uploading: \(uploadRequest.key) Error: \(error)")
                                }
                            } else {
                                print("Error uploading: \(uploadRequest.key) Error: \(error)")
                            }
                            return nil
                        }

                        let uploadOutput = task.result
                        print("Upload complete for: \(uploadRequest.key)")
                        return nil
                    })


            iOS - Objective-C
                .. code-block:: objc

                    [[transferManager upload:uploadRequest] continueWithExecutor:[AWSExecutor mainThreadExecutor]
                                withBlock:^id(AWSTask *task) {
                    if (task.error) {
                        if ([task.error.domain isEqualToString:AWSS3TransferManagerErrorDomain]) {
                            switch (task.error.code) {
                                case AWSS3TransferManagerErrorCancelled:
                                case AWSS3TransferManagerErrorPaused:
                                    break;

                                default:
                                    NSLog(@"Error: %@", task.error);
                                    break;
                            }
                        } else {
                            // Unknown error.
                            NSLog(@"Error: %@", task.error);
                        }
                    }

                    if (task.result) {
                        AWSS3TransferManagerUploadOutput *uploadOutput = task.result;
                        // The file uploaded successfully.
                    }
                    return nil;
                }];



3. Displaying a Downloaded Image in an UIImageView
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The use of `download:` in this example is executed on the main thread. The following code illustrates
    displaying such an image in a `UIImageView` configured in your project .

    Note that it can only succeed after download of the file it displays has completed.

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    self.imageView.image = UIImage(contentsOfFile: downloadingFileURL.path)


            iOS - Objective-C
                .. code-block:: objc

                    self.imageView.image = [UIImage imageWithContentsOfFile:downloadingFilePath];



Pause, Resume, and Cancel Object Transfers
------------------------------------------

In this section:

.. contents::
   :local:
   :depth: 1

The ``TransferManager`` supports pause, resume, and cancel operations for both
uploads and downloads. The `pause`, `cancel`, `resumeAll`, `cancelAll`, `pauseAll`,
`upload:`, and `download:` operations all return instances of `AWSTask`. Use these methods with a
`continueWith` `block:` to handle the returns of these operations.

Use continueWith Block to Handle Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code illustrates using `continueWith` `block:` when calling the `pause` method.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                uploadRequest.pause().continueWith(block: { (task:AWSTask<AnyObject>) -> Any? in
                    if let error = task.error as? NSError {
                        print("Error: \(error)")
                        return nil
                    }

                    // Upload has been paused.
                    return nil
                })


        iOS - Objective-C
            .. code-block:: objc

                [[self.uploadRequest pause] continueWithBlock:^id(AWSTask *task) {
                    if (task.error) {
                        NSLog(@"Error: %@",task.error);
                    } else {

                    }

                    // Upload has been paused.
                    return nil;
                }];

For brevity, the following examples omit the `continueWithBlock`.

Pause a Transfer
~~~~~~~~~~~~~~~~

To pause an object transfer, call `pause` on the request object.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                uploadRequest.pause()
                downloadRequest.pause()


        iOS - Objective-C
            .. code-block:: objc

                [uploadRequest pause];
                [downloadRequest pause];

Resume a Transfer
~~~~~~~~~~~~~~~~~

To resume a transfer, call `upload` or `download` and pass in
the paused request object.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                transferManager.upload(uploadRequest)
                transferManager.download(downloadRequest)

        iOS - Objective-C
            .. code-block:: objc

                [transferManager upload:uploadRequest];
                [transferManager download:downloadRequest];

Cancel a Transfer
~~~~~~~~~~~~~~~~~

To cancel a transfer, call `cancel` on the upload or download request.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                uploadRequest.cancel()
                downloadRequest.cancel()


        iOS - Objective-C
            .. code-block:: objc

                [uploadRequest cancel];
                [downloadRequest cancel];

Pause All Transfers
~~~~~~~~~~~~~~~~~~~

To pause all of the current upload and download requests, call `pauseAll` on the ``TransferManager``.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                transferManager.pauseAll()

        iOS - Objective-C
            .. code-block:: objc

                [transferManager pauseAll];

Resume All Transfers
~~~~~~~~~~~~~~~~~~~~

To resume all of the current upload and download requests, call `resumeAll` on the ``TransferManager``
passing an `AWSS3``TransferManager``ResumeAllBlock`, which is a closure that takes `AWSRequest` as a parameter, and
can be used to reset the progress blocks for the requests.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                transferManager.resumeAll({ (request:AWSRequest?) in
                   // All paused requests have resumed.
                })


        iOS - Objective-C
            .. code-block:: objc

                [transferManager resumeAll:^(AWSRequest *request) {
                    // All paused requests have resumed.
                }];

Cancel All Transfers
~~~~~~~~~~~~~~~~~~~~

To cancel all upload and download requests, call `cancelAll` on the TransferManager.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                transferManager.cancelAll()

        iOS - Objective-C
            .. code-block:: objc

                [transferManager cancelAll];

Track Progress
--------------

Using the `uploadProgress` and `downloadProgress` blocks, you can track the progress of
object transfers. These blocks work in conjunction with the Grand Central Dispatch `dispatch_async` function,
as shown in the following examples.

Upload Progress
~~~~~~~~~~~~~~~

    Track the progress of an upload.

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                        uploadRequest.uploadProgress = {(bytesSent: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64) -> Void in
                            DispatchQueue.main.async(execute: {() -> Void in
                                //Update progress
                            })
                        }

            iOS - Objective-C
                .. code-block:: objc

                    uploadRequest.uploadProgress =  ^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend){
                        dispatch_async(dispatch_get_main_queue(), ^{
                         //Update progress
                    });

Download Progress
~~~~~~~~~~~~~~~~~

    Track the progress of a download.

        .. container:: option

            iOS - Swift
                .. code-block:: swift

                    downloadRequest.downloadProgress = {(bytesSent: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64) -> Void in
                        DispatchQueue.main.async(execute: {() -> Void in
                            //Update progress
                        })
                    }

            iOS - Objective-C
                .. code-block:: objc

                    downloadRequest.downloadProgress = ^(int64_t bytesWritten, int64_t totalBytesWritten, int64_t totalBytesExpectedToWrite){
                    dispatch_async(dispatch_get_main_queue(), ^{
                            //Update progress
                    });

Multipart Upload
----------------

Amazon S3 provides a multipart upload feature to upload a single object as a set of parts.
Each part is a contiguous portion of the object's data. The object parts are uploaded
independently and in any order. If transmission of any part fails, you can retransmit that part
without affecting other parts. After all parts of the object are uploaded, Amazon S3 assembles
these parts and creates the object.

In the AWS Mobile SDK for iOS, the ``TransferManager`` handles multipart upload for you. The
minimum part size for a multipart upload is 5MB.

Additional Resources
--------------------

* `Amazon Simple Storage Service Getting Started Guide <http://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html>`_
* `Amazon Simple Storage Service API Reference <http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html>`_
* `Amazon Simple Storage Service Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html>`_

.. _Identity and Access Management Console: https://console.aws.amazon.com/iam/home
.. _Granting Access to an Amazon S3 Bucket: http://blogs.aws.amazon.com/security/post/Tx3VRSWZ6B3SHAV/Writing-IAM-Policies-How-to-grant-access-to-an-Amazon-S3-bucket
