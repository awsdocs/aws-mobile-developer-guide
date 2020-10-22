# Amazon CloudFront Security Considerations for Mobile Hub Users<a name="reference-cloudfront-security"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

When you enable the AWS Mobile Hub [Hosting and Streaming](hosting-and-streaming.md) feature, an [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) distribution is created in your account\. The distribution caches the web assets you store within an associated Amazon S3 bucket throughout a global network of Amazon edge servers\. This provides your customers with fast local access to the web assets\.

This topic describes the key CloudFront security\-related features that you might want to use for your distribution\. For the same type of information regarding the source bucket, see s3\-security\.

## Access management<a name="cloudfront-security-access"></a>

Hosting and Streaming makes assets in a distribution publically available\. While this is the normal security policy for Internet based resources, you should consider restricting access to the assets if this is not the case\. The best practice for security is to follow a ?minimal permissions? model and restrict access to resources as much as possible\. You may want to modify resource\-based policies, such as the distribution policy or access control lists \(ACLs\), to grant access only to some users or groups of users\.

To protect access to any AWS resources associated with a Hosting and Streaming web app, such as buckets and database tables, we recommend restricting access to only authenticated users\. You can add this restriction to your Mobile Hub project by enabling the [User Sign\-in](User-Sign-in.md#user-sign-in) feature, with the sign\-in required option\.

For more information, see [Authentication and Access Control for CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/auth-and-access-control.html) in the *Amazon CloudFront Developer Guide*\.

## Requiring the HTTPS Protocol<a name="cloudfront-security-https"></a>

CloudFront supports use of the HTTPS protocol to encrypt communications to and from a distribution\. This highly recommended practice protects both the user and the service\. CloudFront enables you to require HTTPS both between customers and your distribution endpoints, and CloudFront between your distribution’s caches and the source bucket where your assets originate\. Global redirection of HTTP traffic to HTTPS, use of HTTPS for custom domains and other options are also supported\.

For more information, see [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) in the *Amazon CloudFront Developer Guide*\.

## Securing Private Content<a name="cloudfront-security-private"></a>

CloudFront supports a range of methods for protecting private content in a distribution cache\. These include the use of signed cookies and signed URLs to restrict access to authenticated, authorized users\.

A best practice is to use techniques like these on both the connection between the user and the distribution endpoint and between the distribution and the content Amazon S3 source bucket\.

For more information, see the [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) section in the *Amazon CloudFront Developer Guide*\.

## Distribution Access Logging<a name="cloudfront-security-logging"></a>

Distribution logging helps you learn more about your app users, helps you meet your organization’s audit requirements, and helps you understand your CloudFront costs\. Each access log record provides details about a single access request, such as the requester, distribution name, request time, request action, response status, and error code, if any\. You can store logs in an Amazon S3 bucket\. To help manage your costs, you can delete logs that you no longer need, or you can suspend logging\.

For more information, see [Access Logs for CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide*\.