# IAM Authentication and Access Control for Mobile Hub<a name="reference-mobile-hub-iam-auth-access"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

**Note**  
 *In depth understanding of AWS IAM, authentication, and access controls are not required to configure a backend for your mobile app using Mobile Hub\.* 

Mobile Hub uses AWS credentials and permissions policies to allow a user to view and/or create and configure the back\-end features the user selects for their mobile app\.

The following sections provide details on how IAM works, how you can use IAM to securely control access to your projects, and what IAM roles and policies Mobile Hub configures on your behalf\.

**Topics**
+ [Authentication](#authentication)
+ [Access Control](#access-control)

## Authentication<a name="authentication"></a>

AWS resources and services can only be viewed, created or modified with the correct authentication using AWS credentials \(which must also be granted [access permissions](reference-mobile-hub-iam-access-control.md) to those resources and services\)\. You can access AWS as any of the following types of identities:
+  **AWS account root user** 

  When you sign up for AWS, you provide an email address and password that is associated with your AWS account\. These are your root credentials and they provide complete access to all of your AWS resources\.
**Important**  
For security reasons, we recommend that you use the root credentials only to create an administrator user, which is an IAM user with full permissions to your AWS account\. Then, you can use this administrator user to create other IAM users and roles with limited permissions\. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users) and [Creating an Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.
+  **IAM user** 

  An [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) is simply an identity within your AWS account that has specific custom permissions \(for example, read\-only permissions to access your Mobile Hub project\)\. You can use an IAM user name and password to sign in to secure AWS webpages like the [AWS Management Console](https://console.aws.amazon.com/), [AWS Discussion Forums](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html), or the [AWS Support Center](https://console.aws.amazon.com/support/home#/)\.

  In addition to a user name and password, you can also generate [access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for each user\. You can use these keys when you access AWS services programmatically, either through [one of the several SDKs](https://aws.amazon.com/tools/) or by using the [AWS Command Line Interface \(CLI\)](https://aws.amazon.com/cli/)\. The SDK and CLI tools use the access keys to cryptographically sign your request\. If you don’t use the AWS tools, you must sign the request yourself\.
+  **IAM role** 

  An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is another IAM identity you can create in your account that has specific permissions\. It is similar to an IAM user, but it is not associated with a specific person\. An IAM role enables you to obtain temporary access keys that can be used to access AWS services and resources\. IAM roles with temporary credentials are useful in the following situations:
  +  **Federated user access** 

    Instead of creating an IAM user, you can use preexisting user identities from your enterprise user directory or a web identity provider\. These are known as federated users\. AWS assigns a role to a federated user when access is requested through an [identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)\. For more information about federated users, see [Federated Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html#intro-access-roles) in the *IAM User Guide*\.
  +  **Cross\-account access** 

    You can use an IAM role in your account to grant another AWS account permissions to access your account’s resources\. For an example, see [Tutorial: Delegate Access Across AWS Accounts Using IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) in the *IAM User Guide*\.
  +  **AWS service access** 

    You can use an IAM role in your account to grant an AWS service permissions to access your account’s resources\. For example, you can create a role that allows Amazon Redshift to access an Amazon S3 bucket on your behalf and then load data stored in the bucket into an Amazon Redshift cluster\. For more information, see [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*\.
  +  **Applications running on Amazon EC2** 

    Instead of storing access keys within the EC2 instance for use by applications running on the instance and making AWS API requests, you can use an IAM role to manage temporary credentials for these applications\. To assign an AWS role to an EC2 instance and make it available to all of its applications, you can create an instance profile that is attached to the instance\. An instance profile contains the role and enables programs running on the EC2 instance to get temporary credentials\. For more information, see [Using Roles for Applications on Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) in the *IAM User Guide*\.

## Access Control<a name="access-control"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions you cannot access or modify a Mobile Hub project\. The same is true for Mobile Hub when it creates and configures services and resources you have configured for your project\.

The following sections describe how to manage permissions and understand those that are being managed on your behalf by Mobile Hub\.
+  [Control Access to Mobile Hub Projects](reference-mobile-hub-iam-managed-policies.md) 