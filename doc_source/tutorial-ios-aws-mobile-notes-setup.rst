.. _tutorial-ios-aws-mobile-notes-setup:

########################
A Simple Note-taking App
########################

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Analytics <tutorial-ios-aws-mobile-notes-analytics>

Start with a working app and then add cloud enable features. In this tutorial you will take a working app, driven from locally stored data, and then:

- :ref:`Add analytics to your app <tutorial-ios-aws-mobile-notes-analytics>` so you can view demographic information about your users.

.. image:: images/tutorial-notes-app-anim.gif
   :scale: 100
   :alt: Demonstration of the Notes tutorial app you can download.

You should be able to complete the setup section of this tutorial within 10-15 minutes after
you have installed all required software. Once you complete the instructions on this page, you can run the project on your local system.

Getting Started
---------------

Before beginning, you must:

-  Use a Mac with a modern OS.

-  Install Xcode 8.0, version or higher, from the Mac App Store.

Download the Source code
------------------------

You can download the source code as a `ZIP
file <https://github.com/aws-samples/aws-mobile-ios-notes-tutorial/archive/master.zip>`_,
or you can download the source code directly from GitHub.

1. Log in to `GitHub <https://github.com/>`_. If you do not have a GitHub account, `sign up for
   GitHub <https://github.com/join?source=header-home>`_ first.

2. Browse to https://github.com/awslabs/aws-mobile-ios-tutorials.

3. Choose :guilabel:`Fork`.

4. Choose your GitHub account.

This will create a copy of the iOS Tutorials in your GitHub account.
To create a copy on your local system, open a terminal window and type:

.. code-block:: bash

    git clone https://github.com/{your-github-id}/aws-mobile-ios-tutorials

This will copy the files within the project to your local system. The
directory :file:`aws-mobile-ios-tutorials` will be created for you.

.. list-table::
   :widths: 2 6

   * - **Note**

     - Git is required

       This step will fail if you have not properly installed Git for your
       platform. If this happens, download and unpack the
       `ZIP file <https://github.com/aws-samples/aws-mobile-ios-notes-tutorial/archive/master.zip>`_ instead.

Compile the Source Code
-----------------------

To compile the source code:

1. Navigate to the folder where you unpacked :file`MyNotes-master`.

2. Launch Xcode by choosing :file:`MyNotes-master/MyNotes.xcodeproj`.

3. Choose :guilabel:`Product > Build` :emphasis:`(Command-B)` to build the project.

**FIX THIS** The compilation step should complete with no errors. Errors are
displayed within the :guilabel:`Messages` window, available on the status bar at
the bottom of the project.

Run the Project on an iOS Simulator
-----------------------------------

1. Select any compatible simulator from :guilabel:`Product > Destination`.

2. Choose the play button on the upper left :emphasis:`(Command-R) to build and run the app.

You should be able to interact with the application as you would any other mobile app. Try Choosing the:guilabel:` + ` on the upper right of the app to create a note, or choose a note to show the content editor.


Running into Problems
---------------------

The most common problems at this stage involve issues with the installation of Xcode or the iOS SDKs and Simulators. Apple provides detailed instructions on `Xcode <https://developer.apple.com/support/xcode/>`_ and dependent features.

Next Steps
----------

Next, :ref:`integrate application analytics <tutorial-ios-aws-mobile-notes-analytics>` into your project.

