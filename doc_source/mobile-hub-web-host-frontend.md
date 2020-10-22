# Host Your Web App<a name="mobile-hub-web-host-frontend"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

**Topics**
+ [About Hosting and Streaming](#about-hosting-and-streaming)
+ [Managing Your App Assets](#manage-app-assets)
+ [Configure a Custom Domain for Your Web App](#configure-a-custom-domain-for-your-web-app)

## About Hosting and Streaming<a name="about-hosting-and-streaming"></a>

The first time that you push your web app to the cloud, the Hosting and Streaming feature is enabled to statically host your app on the web\. Using the AWS Mobile CLI, this happens when you first run:

```
$ awsmobile publish
```

A container for your content is created using an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/) bucket\. The content is available publicly on the Internet and you can preview the content directly using a testing URL\.

Content placed in your bucket is automatically distributed to a global content delivery network \(CDN\)\. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) implements the CDN which can host your app on an endpoint close to every user, globally\. These endpoints can also stream media content\. To learn more, see [CloudFront Streaming Tutorials](https://docs.aws.amazon.com/mobile-hub/latest/developerguide/url-cf-dev;Tutorials.html)\.

By default, Hosting and Streaming deploys a simple sample web app that accesses AWS services\.

## Managing Your App Assets<a name="manage-app-assets"></a>

You can use the AWS Mobile CLI or the Amazon S3 console to manage the content of your bucket\.

### Use the AWS CLI to Manage Your Bucket Contents<a name="manage-app-assets-use-cli"></a>

AWS CLI allows you to review, upload, move or delete your files stored in your bucket using the command line\. To install and configure the AWS CLI client, see [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)\.

As an example, the sync command enables transfer of files to and from your local folder \(`source`\) and your bucket \(`destination`\)\.

```
$ aws s3 sync {source destination} [--options]
```

The following command syncs all files from your current local folder to the folder in your web app’s bucket defined by `path`\.

```
```

$ aws s3 sync \. s3://AWSDOC\-EXAMPLE\-BUCKET/path

To learn more about using AWS CLI to manage Amazon S3, see [Using Amazon S3 with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-s3.html) 

### Use the Amazon S3 Console to Manage Your Bucket<a name="manage-app-assets-use-s3-console"></a>

To use the Amazon S3 console to review, upload, move or delete your files stored in your bucket, use the following steps\.

1. From the root of your project, run:

   ```
   awsmobile console
   ```

1. Choose the tile with the name of your project, then choose the Hosting and Streaming tile\.

1. Choose the link labelled **Manage files** to display the contents of your bucket in the Amazon S3 console\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/hosting-and-streaming-manage-files-link.png)

### Other Useful Functions in the AWS Mobile Hub Console<a name="other-useful-functions-in-the-aws-mobile-hub-console"></a>

The Mobile Hub console also provides convenient ways to browse to your web content, return to the AWS CLI content on this page, and other relevant tasks\. These include:
+ The **View from S3** link browses to the web contents of your bucket\. When Hosting and Streaming is enabled, the bucket is populated with the files for a default web app files that is viewable immediately\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/hosting-and-streaming-view-s3-link.png)
+ The **View from CloudFront** browses to the web contents that have propagated from your bucket to CDN\. The endpoint propagation is dependent on network conditions\. You can expect your content to be distributed and viewable within one hour\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/hosting-and-streaming-view-cloudfront-link.png)
+ The **Sync files with the command line** link takes you to content on this page that describes how to use the command line to manage the web app and streaming media files in your bucket\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/hosting-and-streaming-cli-sync-files-link.png)

## Configure a Custom Domain for Your Web App<a name="configure-a-custom-domain-for-your-web-app"></a>

To use your custom domain for linking to your Web app, use the Route 53 service to configure DNS routing\.

For a web app hosted in a single location, see [Routing Traffic to a Website that Is Hosted in an Amazon S3 Bucket](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html)\.

For a web app distributed through a global CDN, see [Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloud-fron-distribution.html) 