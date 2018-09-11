
.. _getting-started:

###########
Get Started
###########

.. meta::
   :description: Integrate AWS Amplify features into your existing mobile app. Quickly add a powerful cloud backend that scales in capacity and cost.

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    Add Analytics <add-aws-mobile-analytics>
    Add User Sign-in <add-aws-mobile-user-sign-in>
    Add Push Notifications <add-aws-mobile-push-notifications>
    Add User File Storage <add-aws-mobile-user-data-storage>
    Add Serverless Backend (AWS AppSync) <add-aws-mobile-serverless-backend>
    Add Cloud Logic <add-aws-mobile-cloud-logic>
    Add Messaging <add-aws-mobile-messaging>

.. _add-aws-mobile-sdk:

Choose your platform:

.. list-table::
   :widths: 1 1 1

   * - .. image:: images/android-java.png
          :target: getting-started.html#android-java

     - .. image:: images/android-kotlin.png
          :target: getting-started.html#android-kotlin

     - .. image:: images/ios-swift.png
          :target: getting-started.html#ios-swift

.. container:: option

   Android - Java
       .. _android-java:

       Get started building a cloud-powered Android app using the AWS Amplify CLI and the AWS SDK for Android. This page guides you through setting up an initial backend and integrating the SDK into your app.

   Android - Kotlin
       .. _android-kotlin:

       Get started building a cloud-powered Android app using the AWS Amplify CLI and the AWS SDK for Android. This page guides you through setting up an initial backend and integrating the SDK into your app.

   iOS - Swift
       .. _ios-swift:

       Get started building a cloud-powered iOS app using the AWS Amplify CLI and the AWS SDK for iOS. This page guides you through setting up an initial backend and integrating the SDK into your app.

.. _add-aws-mobile-sdk-basic-setup-prerequisites:

Step 1: Set Up Your Development Environment
===========================================

We strongly recommend that you use the Amplify CLI for building the serverless backend for your app. If you have already installed the CLI, skip ahead to :ref:`Step 2 <add-aws-mobile-sdk-basic-setup>`.

*  `Sign up for an AWS Account <https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start>`__.

*  Install `Node.js <https://nodejs.org/>`__ and npm (if they are not already installed).

.. note::

   Verify that you are running at least Node.js version 8.x or greater and npm version 5.x or greater by running :code:`node -v` and :code:`npm -v` in a terminal/console window. Older versions aren't supported and might generate errors.

To install and configure the Amplify CLI globally, run the following commands in a terminal window.

.. code-block:: bash

   $ npm install -g @aws-amplify/cli

   $ amplify configure

Minimum requirements for your development environment are as follows.

    .. container:: option

       Android - Java
           * Choose the Android Java app project you want to integrate with an AWS backend.

           * `Install Android Studio <https://developer.android.com/studio/index.html#downloads>`__ version 2.33 or higher.

           * Install Android SDK for API level 23 (Android SDK 6.0).

       Android - Kotlin
           * Choose the Android Kotlin app project you want to integrate with an AWS backend.

           * `Install Android Studio <https://developer.android.com/studio/index.html#downloads>`__ version 2.33 or higher.

           * Install Android SDK for API level 23 (Android SDK 6.0).

       iOS - Swift
          * Choose the iOS app project you want to integrate with an AWS backend.

          * `Install Xcode <https://developer.apple.com/xcode/downloads/>`__ version 8.0 or later.


.. _add-aws-mobile-sdk-basic-setup:

Step 2: Set Up Your Backend
===========================

#. The CLI prompts you for configuration parameters.

    .. container:: option

       Android - Java
           In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

          .. code-block:: none

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify init

       Android - Kotlin
           In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

          .. code-block:: none

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify init

       iOS - Swift
           In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`xcodeproj` file), and add the SDK to your app.

          .. code-block:: none

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify init

