.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-user-sign-in-customize:

#########################
Customize Your Sign-In UI
#########################

.. _customize-signin-ui-steps:



By default, the SDK presents sign-in UI for each sign in provider you enable in your |AMH| project (Email and Password, Facebook, Google) with a default look and feel. It knows which provider(s) you chose by reading the :file:`awsconfiguration.json` file you downloaded.

To override the defaults, and modify the behavior, look, and feel of the sign-in UI, create an :code:`AuthUIConfiguration` object and set the appropriate properties.

.. container:: option

    Android-Java
        Create and configure an :code:`AuthUIConfiguration` object and set its properties.

            * To present the Email and Password user :code:`SignInUI`, set :code:`userPools` to :code:`true`.

            * To present Facebook or Google  user :code:`SignInUI`, add :code:`signInButton(FacebookButton.class)` or :code:`signInButton(GoogleButton.class)`.

            * To change the logo, use the :code:`logoResId`.

            * To change the background color, use :code:`backgroundColor`.

            * To cancel the sign-in flow, set :code:`.canCancel(true)`.

            * To change the font in the sign-in views, use the :code:`fontFamily` method and pass in the string that represents a font family.

            * To draw the :code:`backgroundColor` full screen, use :code:`fullScreenBackgroundColor`.


        .. code-block:: java

            import android.app.Activity;
            import android.graphics.Color;
            import android.os.Bundle;

            import com.amazonaws.mobile.auth.facebook.FacebookButton;
            import com.amazonaws.mobile.auth.google.GoogleButton;
            import com.amazonaws.mobile.auth.ui.AuthUIConfiguration;
            import com.amazonaws.mobile.auth.ui.SignInUI;

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

            public class YourMainActivity extends Activity {
                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);

                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                        @Override
                        public void onComplete(final AWSStartupResult awsStartupResult) {
                            AuthUIConfiguration config =
                                new AuthUIConfiguration.Builder()
                                    .userPools(true)  // true? show the Email and Password UI
                                    .signInButton(FacebookButton.class) // Show Facebook button
                                    .signInButton(GoogleButton.class) // Show Google button
                                    .logoResId(R.drawable.mylogo) // Change the logo
                                    .backgroundColor(Color.BLUE) // Change the backgroundColor
                                    .isBackgroundColorFullScreen(true) // Full screen backgroundColor the backgroundColor full screenff
                                    .fontFamily("sans-serif-light") // Apply sans-serif-light as the global font
                                    .canCancel(true)
                                    .build();
                            SignInUI signinUI = (SignInUI) AWSMobileClient.getInstance().getClient(YourMainActivity.this, SignInUI.class);
                            signinUI.login(YourMainActivity.this, YourNextActivity.class).authUIConfiguration(config).execute();
                        }
                    }).execute();
                }
            }

    iOS - Swift
        Create and configure an :code:`AWSAuthUIConfiguration` object and set its properties.

        Create and configure an :code:`AuthUIConfiguration` object.

            * To present the Email and Password user :code:`SignInUI`, set et :code:`enableUserPoolsUI` to :code:`true`.

            * To present Facebook or Google  user :code:`SignInUI`, add :code:`.addSignInButtonView(class: AWSFacebookSignInButton.self)` or :code:`.addSignInButtonView(class: AWSFacebookSignInButton.self)`.

            * To change the logo, use :code:`logoImage`.

            * To change the background color, use :code:`backgroundColor`.

            * To cancel the sign-in flow, use :code:`canCancel`.

            * To change the font in the sign-in views, use the :code:`font` property and pass in the :code:`UIFont` object that represents a font family.

            * To draw the :code:`backgroundColor` full screen, use :code:`fullScreenBackgroundColor`.

        .. code-block:: swift

            import UIKit
            import AWSAuthUI
            import AWSMobileClient
            import AWSUserPoolsSignIn
            import AWSFacebookSignIn
            import AWSGoogleSignIn

            class SampleViewController: UIViewController {
                override func viewDidLoad() {
                    super.viewDidLoad()
                    if !AWSSignInManager.sharedInstance().isLoggedIn {
                        presentAuthUIViewController()
                    }
                }

                func presentAuthUIViewController() {
                    let config = AWSAuthUIConfiguration()
                    config.enableUserPoolsUI = true
                    config.addSignInButtonView(class: AWSFacebookSignInButton.self)
                    config.addSignInButtonView(class: AWSGoogleSignInButton.self)
                    config.backgroundColor = UIColor.blue
                    config.font = UIFont (name: "Helvetica Neue", size: 20)
                    config.isBackgroundColorFullScreen = true
                    config.canCancel = true

                    AWSAuthUIViewController.presentViewController(
                        with: self.navigationController!,
                        configuration: config, completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                            if error == nil {
                                // SignIn succeeded.
                            } else {
                                // end user faced error while loggin in, take any required action here.
                            }
                    })
                }
            }

