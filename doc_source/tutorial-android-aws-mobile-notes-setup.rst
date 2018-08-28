.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-setup:

########################
A Simple Note-Taking App
########################

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Analytics <tutorial-android-aws-mobile-notes-analytics>
   Authentication <tutorial-android-aws-mobile-notes-auth>
   Serverless Backend <tutorial-android-aws-mobile-notes-data>

In this tutorial, you start with a working app, driven from locally stored data, and then add cloud-enabled features as follows:

- :ref:`Add analytics to your app <tutorial-android-aws-mobile-notes-analytics>` so you can view demographic information about your users.

- :ref:`Add a simple sign-in/sign-up flow <tutorial-android-aws-mobile-notes-auth>` for authentication.

- :ref:`Access data stores in the AWS cloud <tutorial-android-aws-mobile-notes-data>`, so that a user's notes are available to them on any device with the app installed.

.. image:: images/tutorial-notes-app-anim.gif
   :scale: 100
   :alt: Demonstration of the Notes tutorial app you can download.

You should be able to complete the setup section of this tutorial within 10-15 minutes after you have installed all required software. After you complete the following instructions, you can run the project on your local system.

.. _android-tutorial-notes-getting-started:

Getting Started
---------------

Before you begin, do the following:

#. Complete the `Getting Started <https://aws-amplify.github.io/media/get_started>`__ instructions to install the Amplify CLI.
#. Download and install `Android Studio <https://developer.android.com/studio/index.html>`__ version 3.0.1 or later.
#. Download and install `Android SDK <https://developer.android.com/studio/intro/update.html#sdk-manager>`__ version 8.0 (Oreo), API level 26.
#. Install an `Android Emulator <https://developer.android.com/studio/run/managing-avds.html>`__. The app works with both phone and tablet emulators (for example, the Nexus 5X or Pixel C).

Download the Source Code
------------------------

Download the source code as a `ZIP file <https://github.com/aws-samples/aws-mobile-android-notes-tutorial/archive/master.zip>`__.  After the download is complete, unpack the downloaded ZIP file.

Compile the Source Code
-----------------------

To compile the source code, do the following:

1. Start :guilabel:`Android Studio`.
2. If you have a project open already, choose :guilabel:`File > Close Project`.
3. Choose :guilabel:`Open an existing Android Studio project`.
4. Find and choose the :guilabel:`aws-mobile-android-notes-tutorial-master` project in your file system, and then choose :guilabel:`OK`.

   .. image:: images/open-project.png
      :scale: 100
      :alt: Find MyNotes folder in the Android Studio project explorer.

5. On the menu bar, choose :guilabel:`File > Sync Project with Gradle Files`.
6. On the menu bar, choose :guilabel:`Build > Make Project`.

The compilation step should finish with no errors. Errors are displayed in the :guilabel:`Messages` window, which is available on the status bar at the bottom of the project.

Run the Project in an Emulator
------------------------------

If you haven't already done so, create a new emulator as follows:

#. Choose :guilabel:`Tools > Android > AVD Manager`.
#. Choose :guilabel:`Create Virtual Device....`
#. Choose :guilabel:`Phone  > Nexus 5X`, and then choose :guilabel:`Next`.
#. Choose the :guilabel:`x86 Images` tab, and then choose :guilabel:`Android 8.0 (Google APIs)`.

   -  If you didn't previously downloaded the image, you can download
      it from this screen.

#. Choose :guilabel:`Next`.
#. Choose :guilabel:`Finish`.
#. Close the AVD Manager.

Run the project in an emulator as follows:

#. Choose :guilabel:`Run` > :guilabel:`Run 'app'`.
#. Choose the :guilabel:`Nexus 5X API 26` virtual device.
#. Choose :guilabel:`OK`.

If it isn't already running, the Android emulator starts and then the application runs. You should be able to interact with the application as you would any other mobile app. Try pressing on the plus sign :guilabel:`+` at the of the app to create a note, or choose a note to show in the editor screen. A unique ID for each note is displayed in the list view underneath the note's title.

Troubleshooting
---------------------

The most common problems at this stage involve issues with the installation of Java, Android Studio, the Android SDK, or the Android Emulator. Google provides detailed instructions about `Android Studio <https://developer.android.com/studio/index.html>`__ and dependent features.

Next Steps
----------

Next, :ref:`integrate application analytics <tutorial-android-aws-mobile-notes-analytics>` into your project.