#. To create your backend AWS resources and add a configuration file to your app, run the following:

   .. container:: option

       Android - Java
          .. code-block:: bash

            $ amplify push


       Android - Kotlin
          .. code-block:: none

            $ amplify push

       iOS - Swift
          .. code-block:: none

            $ amplify push

          In the Finder, navigate to the folder containing your app :file:`.xcodeproj` file. From there, drag :code:`awsconfiguration.json` to Xcode under the top Project Navigator folder (the folder name should match your Xcode project name). In the :guilabel:`Options` dialog box that appears, do the following:

          * Clear the :guilabel:`Copy items if needed` check box.

          * Choose :guilabel:`Create groups`, and then choose :guilabel:`Next`.

#. To verify that the CLI is set up for your app, run the following command. The CLI displays a status table with no resources listed. As you add categories to your app, backend resources created for your app are listed in this table.

   .. code-block:: none

      $ amplify status
      | Category | Resource name | Operation | Provider plugin |
      | -------- | ------------- | --------- | --------------- |

   Use the steps in the next section to configure the connection between your app and the serverless backend.

.. _add-aws-mobile-sdk-connect-to-your-backend:

Step 3: Connect to Your Backend
===============================

Perform the following steps to set up a connection to AWS services that you'll use in the Get Started section of this guide.

.. container:: option

   Android - Java
      #. Add dependencies to your :file:`app/build.gradle`, and then choose :guilabel:`Sync Now` on the upper-right side of Android Studio. These libraries enable basic AWS functions, like credentials and analytics.

         .. code-block:: java

             dependencies {
                 implementation 'com.amazonaws:aws-android-sdk-core:2.6.+'
             }

      #. Your :file:`AndroidManifest.xml` must contain the following:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      Your app is now ready for you to add cloud-powered features. We recommend :ref:`adding analytics <add-aws-mobile-analytics>` as your first feature.

   Android - Kotlin
      #. Add dependencies to your :file:`app/build.gradle`, and then choose :guilabel:`Sync Now` on the upper-right side of Android Studio. These libraries enable basic AWS functions, like credentials and analytics.

         .. code-block:: java

             dependencies {
                 implementation 'com.amazonaws:aws-android-sdk-core:2.6.+'
             }

      #. Your :file:`AndroidManifest.xml` must contain the following:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      Your app is now ready for you to add cloud-powered features. We recommend :ref:`adding analytics <add-aws-mobile-analytics>` as your first feature.

   iOS - Swift
      #. Install Cocoapods. From a terminal window run the following:

         .. code-block:: none

            sudo gem install cocoapods

      #. Create :file:`Podfile`. From a terminal window, navigate to the directory that contains your project's :file:`.xcodeproj` file and run the following:

          .. code-block:: none

              pod init

      #. Open :file:`Podfile` in a text editor and add the pod for core AWS Mobile SDK components to your build.

         .. code-block:: none

              platform :ios, '9.0'
              target :'YOUR-APP-NAME' do
                  use_frameworks!

                  pod 'AWSCore', '~> 2.6.13'

                  # other pods
              end

      #. Install dependencies by runnng the following:

         .. code-block:: none

             pod install --repo-update

         If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you might need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

      #. The command :code:`pod install` creates a new workspace file. Close your Xcode project and reopen it using :file:`./YOUR-PROJECT-NAME.xcworkspace`.

         .. list-table::
             :widths: 1 6

             * - Use **ONLY** your .xcworkspace

               - Remember to always use :file:`./YOUR-PROJECT-NAME.xcworkspace` to open your Xcode project from now on.

      #. Rebuild your app after reopening it in the workspace to resolve APIs from new libraries called in your code. This is a good practice any time you add import statements.

      Your app is now ready for you to add cloud-powered features. We recommend :ref:`adding analytics <add-aws-mobile-analytics>` as your first feature.



.. _add-aws-mobile-sdk-next-steps:

Next Steps
==========

  * :ref:`Add Analytics <add-aws-mobile-analytics>`

  * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

  * :ref:`Add Push Notification <add-aws-mobile-push-notifications>`

  * :ref:`Add User File Storage <add-aws-mobile-user-data-storage>`

  * :ref:`Add Serverless Backend <add-aws-mobile-serverless-backend>`

  * :ref:`Add Cloud Logic <add-aws-mobile-cloud-logic>`

  * :ref:`Add Messaging <add-aws-mobile-messaging>`

