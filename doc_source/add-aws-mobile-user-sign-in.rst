.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-user-sign-in:

#######################################################
Add User Sign-in to Your Mobile App with Amazon Cognito
#######################################################

.. meta::
   :description: Integrating user sign-in


Enable your users to sign-in using credentials from Facebook, Google, or your own custom user directory. The AWS Mobile Hub :ref:`user-sign-in` feature is powered by `Amazon Cognito <http://docs.aws.amazon.com/cognito/latest/developerguide/>`__, and the SDK provides a pre-built, :ref:`configurable <add-aws-mobile-user-sign-in-customize>` Sign-in UI based on the identity provider(s) you configure.


.. _auth-setup:

Set Up Your Backend
===================

**Prerequisite** Complete the :ref:`Get Started <getting-started>` steps before your proceed.


.. container:: option

   Email & Password
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. Choose :guilabel:`Email and Password sign-in`

         .. image:: images/add-aws-mobile-sdk-email-and-password.png

         * Choose :guilabel:`Create a new user pool`, the feature and then select sign-in settings including: allowed login methods; multi-factor authentication; and password requirements. Then choose :guilabel:`Create user pool`.

           .. image:: images/add-aws-mobile-sdk-email-and-password-create.png

         Or:

         * Choose :guilabel:`Import an existing user pool`, select a user pool from the list of pools that are  available in the account. Choose if sign-in is required, and then choose :guilabel:`Create user pool`. If you import a user pool that is in use by another app, then the two apps will share the user directory and authenticate sign-in by the same set of users.

           .. image:: images/add-aws-mobile-sdk-email-and-password-import.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the :ref:`Set up Email & Password Login <set-up-email-and-password>` steps to connect to your backend from your app.

   Facebook
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. **Configure Facebook sign-in**: Choose the feature and then type your Facebook App ID and then choose :guilabel:`Enable Facebook login`. To retrieve or create your Facebook App ID, see `Setting Up Facebook Authentication. <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-facebook-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-facebook.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the steps at :ref:`Set Up Facebook Login <set-up-facebook>` to connect to your backend from your app.


   Google
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub console <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`User Sign-in` tile.

      #. Configure **Google sign-in**: Choose the feature and then type in your Google Web App Client ID, and the Google Android or iOS Client ID (or both), and then choose Enable Google Sign-In. To retrieve or create your Google Client IDs, see `Setting Up Google Authentication <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-google-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-google.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner at the top.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend.

         If your project contains apps for more than one platform, any that need to complete those steps will also display a flashing :guilabel:`Integrate` button. The reminder banner will remain in place until you have taken steps to update the configuration of each app in the project.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the steps at :ref:`Set Up Google Login <set-up-google>` to connect to your backend from your app.


.. _set-up-email-and-password:

Setup Email & Password Login in your Mobile App
================================================

:subscript:`Choose your platform:`

