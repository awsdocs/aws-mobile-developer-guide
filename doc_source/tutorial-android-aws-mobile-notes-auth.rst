.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-auth:

###################################
Add Authentication to the Notes App
###################################

In the :ref:`previous section <tutorial-android-aws-mobile-notes-analytics>` of this tutorial, you created a mobile backend project using the AWS Amplify CLI, and then added analytics to the sample note-taking app. This section assumes you have completed these steps. If you jumped ahead to this step, :ref:`go back to the beginning <tutorial-android-aws-mobile-notes-setup>` and start from there. In this tutorial, you configure a sign-up and sign-in flow in our mobile backend. Then, you add a new authentication activity to the note-taking app.

You should be able to complete this section of the tutorial in 20-30 minutes.

Set Up Your Backend
-------------------

Before you work on the client-side code, you need to add user sign-in to the backend project.  These steps assume you have already completed the :ref:`analytics <tutorial-android-aws-mobile-notes-analytics>` portion of this tutorial.

#. Open the project in Android Studio.
#. Choose :guilabel:`View`, choose :guilabel:`Tool Windows`, and then choose :guilabel:`Terminal`.  This opens a terminal prompt in Android Studio at the bottom of the window.
#. In the terminal window, enter the following commands:

.. code-block:: bash

   $ amplify update auth

#. When prompted, use the default configuration.  When asked to overwrite the default authentication and security configuration, answer :userinput:`Yes`.
#. Deploy your new resources with the following command:

.. code-block:: bash

   $ amplify push

The :code:`amplify auth add` command creates an Amazon Cognito user pool configured for username and password authentication with phone verification of the sign-up and forgot password flows.  You can adjust this to include multi-factor authentication, TOTP, phone number sign-up, and more.

Add the Authentication UI Library
---------------------------------

#. Open the :file:`app/build.gradle` file and add the following lines to the :code:`dependencies` section:

    .. code-block:: gradle

       dependencies {
          // Other dependencies will be here already

          // AWS Mobile SDK for Android
          def aws_version = '2.6.27'
          implementation "com.amazonaws:aws-android-sdk-core:$aws_version"
          implementation "com.amazonaws:aws-android-sdk-auth-core:$aws_version@aar"
          implementation "com.amazonaws:aws-android-sdk-auth-ui:$aws_version@aar"
          implementation "com.amazonaws:aws-android-sdk-auth-userpools:$aws_version@aar"
          implementation "com.amazonaws:aws-android-sdk-cognitoidentityprovider:$aws_version"
          implementation "com.amazonaws:aws-android-sdk-pinpoint:$aws_version"
        }

#. On the upper right, choose :guilabel:`Sync Now` to incorporate the dependencies you just declared.

#. Open the :file:`Injection.java` file and add the following method declaration:

    .. code-block:: java

       public static synchronized AWSService getAWSService() {
           return awsService;
       }

Register the Email and Password Sign-in Provider
------------------------------------------------

The sign-in UI is provided by :code:`IdentityManager`. Each method of establishing identity (email and password, Facebook and Google) requires a plug-in provider that handles the appropriate sign-in flow.

1. Open your project in Android Studio.
2. Open the :code:`service/aws/AWSService.java` class.
3. Add the following to the import declarations:

   .. code-block:: java

      import com.amazonaws.mobile.auth.userpools.CognitoUserPoolsSignInProvider;

4. Adjust the constructor to add the :code:`CognitoUserPoolsSignInProvider`.

   .. code-block:: java

      public AWSService(Context context) {
        awsConfiguration = new AWSConfiguration(context);
        identityManager = new IdentityManager(context, awsConfiguration);
        identityManager.addSignInProvider(CognitoUserPoolsSignInProvider.class);
        IdentityManager.setDefaultIdentityManager(identityManager);
      }

Add a AuthenticatorActivity to the Project
------------------------------------------

You can call the IdentityProvider at any point in your application. In this tutorial, you add a new screen to the project that is displayed before the list. The user will be prompted to sign-up or sign-in prior to seeing the list of notes. This ensures that all connections to the backend are authenticated.

