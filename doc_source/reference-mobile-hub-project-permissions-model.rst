.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-mobile-hub-project-permissions-model:

####################################
Mobile Hub Project Permissions Model
####################################


.. meta::
   :description: This section describes the new permissios model for administrators and users of |AMH| accounts.


.. list-table::
   :widths: 1 6

   * - **Important**

     - To modify |AMH| projects in an account, a user must be :ref:`granted administrative permissions <reference-mobile-hub-iam-managed-policies-how-to>` by an account Administrator. Read this section for more information.

       If you are a user who needs additional permissions for a project, contact an administrator for the AWS account. For help with any issues related to the new permissions model, contact `aws-mobilehub-customer@amazon.com <mailto:aws-mobilehub-customer@amazon.com?subject=Mobile%20Hub%20project%20permissions>`__.


.. contents::
   :local:
   :depth: 1

.. _reference-mobile-hub-project-permissions-model-changes:

Mobile Hub Permissions Model
============================

Currently, Mobile Hub's permissions model uses the user's permissions directly when they perform operations in the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`__ or :ref:`command line interface <aws-mobile-cli-reference>`. This model provides account administrators fine-grained access control over what operations their users can perform in the account, regardless of whether they are using Mobile Hub or they’re using the console or command line interface to interact with services directly.

In order to modify projects, users are required to have permissions to use Mobile Hub (granted by AWSMobileHubFullAccess IAM policy), and they must have permission to perform whatever actions Mobile Hub takes on their behalf.  In almost every case, this means an account administrator must :ref:`grant the user the AdministratorAccess policy <reference-mobile-hub-iam-managed-policies-how-to>`  in order to provide access to the AWS resources Mobile Hub modifies. This is because, as project settings are modified, |AMH| will modify the IAM roles and policies used to enable the features affected by those settings. Changing IAM roles and policies allows the user to control access to resources in the account, and so they must have administrative permissions.

When an administrator does not want to grant administrative permissions for the full account, they can choose instead to provide each user or team their own sub-account :ref:`using AWS Organizations <reference-mobile-hub-iam-managed-policies-aws-organizations>`. Within their sub-account, a user will have full administrative permissions. Sub-account owners are only limited in what they can do by the policy put in place by their administrator, and billing rolls up to the parent account.

.. _reference-mobile-hub-project-permissions-model-users:

What if I Currently Use MobileHub_Service_Role to Grant Mobile Hub Permissions?
===============================================================================

Previously, |AMH| assumed a service role called :code:`MobileHub_Service_Role` in order to modify service configurations on your behalf using the following managed policy:

`https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly>`__

In that older model, all that was required to modify Mobile Hub projects was permissions to call Mobile Hub APIs, through the console or command line. An administrator could delegate those permissions by attaching the :code:`AWSMobileHub_FullAccess` policy to an `AWS IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>`__ user, group, or role.

If the account of your Mobile Hub projects relies on the old model, the impact on those who are not granted AdministratorAccess permissions will be as follows.

  * IAM users, groups and roles that have the :code:`AWSMobileHub_FullAccess` policy will no longer have sufficient permissions to perform any mutating operations in |AMH|, either via the console or :code:`awsmobile` command line interface (CLI).

  * In order for IAM users, groups, or roles to be able to perform mutating operations using Mobile Hub, they must have the appropriate permissions. The two choices for an administrator to :ref:`grant users permission <reference-mobile-hub-iam-managed-policies>` to invoke all available operations in Mobile Hub are: attach the :code:`AdministratorAccess` policy to the user, or a role they are attached to, or a group they are a member of; or alternatively, to use AWS Organizations to manage permissions.


.. _reference-mobile-hub-project-permissions-model-why:

Why Did the Permissions Model Change?
=====================================

AWS Mobile Hub creates IAM roles and assigns them permissions in order to enable use of AWS resources in mobile apps. Such operations are considered administrative because they include enabling permission to perform operations on resources in the account. Previously, Mobile Hub's service role provided users who have been granted :code:`AWSMobileHub_FullAccess` permissions with a path to escalate their own privileges to act on resources, potentially in ways their administrator did not intend to permit. Removing the service role, removes the path to escalate privileges and puts control of user permissions directly in the hands of the administrator for a |AMH| project.


