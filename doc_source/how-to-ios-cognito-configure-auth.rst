.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-ios-cognito-configure-auth:

######################################################
iOS: Get User Credentials with Amazon Cognito Manually
######################################################


.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-user-sign-in>` to install the SDK and integrate Amazon Cognito.

*Or, use the contents of this page if your app will integrate existing AWS services.*




Use the following content to manually configure AWS credentials.

For your app to access AWS services and resources, each user must have an identity within AWS. Use Amazon Cognito to create unique identities for your users. Amazon Cognito identities can be unauthenticated, or your app can use a range of sign-in methods to become authenticated. For more information, see :ref:`Integrating Identity Providers <integrating-identity-providers>`.

For information about Amazon Cognito Region availability, see `AWS Service Region Availability <http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`__.


Set Up Your Backend
-------------------

Most implementations of AWS services for mobile app features require identity management through Amazon Cognito. The following steps describe how to  AWS credentials to your app users.

In this section:

.. contents::
   :local:
   :depth: 1

1. Create an identity pool and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Take the following steps to create a new identity pool with `Auth` and `Unauth` roles.

   #. Sign in to the `Amazon Cognito console <https://console.aws.amazon.com/cognito/>`__.

   #. Choose :guilabel:`Manage Federated Identities`.

   #. Choose :guilabel:`Create new identity pool`.

   #. Type an :guilabel:`Identity pool name`.

   #. Optional: Select :guilabel:`Enable access to unauthenticated identities`.

   #. Choose :guilabel:`Create Pool`.

   #. Choose :guilabel:`View Details` to review or edit the role names and default access policy JSON document
      for the identity pool you just created. Note the names of your `Auth` and
      `Unauth` roles. You will use them to enact access policy for the AWS resources you use.

   #. Choose: :guilabel:`Allow`.

   #. Choose the language of your app code in the :guilabel:`Platform` menu. Note the `identityPoolId`
      value in the sample code provided.

   For more information, see :ref:`create-identity-pool`.

2. Add the AWS SDK for iOS to your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps in :doc:`how-to-ios-sdk-setup`.

3. Import `AWScore` and Amazon Cognito APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following imports to your project.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                import AWSCore
                import AWSCognito

        iOS - Objective-C
            .. code-block:: objc

                #import <AWSCore/AWSCore.h>
                #import <AWSCognito/AWSCognito.h>

Connect Your Backend
--------------------

1. Initialize the Amazon Cognito Credentials Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following code, replacing the value of `YourIdentityPoolId` with the
`identitPoolId` value you noted when you created your identity pool.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let credentialProvider = AWSCognitoCredentialsProvider(regionType: .USEast1, identityPoolId: "YourIdentityPoolId")
                let configuration = AWSServiceConfiguration(region: .USEast1, credentialsProvider: credentialProvider)
                AWSServiceManager.default().defaultServiceConfiguration = configuration

        iOS - Objective-C
            .. code-block:: objc

                AWSCognitoCredentialsProvider *credentialsProvider = [[AWSCognitoCredentialsProvider alloc] initWithRegionType:AWSRegionUSEast1
                identityPoolId:@"YourIdentityPoolId"];

                AWSServiceConfiguration *configuration = [[AWSServiceConfiguration alloc] initWithRegion:AWSRegionUSEast1 credentialsProvider:credentialsProvider];

                AWSServiceManager.defaultServiceManager.defaultServiceConfiguration = configuration;

    .. note::

      If you created your identity pool before February 2015, you must reassociate your roles with your identity pool to use this constructor. To do so, open the `Amazon Cognito console <https://console.aws.amazon.com/cognito/>`__, select your identity pool, choose :guilabel:`Edit Identity Pool`, specify your authenticated and unauthenticated roles, and save the changes


2. Retrieve Amazon Cognito IDs and AWS Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After   the login tokens are set in the credentials provider, you can retrieve a unique
Amazon Cognito identifier for your end user and temporary credentials that let the app access
your AWS resources.

.. container:: option

    iOS - Swift
        .. code-block:: swift

            let cognitoId = credentialsProvider.identityId

    iOS - Objective-C
        .. code-block:: objc

            // Retrieve your Amazon Cognito ID.
            NSString *cognitoId = credentialsProvider.identityId;

The unique identifier is available in the ``identityId`` property of the credentials provider object.

The `credentialsProvider` communicates with Amazon Cognito, retrieving a unique identifier for the user as well as temporary, limited privilege AWS credentials for the AWS Mobile SDK. The retrieved credentials are valid for one hour.


.. _create-identity-pool:

Identity Pools and IAM Roles
----------------------------

To use Amazon Cognito to incorporate sign-in through an external identity provider into your
app, create an `Amazon Cognito identity pool <http://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html>`__.

An identity in a pool gets access to the AWS resources used by your app by being assigned a
role in AWS Identity and Access Management (IAM). The access level of an IAM role is
defined by the policy that is attached to it. Typical roles for identity pools allow you to
give different levels of access to authenticated (`Auth`)or signed in users, and unauthenticated (`Unauth`)users.

For more information on identity pools, see `Amazon Cognito Identity: Using Federated Identities <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__.

For more information on using IAM roles with Amazon Cognito, see `IAM Roles <https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html>`__ in the *Amazon Cognito Developer Guide*.


.. _integrating-identity-providers:

Integrating Identity Providers
------------------------------

Amazon Cognito identities can be unauthenticated or use a range of methods to sign in and become authenticated, including:

    * Federating with an `external provider <http://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html>`__ such as Google or Facebook


        * For external providers, a developer account and an application registered with the identity provider
          you want to use (`Facebook <https://developers.facebook.com/>`__,
          `Google <https://developers.google.com/>`__,  or `Amazon <http://login.amazon.com/>`__)


    * Federating with a `SAML Provider <http://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html>`__ such as a Microsoft Active Directory instance

        * For SAML federation, the SAML federation metadata for the authenticating system

    * Federating with your existing custom authentication provider using `developer authenticated identities <http://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html>`__

    * Creating your own AWS-managed identity provider using `Amazon Cognito User Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__

Then, each time your mobile app interacts with Amazon Cognito, your user's identity is given a set of temporary
credentials that give secure access to the AWS resources configured for your app.

For information see, `External Identity Providers <http://docs.aws.amazon.com/cognito/devguide/identity/external-providers/>`__ in the *Amazon Cognito Developer Guide*.

Related Documentation
~~~~~~~~~~~~~~~~~~~~~


`Developer Authenticated Identities`_


.. _Cognito Console: https://console.aws.amazon.com/cognito
.. _Developer Authenticated Identities: http://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html
