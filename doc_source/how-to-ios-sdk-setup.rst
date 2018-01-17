.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _setup-ios:

##############################
iOS: Setup Options for the SDK
##############################

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <getting-started>` to install the SDK and integrate AWS features.

*Or, use the contents of this page if your app will integrate existing AWS services.*



.. contents::
   :local:
   :depth: 2

To add the SDK, install the following on your development machine:

- Xcode 7 or later

- iOS 8 or later

You can view the source code in the `AWS Mobile SDK for iOS GitHub repository <https://github.com/aws/aws-sdk-ios>`_.

.. _include_sdk_ios:

Include the AWS Mobile SDK for iOS in an Existing Application
-------------------------------------------------------------

The samples included with the SDK are standalone projects that are already set up. You can also integrate the SDK into your own existing project. Choose one of the following three ways to import the SDK into your project:

- Cocoapods
- Carthage
- Dynamic Frameworks

.. note:: Importing the SDK in multiple ways loads duplicate copies of the SDK into the project and causes compiler errors.

.. _set-up-options:

.. container:: option

    CocoaPods
        #. The AWS Mobile SDK for iOS is available through `CocoaPods <http://cocoapods.org/>`_. Install CocoaPods by running the following commands from the folder containing your projects :file:`*.xcodeproj` file.

            $ :command:`gem install cocoapods`

            .. note::

               Depending on your system settings, you may need to run the command as administrator using `sudo`, as follows:

            $ :command:`sudo gem install cocoapods`

            $ :command:`pod setup`

            $ :command:`pod init`

        #. In your project directory (the directory where your :file:`*.xcodeproj` file is), open the empty text file named :file:`Podfile` (without a file extension) and add the following lines to the file. Replace ``myAppName`` with your app name. You can also remove pods for services that you don't use. For example, if you don't use `AWSAutoScaling`, remove or do not include the ``AWSAutoScaling`` pod.

            .. code-block:: javascript

                source 'https://github.com/CocoaPods/Specs.git'

                platform :ios, '8.0'
                use_frameworks!

                target :'myAppName' do
                    pod 'AWSAuth'
                    pod 'AWSAuthCore'
                    pod 'AWSAuthUI'
                    pod 'AWSAutoScaling'
                    pod 'AWSCloudWatch'
                    pod 'AWSCognito'
                    pod 'AWSCognitoAuth'
                    pod 'AWSCognitoIdentityProvider'
                    pod 'AWSCognitoIdentityProviderASF'
                    pod 'AWSCognitoSync'
                    pod 'AWSCore'
                    pod 'AWSDynamoDB'
                    pod 'AWSEC2'
                    pod 'AWSElasticLoadBalancing'
                    pod 'AWSFacebookSignIn'
                    pod 'AWSGoogleSignIn'
                    pod 'AWSIoT'
                    pod 'AWSKMS'
                    pod 'AWSKinesis'
                    pod 'AWSLambda'
                    pod 'AWSLex'
                    pod 'AWSLogs'
                    pod 'AWSMachineLearning'
                    pod 'AWSMobileAnalytics'
                    pod 'AWSMobileClient'
                    pod 'AWSPinpoint'
                    pod 'AWSPolly'
                    pod 'AWSRekognition'
                    pod 'AWSS3'
                    pod 'AWSSES'
                    pod 'AWSSNS'
                    pod 'AWSSQS'
                    pod 'AWSSimpleDB'
                    pod 'AWSUserPoolsSignIn'
                end

        #. Run the following command:

            $ :command:`pod install`

        #. Open :file:`*.xcworkspace` with Xcode and start using the SDK.

            .. note::

                Do not open :file:`*.xcodeproj`. Opening this project file instead of a workspace results in an error.

    Carthage
        #. Install the latest version of `Carthage <https://github.com/Carthage/Carthage#installing-carthage>`_.

        #. Add the following to your `Cartfile`::

            github "aws/aws-sdk-ios"

        #. Run the following command:

            $ :command:`carthage update`

        #. With your project open in Xcode, choose your **Target**. In the **General** tab, find **Embedded Binaries**,  then choose the **+** button.

        #. Choose the **Add Other** button, navigate to the ``AWS<#ServiceName#>.framework`` files under **Carthage** > **Build** > **iOS** and select ``AWSCore.framework`` and the other service frameworks you require. Do not select the **Destination: Copy items if needed** checkbox when prompted.

            * :code:`AWSAuth`
            * :code:`AWSAuthCore`
            * :code:`AWSAuthUI`
            * :code:`AWSAutoScaling`
            * :code:`AWSCloudWatch`
            * :code:`AWSCognito`
            * :code:`AWSCognitoAuth`
            * :code:`AWSCognitoIdentityProvider`
            * :code:`AWSCognitoIdentityProviderASF`
            * :code:`AWSCognitoSync`
            * :code:`AWSCore`
            * :code:`AWSDynamoDB`
            * :code:`AWSEC2`
            * :code:`AWSElasticLoadBalancing`
            * :code:`AWSFacebookSignIn`
            * :code:`AWSGoogleSignIn`
            * :code:`AWSIoT`
            * :code:`AWSKMS`
            * :code:`AWSKinesis`
            * :code:`AWSLambda`
            * :code:`AWSLex`
            * :code:`AWSLogs`
            * :code:`AWSMachineLearning`
            * :code:`AWSMobileAnalytics`
            * :code:`AWSMobileClient`
            * :code:`AWSPinpoint`
            * :code:`AWSPolly`
            * :code:`AWSRekognition`
            * :code:`AWSS3`
            * :code:`AWSSES`
            * :code:`AWSSNS`
            * :code:`AWSSQS`
            * :code:`AWSSimpleDB`
            * :code:`AWSUserPoolsSignIn`

        #. Under the **Build Phases** tab in your **Target**, choose the **+** button on the top left and then select **New Run Script Phase**.

        # Setup the build phase as follows. Make sure this phase is below the **Embed Frameworks** phase.

            .. code-block:: bash


                Shell /bin/sh

                bash "${BUILT_PRODUCTS_DIR}/${FRAMEWORKS_FOLDER_PATH}/AWSCore.framework/strip-frameworks.sh"

                Show environment variables in build log: Checked
                Run script only when installing: Not checked

                Input Files: Empty
                Output Files: Empty

    Frameworks
        #. Download the SDK from http://aws.amazon.com/mobile/sdk. The SDK is stored in a compressed
           file archive named :file:`aws-ios-sdk-#.#.#`, where '#.#.#' represents the version number. For version
           2.5.0, the filename is :file:`aws-ios-sdk-2.5.0`.


        #. With your project open in Xcode, choose your **Target**. Under the **General** tab, find
           **Embedded Binaries** and then choose the **+** button.

        #. Choose **Add Other**. Navigate to the ``AWS<#ServiceName#>.framework`` files
           and select ``AWSCore.framework`` and the other service frameworks you require. Select
           the **Destination: Copy items if needed** checkbox when prompted.

            * :code:`AWSAuth`
            * :code:`AWSAuthCore`
            * :code:`AWSAuthUI`
            * :code:`AWSAutoScaling`
            * :code:`AWSCloudWatch`
            * :code:`AWSCognito`
            * :code:`AWSCognitoAuth`
            * :code:`AWSCognitoIdentityProvider`
            * :code:`AWSCognitoIdentityProviderASF`
            * :code:`AWSCognitoSync`
            * :code:`AWSCore`
            * :code:`AWSDynamoDB`
            * :code:`AWSEC2`
            * :code:`AWSElasticLoadBalancing`
            * :code:`AWSFacebookSignIn`
            * :code:`AWSGoogleSignIn`
            * :code:`AWSIoT`
            * :code:`AWSKMS`
            * :code:`AWSKinesis`
            * :code:`AWSLambda`
            * :code:`AWSLex`
            * :code:`AWSLogs`
            * :code:`AWSMachineLearning`
            * :code:`AWSMobileAnalytics`
            * :code:`AWSMobileClient`
            * :code:`AWSPinpoint`
            * :code:`AWSPolly`
            * :code:`AWSRekognition`
            * :code:`AWSS3`
            * :code:`AWSSES`
            * :code:`AWSSNS`
            * :code:`AWSSQS`
            * :code:`AWSSimpleDB`
            * :code:`AWSUserPoolsSignIn`

        #. Under the **Build Phases** tab in your **Target**, click the **+** button on the top left and then select **New Run Script Phase**.

        #. Setup the build phase as follows. Make sure this phase is below the `Embed Frameworks` phase.

            .. code-block:: bash

                Shell /bin/sh

                bash "${BUILT_PRODUCTS_DIR}/${FRAMEWORKS_FOLDER_PATH}/AWSCore.framework/strip-frameworks.sh"

                Show environment variables in build log: Checked
                Run script only when installing: Not checked

                Input Files: Empty
                Output Files: Empty

