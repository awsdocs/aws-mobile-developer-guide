# Overview of Access Permissions Management for Mobile Hub Projects<a name="reference-mobile-hub-iam-access-control"></a>


|  | 
| --- |
|   **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of [AWS Amplify](https://amzn.to/am-amplify-docs)\. The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI\. For existing apps that use AWS Mobile SDK prior to v2\.8\.0, we highly recommend you migrate your app to use [AWS Amplify](https://amzn.to/am-amplify-docs) and the latest SDK\.  | 

**Note**  
 *In depth understanding of AWS IAM, authentication, and access controls are not required to configure a backend for your mobile app using Mobile Hub\.* 

Every AWS resource is owned by an AWS account\. [Permissions to view, create, and/or access the resources](reference-mobile-hub-iam-managed-policies.md) are governed by policies\.

An account administrator can attach permissions policies to IAM identities \(that is, users, groups, and roles\), and some services \(such as AWS Lambda\) also support attaching permissions policies to resources\.

**Note**  
An *account administrator* \(or administrator user\) is a user with administrator privileges\. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*\.  
When granting permissions, you decide who is getting the permissions, the resources they get permissions for, and the specific actions that you want to allow on those resources\.

**Topics**
+ [Understanding Resource Ownership for AWS Mobile Hub](#resource-ownership)
+ [Managing Access to Resources](#managing-access)
+ [Specifying Policy Elements: Actions, Effects, Resources, and Principals](#policy-elements)

## Understanding Resource Ownership for AWS Mobile Hub<a name="resource-ownership"></a>

The primary resource of a Mobile Hub project is the project itself\. In first use of the Mobile Hub console, you allow Mobile Hub to manage permissions and access the project resource for you\. A resource owner is the AWS account that created a resource\. That is, the resource owner is the AWS account of the principal entity \(the root account, an IAM user, or an IAM role\) that authenticates the request that creates the resource\. The following examples illustrate how this works:
+ If you use the root account credentials of your AWS account to create an AWS Mobile Hub project, your AWS account is the owner of the resources associated with that project\.
+ If you create an IAM user in your AWS account and grant permissions to create Mobile Hub projects to that user, the user can also create projects\. However, your AWS account, to which the user belongs, owns the resources associated with the project\.
+ If you create an IAM role in your AWS account with permissions to create AWS Mobile Hub projects, anyone who can assume the role can create, edit, or delete projects\. Your AWS account, to which the role belongs, owns the resources associated with that project\.

## Managing Access to Resources<a name="managing-access"></a>

A *permissions policy* describes who has access to what\. The following section explains the available options for creating permissions policies\.

**Note**  
This section discusses using IAM in the context of AWS Mobile Hub\. It doesn’t provide detailed information about the IAM service\. For complete IAM documentation, see [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*\. For information about IAM policy syntax and descriptions, see [AWS Identity and Access Management Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*\.

Policies attached to an IAM identity are referred to as identity\-based policies \(IAM polices\) and policies attached to a resource are referred to as resource\-based policies\.

**Topics**
+ [Identity\-Based Policies \(IAM Policies\)](#identity-based-policies)
+ [Resource\-Based Policies](#resource-based-policies)

### Identity\-Based Policies \(IAM Policies\)<a name="identity-based-policies"></a>

You can attach policies to IAM identities\. For example, you can do the following:
+  **Attach a permissions policy to a user or a group in your account**? An account administrator can use a permissions policy that is associated with a particular user to grant permissions for that user to view or modify an AWS Mobile Hub project\.
+  **Attach a permissions policy to a role \(grant cross\-account permissions\)** ? You can attach an identity\-based permissions policy to an IAM role to grant cross\-account permissions\. For example, when you first enter Mobile Hub and agree, as account principal, to grant it permissions to provision and configure your project, you are granting the AWS managed `MobileHub_Service_Role` role cross\-account permissions\. An AWS managed policy, `AWSMobileHub_ServiceUseOnly`, is attached to that role in the context of your Mobile Hub project\. The role has a trust policy that allows Mobile Hub to act as account principal with the ability to grant permissions for services and resources used by your project\.

  For more information about using IAM to delegate permissions, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*\.

As an example of using an identity\-based policy, the following policy grants permissions to a user to create an Amazon S3 bucket\. A user with these permissions can create a storage location using the Amazon S3 service\.

```
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
```

For more information about using identity\-based policies with Mobile Hub , see :ref: reference\-mobile\-hub\-project\-permissions\-model`\.

For more information about users, groups, roles, and permissions, see [Identities \(Users, Groups, and Roles\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*\.

### Resource\-Based Policies<a name="resource-based-policies"></a>

Other services, such as Amazon S3, also support resource\-based permissions policies\. For example, you can attach a policy to an Amazon S3 bucket to manage access permissions to that bucket\.

## Specifying Policy Elements: Actions, Effects, Resources, and Principals<a name="policy-elements"></a>

Each service that is configured by Mobile Hub defines a set of API operations\. To grant Mobile Hub permissions for these API operations, a set of actions is specified in an AWS managed policy\. Performing an API operation can require permissions for more than one action\.

The following are the basic policy elements:
+  **Resource** \- In a policy, you use an Amazon Resource Name \(ARN\) to identify the resource to which the policy applies\.
+  **Action** \- You use action keywords to identify resource operations that you want to allow or deny\. For example, the `s3:Createbucket` permission allows Mobile Hub to perform the Amazon S3`CreateBucket` operation\.
+  **Effect** \- You specify the effect when the user requests the specific action?this can be either allow or deny\. If you don’t explicitly grant access to \(allow\) a resource, access is implicitly denied\. You can also explicitly deny access to a resource, which you might do to make sure that a user cannot access it, even if a different policy grants access\.
+  **Principal** \- In identity\-based policies \(IAM policies\), the user that the policy is attached to is the implicit principal\. For resource\-based policies, you specify the user, account, service, or other entity that you want to receive permissions \(applies to resource\-based policies only\)\.