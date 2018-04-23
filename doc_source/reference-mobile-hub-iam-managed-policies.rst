.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-mobile-hub-iam-managed-policies:

#####################################
Control Access to Mobile Hub Projects
#####################################


Overview
========

This section describes two different ways to control access to your |AMH| projects:

* :ref:`Grant a user administrative account permissions <reference-mobile-hub-iam-managed-policies-how-to>`

  For individual developers, or groups whose requirements for segmenting access to their |AMH| projects are simple, permission can be granted by attaching the managed :ref:`AdministratorAccess <aws-mobile-hub-read-only-access-policy>` or :ref:`AWSMobileHub_ReadOnly <aws-mobile-hub-read-only-access-policy>` AWS managed policies to a user, a role they are attached to, or a group they belong to.

Or:

* :ref:`Use AWS Organizations to manage permissions<reference-mobile-hub-iam-managed-policies-aws-organizations>`

  For organizations that require fine-grained access control and cost tracking for their |AMH| projects, AWS account administrators can provide sub-accounts and determine the policies that apply to their users.

.. list-table::
     :widths: 1

     * - To understand how |AMH| uses |IAM| policies attached to a user to create and modify services on a users behalf, see :ref:`Mobile Hub Project Permissions Model <reference-mobile-hub-project-permissions-model>`.

         To understand |IAMlong| (|IAM|) in more detail, see :ref:`reference-mobile-hub-iam-auth-access` and :ref:`reference-mobile-hub-iam-auth-access`.

.. _aws-account-security-recommendations:

Best Practice: Create IAM Users to Access AWS
=============================================

To provide better security, we recommend that you do not use your AWS root account to access |AMH|.
Instead, create an |IAMlong| (|IAM|) user in your AWS account, or use an existing |IAM| user, and
then access |AMH| with that user. For more information, see `AWS Security Credentials
<http://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`__ in the AWS General Reference.

You can create an |IAM| user for yourself or a delegate user using the |IAM| console. First, create an |IAM| administrator group, then create and assign a new |IAM| user to that group.

.. note:: Before any |IAM| user within an account can create a mobile Hub project, a user with
   administrative privileges for the account must navigate to the `Mobile Hub console
   <https://console.aws.amazon.com/mobilehub/>`__ and create an initial project. This step provides
   confirmation that |AMH| can manage AWS services on your behalf.

   To learn more about assigning access rights to |IAM| users or groups, see
   :ref:`reference-mobile-hub-iam-auth-access`.

.. _reference-mobile-hub-iam-managed-policies-how-to:

Grant Users Permissions to Mobile Hub Projects
==============================================

.. contents::
     :local:
     :depth: 1

Use the following steps to create a group and/or users, and grant users access to your |AMH| projects.

To grant permissions to a role, see `Adding Permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#w2ab1c19c19c26b9>`__ in the *AWS IAM User Guide*.

.. _reference-mobile-hub-iam-managed-policies-new-user:

Create a New |IAM| User in Your Account and Grant |AMH| Permissions
-------------------------------------------------------------------

#. Open the `IAM console <https://console.aws.amazon.com/iam/>`__. On the left, choose :guilabel:`Users`, and then choose :guilabel:`Add User`.

#. Type a user name, select the checkboxes for :guilabel:`Programmatic access` and :guilabel:`AWS Management Console access`.

#. Choose the password policy you prefer. Then choose :guilabel:`Next: Permissions`.

#. In the :guilabel:`Add user to group` tab, select the :guilabel:`Administrators` or :guilabel:`Read_Only` group for the user, and choose :guilabel:`Next, Review`.

   In the process, you will see options to customize the user's password, alert them about their new account via   email, and to download their access key ID, key value and password.

#. Choose :guilabel:`Create user`.

#. To apply policy:

   * If you have created a group to manage project permissions, choose :guilabel:`Add user to group`, select the group, choose :guilabel:`Next: Review`, then choose choose :guilabel:`Create User`.

   Or:

   * If you are managing project permissions per user, choose :guilabel:`Attach existing policies directly`, select the policy you want to attach, :guilabel:`AdministratorAccess` or :guilabel:`AWSMobileHub_ReadOnly`, and then choose :guilabel:`Create user`.

Create an |IAM| Group
---------------------

#. Sign in to the AWS Management Console and open the |IAM| console at
   `http://console.aws.amazon.com/iam/ <https://console.aws.amazon.com/iam/>`__.

#. In the navigation pane, choose :guilabel:`Groups`, and then choose :guilabel:`Create New Group`.

#. For :guilabel:`Group Name`, type a name for your group, such as :userinput:`Administrators` or :userinput:`Read_Only`, and
   then choose :guilabel:`Next Step`.

