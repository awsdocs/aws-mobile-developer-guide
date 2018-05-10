.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-mobile-sdk-migrate:

###################################
Upgrade an Existing |AMH|-based App
###################################

.. meta::
   :description: Integrate |AMHlong| features into your existing mobile app. Quickly add a powerful
      cloud backend that scales in capacity and cost.

This section provides information about updating existing apps that use a |AMH| custom SDK to use the AWS
Mobile SDK version 2.6.x.

If you did not download custom files from |AMH| and incorporate them into your app, try starting at
:ref:`getting-started`.

.. _aws-mobile-sdk-migrate-overview:

Overview
========


In previous versions of the SDK, |AMH| app makers downloaded and incorporated a folder
(:file:`AmazonAws` for iOS, :file:`amazonaws` for Android) containing an SDK and helper code. The
SDK and helper code were customized to use the unique AWS resources created for each |AMH| project.

In 2.6.+, the SDK is simpler to use. Functions that previously resided in the
Mobile Hub-supplied helper code have been moved into the SDK. To tie an app's code to the unique AWS
resources of its |AMH| project, you can now download and incorporate a single configuration file,
:file:`awsconfiguration.json`.


.. _aws-mobile-sdk-migrate-changes-build:

Add the SDK to Your App
=======================


#. Download your |AMH| project configuration file.


   #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

   #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file
      that connects your app to your backend.


      .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
         :scale: 100
         :alt: Image of the Download Configuration Files button in the |AMH| console.

      .. only:: pdf

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 50

      .. only:: kindle

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 75

   #. Optionally, if you have enabled NoSQL Database or Cloud Logic, under :guilabel:`NoSQL / Cloud
      Logic` at the bottom of the page, choose the :guilabel:`Downloads` menu, then choose your
      platform.

      .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
         :scale: 100
         :alt: Image of the Download Configuration Files button in the |AMH| console.

      .. only:: pdf

         .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
            :scale: 50

      .. only:: kindle

         .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
            :scale: 75

      :emphasis:`Remember:`

      Each time you change the |AMH| project for your app, download and use an updated
      :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or
      Cloud Logic are changed, also download and use updated files for those features.

   #. Incorporate your configuration file(s) into your app.

      .. container:: option

         Android - Java
            In the Xcode Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 100
                  :alt: Image of the Download Configuration Files button in the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                     :scale: 75

            #. From the location where configuration files were downloaded in a previous step, drag
               :file:`awsconfiguration.json` into the :file:`res/raw` folder.

            #. If NoSQL Database is enabled in your project, from the location where you downloaded
               the data model file(s), drag and drop each file with the form of
               :file:`{your-table-name}DO.java` into the folder that contains your main activity.

            #. If Cloud Logic is enabled in your project:, from the location where you downloaded the
               data model file(s), drag and drop all files in that folder into the Xcode project
               folder that contains :file:`AppDelegate.swift`.


         iOS - Swift
            Add the backend service configuration and data model files you downloaded from the
            |AMH| console, The data object files provide set and get methods for each attribute
            of a |DDB| table they model.


               #. From the location where your |AMH| configuration file was downloaded in a previous
                  step, drag :file:`awsconfiguration.json` into the folder containing your
                  :file:`info.plist` file in your Xcode project.

                  Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

               #. If NoSQL Database is enabled, from the location where you downloaded the data
                  model file(s), drag and drop each file with the form of
                  :file:`{your-table-name}.swift` into the folder that contains your
                  :file:`AppDelegate.swift`.

                  Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

               #. If Cloud Logic is enabled, from the location where you downloaded the data model
                  file(s), drag and drop each file with the form of :file:`{your-api-name}.*` into
                  the folder that contains your :file:`AppDelegate.swift`.

                  Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.


#. Required Upgrade Steps

   .. container:: option

      Android - Java
         #. Add identity providers you want to enable to the app using Gradle.

            .. code-block:: none

                implementation ('com.amazonaws:aws-android-sdk-auth-facebook:2.6.+@aar')  {transitive = true;} // optional
                implementation ('com.amazonaws:aws-android-sdk-auth-google:2.6.+@aar')  {transitive = true;}  // optional
                implementation ('com.amazonaws:aws-android-sdk-auth-userpools:2.6.+@aar')  {transitive = true;}   // optional
                implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar')  {transitive = true;}    // required for auth in 2.6.+

            If you encounter more than one version of a library, choose the one that begins with
            :code:`com.amazonaws.mobile.auth`.

         #. Increment the version number of your :code:`aws-android-sdk` from the following:

            .. code-block:: none

                implementation 'com.amazonaws:aws-android-sdk-s3:2.4.7'

            To the followin:

            .. code-block:: none

                implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'

         #. Use the new SDK-provided sign-in UI.

            The SDK now offers a library that implements an integrated sign-in UI for Facebook,
            Google, and |COG| user pools. If your app use components downloaded from Mobile
            Hub to make your sign-in UI, you can replace them with the following steps.

            Follow the steps in :ref:`add-aws-mobile-user-sign-in`

         #. Replace |SNS| with Amazon Pinpoint

            |AMH| now supports use of Amazon Pinpoint for push notifications. Amazon Pinpoint ties together
            messaging, including push, e-mail, and SMS, with Analytics. Each component can be used
            separately to communicate with users and their devices. Usage data gathered through
            analytics can be used to drive messaging campaigns.

            You can continue to use PushManager framework in an app that uses the new SDK, but you
            must maintain that code going forward.


      iOS - Swift
         #. Use Cocoapods instead of Frameworks.


            #. All AWS Frameworks in the :file:`AmazonAws/Sdk` folder should be deleted.

            #. For 2.6.x, use the following Cocoapods to install the portions of the SDK your |AMH|
               project features depend on.

               .. code-block:: none

                   platform :ios, '9.0'

                   target 'MySampleApp' do

                     use_frameworks!

                         pod 'AWSS3', '~> 2.6.13'              // User File Storage & Hosting and Streaming features
                         pod 'AWSAPIGateway', '~> 2.6.13'      // Cloud Logic feature
                         pod 'AWSDynamoDB', '~> 2.6.13'        // NoSQL Database feature
                         pod 'AWSPinpoint', '~> 2.6.13'        // Messaging and Analytics (and Push Notification) features
                         pod 'AWSLex', '~> 2.6.13'             // Conversational Bots feature
                         pod 'AWSCognito', '~> 2.6.13'         // User File Storage feature
                         pod 'AWSAuthUI', '~> 2.6.13'          // Sign-in UI feature
                         pod 'AWSGoogleSignIn', '~> 2.6.13'    // Google identity provider feature
                         pod 'AWSFacebookSignIn', '~> 2.6.13'  // Facebook identity provider feature
                         pod 'AWSUserPoolsSignIn', '~> 2.6.13' // Email and Password identity provider feature
                         pod 'AWSAuthCore', '~> 2.6.13'        // User Sign-in
                         pod 'GoogleSignIn', '~> 4.0.0'       // Google sign-in SDK

                   end

         #. Use the constants provided in the :file:`awsconfiguration.json` you downloaded instead
            of AWS values in :file:`info.plist`. The AWS values in :file:`info.plist` should be
            deleted.

         #. Replace :code:`AWSMobileHubHelper` functions.

            If your app requires user sign-in:


            * Change your import statement from the following:

              .. code-block:: none

                  import AWSAuthCore

              To the following:

              .. code-block:: none

                  import AWSMobileHubHelper

            If your app uses :code:`ContentManager` or :code:`UserFilemanager`:


            * :code:`AWSMobileHubHelper` framework's :code:`UserFileManager` and
              :code:`ContentManager` have been incorporated into the SDK's :code:`AWSContentManager`
              API. To use :code:`AWSContentManager`, change your import statement from the following:

              .. code-block:: none

                  import AWSMobileHubHelper

              To the following:

              .. code-block:: none

                  import AWSContentManager

              To continue to use calls to :code:`UserFileManager` and
              :code:`ContentManager`, download and incorporate components from the demo application
              for your |AMH| project using the following steps.

              #. Open the |AMH| console, choose your project, and then choose :guilabel:`Integrate`
                 on the left.

              #. Under :guilabel:`Demo Application`, choose :guilabel:`Download`.

              #. Copy the :file:`MySampleApp/Sdk/Aws/AWSMobileHubContentManager.framework` folder
                 from the sample app into your Xcode project.

              #. Use the following import to make the API available.

                 .. code-block:: none

                     import AWSMobileHubContentManager

         #. Use the new SDK-provided sign-in UI

            The SDK now offers a library that implements an integrated sign-in UI for Facebook,
            Google, and |COG| user pools. If your app use components downloaded from |AMH| to make your sign-in UI, you can replace them with the following steps.


            #. Delete the :file:`SignIn` folder.

            #. Delete :code:`IdentityProfiles` registration from :file:`AWSMobileClient.swift` (no longer supported).

            #. Change the callback method signature from :code:`(result, authState, error)` to
               :code:`(result, error)` for calls to :code:`AWSSignInManager`.

            #. Follow the steps in :ref:`add-aws-mobile-user-sign-in`.

         #. Change your push notification backend from |SNS| to Amazon Pinpoint

            |AMH| now supports use of Amazon Pinpoint for push notifications. Amazon Pinpoint ties together
            messaging, including push, e-mail, and SMS, with Analytics. Each component can be used
            separately to communicate with users and their devices. Usage data gathered through
            analytics can be used to drive messaging campaigns.

            :code:`AWSMobileHubHelper` framework's :code:`UPushManager` is being replaced by the
            SDK's :code:`AWSPinpoint` API. To use :code:`AWSContentManager` change your import
            statement from the following:

            .. code-block:: none

                import AWSMobileHubHelper

            To the following:

            .. code-block:: none

                import AWSPinpoint

            Follow the steps in :ref:`add-aws-mobile-push-notifications`.




