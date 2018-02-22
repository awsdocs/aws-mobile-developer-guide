.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _project-import-export-manual:

####################################
Manually Exported Project Components
####################################


.. meta::
   :description: |AMHlong| project components that can be exported manually.


This section describes how to manually add project components to an exported project definition.

.. contents::
   :local:
   :depth: 1

.. _import-export-user-data-storage-contents:

Importing User Data Storage Contents
====================================


When a project that enables User Data Storage is exported, files stored in its |S3| bucket are not
included in its exported project definition. You can manually configure the project definition to
upload those files to the new bucket of the imported project.

**To configure import and upload of project files stored in a User Data Storage bucket**

#. Uncompress your exported project :file:`.zip` file.

#. Copy and paste each file that you want uploaded during import into the unzipped file folder.

#. Add file paths to your exported project definition:


   #. Open the :file:`mobile-hub-project.yml` file of the export in an editor.

   #. If not already present, create an :code:`uploads:` node at the root level.

   #. For each file to be uploaded, add the following three items under :code:`uploads:`.

      #. The namespace :code:`- !com.amazonaws.mobilehub.v0.Upload`

      #. The key :code:`fileName:` with the value of the path to the file within the project
         definition :file:`.zip` file.

      #. The key :code:`targetS3Bucket:` with the value of :code:`user-files`.

         .. code-block:: yaml

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

#. Rezip the files within the uncompressed project definition file (not the folder containing those
   files, because that causes a path error).

.. _import-export-hosting-and-streaming-contents:

Importing Hosting and Streaming Contents
========================================

When a project that enables Hosting and Streaming is exported, files stored in its |S3| bucket are
not included in the exported project definition. You can manually configure the project definition
to upload those files to the new bucket of the imported project.

**To configure import and upload of project files stored in a Hosting and Streaming bucket**

#. Uncompress your exported project :file:`.zip` file.

#. Copy and paste each file that you want uploaded during import into the unzipped file folder.

#. Add file paths to your exported project definition:


   #. Open the :file:`mobile-hub-project.yml` file of the export in an editor.

   #. If not already present, create an :code:`uploads:` node at the root level.

   #. For each file to be uploaded, add the following three items under :code:`uploads:`.

      #. The namespace :code:`- !com.amazonaws.mobilehub.v0.Upload`

      #. The key :code:`fileName:` with the value of the path to the file within the project
         definition :file:`.zip` file.

      #. The key :code:`targetS3Bucket:` with the value of :code:`hosting`.

         .. code-block:: yaml

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

#. Rezip the files within the uncompressed project definition file (not the folder containing those
   files, because that causes a path error).


.. _import-export-saml:

Importing SAML Federated User Sign-in
=====================================


Configuring SAML federation for the |AMH| User Sign-in feature requires you to supply the SAML XML
configuration (:file:`saml.xml`) of the identity provider you federate. The SAML XML configuration
is not included in the :file:`.zip` file exported by |AMH|.


**To configure an exported project to deploy the original project's SAML federation when it is imported**


#. Uncompress your exported project :file:`.zip` file.

#. Copy your identity provider's :file:`saml.xml` file into the root folder of the uncompressed
   :file:`.zip` file.

#. Rezip the files within the uncompressed project definition file (not the folder containing those
   files, because that causes a path error).


.. _import-export-cloud-logic:

Importing API Handlers for Cloud Logic APIs
===========================================


The |AMH| Cloud Logic feature pairs a RESTful API surface (|ABP|) with serverless API handler
functions (|LAM|). While |AMH| supports exporting and importing the definitions of API and handler
objects that Cloud Logic configures, the API handler function code is not exported.

|AMH| enables you to manually configure your project export :file:`.zip` file to deploy your API
handler function code as part of the project import when the following conditions are met:


* Your API handler accesses only |DDB| tables. Import of API handlers that access other AWS
  services, such as |S3|, is not currently supported.


* Your handler code is factored to use `Lambda environmental variables <http://docs.aws.amazon.com/lambda/latest/dg/tutorial-env_cli.html>`__ to
  refer to those |DDB| tables.

  When |AMH| imports API handler code, it uses environmental variables to map data operations to the
  new tables created by the import. You can define the key name of environmental variables in the
  project's definition YAML to match constant names you define in the project's |LAM| API handler
  function code. The following example shows a |LAM| function constant being equated to an
  environmental variable.

  .. code-block:: none

      const YOUR-FUNCTION-CONSTANT-NAME = process.env.KEY-NAME-DEFINED-IN-YAML;";

      // example
      const MENU_TABLE_NAME = process.env.MENU_TABLE_NAME;

  The steps that follow these notes describe how to define your environmental variables in project
  definition YAML.

  .. note:: An alternative is to use the :code:`MOBILE_HUB_DYNAMIC_PREFIX` project identifier prefix
     that |AMH| generates. |AMH| configures its value to be the unique identifier for the imported
     project. When you append a valid table name to that prefix in your function code, it composes a
     valid identifier for the table in the imported project. The following example shows a |LAM|
     function constant being equated to an environmental variable.

     .. code-block:: none

         const YOUR-FUNCTION-CONSTANT-NAME = process.env.MOBILE_HUB_DYNAMIC_PREFIX + "-YOUR-TABLE-NAME";

         // example
         const MENU_TABLE_NAME = process.env.MOBILE_HUB_DYNAMIC_PREFIX + "-bbq-menu";

     This method does not require additional manual configuration of the project definition YAML.