Update the SDK to a Newer Version
=================================

This section describes how to pick up changes when a new SDK is released.

.. container:: option

    CocoaPods
        Run the following command in your project directory. CocoaPods automatically picks up the changes.

        :command:`$ pod update`

        .. note::

            If your pod update command fails, delete :file:`Podfile.lock` and :file:`Pods/`
            and then run :command:`pod install` to cleanly install the SDK.

    Carthage
        Run the following command in your project directory. Carthage automatically updates
        your frameworks with the new changes.

        :command:`$ carthage update`

    Frameworks
        #. In Xcode select the following frameworks in **Project Navigator** and press the **delete** key. Then select **Move to Trash**:

            * :code:`AWSAuth`
            * :code:`AWSAuthCore`
            * :code:`AWSAuthUI`
            * :code:`AWSAutoScaling`
            * :code:`AWSCloudWatch`
            * :code:`AWSCognito`
            * :code:`AWSCognitoAuth`
            * :code:`AWSCognitoIdentityProvider`
            * :code:`AWSCognitoIdentityProviderASF`
            * :code:`AWSCognitoSync`
            * :code:`AWSCore`
            * :code:`AWSDynamoDB`
            * :code:`AWSEC2`
            * :code:`AWSElasticLoadBalancing`
            * :code:`AWSFacebookSignIn`
            * :code:`AWSGoogleSignIn`
            * :code:`AWSIoT`
            * :code:`AWSKMS`
            * :code:`AWSKinesis`
            * :code:`AWSLambda`
            * :code:`AWSLex`
            * :code:`AWSLogs`
            * :code:`AWSMachineLearning`
            * :code:`AWSMobileAnalytics`
            * :code:`AWSMobileClient`
            * :code:`AWSPinpoint`
            * :code:`AWSPolly`
            * :code:`AWSRekognition`
            * :code:`AWSS3`
            * :code:`AWSSES`
            * :code:`AWSSNS`
            * :code:`AWSSQS`
            * :code:`AWSSimpleDB`
            * :code:`AWSUserPoolsSignIn`

        #. Follow the Frameworks installation steps in the previous section, to include the new version of the SDK.


