Add Authentication to the Notes App
===================================

In the :ref:`previous section of this tutorial <tutorial-ios-aws-mobile-notes-analytics>`, we created a mobile
backend project in AWS Mobile Hub, then added analytics to the sample
note-taking app. This tutorial assumes you have completed the previous
tutorials. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-ios-aws-mobile-notes-setup>`. In this tutorial, we will configure a
sign-up / sign-in flow in our mobile backend. We will then add a new
authentication activity to our note-taking app.

You should be able to complete this section of the tutorial in 20-30 minutes.

Add User Sign-in to the AWS Mobile Hub project
----------------------------------------------

Before we work on the client-side code, we need to add User Sign-in to
the backend project:

1. Open the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.
2. Select  your project.
3. Choose the :guilabel:`User Sign-in` tile.
4. Choose :guilabel:`Email and Password`.
5. Scroll to the bottom of the page, then Choose :guilabel:`Create user pool`.

Download the updated AWS configuration file.
--------------------------------------------

Whenever you update the AWS Mobile Hub project, a new AWS configuration
file for your app is generated. To download:

1. Choose :guilabel:`Integrate` in the left hand menu.
2. Choose :guilabel:`Download` in step 1.

If you previously downloaded this file, it may be named differently to
avoid filename conflicts. Add this file to your Android project by
replacing the ``awsconfiguration.json`` file in the
:file:`app/src/main/res/raw` directory.

Add the Authentication UI library to your project.
--------------------------------------------------

Open the :file:`app/build.gradle` file and add the following lines to the
:code:`dependencies` section:

.. code-block:: none
   :emphasize-lines: 13-15

   dependencies {
      compile fileTree(dir: 'libs', include: ['*.jar'])
      compile 'com.android.support:appcompat-v7:25.3.1'
      compile 'com.android.support:support-v4:25.3.1'
      compile 'com.android.support:cardview-v7:25.3.1'
      compile 'com.android.support:recyclerview-v7:25.3.1'
      compile 'com.android.support.constraint:constraint-layout:1.0.2'
      compile 'com.android.support:design:25.3.1'
      compile 'com.android.support:multidex:1.0.1'
      compile 'joda-time:joda-time:2.9.9'
      compile 'com.amazonaws:aws-ios-sdk-core:2.6.+'
      compile 'com.amazonaws:aws-ios-sdk-auth-core:2.6.+@aar'
      compile 'com.amazonaws:aws-ios-sdk-auth-ui:2.6.+@aar'
      compile 'com.amazonaws:aws-ios-sdk-auth-userpools:2.6.+@aar'
      compile 'com.amazonaws:aws-ios-sdk-cognitoidentityprovider:2.6.+'
      compile 'com.amazonaws:aws-ios-sdk-pinpoint:2.6.+'
    }

Register the Email and Password Sign-in Provider
------------------------------------------------

The sign-in UI is provided by :code:`IdentityManager`. Each method of
establishing identity (email and password, Facebook and Google) requires
a plug-in provider that handles the appropriate sign-in flow.

1. Open your project in Android Studio.
2. Open the :code:`AWSProvider.java` class.
3. Add the following to the import declarations:

.. code-block:: none
   :emphasize-lines: 3

   import com.amazonaws.auth.AWSCredentialsProvider; import com.amazonaws.mobile.auth.core.IdentityManager; import com.amazonaws.mobile.auth.userpools.CognitoUserPoolsSignInProvider; import com.amazonaws.mobile.config.AWSConfiguration; import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration; import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;``

4. Adjust the constructor as follows:

  .. code-block:: none
   :emphasize-lines: 3

    private AWSProvider(Context context) {
        this.context = context;
        this.awsConfiguration = new AWSConfiguration(context);

        IdentityManager identityManager = new IdentityManager(context, awsConfiguration);
        IdentityManager.setDefaultIdentityManager(identityManager);
        identityManager.addSignInProvider(CognitoUserPoolsSignInProvider.class);
    }

Add a LoginActivity to the project
----------------------------------

You can call the IdentityProvider at any point in your application. In
this tutorial, we will add a new screen to the project that is displayed
before the list. The user will be prompted to sign-up or sign-in prior
to seeing the list of notes. This ensures that all connections to the
backend will be authenticated.

To add a LoginActivity to the project, in Android Studio:

1. Right-Choose the :file:`com.amazonaws.mobile.samples.mynotes` folder.
2. Choose :guilabel:`New** > Activity > Empty Activity`.
3. Type the :guilabel:`Activity Name` as :userinput`LoginActivity`.
4. Choose :guilabel:`Finish`.
5. Choose :guilabel:`OK`.

Edit the :code:`onCreate()` method of the created :file:`LoginActivity.java`
file as follows:

  .. code-block:: java
     :emphasize-lines: 6-32

      @Override
      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_login);

          final IdentityManager identityManager = AWSProvider.getInstance().getIdentityManager();
          // Set up the callbacks to handle the authentication response
          identityManager.setUpToAuthenticate(this, new DefaultSignInResultHandler() {
              @Override
              public void onSuccess(Activity activity, IdentityProvider identityProvider) {
                  Toast.makeText(LoginActivity.this,
                          String.format("Logged in as %s", identityManager.getCachedUserID()),
                          Toast.LENGTH_LONG).show();
                  // Go to the main activity
                  final Intent intent = new Intent(activity, NoteListActivity.class)
                          .setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                  activity.startActivity(intent);
                  activity.finish();
              }

              @Override
              public boolean onCancel(Activity activity) {
                  return false;
              }
          });

          // Start the authentication UI
          AuthUIConfiguration config = new AuthUIConfiguration.Builder()
                  .userPools(true)
                  .build();
          SignInActivity.startSignInActivity(this, config);
          LoginActivity.this.finish();
      }


  .. note:: What does this do?

     The AWS SDK for Android contains an in-built activity for handling the authentication UI.  This Activity sets up the authentication UI to work for just email and password, then sets up an activity listener to handle the response.  In this case, we transition to the :code:`NoteListActivity` when a successful sign-in occurs, and stay on this activity when it fails. Finally, we transition to the Sign-In activity from the AWS SDK for Android library.

Update the AndroidManifest.xml
------------------------------

The :code:`LoginActivity` will be added to the :file:`AndroidManifest.xml`
automatically, but it will not be set as the default (starting)
activity. To make the LoginActivity primary, edit the
:file:`AndroidManifest.xml`:

  .. code-block:: xml
     :emphasize-lines: 1-8,13

     <activity
         android:name=".LoginActivity"
         android:label="Sign In"
         android:theme="@style/AppTheme.NoActionBar">
         <intent-filter>
             <action android:name="android.intent.action.MAIN" />
             <category android:name="android.intent.category.LAUNCHER" />
         </intent-filter>
     </activity>
     <activity
         android:name=".NoteListActivity"
         android:label="@string/app_name"
         android:theme="@style/AppTheme.NoActionBar">
         <!-- Remove the intent-filter from here -->
     </activity>

The :code:`.LoginActivity` section is added at the end. Ensure it is not
duplicated. You will see build errors if the section is duplicated.

Run the project and validate results
------------------------------------

Rebuild the project and run in the emulator. You should see a sign-in
screen. Choose the :guilabel:`Create new account` button to create a new account.
Once the information is submitted, you will be sent a confirmation code
via email. Enter the confirmation code to complete registration, then
sign-in with your new account.

  .. note:: Tip: Use Amazon WorkMail as a test email account

     If you do not want to use your own email account as a test account, create an
     `Amazon WorkMail <https://aws.amazon.com/workmail/>`_ service within AWS for test accounts. You can get started for
     free with a 30-day trial for up to 25 accounts.

.. raw:: html

  <iframe width="560" height="315" src="images/notes-authentication.mp4" frameborder="0" allowfullscreen></iframe>

.. literal-include:: git-checkin.rst

Next steps
----------

-  Learn more about `Amazon Cognito <https://aws.amazon.com/cognito/>`_.
-  Continue by integrating :ref:`NoSQL Data <tutorial-ios-aws-mobile-notes-data>`.

