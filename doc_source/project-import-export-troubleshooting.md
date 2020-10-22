# Mobile Hub Project Troubleshooting<a name="project-import-export-troubleshooting"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

The following sections describe issues you might encounter when setting up, importing or exporting Mobile Hub projects, and their remedies\.

**Topics**
+ [Cannot Import an API](#import-export-troubleshooting-imported-api)
+ [Cannot Import a NoSQL Table](#import-export-troubleshooting-nosql)
+ [Cannot Import Multiple NoSQL Tables](#import-export-troubleshooting-nosql-maximum)
+ [Cannot Import Push Credentials](#import-export-troubleshooting-push-credentials)
+ [Build Artifacts Can’t be Found](#build-artifacts-can-t-be-found)
+ [Unable to Configure S3 Bucket During](#import-export-troubleshooting-s3-configuration)
+ [Administrator Required Error During Setup](#import-export-troubleshooting-adminstrator-required)
+ [Account Setup Incomplete](#import-export-troubleshooting-incomplete-setup)
+ [File Too Large to Import](#import-export-troubleshooting-file-size)

## Cannot Import an API<a name="import-export-troubleshooting-imported-api"></a>

Error Message
+  `Project owner does not own existing API : arn:aws:execute-api:us-east-1:012345678901:abcdefghij.` 

   *\(where the API identifier arn:aws:execute\-api:us\-east\-1:012345678901:abcdefghij is specific to the project being imported\)* 

Description
+ This message means that the API with the ID shown cannot be imported because it does not exist in the current AWS account\. This occurs when the APIs in the original project were created outside of the Mobile Hub Cloud Logic feature and then imported\.

Remedy
+  **To remedy this condition, take the following steps\.** 

  1. Modify the YAML of the project definition you are importing by removing the sections under the `features:components` node that begin with the name of an API that was imported into the original project’s Cloud Logic feature\.

  1. Save and import the project definition\.

  1. Enable the Mobile Hub Cloud Logic feature in your imported project and recreate the API and its handler\.

## Cannot Import a NoSQL Table<a name="import-export-troubleshooting-nosql"></a>

Error Message
+ There is already an existing DynamoDB table called ‘someprojectname\-mobilehub\-012345678\-TableName’ in your account\. Please choose a different name or remove the existing table and retry your request\.

   *\(where the table name someprojectname\-mobilehub\-012345678\-TableName is specific to the project being imported\)* 

Description
+ This message occurs when you import a project containing the NoSQL Database Feature\. It indicates that the Amazon DynamoDB table in the project configuration already exists\. This can occur when a YAML tablename value was edited in the project definition file and there is more than one attempt to import it into the same account\.

Remedy
+  **To remedy this condition, take the following steps** 

  1. Modify any tablename values to remove the conflict\.

  1. Save and import the project definition\.

  1. Adjust the code of the imported app where it references the old tablename value\.

## Cannot Import Multiple NoSQL Tables<a name="import-export-troubleshooting-nosql-maximum"></a>

Error Message
+ Project file\(s\) cannot be decoded\. They may contain data that was encrypted by a different account\. Failed to decode push feature\. Failed to decode credential attribute\.

Description
+ This message occurs when you import Push Notifications messaging service credentials or Amazon SNS topic identifiers for features that are not associated with your AWS account\.

Remedy
+  **To remedy this condition, take the following steps** 

  1. Modify the YAML of the project definition you are importing by removing table definition sections\.

  1. Save and import the project definition\.

  1. Use the table definitions you removed to manually create those tables using the Mobile Hub NoSQL Database feature\.

## Cannot Import Push Credentials<a name="import-export-troubleshooting-push-credentials"></a>

Error Message
+ Project file\(s\) cannot be decoded\. They may contain data that was encrypted by a different account\. Failed to decode push feature\. Failed to decode credential attribute\.

Description
+ This message occurs when you import Push Notifications messaging service credentials or Amazon SNS topic identifiers for features that are not associated with your AWS account\.

Remedy
+  **To remedy this condition, take the following steps** 

  1. Modify the YAML of the project definition you are importing by removing the push: node\.

  1. Save and import the project definition\.

  1. Enable the Mobile Hub Push Notifications or User Engagement feature using your own messaging service credentials and topics\.

## Build Artifacts Can’t be Found<a name="build-artifacts-can-t-be-found"></a>

Error Message
+ Unable to find build artifact uploads/exported\-project\-definition\.zip in Amazon S3 bucket archive\-deployments\-mobilehub\-0123456789 for project\-name\.

   where exported\-project\-definition, the numerical portion of the Amazon S3 bucket identifier, and the project\-name are specific to the project being imported\) 

Description
+ This message occurs when a project import fails because Mobile Hub can’t find the file of a Cloud Logic API handler function \(Lambda\) that is specified in the \.yml project definition file\.

Remedy
+  **To remedy this condition, take the following steps** 

  The remedy for this condition is to make the location of the Lambda file\(s\) match the path specified in the project definition YAML\.

  The error occurs if, for any reason, the path described in the codeFilename: key in the YAML does not match the actual location of the Lambda function file relative to the root of the `...-deployments-...` Amazon S3 bucket that Mobile Hub deploys when Cloud Logic is enabled\.

## Unable to Configure S3 Bucket During<a name="import-export-troubleshooting-s3-configuration"></a>

Error Message
+ It looks like there was a problem creating or configuring your S3 bucket\.

Description
+ Mobile Hub was unable to create a S3 bucket for your project’s deployment artifacts during Mobile Hub project import\.

Remedy
+  **To remedy this condition, try the following steps** 

  Check that you are not at maximum bucket capacity using the [Amazon S3 console](https://console.aws.amazon.com/s3/)\.

## Administrator Required Error During Setup<a name="import-export-troubleshooting-adminstrator-required"></a>

Error Message
+ It looks like you do not have permission for this operation\.

Description
+ The user does not have permission to create the required Mobile Hub Service Role during configuration of a Mobile Hub project\.

Remedy
+  **To remedy this condition, try the following steps** 

  Contact an administrator for your AWS account and ask them to create the service role at the following location: [https://console\.aws\.amazon\.com/mobilehub/home\#/activaterole/](https://console.aws.amazon.com/mobilehub/home#/activaterole/)\.

## Account Setup Incomplete<a name="import-export-troubleshooting-incomplete-setup"></a>

Error Message
+ It looks like your AWS account is not fully set up\.

Description
+ This error can occur for a range of reasons during Mobile Hub project configuration\.

Remedy
+  **To remedy this condition, try the following steps** 
  + Sign out of the AWS console and lose down all browser windows\. Then try to log in to the [AWS Management Console](https://console.aws.amazon.com/mobilehub) and attempt the operation that initially caused the error\.
  + If the issue persists, post to the [Forum: Moblie Development ](http://forums.aws.amazon.com/88) for support\.

## File Too Large to Import<a name="import-export-troubleshooting-file-size"></a>

Error Message
+ The project file is too large\. The max file size is 10 MB\.

Description
+ This message occurs when you attempt to import a project definition file that is larger than 10MB\.

Remedy
+ Reduce the size of the project export file\. Project exporters may want to deliver large file payloads outside of their project definition files, along with providing instructions for importers about how to use AWS consoles to incorporate those accompanying files\.