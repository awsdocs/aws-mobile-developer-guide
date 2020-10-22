# AWS Mobile CLI Reference<a name="aws-mobile-cli-reference"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

The AWS Mobile CLI provides a command line interface for front end JavaScript developers to seamlessly enable AWS services and configure into their apps\. With minimal configuration, you can start using all of the functionality provided by the [AWS Mobile Hub](https://console.aws.amazon.com/mobilehub) from your favorite terminal program\.

## Installation and Usage<a name="installation-and-usage"></a>

This section details the usage and the core commands of the `awsmobile CLI` for JavaScript\.

### Install AWS Mobile CLI<a name="install-aws-mobile-cli"></a>

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

### Usage<a name="usage"></a>

The AWS Mobile CLI usage is designed to resemble other industry standard command line interfaces\.

```
awsmobile <command> [options]
```

The `help` and `version` options are universal to all the commands\. Additional special options for some commands are detailed in the relevant sections\.

```
-V, --version  output the version number
-h, --help     output usage information
```

For example:

```
awsmobile -help
or
awsmobile init --help
```

## Summary of CLI Commands<a name="summary-of-cli-commands"></a>

The current set of commands supported by the `awsmobile CLI` are listed below\.


|  |  | 
| --- |--- |
|   [awsmobile init](#aws-mobile-cli-reference-init)   |  Initializes a new Mobile Hub project, checks for IAM keys, and pulls the aws\-exports\.js file  | 
|   [awsmobile configure](#aws-mobile-cli-reference-configure)   |  Shows existing keys and allows them to be changed if already set\. If keys aren’t set, deep links the user to the IAM console to create keys and then prompts for the access key and secret key\. This command helps edit configuration settings for the AWS account or the project\.  | 
|   [awsmobile pull](#aws-mobile-cli-reference-pull)   |  Downloads the latest aws\-exports\.js, YAML or any other relevant project details from the Mobile Hub project  | 
|   [awsmobile push](#aws-mobile-cli-reference-push)   |  Uploads local metadata, Lambda code, DynamoDB definitions or any other relevant project details to Mobile Hub  | 
|   [awsmobile publish](#aws-mobile-cli-reference-publish)   |  Executes `awsmobile push`, then builds and publishes client\-side application to S3 and Cloud Front  | 
|   [awsmobile run](#aws-mobile-cli-reference-run)   |  Executes `awsmobile push`, then executes the project’s start command to test run the client\-side application  | 
|   [awsmobile console](#aws-mobile-cli-reference-console)   |  Open the web console of the awsmobile Mobile Hub project in the default browser  | 
|   [awsmobile features](#aws-mobile-cli-reference-features)   |  Shows available and enabled features\. Toggle to select or de\-select features\.  | 
|   [awsmobile <feature\-name> enable \[–prompt\]](#aws-mobile-cli-reference-enable)   |  Enables the feature with the defaults \(and prompt for changes\)  | 
|   [awsmobile <feature\-name> disable](#aws-mobile-cli-reference-disable)   |  Disables the feature  | 
|   [awsmobile <feature\-name> configure](#aws-mobile-cli-reference-feature-configure)   |  Contains feature\-specific sub commands like add\-table, add\-api, etc\.  | 
|   [awsmobile cloud\-api invoke <apiname> <method> <path> \[init\]](#aws-mobile-cli-reference-invoke)   |  Invokes the API for testing locally\. This helps quickly test unsigned APIs in your local environment\.  | 
|   [awsmobile delete](#aws-mobile-cli-reference-delete)   |  Deletes the Mobile hub project\.  | 
|   [awsmobile help \[cmd\]](#aws-mobile-cli-reference-help)   |  Displays help for \[cmd\]\.  | 

## init<a name="aws-mobile-cli-reference-init"></a>

The `awsmobile init` command initializes a new Mobile Hub project, checks for IAM keys, and pulls the aws\-exports\.js file\.

There are two usages of the `awsmobile init` command

1. Initialize the current project with awsmobilejs features

   ```
   awsmobile init
   ```

   When prompted, set these project configs:

   ```
   Please tell us about your project:
   ? Where is your project's source directory:  src
   ? Where is your project's distribution directory that stores build artifacts:  build
   ? What is your project's build command:  npm run-script build
   ? What is your project's start command for local test run:  npm run-script start
   
   ? What awsmobile project name would you like to use:  my-mobile-project
   ```

   The source directory is where the AWS Mobile CLI copies the latest `aws-exports.js` to be easily available for your front\-end code\. This file is automatically updated every time features are added or removed\. Specifying a wrong / unavailable folder will not copy the file over\.

   The Distribution directly is essentially the build directory for your project\. This is used during the `awsmobile publish` process\.

   The project’s build and start values are used during the `awsmobile publish` and `awsmobile run` commands respectively\.

   The awsmobile project name is the name of the backend project created in the Mobile hub\.

   You can alter the settings about your project by using the [awsmobile configure project](#aws-mobile-cli-reference-configure) command\.

1. Initialize and link to an existing awsmobile project as backend

   ```
   awsmobile init <awsmobile-project-id>
   ```

   The awsmobile\-project\-id is the id of the existing backend project in the Mobile Hub\. This command helps attach an existing backend project to your app\.

1. Remove the attached awsmobile project from the backend\.

   ```
   awsmobile init --remove
   ```

   This command removes the attached backend project associated with your app and cleans the associated files\. This will not alter your app in any way, other than removing the backend project itself\.

## configure<a name="aws-mobile-cli-reference-configure"></a>

The `awsmobile configure` shows existing keys and allows them to be changed if already set\. If keys aren’t set, deep links the user to the IAM console to create keys and then prompts for the access key and secret key\. There are two possible usages of this command\. Based on the argument selected, this command can be used to set or change the AWS account settings OR the project settings\.

```
awsmobile configure [aws|project]
```

1. Configuring the AWS account settings using the `aws` argument\. This is the default argument for this command

   ```
   awsmobile configure
   or
   awsmobile configure aws
   ```

   You will be prompted with questions to set the AWS account credentials as below

   ```
   configure aws
   ? accessKeyId:  <ACCESS-KEY-ID>
   ? secretAccessKey:  <SECRET-ACCESS-KEY>
   ? region:  <SELECT-REGION-FROM-THE-LIST>
   ```

1. Configuring the project settings using the `project` argument

   ```
   awsmobile configure project
   ```

   You will be prompted with questions to configure project as detailed below

   ```
   ? Where is your project's source directory:  src
   ? Where is your project's distribution directory to store build artifacts:  dist
   ? What is your project's build command:  npm run-script build
   ? What is your project's start command for local test run:  npm run-script start
   ```

1. Retrieve and display the AWS credentials using the `--list` option

   ```
   awsmobile configure --list
   ```

## pull<a name="aws-mobile-cli-reference-pull"></a>

The `awsmobile pull` command downloads the latest aws\-exports\.js, YAML and any relevant cloud / backend artifacts from the Mobile Hub project to the local dev environment\. Use this command if you modified the project on the Mobile Hub and want to get the latest on your local environment\.

```
awsmobile pull
```

## push<a name="aws-mobile-cli-reference-push"></a>

The `awsmobile push` uploads local metadata, Lambda code, Dynamo definitions and any relevant artifacts to Mobile Hub\. Use this command when you enable, disable or configure features on your local environment and want to update the backend project on the Mobile Hub with the relevant updates\.

```
awsmobile push
```

Use `awsmobile push` after using `awsmobile features`, `awsmobile <feature> enable`, `awsmobile <feature> disable` or `awsmobile <feature> configure` to update the backend project appropriately\. This can be used either after each of these or once after all of the changes are made locally\.

## publish<a name="aws-mobile-cli-reference-publish"></a>

The `awsmobile publish` command first executes the awsmobile `push` command, then builds and publishes client\-side code to Amazon S3 hosting bucket\. This command publishes the client application to s3 bucket for hosting and then opens the browser to show the index page\. It checks the timestamps to automatically build the app if necessary before deployment\. It checks if the client has selected hosting in their backend project features, and if not, it’ll prompt the client to update the backend with hosting feature\.

```
awsmobile publish
```

The publish command has a number of options to be used\.

1. Refresh the Cloud Front distributions

   ```
   awsmobile publish -c
    or
   awsmobile publish --cloud-front
   ```

1. Test the application on AWS Device Farm

   ```
   awsmobile publish -t
   or
   awsmobile publish --test
   ```

1. Suppress the tests on AWS Device Farm

   ```
   awsmobile publish -n
   ```

1. Publish the front end only without updating the backend

   ```
   awsmobile publish -f
   or
   awsmobile publish --frontend-only
   ```

## run<a name="aws-mobile-cli-reference-run"></a>

The `awsmobile run` command first executes the `awsmobile push` command, then executes the start command you set in the project configuration, such as `npm run start` or `npm run ios`\. This can be used to conveniently test run your application locally with the latest backend development pushed to the cloud\.

```
awsmobile run
```

## console<a name="aws-mobile-cli-reference-console"></a>

The `awsmobile console` command opens the web console of the awsmobile Mobile Hub project in the default browser

```
awsmobile console
```

## features<a name="aws-mobile-cli-reference-features"></a>

The `awsmobile features` command displays all the available awsmobile features, and allows you to individually enable/disable them locally\. Use the arrow key to scroll up and down, and use the space key to enable/disable each feature\. Please note that the changes are only made locally, execute awsmobile push to update the awsmobile project in the cloud\.

```
awsmobile features
```

The features supported by the AWS Mobile CLI are:
+ user\-signin \(Amazon Cognito\)
+ user\-files \(Amazon S3\)
+ cloud\-api \(Lambda / API Gateway\)
+ database \(DynamoDB\)
+ analytics \(Amazon Pinpoint\)
+ hosting \(Amazon S3 and CloudFront\)

```
? select features:  (Press <space> to select, <a> to toggle all, <i> to inverse selection)
❯◯ user-signin
 ◯ user-files
 ◯ cloud-api
 ◯ database
 ◉ analytics
 ◉ hosting
```

Use caution when disabling a feature\. Disabling the feature will delete all the related objects \(APIs, Lambda functions, tables etc\)\. These artifacts can not be recovered locally, even if you re\-enable the feature\.

Use `awsmobile push` after using `awsmobile <feature> disable` to update the backend project on the AWS Mobile Hub project with the selected features\.

## enable<a name="aws-mobile-cli-reference-enable"></a>

The `awsmobile <feature> enable` enables the specified feature with the default settings\. Please note that the changes are only made locally, execute `awsmobile` push to update the AWS Mobile project in the cloud\.

```
awsmobile <feature> enable
```

The features supported by the AWS Mobile CLI are:
+ user\-signin \(Amazon Cognito\)
+ user\-files \(Amazon S3\)
+ cloud\-api \(Lambda / API Gateway\)
+ database \(DynamoDB\)
+ analytics \(Amazon Pinpoint\)
+ hosting \(Amazon S3 and CloudFront\)

The `awsmobile <feature> enable --prompt` subcommand allows user to specify the details of the mobile hub feature to be enabled, instead of using the default settings\. It prompts the user to answer a list of questions to specify the feature in detail\.

```
awsmobile <feature> enable -- prompt
```

Enabling the `user-signin` feature will prompt you to change the way it is enabled, configure advanced settings or disable sign\-in feature to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile user-signin enable --prompt

? Sign-in is currently disabled, what do you want to do next (Use arrow keys)
❯ Enable sign-in with default settings
  Go to advance settings
```

Enabling the `user-files` feature with the `--prompt` option will prompt you to confirm usage of S3 for user files\.

```
awsmobile user-files enable --prompt

? This feature is for storing user files in the cloud, would you like to enable it? Yes
```

Enabling the `cloud-api` feature with the `--prompt` will prompt you to create, remove or edit an API related to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile cloud-api enable --prompt

 ? Select from one of the choices below. (Use arrow keys)
 ❯ Create a new API
```

Enabling the `database` feature with the `--prompt` will prompt you to with initial questions to specify your database table details related to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile database enable --prompt

? Should the data of this table be open or restricted by user? (Use arrow keys)
❯ Open
  Restricted
```

Enabling the `analytics` feature with the `--prompt` will prompt you to confirm usage of Pinpoint Analytics\.

```
 awsmobile analytics enable --prompt

? Do you want to enable Amazon Pinpoint analytics? (y/N)
```

Enabling the `hosting` feature with the `--prompt` will prompt you to confirm hosting and streaming on CloudFront distribution\.

```
awsmobile hosting enable --prompt

? Do you want to host your web app including a global CDN? (y/N)
```

Execute `awsmobile push` after using `awsmobile <feature> enable` to update the awsmobile project in the cloud\.

## disable<a name="aws-mobile-cli-reference-disable"></a>

The `awsmobile <feature> disable` disables the feature in their backend project\. Use caution when disabling a feature\. Disabling the feature will delete all the related objects \(APIs, Lambda functions, tables etc\)\. These artifacts can not be recovered locally, even if you re\-enable the feature\.

```
awsmobile <feature> disable
```

The features supported by the AWS Mobile CLI are:
+ user\-signin \(Amazon Cognito\)
+ user\-files \(Amazon S3\)
+ cloud\-api \(Lambda / API Gateway\)
+ database \(DynamoDB\)
+ analytics \(Amazon Pinpoint\)
+ hosting `

Use `awsmobile push` after using `awsmobile <feature> disable` to update the backend project on the AWS Mobile Hub project with the disabled features\.

## configure<a name="aws-mobile-cli-reference-feature-configure"></a>

The `awsmobile <feature> configure` configures the objects in the selected feature\. The configuration could mean adding, deleting or updating a particular artifact\. This command can be used only if the specific feature is already enabled\.

```
awsmobile <feature> configure
```

The features supported by the AWS Mobile CLI are:
+ user\-signin \(Amazon Cognito\)
+ user\-files \(Amazon S3\)
+ cloud\-api \(Lambda / API Gateway\)
+ database \(DynamoDB\)
+ analytics \(Amazon Pinpoint\)
+ hosting \(Amazon S3 and CloudFront\)

Configuring the `user-signin` feature will prompt you to change the way it is enabled, configure advanced settings or disable sign\-in feature to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile user-signin configure

? Sign-in is currently enabled, what do you want to do next (Use arrow keys)
❯ Configure Sign-in to be required (Currently set to optional)
  Go to advance settings
  Disable sign-in
```

Configuring the `user-files` feature will prompt you to confirm usage of S3 for user files\.

```
 awsmobile user-files configure

? This feature is for storing user files in the cloud, would you like to enable it? (Y/n)
```

Configuring the `cloud-api` feature will prompt you to create, remove or edit an API related to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile cloud-api configure

? Select from one of the choices below. (Use arrow keys)
❯ Create a new API
  Remove an API from the project
  Edit an API from the project
```

Configuring the `database` feature will prompt you to create, remove or edit a table related to the project\. Selecting the desired option may prompt you with further questions\.

```
awsmobile database configure

  ? Select from one of the choices below. (Use arrow keys)
  ❯ Create a new table
    Remove table from the project
    Edit table from the project
```

Configuring the `analytics` feature will prompt you to confirm usage of Pinpoint Analytics\.

```
awsmobile analytics configure

? Do you want to enable Amazon Pinpoint analytics? Yes
```

Configuring the `hosting` feature will prompt you to confirm hosting and streaming on CloudFront distribution\.

```
awsmobile hosting configure

? Do you want to host your web app including a global CDN? Yes
```

Use `awsmobile push` after using `awsmobile <feature> configure` to update the backend project on the AWS Mobile Hub project with the configured features\.

## invoke<a name="aws-mobile-cli-reference-invoke"></a>

The `awsmobile cloud-api invoke` invokes the API for testing locally\. This helps quickly test the unsigned API locally by passing the appropriate arguments\. This is intended to be used for the development environment or debugging of your API / Lambda function\.

```
awsmobile cloud-api invoke <apiname> <method> <path> [init]
```

For example you could invoke the sampleCloudApi post method as shown below

```
awsmobile cloud-api invoke sampleCloudApi post /items '{"body":{"test-key":"test-value"}}'
```

The above test will return a value that looks like

```
{ success: 'post call succeed!',
  url: '/items',
  body: { 'test-key': 'test-value' } }
```

Similarly, you could invoke the sampleCloudApi get method as shown below

```
awsmobile cloud-api invoke sampleCloudApi get /items
```

The above test will return a value that looks like

```
{ success: 'get call succeed!', url: '/items' }
```

## delete<a name="aws-mobile-cli-reference-delete"></a>

The `awsmobile delete` command deletes the Mobile hub project in the cloud\. Use extra caution when you decide to execute this command, as it can irrevocably affect your team’s work, the mobile hub project will be delete and cannot be recovered once this command is executed\.

```
awsmobile delete
```

## help<a name="aws-mobile-cli-reference-help"></a>

The `awsmobile help` command can be used as a standalone command or the command name that you need help in can be passed as an argument\. This gives the usage information for that command including any options that can be used with it\.

For Example:

```
awsmobile help
or
awsmobile help init
```

The `--help` option detailing at the beginning of this page and the `awsmobile help` command provide the same level of detail\. The difference is in the usage\.