Logging
=======

As of version 2.5.4 of this SDK, logging utilizes `CocoaLumberjack SDK <https://github.com/CocoaLumberjack/CocoaLumberjack>`_, a flexible, fast, open source logging framework. It supports many capabilities including the ability to set logging level per output target, for instance, concise messages logged to the console and verbose messages to a log file.

CocoaLumberjack logging levels are additive such that when the level is set to verbose, all messages from the levels below verbose are logged. It is also possible to set custom logging to meet your needs. For more information, see `CocoaLumberjack Logging Levels <https://github.com/CocoaLumberjack/CocoaLumberjack/blob/master/Documentation/CustomLogLevels.md>`_

Changing Logging Level
----------------------

You can change the logging level to suit the phase of your development cycle by importing AWSCore and calling:

    .. container:: option

        iOS - Swift
            :code:`AWSDDLog.sharedInstance().logLevel = .verbose`

            The following logging level options are available:

            - ``.off``
            - ``.error``
            - ``.warning``
            - ``.info``
            - ``.debug``
            - ``.verbose``

            We recommend setting the log level to ``.off`` before publishing to the App Store.

        iOS - Objective-C
            :code:`[AWSDDLog sharedInstance].logLevel = AWSDDLogLevelVerbose;`

            The following logging level options are available:

            - ``AWSDDLogLevelOff``
            - ``AWSDDLogLevelError``
            - ``AWSDDLogLevelWarning``
            - ``AWSDDLogLevelInfo``
            - ``AWSDDLogLevelDebug``
            - ``AWSDDLogLevelVerbose``

            We recommend setting the log level to ``AWSDDLogLevelOff`` before publishing to the App Store.


Targeting Log Output
--------------------

CocoaLumberjack can direct logs to file or used as a framework that integrates with the Xcode console.

To initialize logging to files, use the following code:

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let fileLogger: AWSDDFileLogger = AWSDDFileLogger() // File Logger
                fileLogger.rollingFrequency = TimeInterval(60*60*24)  // 24 hours
                fileLogger.logFileManager.maximumNumberOfLogFiles = 7
                AWSDDLog.add(fileLogger)

        iOS - Objective-C
            .. code-block:: objc

                AWSDDFileLogger *fileLogger = [[AWSDDFileLogger alloc] init]; // File Logger
                fileLogger.rollingFrequency = 60 * 60 * 24; // 24 hour rolling
                fileLogger.logFileManager.maximumNumberOfLogFiles = 7;
                [AWSDDLog addLogger:fileLogger];

To initialize logging to your Xcode console, use the following code:

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                AWSDDLog.add(AWSDDTTYLogger.sharedInstance) // TTY = Xcode console

        iOS - Objective-C
            .. code-block:: objc

                [AWSDDLog addLogger:[AWSDDTTYLogger sharedInstance]]; // TTY = Xcode console

To learn more, see `CocoaLumberjack <https://github.com/CocoaLumberjack/CocoaLumberjack>`_ on GitHub.

Sample Apps
===========

The AWS Mobile SDK for iOS includes sample apps that demonstrate common use cases.

