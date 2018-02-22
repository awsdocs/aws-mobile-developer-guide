.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-react-native-aws-mobile-notes-setup:

########################
A Simple Note-taking App
########################

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Analytics <tutorial-react-native-aws-mobile-notes-analytics>
   Authentication <tutorial-react-native-aws-mobile-notes-auth>
   NoSQL Data <tutorial-react-native-aws-mobile-notes-data>

Start with a working app and then add cloud enabled features. In this tutorial you will take a working app, driven from locally stored data, and then:

- :ref:`Add analytics to your app <tutorial-react-native-aws-mobile-notes-analytics>` so you can view demographic information about your users.

- :ref:`Add a simple sign-in/sign-up flow <tutorial-react-native-aws-mobile-notes-analytics>` for authentication.

- :ref:`Access data stores in the AWS <tutorial-react-native-aws-mobile-notes-data>` cloud, so that a user's notes are available to them on any device with the app installed.

.. image:: images/tutorial-react-native-notes-app-anim.gif
   :scale: 100
   :alt: Demonstration of the Notes tutorial app you can download.

You should be able to complete the setup section of this tutorial within 10-15 minutes after
you have installed all required software. Once you complete the instructions on this page, you can run the project on your local system.

.. _react-native-tutorial-notes-getting-started:

Getting Started
---------------

Before beginning:

#. Install Platform Development Environments

   **For Android**

   -  Download and install `Android Studio <https://developer.android.com/studio/index.html>`__ version 2.33 or later.

   -  Download an install `Android SDK <https://developer.android.com/studio/intro/update.html#sdk-manager>`__ version 7.11 (Nougat), API level 25.

   -  Install an `Android Emulator <https://developer.android.com/studio/run/managing-avds.html>`__ - the app works with both phone and tablet emulators (for example, the Nexus 5X or Pixel C).

   **For iOS**

   -  Install `XCode <https://itunes.apple.com/us/app/xcode/id497799835?mt=12>`__ using the Mac App Store.

   -  Configure the XCode command line tools from a terminal window by running:

      .. code-block:: bash

         ixcode-select --install`

   -  Configure an iOS Simulator.

#. `Sign up for the AWS Free Tier <https://aws.amazon.com/free/>`__.

#. Install `Node.js <https://nodejs.org/en/download/>`__ with NPM.

#. Install AWS Mobile CLI

   .. code-block:: bash

       npm install -g awsmobile-cli

#. Configure the CLI with your AWS credentials

   To setup permissions for the toolchain used by the CLI, run:

   .. code-block:: bash

      awsmobile configure

   If prompted for credentials, follow the steps provided by the CLI. For more information, see :ref:`provide IAM credentials to AWS Mobile CLI <aws-mobile-cli-credentials>`.


Download the Source code
------------------------

1. Get the tutorial source code using one of the following choices:

* Download the source code as a `ZIP file <https://github.com/aws-samples/aws-mobile-react-native-notes-tutorial/archive/master.zip>`__.

* Browse to  `https://github.com/aws-samples/aws-mobile-react-native-notes-tutorial <https://github.com/aws-samples/aws-mobile-react-native-notes-tutorial/>`__ and clone or fork the repository. (If you do not have one, `sign up for GitHub account <https://github.com/join?source=header-home>`__).


Compile and run the Source Code
-------------------------------

To compile and run the source code:

#. If you downloaded the source, unpack it.
#. Open a terminal in the directory that contains the source code.
#. Run :code:`yarn install`.
#. To build and run the app, run :code:`yarn run ios` or :code:`yarn run android`.

For Android, it’s a good idea to have the Android Emulator started before you run the application. You might see failures to start the emulator if you don’t. You can start the emulator from within Android Studio. If you’ve fully set up your environment, you can also use the emulator command (located in :code:`$ANDROID_HOME/tools`).


Running into Problems
---------------------

The most common problems at this stage involve issues with the
installation of Java, Android Studio, the Android SDK or the Android
Emulator. Google provides detailed instructions on `Android Studio <https://developer.android.com/studio/index.html>`__ and
dependent features.

Next Steps
----------

Next, :ref:`integrate application analytics <tutorial-react-native-aws-mobile-notes-analytics>` into your project.