.. container:: option

   Android - Java
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add these permisions to the :file:`AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add these dependencies to the :file:`app/build.gradle` file:

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

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.


         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction completes.

         If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI. :code:`NextActivity`  :code:`Activity` class a user sees after a successful sign-in.


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

      Choose the Run icon in Android Studio to build your app and run it on your device/emulator. You should see our ready made sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following dependencies in your project's :file:`Podfile`.

         .. code-block:: bash

            platform :ios, '9.0'
            target :'YOUR-APP-NAME' do
                use_frameworks!
                pod 'AWSUserPoolsSignIn', '~> 2.6.13'
                pod 'AWSAuthUI', '~> 2.6.13'
                pod 'AWSMobileClient', '~> 2.6.13'
                # other pods
            end

      #. Pull the SDK libraries into your local repo.

         .. code-block::

             pod install --repo-update


      #. Create a AWSMobileClient and initialize the SDK.

         Add code to create an instance of :code:`AWSMobileClient` in the :code:`application:open url` function  of your :code:`AppDelegate.swift`, to resume a previously signed-in authenticated session.

         Then add another instance of :code:`AWSMobileClient` in the :code:`didFinishLaunching` function to register the sign in providers, and to fetch an Amazon Cognito credentials that AWS will use to authorize access once the user signs in.

         .. code-block:: swift

             import UIKit

             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add a AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add a AWSMobileClient call in application:didFinishLaunching
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

      #. Implement your sign-in UI by calling the library provided in the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

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

        Choose the Run icon in the top left of the Xcode window or type Command-R to build and run your app. You should see our pre-built sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

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

Setup Facebook Login in your Mobile App
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

            <!-- ... -->

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

            <!-- ... -->

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

            <!-- ... -->

            <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id" />

            <!-- ... -->

      #. Add these dependencies to your `app/build.gradle` file:

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

      #. In :file:`strings.xml`, add string definitions for your Facebook App ID and login protocol scheme.The value should contain your Facebook AppID in both cases, the login protocol value is always prefaced with :code:`fb`.

         .. code-block:: xml

            <string name="facebook_app_id">1231231231232123123</string>
            <string name="fb_login_protocol_scheme">fb1231231231232123123</string>

      #. Create an activity that will present your sign-in screen.

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction completes.

         If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI. :code:`NextActivity`  :code:`Activity` class a user sees after a successful sign-in.

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

      Choose the Run icon in Android Studio to build your app and run it on your device/emulator. You should see our ready made sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following dependencies in your project's :file:`Podfile` and run :code:`pod install --repo-update`.

         .. code-block:: bash

            platform :ios, '9.0'
              target :'YOUR-APP-NAME' do
                use_frameworks!
                pod 'AWSMobileClient', '~> 2.6.13'
                pod 'AWSFacebookSignIn', '~> 2.6.13'
                pod 'AWSAuthUI', '~> 2.6.13'
                # other pods
              end

      #. Add Facebook meta data to :file:`Info.plist`.

         To configure your Xcode project to use Facebook Login, right-choose :file:`Info.plist` and then choose :guilabel:`Open As > Source Code`.

         Add the following entry, using your project name, Facebook ID and login scheme ID.

         .. code-block:: xml

            <plist version="1.0">
            <!-- ... -->
            <dict>
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
            <key>CFBundleURLTypes</key>
            <array>
                <dict>
                    <key>CFBundleURLSchemes</key>
                    <array>
                        <string>fb0123456789012345</string>
                    </array>
                </dict>
            </array>
            </dict>
            <!-- ... -->

      #. Create a AWSMobileClient and initialize the SDK.

         Add code to create an instance of :code:`AWSMobileClient` in the :code:`application:open url` function  of your :code:`AppDelegate.swift`, to resume a previously signed-in authenticated session.

         Then add another instance of :code:`AWSMobileClient` in the :code:`didFinishLaunching` function to register the sign in providers, and to fetch an Amazon Cognito credentials that AWS will use to authorize access once the user signs in.

         .. code-block:: swift

             import UIKit

             //import AWSMobileClient
             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add a AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add a AWSMobileClient call in application:didFinishLaunching
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


      #. Implement your sign-in UI by calling the library provided by the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

                     if !AWSSignInManager.sharedInstance().isLoggedIn {
                        AWSAuthUIViewController
                          .presentViewController(with: self.navigationController!,
                               configuration: nil,
                               completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                                  if error != nil {
                                      print("Error occurred: \(String(describing: error))")
                                  } else {
                                      // sign in successful.
                                  }
                               })
                     }
                 }
             }

      Choose the Run icon in the top left of the Xcode window or type Command-R to build and run your app. You should see our pre-built sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

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

Setup Google Login in your Mobile App
=====================================

.. container:: option

   Android - Java
      .. list-table::
         :widths: 1 6

         * - **Use Android API level 23 or higher**

           - The AWS Mobile SDK library for Android sign-in (:code:`aws-android-sdk-auth-ui`) provides the activity and view for presenting a :code:`SignInUI` for the sign-in providers you configure. This library depends on the Android SDK API Level 23 or higher.

      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add these permissions to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add these dependencies to your `app/build.gradle` file:

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

         In Android Studio, choose :guilabel:`File > New > Activity > Basic Activity` and type an activity name, such as :userinput:`AuthenticatorActivity`. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity` in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

                <activity android:name=".AuthenticatorActivity">
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session. It makes a network call to retrieve the AWS credentials that allow users to access your AWS resources and registers a callback for when that transaction completes.

         If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI. :code:`NextActivity`  :code:`Activity` class a user sees after a successful sign-in.

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

      Choose the Run icon in Android Studio to build your app and run it on your device/emulator. You should see our ready made sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

      .. list-table::
         :widths: 1 6

         * - API References

           - * `AWSMobileClient <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/client/AWSMobileClient.html>`_

               :superscript:`A library that initializes the SDK, constructs CredentialsProvider and AWSConfiguration objects, fetches the AWS credentials, and creates a SDK SignInUI client instance.`

             * `Auth UserPools <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/userpools/CognitoUserPoolsSignInProvider.html>`_

               :superscript:`A wrapper Library for Amazon Cognito UserPools that provides a managed Email/Password sign-in UI.`

             * `Auth Core <https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobile/auth/core/IdentityManager.html>`_

               :superscript:`A library that caches and federates a login provider authentication token using Amazon Cognito Federated Identities, caches the federated AWS credentials, and handles the sign-in flow.`

   iOS - Swift
      #. Add or update your AWS backend configuration file to incorporate your new sign-in. For details, see the last steps in the :ref:`Get Started: Set Up Your Backend <add-aws-mobile-sdk-basic-setup>` section.

      #. Add the following dependencies in the Podfile and run **pod install --repo-update**

         .. code-block:: bash

              platform :ios, '9.0'
                target :'YOUR-APP-NAME' do
                  use_frameworks!
                  pod 'AWSMobileClient', '~> 2.6.13'
                  pod 'AWSGoogleSignIn', '~> 2.6.13'
                  pod 'AWSAuthUI', '~> 2.6.13'
                  pod 'GoogleSignIn', '~> 4.0'
                  # other pods
                end

      #. Add Google metadata to info.plist

         To configure your Xcode project to use Google Login, open its Info.plist file using **Right-click > Open As > Source Code.** Add the following entry. Substitute your project name for the placeholder string.

         .. code-block:: xml

            <plist version="1.0">
            <!-- ... -->
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

             //import AWSMobileClient
             import AWSMobileClient

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // Add a AWSMobileClient call in application:open url
                 func application(_ application: UIApplication, open url: URL,
                     sourceApplication: String?, annotation: Any) -> Bool {

                     return AWSMobileClient.sharedInstance().interceptApplication(
                         application, open: url,
                         sourceApplication: sourceApplication,
                         annotation: annotation)

                 }

                 // Add a AWSMobileClient call in application:didFinishLaunching
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

      #. Implement your sign-in UI by calling the library provided by the SDK.

         .. code-block:: swift

             import UIKit
             import AWSAuthCore
             import AWSAuthUI

             class SampleViewController: UIViewController {

                 override func viewDidLoad() {

                     super.viewDidLoad()

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


      Choose the Run icon in the top left of the Xcode window or type Command-R to build and run your app. You should see our pre-built sign-in UI for your app. Checkout the next steps to learn how to :ref:`customize your UI <add-aws-mobile-user-sign-in-customize>`.

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
                   Log.d(LOG_TAG, "User Signed In");
               }

               // Sign-out listener
               @Override
               public void onUserSignedOut() {

                   // return to the sign-in screen upon sign-out
                  showSignIn();
               }
           });

       To initiate a sign-out, call the :code:`signOut` method of :code:`IdentityManager`.

        .. code-block:: java

           IdentityManager.getDefaultIdentityManager().signOut();

   iOS - Swift
       To initiate a sign-out, add a call to  :code:`AWSSignInManager.sharedInstance().logout`.

       .. code-block:: swift

          @IBAction func signOutButtonPress(_ sender: Any) {

              AWSSignInManager.sharedInstance().logout(completionHandler: {(result: Any?, error: Error?) in
                  self.showSignIn()
                  // print("Sign-out Successful: \(signInProvider.getDisplayName)");

              })
          }

For a fuller example, see :ref:`Sign-out a Signed-in User <how-to-user-sign-in-sign-out>` in the How To section.

.. _auth-next-steps:

Next Steps
==========

  * :ref:`Customize the UI <add-aws-mobile-user-sign-in-customize>`

  * :ref:`Import Your Exisiting Amazon Cognito Identity Pool <how-to-cognito-integrate-an-existing-identity-pool>`

  * `Amazon Cognito Developer Guide <http://docs.aws.amazon.com/cognito/latest/developerguide/>`__


