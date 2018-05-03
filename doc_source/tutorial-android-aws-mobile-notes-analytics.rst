.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-analytics:

##############################
Add Analytics to the Notes App
##############################

In the :ref:`previous section <tutorial-android-aws-mobile-notes-setup>` of this tutorial, we installed Android Studio,
downloaded a sample note-taking app from GitHub, then compiled and ran
it in the Android Emulator. This tutorial assumes you have completed the
those steps. In this section, we will extend the notes app to
include application analytics. Application analytics allow us to gather
demographic information about the application usage.

You should be able to complete this section in 10-15 minutes.

Set Up Your Back End
--------------------

To start, set up the mobile backend resources in AWS:

#. Open the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.

   -  If you do not have an AWS account, `sign up for the AWS
      Free Tier <https://aws.amazon.com/free/>`__.

#. Choose :guilabel:`Create` on the upper left, and the type :userinput:`android-notes-app` for the name of the Mobile Hub project.
#. Choose :guilabel:`Next`, choose :guilabel:`Android`, and then choose :guilabel:`Add`.
#. Choose :guilabel:`Download Cloud Config`, and save :file:`awsconfiguration.json`. This file the configuration to connect your app to your backend.
#. Choose :guilabel:`Next` and then choose :guilabel:`Done` to create the project.

.. list-table::
   :widths: 1 6

   * - Used in this section

     - `AWS Mobile Hub <https://console.aws.amazon.com/mobilehub/home/>`__: Configure your mobile app's AWS backend in minutes, and then to manage those resources as your app evolves.

Add Permissions to the AndroidManifest.xml
------------------------------------------

#. Open the project in Android Studio.
#. Choose :guilabel:`Project` on the left side of the project to open the project browser. Find the app manifest by changing the project browser view menu at the top to :guilabel:`Android`, and opening the :file:`app/manifests` folder.
#. Add the :code:`INTERNET`, :code:`ACCESS_NETWORK_STATE`, and
   :code:`ACCESS_WIFI_STATE`: permissions to your project's :file:`AndroidManifest.xml` file.

.. code-block:: xml
   :emphasize-lines: 5-7

    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.amazonaws.mobile.samples.mynotes">

        <uses-permission android:name="android.permission.INTERNET"/>
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
        <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>

        <application
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            android:roundIcon="@mipmap/ic_launcher_round"
            android:supportsRtl="true"
            android:theme="@style/AppTheme"
            android:name=".Application">
            <!-- Other settings -->
        </application>
    </manifest>

Add AWS SDK for Android library
-------------------------------

#. Edit the :file:`app/build.gradle` file. Add the following lines to the
    :code:`dependencies` section:

    .. code-block:: xml
       :emphasize-lines: 11-14

       dependencies {
          compile fileTree(dir: 'libs', include: ['*.jar'])
          implementation 'com.android.support:appcompat-v7:26.1.0'
          implementation 'com.android.support:support-v4:26.1.0'
          implementation 'com.android.support:cardview-v7:26.1.0'
          implementation 'com.android.support:recyclerview-v7:26.1.0'
          implementation 'com.android.support.constraint:constraint-layout:1.0.2'
          implementation 'com.android.support:design:26.1.0'
          implementation 'com.android.support:multidex:1.0.1'
          implementation 'joda-time:joda-time:2.9.9'

          // AWS Mobile SDK for Android
          implementation 'com.amazonaws:aws-android-sdk-core:2.6.+'
          implementation 'com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar'
          implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
       }

#. Choose :guilabel:`Sync Now` on the upper right to incorporate the dependencies you just declared.

Integrate the AWS Configuration File
------------------------------------

First, create a :file:`raw` resource folder to store the AWS configuration file:

#. Expand the :file:`app` folder.
#. Right-click the :file:`res` folder.
#. Choose :guilabel:`New > Directory`.
#. Type :userinput:`raw`.

   .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
       :scale: 100
       :alt: Image of creating a raw directory in Android Studio.

#. Choose :guilabel:`OK`.
#. Copy the :file:`awsconfiguration.json` file from its download location to the
   :file:`app/src/main/res/raw` directory.

Android gives a resource ID to any arbitrary file placed in the :file:`raw` folder, making it easy to reference in the app.

  .. list-table::
   :widths: 1 6

   * - **Tip**

     - Use Reveal in Finder

       If you are having trouble locating the right directory on disk, use Android Studio.
       Right-click the :file:`raw` folder, then select :guilabel:`Reveal in Finder`. A new
       window with the location of the :file:`raw directory` pre-loaded will appear.



Create an AWSProvider.java Singleton Class
------------------------------------------

In our sample, all access to AWS is consolidated into a singleton class
called :file:`AWSProvider.java`.

