# Mobile Hub Project Export Format<a name="project-import-export-yaml"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

AWS Mobile Hub provides the ability to export a YAML file containing the configuration of your project\. The YAML file itself can be imported or it can be included in a `.zip` file with other project components that get deployed during project import\. This section describes the anatomy of the YAML and a typical Mobile Hub project export `.zip` file\. For more information about the Mobile Hub Import/Export feature, see [Exporting and Importing AWS Mobile Hub Projects](project-import-export.md)\.

**Topics**
+ [Structure of a Project Export \.zip File](#project-import-export-zip)
+ [Structure of a Project Export \.yml File](#project-import-export-yaml-details)

## Structure of a Project Export \.zip File<a name="project-import-export-zip"></a>

When you choose **Export \(file\)**, Mobile Hub generates a `.zip` file named for your project\.

Default file structure

Mobile Hub also generates a `mobile-hub-project.yml` project configuration file in the `.zip` root\. A valid `mobile-hub-project.yml` file in this location is required for Mobile Hub project import to succeed\.

Example file structure

File structure of the `.zip` file an exported project, configured to include deployment of both SAML federation and Cloud Logic API handlers, is as follows:
+  ` /your-project-name.zip` 
  +  `mobile-hub-project.yml` 
  +  `saml.xml` 
  +  `lambda API handler functions` 
  +  `user data stored files` 
  +  `hosted files` 

Files in a project export `.zip` file can be arranged in folders\. The relative paths within the archive must be reflected in the project definition YAML key values that refer to their paths\.

**Note**  
The presence of any files or folders in the project configuration `.zip` file, other than those described in the preceding section, may be ignored or cause issues upon import\.

## Structure of a Project Export \.yml File<a name="project-import-export-yaml-details"></a>

In the abstract, the basic structure of a Mobile Hub project export `.yml` file is as follows:

```
features:
    FEATURE-TYPE: !com.amazonaws.mobilehub.v0.:FEATURE-TYPE
          components:
            FEATURE-NAME: !com.amazonaws.mobilehub.v0.FEATURE-TYPE
                attributes:
                    ATTRIBUTE-NAME: !com.amazonaws.mobilehub.v0.ATTRIBUTE-VALUE
                OTHER-FEATURE-PROPERTY-TYPES: OTHER-FEATURE-PROPERTY-VALUES
            . . .
```

The following YAML is a sample of the `mobile-hub-project.yml` exported from a project with many Mobile Hub features enabled\. The project definition has also been manually updated to enable the import and upload of components of the original project\. These components include files stored in the original project’s User File Storage bucket, files hosted in its Hosting and Streaming bucket, and API handler code in its Lambda functions\.

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
            codeFilename: uploads/lambda-archive.zip
            description: "Handler for calls to resource path : /items"
            enableCORS: true
            handler: lambda.handler
            memorySize: "128"
            name: handler-name
            runtime: nodejs6.10
            timeout: "3"
          "/items/{proxy+}": !com.amazonaws.mobilehub.v0.Function
            codeFilename: uploads/lambda-archive.zip
            description: "Handler for calls to resource path : /items/{proxy+}"
            enableCORS: true
            handler: lambda.handler
            memorySize: "128"
            name: handler-name
            runtime: nodejs6.10
            timeout: "3"
  content-delivery: !com.amazonaws.mobilehub.v0.ContentDelivery
    attributes:
      enabled: true
      visibility: public-global
    components:
      release: !com.amazonaws.mobilehub.v0.Bucket {}
  database: !com.amazonaws.mobilehub.v0.Database
    components:
      database-nosql: !com.amazonaws.mobilehub.v0.NoSQLDatabase
        tables:
          - !com.amazonaws.mobilehub.v0.NoSQLTable
            attributes:
            id: S
            hashKeyName: id
            hashKeyType: S
            rangeKeyName: ""
            rangeKeyType: ""
            tableName: ___DYNAMIC_PREFIX___-bbq-order
            tablePrivacy: public
          - !com.amazonaws.mobilehub.v0.NoSQLTable
            attributes:
            id: S
            hashKeyName: id
            hashKeyType: S
            rangeKeyName: ""
            rangeKeyType: ""
            tableName: ___DYNAMIC_PREFIX___-bbq_restaurants
            tablePrivacy: public
          - !com.amazonaws.mobilehub.v0.NoSQLTable
            attributes:
            id: S
            restaurant_id: S
            hashKeyName: restaurant_id
            hashKeyType: S
            rangeKeyName: id
            rangeKeyType: S
            tableName: ___DYNAMIC_PREFIX___-bbq_menu_item
            tablePrivacy: public
  sign-in: !com.amazonaws.mobilehub.v0.SignIn
    attributes:
      enabled: true
      optional-sign-in: false
    components:
      sign-in-user-pools: !com.amazonaws.mobilehub.v0.UserPoolsIdentityProvider
        attributes:
          alias-attributes:
            - email
            - phone_number
          mfa-configuration: ON
          name: userpool
          password-policy: !com.amazonaws.mobilehub.ConvertibleMap
            min-length: "8"
            require-lower-case: true
            require-numbers: true
            require-symbols: true
            require-upper-case: true
  user-files: !com.amazonaws.mobilehub.v0.UserFiles
    attributes:
      enabled: true
  user-profiles: !com.amazonaws.mobilehub.v0.UserSettings
    attributes:
      enabled: truename: myProject
region: us-east-1
uploads:
    - !com.amazonaws.mobilehub.v0.Upload
      fileName: stored-file
      targetS3Bucket: user-file.png
    - !com.amazonaws.mobilehub.v0.Upload
      fileName: hosted-file
      targetS3Bucket: hosting.html
    - !com.amazonaws.mobilehub.v0.Upload
      fileName: api-handler-file.zip
      targetS3Bucket: deployments
```