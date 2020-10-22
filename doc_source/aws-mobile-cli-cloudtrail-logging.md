# Logging AWS Mobile CLI API Calls with AWS CloudTrail<a name="aws-mobile-cli-cloudtrail-logging"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

The AWS Mobile CLI is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in the CLI\. CloudTrail captures all API calls for the CLI as events, including calls from code calls to the CLI APIs\. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for the CLI\. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**\. Using the information collected by CloudTrail, you can determine the request that was made to the CLI, the IP address from which the request was made, who made the request, when it was made, and additional details\.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)\.

## AWS Mobile CLI Information in CloudTrail<a name="aws-mobile-cli-information-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account\. When activity occurs in AWS Mobile CLI, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**\. You can view, search, and download recent events in your AWS account\. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)\.

For an ongoing record of events in your AWS account, including events for AWS Mobile CLI, create a trail\. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket\. By default, when you create a trail in the console, the trail applies to all regions\. The trail logs events from all regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify\. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs\. For more information, see:
+  [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations) 
+  [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

All AWS Mobile CLI actions are logged by CloudTrail and are documented in the [AWS Mobile CLI API Reference](aws-mobile-cli-reference.md)\. For example, calls to the `awsmobile init`, `awsmobile pull` and `awsmobile push` generate entries in the CloudTrail log files\.

Every event or log entry contains information about who generated the request\. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management \(IAM\) user credentials\.
+ Whether the request was made with temporary security credentials for a role or federated user\.
+ Whether the request was made by another AWS service\.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

## Understanding AWS Mobile ClI Log File Entries<a name="understanding-your-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify\. CloudTrail log files contain one or more log entries\. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on\. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order\.

The following example shows a CloudTrail log entry that demonstrates the `ListProjects` action\.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "ABCDEFGHIJK0123456789",
        "arn": "arn:aws:iam::012345678901:user/Administrator",
        "accountId": "012345678901",
        "accessKeyId": "ABCDEFGHIJK0123456789",
        "userName": "YOUR_ADMIN_USER_NAME"
    },
    "eventTime": "2017-12-18T23:10:13Z",
    "eventSource": "mobilehub.amazonaws.com",
    "eventName": "ListProjects",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "111.111.111.111",
    "userAgent": "aws-cli/1.11.140 Python/2.7.13 Darwin/15.6.0 botocore/1.6.7 ",
    "requestParameters": {
        "maxResults": 0
    },
    "responseElements": {
        "projects": [{
            "name": "YOUR_PROJECT_NAME-0123456789012",
            "projectId": "abcd0123-0123-0123-0123-abcdef012345"
        }]
    },
    "requestID": "abcd0123-0123-0123-0123-abcdef012345",
    "eventID": "abcd0123-0123-0123-0123-abcdef012345",
    "eventType": "AwsApiCall",
    "recipientAccountId": "012345678901"
}
```