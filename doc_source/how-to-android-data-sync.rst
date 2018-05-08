.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. highlight:: java

###########################################
Android: Sync Data with Amazon Cognito Sync
###########################################

.. list-table::
   :widths: 1 6

   * - New User?

     - Use `AWS AppSync <https://aws.amazon.com/appsync/>`__ instead. AppSync is a new service for synchronizing application data across devices. Like Cognito Sync, AppSync enables synchronization of a user's own data, such as game state or app preferences. AppSync extends these capabilities by allowing multiple users to synchronize and collaborate in real-time on shared data, such as a virtual meeting space or chatroom.

       `Start building an Android app with AWS AppSync now <https://docs.aws.amazon.com/appsync/latest/devguide/building-a-client-app-android.html>`__.

Overview
--------

|COG| Sync is an AWS service and client library that enables cross-device syncing of
application-related user data. You can use the |COG| Sync API to synchronize user profile data
across devices and across login providers |mdash| Amazon, Facebook, Twitter/Digits, Google, and your
own custom identity provider.

For instructions on how to integrate Amazon Cognito Sync in your application, see  `Amazon Cognito
Sync Developer Guide <http://docs.aws.amazon.com/cognito/devguide/sync/>`_.


Set Up the SDK
--------------

You must complete all of the instructions on the :doc:`how-to-android-sdk-setup` page before beginning
this tutorial.


Initialize the CognitoSyncManager
---------------------------------

Pass your initialized Amazon Cognito credentials provider to the :code:`CognitoSyncManager`
constructor::

  CognitoSyncManager client = new CognitoSyncManager(
      getApplicationContext(),
      Regions.YOUR_REGION,
      credentialsProvider);

For more information about Cognito Identity, see :doc:`cognito-auth-legacy`.


Syncing User Data
-----------------

To sync unauthenticated user data:

#. Create a dataset and add user data.
#. Synchronize the dataset with the cloud.


Create a Dataset and Add User Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: option

   Android - Java

    Create an instance of :code:`Dataset`. User data is added in the form of key/value pairs. Dataset objects are created with the :code:`CognitoSyncManager` class which functions as a Cognito client object. Use the defaultCognito method to get a reference to the instance of CognitoSyncManager. The openOrCreateDataset method is used to create a new dataset or open an existing instance of a dataset stored locally on the device::

    .. code-block:: java

       Dataset dataset = client.openOrCreateDataset("datasetname");

    Cognito datasets function as dictionaries, with values accessible by key::

    .. code-block:: java

       String value = dataset.get("myKey");
       dataset.put("myKey", "my value");

   Android - Kotlin

    Create an instance of :code:`Dataset`. User data is added in the form of key/value pairs. Dataset objects are created with the :code:`CognitoSyncManager` class which functions as a Cognito client object. Use the defaultCognito method to get a reference to the instance of CognitoSyncManager. The openOrCreateDataset method is used to create a new dataset or open an existing instance of a dataset stored locally on the device::

    .. code-block:: kotlin

       val dataset = client.openOrCreateDataset("datasetname")

    Cognito datasets function as dictionaries, with values accessible by key::

    .. code-block:: kotlin

      var dataValue = dataset.get("myKey")
      dataset.put("myKey", dataValue);

Synchronize Dataset with the Cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To synchronize a dataset, call its synchronize method::

  dataset.synchronize();

All data written to datasets will be stored locally until the dataset is synced. The code in this section assumes you are using an unauthenticated Cognito identity, so when the user data is synced with the cloud it will be stored per device. The device has a device ID associated with it. When the user data is synced to the cloud, it will be associated with that device ID.

To sync user data across devices (using an authenticated identity), see `Amazon Cognito Sync
<http://docs.aws.amazon.com/cognito/devguide/sync/>`_.

.. _Cognito Console: https://console.aws.amazon.com/cognito
