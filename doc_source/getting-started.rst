.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _getting-started:

###########
Get Started
###########

.. meta::
   :description: Integrate |AMHlong| features into your existing mobile app. Quickly add a powerful
      cloud backend that scales in capacity and cost.

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    Add Analytics <add-aws-mobile-analytics>
    Add User Sign-in <add-aws-mobile-user-sign-in>
    Add Push Notifications <add-aws-mobile-push-notifications>
    Add NoSQL Database <add-aws-mobile-nosql-database>
    Add Data Storage <add-aws-mobile-user-data-storage>
    Add Cloud Logic <add-aws-mobile-cloud-logic>
    Add Messaging <add-aws-mobile-messaging>
    Add Conversational Bots <add-aws-mobile-conversational-bots>
    Add Hosting and Streaming <add-aws-mobile-hosting-and-streaming>

.. _add-aws-mobile-sdk:

Overview
========

The AWS Mobile Android and iOS SDKs help you build high quality mobile apps quickly and easily. They provide easy access to a range of AWS services, including Amazon Cognito, AWS Lambda, Amazon S3, Amazon Kinesis, Amazon DynamoDB, Amazon Pinpoint and many more.

.. _add-aws-mobile-sdk-basic-setup:

Set Up Your Backend
===================

#. `Sign up for the AWS Free Tier. <https://aws.amazon.com/free/>`__

#. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`__ by signing into the console. The Mobile Hub console provides a single location for managing and monitoring your app's cloud resources.

   To integrate existing AWS resources using the SDK directly, without Mobile Hub, see :doc:`Setup  Options for Android <how-to-android-sdk-setup>` or :doc:`Setup  Options for iOS <how-to-ios-sdk-setup>`.

#. Name your project, check the box to allow Mobile Hub to administer resources for you and then choose :guilabel:`Next`.

.. container:: option

    Android - Java
      #. Choose :guilabel:`Android` as your platform and then choose Next.

         .. image:: images/wizard-createproject-platform-android.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-android.png
            :scale: 75

      #. Add awsconfiguration.json to your app.

         From your download location, place :file:`awsconfiguration.json` into a :file:`res/raw` `Android Resource Directory <https://developer.android.com/studio/write/add-resources.html>`__ in your Android project. Choose :guilabel:`Next`.

      #. You are now ready to connect your app to your newly setup backend. Choose :guilabel:`Add the AWS Mobile SDK` to connect to your backend.

         .. image:: images/wizard-createproject-backendconnect.png
            :scale: 75

    iOS - Swift
      #. Pick :guilabel:`iOS` as your platform and choose Next.

         .. image:: images/wizard-createproject-platform-ios.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-ios.png
            :scale: 75

      #. Add awsconfiguration.json file to your app.

         From your download location, place :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file in your Xcode project. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog. Choose :guilabel:`Next`.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      #. You are now ready to connect your app to your newly setup backend. Choose :guilabel:`Add the AWS Mobile SDK to your app`.

         .. image:: images/wizard-createproject-backendconnect.png
            :scale: 75


Connect to Your Backend
====================

.. container:: option

   Android - Java
      #. Prerequisites

         Install Android Studio version 2.33 or higher.

         Install Android SDK v7.11 (Nougat), API level 25.

      #. Your :file:`AndroidManifest.xml` must contain:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add dependencies to your :file:`app/build.gradle`, then choose :guilabel:`Sync Now` in the upper right of Android Studio. This libraries enable basic AWS functions, like credentials, and analytics.

         .. code-block:: java

             dependencies {
                 compile ('com.amazonaws:aws-android-sdk-mobile-client:2.6.7@aar') { transitive = true; }
             }

      #. Add the following code to the :code:`onCreate` method of your main or startup activity. This will establish a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

         .. code-block:: java

            import com.amazonaws.mobile.client.AWSMobileClient;

              public class YourMainActivity extends Activity {
                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);

                    AWSMobileClient.getInstance().initialize(this).execute();
                 }
              }

         Your app is now set up to interact with the AWS services you configured in your Mobile Hub project!


         Choose the Run icon in Android Studio to build your app and run it on your device/emulator. Look for :code:`Welcome to AWS!` in your Android Logcat output (choose :guilabel:`View > Tool Windows > Logcat`).


   iOS - Swift
      #. Prerequisites

         Install Xcode version 8.0 or later.

      #. Install Cocoapods. From a terminal window run:

         .. code-block:: bash

            sudo gem install cocoapods

      #. Create :file:`Podfile`. From a terminal window, navigate to the directory that contains your project's :file:`.xcodeproj` file and run:

          .. code-block:: bash

              pod init

      #. Add core AWS Mobile SDK components to your build.

         .. code-block:: none

              platform :ios, '9.0'
              target :'YOUR-APP-NAME' do
                  use_frameworks!
                  pod 'AWSMobileClient', '~> 2.6.6'
                  # other pods
              end

         Then install dependencies by runnng:

         .. code-block:: none

             pod install --repo-update

         .. list-table::
             :widths: 1 6

             * - Use **ONLY** your .xcworkspace

               - Use the .xcworkspace file generated by cocoapods for all further development. If you used the :file:`xcodeproj` to open your project, close it now and do not use it again.

      #. Add the following code to your AppDelegate to establish a run-time connection with AWS Mobile.

         .. code-block:: swift

            import UIKit
            import AWSMobileClient

            @UIApplicationMain
            class AppDelegate: UIResponder, UIApplicationDelegate {

            func application(_ application: UIApplication,
                             didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                // Override point for customization after application launch.

                // Create AWSMobileClient to connect with AWS
                return AWSMobileClient.sharedInstance().interceptApplication(
                    application,
                    didFinishLaunchingWithOptions: launchOptions)

            }

      #. `Optional`: If you want to make sure you're connected to AWS, import :code:`AWSCore` and add the following code to :code:`didFinishLaunchingWithOptions` before you return :code:`AWSMobileClient`.

         .. code-block:: swift

            import AWSCore

            //. . .

            AWSDDLog.add(AWSDDTTYLogger.sharedInstance)
            AWSDDLog.sharedInstance.logLevel = .info

        Your app is now set up to interact with the AWS services you configured in your |AMH| project! Choose the run icon in the top left of the Xcode window or type Command-R to build and run your app. Look for  :code:`Welcome to AWS!` in the log output.

.. _add-aws-mobile-sdk-next-steps:

Next Steps
==========

  * :ref:`Add Analytics <add-aws-mobile-analytics-app>`

  * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

  * :ref:`Add Push Notification <add-aws-mobile-push-notifications>`

  * :ref:`Add NoSQL Database <add-aws-mobile-nosql-database>`

  * :ref:`Add User Data Storage <add-aws-mobile-user-data-storage>`

  * :ref:`Add Cloud logic <cloud-backend>`

  * :ref:`Add Messaging <add-aws-mobile-messaging>`

  * :ref:`Add Conversational Bots <add-aws-mobile-conversational-bots>`

  * :ref:`Add Hosting and Streaming <add-aws-mobile-hosting-and-streaming>`



