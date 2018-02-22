.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-ios-data-sync:

#######################################
iOS: Sync Data with Amazon Cognito Sync
#######################################

Authenticate Users with Amazon Cognito Identity
-----------------------------------------------

Amazon Cognito Identity provides secure access to AWS services. Identities are managed by an identity pool. Roles specify resources an identity can access and are associated with an identity pool. To create an identity pool for your application:

#. Log into the `Amazon Cognito console <https://console.aws.amazon.com/cognito/>`__ and click the :guilabel:`New Identity Pool` button
#. Give your Identity Pool a unique name and enable access to unauthenticated identities
#. Click the :guilabel:`Create Pool` button and then the :guilabel:`Update Roles` to create your identity pool and associated roles

For more information on Amazon Cognito Identity, see :ref:`Amazon Cognito Setup for iOS <cognito-auth-aws-identity-for-ios-legacy>`.

.. note::

    The auto-generated Roles include the permissions needed to access Amazon Cognito Sync, so no further configuration is required.

The next page displays code that creates a credential provider that provides a Amazon Cognito Identity for your app to use. Copy the code from Steps 1 & 2 into your AppDelegate.m file as shown below:

Add the following import statements:

    .. container:: option

        Swift
            .. code-block:: swift

                import AWSCore
                import AWSCognito

        Objective-C
            .. code-block:: objc

                #import <AWSCore/AWSCore.h>
                #import <AWSCognito/AWSCognito.h>

If you have an existing AWS credential provider, add the following code to `application:didFinishLaunchingWithOptions` method:

    .. container:: option

        Swift
            .. code-block:: swift

                let credentialProvider = AWSCognitoCredentialsProvider(regionType: .USEast1, identityPoolId: "YourIdentityPoolId")
                let configuration = AWSServiceConfiguration(region: .USEast1, credentialsProvider: credentialProvider)
                AWSServiceManager.default().defaultServiceConfiguration = configuration


        Objective-C
            .. code-block:: objc

                AWSCognitoCredentialsProvider *credentialsProvider = [[AWSCognitoCredentialsProvider alloc] initWithRegionType:AWSRegionUSEast1
                identityPoolId:@"<your-identity-pool-arn>"];

                AWSServiceConfiguration *configuration = [[AWSServiceConfiguration alloc] initWithRegion:AWSRegionUSEast1 credentialsProvider:credentialsProvider];

                AWSServiceManager.defaultServiceManager.defaultServiceConfiguration = configuration;

For more information on Amazon Cognito Identity, see :ref:`Amazon Cognito Setup for iOS <cognito-auth-aws-identity-for-ios>`

Syncing User Data
-----------------

To sync unauthenticated user data:

#. Create a dataset and add user data.
#. Synchronize the dataset with the cloud.

Create a Dataset and Add User Data
----------------------------------

Create an instance of :code:`AWSCognitoDataset`. User data is added in the form of key/value pairs. Dataset objects are created with the :code:`AWSCognito` class which functions as a Amazon Cognito client object. Use the defaultCognito method to get a reference to the default singleton instance of AWSCognito. The openOrCreateDataset method is used to create a new dataset or open an existing instance of a dataset stored locally on the device:

    .. container:: option

        Swift
            .. code-block:: swift

                let dataset = AWSCognito.default().openOrCreateDataset("user_data")

        Objective-C
            .. code-block:: objc

                AWSCognitoDataset *dataset = [[AWSCognito defaultCognito] openOrCreateDataset:datasetName];:@"user_data"];

User data is added to an AWSCognitoDataset instance using the setString\:forKey or setValue\:forKey methods. The following code snippet shows how to add some user data to a dataset:

    .. container:: option

        Swift
            .. code-block:: swift

                dataset?.setString("John Doe", forKey:"Username")
                dataset?.setString("10000", forKey:"HighScore")

        Objective-C
            .. code-block:: objc

                [dataset setString:@"John Doe" forKey:@"Username"];
                [dataset setString:@"10000" forKey:@"HighScore"];

Synchronize Dataset with the Cloud
----------------------------------

To sync the dataset with the cloud, call the synchronize method on the dataset object:

    .. container:: option

        Swift
            .. code-block:: swift

                _ = dataset?.synchronize()

        Objective-C
            .. code-block:: objc

                [dataset synchronize];

All data written to datasets will be stored locally until the dataset is synced. The code in this section assumes you are using an unauthenticated Amazon Cognito identity, so when the user data is synced with the cloud it will be stored per device. The device has a device ID associated with it, when the user data is synced to the cloud, it will be associated with that device ID.

To sync user data across devices (based on an authenticated Cognito Identity) see `Amazon Cognito Sync Developer Guide
<http://docs.aws.amazon.com/cognito/devguide/sync/>`__.

Related Documentation
---------------------
:ref:`Amazon Cognito Setup for iOS <cognito-auth-aws-identity-for-ios>`

`Developer Authenticated Identities`_


.. _Cognito Console: https://console.aws.amazon.com/cognito
.. _Developer Authenticated Identities: http://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html

