
.. _reference-mobile-hub-backend-setup:

#####################################################
Use the AWS Mobile Hub Console to Set Up Your Backend
#####################################################


.. meta::
   :description: Use the |AMH| Console to Set Up Your Backend

AWS Mobile enables you to create, configure, and integrate common mobile app backend features using AWS resources. With the :ref:`Amplify CLI <add-aws-mobile-sdk>` you can use the command line to add the AWS Mobile SDK to your app and create your AWS resources.

The following steps show how to perform the same actions in the Mobile Hub console, if you prefer a console experience or need to manage an existing Mobile Hub project.

.. contents::
   :local:
   :depth: 2

.. _add-aws-mobile-sdk-basic-setup-console:

Get Started
===========

#. `Sign up for the AWS Free Tier. <https://aws.amazon.com/free/>`__

#. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`__ by signing into the console. The Mobile Hub console provides a single location for managing and monitoring your app's cloud resources.

   To integrate existing AWS resources using the SDK directly, without Mobile Hub, see :doc:`Setup  Options for Android <how-to-android-sdk-setup>` or :doc:`Setup  Options for iOS <how-to-ios-sdk-setup>`.

#. Name your project, check the box to allow Mobile Hub to administer resources for you and then choose :guilabel:`Add`.

.. container:: option

    Android - Java
      #. Choose :guilabel:`Android` as your platform and then choose Next.

         .. image:: images/wizard-createproject-platform-android.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-android.png
            :scale: 75


      #. Add the backend service configuration file to your app.

         In the Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of creating a raw directory in Android Studio.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         From the location where configuration file, :file:`awsconfiguration.json`, was downloaded in a previous step, drag it into the :file:`res/raw` folder.  Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      Your backend is now configured. Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-sdk-connect-to-your-backend>`.

    Android - Kotlin
      #. Choose :guilabel:`Android` as your platform and then choose Next.

         .. image:: images/wizard-createproject-platform-android.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-android.png
            :scale: 75


      #. Add the backend service configuration file to your app.

         In the Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of creating a raw directory in Android Studio.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         From the location where configuration file, :file:`awsconfiguration.json`, was downloaded in a previous step, drag it into the :file:`res/raw` folder.  Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      Your backend is now configured. Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-sdk-connect-to-your-backend>`.


    iOS - Swift
      #. Pick :guilabel:`iOS` as your platform and choose Next.

         .. image:: images/wizard-createproject-platform-ios.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-ios.png
            :scale: 75

         .. _ios-add-backend-configuration:

      #. Add the backend service configuration file to your app.

         From your download location, place :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file in your Xcode project. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog. Choose :guilabel:`Next`.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      Your backend is now configured. Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-sdk-connect-to-your-backend>`.

.. _setup-your-backend-analytics-console:

Add Analytics (Amazon Pinpoint)
===============================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup-console>` steps before you proceed.

#. When you create a project, we enable analytics by default in your backend. You should see a green check mark  present on the :guilabel:`Analytics` tile in your backend, indicating that the feature is enabled. If the check mark is absent, choose :guilabel:`Analytics`, and then choose :guilabel:`Enable`.

  .. image:: images/project-detail-analytics.png
     :scale: 25

Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-analytics-app>`.

After your app is connected and used:

#. To see visualizations of the analytics coming from your app, open your project in the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`__.

#. Choose :guilabel:`Analytics` on the upper right to open the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__.

  .. image:: images/analytics-link-mhconsole.png
     :alt: |AMH| console link to your project in the Amazon Pinpoint console.


.. _auth-setup-console:

Add User Sign-in (Amazon Cognito)
=================================

**Prerequisite** Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup-console>` steps before you proceed.


.. container:: option

   Email & Password
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. Choose :guilabel:`Email and Password sign-in`

         .. image:: images/add-aws-mobile-sdk-email-and-password.png

         * Choose :guilabel:`Create a new user pool`, the feature and then select sign-in settings including: allowed login methods; multi-factor authentication; and password requirements. Then choose :guilabel:`Create user pool`.

           .. image:: images/add-aws-mobile-sdk-email-and-password-create.png

         Or:

         * Choose :guilabel:`Import an existing user pool`, select a user pool from the list of pools that are  available in the account. Choose if sign-in is required, and then choose :guilabel:`Create user pool`. If you import a user pool that is in use by another app, then the two apps will share the user directory and authenticate sign-in by the same set of users.

           .. image:: images/add-aws-mobile-sdk-email-and-password-import.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the :ref:`Set up Email & Password Login <set-up-email-and-password>` steps to connect to your backend from your app.

   Facebook
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. **Configure Facebook sign-in**: Choose the feature and then type your Facebook App ID and then choose :guilabel:`Enable Facebook login`. To retrieve or create your Facebook App ID, see `Setting Up Facebook Authentication. <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-facebook-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-facebook.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the steps at :ref:`Set Up Facebook Login <set-up-facebook>` to connect to your backend from your app.


   Google
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. Configure **Google sign-in**: Choose the feature and then type in your Google Web App Client ID, and the Google Android or iOS Client ID (or both), and then choose Enable Google Sign-In. To retrieve or create your Google Client IDs, see `Setting Up Google Authentication <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-google-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-google.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the steps at :ref:`Set Up Google Login <set-up-google>` to connect to your backend from your app.



.. _setup-your-backend-push-notifications-console:

Add Push Notifications (Amazon Pinpoint)
========================================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup-console>` steps before you proceed.

