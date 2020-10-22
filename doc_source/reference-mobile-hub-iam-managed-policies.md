# Control Access to Mobile Hub Projects<a name="reference-mobile-hub-iam-managed-policies"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

## Overview<a name="overview"></a>

This section describes two different ways to control access to your Mobile Hub projects:
+  [Grant a user administrative account permissions](#reference-mobile-hub-iam-managed-policies-how-to) 

  For individual developers, or groups whose requirements for segmenting access to their Mobile Hub projects are simple, permission can be granted by attaching the managed [AdministratorAccess](#aws-mobile-hub-administrator-access-policy) or [AWSMobileHub\_ReadOnly](#aws-mobile-hub-read-only-access-policy) AWS managed policies to a user, a role they are attached to, or a group they belong to\.

Or:
+  [Use AWS Organizations to manage permissions](#reference-mobile-hub-iam-managed-policies-aws-organizations) 

  For organizations that require fine\-grained access control and cost tracking for their Mobile Hub projects, AWS account administrators can provide sub\-accounts and determine the policies that apply to their users\.


|  | 
| --- |
|  To understand how Mobile Hub uses IAM policies attached to a user to create and modify services on a users behalf, see [Mobile Hub Project Permissions Model](reference-mobile-hub-project-permissions-model.md)\. To understand AWS Identity and Access Management \(IAM\) in more detail, see [IAM Authentication and Access Control for Mobile Hub](reference-mobile-hub-iam-auth-access.md) and [IAM Authentication and Access Control for Mobile Hub](reference-mobile-hub-iam-auth-access.md)\.  | 

## Best Practice: Create IAM Users to Access AWS<a name="aws-account-security-recommendations"></a>

To provide better security, we recommend that you do not use your AWS root account to access Mobile Hub\. Instead, create an AWS Identity and Access Management \(IAM\) user in your AWS account, or use an existing IAM user, and then access Mobile Hub with that user\. For more information, see [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) in the AWS General Reference\.

You can create an IAM user for yourself or a delegate user using the IAM console\. First, create an IAM administrator group, then create and assign a new IAM user to that group\.

**Note**  
Before any IAM user within an account can create a mobile Hub project, a user with administrative privileges for the account must navigate to the [Mobile Hub console](https://console.aws.amazon.com/mobilehub/) and create an initial project\. This step provides confirmation that Mobile Hub can manage AWS services on your behalf\.  
To learn more about assigning access rights to IAM users or groups, see [IAM Authentication and Access Control for Mobile Hub](reference-mobile-hub-iam-auth-access.md)\.

## Grant Users Permissions to Mobile Hub Projects<a name="reference-mobile-hub-iam-managed-policies-how-to"></a>

**Topics**
+ [Create a New IAM User in Your Account and Grant Mobile Hub Permissions](#reference-mobile-hub-iam-managed-policies-new-user)
+ [Create an IAM Group](#create-an-iam-group)
+ [Grant Mobile Hub Permissions to an Existing Account User](#reference-mobile-hub-iam-managed-policies-existing-user)

Use the following steps to create a group and/or users, and grant users access to your Mobile Hub projects\.

To grant permissions to a role, see [Adding Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#w2ab1c19c19c26b9) in the *AWS IAM User Guide*\.

### Create a New IAM User in Your Account and Grant Mobile Hub Permissions<a name="reference-mobile-hub-iam-managed-policies-new-user"></a>

1. Open the [IAM console](https://console.aws.amazon.com/iam/)\. On the left, choose **Users**, and then choose **Add User**\.

1. Type a user name, select the check boxes for **Programmatic access** and **AWS Management Console access**\.

1. Choose the password policy you prefer\. Then choose **Next: Permissions**\.

1. In the **Add user to group** tab, select the **Administrators** or **Read\_Only** group for the user, and choose **Next, Review**\.

   In the process, you will see options to customize the user’s password, alert them about their new account via email, and to download their access key ID, key value and password\.

1. Choose **Create user**\.

1. To apply policy:
   + If you have created a group to manage project permissions, choose **Add user to group**, select the group, choose **Next: Review**, then choose **Create User**\.

   Or:
   + If you are managing project permissions per user, choose **Attach existing policies directly**, select the policy you want to attach, **AdministratorAccess** or **AWSMobileHub\_ReadOnly**, and then choose **Create user**\.

### Create an IAM Group<a name="create-an-iam-group"></a>

1. Sign in to the AWS Management Console and open the IAM console at [http://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane, choose **Groups**, and then choose **Create New Group**\.

1. For **Group Name**, type a name for your group, such as `Administrators` or `Read_Only`, and then choose **Next Step**\.

1. In the list of policies, select the check box next to the **AdministratorAccess** policy to grant full permissions to the group, or **AWSMobileHub\_ReadOnly** to grant only read access\. You can use the **Filter** menu and the **Search** box to filter the list of policies\.

1. Choose **Next Step**, and then choose **Create Group**\. Your new group is listed under **Group Name**\.

### Grant Mobile Hub Permissions to an Existing Account User<a name="reference-mobile-hub-iam-managed-policies-existing-user"></a>

1. On the left, choose **Policies**\.

1. Choose the link for the managed policy, **AdministratorAccess** or **AWSMobileHub\_ReadOnly** you want to attach\.

1. Choose **Attached Entities**\.

1. Choose **Attach**\.

1. Choose the users, roles, or groups you want to grant permissions\.

1. Choose **Attach Policy**\.

## Use AWS Organizations to Manage Permissions<a name="reference-mobile-hub-iam-managed-policies-aws-organizations"></a>

 [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) can be used to manage permissions for groups that need to segment access to their Mobile Hub projects\. For example, an administrator could provide an account for each developer on a team\. Within their own account, each user would have the permissions granted by the administrator\. The steps to achieve this would be:

1. If you do not have an AWS account, [sign up for the AWS Free Tier](https://aws.amazon.com/free/)\.

1. Create an organization in the [AWS Organizations console](https://console.aws.amazon.com/organizations/)\.

1. Create or add existing accounts for each user in the organization\.

1. Invite the users\.

1. Create a organizational unit for the developers\.

1. Enable and attach a policy for members of the unit\.

   The policy you attach will apply within the scope of the AWS account of a user\. You may want to limit access to services and capabilities not required for Mobile Hub use\. For instance, the following policy, grants all permissions defined in the `FullAWSAccess` managed policy, but excludes access to the Amazon EC2 service\.

   ```
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
   ```

For step by step instructions, see the tutorial at [Creating and Managing an AWS Organization](https://alpha-docs-aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)\.

## AWS Managed \(Predefined\) Policies for Mobile Hub Project Access<a name="mobilehub-policies"></a>

The AWS Identity and Access Management service controls user permissions for AWS services and resources\. Specific permissions are required in order to view and modify configuration for any project with AWS Mobile Hub\. These permissions have been grouped into the following managed policies, which you can attach to an IAM user, role, or group\.<a name="aws-mobile-hub-administrator-access-policy"></a>
+  **AdministratorAccess** 

  This policy provides unlimited access to AWS services in the account\. That includes read and write access to AWS Mobile Hub projects\. Users with this policy attached to their IAM user, role, or group are allowed to create new projects, modify configuration for existing projects, and delete projects and resources\. This policy also includes all of the permissions that are allowed under the `AWSMobileHub_ReadOnly` managed policy\. After you sign in to the Mobile Hub console and create a project, you can use the following link to view this policy and the IAM identities that are attached to it\.
  +  [https://console\.aws\.amazon\.com/iam/home?region=us\-east\-1\#/policies/arn:aws:iam::aws:policy/AdministratorAccess$jsonEditor](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AdministratorAccess$jsonEditor) <a name="aws-mobile-hub-read-only-access-policy"></a>
+  **AWSMobileHub\_ReadOnly** 

  This policy provides read\-only access to AWS Mobile Hub projects\. Users with this policy attached to their IAM user, role, or group are allowed to view project configuration and generate sample quick start app projects that can be downloaded and built on a developer’s desktop \(e\.g\., in Android Studio or Xcode\)\. This policy does not allow modification to Mobile Hub project configuration, and it does not allow the user to enable the use of AWS Mobile Hub in an account where it has not already been enabled\. After you sign in to the Mobile Hub console and create a project, you can use the following link to view this policy and the IAM identities that are attached to it\.
  +  [http://console\.aws\.amazon\.com/iam/home?region=us\-east\-1\#policies/arn:aws:iam::aws:policy/AWSMobileHub\_ReadOnly](https://console.aws.amazon.com/iam/home?region=us-east-1#policies/arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly) 

  If your IAM user, role, or group has read\-only permissions for use in an AWS Mobile Hub project, then the project information you see in the console will not reflect any changes made outside of Mobile Hub\. For example, if you remove a Cloud Logic API in API Gateway, it may still be present in the Cloud Logic Functions list of your Mobile Hub project, until a user with **mobilehub:SynchronizeProject** permissions visits the console\. Users who are granted console access through the **AdminstratorAccess** policy have those permissions\. If you need additional permissions in Mobile Hub, please contact your administrator and request the **AdminstratorAccess** policy\.