**Amazon Cognito Your User Pools Sample** (`Objective-C <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/CognitoYourUserPools-Sample/Objective-C/>`__)

    This sample demonstrates how sign up and sign in a user to display an authenticated portion of your app.

    AWS services demonstrated:

    - `Amazon Cognito Pools <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`_
    - `Amazon Cognito Identity <http://aws.amazon.com/cognito/>`_

**Amazon Cognito Sync Sample**
(`Swift <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/CognitoSync-Sample/Swift/>`__,
`Objective-C <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/CognitoSync-Sample/Objective-C/>`__)

    This sample demonstrates how to securely manage and sync your mobile app data. It also demonstrates how to create unique identities using login providers including Facebook, Google, and Login with Amazon.

    AWS services demonstrated:

    - `Amazon Cognito Sync <http://aws.amazon.com/cognito/>`_
    - `Amazon Cognito Identity <http://aws.amazon.com/cognito/>`_

**Amazon DynamoDB Object Mapper Sample**
(`Swift <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/DynamoDBObjectMapper-Sample/Swift>`__, `Objective-C <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/DynamoDBObjectMapper-Sample/Objective-C/>`__)

    This sample demonstrates how to insert, update, delete, query items using DynamoDBObjectMapper.

    AWS services demonstrated:

    - `Amazon DynamoDB <http://aws.amazon.com/dynamodb/>`_
    - `Amazon Cognito Identity <http://aws.amazon.com/cognito/>`_

**Amazon S3 Transfer Utility Sample**
(`Swift <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferUtility-Sample/Swift/>`__, `Objective-C <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/S3TransferUtility-Sample/Objective-C/>`__)

    This sample demonstrates how to use the Amazon S3 TransferUtility to download / upload files.

    AWS services demonstrated:

    - `Amazon S3 <http://aws.amazon.com/s3/>`_
    - `Amazon Cognito Identity <http://aws.amazon.com/cognito/>`_

**Amazon SNS Mobile Push and Mobile Analytics Sample**
(`Swift <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/SNS-MobileAnalytics-Sample/Swift/>`__, `Objective-C <https://github.com/awslabs/aws-sdk-ios-samples/tree/master/SNS-MobileAnalytics-Sample/Objective-C/>`_)

    This sample demonstrates how to set up Amazon SNS mobile push notifications and to record events using Amazon Mobile Analytics.

    AWS services demonstrated:

    - `Amazon SNS (mobile push notification) <http://aws.amazon.com/sns/>`_
    - `Amazon Mobile Analytics <http://aws.amazon.com/mobileanalytics/>`_
    - `Amazon Cognito Identity <http://aws.amazon.com/cognito/>`_

Install the Reference Documentation in Xcode
============================================

The AWS Mobile SDK for iOS includes documentation in the DocSets format that you can view within
Xcode. The easiest way to install the documentation is to use the macOS terminal.

To install the DocSet for Xcode
-------------------------------

Open the macOS terminal and go to the directory containing the expanded
archive. For example:

    :command:`$ cd ~/Downloads/aws-ios-sdk-2.5.0`

.. note::

    Replace :command:`2.5.0` in the preceding example with the
    version number of the AWS Mobile SDK for iOS that you downloaded.

Create a directory called
:file:`~/Library/Developer/Shared/Documentation/DocSets`:


    :command:`$ mkdir -p ~/Library/Developer/Shared/Documentation/DocSets`

Copy (or move) :file:`documentation/com.amazon.aws.ios.docset`
from the SDK installation files to the directory you created in the previous
step:

    :command:`$ mv documentation/com.amazon.aws.ios.docset ~/Library/Developer/Shared/Documentation/DocSets/`

If Xcode was running during this procedure, restart Xcode. To browse the
documentation, go to :strong:`Help`, click :strong:`Documentation and API Reference`, and select :strong:`AWS Mobile SDK for iOS v2.0 Documentation`
(where '2.0' is the appropriate version number).

Next Steps
==========

- **Run the demos**: View our `sample iOS apps
  <https://github.com/awslabs/aws-sdk-iOS-samples>`_ that demonstrate common use cases. To run
  the sample apps, set up the SDK for iOS as described above, and then follow the instructions
  contained in the README files of the individual samples.

- **Read the API Reference**: View the `API Reference
  <https://docs.aws.amazon.com/AWSiOSSDK/latest/>`_ for the AWS Mobile SDK for Android.

- **Try AWS Mobile Hub**: Quickly configure and provision an AWS cloud backend for many common mobile
  app features, and download end to end working iOS demonstration projects, SDK, and helper code, all
  generated based on your choices.

- **Ask questions**: Post questions on the :forum:`AWS Mobile SDK Forums <88>`.


