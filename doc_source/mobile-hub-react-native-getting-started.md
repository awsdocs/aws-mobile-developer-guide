# Get Started<a name="mobile-hub-react-native-getting-started"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Overview<a name="mobile-hub-react-native-getting-started-overview"></a>

The AWS Mobile CLI provides a command line experience that allows frontend JavaScript developers to quickly create and integrate AWS backend resources into their mobile apps\.

## Prerequisites<a name="mobile-hub-react-native-getting-started-prerequisites"></a>

1.  [Sign up for the AWS Free Tier](https://aws.amazon.com/free/) to learn and prototype at little or no cost\.

1. Install [Node\.js](https://nodejs.org/en/download/) with NPM\.

1. Install the AWS Mobile CLI

   ```
   npm install --global awsmobile-cli
   ```

1. Configure the CLI with your AWS credentials

   To setup permissions for the toolchain used by the CLI, run:

   ```
   awsmobile configure
   ```

   If prompted for credentials, follow the steps provided by the CLI\. For more information, see [Provide IAM credentials to AWS Mobile CLI](aws-mobile-cli-credentials.md)\.

## Set Up Your Backend<a name="mobile-hub-react-native-getting-started-create-or-integrate"></a>


|  | 
| --- |
|  Need to create a quick sample React Native app? See [Create a React Native App](https://facebook.github.io/react-native/docs/getting-started.html)\.  | 

 **To configure backend features for your app** 

1. In the root folder of your app, run:

   ```
   awsmobile init
   ```

   The `init` command creates a backend project for your app\. By default, analytics and web hosting are enabled in your backend and this configuration is automatically pulled into your app when you initialize\.

1. When prompted, provide the source directory for your project\. The CLI will generate `aws-exports.js` in this location\. This file contains the configuration and endpoint metadata used to link your frontend to your backend services\.

   ```
   ? Where is your project's source directory:  /
   ```

   Then respond to further prompts with the following values\.

   ```
   Please tell us about your project:
   ? Where is your project's source directory:  /
   ? Where is your project's distribution directory that stores build artifacts:  build
   ? What is your project's build command:  npm run-script build
   ? What is your project's start command for local test run:  npm run-script start
   ```

## Connect to Your Backend<a name="mobile-hub-react-native-getting-started-configure-aws-amplify"></a>

AWS Mobile uses the open source [AWS Amplify library](https://github.com/aws/aws-amplify) to link your code to the AWS features configured for your app\.

 **To connect the app to your configured AWS services** 

1. Install AWS Amplify for React Native library\.

   ```
   npm install --save aws-amplify
   ```

1. In `App.js` \(or in other code that runs at launch\-time\), add the following imports\.

   ```
   import Amplify from 'aws-amplify';
   
   import aws_exports from './YOUR-PATH-TO/aws-exports';
   ```

1. Then add the following code\.

   ```
   Amplify.configure(aws_exports);
   ```

### Run Your App Locally<a name="run-your-app-locally"></a>

Your app is now ready to launch and use the default services configured by AWS Mobile\.

 **To launch your app locally** 

Use the command native to the React Native tooling you are using\. For example, if you made your app using `create-react-native-app` then run:

```
npm run android

# OR

npm run ios
```

Anytime you launch your app, [app usage analytics are gathered and can be visualized](mobile-hub-react-native-add-analytics.md#react-native-add-analytics) in an AWS console\.


|  |  | 
| --- |--- |
|  AWS Free Tier  |  Initializing your app or adding features through the CLI will cause AWS services to be configured on your behalf\. The [pricing for AWS Mobile services](https://aws.amazon.com/mobile/pricing) enables you to learn and prototype at little or no cost using the [AWS Free Tier](https://aws.amazon.com/free)\.  | 

## Next Steps<a name="mobile-hub-react-native-getting-started-deploying-and-testing"></a>

### Add Features<a name="mobile-hub-react-native-getting-started-add-features"></a>

Add the following AWS Mobile features to your mobile app using the CLI\.
+  [Analytics](mobile-hub-react-native-add-analytics.md#react-native-add-analytics) 
+  [User Sign\-in](mobile-hub-react-native-add-user-sign-in.md#react-native-add-user-sign-in) 
+  [NoSQL Database](mobile-hub-react-native-access-databases.md#react-native-access-databases) 
+  [User File Storage](mobile-hub-react-native-add-storage.md#react-native-add-storage) 
+  [Cloud Logic](mobile-hub-react-native-access-apis.md#react-native-access-apis) 

### Learn more<a name="learn-more"></a>

To learn more about the commands and usage of the AWS Mobile CLI, see the [AWS Mobile CLI reference](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify)\.