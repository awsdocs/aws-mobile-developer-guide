# Get Started<a name="mobile-hub-web-getting-started"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Overview<a name="mobile-hub-web-getting-started-overview"></a>

The AWS Mobile CLI provides a command line experience that allows front end JavaScript developers to quickly create and integrate AWS backend resources into their mobile apps\.

## Prerequisites<a name="mobile-hub-web-getting-started-prerequisites"></a>

1.  [Sign up for the AWS Free Tier](https://aws.amazon.com/free/)\.

1. Install [Node\.js](https://nodejs.org/en/download/) with NPM\.

1. Install AWS Mobile CLI

   ```
   npm install -g awsmobile-cli
   ```

1. Configure the CLI with your AWS credentials

   To setup permissions for the toolchain used by the CLI, run:

   ```
   awsmobile configure
   ```

   If prompted for credentials, follow the steps provided by the CLI\. For more information, see [provide IAM credentials to AWS Mobile CLI](aws-mobile-cli-credentials.md)\.

## Set Up Your Backend<a name="mobile-hub-web-getting-started-create-or-integrate"></a>


****  

|  | 
| --- |
|  Need to create a quick sample React app? See [Create a React App](https://reactjs.org/blog/2016/07/22/create-apps-with-no-configuration.html)\.  | 

 **To configure backend features for your app** 

1. In the root folder of your app, run:

   ```
   awsmobile init
   ```

   The `init` command creates a backend project for your app\. By default, analytics and web hosting are enabled in your backend and this configuration is automatically pulled into your app when you initialize\.

1. When prompted, provide the source directory for your project\. The CLI will generate `aws-exports.js` in this location\. This file contains the configuration and endpoint metadata used to link your front end to your backend services\.

   ```
   ? Where is your project's source directory:  src
   ```

1. Respond to further prompts with the following values\.

   ```
   ? Where is your project's distribution directory to store build artifacts:  build
   ? What is your project's build command:  npm run-script build
   ? What is your project's start command for local test run:  npm run-script start
   ? What awsmobile project name would you like to use:  YOUR-APP-NAME-2017-11-10-15-17-48
   ```

After the project is created you will get a success message which also includes details on the path where the aws\-exports\.js is copied\.

```
awsmobile project's details logged at: awsmobilejs/#current-backend-info/backend-details.json
awsmobile project's access information logged at: awsmobilejs/#current-backend-info/aws-exports.js
awsmobile project's access information copied to: src/aws-exports.js
awsmobile project's specifications logged at: awsmobilejs/#current-backend-info/mobile-hub-project.yml
contents in #current-backend-info/ is synchronized with the latest information in the aws cloud
```

Your project is now initialized\.

**Note**  
You can add the AWS backend resources you create for this project to another exisiting app using `awsmobile init YOUR_MOBILE_HUB_PROJECT_ID`\. To find the project ID, open your Mobile Hub project in the Mobile Hub console by running `awsmobile console`\. The project ID is the GUID portion of the console address, in the form of `XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`\.

## Connect to Your Backend<a name="mobile-hub-web-getting-started-configure-aws-amplify"></a>

AWS Mobile uses the open source [AWS Amplify library](https://aws.github.io/aws-amplify) to link your code to the AWS features configured for your app\.

This section of the guide shows examples using a React application of the kind output by `create-react-app` or a similar tool\.

 **To connect the app to your configured AWS features** 

In `index.js` \(or in other code that runs at launch\-time\), add the following imports\.

```
import Amplify from 'aws-amplify';
import awsmobile from './YOUR-PATH-TO/aws-exports';
```

Then add the following code\.

```
Amplify.configure(awsmobile);
```

### Run Your App Locally<a name="run-your-app-locally"></a>

Your app is now ready to launch and use the default features configured by AWS Mobile\.

 **To launch your app locally in a browser** 

In the root folder of your app, run:

```
awsmobile run
```

Behind the scenes, this command runs `npm install` to install the Amplify library and also pushes any backend configuration changes to AWS Mobile\. To run your app locally without pushing backend changes you can choose to run `npm install` and then run `npm start`\.

Anytime you launch your app, [app analytics are gathered and can be visualized](mobile-hub-web-add-analytics.md#web-add-analytics) in an AWS console\.


|  |  | 
| --- |--- |
|  AWS Free Tier  |  Initializing your app or adding features through the CLI will cause AWS services to be configured on your behalf\. The [pricing for AWS Mobile services](https://aws.amazon.com/mobile/pricing) enables you to learn and prototype at little or no cost using the [AWS Free Tier](https://aws.amazon.com/free)\.  | 

## Next Steps<a name="mobile-hub-web-getting-started-deploying-and-testing"></a>

**Topics**
+ [Deploy your app to the cloud](#deploy-your-app-to-the-cloud)
+ [Test Your App on Our Mobile Devices](#test-your-app-on-our-mobile-devices)
+ [Add Features](#mobile-hub-web-getting-started-add-features)
+ [Learn more](#learn-more)

### Deploy your app to the cloud<a name="deploy-your-app-to-the-cloud"></a>

Using a simple command, you can publish your app’s front end to hosting on a robust content distribution network \(CDN\) and view it in a browser\.

 **To deploy your app to the cloud and launch it in a browser** 

In the root folder of your app, run:

```
awsmobile publish
```

To push any backend configuration changes to AWS and view content locally, run `awsmobile run`\. In both cases, any pending changes you made to your backend configuration are made to your backend resources\.

By default, the CLI configures AWS Mobile [Hosting and Streaming](hosting-and-streaming.md) feature, that hosts your app on [Amazon CloudFront](https://aws.amazon.com/cloudfront/) CDN endpoints\. These locations make your app highly available to the public on the Internet and support [media file streaming](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html) 

You can also [use a custom domain](mobile-hub-web-host-frontend.md#web-host-frontend) for your hosting location\.

### Test Your App on Our Mobile Devices<a name="test-your-app-on-our-mobile-devices"></a>

Invoke a free remote test of your app on a variety of real devices and see results, including screen shots\.

 **To invoke a remote test of your app** 

In the root folder of your app, run:

```
awsmobile publish --test
```

The CLI will open the reporting page for your app in the Mobile Hub console to show the metrics gathered from the test devices\. The device that runs the remote test you invoke resides in [AWS Device Farm](https://aws.amazon.com/device-farm/) which provides flexible configuration of tests and reporting\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/web-performance-testing.png)

### Add Features<a name="mobile-hub-web-getting-started-add-features"></a>

Add the following AWS Mobile features to your mobile app using the CLI\.
+  [Analytics](mobile-hub-web-add-analytics.md#web-add-analytics) 
+  [User Sign\-in](mobile-hub-web-add-user-sign-in.md#web-add-user-sign-in) 
+  [NoSQL Database](mobile-hub-web-access-databases.md#web-access-databases) 
+  [User File Storage](mobile-hub-web-add-storage.md#web-add-storage) 
+  [Cloud Logic](mobile-hub-web-access-apis.md#web-access-apis) 

### Learn more<a name="learn-more"></a>

To learn more about the commands and usage of the AWS Mobile CLI, see the [AWS Mobile CLI reference](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify)\.