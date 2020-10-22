# AWS Mobile CLI User Credentials<a name="aws-mobile-cli-credentials"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Overview<a name="overview"></a>

The first time you set up the CLI you will be prompted to provide AWS user credentials\. The credentials establish permissions for the CLI to manage AWS services on your behalf\. They must belong to an AWS IAM user with administrator permissions in the account where the CLI is being used\.

## Permissions<a name="permissions"></a>

Administrator permissions are granted by an AWS account administrator\. If don’t have administrator permissions you will need to ask an administrator for the AWS account to grant them\.

If you are the account owner and signed in under the root credentials for the account, then you have, or can grant yourself, administrator permissions using the `AdministratorAccess` managed policy\. Best practice is to create a new IAM user under your account to access AWS services instead of using root credentials\.

For more information, see [Control Access to Mobile Hub Projects](reference-mobile-hub-iam-managed-policies.md)\.

## Get Account User Credentials<a name="get-account-user-credentials"></a>

If you have administrator permissions, the values you need to provide the CLI are your IAM user’s Access Key ID and a Secret Access Key\. If not, you will need to get these from an administrator\.

To provide the ID and the Key to AWS CLI, follow the CLI prompts to sign\-in to AWS, and provide a user name and AWS region\. The CLI will open the [AWS IAM console](https://console.aws.amazon.com/iam/) **Add user** dialog, with the `AdministratorAccess` policy attached, and the **Programmatic access** option selected by default\.

**Topics**
+ [Get credentials for a new user](#get-credentials-for-a-new-user)
+ [Get credentials for an existing user](#get-credentials-for-an-existing-user)

### Get credentials for a new user<a name="get-credentials-for-a-new-user"></a>

1. Choose **Next: Permissions** and then choose **Create user**\.

   Alternatively, you could add the user to a group with `AdministratorAccess` attached\.  
![\[Create an AWS IAM user to validate AWS Mobile CLI permissions.\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/aws-mobile-cli-create-user.png)

1. Choose **Create user**\.

1. Copy the values from the table displayed, or choose **Download \.csv** to save the values locally, and then type them into the prompts\.  
![\[Create an AWS IAM user to validate AWS Mobile CLI permissions.\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/aws-mobile-cli-get-keys.png)

For more detailed steps, see [add a new account user with administrator permissions](reference-mobile-hub-iam-managed-policies.md#reference-mobile-hub-iam-managed-policies-new-user)\.

### Get credentials for an existing user<a name="get-credentials-for-an-existing-user"></a>

1. Choose **cancel**\.

1. On the left, choose **Users**, then select the user from the list\. Choose **Security credentials**, then choose **Create access key**\.