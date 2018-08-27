
.. _getting-started:

###########
Get Started
###########

.. meta::
   :description: Integrate AWS Amplify features into your existing mobile app. Quickly add a powerful cloud backend that scales in capacity and cost.

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    Add Analytics <add-aws-mobile-analytics>
    Add User Sign-in <add-aws-mobile-user-sign-in>
    Add Push Notifications <add-aws-mobile-push-notifications>
    Add User File Storage <add-aws-mobile-user-data-storage>
    Add Serverless Backend (AWS AppSync) <add-aws-mobile-serverless-backend>
    Add Cloud Logic <add-aws-mobile-cloud-logic>
    Add Messaging <add-aws-mobile-messaging>

.. _add-aws-mobile-sdk:

Choose your platform:

.. list-table::
   :widths: 1 1 1

   * - .. image:: images/android-java.png
          :target: getting-started.html#android-java

     - .. image:: images/android-kotlin.png
          :target: getting-started.html#android-kotlin

     - .. image:: images/ios-swift.png
          :target: getting-started.html#ios-swift

.. container:: option

   Android - Java
       .. _android-java:

       Get started creating your cloud backend with Amplify CLI for Android using Java.

   Android - Kotlin
       .. _android-kotlin:

       Get started creating your cloud backend with Amplify CLI for Android using Kotlin.

   iOS - Swift
       .. _ios-swift:

       Get started creating your cloud backend with Amplify CLI for iOS using Swift.

.. _add-aws-mobile-sdk-basic-setup-prerequisites:

Step 1: Set Up Your Development Environment
===========================================

We strongly recommend that you use the Amplify CLI for building the serverless backend for your app. If you have already installed the CLI, skip ahead to :ref:`Step 2 <add-aws-mobile-sdk-basic-setup>`.

*  `Sign up for an AWS Account <https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start>`__.

*  Install `Node.js <https://nodejs.org/>`__ and npm if they are not already on your machine.

Note: Verify that you are running at least Node.js version 8.x or greater and npm version 5.x or greater by running :code:`node -v` and :code:`npm -v` in a terminal/console window. Older versions may produce errors and are unsupported.

Now, install and configure the Amplify CLI globally.

.. code-block:: bash

   $ npm install -g @aws-amplify/cli

   $ amplify configure

Check the minimum requirements for your development environment.

    .. container:: option

       Android - Java
           * Choose the Android Java app project you want to integrate with an AWS backend.

           * `Install Android Studio <https://developer.android.com/studio/index.html#downloads>`__ version 2.33 or higher.

           * Install Android SDK for API level 23 (Android SDK 6.0).

       Android - Kotlin
           * Choose the Android Kotlin app project you want to integrate with an AWS backend.

           * `Install Android Studio <https://developer.android.com/studio/index.html#downloads>`__ version 2.33 or higher.

           * Install Android SDK for API level 23 (Android SDK 6.0).

       iOS - Swift
          * Choose the iOS app project you will integrate with an AWS backend.

          * `Install Xcode <https://developer.apple.com/xcode/downloads/>`__ version 8.0 or later.


.. _add-aws-mobile-sdk-basic-setup:

Step 2: Set Up Your Backend
===========================

#. Navigate to the root of your app files and add the SDK to your app. The CLI will prompt you for configuration parameters.

    .. code-block:: none

        $ cd ./ROOT_OF_YOUR_APP_FILES
        $ amplify init

#. To create your backend AWS resources run the following:

   .. container:: option

       Android - Java
          .. code-block:: bash

            $ amplify push


       Android - Kotlin
          .. code-block:: none

            $ amplify push

       iOS - Swift
          .. code-block:: none

            $ amplify push

          Then navigate to your app root, and drag :code:`awsconfiguration.json` into the root of your XCode project.  Choose :guilabel:`Copy items` if needed and then choose :guilabel:`Create groups` in the :guilabel:`Options` dialog box. Choose :guilabel:`Next`.

