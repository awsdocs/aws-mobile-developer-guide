.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-cognito-integrate-an-existing-identity-pool:

########################################
How to Integrate Your Existing Identity Pool
########################################

.. _native-integrate-exisitng-identity-pool:

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-user-sign-in>` to install the SDK and integrate Amazon Cognito.

The :ref:`Get Started <add-aws-mobile-user-sign-in>` section of this guide allows you to create new resources and complete the steps described on this page in minutes. If you want to import existing resources or create them from scratch, this page will walk you through the following steps:

    * Set up short-lived credentials for accessing your AWS resources using a `Cognito Identity Pool <http://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html>`__.

    * Create an AWS Mobile configuration file that ties your app code to the identity pool that enables users to acces your AWS resources.

    * Make small adjustments to your app code to install the SDK and retrieve AWS credentials for your user.


Set Up Your Backend
===================

.. _import-an-existing-identity-pool:


.. _create-a-new-identity-pool:

Create a New Identity Pool
--------------------------

.. list-table::
   :widths: 1 6

   * - **Or Import an Existing Identity Pool**

     - If you already have an Amazon Cognito Identity Pool and know its ID and region, you can skip to :ref:`how-to-auth-connect-to-your-backend`.


#. Go to `Amazon Cognito Console <https://console.aws.amazon.com/cognito>`__ and choose :guilabel:`Manage Federated Identities`.

#. Choose :guilabel:`Create new Identity pool` on the top left of the console.

#. Type a name for the Identity pool, select :guilabel:`Enable access to unauthenticated identities` under the :guilabel:`Unauthenticated Identities` section, and then choose :guilabel:`Create pool` on the bottom right.

#. Expand the :guilabel:`View Details` section to see the two roles that are to be created to enable access to your bucket. Copy and keep both the Authenticated and Unauthenticated role names, in the form of :code:`Cognito_<IdentityPoolName>Auth_Role` and :code:`Cognito_<IdentityPoolName>Unauth_Role`. In many cases, you will modify the permissions policy of these roles to control access to AWS resources that you add to your app.

#. Choose  :guilabel:`Allow` on the bottom right.

#. In the code snippet labeled :guilabel:`Get AWSCredentials` displayed by the console, copy the Identity Pool ID and the Region for use in a following configuration step. You will use these values to connect your backend to your app.


.. _how-to-auth-connect-to-your-backend:

Connect to Your Backend
=======================

Create the awsconfiguration.json file
-------------------------------------

#. Create a file with name :file:`awsconfiguration.json` with the following contents:

    .. code-block:: json

      {
          "Version": "1.0",
          "CredentialsProvider": {
              "CognitoIdentity": {
                  "Default": {
                      "PoolId": "COGNITO-IDENTITY-POOL-ID",
                      "Region": "COGNITO-IDENTITY-POOL-REGION"
                  }
              }
          },
          "IdentityManager" : {
            "Default" : {

            }
          }
      }


#. Make the following changes to the configuration file.

    * Replace the :code:`COGNITO-IDENTITY-POOL-ID` with the identity pool ID.

    * Replace the :code:`COGNITO-IDENTITY-POOL-REGION` with the region the identity pool was created in.


      .. list-table::
         :widths: 1 6

         * - Need to find your pool's ID and region?

           - Go to `Amazon Cognito Console <https://console.aws.amazon.com/cognito>`__ and choose :guilabel:`Manage Federated Identities`, then choose your pool and choose :guilabel:`Edit identity pool`. Copy the value of :guilabel:`Identity pool ID`.

             Insert this region value into the following form to create the value you need for this integration.

             .. code-block:: bash

                "Region": "REGION-PREFIX-OF-YOUR-POOL-ID".

             For example, if your pool ID is :code:`us-east-1:01234567-yyyy-0123-xxxx-012345678901`, then your integration region value would be:

             .. code-block:: bash

                "Region": "us-east-1"

Add the awsconfiguration.json file to your app
-----------------------------------------------

.. container:: option

    Android - Java
      Place the :file:`awsconfiguration.json` file you created in the previous step into a :file:`res/raw` `Android Resource Directory <https://developer.android.com/studio/write/add-resources.html>`__ in your Android project.

    iOS - Swift
      Drag the :file:`awsconfiguration.json` into the folder containing your :file:`Info.plist` file in your Xcode project. Choose :guilabel:`Copy items` and :guilabel:`Create groups` in the options dialog.


