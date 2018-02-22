.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-mobile-hub-iam-auth-access:

#################################################
|IAM| Authentication and Access Control for |AMH|
#################################################


In depth understanding of AWS authentication and access controls is not required to build a mobile
app using |AMHlong|.

|AMH| uses AWS credentials and permissions policies in two ways:


* :ref:`reference-mobile-hub-iam-managed-policies`.

* Providing :ref:`reference-mobile-hub-iam-service-role` to create and configure the back-end features you select
  for your mobile app.

The following sections provide details on how |IAM| works, how you can use |IAM| to securely control
access to your projects, and what |IAM| roles and policies |AMH| configures on your behalf.


.. contents::
   :local:
   :depth: 1

.. _authentication:

Authentication
~~~~~~~~~~~~~~


AWS resources and services can only be viewed, created or modified with the
correct authentication using AWS credentials (which must also be granted
:ref:`access permissions <reference-mobile-hub-iam-access-control>` to
those resources and services). You can access AWS as any of the following types of identities:


* **AWS account root user**

  When you sign up for AWS, you provide an email address and password that is associated with your
  AWS account. These are your root credentials and they provide complete access to all of your AWS
  resources.



  .. important:: For security reasons, we recommend that you use the root credentials only to create an
     administrator user, which is an |IAM| user with full permissions to your AWS account. Then, you
     can use this administrator user to create other |IAM| users and roles with limited permissions.
     For more information, see `IAM Best Practices <http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users>`__ and
     `Creating an Admin User and Group <http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html>`__ in the
     :title:`IAM User Guide`.

* **IAM user**

  An `IAM user <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html>`__ is simply an identity within your AWS account that has specific
  custom permissions (for example, read-only permissions to access your |AMH| project). You can use
  an |IAM| user name and password to sign in to secure AWS webpages like the `AWS Management Console
  <https://console.aws.amazon.com/>`__, `AWS Discussion Forums <http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html>`__, or the `AWS Support
  Center <https://console.aws.amazon.com/support/home#/>`__.

  In addition to a user name and password, you can also generate `access keys
  <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html>`__ for each user. You can use these keys when you access AWS
  services programmatically, either through `one of the several SDKs <https://aws.amazon.com/tools/>`__ or by using the `AWS
  Command Line Interface (CLI) <https://aws.amazon.com/cli/>`__. The SDK and CLI tools use the access keys to
  cryptographically sign your request. If you don't use the AWS tools, you must sign the request
  yourself.

* **IAM role**

  An `IAM role <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`__ is another |IAM| identity you can create in your account that has
  specific permissions. It is similar to an |IAM| user, but it is not associated with a specific
  person. An |IAM| role enables you to obtain temporary access keys that can be used to access AWS
  services and resources. |IAM| roles with temporary credentials are useful in the following
  situations:


  * **Federated user access**

    Instead of creating an |IAM| user, you can use preexisting user identities from your enterprise
    user directory or a web identity provider. These are known as federated users. AWS assigns a
    role to a federated user when access is requested through an `identity provider
    <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`__. For more information about federated users, see `Federated Users
    and Roles <http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html#intro-access-roles>`__ in the
    :title:`IAM User Guide`.

  * **Cross-account access**

    You can use an |IAM| role in your account to grant another AWS account permissions to access
    your account's resources. For an example, see `Tutorial: Delegate Access Across AWS Accounts
    Using IAM Roles <http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`__ in the :title:`IAM User Guide`.

  * **AWS service access**

    You can use an |IAM| role in your account to grant an AWS service permissions to access your
    account's resources. For example, you can create a role that allows |RSlong| to access an |S3|
    bucket on your behalf and then load data stored in the bucket into an |RS| cluster. For more
    information, see `Creating a Role to Delegate Permissions to an AWS Service
    <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html>`__ in the :title:`IAM User Guide`.

  * **Applications running on Amazon EC2**

    Instead of storing access keys within the EC2 instance for use by applications running on the
    instance and making AWS API requests, you can use an |IAM| role to manage temporary credentials
    for these applications. To assign an AWS role to an EC2 instance and make it available to all of
    its applications, you can create an instance profile that is attached to the instance. An
    instance profile contains the role and enables programs running on the EC2 instance to get
    temporary credentials. For more information, see `Using Roles for Applications on Amazon EC2
    <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html>`__ in the :title:`IAM User Guide`.

Access Control
~~~~~~~~~~~~~~

You can have valid credentials to authenticate your requests, but unless you have permissions you
cannot access or modify a |AMH| project. The same is true for |AMH| when it creates and configures
services and resources you have configured for your project.

The following sections describe how to manage permissions and understand those that are being
managed on your behalf by |AMH|.


   * :ref:`reference-mobile-hub-iam-managed-policies`

   * :ref:`reference-mobile-hub-iam-service-role`




