
.. _add-aws-mobile-user-sign-in:

#######################################################
Add User Sign-in to Your Mobile App with Amazon Cognito
#######################################################

.. meta::
   :description: Integrating user sign-in


.. container:: option

   Android - Java
      .. _android-java:

      Enable your users to sign in using credentials from Facebook, Google, or your own custom user directory. The CLI deploys `Amazon Cognito identity pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ and `user pools <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__ to create your backend.

   Android - Kotlin
      .. _android-kotlin:

      Enable your users to sign in using credentials from Facebook, Google, or your own custom user directory. The CLI deploys `Amazon Cognito identity pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ and `user pools <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__ to create your backend.

   iOS - Swift
      .. _ios-swift:

      Enable your users to sign-in using credentials from Facebook, Google, or your own custom user directory. The CLI deploys `Amazon Cognito identity pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ and `user pools <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__ to create your backend.


.. _auth-setup:

Set Up Your Backend
===================

**Prerequisite** Complete the :ref:`Get Started <getting-started>` steps before you proceed.


.. container:: option

   Email & Password
      .. _email-and-password-backend-setup:

      `This default auth configuration sets up a custom user pool for your app.`

      **To set up email and password sign-in**

      #. In a terminal window, navigate to the root of your app files and add the auth category to your app. The CLI will prompt you for configuration parameters.

          .. container:: option

             Android - Java
                 Navigate to your project folder (the folder that typically contains your project level build.gradle), and add the SDK to your app.

                .. code-block:: bash

                    $ cd ./YOUR_PROJECT_FOLDER
                    $ amplify add auth


             Android - Kotlin
                 Navigate to your project folder (the folder that typically contains your project level build.gradle), and add the SDK to your app.

                .. code-block:: bash

                    $ cd ./YOUR_PROJECT_FOLDER
                    $ amplify add auth


             iOS - Swift
                 Navigate to your project folder (the folder that contains your app :file:`.xcodeproj` file), and add the SDK to your app.

                .. code-block:: bash

                    $ cd ./YOUR_PROJECT_FOLDER
                    $ amplify add auth


      #. Choose the default configuration.

         .. code-block:: none

            ❯ Yes, use the default configuration.


      #. When configuration for email and password sign-in is complete, a message appears confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

         .. code-block:: none

            $ amplify push
              | Category | Resource name   | Operation | Provider plugin   |
              | -------- | --------------- | --------- | ----------------- |
              | Auth     | cognitoabcd0123 | Create    | awscloudformation |

      #. To create your backend AWS resources run the following:

           .. code-block:: none

              amplify push

      #. Follow the :ref:`Set up Email & Password Login <set-up-email-and-password>` steps to connect to your backend from your app.


   Facebook
      .. _facebook-backend-setup:

      **To set up Facebook sign-in**

      #. In a terminal window, navigate to the root of your app files and add the auth category to your app. The CLI prompts you for configuration parameters.

         .. code-block:: none

            $ cd ./YOUR_APP_ROOT
            $ amplify add auth


      #. Choose to set up your own configuration.

         .. code-block:: none

            ❯ No, I will set up my own configuration.

      #. Choose to set up authentication flow using AWS IAM access controls.

         .. code-block:: none

            ❯ User Sign-Up, Sign-In, connected with AWS IAM controls


      #. Choose yes, to: :code:`? Allow unauthenticated logins?`.

      #. Choose yes, to: :code:`? Do you want to enable 3rd party authentication providers in your identity pool?`.

      #. Choose Facebook and then provide your Facebook app ID. To retrieve or create your Facebook app ID, see `Setting Up Facebook Authentication. <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-facebook-setup.html>`__.

      #. When configuration for Facebook sign-in is complete, the CLI displays a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

         .. code-block:: none

            $ amplify status
            | Category  | Resource name   | Operation | Provider plugin   |
            | --------- | --------------- | --------- | ----------------- |
            | Auth      | cognitoa7cbb553 | Create    | awscloudformation |

      #. To create your backend AWS resources run the following:

           .. code-block:: none

              amplify push

      #. Follow the steps at :ref:`Set Up Facebook Login <set-up-facebook>` to connect to your backend from your app.


   Google
      .. _google-backend-setup:

      **To set up Google sign-in**

      #. In a terminal window, navigate to the root of your app files and add the auth category to your app. The CLI prompts you for configuration parameters.

         .. code-block:: none

            $ cd ./YOUR_APP_ROOT
            $ amplify add auth

      #. Choose to set up your own configuration.

         .. code-block:: none

            ❯ No, I will set up my own configuration.

      #. Choose to set up authentication flow using AWS IAM access controls.

         .. code-block:: none

            ❯ User Sign-Up, Sign-In, connected with AWS IAM controls ...


      #. Choose yes, to: :code:`? Allow unauthenticated logins?`.

      #. Choose yes, to: :code:`? Do you want to enable 3rd party authentication providers in your identity pool?`.

      #. Choose Google and then provide your Google client ID. To retrieve or create your Google app ID, see `Setting Up Google Authentication. <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-google-setup.html>`__.

      #. When configuration for Google sign-in is complete, the CLI displays a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

         .. code-block:: none

            $ amplify status
            | Category  | Resource name   | Operation | Provider plugin   |
            | --------- | --------------- | --------- | ----------------- |
            | Auth      | cognitoa7cbb553 | Create    | awscloudformation |

      #. To create your backend AWS resources run the following:

           .. code-block:: none

              amplify push


      #. Follow the steps at :ref:`Set Up Google Login <set-up-google>` to connect to your backend from your app.