Add the SDK to your App
-----------------------

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none

               dependencies {
                  compile ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true; }

                  // other dependencies . . .
               }

         #. Perform a Gradle sync to download the AWS Mobile SDK components into your app.

         #. Add the following code to the :code:`onCreate` method of your main or startup activity. This will establish a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

            Once the network call to retrieve the user's AWS identity ID has succeeded, you can get the users identity using :code:`getCachedUserID()` from the :code:`AWSIdentityManager`.

            .. code-block:: java

                import com.amazonaws.auth.AWSCredentialsProvider;
                import com.amazonaws.mobile.auth.core.IdentityHandler;
                import com.amazonaws.mobile.auth.core.IdentityManager;
                import com.amazonaws.mobile.client.AWSMobileClient;
                import com.amazonaws.mobile.client.AWSStartupHandler;
                import com.amazonaws.mobile.client.AWSStartupResult;

                public class MainActivity extends AppCompatActivity {

                    @Override
                    protected void onCreate(Bundle savedInstanceState) {
                        super.onCreate(savedInstanceState);
                        setContentView(R.layout.activity_main);

                        AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                            @Override
                            public void onComplete(AWSStartupResult awsStartupResult) {

                                //Make a network call to retrieve the identity ID
                                // using IdentityManager. onIdentityId happens UPon success.
                                IdentityManager.getDefaultIdentityManager().getUserID(new IdentityHandler() {

                                    @Override
                                    public void onIdentityId(String s) {

                                        //The network call to fetch AWS credentials succeeded, the cached
                                        // user ID is available from IdentityManager throughout your app
                                        Log.d("MainActivity", "Identity ID is: " + s);
                                        Log.d("MainActivity", "Cached Identity ID: " + IdentityManager.getDefaultIdentityManager().getCachedUserID());
                                    }

                                    @Override
                                    public void handleError(Exception e) {
                                        Log.e("MainActivity", "Error in retrieving Identity ID: " + e.getMessage());
                                    }
                                });
                            }
                        }).execute();
                    }
                }

            When you run your app, you should see no behavior change. To verify success, look for the message :code:`"Welcome to AWS!"` in your debug output.


   iOS - Swift
      Set up AWS Mobile SDK components as follows:

         #. Add the :code:`AWSMobileClient` pod to your :file:`Podfile` to install the AWS Mobile SDK.

            .. code-block:: swift

               platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                      pod 'AWSMobileClient', '~> 2.6.13'

                      # other pods . . .

                  end

         #. Run :code:`pod install --repo-update` in your app root folder before you continue.


         #. Add the following code to your AppDelegate to establish a run-time connection with AWS Mobile.

            .. code-block:: swift

               import UIKit
               import AWSMobileClient

               @UIApplicationMain
               class AppDelegate: UIResponder, UIApplicationDelegate {

                 func application(_ application: UIApplication,
                       didFinishLaunchingWithOptions launchOptions:

                       [UIApplicationLaunchOptionsKey: Any]?) -> Bool {


                       // Uncomment to turn on logging, look for "Welcome to AWS!" to confirm success
                       // AWSDDLog.add(AWSDDTTYLogger.sharedInstance)
                       // AWSDDLog.sharedInstance.logLevel = .info


                       // Instantiate AWSMobileClient to get AWS user credentials
                       return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)

                 }
               }

            When you run your app, you should see no behavior change. To verify success, turn on logging by uncommenting the lines in the preceding example, and look for the message :code:`"Welcome to AWS!"` in your the output.

         #. To get the users identity, use :code:`getCredentialsProvider()` to access :code:`AWSIdentityManager`, shown here being done in a :code:`ViewController`.

             .. code-block:: swift

                import UIKit
                import AWSMobileClient
                import AWSAuthCore

                class ViewController: UIViewController {

                    @IBOutlet weak var textfield: UITextField!
                    override func viewDidLoad() {
                        super.viewDidLoad()
                        textfield.text = "View Controller Loaded"

                        // Get the identity Id from the AWSIdentityManager
                        let appDelegate = UIApplication.shared.delegate as! AppDelegate
                        let credentialsProvider = AWSMobileClient.sharedInstance().getCredentialsProvider()
                        let identityId = AWSIdentityManager.default().identityId
                    }
                }



Next Steps
==========

* For further information, see `Amazon Cognito Developer Guide <https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html>`__.