#. Choose the :guilabel:`Messaging and Analytics` tile

#. Choose :guilabel:`Mobile push`.

   **For Android - Firebase/Google Cloud Messaging (FCM/GCM):** Choose :guilabel:`Android` and provide your Firebase/Google application API key and Sender ID. To retrieve or create these values, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`__ .

   **For iOS - Apple Push Notification Service (APNs):** Choose :guilabel:`iOS` and provide your Apple app P12 Certificate and, optionally, Certificate password. To retrieve or create these items, see `Setting Up iOS Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/apns-setup.html>`__.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done with configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the Push Notification documentation below to connect to your backend.

Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-push-notifications-app>`.


.. _setup-your-backend-noSQL-console:

Add NoSQL Database (Amazon DynamoDB)
====================================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before you proceed.

#. Enable :guilabel:`NoSQL Database`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`NoSQL Database` tile to enable the feature.

#. Follow the console work flow to define the tables you need. See :ref:`config-nosqldb` for details.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the NoSQL Database documentation below to connect to your backend.

#. Download the models required for your app. The data models provide set and get methods for each attribute of a |DDB| table.

Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-push-notifications-app>`.


.. _setup-your-backend-user-file-storage-console:

Add User File Storage (Amazon S3)
=================================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before you proceed.

   If you want to integrate an |S3| bucket that you have already configured, go to :ref:`Integrate an Existing Bucket <how-to-integrate-an-existing-bucket>`.

#. Enable :guilabel:`User File Storage`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User File Storage` tile to enable the feature.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the User File Storage documentation below to connect to your backend.

Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-user-data-storage-app>`.


.. _cloud-backend-console:

Add Cloud Logic (API GateWay and AWS Lambda)
============================================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before you proceed.

#. Enable :guilabel:`Cloud Logic`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`Cloud Logic` tile to enable the feature.

#. Create a new API or import one that you created in the `API Gateway console <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__.

   #. To create a new API choose :guilabel:`Create an API`.

   #. Type an :guilabel:`API Name` and :guilabel:`Description`.

   #. Configure your :guilabel:`Paths`. Paths are locations to the serverless |LAMlong| functions that handle requests to your API.

      Choose :guilabel:`Create API` to deploy a default API and its associated handler function. The default handler is a Node.js function that echoes JSON input that it receives. For more information, see `Using AWS Lambda with Amazon API Gateway <with-on-demand-https.html>`__.

      The definition of APIs and paths configured in a |AMH| project are captured in an AWS CloudFormation‎ template. The body of a request containing a template is limited to 51,200 bytes, see `AWS CloudFormation Limits <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__ for details. If your API definition is too large to fit this size, you can use the `AWS API Gateway Console <https://console.aws.amazon.com/apigateway/>`__ to create your API and the import it into your |AMH| project.

#. When you are done configuring the feature and the last operation is complete, choose your project name in the upper left to go the project details page. The banner that appears also links there.

   .. image:: images/updated-cloud-config.png

#. Choose :guilabel:`Integrate` on the app card.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

   If you have created apps for more than one platform, the :guilabel:`Integrate` button of each that is affected by your project changes will flash, indicating that there is an updated configuration file available for each of those versions.

#. Choose :guilabel:`Download Cloud Config` and replace the old the version of :code:`awsconfiguration.json` with the new download. Your app now references the latest version of your backend.

#. Choose  :guilabel:`Swift Models` to download API models that were generated for your app. These files provide access to the request surface for the API Gateway API you just created. Choose :guilabel:`Next` and follow the Cloud API documentation below to connect to your backend.

Follow the next steps at :ref:`Connect to Your Backend <cloud-logic-connect-to-your-backend>`.


.. _setup-your-backend-conversational-bots-console:

Add Conversational Bots (Amazon Lex)
====================================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup-console>` steps before you proceed.

#. Enable :guilabel:`Conversational Bots`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`Conversational Bots` tile to enable the feature.

   #. Choose one of the sample Bots or import one that you have created in the `Amazon Lex console
      <http://docs.aws.amazon.com/lex/latest/dg/what-is.html>`__.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend.

Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-conversational-bots-app>`.