Note that the CLI allows you to select more than one identity provider for your app. You can also run :code:`amplify auth update` to add an identity provider to an existing auth configuration.

.. _set-up-email-and-password:

Set Up Email and Password Login in Your Mobile App
================================================

:subscript:`Choose your platform:`

.. container:: option

   Android - Java
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add the following permissions to the :file:`AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add the following dependencies to the :file:`app/build.gradle` file:

         .. code-block:: java

             dependencies {
                  // Mobile Client for initializing the SDK
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                  // Cognito UserPools for SignIn
                  implementation 'com.android.support:support-v4:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-userpools:2.6.+@aar') { transitive = true }

                  // Sign in UI Library
                  implementation 'com.android.support:appcompat-v7:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
             }

          Note: When you add the dependencies, make sure that the major version of appcompat and support libraries match. In the previous example, we're using version 24.

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.


         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user isn't signed in, the user is presented with the AWS Mobile configurable sign-in UI.  After the user is authenticated, the app continues to the :code:`NextActivity`.


         .. code-block:: java

              import android.app.Activity;
              import android.os.Bundle;

              import com.amazonaws.mobile.auth.ui.SignInUI;
              import com.amazonaws.mobile.client.AWSMobileClient;
              import com.amazonaws.mobile.client.AWSStartupHandler;
              import com.amazonaws.mobile.client.AWSStartupResult;

              public class AuthenticatorActivity extends Activity {
                  @Override
                  protected void onCreate(Bundle savedInstanceState) {
                      super.onCreate(savedInstanceState);
                      setContentView(R.layout.activity_authenticator);

                      // Add a call to initialize AWSMobileClient
                      AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                          @Override
                          public void onComplete(AWSStartupResult awsStartupResult) {
                              SignInUI signin = (SignInUI) AWSMobileClient.getInstance().getClient(
                                    AuthenticatorActivity.this,
                                    SignInUI.class);
                              signin.login(
                                    AuthenticatorActivity.this,
                                    NextActivity.class).execute();
                          }
                      }).execute();
                  }
              }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see the ready made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   Android - Kotlin
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add the following permissions to the :file:`AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add the following dependencies to the :file:`app/build.gradle` file:

         .. code-block:: java

             dependencies {
                  // Mobile Client for initializing the SDK
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                  // Cognito UserPools for SignIn
                  implementation 'com.android.support:support-v4:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-userpools:2.6.+@aar') { transitive = true }

                  // Sign in UI Library
                  implementation 'com.android.support:appcompat-v7:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
             }

          Note: When you add the dependencies, make sure that the major version of appcompat and support libraries match. In the previous example, we're using version 24.

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.


         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allows users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user isn't signed in, the user is presented with the AWS Mobile configurable sign-in UI.  After the user is authenticated, the app continues to the :code:`NextActivity`.


         .. code-block:: kotlin

              import android.app.Activity;
              import android.os.Bundle;

              import com.amazonaws.mobile.auth.ui.SignInUI;
              import com.amazonaws.mobile.client.AWSMobileClient;
              import com.amazonaws.mobile.client.AWSStartupHandler;
              import com.amazonaws.mobile.client.AWSStartupResult;

              class AuthenticatorActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                  super.onCreate(savedInstanceState)


                AWSMobileClient.getInstance().initialize(this) {
                    val signInUI = AWSMobileClient.getInstance().getClient(
                            this@AuthenticatorActivity,
                            SignInUI::class.java) as SignInUI?
                    signInUI?.login(
                            this@AuthenticatorActivity,
                            MainActivity::class.java)?.execute()
                }.execute()

              }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see the ready made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add the following dependencies in your project's :file:`Podfile`:

         .. code-block:: none

            platform :ios, '9.0'
            target :'YOUR-APP-NAME' do
                use_frameworks!
                pod 'AWSUserPoolsSignIn', '~> 2.6.13'
                pod 'AWSAuthUI', '~> 2.6.13'
                pod 'AWSMobileClient', '~> 2.6.13'
                # other pods
            end

      #. Pull the SDK libraries into your local repo as follows:

         .. code-block:: bash

             pod install --repo-update

         If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.


      #. Create a AWSMobileClient and initialize the SDK.

         Add code to create an instance of :code:`AWSMobileClient` in the :code:`application:open url` function  of your :code:`AppDelegate.swift`, to resume a previously signed-in authenticated session.

         Then add another instance of :code:`AWSMobileClient` in the :code:`didFinishLaunching` function to register the sign-in providers, and to fetch Amazon Cognito credentials that AWS will use to authorize access when the user signs in.

         .. code-block:: swift

             import UIKit

             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add an AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add an AWSMobileClient call in application:didFinishLaunching
                  func application(
                     _ application: UIApplication,
                         didFinishLaunchingWithOptions launchOptions:
                             [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                      // Other code for application startup here.

                      return AWSMobileClient.sharedInstance().interceptApplication(
                          application, didFinishLaunchingWithOptions:
                          launchOptions)
                 }

                 // Other functions in AppDelegate . . .

               }


      #. Make sure you have a :code:`UINavigationController` in your app to use the sign-in UI. The sign-in UI uses the :code:`UINavigationController` as an anchor to perform all the transitions. Learn more about using `UINavigationController <https://medium.com/whoknows-swift/swift-the-hierarchy-of-uinavigationcontroller-programmatically-91631990f495>`__.


      #. Implement your sign-in UI by calling the library provided in the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

                     // Call the showSignIn method from your `viewDidLoad` method
                     // The showSignIn() method will check if the user is logged in,
                     // and if the user is not logged in, it will present a sign-in UI using the navigation controller the view is part of.
                     showSignIn()
                 }

                 func showSignIn() {
                     if !AWSSignInManager.sharedInstance().isLoggedIn {
                        AWSAuthUIViewController
                          .presentViewController(with: self.navigationController!,
                               configuration: nil,
                               completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                                  if error != nil {
                                      print("Error occurred: \(String(describing: error))")
                                  } else {
                                      // Sign in successful.
                                  }
                               })
                     }
                 }
             }

        Choose the run icon (|play|) in the top left of the Xcode window or type |Acommand|-R to build and run your app. You should see our pre-built sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSUserPoolsUIOperations.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSIdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`

.. _set-up-facebook:

Set Up Facebook Login in Your Mobile App
=======================================

.. container:: option

   Android - Java
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following permissions and Activity to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>


         .. code-block:: xml

            <activity
                android:name="com.facebook.FacebookActivity"
                android:exported="true">
                <intent-filter>
                    <action android:name="android.intent.action.VIEW" />
                    <category android:name="android.intent.category.DEFAULT" />
                    <category android:name="android.intent.category.BROWSABLE" />
                    <data android:scheme="@string/fb_login_protocol_scheme" />
                </intent-filter>
            </activity>


         .. code-block:: xml

            <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id" />


      #. Add the following dependencies to your `app/build.gradle` file:

         .. code-block:: java

            dependencies {
              // Mobile Client for initializing the SDK
              implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

              // Facebook SignIn
              implementation 'com.android.support:support-v4:24.+'
              implementation ('com.amazonaws:aws-android-sdk-auth-facebook:2.6.+@aar') { transitive = true }

              // Sign in UI
              implementation 'com.android.support:appcompat-v7:24.+'
              implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
            }

          Note: When you add the dependencies, make sure that the major version of appcompat and support libraries match. In the previous example, we're using version 24.

      #. In :file:`strings.xml`, add string definitions for your Facebook app ID and login protocol scheme. The value for app_id is your Facebook app ID and the value for logic_protocol_scheme should be your Facebook app ID prefixed with :code:`fb`.

         .. code-block:: xml

            <string name="facebook_app_id">1231231231232123123</string>
            <string name="fb_login_protocol_scheme">fb1231231231232123123</string>

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user is not signed in, the user is presented with the AWS Mobile configurable sign-in UI.  After the user is authenticated, the app continues to the :code:`NextActivity`.

         .. code-block:: java

              import android.app.Activity;
              import android.os.Bundle;

              import com.amazonaws.mobile.auth.ui.SignInUI;
              import com.amazonaws.mobile.client.AWSMobileClient;
              import com.amazonaws.mobile.client.AWSStartupHandler;
              import com.amazonaws.mobile.client.AWSStartupResult;

              public class AuthenticatorActivity extends Activity {
                  @Override
                  protected void onCreate(Bundle savedInstanceState) {
                      super.onCreate(savedInstanceState);
                      setContentView(R.layout.activity_authenticator);

                      // Add a call to initialize AWSMobileClient
                      AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                          @Override
                          public void onComplete(AWSStartupResult awsStartupResult) {
                              SignInUI signin = (SignInUI) AWSMobileClient.getInstance().getClient(AuthenticatorActivity.this, SignInUI.class);
                              signin.login(AuthenticatorActivity.this, NextActivity.class).execute();
                          }
                      }).execute();
                  }
              }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see the ready made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   Android - Kotlin
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following permissions and Activity to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>


         .. code-block:: xml

            <activity
                android:name="com.facebook.FacebookActivity"
                android:exported="true">
                <intent-filter>
                    <action android:name="android.intent.action.VIEW" />
                    <category android:name="android.intent.category.DEFAULT" />
                    <category android:name="android.intent.category.BROWSABLE" />
                    <data android:scheme="@string/fb_login_protocol_scheme" />
                </intent-filter>
            </activity>


         .. code-block:: xml

            <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id" />

      #. Add the following dependencies to your `app/build.gradle` file:

         .. code-block:: java

            dependencies {
              // Mobile Client for initializing the SDK
              implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

              // Facebook SignIn
              implementation 'com.android.support:support-v4:24.+'
              implementation ('com.amazonaws:aws-android-sdk-auth-facebook:2.6.+@aar') { transitive = true }

              // Sign in UI
              implementation 'com.android.support:appcompat-v7:24.+'
              implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
            }

      #. In :file:`strings.xml`, add string definitions for your Facebook app ID and login protocol scheme. The value for app_id is your Facebook app ID and the value for logic_protocol_scheme should be your Facebook app ID prefixed with :code:`fb`.

         .. code-block:: xml

            <string name="facebook_app_id">1231231231232123123</string>
            <string name="fb_login_protocol_scheme">fb1231231231232123123</string>

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user is not signed in, the user is presented with the AWS Mobile configurable sign-in UI. After the user is authenticated, the app continues to the :code:`NextActivity`.

         .. code-block:: kotlin

              import android.app.Activity;
              import android.os.Bundle;

              import com.amazonaws.mobile.auth.ui.SignInUI;
              import com.amazonaws.mobile.client.AWSMobileClient;
              import com.amazonaws.mobile.client.AWSStartupHandler;
              import com.amazonaws.mobile.client.AWSStartupResult;

                class AuthenticatorActivity : Activity() {
                  override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)

                  AWSMobileClient.getInstance().initialize(this) {
                      val signInUI = AWSMobileClient.getInstance().getClient(
                            this@AuthenticatorActivity,
                            SignInUI::class.java) as SignInUI?
                      signInUI?.login(
                            this@AuthenticatorActivity,
                            MainActivity::class.java)?.execute()
                  }.execute()
                }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see the ready-made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following dependencies in your project's :file:`Podfile`.

         .. code-block:: none

            platform :ios, '9.0'
              target :'YOUR-APP-NAME' do
                use_frameworks!
                pod 'AWSMobileClient', '~> 2.6.13'
                pod 'AWSFacebookSignIn', '~> 2.6.13'
                pod 'AWSUserPoolsSignIn', '~> 2.6.13'
                pod 'AWSAuthUI', '~> 2.6.13'
                # other pods
              end

         Run :code:`pod install --repo-update`.

         If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

      #. Add Facebook meta data to :file:`Info.plist`.

         To configure your Xcode project to use Facebook Login, right-choose :file:`Info.plist` and then choose :guilabel:`Open As > Source Code`.

         Add the following entry, using your project name, Facebook ID and login scheme ID.

         .. code-block:: xml

            <plist version="1.0">

            <dict>
            <!-- YOUR OTHER PLIST ENTRIES HERE -->

            <!-- START OF FACEBOOK PLIST ENTRIES HERE -->
            <!-- 0123456789012345 BELOW IS EQUIVALENT TO YOUR APP ID -->
            <key>FacebookAppID</key>
            <string>0123456789012345</string>
            <key>FacebookDisplayName</key>
            <string>YOUR-PROJECT-NAME</string>
            <key>LSApplicationQueriesSchemes</key>
            <array>
                <string>fbapi</string>
                <string>fb-messenger-api</string>
                <string>fbauth2</string>
                <string>fbshareextension</string>
            </array>
            <!-- END OF FACEBOOK PLIST ENTRIES HERE -->


            <!-- ADD AN ENTRY TO CFBundleURLTypes for Facebook -->
            <!-- IF YOU DO NOT HAVE CFBundleURLTypes, YOU CAN COPY THE WHOLE BLOCK BELOW -->
            <key>CFBundleURLTypes</key>
            <array>
                <dict>
                    <key>CFBundleURLSchemes</key>
                    <array>
                        <string>fb0123456789012345</string>
                    </array>
                </dict>
            </array>

            <!-- ... -->
            </dict>

      #. Create a AWSMobileClient and initialize the SDK.

         Add code to create an instance of :code:`AWSMobileClient` in the :code:`application:open url` function  of your :code:`AppDelegate.swift`, to resume a previously signed-in authenticated session.

         Then add another instance of :code:`AWSMobileClient` in the :code:`didFinishLaunching` function to register the sign in providers, and to fetch an Amazon Cognito credentials that AWS will use to authorize access once the user signs in.

         .. code-block:: swift

             import UIKit

             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add an AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add an AWSMobileClient call in application:didFinishLaunching
                  func application(
                     _ application: UIApplication,
                         didFinishLaunchingWithOptions launchOptions:
                             [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                      return AWSMobileClient.sharedInstance().interceptApplication(
                          application, didFinishLaunchingWithOptions:
                          launchOptions)
                 }

                 // Other functions in AppDelegate . . .

               }


      #. Make sure you have a :code:`UINavigationController` in your app to use the sign-in UI. The sign-in UI uses the :code:`UINavigationController` as an anchor to perform all the transitions.
        Learn more about using `UINavigationController <https://medium.com/whoknows-swift/swift-the-hierarchy-of-uinavigationcontroller-programmatically-91631990f495>`__.


      #. Implement your sign-in UI by calling the library provided by the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

                     // Call the showSignIn method from your `viewDidLoad` method
                     // The showSignIn() method will check if the user is logged in,
                     // and if the user is not logged in, it will present a sign-in UI using the navigation controller the view is part of.
                     showSignIn()
                 }

                 func showSignIn() {
                     if !AWSSignInManager.sharedInstance().isLoggedIn {
                        AWSAuthUIViewController
                          .presentViewController(with: self.navigationController!,
                               configuration: nil,
                               completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                                  if error != nil {
                                      print("Error occurred: \(String(describing: error))")
                                  } else {
                                      // Sign in successful.
                                  }
                               })
                     }
                 }
             }

      Choose the run icon (|play|) in the top left of the Xcode window or type |Acommand|-R to build and run your app. You should see our pre-built sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSUserPoolsUIOperations.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSIdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`


.. _set-up-google:

Set Up Google Login in Your Mobile App
=====================================

.. container:: option

   Android - Java
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following permissions to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add the following dependencies to your `app/build.gradle` file:

         .. code-block:: java

              dependencies {
                  // Mobile Client for initializing the SDK
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                  // Google SignIn
                  implementation 'com.android.support:support-v4:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-google:2.6.+@aar') { transitive = true }

                  // Sign in UI Library
                  implementation 'com.android.support:appcompat-v7:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
              }


      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

                <activity android:name=".AuthenticatorActivity">
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user is not signed in, the user is presented with the AWS Mobile configurable sign-in UI.  After the user is authenticated, the app continues to the :code:`NextActivity`.

         .. code-block:: java

            import android.app.Activity;
            import android.os.Bundle;

            import com.amazonaws.mobile.auth.ui.SignInUI;
            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

            public class AuthenticatorActivity extends Activity {
                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_authenticator);

                    // Add a call to initialize AWSMobileClient
                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                        @Override
                        public void onComplete(AWSStartupResult awsStartupResult) {
                            SignInUI signin = (SignInUI) AWSMobileClient.getInstance().getClient(AuthenticatorActivity.this, SignInUI.class);
                            signin.login(AuthenticatorActivity.this, MainActivity.class).execute();
                        }
                    }).execute();
                }
            }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see our ready made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      Note: If you get an exception which mentions :code:`Developer Error`, it is likely due to missing SHA1 value from the Google configuration console. Create an Android client app from the Google console and add your machine's SHA1 keys there. `Reference Link <https://stackoverflow.com/questions/37273145/error-statusstatuscode-developer-error-resolution-null>`_

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   Android - Kotlin
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following permissions to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add the following dependencies to your `app/build.gradle` file:

         .. code-block:: java

              dependencies {
                  // Mobile Client for initializing the SDK
                  implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                  // Google SignIn
                  implementation 'com.android.support:support-v4:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-google:2.6.+@aar') { transitive = true }

                  // Sign in UI Library
                  implementation 'com.android.support:appcompat-v7:24.+'
                  implementation ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true }
              }


      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

                <activity android:name=".AuthenticatorActivity">
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction is complete.

         If the user is already signed in, the app switches to the :code:`NextActivity`.  If the user is not signed in, the user is presented with the AWS Mobile configurable sign-in UI.  After the user is authenticated, the app continues to the :code:`NextActivity`.

         .. code-block:: kotlin

            import android.app.Activity;
            import android.os.Bundle;

            import com.amazonaws.mobile.auth.ui.SignInUI;
            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

              class AuthenticatorActivity : Activity() {
                override fun onCreate(savedInstanceState: Bundle?) {
                  super.onCreate(savedInstanceState)

                AWSMobileClient.getInstance().initialize(this) {
                    val signInUI = AWSMobileClient.getInstance().getClient(
                          this@AuthenticatorActivity,
                          SignInUI::class.java) as SignInUI?
                    signInUI?.login(
                          this@AuthenticatorActivity,
                          MainActivity::class.java)?.execute()
                }.execute()
            }

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. You should see our ready made sign-in UI for your app. Check out the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      Note: If you get an exception which mentions :code:`Developer Error`, it is likely due to missing SHA1 value from the Google configuration console. Create an Android client app from the Google console and add your machine's SHA1 keys there. `Reference Link <https://stackoverflow.com/questions/37273145/error-statusstatuscode-developer-error-resolution-null>`_

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper library for Amazon Cognito user pools that provides a managed email/password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito federated identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following dependencies in the Podfile.

         .. code-block:: none

              platform :ios, '9.0'
                target :'YOUR-APP-NAME' do
                  use_frameworks!
                  pod 'AWSMobileClient', '~> 2.6.13'
                  pod 'AWSGoogleSignIn', '~> 2.6.13'
                  pod 'AWSUserPoolsSignIn', '~> 2.6.13'
                  pod 'AWSAuthUI', '~> 2.6.13'
                  pod 'GoogleSignIn', '~> 4.0'
                  # other pods
                end

         Run :code:`pod install --repo-update` before you continue.

         If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

      #. Add Google metadata to :file:`Info.plist`.

         To configure your Xcode project to use Google Login, open its :file:`Info.plist` file using **Right-click > Open As > Source Code.** Add the following entry. Substitute your project name for the placeholder string.

         .. code-block:: xml

            <plist version="1.0">
            <!-- YOUR OTHER PLIST ENTRIES HERE -->

            <!-- ADD AN ENTRY TO CFBundleURLTypes for Google -->
            <!-- IF YOU DO NOT HAVE CFBundleURLTypes, YOU CAN COPY THE WHOLE BLOCK BELOW -->
            <key>CFBundleURLTypes</key>
            <array>
                <dict>
                <key>CFBundleURLSchemes</key>
                <array>
                    <string>com.googleusercontent.apps.xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</string>
                </array>
                </dict>
            </array>

            <!-- ... -->

      #. Create a AWSMobileClient and initialize the SDK.

         Add code to create an instance of :code:`AWSMobileClient` in the :code:`application:open url` function  of your :code:`AppDelegate.swift`, to resume a previously signed-in authenticated session.

         Then add another instance of :code:`AWSMobileClient` in the :code:`didFinishLaunching` function to register the sign in providers, and to fetch an Amazon Cognito credentials that AWS will use to authorize access once the user signs in.

         .. code-block:: swift

             import UIKit

             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add an AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add an AWSMobileClient call in application:didFinishLaunching
                 func application(
                     _ application: UIApplication,
                         didFinishLaunchingWithOptions launchOptions:
                             [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                      return AWSMobileClient.sharedInstance().interceptApplication(
                          application, didFinishLaunchingWithOptions:
                          launchOptions)
                 }

                 // Other functions in AppDelegate . . .

               }


      #. Make sure you have a :code:`UINavigationController` in your app to use the sign-in UI. The sign-in UI uses the :code:`UINavigationController` as an anchor to perform all the transitions.
        Learn more about using `UINavigationController <https://medium.com/whoknows-swift/swift-the-hierarchy-of-uinavigationcontroller-programmatically-91631990f495>`__.


      #. Implement your sign-in UI by calling the library provided by the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

                     // Call the showSignIn method from your `viewDidLoad` method
                     // The showSignIn() method will check if the user is logged in,
                     // and if the user is not logged in, it will present a sign-in UI using the navigation controller the view is part of.
                     showSignIn()
                 }

                 func showSignIn() {
                     if !AWSSignInManager.sharedInstance().isLoggedIn {
                        AWSAuthUIViewController
                          .presentViewController(with: self.navigationController!,
                               configuration: nil,
                               completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                                  if error != nil {
                                      print("Error occurred: \(String(describing: error))")
                                  } else {
                                      // Sign in successful.
                                  }
                               })
                     }
                 }
             }


      Choose the run icon (|play|) in the top left of the Xcode window or type |Acommand|-R to build and run your app. You should see our pre-built sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSUserPoolsUIOperations.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSIdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`

.. _auth-sign-out:

Enable Sign-out
===============

.. container:: option

   Android - Java
       To enable a user to sign-out of your app, register a callback for sign-in events by adding a :code:`SignInStateChangeListener` to :code:`IdentityManager`. The listener captures both :code:`onUserSignedIn` and :code:`onUserSignedOut` events.

        .. code-block:: java

           IdentityManager.getDefaultIdentityManager().addSignInStateChangeListener(new SignInStateChangeListener() {
               @Override
               // Sign-in listener
               public void onUserSignedIn() {
                   Log.d(TAG, "User Signed In");
               }

               // Sign-out listener
               @Override
               public void onUserSignedOut() {
                  Log.d(TAG, "User signed out");
               }
           });

       To initiate a sign-out, call the :code:`signOut` method of :code:`IdentityManager`.

        .. code-block:: java

           IdentityManager.getDefaultIdentityManager().signOut();

   Android - Kotlin
       To enable a user to sign-out of your app, register a callback for sign-in events by adding a :code:`SignInStateChangeListener` to :code:`IdentityManager`. The listener captures both :code:`onUserSignedIn` and :code:`onUserSignedOut` events.

        .. code-block:: kotlin

            IdentityManager.getDefaultIdentityManager().addSignInStateChangeListener(
                    object : SignInStateChangeListener {
                        override fun onUserSignedIn() {
                            Log.d(TAG, "User signed in")
                        }

                        override fun onUserSignedOut() {
                            Log.d(TAG, "User signed out")
                        }
                    }
            )

       To initiate a sign-out, call the :code:`signOut` method of :code:`IdentityManager`.

        .. code-block:: kotlin

           IdentityManager.getDefaultIdentityManager().signOut()

   iOS - Swift
       To initiate a sign-out, add a call to  :code:`AWSSignInManager.sharedInstance().logout`.

       .. code-block:: swift

             // This call should be invoked on a UI activity like a button press triggered by the end user. E.g. `onSignOutButtonClicked` action of sign out button in your app.
             AWSSignInManager.sharedInstance().logout(completionHandler: {(result: Any?, error: Error?) in

                 // Note: The showSignIn() method used below was added by us previously while integrating the sign-in UI.
                 self.showSignIn()
             })


For a fuller example, see :ref:`Sign-out a Signed-in User <how-to-user-sign-in-sign-out>` in the How To section.

.. _auth-next-steps:

Next Steps
==========

  * :ref:`Customize the UI <add-aws-mobile-user-sign-in-customize>`

  * :ref:`Import Your Existing Amazon Cognito Identity Pool <how-to-cognito-integrate-an-existing-identity-pool>`

  * `Amazon Cognito Developer Guide <http://docs.aws.amazon.com/cognito/latest/developerguide/>`__
