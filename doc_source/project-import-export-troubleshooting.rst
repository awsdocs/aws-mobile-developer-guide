.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _project-import-export-troubleshooting:

###################################################
Troubleshooting Project Creation, Import and Export
###################################################


.. meta::
   :description: Troubleshooting for issues encountered when using the |AMHlong| console to import
      projects.


The following sections describe issues you might encounter when setting  up, importing or exporting |AMH| projects,  and their remedies.


.. contents::
   :local:
   :depth: 1

.. _import-export-troubleshooting-imported-api:

Cannot Import an API
====================

Error Message

   - :code:`Project owner does not own existing API : arn:aws:execute-api:us-east-1:012345678901:abcdefghij.`

     :emphasis:`(where the API identifier arn:aws:execute-api:us-east-1:012345678901:abcdefghij is specific to the project being imported)`

Description

   - This message means that the API with the ID shown cannot be imported because it does not exist in the current AWS account. This occurs when the APIs in the original project were created outside of the Mobile Hub Cloud Logic feature and then imported.

Remedy

   - **To remedy this condition, take the following steps.**

     #. Modify the YAML of the project definition you are importing by removing the sections under
        the :code:`features:components` node that begin with the name of an API that was imported
        into the original project's Cloud Logic feature.

     #. Save and import the project definition.

     #. Enable the |AMH| Cloud Logic feature in your imported project and recreate the API and its
        handler.


.. _import-export-troubleshooting-nosql:

Cannot Import a NoSQL Table
===========================

Error Message

    - There is already an existing DynamoDB table called 'someprojectname-mobilehub-012345678-TableName' in your account. Please choose a different name or remove the existing table and retry your request.

      :emphasis:`(where the table name someprojectname-mobilehub-012345678-TableName is specific to the project being imported)`

Description

    - This message occurs when you import a project containing the NoSQL Database Feature. It indicates that the Amazon DynamoDB table in the project configuration already exists. This can occur when a YAML tablename value was edited in the project definition file and there is more than one attempt to import it into the same account.

Remedy

    - **To remedy this condition, take the following steps**

      #. Modify any tablename values to remove the conflict.

      #. Save and import the project definition.

      #. Adjust the code of the imported app where it references the old tablename value.



.. _import-export-troubleshooting-nosql-maximum:

Cannot Import Multiple NoSQL Tables
===================================



Error Message

    - Project file(s) cannot be decoded. They may contain data that was encrypted by a different account. Failed to decode push feature. Failed to decode credential attribute.

Description

    - This message occurs when you import Push Notifications messaging service credentials or Amazon SNS topic identifiers for features that are not associated with your AWS account.

Remedy

    * **To remedy this condition, take the following steps**

      #. Modify the YAML of the project definition you are importing by removing table definition
         sections.

      #. Save and import the project definition.

      #. Use the table definitions you removed to manually create those tables using the |AMH| NoSQL
         Database feature.


.. _import-export-troubleshooting-push-credentials:

Cannot Import Push Credentials
==============================

Error Message

    - Project file(s) cannot be decoded. They may contain data that was encrypted by a different account. Failed to decode push feature. Failed to decode credential attribute.

Description

    - This message occurs when you import Push Notifications messaging service credentials or Amazon SNS topic identifiers for features that are not associated with your AWS account.

Remedy

    * **To remedy this condition, take the following steps**

      #. Modify the YAML of the project definition you are importing by removing the push: node.

      #. Save and import the project definition.

      #. Enable the Mobile Hub Push Notifications or User Engagement feature using your own messaging service credentials and topics.


Build Artifacts Can't be Found
==============================

Error Message

    - Unable to find build artifact uploads/exported-project-definition.zip in Amazon S3 bucket archive-deployments-mobilehub-0123456789 for project-name.

      :superscript:`where exported-project-definition, the numerical portion of the Amazon S3 bucket identifier, and the project-name are specific to the project being imported)`

Description

    - This message occurs when a project import fails because Mobile Hub can't find the file of a Cloud Logic API handler function (Lambda) that is specified in the .yml project definition file.

Remedy

    * **To remedy this condition, take the following steps**

      The remedy for this condition is to make the location of the Lambda file(s) match the path specified in the project definition YAML.

      The error occurs if, for any reason, the path described in the codeFilename: key in the YAML does not match the actual location of the Lambda function file relative to the root of the :code:`...-deployments-...` Amazon S3 bucket that Mobile Hub deploys when Cloud Logic is enabled. For more information, see :ref:`Importing API Handlers for Cloud Logic APIs <import-export-cloud-logic>`.

      .. code-block:: yaml

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
           . . .

      Potential reasons include:

      * A typo in the path value of the :code:`uploads: fileName` key in the YAML.

      *  A path error caused during manual modifications to a project definition .zip file.

         To make a project's Cloud Logic API handler Lambda functions available for import, an author must unzip, modify, and rezip the exported project file. If the uncompressed project definition file folder is rezipped, rather than zipping the contents within that folder, the path is changed so that the original archive is inside of a new archive folder. If the path to an original export named :file:`your-project.zip` was :file:`lambda-archive.zip`, then the path would change to :file:`your-project/lambda-archive.zip`. You can remedy this by modifying the uploads: fileName value or rezipping the project export file contents without the including the folder.

      * A missing Lambda file in a project definition file containing a YAML file that specifies a path for :code:`uploads: fileName`.


.. _import-export-troubleshooting-s3-configuration:


Unable to Configure S3 Bucket During
====================================


Error Message

  - It looks like there was a problem creating or configuring your S3 bucket.

Description

  - Mobile Hub was unable to create a S3 bucket for your project's deployment artifacts during |AMH| project import.

Remedy

  * **To remedy this condition, try the following steps**

    Check that you are not at maximum bucket capacity using the `Amazon S3 console <https://console.aws.amazon.com/s3/>`__.

.. _import-export-troubleshooting-adminstrator-required:

Administrator Required Error During Setup
=========================================


Error Message

  - It looks like you do not have permission for this operation.

Description

  - The user does not have permission to create the required Mobile Hub Service Role during configuration of a |AMH| project.

Remedy

  * **To remedy this condition, try the following steps**

    Contact an administrator for your AWS account and ask them to create the service role at the following location: `https://console.aws.amazon.com/mobilehub/home#/activaterole/ <https://console.aws.amazon.com/mobilehub/home#/activaterole/>`__.

.. _import-export-troubleshooting-incomplete-setup:

Account Setup Incomplete
========================

Error Message

  - It looks like your AWS account is not fully set up.

Description

  - This error can occur for a range of reasons during |AMH| project configuration.

Remedy

  * **To remedy this condition, try the following steps**

    * Sign out of the AWS console and lose down all browser windows. Then try to log in to the `AWS Mobile console <>`__ and attempt the operation that initially caused the er.
    * If the issue persists, post to the `AWS Mobile Development forum<https://forums.aws.amazon.com/forum.jspa?forumID=88>`__ for support.


.. _import-export-troubleshooting-file-size:

File Too Large to Import
========================

Error Message

    - The project file is too large. The max file size is 10 MB.

Description

    - This message occurs when you attempt to import a project definition file that is larger than 10MB.

Remedy

    - Reduce the size of the project export file. Project exporters may want to deliver large file payloads outside of their project definition files, along with providing instructions for importers about how to use AWS consoles to incorporate those accompanying files.