**To add a AuthenticatorActivity to the project in Android Studio**

1. Right-click the :file:`ui` package.
2. Choose :guilabel:`New > Activity > Empty Activity`.
3. For :guilabel:`Activity Name`, enter :userinput:`AuthenticatorActivity`.
4. Choose :guilabel:`Finish`.

Add the following imports to the top of the :file:`AuthenticatorActivity.java`:

  .. code-block:: java

     import android.app.Activity;
     import android.content.Intent;
     import android.support.v7.app.AppCompatActivity;
     import android.os.Bundle;
     import android.widget.Toast;

     import com.amazonaws.mobile.auth.core.DefaultSignInResultHandler;
     import com.amazonaws.mobile.auth.core.IdentityManager;
     import com.amazonaws.mobile.auth.core.IdentityProvider;
     import com.amazonaws.mobile.auth.ui.AuthUIConfiguration;
     import com.amazonaws.mobile.auth.ui.SignInActivity;
     import com.amazonaws.mobile.samples.mynotes.Injection;
     import com.amazonaws.mobile.samples.mynotes.R;

Edit the :code:`onCreate()` method of :file:`AuthenticatorActivity.java` as follows:

  .. code-block:: java

      @Override
      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_authenticator);

          final IdentityManager identityManager = Injection.getAWSService().getIdentityManager();
          // Set up the callbacks to handle the authentication response
          identityManager.login(this, new DefaultSignInResultHandler() {
              @Override
              public void onSuccess(Activity activity, IdentityProvider identityProvider) {
                  Toast.makeText(AuthenticatorActivity.this,
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
          AuthenticatorActivity.this.finish();
      }


 .. list-table::
   :widths: 1 6

   * - What does this do?

     - The AWS SDK for Android contains an in-built activity for handling the authentication UI.  This Activity sets up the authentication UI to work for just email and password, then sets up an activity listener to handle the response.  In this case, we transition to the :code:`NoteListActivity` when a successful sign-in occurs, and stay on this activity when it fails. Finally, we transition to the Sign-In activity from the AWS SDK for Android library.

Update the AndroidManifest.xml
------------------------------

The :code:`AuthenticatorActivity` will be added to the :file:`AndroidManifest.xml`
automatically, but it will not be set as the default (starting)
activity. To make the AuthenticatorActivity primary, edit the
:file:`AndroidManifest.xml`:

  .. code-block:: xml

     <activity
         android:name=".ui.AuthenticatorActivity"
         android:label="Sign In"
         android:theme="@style/AppTheme.NoActionBar">
         <intent-filter>
             <action android:name="android.intent.action.MAIN" />
             <category android:name="android.intent.category.LAUNCHER" />
         </intent-filter>
     </activity>
     <activity
         android:name=".ui.NoteListActivity"
         android:label="@string/app_name"
         android:theme="@style/AppTheme.NoActionBar">
         <!-- Remove the intent-filter from here -->
     </activity>

The :code:`.AuthenticatorActivity` section is added at the end. Ensure it is not
duplicated. If the section is duplicated, build errors occur.

Run the Project and Validate Results
------------------------------------

In the emulator, run the project using :guilabel:`Run` > :guilabel:`Run 'app'`. You should see a sign-in
screen. Choose :guilabel:`Create new account` to create a new account.
After the information is submitted, you should receive a confirmation code
via email. Enter the confirmation code to complete registration, and then
sign-in with your new account.

.. list-table::
   :widths: 1 6

   * - **Tip**

     - Use Amazon WorkMail as a test email account.

       If you don't want to use your own email account as a test account, create an
       `Amazon WorkMail <https://aws.amazon.com/workmail/>`__ service within AWS for test accounts. You can get started for free with a 30-day trial for up to 25 accounts.

.. image:: images/tutorial-notes-authentication-anim.gif
   :scale: 75
   :alt: Demo of Notes tutorial app with user sign-in added.

Next Steps
----------

-  Continue by integrating :ref:`Serverless Backend <tutorial-android-aws-mobile-notes-data>`.

-  Learn more about `Amazon Cognito <https://aws.amazon.com/cognito/>`__.
