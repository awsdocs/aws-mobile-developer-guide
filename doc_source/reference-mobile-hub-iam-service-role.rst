.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-mobile-hub-iam-service-role:

###################################################
|AMH| Service Role and Policies Used on Your Behalf
###################################################


The following section describes the :code:`MobileHub_Service_Role` |IAM| role that allows |AMH| to
create and modify your AWS resources and services for the project you configure.

To understand how to grant and restrict permissions to your projects in the |AMH| console, see
:ref:`reference-mobile-hub-iam-managed-policies`.

To understand |IAMlong| in more detail, see :ref:`reference-mobile-hub-iam-auth-access` and
:ref:`reference-mobile-hub-iam-auth-access`.


.. contents::
   :local:
   :depth: 1

.. _permissions-source:

Source of |AMH| Service Role Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


|AMHlong| provides an integrated console experience in which you select mobile back-end features you
can access from a mobile app. When you select and enable a feature, |AMH| configures multiple AWS
services and resources on your behalf. Configuring AWS service or resource requires your permission
to allow |AMH| to manage AWS services and resources for you. When you agree to the |AMH| console
one-time request to manage AWS resources and services for you, you are giving |AMH| permissions that
allow it to create a pre-defined |IAM| administrative service role, called
:code:`MobileHub_Service_Role`.

After this service role is created, you can see it at
`http://console.aws.amazon.com/iam/home?region=us-east-1#roles/MobileHub_Service_Role
<https://console.aws.amazon.com/iam/home?region=us-east-1#roles/MobileHub_Service_Role>`_.


.. _service-role-trust-relationship:

Trust Relationship
~~~~~~~~~~~~~~~~~~


In the |IAM| console at
`http://console.aws.amazon.com/iam/home?region=us-east-1#roles/MobileHub_Service_Role
<https://console.aws.amazon.com/iam/home?region=us-east-1#roles/MobileHub_Service_Role>`_, there is a section for the trust
relationship. The trust relationship dictates which entities can assume this role and make use of
its permissions. The trust relationship for this service role has an access control policy that
looks like this:

.. code-block:: json

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {
                    "Service": "mobilehub.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

This access control policy dictates that only |AMHlong| (:code:`mobilehub.amazonaws.com`) can assume
this role. This policy should not be modified. No other user or system can assume this role and use
its permissions.


.. _service-role-admin-privileges:

Administrative Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~


By allowing |AMH| to create and assume the :code:`MobileHub_Service_Role` role, you give |AMH|
permissions to create additional roles as necessary to support the features enabled in your project.
The :code:`MobileHub_Service_Role` gives |AMH| permission to enable any service policies necessary
on these additional roles for proper operation of the mobile app.

There are no limits on the number or scope of service policies or roles |AMH| may create. Actions
taken by |AMH| in this regard are always in response to your actions in the |AMH| console. Roles or
policies are never created without direct action from you, such as creating a |AMH| project or
configuring an app feature.

.. _revoking-privileges:

Revoking Privileges
"""""""""""""""""""


To disallow |AMH| access to any users of your account, delete the :code:`MobileHub_Service_Role`
role. Make sure your users don't have permission to re-create the role, for example by having the
:code:`IAM:CreateRole` permission.



.. _service-role-service-policy:

Service Policy
~~~~~~~~~~~~~~


The service policy states which operations an entity that assumes the :code:`MobileHub_Service_Role`
role can perform. The role is created for your account when you agree to allow |AMH| to manage
permissions on your behalf. The following JSON is a reproduction of the policy. You can also view
the source at `http://console.aws.amazon.com/iam/home?region=us-east-1#roles/MobileHub_Service_Role
<https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly$jsonEditor>`_.

.. code-block:: json

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "cloudformation:CreateUploadBucket",
            "cloudformation:ValidateTemplate",
            "cloudfront:CreateDistribution",
            "cloudfront:DeleteDistribution",
            "cloudfront:GetDistribution",
            "cloudfront:GetDistributionConfig",
            "cloudfront:UpdateDistribution",
            "cognito-identity:CreateIdentityPool",
            "cognito-identity:UpdateIdentityPool",
            "cognito-identity:DeleteIdentityPool",
            "cognito-identity:SetIdentityPoolRoles",
            "cognito-idp:CreateUserPool",
            "dynamodb:CreateTable",
            "dynamodb:DeleteTable",
            "dynamodb:DescribeTable",
            "dynamodb:UpdateTable",
            "iam:AddClientIDToOpenIDConnectProvider",
            "iam:CreateOpenIDConnectProvider",
            "iam:GetOpenIDConnectProvider",
            "iam:ListOpenIDConnectProviders",
            "iam:CreateSAMLProvider",
            "iam:GetSAMLProvider",
            "iam:ListSAMLProvider",
            "iam:UpdateSAMLProvider",
            "lambda:CreateFunction",
            "lambda:DeleteFunction",
            "lambda:GetFunction",
            "mobileanalytics:CreateApp",
            "mobileanalytics:DeleteApp",
            "sns:CreateTopic",
            "sns:DeleteTopic",
            "sns:ListPlatformApplications",
            "ec2:DescribeSecurityGroups",
            "ec2:DescribeSubnets",
            "ec2:DescribeVpcs",
            "lex:PutIntent",
            "lex:GetIntent",
            "lex:GetIntents",
            "lex:PutSlotType",
            "lex:GetSlotType",
            "lex:GetSlotTypes",
            "lex:PutBot",
            "lex:GetBot",
            "lex:GetBots",
            "lex:GetBotAlias",
            "lex:GetBotAliases"
          ],
          "Resource": [
            "*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "sns:CreatePlatformApplication",
            "sns:DeletePlatformApplication",
            "sns:GetPlatformApplicationAttributes",
            "sns:SetPlatformApplicationAttributes"
          ],
          "Resource": [
            "arn:aws:sns:*:*:app/*_MOBILEHUB_*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:CreateBucket",
            "s3:DeleteBucket",
            "s3:DeleteBucketPolicy",
            "s3:ListBucket",
            "s3:ListBucketVersions",
            "s3:GetBucketLocation",
            "s3:GetBucketVersioning",
            "s3:PutBucketVersioning"
          ],
          "Resource": [
            "arn:aws:s3:::*-userfiles-mobilehub-*",
            "arn:aws:s3:::*-contentdelivery-mobilehub-*",
            "arn:aws:s3:::*-deployments-mobilehub-*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:DeleteObject",
            "s3:DeleteVersion",
            "s3:DeleteObjectVersion",
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:PutObject",
            "s3:PutObjectAcl"
          ],
          "Resource": [
            "arn:aws:s3:::*-userfiles-mobilehub-*/*",
            "arn:aws:s3:::*-contentdelivery-mobilehub-*/*",
            "arn:aws:s3:::*-deployments-mobilehub-*/*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "lambda:AddPermission",
            "lambda:CreateAlias",
            "lambda:DeleteAlias",
            "lambda:UpdateAlias",
            "lambda:GetFunctionConfiguration",
            "lambda:GetPolicy",
            "lambda:RemovePermission",
            "lambda:UpdateFunctionCode",
            "lambda:UpdateFunctionConfiguration"
          ],
          "Resource": [
            "arn:aws:lambda:*:*:function:*-mobilehub-*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "iam:CreateRole",
            "iam:DeleteRole",
            "iam:DeleteRolePolicy",
            "iam:GetRole",
            "iam:GetRolePolicy",
            "iam:ListRolePolicies",
            "iam:PassRole",
            "iam:PutRolePolicy",
            "iam:UpdateAssumeRolePolicy",
            "iam:AttachRolePolicy",
            "iam:DetachRolePolicy"
          ],
          "Resource": [
            "arn:aws:iam::*:role/*_unauth_MOBILEHUB_*",
            "arn:aws:iam::*:role/*_auth_MOBILEHUB_*",
            "arn:aws:iam::*:role/*_consolepush_MOBILEHUB_*",
            "arn:aws:iam::*:role/*_lambdaexecutionrole_MOBILEHUB_*",
            "arn:aws:iam::*:role/*_smsverification_MOBILEHUB_*",
            "arn:aws:iam::*:role/*_botexecutionrole_MOBILEHUB_*",
            "arn:aws:iam::*:role/pinpoint-events",
            "arn:aws:iam::*:role/MOBILEHUB-*-lambdaexecution*",
            "arn:aws:iam::*:role/MobileHub_Service_Role"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "iam:CreateServiceLinkedRole",
            "iam:GetRole"
          ]
          "Resource": [
            "arn:aws:iam::*:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [        "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource": [
            "arn:aws:logs:*:*:log-group:/aws/mobilehub/*:log-stream:*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "iam:ListAttachedRolePolicies"
          ],
          "Resource": [
            "arn:aws:iam::*:role/MobileHub_Service_Role"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "cloudformation:CreateStack",
            "cloudformation:DeleteStack",
            "cloudformation:DescribeStacks",
            "cloudformation:DescribeStackEvents",
            "cloudformation:DescribeStackResource",
            "cloudformation:GetTemplate",
            "cloudformation:ListStackResources",
            "cloudformation:UpdateStack"
          ],
          "Resource": [
            "arn:aws:cloudformation:*:*:stack/MOBILEHUB-*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "apigateway:DELETE",
            "apigateway:GET",
            "apigateway:HEAD",
            "apigateway:OPTIONS",
            "apigateway:PATCH",
            "apigateway:POST",
            "apigateway:PUT"
          ],
          "Resource": [
            "arn:aws:apigateway:*::/restapis*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "cognito-idp:DeleteUserPool",
            "cognito-idp:DescribeUserPool",
            "cognito-idp:CreateUserPoolClient",
            "cognito-idp:DescribeUserPoolClient",
            "cognito-idp:DeleteUserPoolClient"
          ],
          "Resource": [
            "arn:aws:cognito-idp:*:*:userpool/*"
          ]
        },
        {
          "Effect": "Allow",
          "Action": [
            "mobiletargeting:UpdateApnsChannel",
            "mobiletargeting:UpdateApnsSandboxChannel",
            "mobiletargeting:UpdateEmailChannel",
            "mobiletargeting:UpdateGcmChannel",
            "mobiletargeting:UpdateSmsChannel",
            "mobiletargeting:DeleteApnsChannel",
            "mobiletargeting:DeleteApnsSandboxChannel",
            "mobiletargeting:DeleteEmailChannel",
            "mobiletargeting:DeleteGcmChannel",
            "mobiletargeting:DeleteSmsChannel"
          ],
          "Resource": [
            "arn:aws:mobiletargeting:*:*:apps/*/channels/*"
          ]
        }
          ]
    }

