.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _s3-pre-signed-urls:

Amazon S3 Pre-Signed URLs: For Background Transfer
##################################################

If you are working with large file transfers, you
may want to perform uploads and downloads in the background. To do this, you need to create a
background session using ``NSURLSession`` and then transfer your objects using pre-signed URLs.

The following sections describe pre-signed S3 URLs. To learn more about ``NSURLSession``, see
`Using NSURLSession <https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/URLLoadingSystem/Articles/UsingNSURLSession.html>`_.

Pre-Signed URLs
---------------
By default, all Amazon S3 resources are private. If you want your users to have access to Amazon S3 buckets
or objects, you can assign appropriate permissions with an `IAM policy <http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html>`_.

Alternatively, you can use pre-signed URLs to give your users access to Amazon S3 objects. A pre-signed URL
provides access to an object without requiring AWS security credentials or permissions.

When you create a pre-signed URL, you must provide your security credentials, specify a bucket name,
an object key, an HTTP method, and an expiration date and time. The pre-signed URL is valid only for the specified duration.

Build a Pre-Signed URL
----------------------

The following example shows how to build a pre-signed URL for an Amazon S3 download in the background.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                AWSS3PreSignedURLBuilder.default().getPreSignedURL(getPreSignedURLRequest).continueWith { (task:AWSTask<NSURL>) -> Any? in
                    if let error = task.error as? NSError {
                        print("Error: \(error)")
                        return nil
                    }

                    let presignedURL = task.result
                    print("Download presignedURL is: \(presignedURL)")

                    let request = URLRequest(url: presignedURL as! URL)
                    let downloadTask: URLSessionDownloadTask = URLSession.shared.downloadTask(with: request)
                    downloadTask.resume()

                    return nil
                }

        iOS - Objective-C
            .. code-block:: objc

                AWSS3GetPreSignedURLRequest *getPreSignedURLRequest = [AWSS3GetPreSignedURLRequest new];
                getPreSignedURLRequest.bucket = @"myBucket";
                getPreSignedURLRequest.key = @"myImage.jpg";
                getPreSignedURLRequest.HTTPMethod = AWSHTTPMethodGET;
                getPreSignedURLRequest.expires = [NSDate dateWithTimeIntervalSinceNow:3600];

                [[[AWSS3PreSignedURLBuilder defaultS3PreSignedURLBuilder] getPreSignedURL:getPreSignedURLRequest]
                    continueWithBlock:^id(AWSTask *task) {

                    if (task.error) {
                        NSLog(@"Error: %@",task.error);
                    } else {

                        NSURL *presignedURL = task.result;
                        NSLog(@"download presignedURL is: \n%@", presignedURL);

                        NSURLRequest *request = [NSURLRequest requestWithURL:presignedURL];
                        self.downloadTask = [self.session downloadTaskWithRequest:request];
                        //downloadTask is an instance of NSURLSessionDownloadTask.
                        //session is an instance of NSURLSession.
                        [self.downloadTask resume];

                    }
                    return nil;
                }];

The preceding example uses ``GET`` as the HTTP method: ``AWSHTTPMethodGET``. For an upload request to Amazon S3,
we would need to use a PUT method and also specify a content type.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                getPreSignedURLRequest.httpMethod = .PUT
                let fileContentTypeStr = "text/plain"
                getPreSignedURLRequest.contentType = fileContentTypeStr


        iOS - Objective-C
            .. code-block:: objc

                getPreSignedURLRequest.HTTPMethod = AWSHTTPMethodPUT;
                NSString *fileContentTypeStr = @"text/plain";
                getPreSignedURLRequest.contentType = fileContentTypeStr;

Here's an example of building a pre-signed URL for a background upload to S3.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let getPreSignedURLRequest = AWSS3GetPreSignedURLRequest()
                getPreSignedURLRequest.bucket = "myBucket"
                getPreSignedURLRequest.key = "myFile.txt"
                getPreSignedURLRequest.httpMethod = .PUT
                getPreSignedURLRequest.expires = Date(timeIntervalSinceNow: 3600)

                //Important: set contentType for a PUT request.
                let fileContentTypeStr = "text/plain"
                getPreSignedURLRequest.contentType = fileContentTypeStr

                AWSS3PreSignedURLBuilder.default().getPreSignedURL(getPreSignedURLRequest).continueWith { (task:AWSTask<NSURL>) -> Any? in
                    if let error = task.error as? NSError {
                        print("Error: \(error)")
                        return nil
                    }

                    let presignedURL = task.result
                    print("Download presignedURL is: \(presignedURL)")

                    var request = URLRequest(url: presignedURL as! URL)
                    request.cachePolicy = .reloadIgnoringLocalCacheData
                    request.httpMethod = "PUT"
                    request.setValue(fileContentTypeStr, forHTTPHeaderField: "Content-Type")

                    let uploadTask: URLSessionTask = URLSession.shared.uploadTask(with: request, fromFile: URL(fileURLWithPath: "your/file/path/myFile.txt"))
                    uploadTask.resume()

                    return nil
                }


        iOS - Objective-C
            .. code-block:: objc

                AWSS3GetPreSignedURLRequest *getPreSignedURLRequest = [AWSS3GetPreSignedURLRequest new];
                getPreSignedURLRequest.bucket = @"myBucket";
                getPreSignedURLRequest.key = @"myFile";
                getPreSignedURLRequest.HTTPMethod = AWSHTTPMethodPUT;
                getPreSignedURLRequest.expires = [NSDate dateWithTimeIntervalSinceNow:3600];

                //Important: set contentType for a PUT request.
                NSString *fileContentTypeStr = @"text/plain";
                getPreSignedURLRequest.contentType = fileContentTypeStr;

                [[[AWSS3PreSignedURLBuilder defaultS3PreSignedURLBuilder] getPreSignedURL:getPreSignedURLRequest]
                                                                continueWithBlock:^id(AWSTask *task) {
                    if (task.error) {
                        NSLog(@"Error: %@",task.error);
                    } else {
                        NSURL *presignedURL = task.result;
                        NSLog(@"upload presignedURL is: \n%@", presignedURL);

                        NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:presignedURL];
                        request.cachePolicy = NSURLRequestReloadIgnoringLocalCacheData;
                        [request setHTTPMethod:@"PUT"];
                        [request setValue:fileContentTypeStr forHTTPHeaderField:@"Content-Type"];

                        self.uploadTask = [self.session uploadTaskWithRequest:request fromFile:self.uploadFileURL];
                        //uploadTask is an instance of NSURLSessionDownloadTask.
                        //session is an instance of NSURLSession.
                        [self.uploadTask resume];
                    }
                    return nil;
                }];


Additional Resources
====================

* `Amazon Simple Storage Service Getting Started Guide <http://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html>`_
* `Amazon Simple Storage Service API Reference <http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html>`_
* `Amazon Simple Storage Service Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html>`_

.. _Identity and Access Management Console: https://console.aws.amazon.com/iam/home
.. _Granting Access to an Amazon S3 Bucket: http://blogs.aws.amazon.com/security/post/Tx3VRSWZ6B3SHAV/Writing-IAM-Policies-How-to-grant-access-to-an-Amazon-S3-bucket
