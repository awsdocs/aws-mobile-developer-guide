.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-mobile-hub-iam-access-control:

############################################################
Overview of Access Permissions Management for |AMH| Projects
############################################################

In depth understanding of AWS authentication and access controls is not required to build a mobile
app using |AMHlong|.

Every AWS resource is owned by an AWS account, and permissions to create or access the resources are
governed by permissions policies. This includes:


* Policies for :ref:`reference-mobile-hub-iam-managed-policies`.

* AWS :ref:`reference-mobile-hub-iam-service-role` to create and configure the back-end features you select for
  your mobile app.

An account administrator can attach permissions policies to |IAM| identities (that is, users,
groups, and roles), and some services (such as |LAMlong|) also support attaching permissions
policies to resources.

.. note:: An :emphasis:`account administrator` (or administrator user) is a user with administrator
   privileges. For more information, see `IAM Best Practices <http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>`_ in the
   :title:`IAM User Guide`.

   When granting permissions, you decide who is getting the permissions, the resources they get
   permissions for, and the specific actions that you want to allow on those resources.


.. contents::
   :local:
   :depth: 1

.. _resource-ownership:

Understanding Resource Ownership for |AMHlong|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The primary resource of a |AMH| project is the project itself. In first use of the |AMH| console,
you allow |AMH| to manage permissions and access the project resource for you. A resource owner is
the AWS account that created a resource. That is, the resource owner is the AWS account of the
principal entity (the root account, an |IAM| user, or an |IAM| role) that authenticates the request
that creates the resource. The following examples illustrate how this works:


* If you use the root account credentials of your AWS account to create an |AMHlong| project, your
  AWS account is the owner of the resources associated with that project.

* If you create an |IAM| user in your AWS account and grant permissions to create |AMH| projects to
  that user, the user can also create projects. However, your AWS account, to which the user
  belongs, owns the resources associated with the project.

* If you create an |IAM| role in your AWS account with permissions to create |AMHlong| projects,
  anyone who can assume the role can create, edit, or delete projects. Your AWS account, to which
  the role belongs, owns the resources associated with that project.


.. _managing-access:

Managing Access to Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


A :emphasis:`permissions policy` describes who has access to what. The following section explains
the available options for creating permissions policies.

.. note::

   This section discusses using |IAM| in the context of |AMHlong|. It doesn't provide
   detailed information about the |IAM| service. For complete |IAM| documentation, see
   `What Is IAM? <http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>`_
   in the :title:`IAM User Guide`. For information about |IAM|
   policy syntax and descriptions, see `AWS Identity and Access Management Policy Reference
   <http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html>`_ in the :title:`IAM User Guide`.

Policies attached to an |IAM| identity are referred to as identity-based policies (|IAM| polices)
and policies attached to a resource are referred to as resource-based policies.


.. contents::
   :local:
   :depth: 1

.. _identity-based-policies:

Identity-Based Policies (|IAM| Policies)
""""""""""""""""""""""""""""""""""""""""


You can attach policies to |IAM| identities. For example, you can do the following:


* **Attach a permissions policy to a user or a group in your account**? An account
  administrator can use a permissions policy that is associated with a particular user to grant
  permissions for that user to view or modify an |AMHlong| project.

* **Attach a permissions policy to a role (grant cross-account permissions)** ? You can
  attach an identity-based permissions policy to an |IAM| role to grant cross-account permissions.
  For example, when you first enter |AMH| and agree, as account principal, to grant it permissions
  to provision and configure your project, you are granting the AWS managed
  :code:`MobileHub_Service_Role` role cross-account permissions. An AWS managed policy,
  :code:`AWSMobileHub_ServiceUseOnly`, is attached to that role in the context of your |AMH|
  project. The role has a trust policy that allows |AMH| to act as account principal with the
  ability to grant permissions for services and resources used by your project.

  For more information about using |IAM| to delegate permissions, see `Access Management
  <http://docs.aws.amazon.com/IAM/latest/UserGuide/access.html>`_ in the :title:`IAM User Guide`.

As an example of using an identity-based policy, the following policy grants permissions to a user
to create an |S3| bucket. A user with these permissions can create a storage location using the |S3|
service.

.. code-block:: json

    {
           "Version":"2012-10-17",
           "Statement":[
              {
                 "Effect":"Allow",
                 "Action":"s3:CreateBucket*",
                 "Resource":"*"
              }
           ]
        }

For more information about using identity-based policies with |AMH| , see :ref:`reference-mobile-hub-iam-managed-policies`
and :ref:`reference-mobile-hub-iam-service-role`.

For more information about users, groups, roles, and permissions, see `Identities (Users, Groups,
and Roles) <http://docs.aws.amazon.com/IAM/latest/UserGuide/id.html>`_ in the :title:`IAM User Guide`.


.. _resource-based-policies:

Resource-Based Policies
"""""""""""""""""""""""


Other services, such as |S3|, also support resource-based permissions policies. For example, you can
attach a policy to an |S3| bucket to manage access permissions to that bucket.



.. _policy-elements:

Specifying Policy Elements: Actions, Effects, Resources, and Principals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Each service that is configured by |AMH| defines a set of API operations. To grant |AMH| permissions
for these API operations, a set of actions is specified in an AWS managed policy. Performing an API
operation can require permissions for more than one action.

The following are the basic policy elements:


* **Resource** - In a policy, you use an Amazon Resource Name (ARN) to identify the resource
  to which the policy applies.

* **Action** - You use action keywords to identify resource operations that you want to
  allow or deny. For example, the :code:`s3:Createbucket` permission allows |AMH| to perform the
  |S3| :code:`CreateBucket` operation.

* **Effect** - You specify the effect when the user requests the specific action?this can be
  either allow or deny. If you don't explicitly grant access to (allow) a resource, access is
  implicitly denied. You can also explicitly deny access to a resource, which you might do to make
  sure that a user cannot access it, even if a different policy grants access.

* **Principal** - In identity-based policies (|IAM| policies), the user that the policy is
  attached to is the implicit principal. For resource-based policies, you specify the user, account,
  service, or other entity that you want to receive permissions (applies to resource-based policies
  only).