All of these permissions pertain to resources |AMH| creates on your behalf. You can see these
resources by choosing :guilabel:`Resources` in the left navigation panel of the |AMH| console.

.. _service-role-iam:

|IAMlong| (IAM)
"""""""""""""""


These are the items in the service policy for the |AMH| service role defining |IAM| permissions.

.. code-block:: json

    "iam:CreateRole",
    "iam:DeleteRole",
    "iam:DeleteRolePolicy",
    "iam:GetRole",
    "iam:ListRolePolicies",
    "iam:PassRole",
    "iam:PutRolePolicy",
    "iam:UpdateAssumeRolePolicy",
    "iam:AttachRolePolicy",
    "iam:DetachRolePolicy"

|AMH| creates one or more |IAM| roles to use with your mobile app project, depending on the
configuration options you choose for each feature. By default, |IAM| creates an unauthenticated app
user role to allow users of your app to get temporary permissions to perform various operations with
other services you've enabled. For example, you need this role when your app calls an |LAMlong|
function in the Cloud Logic feature.

If you enable the Cloud Logic feature, |AMH| also creates an |LAMlong| execution role. This role
provides your |LAMlong| functions the permissions they need to carry out their tasks; for example,
writing debug logs to |CWlong|.

If you enable the User Sign-in feature, |AMH| creates an authenticated app user role. When users of
your app sign in using a sign-in provider such as Facebook or Google+, their temporary credentials
are assigned the authenticated role. If you select the :guilabel:`Sign-in is required` option in
User Sign-in, the unauthenticated app user role is removed. All access to your resources from the
app then require use of the authenticated role.

When you use the SAML Federation feature for user authentication, |AMH| uses |IAM| SAML Provider
permissions.

.. code-block:: json

    "iam:CreateSAMLProvider",
    "iam:GetSAMLProvider",
    "iam:ListSAMLProvider",
    "iam:UpdateSAMLProvider"

In addition, if you select Google as a sign-in provider, |AMH| needs access to the following Open ID
Connect Provider APIs from IAM:

.. code-block:: json

    "iam:AddClientIDToOpenIDConnectProvider",
    "iam:CreateOpenIDConnectProvider",
    "iam:GetOpenIDConnectProvider",
    "iam:ListOpenIDConnectProviders",

These permissions allow the service to create an Open ID Connect Provider for Google if it does not
already exist, and add ClientIDs to that provider.

If you enable the Conversational Bots feature, Mobile Hub uses the following permissions to create
and access a role that allows the Amazon Lex Service to generate speech by communicating with the
Amazon Polly service.

.. code-block:: json

    "iam:CreateServiceLinkedRole",
    "iam:GetRole"


.. _service-role-api-gateway:

|ABPlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |ABP| permissions.

.. code-block:: json

    "apigateway:DELETE",
    "apigateway:GET",
    "apigateway:PATCH",
    "apigateway:POST",
    "apigateway:PUT",
    "apigateway:HEAD",
    "apigateway:OPTIONS"

These policies enable |AMH| to configure REST APIs for mobile back-ends.


.. _service-role-cognito:

|COGlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |COG| permissions.

.. code-block:: json

    "cognito-identity:CreateIdentityPool",
    "cognito-identity:UpdateIdentityPool",
    "cognito-identity:DeleteIdentityPool",
    "cognito-identity:SetIdentityPoolRoles",
    "cognito-idp:CreateUserPool",
    "cognito-idp:DeleteUserPool",
    "cognito-idp:DescribeUserPool,
    "cognito-idp:CreateUserPoolClient",
    "cognito-idp:DescribeUserPoolClient",
    "cognito-idp:DeleteUserPoolClient""

|COGlong| provides temporary credentials that give app users access to your AWS resources. By
default |AMH| creates an |COG| identity pool to provide a scope or namespace for user identities. If
you enable the User Sign-in feature and configure a sign-in provider, such as Facebook or Google+,
|AMH| updates the identity pool to support that feature in your app.


.. _service-role-cloudformation:

|CFNlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |CFN| permissions.

.. code-block:: json

    "cloudformation:CreateUploadBucket",
    "cloudformation:ValidateTemplate",
    "cloudformation:CreateStack",
    "cloudformation:ListStackResources",
    "cloudformation:DeleteStack",
    "cloudformation:DescribeStacks",
    "cloudformation:DescribeStackEvents",
    "cloudformation:DescribeStackResource",
    "cloudformation:GetTemplate",
    "cloudformation:UpdateStack"

These policies allow |AMH| to dynamically provision and configure back-end stacks to support your
mobile app's requirements.


.. _service-role-cloudfront:

|CFlong|
""""""""


These are the items in the service policy for the |AMH| service role defining |CF| permissions.

.. code-block:: json

    "cloudfront:CreateDistribution",
    "cloudfront:DeleteDistribution",
    "cloudfront:GetDistribution",
    "cloudfront:GetDistributionConfig",
    "cloudfront:UpdateDistribution",

If you enable the App Content Delivery feature and configure it for Multi-Region CDN, |AMH| creates
a |CF| distribution with your |S3| bucket set as the origin.


.. _service-role-dynamodb:

|DDBlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |DDB| permissions.

.. code-block:: json

    "dynamodb:CreateTable",
    "dynamodb:DeleteTable",
    "dynamodb:DescribeTable",
    "dynamodb:UpdateTable"


.. _service-role-ec2:

|EC2long|
"""""""""


