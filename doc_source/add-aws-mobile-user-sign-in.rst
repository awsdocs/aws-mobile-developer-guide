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
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the feature's tile.

      #. **Configure Email and Password sign-in**: Choose the feature and then select sign-in policies including: allowed login methods; multi-factor authentication; and password requirements and then choose :guilabel:`Create user pool`.

         .. image:: images/add-aws-mobile-sdk-email-and-password.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, for each app that will use the updates to your backend configuration, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend. If any apps in the project have not completed those steps the reminder banner and flashing button for those apps will remain in place.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the :ref:`next steps <set-up-email-and-password>` to connect to your backend from your app.

   Facebook
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the feature's tile.

      #. **Configure Facebook sign-in**: Choose the feature and then type your Facebook App ID and then choose :guilabel:`Enable Facebook login`. To retrieve or create your Facebook App ID, see `Setting Up Facebook Authentication. <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-facebook-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-facebook.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, for each app that will use the updates to your backend configuration, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend. If any apps in the project have not completed those steps the reminder banner and flashing button for those apps will remain in place.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the :ref:`next steps <set-up-facebook>` to connect to your backend from your app..


   Google
      #. Enable :guilabel:`User Sign-in`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the feature's tile.

      #. **Configure Google sign-in**: Choose the feature and then type in your Google Web App Client ID, and the Google Android or iOS Client ID (or both), and then choose Enable Google Sign-In. To retrieve or create your Google Client IDs, see `Setting Up Google Authentication <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/auth-google-setup.html>`__.

         .. image:: images/add-aws-mobile-sdk-google.png

      #. When you are done configuring providers, choose :guilabel:`Click here to return to project details page` in the blue banner.

          .. image:: images/updated-cloud-config.png

      #. On the project detail page, for each app that will use the updates to your backend configuration, choose the flashing :guilabel:`Integrate` button, and then complete the steps that guide you to connect your backend. If any apps in the project have not completed those steps the reminder banner and flashing button for those apps will remain in place.

          .. image:: images/updated-cloud-config2.png
             :scale: 25

      #. Follow the :ref:`next steps <set-up-google>` to connect to your backend from your app..


.. _set-up-email-and-password:

Setup Email & Password Login in your Mobile App
================================================

:subscript:`Choose your platform:`

.. container:: option

   Android-Java
      #. Add these permisions to the :file:`AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add these dependencies to the :file:`app/build.gradle` file:

         .. code-block:: java

             dependencies {
                  // Mobile Client for initializing the SDK
                  compile ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true; }

                  // Cognito UserPools for SignIn
                  compile 'com.android.support:support-v4:24.+'
                  compile ('com.amazonaws:aws-android-sdk-auth-userpools:2.6.+@aar') { transitive = true; }

                  // Sign in UI Library
                  compile 'com.android.support:appcompat-v7:24.+'
                  compile ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true; }
             }

      #. Create an activity that will present your sign-in screen, called :code:`AuthenticatorActivity` in the following fragments. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity`  in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session and to register a callback for credentials that allow users to access your AWS resources. If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI.

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

   iOS - Swift
      #. Add the following dependencies in your project's :file:`Podfile` and then run :code:`pod install --repo-update`.

         .. code-block:: bash

            platform :ios, '9.0'
            target :'YOUR-APP-NAME' do
                use_frameworks!
                pod 'AWSUserPoolsSignIn', '~> 2.6.13'
                pod 'AWSAuthUI', '~> 2.6.13'
                pod 'AWSMobileClient', '~> 2.6.13'
                # other pods
            end

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

.. _set-up-facebook:

Setup Facebook Login in your Mobile App
=======================================

.. container:: option

   Android-Java
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
              compile ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true; }

              // Facebook SignIn
              compile 'com.android.support:support-v4:24.+'
              compile ('com.amazonaws:aws-android-sdk-auth-facebook:2.6.+@aar') { transitive = true; }

              // Sign in UI
              compile 'com.android.support:appcompat-v7:24.+'
              compile ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true; }
            }

      #. In :file:`strings.xml`, add string definitions for your Facebook App ID and login protocol scheme.The value should contain your Facebook AppID in both cases, the login protocol value is always prefaced with :code:`fb`.

         .. code-block:: xml

            <string name="facebook_app_id">1231231231232123123</string>
            <string name="fb_login_protocol_scheme">fb1231231231232123123</string>

      #. Create an activity that will present your sign-in screen, called :code:`AuthenticatorActivity` in the following fragments. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity`  in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

            <activity android:name=".AuthenticatorActivity">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session and to register a callback for credentials that allow users to access your AWS resources. If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI.

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

   iOS - Swift
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

.. _set-up-google:

Setup Google Login in your Mobile App
=====================================

.. container:: option

   Android-Java
      #. Add these permissions to your `AndroidManifest.xml` file:

         .. code-block:: xml

            <uses-permission android:name="android.permission.INTERNET"/>
            <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add these dependencies to your `app/build.gradle` file:

         .. code-block:: java

              dependencies {
                  // Mobile Client for initializing the SDK
                  compile ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true; }

                  // Google SignIn
                  compile 'com.android.support:support-v4:24.+'
                  compile ('com.amazonaws:aws-android-sdk-auth-google:2.6.+@aar') { transitive = true; }

                  // Sign in UI Library
                  compile 'com.android.support:appcompat-v7:24.+'
                  compile ('com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar') { transitive = true; }
              }


      #. Create an activity that will present your sign-in screen, called :code:`AuthenticatorActivity` in the following fragments. If you want to make this your starting activity, move the the intent filter block containing :code:`.LAUNCHER` to the :code:`AuthenticatorActivity`  in your app's :file:`AndroidManifest.xml`.

         .. code-block:: xml

                <activity android:name=".AuthenticatorActivity">
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>

      #. Update the :code:`onCreate` function of your :code:`AuthenticatorActivity` to call :code:`AWSMobileClient`. This component provides the functionality to resume a signed-in authentication session and to register a callback for credentials that allow users to access your AWS resources. If the user is signed in, the app goes to the :code:`NextActivity`, otherwise it presents the user with the AWS Mobile ready made, configurable sign-in UI.

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

   iOS - Swift
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

.. _auth-next-steps:

Next Steps
========

  * :ref:`Customize the UI <add-aws-mobile-user-sign-in-customize>`

  * `Amazon Cognito Developer Guide <http://docs.aws.amazon.com/cognito/latest/developerguide/>`__


