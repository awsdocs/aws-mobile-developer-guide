.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _auth-facebook-setup:


##############################
Set Up Facebook Authentication
##############################

To use the following Facebook service configuration steps to federate Facebook as a user sign-in
provider for AWS services called in your app, try the |AMHlong|  :ref:`User Sign-in feature
<user-sign-in>`.

You must first register your application with Facebook by using the `Facebook Developers portal
<https://developers.facebook.com/>`_.

|AMH| generates code that enables you to use Facebook to provide federated authentication for your
mobile app users. This topic explains how to set up Facebook as an identity provider for your app.

If you already have a Facebook app ID, copy and paste it into the :guilabel:`Facebook App ID` field
in the |AMH| console, and choose :guilabel:`Save changes`.

**To get a Facebook app ID**

#. In the `Facebook Developers portal <https://developers.facebook.com/>`_, sign in with your
   Facebook credentials.

#. From :guilabel:`Create App`, choose :guilabel:`Add a New App` (note: this menu label will be
   :guilabel:`My Apps` if you have previously created an app.

   .. image:: images/new-facebook-app.png
      :scale: 100
      :alt: Adding a new app in the Facebook Developers portal

   .. only:: pdf

      .. image:: images/new-facebook-app.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-facebook-app.png
         :scale: 85


#. If asked, choose the platform of your app that will use Facebook sign-in, and :guilabel:`basic
   setup`.

#. Type a display name for your app, select a category for your app from the :guilabel:`Category`
   drop-down list, and then choose :guilabel:`Create App ID`.

   .. image:: images/new-facebook-app-new-app-id.png
      :scale: 100
      :alt: Creating a new App ID in the Facebook Developers portal

   .. only:: pdf

      .. image:: images/new-facebook-app-new-app-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-facebook-app-new-app-id.png
         :scale: 85


#. Complete the :guilabel:`Security Check` that appears. Your new app then appears in the
   :guilabel:`Dashboard`.

   .. image:: images/new-facebook-app-id.png
      :scale: 100
      :alt: New app appearing in the Dashboard of the Facebook Developers portal

   .. only:: pdf

      .. image:: images/new-facebook-app-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-facebook-app-id.png
         :scale: 85


#. Copy the App ID and paste it into the :guilabel:`Facebook App ID` field in the |AMH| console.

   .. image:: images/facebook-app-id-console-entry.png
      :scale: 100
      :alt: Place to type the Facebook App ID in the |AMH| console

   .. only:: pdf

      .. image:: images/facebook-app-id-console-entry.png
         :scale: 65

   .. only:: kindle

      .. image:: images/facebook-app-id-console-entry.png
         :scale: 85

#. In the Facebook Developer portal's left hand navigation list, choose :guilabel:`Settings`, then
   choose :guilabel:`+ Add Platform`.

   .. image:: images/new-facebook-add-platform.png
      :scale: 100
      :alt: Choose Facebook Developer portal Settings and Add Platform to choose the platform to configure.

   .. only:: pdf

      .. image:: images/new-facebook-add-platform.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-facebook-add-platform.png
         :scale: 85


#. Choose your platform and provide information about your Mobile Hub app that Facebook will use for
   integration during credential validation.

   :guilabel:`For iOS:`

   #. Add your app's :guilabel:`Bundle ID`. (ie. :code:`com.amazon.YourProjectName`). To use the AWS
      Mobile Hub sample app project, set your this value to :code:`com.amazon.MySampleApp`.

      .. image:: images/new-facebook-add-platform-ios.png
         :scale: 100
         :alt: Provide Facebook with your iOS app's Bundle ID.

      .. only:: pdf

         .. image:: images/new-facebook-add-platform-ios.png
            :scale: 65

      .. only:: kindle

         .. image:: images/new-facebook-add-platform-ios.png
            :scale: 85


   :guilabel:`For Android:`

   #. Provide your app's :guilabel:`Google Play Package Name`. (ie. :code:`com.yourprojectname`). To
      use the AWS Mobile Hub sample app project, set this value to :code:`com.amazon.mysampleapp`.

   #. Provide your :guilabel:`Class Name` that handles deep links (ie.
      :code:`com.yourprojectname.MainActivity`). To use the AWS Mobile Hub sample app project, set
      your class name to :code:`com.mysampleapp.MainActivity`.

      .. image:: images/new-facebook-add-platform-android.png
         :scale: 100
         :alt: Provide Facebook with your Android app's Google Play Package Name.

      .. only:: pdf

         .. image:: images/new-facebook-add-platform-android.png
            :scale: 65

      .. only:: kindle

         .. image:: images/new-facebook-add-platform-android.png
            :scale: 85


   #. Provide your app's Facebook development :guilabel:`Key Hashes`. This is a value that you
      generate via a terminal in your development environment, and is unique to that environment.

      To generate a development key for your Android environment on Mac, run the following command
      line.



      .. code-block:: bash

          keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore | openssl sha1 -binary | openssl base64

      To generate a development key for your Android environment on Windows, run the following
      command line.

      .. code-block:: bash

          keytool -exportcert -alias androiddebugkey -keystore %HOMEPATH%\.android\debug.keystore | openssl sha1 -binary | openssl base64

      For more information, choose the :guilabel:`Quick Start` button in the upper left of the
      Facebook Developer Portal Add Platform dialog.

#. In the Facebook Developers portal, choose :guilabel:`Save changes`, then :guilabel:`Use this
   package name` if a dialog appears saying that Google Play has an issue with your package name.

#. Only users with roles assigned in the Facebook portal will be abel to authenticate through your
   app while it is in development (not yet published).

   To authorize users, in the Facebook Developer portal's left hand navigation list, choose
   :guilabel:`Roles`, then :guilabel:`Add Testers`. Provide a valid Facebook ID.

   .. image:: images/new-facebook-add-testers.png
      :scale: 100
      :alt: Choose Facebook Developer portal Settings and Add Platform to choose the platform to configure.

   .. only:: pdf

      .. image:: images/new-facebook-add-testers.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-facebook-add-testers.png
         :scale: 85


#. In the |AMH| console, choose :guilabel:`Save changes`.

For more information about integrating with Facebook Login, see the `Facebook Getting Started Guide
<https://developers.facebook.com/docs/facebook-login>`_.