#. In the list of policies, select the check box next to the :guilabel:`AdministratorAccess` policy to grant full permissions to the group, or :guilabel:`AWSMobileHub_ReadOnly` to grant only read access. You can use the :guilabel:`Filter` menu and the :guilabel:`Search` box to filter the list of
   policies.

#. Choose :guilabel:`Next Step`, and then choose :guilabel:`Create Group`. Your new group is listed
   under :guilabel:`Group Name`.

.. _reference-mobile-hub-iam-managed-policies-existing-user:

Grant |AMH| Permissions to an Existing Account User
---------------------------------------------------

#. On the left, choose :guilabel:`Policies`.

#. Choose the link for the managed policy, :guilabel:`AdministratorAccess` or :guilabel:`AWSMobileHub_ReadOnly` you want to attach.

#. Choose :guilabel:`Attached Entities`.

#. Choose :guilabel:`Attach`.

#. Choose the users, roles, or groups you want to grant permissions.

#. Choose :guilabel:`Attach Policy`.

.. _reference-mobile-hub-iam-managed-policies-aws-organizations:

Use AWS Organizations to Manage Permissions
===========================================

`AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`__ can be used to manage permissions for groups that need to segment access to their |AMH| projects. For example, an administrator could provide an account for each developer on a team. Within their own account, each user would have the permissions granted by the administrator. The steps to acheive this would be:

#. If you do not have an AWS account, `sign up for the AWS Free Tier <https://aws.amazon.com/free/>`__.

#. Create an organization in the `AWS Organizations console <https://console.aws.amazon.com/organizations/>`__.

#. Create or add existing accounts for each user in the organization.

#. Invite the users.

#. Create a organizational unit for the developers.

#. Enable and attach a policy for members of the unit.

   The policy you attach will apply within the scope of the AWS account of a user. You may want to limit access to services and capabilites not required for |AMH| use. For instance, the following policy, grants all permissions defined in the :code:`FullAWSAccess` managed policy, but excludes access to the Amazon EC2 service.

    .. code-block:: json

        "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*"
                },
                {
                    "Effect": “Deny”,
                    "Action": “ec2:*”,
                    "Resource": "*"
                }
        ]

For step by step instructions, see the tutorial at `Creating and Managing an AWS Organization <https://alpha-docs-aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html>`__.

.. _mobilehub-policies:

AWS Managed (Predefined) Policies for |AMH| Project Access
==========================================================

The |IAMlong| service controls user permissions for AWS services and resources. Specific permissions
are required in order to view and modify configuration for any project with |AMHlong|. These
permissions have been grouped into the following managed policies, which you can attach to an |IAM|
user, role, or group.

.. _administrator-access-policy:

* **AdministratorAccess**

  This policy provides unlimited access to AWS services in the account. That includes read and write access to |AMHlong| projects. Users with this policy attached to their |IAM| user, role, or group are allowed to create new projects, modify configuration for existing projects, and delete projects and resources. This policy also includes all of the
  permissions that are allowed under the :code:`AWSMobileHub_ReadOnly` managed policy. After you
  sign in to the Mobile Hub console and create a project, you can use the following link to view
  this policy and the IAM identities that are attached to it.

    *  `https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AdministratorAccess$jsonEditor <https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AdministratorAccess$jsonEditor>`__

.. _aws-mobile-hub-read-only-access-policy:

* **AWSMobileHub_ReadOnly**

  This policy provides read-only access to |AMHlong| projects. Users with this policy attached to
  their |IAM| user, role, or group are allowed to view project configuration and generate sample
  quick start app projects that can be downloaded and built on a developer's desktop (e.g., in
  Android Studio or Xcode). This policy does not allow modification to |AMH| project configuration,
  and it does not allow the user to enable the use of |AMHlong| in an account where it has not
  already been enabled. After you sign in to the Mobile Hub console and create a project, you can
  use the following link to view this policy and the IAM identities that are attached to it.

    * `http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly <http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly>`__

  If your |IAM| user, role, or group has read-only permissions for use in an |AMHlong| project, then the project information you see in the console will not reflect any changes made outside of |AMH|. For example, if you remove a Cloud Logic API in |ABP|, it may still be present in the Cloud Logic Functions list of your |AMH| project, until a user with :guilabel:`mobilehub:SynchronizeProject` permissions visits the console. Users who are granted console access through the :guilabel:`AdminstratorAccess` policy have those permissions. If you need additional permissions in Mobile Hub, please contact your administrator and request the :guilabel:`AdminstratorAccess` policy.



