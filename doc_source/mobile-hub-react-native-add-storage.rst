
.. _react-native-add-storage:

###########
Add Storage
###########


.. meta::
   :description:

   Learn how to use |AMHlong| to create, build, test and monitor mobile apps that are integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

.. _react-native-add-storage-setup:

Set Up Your Backend
===================

The AWS Mobile CLI :ref:`User File Storage <user-data-storage>` feature enables apps to store user files in the cloud.

.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <mobile-hub-react-native-getting-started>`.

**To configure your app's cloud storage location**

In your app root folder, run:

.. code-block:: shell

      awsmobile user-files enable

      awsmobile push


.. _react-native-add-storage-connect:

Connect to Your Backend
=======================

**To add User File Storage to your app**

In your component where you want to transfer files:

Import the :code:`Storage` module from aws-amplify and configure it to communicate with your backend.

.. code-block:: javacript

    import { Storage } from 'aws-amplify';


Now that the Storage module is imported and ready to communicate with your backend, implement common file transfer actions using the code below.

.. _react-native-add-storage-upload:

Upload a file
-------------

**To upload a file to storage**

Add the following methods to the component where you handle file uploads.

.. code-block:: javascript

    async uploadFile() {
      let file = 'My upload text';
      let name = 'myFile.txt';
      const access = { level: "public" }; // note the access path
      Storage.put(name, file, access);
    }


.. _react-native-add-storage-get:

Get a specific file
-------------------

**To download a file from cloud storage**

Add the following code to a component where you display files.

.. code-block:: javascript

    async getFile() {
      let name = 'myFile.txt';
      const access = { level: "public" };
      let fileUrl = await Storage.get(name, access);
      // use fileUrl to get the file
    }

.. _react-native-add-storage-list:

List all files
--------------

**To list the files stored in the cloud for your app**

Add the following code to a component where you list a collection of files.

.. code-block:: javascript

    async componentDidMount() {
      const path = this.props.path;
      const access = { level: "public" };
      let files = await Storage.list(path, access);
       // use file list to get single files
    }

Use the following code to fetch file attributes such as the size or time of last file change.

.. code-block:: javascript

    file.Size; // file size
    file.LastModified.toLocaleDateString(); // last modified date
    file.LastModified.toLocaleTimeString(); // last modified time

.. _react-native-add-storage-remove:

Delete a file
-------------

Add the following state to the element where you handle file transfers.

.. code-block:: javascript

    async deleteFile(key) {
      const access = { level: "public" };
      Storage.remove(key, access);
    }


Next Steps
==========

Learn more about the analytics in AWS Mobile which are part of the :ref:`User File Storage <user-data-storage>` feature. This feature uses `Amazon Simple Storage Service (S3) <https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html>`__.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://aws.github.io/aws-amplify>`__.
