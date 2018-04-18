.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-user-sign-in-sign-out:

#########################
Sign-out a Signed-in User
#########################


.. meta::
    :description:
        Learn how to add sign out flow for a signed in user in your mobile app.

.. list-table::
   :widths: 1 6

   * - **Prerequisite**

     - This section describes how to add sign-out flow for a signed-in user. In the following example, the built-in AWS Mobile SDK sign-in/sign-up screen is displayed after the user signs out.

       The examples on this page assume that you have added the AWS Mobile SDK to your mobile app using the steps on the `Add User Sign-in <https://docs.aws.amazon.com/aws-mobile/latest/developerguide/add-aws-mobile-user-sign-in.html>`__ page, and have configured an identity provider.

Enable User Sign-out
====================

.. container:: option

   Android - Java
       In the following example, :code:`AWSMobileClient` is instantiated within the :code:`onCreate` method of an activity called :code:`AuthenticatorActivity`.  If the client does not find a cached identity from a previous sign-in, it retrieves an unauthenticated “guest” Amazon Cognito Federated Identity ID that is used to access other AWS services. In Logcat, look for the string: :code:`Welcome to AWS!` to see that the client has successfully instantiated.

       If the user already has a cached authenticated identity ID from a previous sign-in, then  :code:`AWSMobileClient` will resume the session without an additional sign-in. In this case, :code:`IdentityManager.getDefaultIdentityManager().isUserSignedIn()` is set to :code:`true`.

       A :code:`SignInStateChangeListener` object is added to :code:`IdentityManager`, which captures :code:`onUserSignedIn` and :code:`onUserSignedOut` events.

       Finally, :code:`showSignIn()` is called to create a :code:`SignInUI` object, and to call the object's :code:`login` method. This displays the built-in sign-in UI of the SDK, and defines :code:`MainActivity` as the navigation target of a successful sign-in. The :code:`SignInUI` calls are placed in a separate function so they can also easily be called when the :code:`onUserSignedOut` event fires.

       In Logcat, a successful sign-in prints the string; :code:`Sign-in succeeded`.

       .. code-block:: java

            // AuthenticatorActivity.java

            package com.your-domain.android.YOUR-APP-NAME;

            import android.content.Intent;
            import android.support.v7.app.AppCompatActivity;
            import android.os.Bundle;
            import android.util.Log;
            import android.widget.TextView;

            // AWSMobileClient imports
            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

            // AWS SDK sign-in UI imports
            import com.amazonaws.mobile.auth.core.IdentityHandler;
            import com.amazonaws.mobile.auth.core.IdentityManager;
            import com.amazonaws.mobile.auth.core.SignInStateChangeListener;
            import com.amazonaws.mobile.auth.ui.SignInUI;

            public class AuthenticatorActivity extends AppCompatActivity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_authenticator);

                    AWSMobileClient.getInstance().initialize(this).execute();

                    // Sign-in listener
                    IdentityManager.getDefaultIdentityManager().addSignInStateChangeListener(new SignInStateChangeListener() {
                        @Override
                        public void onUserSignedIn() {
                            Log.d(LOG_TAG, "User Signed In");
                        }

                        // Sign-out listener
                        @Override
                        public void onUserSignedOut() {

                            Log.d(LOG_TAG, "User Signed Out");
                            showSignIn();
                        }
                    });

                    showSignIn();
                }


                /*
                 * Display the AWS SDK sign-in/sign-up UI
                 */
                private void showSignIn() {

                    Log.d(LOG_TAG, "showSignIn");

                    SignInUI signin = (SignInUI) AWSMobileClient.getInstance().getClient(AuthenticatorActivity.this, SignInUI.class);
                    signin.login(AuthenticatorActivity.this, MainActivity.class).execute();
                }
            }

       :code:`MainActivity` displays a sign-out button, that calls the :code:`signOut()` method of the :code:`IdentityManager`. This will fire the :code:`SignInStateChangeListener.onSignedOut()` event defined in the :code:`AuthenticatorActivity`. In Logcat, you should see the string: :code:`Signing out...`.

       :code:`onUserSignedOut()` then calls  :code:`showSignIn` which causes the sign-in screen to reappear.

        .. code-block:: java

            package com.dzmedia.android.YOUR-APP-NAME;

            import android.support.v7.app.AppCompatActivity;
            import android.os.Bundle;
            import android.util.Log;
            import android.view.View;
            import android.widget.Button;
            import android.widget.TextView;


            import com.amazonaws.mobile.auth.core.IdentityHandler;
            import com.amazonaws.mobile.auth.core.IdentityManager;
            import com.amazonaws.mobile.client.AWSMobileClient;

            public class MainActivity extends AppCompatActivity {

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_main);

                        // Create log out Button on click listener
                        Button clickButton = (Button) findViewById(R.id.signOutButton);
                        clickButton.setOnClickListener( new View.OnClickListener() {

                          public void onClick(View v) {
                              IdentityManager.getDefaultIdentityManager().signOut();
                        }
                    });
                }
                // other MainActivity code . . .
            }


   iOS - Swift
       In the following example, :code:`AWSMobileClient` is instantiated within the :code:`didfinishlaunching` and :code:`open url` blocks in :code:`AppDelegate`, as described in :ref:`Add User Sign-In <add-aws-mobile-user-sign-in>`.  If the client does not find a cached identity from a previous sign-in, it retrieves an unauthenticated “guest” Amazon Cognito Federated Identity ID that is used to access other AWS services. In debug output, look for the string: :code:`Welcome to AWS!`.

       If the user already has a cached authenticated identity ID from a previous sign-in, then  :code:`AWSMobileClient` will resume the session without an additional sign-in. In this case, :code:`AWSSignInManager.sharedInstance().isLoggedIn` is set to :code:`true`.

       When :code:`AWSMobileClient` is instantiated, the app navigates to a Navigation Control hosted in a ViewController whose UIView contains a sign-out button.  If the user is not already signed in, the viewDidLoad of the ViewController calls the built-in sign-in UI of the AWS Mobile SDK.  A successful sign-in prints the string: :code:`Sign-in succeeded` to debug output.

       In the action of the sign-out button, a successful sign-out calls for the sign-in screen to be displayed again.

        .. code-block:: swift

            // ViewController.swift

            import UIKit

            import AWSMobileClient
            import AWSAuthCore
            import AWSAuthCore
            import AWSAuthUI
            class ViewController: UIViewController {

                @IBOutlet weak var textfield: UITextField!

                public var identityId: String = ""

                override func viewDidLoad() {
                    super.viewDidLoad()

                    if !AWSSignInManager.sharedInstance().isLoggedIn {
                      showSignIn()
                }

                }

                override func didReceiveMemoryWarning() {
                    super.didReceiveMemoryWarning()
                    // Dispose of any resources that can be recreated.
                }

                @IBAction func signOutButtonPress(_ sender: Any) {
                        AWSSignInManager.sharedInstance().logout(completionHandler: {(result: Any?, error: Error?) in
                            self.showSignIn()
                         // print("Sign-out Successful: \(signInProvider.getDisplayName)");

                        })

                }


                func showSignIn() {
                        AWSAuthUIViewController.presentViewController(with: self.navigationController!, configuration: nil, completionHandler: {
                            (provider: AWSSignInProvider, error: Error?) in
                            if error != nil {
                                print("Error occurred: \(String(describing: error))")
                            } else {
                                print("Sign-in successful.")

                             }
                        })
                }
            }