The `AWS Mobile React sample app <https://github.com/awslabs/aws-mobile-react-sample>`__ provides an
end to end example of using environmental variables to access data tables through an API and its
handler. Take the following steps for each API handler whose code you want to import. Examples from
the sample app are given in line.


**To enable import of |LAM| handler functions for your exported Cloud Logic API**

#. Uncompress your exported project :file:`.zip` file.

#. Copy your |LAM| function(s) into the uncompressed file.


   #. Go to the `Amazon S3 console <https://console.aws.amazon.com/s3/>`__ and search for your |AMH| project name.

   #. Choose the bucket with the name containing :code:`-deployments-`, then choose the
      :file:`uploads` folder.

   #. Copy and save the name(s) of the |LAM| function file(s) in the folder for use in following
      steps.

   #. Copy the |LAM| function file(s) in the folder into your unzipped exported project file.

#. Add file paths to your exported project definition.


   #. Open the :file:`mobile-hub-project.yml` file of the export in an editor.

   #. If not already present, create an :code:`uploads:` node at the root level.

   #. For each file to be uploaded, add the following three items under :code:`uploads:`.

      #. The namespace :code:`- !com.amazonaws.mobilehub.v0.Upload`

      #. The key :code:`fileName:` with the value of the path to the file within the project
         definition :file:`.zip` file.

      #. The key :code:`targetS3Bucket:` with the value of :code:`deployments`.

   #. If not already present in each Cloud Logic :code:`. . . paths: items` node, create a
      :code:`codeFilename:` key with the value of the path of the |LAM| function code file for that
      handler.

      .. note:: The path in this case is relative to the root of the :code:`-deployments-` |S3|
         bucket |AMH| provisioned for Cloud Logic. Typically, |AMH| places these files in an
         :file:`/uploads` folder.

         If no :code:`codeFilename` is specified, then |AMH| deploys a default handler that echos
         requests it receives.

   #. Add environmental variables to your exported project definition.

      For each Cloud Logic :code:`. . . paths: items` node that describes a handler that interacts
      with a |DDB| table, add an :code:`environment:` node with child members that are composed by
      concatenating an environmental variable name, with the string :code:`__DYNAMIC_PREFIX__`, and
      the associated table name. The variable name should map to the associated variable in your
      |LAM| API handler function code.

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

#. Save the :file:`.yml` file and rezip the files within the uncompressed project definition file
   (not the folder containing those files, because that causes a path error).

#. Test your revised project export definition by importing it through the |AMH| console. You can
   verify your environmental variables through the |LAM| console.

.. note:: By default, the |AMH| NoSQL Database feature configures a table's permissions to grant
   read and write access for |LAM| functions. The kind of custom |IAM| policy configuration required
   to change the table's permissions is not included in the export of a project. An importer of a
   project dependent on custom policy needs enough information to recreate the policy once they have
   imported the project. For such a case, we recommend you provide both your policy JSON and step by
   step instructions (console or |CLI|) on how and where to attach it. For more information on those
   steps, see `Authentication and Access Control for Amazon DynamoDB
   <http://docs.aws.amazon.com/lambda/latest/dg/authentication-and-access-control.html>`__.


.. _import-export-cors:

Importing Cross-Origin Resource Sharing (CORS) Configuration
============================================================


By default, AWS security infrastructure prevents calls to an |ABP| API from a browser. Configuring
CORS for each path of your API securely enables your API calls over the web. CORS configuration is
not included in |AMH| project export. The following steps describe how to manually include import of
CORS configuration in your project export file.


**To include CORS configuration for your |ABP| API paths**


#. Unzip your exported project definition :file:`.zip` file.

#. Open the export's :file:`mobile-hub-project.yml` file in an editor.

#. For each API path, add a key named :code:`enableCORS` with the value :code:`true` under
   :code:`... paths: "/items/. . .": !com.amazonaws.mobilehub.v0.Function`, as shown in the
   following fragment.

   .. code-block:: yaml
      :emphasize-lines: 24

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

#. Rezip the files within the uncompressed project definition file (not the folder containing those
   files, because that causes a path error).



