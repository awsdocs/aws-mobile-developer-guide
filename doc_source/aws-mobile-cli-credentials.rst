.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


.. _aws-mobile-cli-credentials:

###############################
AWS Mobile CLI User Credentials
###############################


.. meta::
    :description:
        Learn about the credentials required to use |AMHlong| to create, build, test and monitor mobile apps that are
        integrated with AWS services.

Overview
--------

As described on the AWS Mobile CLI :ref:`Get Started <web-getting-started>` page, the first time you set up the CLI you will be prompted to provide AWS user credentials. The credentials establish permissions for the CLI to manage AWS services on your behalf. They must belong to an AWS IAM user with administrator permissions in the account where the CLI is being used.

Permissions
-----------

Administrator permissions are granted by an AWS account administrator. If don't have administrator permissions you will need to ask an administrator for the AWS account to grant them.

If you are the account owner and signed in under the root credentials for the account, then you have, or can grant yourself, administrator permissions using the :code:`AdministratorAccess` managed policy. Best practice is to create a new IAM user under your account to access AWS services instead of using root credentials.

For more information, see :ref:`Control Access to Mobile Hub Projects <reference-mobile-hub-iam-managed-policies>`.

Get Account User Credentials
------------------------------

If you have administrator permissions, the values you need to provide the CLI are your IAM user's Access Key ID and a Secret Access Key. If not, you will need to get these from an administrator.

To provide the ID and the Key to AWS CLI, follow the CLI prompts to sign-in to AWS, and provide a user name and AWS region. The CLI will open the `AWS IAM console <https://console.aws.amazon.com/iam/>`__ :guilabel:`Add user` dialog, with the :code:`AdministratorAccess` policy attached, and the :guilabel:`Programmatic access` option selected by default.

.. contents::
   :local:
   :depth: 1

Get credentials for a new user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Choose :guilabel:`Next: Permissions` and then choose :guilabel:`Create user`.

   Alternatively, you could add the user to a group with :code:`AdministratorAccess` attached.

     .. image:: images/aws-mobile-cli-create-user.png
        :scale: 100
        :alt: Create an AWS IAM user to validate AWS Mobile CLI permissions.

#. Choose :guilabel:`Create user`.

#. Copy the values from the table displayed, or choose :guilabel:`Download .csv` to save the values locally, and then type them into the prompts.

   .. image:: images/aws-mobile-cli-get-keys.png
      :scale: 100
      :alt: Create an AWS IAM user to validate AWS Mobile CLI permissions.

For more detailed steps, see :ref:`add a new account user with administrator permissions <reference-mobile-hub-iam-managed-policies-new-user>`.

Get credentials for an existing user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Choose :guilabel:`cancel`.

#. On the left, choose :guilabel:`Users`, then select the user from the list. Choose :guilabel:`Security credentials`, then choose :guilabel:`Create access key`.




