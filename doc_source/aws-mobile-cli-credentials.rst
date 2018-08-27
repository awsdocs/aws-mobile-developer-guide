
.. _aws-mobile-cli-credentials:

###############################
AWS Mobile CLI User Credentials
###############################


.. meta::
    :description:
        Learn about the credentials required to use |AMHlong| to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.


Overview
--------

The first time you set up the CLI you will be prompted to provide AWS user credentials. The credentials establish permissions for the CLI to manage AWS services on your behalf. They must belong to an AWS IAM user with administrator permissions in the account where the CLI is being used.

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




