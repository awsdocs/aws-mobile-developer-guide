# Mobile Hub Project Permissions Model<a name="reference-mobile-hub-project-permissions-model"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

 **Important** 

To modify Mobile Hub projects in an account, a user must be [granted administrative permissions](reference-mobile-hub-iam-managed-policies.md#reference-mobile-hub-iam-managed-policies-how-to) by an account Administrator\. Read this section for more information\.

If you are a user who needs additional permissions for a project, contact an administrator for the AWS account\. For help with any issues related to the new permissions model, contact [aws\-mobilehub\-customer@amazon\.com](mailto:aws-mobilehub-customer@amazon.com?subject=Mobile%20Hub%20project%20permissions)\.

**Topics**
+ [Mobile Hub Permissions Model](#reference-mobile-hub-project-permissions-model-changes)
+ [What if I Currently Use MobileHub\_Service\_Role to Grant Mobile Hub Permissions?](#reference-mobile-hub-project-permissions-model-users)
+ [Why Did the Permissions Model Change?](#reference-mobile-hub-project-permissions-model-why)

## Mobile Hub Permissions Model<a name="reference-mobile-hub-project-permissions-model-changes"></a>

Currently, Mobile Hub’s permissions model uses the user’s permissions directly when they perform operations in the Mobile Hub console or command line interface\. This model provides account administrators fine\-grained access control over what operations their users can perform in the account, regardless of whether they are using Mobile Hub or they’re using the console or command line interface to interact with services directly\.

In order to modify projects, users are required to have permissions to use Mobile Hub \(granted by AWSMobileHubFullAccess IAM policy\), and they must have permission to perform whatever actions Mobile Hub takes on their behalf\. In almost every case, this means an account administrator must [grant the user the AdministratorAccess policy](reference-mobile-hub-iam-managed-policies.md#reference-mobile-hub-iam-managed-policies-how-to) in order to provide access to the AWS resources Mobile Hub modifies\. This is because, as project settings are modified, Mobile Hub will modify the IAM roles and policies used to enable the features affected by those settings\. Changing IAM roles and policies allows the user to control access to resources in the account, and so they must have administrative permissions\.

When an administrator does not want to grant administrative permissions for the full account, they can choose instead to provide each user or team their own sub\-account [using AWS Organizations](reference-mobile-hub-iam-managed-policies.md#reference-mobile-hub-iam-managed-policies-aws-organizations)\. Within their sub\-account, a user will have full administrative permissions\. Sub\-account owners are only limited in what they can do by the policy put in place by their administrator, and billing rolls up to the parent account\.

## What if I Currently Use MobileHub\_Service\_Role to Grant Mobile Hub Permissions?<a name="reference-mobile-hub-project-permissions-model-users"></a>

Previously, Mobile Hub assumed a service role called `MobileHub_Service_Role` in order to modify service configurations on your behalf using the following managed policy:

 [https://console\.aws\.amazon\.com/iam/home?\#/policies/arn:aws:iam::aws:policy/service\-role/AWSMobileHub\_ServiceUseOnly](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly) 

In that older model, all that was required to modify Mobile Hub projects was permissions to call Mobile Hub APIs, through the console or command line\. An administrator could delegate those permissions by attaching the `AWSMobileHub_FullAccess` policy to an [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) user, group, or role\.

If the account of your Mobile Hub projects relies on the old model, the impact on those who are not granted AdministratorAccess permissions will be as follows\.
+ IAM users, groups and roles that have the `AWSMobileHub_FullAccess` policy will no longer have sufficient permissions to perform any mutating operations in Mobile Hub, either via the console or `awsmobile` command line interface \(CLI\)\.
+ In order for IAM users, groups, or roles to be able to perform mutating operations using Mobile Hub, they must have the appropriate permissions\. The two choices for an administrator to [grant users permission](reference-mobile-hub-iam-managed-policies.md) to invoke all available operations in Mobile Hub are: attach the `AdministratorAccess` policy to the user, or a role they are attached to, or a group they are a member of; or alternatively, to use AWS Organizations to manage permissions\.

## Why Did the Permissions Model Change?<a name="reference-mobile-hub-project-permissions-model-why"></a>

AWS Mobile Hub creates IAM roles and assigns them permissions in order to enable use of AWS resources in mobile apps\. Such operations are considered administrative because they include enabling permission to perform operations on resources in the account\. Previously, Mobile Hub’s service role provided users who have been granted `AWSMobileHub_FullAccess` permissions with a path to escalate their own privileges to act on resources, potentially in ways their administrator did not intend to permit\. Removing the service role, removes the path to escalate privileges and puts control of user permissions directly in the hands of the administrator for a Mobile Hub project\.