These are the items in the service policy for the |AMH| service role defining |EC2| permissions.

.. code-block:: json

    "ec2:DescribeSecurityGroups",
    "ec2:DescribeSubnets",
    "ec2:DescribeVpcs"


.. _service-role-lambda:

|LAMlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |LAM| permissions.

.. code-block:: json

    "lambda:AddPermission",
    "lambda:CreateFunction",
    "lambda:DeleteFunction",
    "lambda:GetFunction",
    "lambda:CreateAlias",
    "lambda:DeleteAlias",
    "lambda:GetFunctionConfiguration",
    "lambda:GetPolicy",
    "lambda:UpdateFunctionCode",
    "lambda:UpdateAlias",
    "lambda:UpdateFunctionConfiguration"

If you enable the Cloud Logic or Connector features, |AMH| creates an example |LAM| function. You
can use this function to demonstrate invocation of a |LAM| function from your app.


.. _service-role-lex:

|LEXlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |LEXlong| permissions.

.. code-block:: json

    "lex:PutIntent",
    "lex:GetIntent",
    "lex:GetIntents",
    "lex:GetSlotType",
    "lex:PutSlotType",
    "lex:GetSlotTypes",
    "lex:PutBot",
    "lex:GetBot",
    "lex:GetBots",
    "lex:GetBotAlias",
    "lex:GetBotAliases"

