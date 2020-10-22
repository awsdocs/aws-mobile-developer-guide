# Exporting and Importing AWS Mobile Hub Projects<a name="project-import-export"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

## Overview<a name="import-export-overview"></a>

Mobile Hub provides the ability to export and import YAML files that describe the configuration of your Mobile Hub project\. Anyone with an AWS account can import an exported project configuration file to deploy a new project, with new AWS resources that match the configuration being imported\.

This feature enables you to replicate the AWS service configuration of an exported project\. While the data in a project’s tables is not exported, files in storage or hosting buckets and API handler function code can be manually added to your exported project definition\. To learn more, see import\-export\-manual\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/diagram-abstract-import-export.png)

 **To export a project configuration file** 

1. Navigate to your project list in the Mobile Hub console\.

1. Hover over the ellipses \(three dots\) in the upper right of the project card\.

1. Choose **Export \(file\)** in the upper right of the card for the project you want to export\.

1. Save your project export file\.

To learn more about the content of an exported project configuration file, see [Structure of a Project Export \.yml File](project-import-export-yaml.md#project-import-export-yaml-details)\.

 **To import a project** 

1. Navigate to your project list in the Mobile Hub console\.

1. Choose **Import your project** in the upper left of the page\.

1. Browse or drag a project definition file into the **Import project configuration** dialog\.

1. Choose **Import project**\.

## Sharing Your Project Configuration with a Deploy to AWS Mobile Hub Link<a name="import-export-deploy-links"></a>

In any public GitHub repo, you can provide a link that instantly kicks off creation of a new Mobile Hub project by importing the exported project configuration file define in the link’s querystring\. The form of the link should be:

 `https://console.aws.amazon.com/mobilehub/home?#/?config=YOUR-MOBILE-HUB-PROJECT-CONFIGURATION-LOCATION` 

For example, the following HTML creates a link that provides instant configuration of an app’s AWS backend services, based on Mobile Hub features defined in `react-sample.zip`\. To see this code in action, see `README.md` for the [AWS Mobile React Sample](https://github.com/awslabs/aws-mobile-react-sample)\.

```
<p align="center">
   <a target="_blank" href="https://console.aws.amazon.com/mobilehub/home?#/?config=https://github.com/awslabs/aws-mobile-react-sample/blob/master/backend/import_mobilehub/react-sample.zip">
   <span>
       <img height="100%" src="https://s3.amazonaws.com/deploytomh/button-deploy-aws-mh.png"/>
   </span>
   </a>
</p>
```

The querystring portion of the link can point to the location of a Mobile Hub project configuration `mobile-hub-project.yml` file or a project export `.zip` file containing a `mobile-hub-project.yml` file\.

**Important**  
If you are using a `.zip` file it must conform to the structure and content required by a Mobile Hub project configuration import\. For details, see [Structure of a Project Export \.zip File](project-import-export-yaml.md#project-import-export-zip)\.

## Limitations of Importing Projects<a name="import-export-limitations"></a>

**Topics**
+ [Maximum Project Definition File Size is 10MB](#import-export-limitations-file-size)
+ [Project Components that Require Manual Export](#import-export-limitations-manual-mods)
+ [Cross Account Credentials](#import-export-limitations-manual-credentials)
+ [Project Components that Are Not Exported](#import-export-limitations-manual-unsupported)

### Maximum Project Definition File Size is 10MB<a name="import-export-limitations-file-size"></a>

Import of Mobile Hub project `.zip` or `.yml` files larger than 10MB is not supported\.

### Project Components that Require Manual Export<a name="import-export-limitations-manual-mods"></a>

To enable import of the following project configuration items, you must manually modify your project’s exported `.zip` file:
+ Data User Storage Contents

  To import files stored in a User File Storage Amazon S3 bucket in your original project, see [Importing User File Storage Contents](project-import-export-manual.md#import-export-user-data-storage-contents)\.
+ Hosting and Streaming Contents

  To import files hosted in a Hosting and Streaming bucket in your original project, see [Importing Hosting and Streaming Contents](project-import-export-manual.md#import-export-hosting-and-streaming-contents)\.
+ SAML Federation

  To import User Sign\-in SAML federation configuration from your original project, see [Importing SAML Federated User Sign\-in](project-import-export-manual.md#import-export-saml)\.
+ Cloud Logic API Handlers

  To import Cloud Logic API handler code and configuration from your original project, see [Importing API Handlers for Cloud Logic APIs](project-import-export-manual.md#import-export-cloud-logic)\.
**Note**  
Calling Cloud Logic APIs from a browser requires that Cross\-Origin Resource Sharing \(CORS\) is configured for each API path\. To enable CORS configuration when your project is imported, see [Importing Cross\-Origin Resource Sharing \(CORS\) Configuration](project-import-export-manual.md#import-export-cors)\.

### Cross Account Credentials<a name="import-export-limitations-manual-credentials"></a>

Some features require credentials and assets that are associated with the AWS account where they are configured\. Mobile Hub projects that contain such features can only be imported into the account that exported them\. Features with this restriction include Cloud Logic APIs that were created outside of the Mobile Hub project being exported, messaging provider credentials for Push Notification, and Amazon SNS topics\.


|  **Mobile Hub Feature**  |  **Can be exported from one AWS account and imported into another?**  | 
| --- | --- | 
|   **User Sign\-in**   |  Yes  | 
|   **NoSQL Database**   |  Yes  | 
|   **Cloud Logic**   |   Using APIs created within your Mobile Hub project:  Yes  Using APIs imported into your project:  No \(for remedy, see [Cannot Import an API](project-import-export-troubleshooting.md#import-export-troubleshooting-imported-api)\)  | 
|   **User File Storage**   |  Yes  | 
|   **App Content Delivery**   |  Yes  | 
|   **Connectors**   |  Yes  | 
|   **Push Notifications**   |  No \(for remedy, see [Cannot Import Push Credentials](project-import-export-troubleshooting.md#import-export-troubleshooting-push-credentials)\)  | 
|   **Messaging and Analytics** \(Push Notification\)  |  No \(for remedy, see [Cannot Import Push Credentials](project-import-export-troubleshooting.md#import-export-troubleshooting-push-credentials)\)  | 

### Project Components that Are Not Exported<a name="import-export-limitations-manual-unsupported"></a>

The following items are not supported by the Mobile Hub import/export feature:
+ Custom policy

  When you enable a Mobile Hub feature, a set of AWS services is deployed\. Mobile Hub attaches default access roles and policies to these objects\. When a project is imported, the default roles and policies are applied\.

  In your original project, you can modify or add to these defaults; for example, to set access to a data table to read only\. When you export your project configuration, any such customizations are not included in the project export\. To enable your custom policy in an imported project, the importer must manually configure those policies in the imported project\. In addition to your project export file, we recommend you provide both your policy JSON and step by step instructions for importers\. These instructions should describe how to use AWS consoles or the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/) to implement your customizations\.
+ Legacy Cloud Logic

  Import and export are not supported for projects using the legacy Cloud Logic feature\. A project of this kind calls Lambda functions directly\. The current version of Cloud Logic makes RESTful calls to Amazon API Gateway APIs linked to Lambda function handlers\.