#. To verify that the CLI is set up for your app, run the following command. The CLI displays a status table with no resources listed. As you add categories to your app, backend resources created for your app are listed in this table.

   .. code-block:: none

      $ amplify status
      | Category | Resource name | Operation | Provider plugin |
      | -------- | ------------- | --------- | --------------- |

   Use the steps in the next section to configure the connection between your app and the serverless backend.

.. _add-aws-mobile-sdk-connect-to-your-backend:

Step 3: Connect to Your Backend
===============================

Perform the following steps to set up a connection to AWS services that you'll use in the Get Started section of this guide.

.. container:: option

   Android - Java
      #. Your :file:`AndroidManifest.xml` must contain:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add dependencies to your :file:`app/build.gradle`, and then choose :guilabel:`Sync Now` on the upper-right side of Android Studio. These libraries enable basic AWS functions, like credentials and analytics.

         .. code-block:: java

             dependencies {
                 implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
             }

      #. Add the following code to the :code:`onCreate` method of your main or startup activity. :code:`AWSMobileClient` is a singleton that establishes your connection to |AWS| and acts as an interface for your services.

         .. code-block:: java

            import com.amazonaws.mobile.client.AWSMobileClient;

              public class YourMainActivity extends Activity {
                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);

                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                        @Override
                        public void onComplete(AWSStartupResult awsStartupResult) {
                            Log.d("YourMainActivity", "AWSMobileClient is instantiated and you are connected to AWS!");
                        }
                    }).execute();

                    // More onCreate code ...
                }
              }

         .. list-table::
            :widths: 1 6

            * - What does this do?

              - When :code:`AWSMobileClient` is initialized, it constructs the :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects that, in turn, are used when creating other SDK clients. The client then makes a `Sigv4 signed <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ network call to `Amazon Cognito Federated Identities <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ to retrieve AWS credentials that provide the user access to your backend resources. When the network interaction succeeds, the :code:`onComplete` method of the :code:`AWSStartUpHandler` is called.

      Your app is now set up to interact with the AWS services you configured in your Amplify CLI project.

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. Look for :code:`Welcome to AWS!` in your Android Logcat output (choose :guilabel:`View > Tool Windows > Logcat`).

      :guilabel:`Reference AWSCredentialsProvider and AWSConfiguration (Optional)`

      The following example shows how to retrieve the reference to :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects that can be used to instantiate other SDK clients. You can use the :code:`IdentityManager` to fetch the user's AWS identity ID either directly from Amazon Cognito or from the locally cached identity ID value.

         .. code-block:: java

            import com.amazonaws.auth.AWSCredentialsProvider;
            import com.amazonaws.mobile.auth.core.IdentityHandler;
            import com.amazonaws.mobile.auth.core.IdentityManager;
            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;
            import com.amazonaws.mobile.config.AWSConfiguration;

            public class YourMainActivity extends Activity {

                private AWSCredentialsProvider credentialsProvider;
                private AWSConfiguration configuration;

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);

                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                        @Override
                        public void onComplete(AWSStartupResult awsStartupResult) {

                            // Obtain the reference to the AWSCredentialsProvider and AWSConfiguration objects
                            credentialsProvider = AWSMobileClient.getInstance().getCredentialsProvider();
                            configuration = AWSMobileClient.getInstance().getConfiguration();

                            // Use IdentityManager#getUserID to fetch the identity id.
                            IdentityManager.getDefaultIdentityManager().getUserID(new IdentityHandler() {
                                @Override
                                public void onIdentityId(String identityId) {
                                    Log.d("YourMainActivity", "Identity ID = " + identityId);

                                    // Use IdentityManager#getCachedUserID to
                                    //  fetch the locally cached identity id.
                                    final String cachedIdentityId =
                                        IdentityManager.getDefaultIdentityManager().getCachedUserID();
                                }

                                @Override
                                public void handleError(Exception exception) {
                                    Log.d("YourMainActivity", "Error in retrieving the identity" + exception);
                                }
                            });
                        }
                    }).execute();

                    // .. more code
                }
            }

   Android - Kotlin
      #. Your :file:`AndroidManifest.xml` must contain the following:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add dependencies to your :file:`app/build.gradle`, and then choose :guilabel:`Sync Now` on the upper-right side of Android Studio. These libraries enable basic AWS functions, like credentials and analytics.

         .. code-block:: java

             dependencies {
                 implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
             }

      #. Add the following code to the :code:`onCreate` method of your main or startup activity. :code:`AWSMobileClient` is a singleton that establishes your connection to |AWS| and acts as an interface for your services.

         .. code-block:: kotlin

            import com.amazonaws.mobile.client.AWSMobileClient;

            class YourMainActivity : Activity() {
              companion object {
                private val TAG: String = this::class.java.simpleName
              }

              override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState);

                AWSMobileClient.getInstance().initialize(this) {
                  Log.d(TAG, "AWSMobileClient is initialized")
                }.execute()

                // More onCreate code...
              }
            }

         .. list-table::
            :widths: 1 6

            * - What does this do?

              - When :code:`AWSMobileClient` is initialized, it constructs the :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects which, in turn, are used when creating other SDK clients. The client then makes a `Sigv4 signed <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ network call to `Amazon Cognito Federated Identities <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ to retrieve AWS credentials that provide the user access to your backend resources. When the network interaction succeeds, the callback (which is technically the :code:`onComplete` method of the :code:`AWSStartUpHandler`) is called.

      Your app is now set up to interact with the AWS services you configured in your Amplify CLI project.

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. Look for :code:`Welcome to AWS!` in your Android Logcat output (choose :guilabel:`View > Tool Windows > Logcat`).

      :guilabel:`Reference AWSCredentialsProvider and AWSConfiguration (Optional)`

      The following example shows how to retrieve the reference to :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects that can be used to instantiate other SDK clients. You can use the :code:`IdentityManager` to fetch the user's AWS identity ID either directly from Amazon Cognito or from the locally cached identity ID value.

         .. code-block:: kotlin

            import com.amazonaws.auth.AWSCredentialsProvider
            import com.amazonaws.mobile.auth.core.IdentityHandler
            import com.amazonaws.mobile.auth.core.IdentityManager
            import com.amazonaws.mobile.client.AWSMobileClient
            import com.amazonaws.mobile.config.AWSConfiguration

            class YourMainActivity : Activity() {
              companion object {
                private val TAG: String = this::class.java.simpleName
              }

              private var credentialsProvider: AWSCredentialsProvider? = null
              private var awsConfiguration: AWSConfiguration? = null

              override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState);

                AWSMobileClient.getInstance().initialize(this) {
                  credentialsProvider = AWSMobileClient.getInstance().credentialsProvider
                  awsConfiguration = AWSMobileClient.getInstance().configuration

                  IdentityManager.getDefaultIdentityManager().getUserID(object : IdentityHandler {
                    override fun handleError(exception: Exception?) {
                      Log.e(TAG, "Retrieving identity: ${exception.message}")
                    }

                    override fun onIdentityId(identityId: String?) {
                      Log.d(TAG, "Identity = $identityId")
                      val cachedIdentityId = IdentityManager.getDefaultIdentityManager().cachedUserID
                      // Do something with the identity here
                    }
                  })
                }.execute()

                // More onCreate code...
              }
            }

   iOS - Swift
      #. Install Cocoapods. From a terminal window run:

         .. code-block:: none

            sudo gem install cocoapods

      #. Create :file:`Podfile`. From a terminal window, navigate to the directory that contains your project's :file:`.xcodeproj` file and run:

          .. code-block:: none

              pod init

      #. Add core AWS Mobile SDK components to your build.

         .. code-block:: none

              platform :ios, '9.0'
              target :'YOUR-APP-NAME' do
                  use_frameworks!
                  pod 'AWSMobileClient', '~> 2.6.13'
                  # other pods
              end

      #. Install dependencies by runnng:

         .. code-block:: none

             pod install --repo-update

         If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

      #. The command :code:`pod install` creates a new workspace file. Close your Xcode project and reopen it using :file:`./YOUR-PROJECT-NAME.xcworkspace`.

         .. list-table::
             :widths: 1 6

             * - Use **ONLY** your .xcworkspace

               - Remember to always use :file:`./YOUR-PROJECT-NAME.xcworkspace` to open your Xcode project from now on.

      #. Rebuild your app after reopening it in the workspace to resolve APIs from new libraries called in your code. This is a good practice any time you add import statements.

      #. Replace the :code:`return true` statement in :code:`didFinishLaunching` with the following code in your AppDelegate to establish a run-time connection with AWS Mobile.

         .. code-block:: swift

            import UIKit
            import AWSMobileClient

            @UIApplicationMain
            class AppDelegate: UIResponder, UIApplicationDelegate {

            func application(_ application: UIApplication,
                             didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                // Override point for customization after application launch.

                // Create AWSMobileClient to connect with AWS
                return AWSMobileClient.sharedInstance().interceptApplication(
                    application,
                    didFinishLaunchingWithOptions: launchOptions)

            }


         .. list-table::
            :widths: 1 6

            * - What does this do?

              - When :code:`AWSMobileClient` is initialized, it makes a `Sigv4 signed <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ network call to `Amazon Cognito Federated Identities <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ to retrieve AWS credentials that provide the user access to your backend resources. When the network interaction succeeds, the :code:`onComplete` method of the :code:`AWSStartUpHandler` is called.

      Your app is now set up to interact with the AWS services you configured in your Amplify CLI project!

      Choose the run icon (|play|) in the top left of the Xcode window or type |Acommand|-R to build and run your app. Look for  :code:`Welcome to AWS!` in the log output.

      .. list-table::
         :widths: 1

         * - **Optional:** If you want to make sure you're connected to AWS, import :code:`AWSCore` and add the following code to :code:`didFinishLaunchingWithOptions` before you return :code:`AWSMobileClient`.

             .. code-block:: swift

                  import AWSCore

                        //. . .

                  AWSDDLog.add(AWSDDTTYLogger.sharedInstance)
                  AWSDDLog.sharedInstance.logLevel = .info

             **Optional:** The following example shows how to retrieve the reference to :code:`AWSCredentialsProvider` object which can be used to instantiate other SDK clients. You can use the :code:`AWSIdentityManager` to fetch the AWS identity id of the user from Amazon Cognito.

             .. code-block:: swift

                  import UIKit
                  import AWSMobileClient
                  import AWSAuthCore

                  class ViewController: UIViewController {

                      @IBOutlet weak var textfield: UITextField!
                      override func viewDidLoad() {
                          super.viewDidLoad()
                          textfield.text = "View Controller Loaded"

                          // Get the AWSCredentialsProvider from the AWSMobileClient
                          let credentialsProvider = AWSMobileClient.sharedInstance().getCredentialsProvider()

                          // Get the identity Id from the AWSIdentityManager
                          let identityId = AWSIdentityManager.default().identityId
                      }
                  }

.. _add-aws-mobile-sdk-next-steps:

Next Steps
==========

  * :ref:`Add Analytics <add-aws-mobile-analytics>`

  * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

  * :ref:`Add Push Notification <add-aws-mobile-push-notifications>`

  * :ref:`Add User File Storage <add-aws-mobile-user-data-storage>`

  * :ref:`Add Serverless Backend <add-aws-mobile-serverless-backend>`

  * :ref:`Add Cloud logic <add-aws-mobile-cloud-logic>`

  * :ref:`Add Messaging <add-aws-mobile-messaging>`

