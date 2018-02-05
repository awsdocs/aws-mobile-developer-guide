.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-ios-aws-mobile-notes-setup:

########################
A Simple Note-taking App
########################

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Analytics <tutorial-ios-aws-mobile-notes-analytics>
   Authentication <tutorial-ios-aws-mobile-notes-auth>
   NoSQL Data <tutorial-ios-aws-mobile-notes-data>

Start with a working app and then add cloud enable features. In this tutorial, you will take a working app, driven from locally stored data, and then:

- :ref:`Add analytics to your app <tutorial-ios-aws-mobile-notes-analytics>` so you can view demographic information about your users.

- :ref:`Add a simple sign-in/sign-up flow <tutorial-ios-aws-mobile-notes-analytics>` for authentication.

- :ref:`Access data stores in the AWS <tutorial-ios-aws-mobile-notes-data>` cloud, so that a user's notes are available to them on any device with the app installed.

.. image:: images/tutorial-ios-notes-app-anim.gif
   :scale: 100
   :alt: Demonstration of the Notes tutorial app you can download.

You should be able to complete the setup section of this tutorial within 10-15 minutes after
you have installed all required software. Once you complete the instructions on this page, you can run the project on your local system.

Getting Started
---------------

Before beginning, on your Mac:

-  Install
   `XCode <https://itunes.apple.com/us/app/xcode/id497799835?mt=12>`__
   using the Mac App Store (version 8.0 or higher is required).

-  Configure the XCode command line tools. Run
   ``xcode-select --install`` from a Terminal window.



- Install Cocoapods. From a terminal window run:


  .. code-block:: bash

      sudo gem install cocoapods


Download the Source code
------------------------

1. Get the tutorial source code using one of the following choices:

* Download the source code as a `ZIP file <https://github.com/aws-samples/aws-mobile-ios-notes-tutorial/archive/master.zip>`_.

* Browse to  `https://github.com/aws-samples/aws-mobile-ios-notes-tutorial/ <https://github.com/aws-samples/aws-mobile-ios-notes-tutorial/>`_ and clone or fork the repository (`sign up for GitHub account <https://github.com/join?source=header-home>`_, if you do not have one).


Compile and Run the Project
---------------------------

To compile the source code and the project in a simulator:

#.  Unzip :file:`aws-mobile-ios-notes-tutorial-latest.zip and launch Xcode by choosing :file:`MyNotes.xcodeproj` in the expanded folder.
#.  Select :guilabel:`Product > Build` :userinput:`Command-B` to build the project.
#.  Select any compatible simulator from the list in toolbar at the top, next to the label with your app name.
#.  Choose the Run icon (Play button) on the top left or type :userinput:`Command-R` to build and run the app.

You should be able to interact with the application. Try clicking on the :guilabel:`+` at the top right to create a note, or click on a note to show the editor screen.


Next Steps
----------

Next, :ref:`integrate application analytics <tutorial-ios-aws-mobile-notes-analytics>` into your project.

