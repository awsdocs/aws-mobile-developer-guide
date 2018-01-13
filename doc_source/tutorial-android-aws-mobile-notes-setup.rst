.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-setup:

########################
A Simple Note-taking App
########################

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Analytics <tutorial-android-aws-mobile-notes-analytics>
   Authentication <tutorial-android-aws-mobile-notes-auth>
   NoSQL Data <tutorial-android-aws-mobile-notes-data>

Start with a working app and then add cloud enable features. In this tutorial you will take a working app, driven from locally stored data, and then:

- :ref:`Add analytics to your app <tutorial-android-aws-mobile-notes-analytics>` so you can view demographic information about your users.

- :ref:`Add a simple sign-in/sign-up flow <tutorial-android-aws-mobile-notes-analytics>` for authentication.

- :ref:`Access data stores in the AWS <tutorial-android-aws-mobile-notes-data>` cloud, so that a user's notes are available to them on any device with the app installed.

.. image:: images/tutorial-notes-app-anim.gif
   :scale: 100
   :alt: Demonstration of the Notes tutorial app you can download.

You should be able to complete the setup section of this tutorial within 10-15 minutes after
you have installed all required software. Once you complete the instructions on this page, you can run the project on your local system.

Getting Started
---------------

Before beginning, you must:

-  Download and install `Android Studio <https://developer.android.com/studio/index.html>`_ version 2.33 or later.

-  Download an install `Android SDK <https://developer.android.com/studio/intro/update.html#sdk-manager>`_ version 7.11 (Nougat), API level 25.

-  Install an `Android Emulator <https://developer.android.com/studio/run/managing-avds.html>`_ - the app works with both phone and tablet emulators (for example, the Nexus 5X or Pixel C).

Windows Specific Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install `Git for Windows <https://git-scm.com/download/win>`_.

Mac Specific Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install
   `XCode <https://itunes.apple.com/us/app/xcode/id497799835?mt=12>`__
   using the Mac App Store.

-  Configure the XCode command line tools. Run
   ``xcode-select --install`` from a Terminal window.

   .. list-table::
      :widths: 1

      * - Why do I need XCode?

          The XCode package includes command line tools that are used on a Mac to assist with software development. You don't need to run the UI XCode application.

Download the Source code
------------------------

You can download the source code as a `ZIP
file <https://github.com/aws-samples/aws-mobile-android-notes-tutorial/archive/master.zip>`_,
or you can download the source code directly from GitHub.

1. Log in to `GitHub <https://github.com/>`_. If you do not have a GitHub account, `sign up for
   GitHub <https://github.com/join?source=header-home>`_ first.
2. Browse to  https://github.com/aws-samples/aws-mobile-android-notes-tutorial
3. Choose :guilabel:`Fork`.
4. Choose your GitHub account.

This will create a copy of the Android Tutorials in your GitHub account.
To create a copy on your local system, open a terminal window and type:

.. code-block:: bash

    git clone  https://github.com/aws-samples/aws-mobile-android-notes-tutorial

This will copy the files within the project to your local system. The
directory :file:`aws-mobile-android-notes-tutorials` will be created for you.

.. list-table::
   :widths: 2 6

   * - **Note**

     - Git is required

       This step will fail if you have not properly installed Git for your
       platform. If this happens, download and unpack the
       `ZIP file <https://github.com/aws-samples/aws-mobile-android-notes-tutorial/archive/master.zip>`_ instead.

Compile the Source Code
-----------------------

To compile the source code:

1. Start :guilabel:`Android Studio`.
2. If you have a project open already, choose :guilabel:`File > Close Project`.
3. Choose :guilabel:`Open an existing Android Studio project`.
4. Find and choose the :guilabel:`MyNotes` project in your file system, then
   choose :guilabel:`OK`.

   .. image:: images/open-project.png
      :scale: 100
      :alt: Find MyNotes folder in the Android Studio project explorer.

5. Select :guilabel:`Build > Make Project` from the menu bar.

The compilation step should complete with no errors. Errors are
displayed within the :guilabel:`Messages` window, available on the status bar at
the bottom of the project.

Run the Project in an Emulator
------------------------------

Create a new emulator if you have not done so already:

1. Select :guilabel:`Tools > Android > AVD Manager`.
2. Choose :guilabel:`Create Virtual Device....`
3. Select :guilabel:`Phone`  > Nexus 5X`, then choose :guilabel:`Next`.
4. Select the :guilabel:`x86 Images` tab, then select :guilabel:`Android 7.1.1 (Google APIs)`.

   -  If you have not previously downloaded the image, you can download
      it from this screen.

5. Choose :guilabel:`Next`.
6. Choose :guilabel:`Finish`.

Run the project in an emulator.

1. Select :guilabel:`Run` > :guilabel:`Run app`.
2. Select the :guilabel:`Nexus 5X API 25` virtual device.
3. Choose :guilabel:`OK`.

The Android emulator will boot (if it is not already started) and the
application will run. You should be able to interact with the
application as you would any other mobile app. Try choosing on the :guilabel:`+` at
the bottom to create a note, or choose on a note to show the editor
screen. A unique ID for each note is displayed in
the list view underneath the note's title.

Running into Problems
---------------------

The most common problems at this stage involve issues with the
installation of Java, Android Studio, the Android SDK or the Android
Emulator. Google provides detailed instructions on `Android Studio <https://developer.android.com/studio/index.html>`_ and
dependent features.

Next Steps
----------

Next, :ref:`integrate application analytics <tutorial-android-aws-mobile-notes-analytics>` into your project.