These policies enable |AMH| to configure instances of the Conversation Bots feature. Note that when
you enable this feature, Mobile Hub uses the following |IAM| permissions to create and access a role
that allows the Amazon Lex Service to generate speech by communicating with the Amazon Polly
service.

.. code-block:: json

    "iam:CreateServiceLinkedRole",
    "iam:GetRole"


.. _service-role-pinpoint:

Amazon Pinpoint
"""""""""""""""


These are the items in the service policy for the |AMH| service role defining Amazon Pinpoint permissions.

The Amazon Pinpoint service, which links app analytics to user messaging campaigns, can activate other
services. When you enable the Messaging and Analytics feature, |AMH| uses the following permissions
for the |MA| service.

.. code-block:: json

    "mobileanalytics:CreateApp",
    "mobileanalytics:DeleteApp",

When you enable the Messaging options of the feature, |AMH| uses the following permissions to
configure Amazon Pinpoint.

.. code-block:: json

    "mobiletargeting:UpdateApnsChannel",
    "mobiletargeting:UpdateApnsSandboxChannel",
    "mobiletargeting:UpdateEmailChannel",
    "mobiletargeting:UpdateGcmChannel",
    "mobiletargeting:UpdateSmsChannel",
    "mobiletargeting:DeleteApnsChannel",
    "mobiletargeting:DeleteApnsSandboxChannel",
    "mobiletargeting:DeleteEmailChannel",
    "mobiletargeting:DeleteGcmChannel",
    "mobiletargeting:DeleteSmsChannel"


.. _service-role-sns:

|SNSlong|
"""""""""


These are the items in the service policy for the |AMH| service role defining |SNS| permissions.

.. code-block:: json

    "sns:CreateTopic",
    "sns:DeleteTopic",
    "sns:CreatePlatformApplication",
    "sns:DeletePlatformApplication",
    "sns:GetPlatformApplicationAttributes",
    "sns:SetPlatformApplicationAttributes",
    "sns:ListPlatformApplications"

When you enable the Push Notifications feature, |AMH| creates an |SNS| platform application for each
push platform you configure. It also creates a default |SNS| topic you can use to push messages to
all users of your app. The topic and platform application are deleted if you delete the associated
|AMH| project.


.. _service-role-s3:

|S3long|
""""""""


These are the items in the service policy for the |AMH| service role defining |S3| permissions.

.. code-block:: json

    "s3:CreateBucket",
    "s3:DeleteBucket",
    "s3:DeleteBucketPolicy",
    "s3:ListBucket",
    "s3:ListBucketVersions",
    "s3:DeleteObject",
    "s3:DeleteVersion",
    "s3:PutObject",
    "s3:PutObjectAcl",
    "s3:GetBucketLocation",
    "s3:GetObject",
    "s3:GetObjectVersion",

App Content Delivery and User Data Storage features both use |S3long|. When you enable one of these
features, |AMH| creates an |S3| bucket on your behalf. |AMH| also puts example files and folders in
the bucket so you can demonstrate your app downloading and navigating between folders. Some of these
permissions are required to set up your |S3| bucket for use with |CFlong| if you enable the App
Content Delivery feature and select Multi-Region CDN. Other policies enable storage capabilities
needed by mobile back-end features that use multiple AWS services.

