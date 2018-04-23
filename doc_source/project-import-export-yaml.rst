.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _project-import-export-yaml:

###########################
|AMH| Project Export Format
###########################


.. meta::
   :description: Details of how |AMHlong| project configurations can be exported as a YAML file and
      then imported to create a new project with a configuration that matches the original.


|AMHlong| provides the ability to export a YAML file containing the configuration of your project.
The YAML file itself can be imported or it can be included in a :file:`.zip` file with other project
components that get deployed during project import. This section describes the anatomy of the YAML
and a typical |AMH| project export :file:`.zip` file. For more information about the |AMH|
Import/Export feature, see :ref:`project-import-export`.


.. contents::
   :local:
   :depth: 1

.. _project-import-export-zip:

Structure of a Project Export .zip File
=======================================


When you choose :guilabel:`Export (file)`, |AMH| generates a :file:`.zip` file named for your
project.

Default file structure

    Mobile Hub also generates a :file:`mobile-hub-project.yml` project configuration file in the :file:`.zip` root. A valid :file:`mobile-hub-project.yml` file in this location is required for Mobile Hub project import to succeed.

Example file structure

    File structure of the :file:`.zip` file an exported project, configured to include deployment of both SAML federation and Cloud Logic API handlers, is as follows:

    * :file:`{/your-project-name}.zip`


      * :file:`mobile-hub-project.yml`

      * :file:`saml.xml`

      * :file:`lambda API handler functions`

      * :file:`user data stored files`

      * :file:`hosted files`

Files in a project export :file:`.zip` file can be arranged in folders. The relative paths within
the archive must be reflected in the project definition YAML key values that refer to their paths.

.. note:: The presence of any files or folders in the project configuration :file:`.zip` file, other
   than those described in the preceding section, may be ignored or cause issues upon import.


.. _project-import-export-yaml-details:

Structure of a Project Export .yml File
=======================================


In the abstract, the basic structure of a |AMH| project export :file:`.yml` file is as follows:

.. code-block:: yaml

    features:
        FEATURE-TYPE: !com.amazonaws.mobilehub.v0.:FEATURE-TYPE
              components:
                FEATURE-NAME: !com.amazonaws.mobilehub.v0.FEATURE-TYPE
                    attributes:
                        ATTRIBUTE-NAME: !com.amazonaws.mobilehub.v0.ATTRIBUTE-VALUE
                    OTHER-FEATURE-PROPERTY-TYPES: OTHER-FEATURE-PROPERTY-VALUES
                . . .

The following YAML is a sample of the :file:`mobile-hub-project.yml` exported from a project with
many |AMH| features enabled. The project definition has also been manually updated to enable the
import and upload of components of the original project. These components include files stored in
the original project's User File Storage bucket, files hosted in its Hosting and Streaming bucket,
and API handler code in its |LAM| functions.

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



