.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _project-import-export:

##########################################
Exporting and Importing |AMHlong| Projects
##########################################


.. meta::
   :description: How to use the |AMHlong| console and manual actions to export and import projects.


.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

    Import /Export Troubleshooting <project-import-export-troubleshooting>
    Project Export Format <project-import-export-yaml>
    Manually Exported Components <project-import-export-manual>


.. _import-export-overview:

Overview
========


|AMH| provides the ability to export and import YAML files that describe the configuration of your
|AMH| project. Anyone with an AWS account can import an exported project configuration file to
deploy a new project, with new AWS resources that match the configuration being imported.

This feature enables you to replicate the AWS service configuration of an exported project. While
the data in a project's tables is not exported, files in storage or hosting buckets and API handler
function code can be manually added to your exported project definition. To learn more, see
:ref:`import-export-manual`.

.. image:: images/diagram-abstract-import-export.png


**To export a project configuration file**


#. Navigate to your project list in the |AMH| console.

#. Hover over the ellipses (three dots) in the upper right of the project card.

#. Choose :guilabel:`Export (file)` in the upper right of the card for the project you want to
   export.

#. Save your project export file.

To learn more about the content of an exported project configuration file, see
:ref:`project-import-export-yaml-details`.


**To import a project**

#. Navigate to your project list in the |AMH| console.

#. Choose :guilabel:`Import your project` in the upper left of the page.

#. Browse or drag a project definition file into the :guilabel:`Import project configuration`
   dialog.

#. Choose :guilabel:`Import project`.


.. _import-export-deploy-links:

Sharing Your Project Configuration with a Deploy to |AMHlong| Link
==================================================================


In any public GitHub repo, you can provide a link that instantly kicks off creation of a new |AMH|
project by importing the exported project configuration file define in the link's querystring. The
form of the link should be:

:code:`https://console.aws.amazon.com/mobilehub/home?#/?config=YOUR-MOBILE-HUB-PROJECT-CONFIGURATION-LOCATION`

For example, the following HTML creates a link that provides instant configuration of an app's AWS
backend services, based on |AMH| features defined in :file:`react-sample.zip`. To see this code in
action, see :file:`README.md` for the `AWS Mobile React Sample
<https://github.com/awslabs/aws-mobile-react-sample>`_.

.. code-block:: html

    <p align="center">
       <a target="_blank" href="https://console.aws.amazon.com/mobilehub/home?#/?config=https://github.com/awslabs/aws-mobile-react-sample/blob/master/backend/import_mobilehub/react-sample.zip">
       <span>
           <img height="100%" src="https://s3.amazonaws.com/deploytomh/button-deploy-aws-mh.png"/>
       </span>
       </a>
    </p>

The querystring portion of the link can point to the location of a |AMH| project configuration
:file:`mobile-hub-project.yml` file or a project export :file:`.zip` file containing a
:file:`mobile-hub-project.yml` file.

.. important:: If you are using a :file:`.zip` file it must conform to the structure and content
   required by a |AMH| project configuration import. For details, see
   :ref:`project-import-export-zip`.


.. _import-export-limitations:

Limitations of Importing Projects
=================================



.. contents::
   :local:
   :depth: 1

.. _import-export-limitations-file-size:

Maximum Project Definition File Size is 10MB
--------------------------------------------


Import of |AMH| project :file:`.zip` or :file:`.yml` files larger than 10MB is not supported.


.. _import-export-limitations-manual-mods:

Project Components that Require Manual Export
---------------------------------------------


To enable import of the following project configuration items, you must manually modify your
project's exported :file:`.zip` file:


* Data User Storage Contents

  To import files stored in a User Data Storage |S3| bucket in your original project, see
  :ref:`import-export-user-data-storage-contents`.


* Hosting and Streaming Contents

  To import files hosted in a Hosting and Streaming bucket in your original project, see
  :ref:`import-export-hosting-and-streaming-contents`.


* SAML Federation

  To import User Sign-in SAML federation configuration from your original project, see
  :ref:`import-export-saml`.


* Cloud Logic API Handlers

  To import Cloud Logic API handler code and configuration from your original project, see
  :ref:`import-export-cloud-logic`.

  .. note:: Calling Cloud Logic APIs from a browser requires that Cross-Origin Resource Sharing
     (CORS) is configured for each API path. To enable CORS configuration when your project is
     imported, see :ref:`import-export-cors`.


.. _import-export-limitations-manual-credentials:

Cross Account Credentials
-------------------------


Some features require credentials and assets that are associated with the AWS account where they are
configured. |AMH| projects that contain such features can only be imported into the account that
exported them. Features with this restriction include Cloud Logic APIs that were created outside of
the |AMH| project being exported, messaging provider credentials for Push Notification, and |SNS|
topics.


.. list-table::
   :header-rows: 1
   :widths: 1 4

   * - :guilabel:`Mobile Hub Feature`

     - :guilabel:`Can be exported from one AWS account and imported into another?`

   * - :guilabel:`User Sign-in`

     - Yes

   * - :guilabel:`NoSQL Database`

     - Yes

   * - :guilabel:`Cloud Logic`

     - :subscript:`Using APIs created within your Mobile Hub project:`

       Yes

       :subscript:`Using APIs imported into your project:`

       No (for remedy, see :ref:`import-export-troubleshooting-imported-api`)

   * - :guilabel:`User Data Storage`

     - Yes

   * - :guilabel:`App Content Delivery`

     - Yes

   * - :guilabel:`Connectors`

     - Yes

   * - :guilabel:`Push Notifications`

     -  No (for remedy, see :ref:`import-export-troubleshooting-push-credentials`)

   * - :guilabel:`Messaging and Analytics` (Push Notification)

     -  No (for remedy, see :ref:`import-export-troubleshooting-push-credentials`)


.. _import-export-limitations-manual-unsupported:

Project Components that Are Not Exported
----------------------------------------


The following items are not supported by the |AMH| import/export feature:


* Custom policy

  When you enable a |AMH| feature, a set of AWS services is deployed. |AMH| attaches default access
  roles and policies to these objects. When a project is imported, the default roles and policies
  are applied.

  In your original project, you can to modify or add to these defaults; for example, to set access
  to a data table to read only. When you export your project configuration, any such customizations
  are not included in the project export. To enable your custom policy in an imported project, the
  importer must manually configure those policies in the imported project. In addition to your
  project export file, we recommend you provide both your policy JSON and step by step instructions
  for importers. These instructions should describe how to use AWS consoles or the `AWS CLI <http://docs.aws.amazon.com/cli/latest/userguide/>`_ to
  implement your customizations.


* Legacy Cloud Logic

  Import and export are not supported for projects using the legacy Cloud Logic feature. A project
  of this kind calls |LAM| functions directly. The current version of Cloud Logic makes RESTful
  calls to |ABPlong| APIs linked to |LAM| function handlers.






