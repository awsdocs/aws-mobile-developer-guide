.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _getting-started:

###########
Get Started
###########

.. meta::
   :description: Integrate |AMHlong| features into your existing mobile app. Quickly add a powerful
      cloud backend that scales in capacity and cost.

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    Add Analytics <add-aws-mobile-analytics>
    Add User Sign-in <add-aws-mobile-user-sign-in>
    Add Push Notifications <add-aws-mobile-push-notifications>
    Add NoSQL Database <add-aws-mobile-nosql-database>
    Add User File Storage <add-aws-mobile-user-data-storage>
    Add Cloud Logic <add-aws-mobile-cloud-logic>
    Add Messaging <add-aws-mobile-messaging>
    Add Conversational Bots <add-aws-mobile-conversational-bots>
    Add Hosting and Streaming <add-aws-mobile-hosting-and-streaming>

.. _add-aws-mobile-sdk:

Overview
========

The AWS Mobile Android and iOS SDKs help you build high quality mobile apps quickly and easily. They provide easy access to a range of AWS services, including Amazon Cognito, AWS Lambda, Amazon S3, Amazon Kinesis, Amazon DynamoDB, Amazon Pinpoint and many more.

.. _add-aws-mobile-sdk-basic-setup:

Set Up Your Backend
===================

#. `Sign up for the AWS Free Tier. <https://aws.amazon.com/free/>`__

#. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`__ by signing into the console. The Mobile Hub console provides a single location for managing and monitoring your app's cloud resources.

   To integrate existing AWS resources using the SDK directly, without Mobile Hub, see :doc:`Setup  Options for Android <how-to-android-sdk-setup>` or :doc:`Setup  Options for iOS <how-to-ios-sdk-setup>`.

#. Name your project, check the box to allow Mobile Hub to administer resources for you and then choose :guilabel:`Add`.

.. container:: option

    Android - Java
      #. Choose :guilabel:`Android` as your platform and then choose Next.

         .. image:: images/wizard-createproject-platform-android.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-android.png
            :scale: 75


      #. Add the backend service configuration file to your app.

         In the Xcode Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of creating a raw directory in Android Studio.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         From the location where configuration file, :file:`awsconfiguration.json`, was downloaded in a previous step, drag it into the :file:`res/raw` folder.  Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      Your backend is now configured. Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-sdk-connect-to-your-backend>`.


    iOS - Swift
      #. Pick :guilabel:`iOS` as your platform and choose Next.

         .. image:: images/wizard-createproject-platform-ios.png
            :scale: 75

      #. Choose the :guilabel:`Download Cloud Config` and then choose :guilabel:`Next`.

         The :file:`awsconfiguration.json` file you download contains the configuration of backend resources that |AMH| enabled in your project. Analytics cloud services are enabled for your app by default.

         .. image:: images/wizard-createproject-backendsetup-ios.png
            :scale: 75

         .. _ios-add-backend-configuration:

      #. Add the backend service configuration file to your app.

         From your download location, place :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file in your Xcode project. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog. Choose :guilabel:`Next`.

         .. list-table::
            :widths: 1 6

            * - **Remember**

              - Every time you create or update a feature in your |AMH| project, download and integrate a new version of your :file:`awsconfiguration.json` into each app in the project that will use the update.

      Your backend is now configured. Follow the next steps at :ref:`Connect to Your Backend <add-aws-mobile-sdk-connect-to-your-backend>`.


.. _add-aws-mobile-sdk-connect-to-your-backend:

Connect to Your Backend
=======================

.. container:: option

   Android - Java
      #. Prerequisites

         * `Install Android Studio <https://developer.android.com/studio/index.html#downloads>`__ version 2.33 or higher.

         * Install Android SDK v7.11 (Nougat), API level 25.

      #. Your :file:`AndroidManifest.xml` must contain:

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET"/>
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

      #. Add dependencies to your :file:`app/build.gradle`, then choose :guilabel:`Sync Now` in the upper right of Android Studio. This libraries enable basic AWS functions, like credentials, and analytics.

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

              - When :code:`AWSMobileClient` is initialized, it constructs the :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects which, in turn, are used when creating other SDK clients. The client then makes a `Sigv4 signed <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ network call to `Amazon Cognito Federated Identities <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html>`__ to retrieve AWS credentials that provide the user access to your backend resources. When the network interaction succeeds, the :code:`onComplete` method of the :code:`AWSStartUpHandler` is called.

      Your app is now set up to interact with the AWS services you configured in your Mobile Hub project!

      Choose the run icon (|play|) in Android Studio to build your app and run it on your device/emulator. Look for :code:`Welcome to AWS!` in your Android Logcat output (choose :guilabel:`View > Tool Windows > Logcat`).

      .. list-table::
         :widths: 1

         * - **Optional:** The following example shows how to retrieve the reference to :code:`AWSCredentialsProvider` and :code:`AWSConfiguration` objects which can be used to instantiate other SDK clients. You can use the :code:`IdentityManager` to fetch the user's AWS identity id either directly from Amazon Cognito or from the locally cached identity id value.

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

   iOS - Swift
      #. Prerequisites

         * `Install Xcode <https://developer.apple.com/xcode/downloads/>`__ version 8.0 or later.

      #. Install Cocoapods. From a terminal window run:

         .. code-block:: bash

            sudo gem install cocoapods

      #. Create :file:`Podfile`. From a terminal window, navigate to the directory that contains your project's :file:`.xcodeproj` file and run:

          .. code-block:: bash

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

      Your app is now set up to interact with the AWS services you configured in your |AMH| project!

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

  * :ref:`Add Analytics <add-aws-mobile-analytics-app>`

  * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

  * :ref:`Add Push Notification <add-aws-mobile-push-notifications>`

  * :ref:`Add NoSQL Database <add-aws-mobile-nosql-database>`

  * :ref:`Add User File Storage <add-aws-mobile-user-data-storage>`

  * :ref:`Add Cloud logic <cloud-backend>`

  * :ref:`Add Messaging <add-aws-mobile-messaging>`

  * :ref:`Add Conversational Bots <add-aws-mobile-conversational-bots>`

  * :ref:`Add Hosting and Streaming <add-aws-mobile-hosting-and-streaming>`