1. Expand :file:`app/java` in the Android Studio project explorer.
2. Right-click the :file:`com.amazonaws.mobile.samples.mynotes` directory.
3. Select :guilabel:`New > Java Class`.
4. Enter the details:

   -  Name: :userinput:`AWSProvider`
   -  Kind: :userinput:`Singleton`

5. Choose :guilabel:`OK`.

You may be asked if you want to add the file to Git. Choose :guilabel:`Yes`.

The following is the initial code in this class:

  .. code-block:: java

      package com.amazonaws.mobile.samples.mynotes;

      import android.content.Context;

      import com.amazonaws.auth.AWSCredentialsProvider;
      import com.amazonaws.mobile.auth.core.IdentityManager;
      import com.amazonaws.mobile.config.AWSConfiguration;
      import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
      import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;

      public class AWSProvider {
          private static AWSProvider instance = null;
          private Context context;
          private AWSConfiguration awsConfiguration;
          private PinpointManager pinpointManager;

          public static AWSProvider getInstance() {
              return instance;
          }

          public static void initialize(Context context) {
              if (instance == null) {
                  instance = new AWSProvider(context);
              }
          }

          private AWSProvider(Context context) {
              this.context = context;
              this.awsConfiguration = new AWSConfiguration(context);

              IdentityManager identityManager = new IdentityManager(context, awsConfiguration);
              IdentityManager.setDefaultIdentityManager(identityManager);
          }

          public Context getContext() {
              return this.context;
          }

          public AWSConfiguration getConfiguration() {
              return this.awsConfiguration;
          }

          public IdentityManager getIdentityManager() {
              return IdentityManager.getDefaultIdentityManager();
          }

          public PinpointManager getPinpointManager() {
              if (pinpointManager == null) {
                  final AWSCredentialsProvider cp = getIdentityManager().getCredentialsProvider();
                  PinpointConfiguration config = new PinpointConfiguration(
                          getContext(), cp, getConfiguration());
                  pinpointManager = new PinpointManager(config);
              }
              return pinpointManager;
          }
      }


.. list-table::
   :widths: 1 6

   * - What does this do?

     - The AWSProvider provides a central place
       to add code that accesses AWS resources. The constructor will load the
       AWS Configuration (a JSON file that you downloaded earlier) and create an
       IdentityManager object that is used to authenticate the device and/or
       user to AWS for accessing resources. The :code:`getPinpointManager()` method
       will create a connection to Amazon Pinpoint if it doesn't exist.

Update the Application Class
----------------------------

All Android applications that include the AWS SDK for Android must
inherit from
`MultiDexApplication <https://developer.android.com/studio/build/multidex.html>`__.
This has been done for you in this project. Open the
:file:`Application.java` file. In the :code:`onCreate()` method of the
:code:`Application` class, add code to initialize the :code:`AWSProvider` object
we previously added:

.. code-block:: java
   :emphasize-lines: 6,7

   public class Application extends MultiDexApplication {
      @Override
      public void onCreate() {
          super.onCreate();

          // Initialize the AWS Provider
          AWSProvider.initialize(getApplicationContext());

          registerActivityLifecycleCallbacks(new ActivityLifeCycle());
      }
   }


Update the ActivityLifeCycle Class
----------------------------------

We use an
`ActivityLifeCycle <https://developer.android.com/guide/components/activities/activity-lifecycle.html>`__
to monitor for activity events like start, stop, pause and resume. We
need to determine when the user starts the application so that we can
send a :code:`startSession` event and :code:`stopSession` event to Amazon
Pinpoint. Adjust the :code:`onActivityStarted()` and :code:`onActivityStopped()`
methods as follows:

.. code-block:: java
   :emphasize-lines: 5,6,16,17

    @Override
    public void onActivityStarted(Activity activity) {
        if (depth == 0) {
            Log.d("ActivityLifeCycle", "Application entered foreground");
            AWSProvider.getInstance().getPinpointManager().getSessionClient().startSession();
            AWSProvider.getInstance().getPinpointManager().getAnalyticsClient().submitEvents();
        }
        depth++;
    }

    @Override
    public void onActivityStopped(Activity activity) {
        depth--;
        if (depth == 0) {
            Log.d("ActivityLifeCycle", "Application entered background");
            AWSProvider.getInstance().getPinpointManager().getSessionClient().stopSession();
            AWSProvider.getInstance().getPinpointManager().getAnalyticsClient().submitEvents();
        }
    }


Monitor Add and Delete Events in Amazon Pinpoint
------------------------------------------------

We can also monitor feature usage within our app. In this example, we
will monitor how often users add and delete notes. We will record a
custom event for each operation. The Delete Note operation occurs in the
:file:`NoteListActivity.java` class. Review the :code:`onSwiped` method, and add the following code:

.. code-block:: java
   :emphasize-lines: 6-13

    @Override
    public void onSwiped(RecyclerView.ViewHolder viewHolder, int direction) {
        final NoteViewHolder noteHolder = (NoteViewHolder) viewHolder;
        ((NotesAdapter) notesList.getAdapter()).remove(noteHolder);

        // Send Custom Event to Amazon Pinpoint
        final AnalyticsClient mgr = AWSProvider.getInstance()
                .getPinpointManager()
                .getAnalyticsClient();
        final AnalyticsEvent evt = mgr.createEvent("DeleteNote")
                .withAttribute("noteId", noteHolder.getNote().getNoteId());
        mgr.recordEvent(evt);
        mgr.submitEvents();
    }


The Add Note operation occurs in the ``NoteDetailFragment.java`` class.
Review the :code:`saveData()` method, and add code to send the custom event
to Amazon Pinpoint as shown in the following fragment.

.. code-block:: java
   :emphasize-lines: 24-31

    private void saveData() {
        // Save the edited text back to the item.
        boolean isUpdated = false;
        if (!mItem.getTitle().equals(editTitle.getText().toString().trim())) {
            mItem.setTitle(editTitle.getText().toString().trim());
            mItem.setUpdated(DateTime.now(DateTimeZone.UTC));
            isUpdated = true;
        }
        if (!mItem.getContent().equals(editContent.getText().toString().trim())) {
            mItem.setContent(editContent.getText().toString().trim());
            mItem.setUpdated(DateTime.now(DateTimeZone.UTC));
            isUpdated = true;
        }

        // Convert to ContentValues and store in the database.
        if (isUpdated) {
            ContentValues values = mItem.toContentValues();
            if (isUpdate) {
                contentResolver.update(itemUri, values, null, null);
            } else {
                itemUri = contentResolver.insert(NotesContentContract.Notes.CONTENT_URI, values);
                isUpdate = true;    // Anything from now on is an update

                // Send Custom Event to Amazon Pinpoint
                final AnalyticsClient mgr = AWSProvider.getInstance()
                        .getPinpointManager()
                        .getAnalyticsClient();
                final AnalyticsEvent evt = mgr.createEvent("AddNote")
                        .withAttribute("noteId", mItem.getNoteId());
                mgr.recordEvent(evt);
                mgr.submitEvents();
            }
        }
    }


The AnalyticsClient and AnalyticsEvent classes are not imported by
default. Use Alt-Return to import the missing classes.


  .. list-table::
   :widths: 1 6

   * - **Tip**

     - Auto Import

       You can set up Auto-Import to automatically import
       classes that you need. On Windows or Linux, you can find Auto-Import
       under :guilabel:`File > Settings`. On a Mac, you can find the same area
       under :guilabel:`Android Studio > Preferences`. The auto-import setting is
       under :guilabel:`Editor > General > Auto Import >Java`. Change
       :guilabel:`Insert imports on paste` to :guilabel:`All` and select the :guilabel:`Add unambiguous
       imports on the fly` option.


Run the Project and Validate Results
------------------------------------

Run the application in the emulator using :guilabel:`Run` > :guilabel:`Run 'app'`. It
should work as before. Ensure you try to add and delete some notes to
generate some traffic that can be shown in the Pinpoint console.

To view the demographics and custom events:

#. Open the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`__.
#. Choose your project.
#. Choose the :guilabel:`Analytics` icon on the left, to navigate to your project in the `AWS Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__.
#. Choose :guilabel:`Analytics` on the left.
#. You should see an up-tick in several graphs:

   .. image:: images/pinpoint-overview.png
      :scale: 100 %
      :alt: Image of the Amazon Pinpoint console.

   .. only:: pdf

      .. image:: images/pinpoint-overview.png
         :scale: 50

   .. only:: kindle

      .. image:: images/pinpoint-overview.png
         :scale: 75


#. Choose :guilabel:`Demographics` to view the demographics information.

   .. image:: images/pinpoint-demographics.png
      :scale: 100 %
      :alt: Image of the Amazon Pinpoint console Demographics tab.

   .. only:: pdf

      .. image:: images/pinpoint-demographics.png
         :scale: 50

   .. only:: kindle

      .. image:: images/pinpoint-demographics.png
         :scale: 75


#. Choose :guilabel:`Events`.

#. Use the Event drop down to show only the :guilabel:`AddNote` event.

   .. image:: images/pinpoint-addnote.png
      :scale: 100 %
      :alt: Image of the Add note event in the Amazon Pinpoint.

   .. only:: pdf

      .. image:: images/pinpoint-addnote.png
         :scale: 50

   .. only:: kindle

      .. image:: images/pinpoint-addnote.png
         :scale: 75


If you see data within each page, you have successfully added analytics
to your app. Should you release your app on the App Store, you can come
back here to see more details about your users.

Next steps
----------

*  Continue by adding :ref:`Authentication <tutorial-android-aws-mobile-notes-auth>`.

*  Learn more about `Amazon Pinpoint <https://aws.amazon.com/pinpoint/>`__.


