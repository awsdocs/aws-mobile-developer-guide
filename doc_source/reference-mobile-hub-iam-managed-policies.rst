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


This section describes how to control access to your projects using the
:guilabel:`AWSMobileHub_FullAccess` and :guilabel:`AWSMobileHub_ReadOnly` AWS managed policies
provided by |AMH|.

To understand how |AMH| uses |IAM| policies attached to the :guilabel:`MobileHub_Service_Role` to
create and modify services on your behalf, see :ref:`reference-mobile-hub-iam-service-role`.

To understand |IAMlong| (|IAM|) in more detail, see :ref:`reference-mobile-hub-iam-auth-access` and
:ref:`reference-mobile-hub-iam-auth-access`.

.. _aws-account-security-recommendations:

Create an IAM User for Better AWS Account Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


To provide better security, we recommend that you do not use your AWS root account to access |AMH|.
Instead, create an |IAMlong| (|IAM|) user, or use an existing |IAM| user, in your AWS account and
then access |AMH| with that user. For more information, see `AWS Security Credentials
<http://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`_ in the AWS General Reference.

If you signed up for AWS but have not created an |IAM| user for yourself, you can create one by
using the |IAM| console. First, create an |IAM| administrator group, then create and assign a new
|IAM| user to that group.

.. note:: Before any |IAM| user within an account can create a mobile Hub project, a user with
   administrative privileges for the account must navigate to the `Mobile Hub console
   <https://console.aws.amazon.com/mobilehub/>`_ and create an initial project. This step provides
   confirmation that |AMH| can manage AWS services on your behalf.

   To learn more about assigning access rights to |IAM| users or groups, see
   :ref:`reference-mobile-hub-iam-auth-access`.


**To create an |IAM| administrators group**

#. Sign in to the AWS Management Console and open the |IAM| console at
   `http://console.aws.amazon.com/iam/ <https://console.aws.amazon.com/iam/>`_

#. In the navigation pane, choose :guilabel:`Groups`, and then choose :guilabel:`Create New Group`.

#. For :guilabel:`Group Name`, type a name for your group, such as :guilabel:`Administrators`, and
   then choose :guilabel:`Next Step`.

#. In the list of policies, select the check box next to the :guilabel:`AdministratorAccess` policy.
   You can use the :guilabel:`Filter` menu and the :guilabel:`Search` box to filter the list of
   policies.

#. Choose :guilabel:`Next Step`, and then choose :guilabel:`Create Group`. Your new group is listed
   under :guilabel:`Group Name`.

The following procedure describes how to create an |IAM| user for yourself, add the user to the
administrators group, and create a password for the user.


**To add an |IAM| user to your group and assign a password**

#. In the navigation pane, choose :guilabel:`Users`, and then choose :guilabel:`Create New Users`.

#. In box :guilabel:`1`, type a user name. Clear the check box next to :guilabel:`Generate an access
   key for each user`. Then choose :guilabel:`Create`.

#. In the list of users, choose the name (not the check box) of the user you just created. You can
   use the :guilabel:`Search` box to search for the user name.

#. In the :guilabel:`Groups` section, choose :guilabel:`Add User to Groups`.

#. Select the check box next to the administrators group. Then choose :guilabel:`Add to Groups`.

#. Scroll down to the :guilabel:`Security Credentials` section. Under :guilabel:`Sign-In
   Credentials`, choose :guilabel:`Manage Password`.

#. Select :guilabel:`Assign a custom password`. Then type a password in the :guilabel:`Password` and
   :guilabel:`Confirm Password` boxes. When you are finished, choose :guilabel:`Apply`.


.. _mobilehub-policies:

AWS Managed (Predefined) Policies for |AMH| Project Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |IAMlong| service controls user permissions for AWS services and resources. Specific permissions
are required in order to view and modify configuration for any project with |AMHlong|. These
permissions have been grouped into the following managed policies, which you can attach to an |IAM|
user, role, or group.

* **AWSMobileHub_FullAccess**

  This policy provides read and write access to |AMHlong| projects. Users with this policy attached
  to their |IAM| user, role, or group are allowed to create new projects, modify configuration for
  existing projects, and delete projects and resources. This policy also includes all of the
  permissions that are allowed under the :code:`AWSMobileHub_ReadOnly` managed policy. After you
  sign in to the Mobile Hub console and create a project, you can use the following link to view
  this policy and the IAM identities that are attached to it.

  `http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_FullAccess
  <http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_FullAccess>`_

* **AWSMobileHub_ReadOnly**

  This policy provides read-only access to |AMHlong| projects. Users with this policy attached to
  their |IAM| user, role, or group are allowed to view project configuration and generate sample
  quick start app projects that can be downloaded and built on a developer's desktop (e.g., in
  Android Studio or Xcode). This policy does not allow modification to |AMH| project configuration,
  and it does not allow the user to enable the use of |AMHlong| in an account where it has not
  already been enabled. After you sign in to the Mobile Hub console and create a project, you can
  use the following link to view this policy and the IAM identities that are attached to it.

  `http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly
  <http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly>`_


.. _console-readonly:

Viewing the Mobile Hub Console with Read-only Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your |IAM| user, role, or group has read-only permissions for use in an |AMHlong| project, then
the project information you see in the console will not reflect any changes made outside of |AMH|.
For example, if you remove a Cloud Logic API in |ABP|, it may still be present in the Cloud Logic
Functions list of your |AMH| project, until a user with :code:`mobilehub:SynchronizeProject`
permissions visits the console. Users who are granted console access through the
:code:`AWSMobileHub_FullAccess` policy have those permissions. If you need additional permissions in
Mobile Hub, please contact your administrator and request the Full Access policy.


.. _attach-managed-policy:

Attaching a Managed Policy to a User, Role, or Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use these managed policies, a user with administrative privileges must attach one of them to a
user, role or group in the |IAMlong| console.


**To attach a managed policy**

#. Choose the link for the managed policy you want to attach.

   * `http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_FullAccess
     <https://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_FullAccess>`_
   * `http://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly
     <https://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly>`_

#. Choose :guilabel:`Attached Entities`.

#. Choose :guilabel:`Attach`.

#. Choose the users, roles, or groups you want to grant permissions.

#. Choose :guilabel:`Attach Policy`.
