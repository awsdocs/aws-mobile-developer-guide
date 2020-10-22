# Manually Exported Project Components<a name="project-import-export-manual"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

This section describes how to manually add project components to an exported project definition\.

**Topics**
+ [Importing User File Storage Contents](#import-export-user-data-storage-contents)
+ [Importing Hosting and Streaming Contents](#import-export-hosting-and-streaming-contents)
+ [Importing SAML Federated User Sign\-in](#import-export-saml)
+ [Importing API Handlers for Cloud Logic APIs](#import-export-cloud-logic)
+ [Importing Cross\-Origin Resource Sharing \(CORS\) Configuration](#import-export-cors)

## Importing User File Storage Contents<a name="import-export-user-data-storage-contents"></a>

When a project that enables User File Storage is exported, files stored in its Amazon S3 bucket are not included in its exported project definition\. You can manually configure the project definition to upload those files to the new bucket of the imported project\.

 **To configure import and upload of project files stored in a User File Storage bucket** 

1. Uncompress your exported project `.zip` file\.

1. Copy and paste each file that you want uploaded during import into the unzipped file folder\.

1. Add file paths to your exported project definition:

   1. Open the `mobile-hub-project.yml` file of the export in an editor\.

   1. If not already present, create an `uploads:` node at the root level\.

   1. For each file to be uploaded, add the following three items under `uploads:`\.

      1. The namespace `- !com.amazonaws.mobilehub.v0.Upload` 

      1. The key `fileName:` with the value of the path to the file within the project definition `.zip` file\.

      1. The key `targetS3Bucket:` with the value of `user-files`\.

         ```
         --- !com.amazonaws.mobilehub.v0.Project
         features:
           sign-in: !com.amazonaws.mobilehub.v0.SignIn {}
           user-files: !com.amazonaws.mobilehub.v0.UserFiles
             attributes:
               enabled: true
           user-profiles: !com.amazonaws.mobilehub.v0.UserSettings
             attributes:
               enabled: true
         name: userfiles
         region: us-east-1
         uploads:
           - !com.amazonaws.mobilehub.v0.Upload
             fileName: {example1.png}
             targetS3Bucket: user-files
           - !com.amazonaws.mobilehub.v0.Upload
             fileName: {example2.xml}
             targetS3Bucket: user-files
         . . .
         ```

1. Rezip the files within the uncompressed project definition file \(not the folder containing those files, because that causes a path error\)\.

## Importing Hosting and Streaming Contents<a name="import-export-hosting-and-streaming-contents"></a>

When a project that enables Hosting and Streaming is exported, files stored in its Amazon S3 bucket are not included in the exported project definition\. You can manually configure the project definition to upload those files to the new bucket of the imported project\.

 **To configure import and upload of project files stored in a Hosting and Streaming bucket** 

1. Uncompress your exported project `.zip` file\.

1. Copy and paste each file that you want uploaded during import into the unzipped file folder\.

1. Add file paths to your exported project definition:

   1. Open the `mobile-hub-project.yml` file of the export in an editor\.

   1. If not already present, create an `uploads:` node at the root level\.

   1. For each file to be uploaded, add the following three items under `uploads:`\.

      1. The namespace `- !com.amazonaws.mobilehub.v0.Upload` 

      1. The key `fileName:` with the value of the path to the file within the project definition `.zip` file\.

      1. The key `targetS3Bucket:` with the value of `hosting`\.

         ```
         --- !com.amazonaws.mobilehub.v0.Project
         features:
           content-delivery: !com.amazonaws.mobilehub.v0.ContentDelivery
             attributes:
               enabled: true
               visibility: public-global
             components:
               release: !com.amazonaws.mobilehub.v0.Bucket {}
         
         . . .
         
         uploads:
           - !com.amazonaws.mobilehub.v0.Upload
             fileName: {example1.html}
             targetS3Bucket: hosting
           - !com.amazonaws.mobilehub.v0.Upload
             fileName: {example2.js}
             targetS3Bucket: hosting
         . . .
         ```

1. Rezip the files within the uncompressed project definition file \(not the folder containing those files, because that causes a path error\)\.

## Importing SAML Federated User Sign\-in<a name="import-export-saml"></a>

Configuring SAML federation for the Mobile Hub User Sign\-in feature requires you to supply the SAML XML configuration \(`saml.xml`\) of the identity provider you federate\. The SAML XML configuration is not included in the `.zip` file exported by Mobile Hub\.

 **To configure an exported project to deploy the original project’s SAML federation when it is imported** 

1. Uncompress your exported project `.zip` file\.

1. Copy your identity provider’s `saml.xml` file into the root folder of the uncompressed `.zip` file\.

1. Rezip the files within the uncompressed project definition file \(not the folder containing those files, because that causes a path error\)\.

## Importing API Handlers for Cloud Logic APIs<a name="import-export-cloud-logic"></a>

The Mobile Hub Cloud Logic feature pairs a RESTful API surface \(API Gateway\) with serverless API handler functions \(Lambda\)\. While Mobile Hub supports exporting and importing the definitions of API and handler objects that Cloud Logic configures, the API handler function code is not exported\.

Mobile Hub enables you to manually configure your project export `.zip` file to deploy your API handler function code as part of the project import when the following conditions are met:
+ Your API handler accesses only DynamoDB tables\. Import of API handlers that access other AWS services, such as Amazon S3, is not currently supported\.
+ Your handler code is factored to use [Lambda environmental variables](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-env_cli.html) to refer to those DynamoDB tables\.

  When Mobile Hub imports API handler code, it uses environmental variables to map data operations to the new tables created by the import\. You can define the key name of environmental variables in the project’s definition YAML to match constant names you define in the project’s Lambda API handler function code\. The following example shows a Lambda function constant being equated to an environmental variable\.

  ```
  const YOUR-FUNCTION-CONSTANT-NAME = process.env.KEY-NAME-DEFINED-IN-YAML;";
  
  // example
  const MENU_TABLE_NAME = process.env.MENU_TABLE_NAME;
  ```

  The steps that follow these notes describe how to define your environmental variables in project definition YAML\.
**Note**  
An alternative is to use the `MOBILE_HUB_DYNAMIC_PREFIX` project identifier prefix that Mobile Hub generates\. Mobile Hub configures its value to be the unique identifier for the imported project\. When you append a valid table name to that prefix in your function code, it composes a valid identifier for the table in the imported project\. The following example shows a Lambda function constant being equated to an environmental variable\.  

  ```
  const YOUR-FUNCTION-CONSTANT-NAME = process.env.MOBILE_HUB_DYNAMIC_PREFIX + "-YOUR-TABLE-NAME";
  
  // example
  const MENU_TABLE_NAME = process.env.MOBILE_HUB_DYNAMIC_PREFIX + "-bbq-menu";
  ```
This method does not require additional manual configuration of the project definition YAML\.

The [AWS Mobile React sample app](https://github.com/awslabs/aws-mobile-react-sample) provides an end to end example of using environmental variables to access data tables through an API and its handler\. Take the following steps for each API handler whose code you want to import\. Examples from the sample app are given in line\.

 **To enable import of \|LAM\| handler functions for your exported Cloud Logic API** 

1. Uncompress your exported project `.zip` file\.

1. Copy your Lambda function\(s\) into the uncompressed file\.

   1. Go to the [Amazon S3 console](https://console.aws.amazon.com/s3/) and search for your Mobile Hub project name\.

   1. Choose the bucket with the name containing `-deployments-`, then choose the `uploads` folder\.

   1. Copy and save the name\(s\) of the Lambda function file\(s\) in the folder for use in following steps\.

   1. Copy the Lambda function file\(s\) in the folder into your unzipped exported project file\.

1. Add file paths to your exported project definition\.

   1. Open the `mobile-hub-project.yml` file of the export in an editor\.

   1. If not already present, create an `uploads:` node at the root level\.

   1. For each file to be uploaded, add the following three items under `uploads:`\.

      1. The namespace `- !com.amazonaws.mobilehub.v0.Upload` 

      1. The key `fileName:` with the value of the path to the file within the project definition `.zip` file\.

      1. The key `targetS3Bucket:` with the value of `deployments`\.

   1. If not already present in each Cloud Logic `. . . paths: items` node, create a `codeFilename:` key with the value of the path of the Lambda function code file for that handler\.
**Note**  
The path in this case is relative to the root of the `-deployments-`Amazon S3 bucket Mobile Hub provisioned for Cloud Logic\. Typically, Mobile Hub places these files in an `/uploads` folder\.  
If no `codeFilename` is specified, then Mobile Hub deploys a default handler that echos requests it receives\.

   1. Add environmental variables to your exported project definition\.

      For each Cloud Logic `. . . paths: items` node that describes a handler that interacts with a DynamoDB table, add an `environment:` node with child members that are composed by concatenating an environmental variable name, with the string `__DYNAMIC_PREFIX__`, and the associated table name\. The variable name should map to the associated variable in your Lambda API handler function code\.

      ```
      --- !com.amazonaws.mobilehub.v0.Project
      features:
        cloudlogic: !com.amazonaws.mobilehub.v0.CloudLogic
          components:
            api-name: !com.amazonaws.mobilehub.v0.API
              attributes:
                name: api-name
                requires-signin: true
                sdk-generation-stage-name: Development
              paths:
                /items: !com.amazonaws.mobilehub.v0.Function
                  codeFilename: {uploads/lambda-archive.zip}
                  description: "Handler for calls to resource path : /items"
                  enableCORS: true
                  handler: lambda.handler
                  memorySize: "128"
                  name: handler-name
                  runtime: nodejs6.10
                  timeout: "3"
                  environment:
                    {MENU_TABLE_NAME}: ___DYNAMIC_PREFIX___{-bbq_menu_item}
                    {ORDERS_TABLE_NAME}: ___DYNAMIC_PREFIX___{-bbq_orders}
                    {RESTAURANTS_TABLE_NAME}: ___DYNAMIC_PREFIX___-{bbq_restaurants}
                "/items/{proxy+}": !com.amazonaws.mobilehub.v0.Function
                  codeFilename: {uploads/lambda-archive.zip}
                  description: "Handler for calls to resource path : /items/{proxy+}"
                  enableCORS: true
                  handler: lambda.handler
                  memorySize: "128"
                  name: handler-name
                  runtime: nodejs6.10
                  timeout: "3"
                  environment:
                    {MENU_TABLE_NAME}: ___DYNAMIC_PREFIX___{-bbq_menu_item}
                    {ORDERS_TABLE_NAME}: ___DYNAMIC_PREFIX___{-bbq_orders}
                    {RESTAURANTS_TABLE_NAME}: ___DYNAMIC_PREFIX___-{bbq_restaurants}
      . . .
      
      uploads:
        - !com.amazonaws.mobilehub.v0.Upload
          fileName: {lambda-archive.zip}
          targetS3Bucket: deployments
        - !com.amazonaws.mobilehub.v0.Upload
          fileName: {lambda.jar}
          targetS3Bucket: deployments
      . . .
      ```

1. Save the `.yml` file and rezip the files within the uncompressed project definition file \(not the folder containing those files, because that causes a path error\)\.

1. Test your revised project export definition by importing it through the Mobile Hub console\. You can verify your environmental variables through the Lambda console\.

**Note**  
By default, the Mobile Hub NoSQL Database feature configures a table’s permissions to grant read and write access for Lambda functions\. The kind of custom IAM policy configuration required to change the table’s permissions is not included in the export of a project\. An importer of a project dependent on custom policy needs enough information to recreate the policy once they have imported the project\. For such a case, we recommend you provide both your policy JSON and step by step instructions \(console or AWS CLI\) on how and where to attach it\. For more information on those steps, see [Authentication and Access Control for Amazon DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/authentication-and-access-control.html)\.

## Importing Cross\-Origin Resource Sharing \(CORS\) Configuration<a name="import-export-cors"></a>

By default, AWS security infrastructure prevents calls to an API Gateway API from a browser\. Configuring CORS for each path of your API securely enables your API calls over the web\. CORS configuration is not included in Mobile Hub project export\. The following steps describe how to manually include import of CORS configuration in your project export file\.

 **To include CORS configuration for your \|ABP\| API paths** 

1. Unzip your exported project definition `.zip` file\.

1. Open the export’s `mobile-hub-project.yml` file in an editor\.

1. For each API path, add a key named `enableCORS` with the value `true` under `... paths: "/items/. . .": !com.amazonaws.mobilehub.v0.Function`, as shown in the following fragment\.

   ```
   --- !com.amazonaws.mobilehub.v0.Project
       features:
         cloudlogic: !com.amazonaws.mobilehub.v0.CloudLogic
           components:
             ReactSample: !com.amazonaws.mobilehub.v0.API
               attributes:
                 name: ReactSample
                 requires-signin: false
               paths:
                 "/items/{proxy+}": !com.amazonaws.mobilehub.v0.Function
                   name: FirstHandler
                   handler: lambda.handler
                   enableCORS: true
                   runtime: nodejs6.10
                   . . .
   ```

1. Rezip the files within the uncompressed project definition file \(not the folder containing those files, because that causes a path error\)\.