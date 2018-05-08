.. _add-aws-mobile-sdk:

##################################
Add the AWS Mobile SDK to Your App
##################################


.. meta::
   :description: Integrate |AMHlong| features into your existing mobile app. Quickly add a powerful
      cloud backend that scales in capacity and cost.


.. _add-aws-mobile-sdk-basic-setup:

Basic Backend Setup
===================


:subscript:`Choose your platform.`

.. container:: option

   Android - Java
      #. `Get a free AWS Account. <https://aws.amazon.com/free>`_

      #. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`_ to enable backend features for your app, if you
         don't already have one.

         Already have an app using a Mobile Hub custom SDK?
         :ref:`aws-mobile-sdk-migrate`.

         .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
            :scale: 100
            :alt: Image of the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 75

         :emphasis:`Analytics are enabled by default for new projects created in Mobile Hub.`

      #. Download your Mobile Hub project configuration file.

         #. In the Mobile Hub console, choose your project, and then choose the :guilabel:`Integrate` icon from the left margin.

         #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

            .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
               :scale: 100 %
               :alt: Image of the Mobile Hub console when choosing Download Configuration File.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                  :scale: 75

          *Remember:*

          Each time you change the Mobile Hub project for your app, download and use a fresh :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use fresh files for those features.

   Android - Kotlin
      #. `Get a free AWS Account. <https://aws.amazon.com/free>`_

      #. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`_ to enable backend features for your app, if you
         don't already have one.

         Already have an app using a Mobile Hub custom SDK?
         :ref:`aws-mobile-sdk-migrate`.

         .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
            :scale: 100
            :alt: Image of the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 75

         :emphasis:`Analytics are enabled by default for new projects created in Mobile Hub.`

      #. Download your Mobile Hub project configuration file.

         #. In the Mobile Hub console, choose your project, and then choose the :guilabel:`Integrate` icon from the left margin.

         #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

            .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
               :scale: 100 %
               :alt: Image of the Mobile Hub console when choosing Download Configuration File.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                  :scale: 75

          *Remember:*

          Each time you change the Mobile Hub project for your app, download and use a fresh :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use fresh files for those features.


   iOS - Swift
      #. `Get a free AWS Account. <https://aws.amazon.com/free>`_

      #. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub/>`_ to enable backend features for your app, if you
         don't already have one.

         :emphasis:`Analytics are enabled by default for new projects created in Mobile Hub.`

         Already have an app using a Mobile Hub custom SDK?
         :ref:`aws-mobile-sdk-migrate`.

         .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
            :scale: 100
            :alt: Image of the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-mobile-hub-console.png
               :scale: 75

      #. Download your Mobile Hub project configuration file.

         #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate`
            icon from the left margin.

         #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json`
            file that connects your app to your backend.

         :emphasis:`Remember:`

         Each time you change the |AMH| project for your app, download and
         use a fresh :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL
         Database or Cloud Logic are changed, also download and use fresh files for those
         features.

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 100
            :alt: Image of the Download Configuration Files button in the |AMH| console.

         .. only:: pdf

            .. image::  images/add-aws-mobile-sdk-download-configuration-file.png
              :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
               :scale: 75


   JavaScript
      New!

      **Try our Starter Tutorials to get up and running with Mobile Hub and JavaScript:**

      .. list-table::
        :widths: 1 2

        * - .. image:: images/react-icon.png
               :target: https://github.com/awslabs/aws-mobile-react-sample

            `REACT STARTER KIT <https://github.com/awslabs/aws-mobile-react-sample>`_
          - .. image:: images/ionic-icon.png
               :target: https://github.com/ionic-team/ionic2-starter-aws

            `IONIC STARTER KIT <https://github.com/ionic-team/ionic2-starter-aws>`_


      Or, manually create your backend and integrate the SDK into your
      JavaScript web app with the following steps.

      #. `Get a free AWS Account. <https://aws.amazon.com/free/>`_

      #. `Create a Mobile Hub project <https://console.aws.amazon.com/mobilehub>`_ to enable backend features for your app. If you
         already have a |AMH| app, open it.


         #. Choose the :ref:`hosting-and-streaming` feature.

            .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                :scale: 100
                :alt: Image of the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                  :scale: 75

         #. Check the box to indicate you understand that content hosted by the feature is public,
            then choose :guilabel:`Enable`.


            .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
               :scale: 100
               :alt: Image of the |AMH| console with Hosting and Streaming enabled.

            .. only:: pdf

               .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                  :scale: 75

      #. Download your Mobile Hub project configuration file.`

         Choose :guilabel:`Download aws-config.js file` towards the bottom right.

         .. image:: images/add-aws-mobile-add-hosting-and-streaming-download-config.png
            :scale: 100
            :alt: Image of the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-add-hosting-and-streaming-download-config.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-add-hosting-and-streaming-download-config.png
               :scale: 75

.. _add-aws-mobile-sdk-setup-app:

Set Up Your App for AWS Mobile Services
=======================================

If you have not created a |AMH| project and downloaded its configuration file, see
:ref:`add-aws-mobile-sdk-basic-setup`.

:subscript:`Choose your platform.`

.. container:: option

   Android - Java
      #. `Install Android Studio <https://developer.android.com/studio/index.html>`_
         version 2.33 or higher .

      #. Install Android SDK version 7.11 (Nougat), API level 25

         In Android Studio, from the top menu bar choose :guilabel:`Tools > Android > SDK Manager`
         to install an SDK version.

      #. Add the backend service configuration file to your app.`


         #. Open your mobile app project in Android Studio and choose :guilabel:`Project` in the
            left margin to open project view.

         #. Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android
            Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown
            menu.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of the Download Configuration Files button in the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

            Learn more about `Android Studio
            <https://developer.android.com/studio/intro/index.html>`_.

         #. From the location where configuration files were downloaded in a previous step, drag
            :file:`awsconfiguration.json` into the :file:`res/raw` folder.

      #. Add dependencies to the your app/build.gradle.

         Add the following `Android gradle dependencies
         <https://docs.gradle.org/current/userguide/artifact_dependencies_tutorial.html>`_ entries
         and configuration to your :file:`app/build.gradle`. These libraries enable basic AWS
         functions, like credentials, and analytics. Adding `:code:`multidex application`
         <https://developer.android.com/studio/build/multidex.html>`_ configuration ensures that you
         won't run into method count limitations in your app.

         .. code-block:: none
            :emphasize-lines: 6, 18

             android {
                 defaultConfig {
                     ...
                     multiDexEnabled true
                 }
                 ...
             }

             dependencies {
               compile 'com.android.support:multidex:1.0.1'
               compile 'com.amazonaws:aws-android-sdk-core:2.6.0'
               compile ('com.amazonaws:aws-android-sdk-auth-core:2.6.0@aar')  {transitive = true;}
             }

      #. Create an :code:`Application` class and add the following code to its
         :code:`onCreate` method.

         To create the class, right click on the :file:`java` folder in your Xcode project explorer,
         and then choose :guilabel:`New > Java Class`. Name the class :code:`Application` and choose
         public for :guilabel:`Visibility` and none for :guilabel:`Modifiers`.

         .. code-block:: java

             import com.amazonaws.mobile.config.AWSConfiguration;
             import com.amazonaws.mobile.auth.core.IdentityManager;
             import android.support.multidex.MultiDexApplication;


             /**
              * Application class responsible for initializing singletons and other common components.
              */
             public class Application extends MultiDexApplication {
                 private static final String LOG_TAG = Application.class.getSimpleName();


                 @Override
                 public void onCreate() {
                     super.onCreate();
                     initializeApplication();

                 }

                 private void initializeApplication() {

                    AWSConfiguration awsConfiguration = new AWSConfiguration(getApplicationContext());

                    // If IdentityManager is not created, create it
                    if (IdentityManager.getDefaultIdentityManager() == null) {
                            IdentityManager identityManager =
                                 new IdentityManager(getApplicationContext(), awsConfiguration);
                            IdentityManager.setDefaultIdentityManager(identityManager);
                    }

                 }
             }

      #. Create a :code:`SplashActivity` class or modify your existing splash activity.


         #. To create the activity, right click on the :file:`java` folder in your Xcode project
            explorer, and then choose :guilabel:`File > New > Activity > Basic Activity`.


            .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
               :scale: 100
               :alt: Image of the Download Configuration Files button in the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
                  :scale: 75

         #. Add the following code to the activity's :code:`onCreate` method to establish user
            credentials that enable access to AWS services whenever your app starts.

            .. code-block:: java

                import com.amazonaws.mobile.config.AWSConfiguration;
                import com.amazonaws.mobile.auth.core.IdentityManager;
                import com.amazonaws.mobile.auth.core.StartupAuthResultHandler;
                import com.amazonaws.mobile.auth.core.StartupAuthResult;

                public class SplashActivity extends AppCompatActivity {

                    @Override
                    protected void onCreate(Bundle savedInstanceState) {
                        super.onCreate(savedInstanceState);
                        setContentView(R.layout.activity_splash);

                        Context appContext = getApplicationContext();
                        AWSConfiguration awsConfig = new AWSConfiguration(appContext);
                        IdentityManager identityManager = new IdentityManager(appContext, awsConfig);
                        IdentityManager.setDefaultIdentityManager(identityManager);
                        identityManager.doStartupAuth(this, new StartupAuthResultHandler() {
                            @Override
                            public void onComplete(StartupAuthResult startupAuthResult) {
                                // User identity is ready as unauthenticated user or previously signed-in user.
                            }
                        });

                        // Go to the main activity
                        final Intent intent = new Intent(this, :samp:`{MainActivity}`.class)
                                .setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                        this.startActivity(intent);
                        this.finish();

                    }
                }

      #. Modify your app manifest to add `Android permissions
         <https://developer.android.com/guide/topics/permissions/requesting.html>`_

         Delete the :code:`intent-filter` declarations for the :code:`MAIN` action and and
         :code:`LAUNCHER` category from your original start up activity. If there are no other
         declarations in the :code:`intent-filter`, then also delete the empty
         :code:`<intent-filter></intent-filter>` tags.

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET" />
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
             <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
              . . .
             <application
                 android:name="com.:samp:`{yourpackagename}`.Application">
              . . .
                <activity android:name=".SplashActivity" >
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>
                 <activity android:name=".MainActivity" >
                    <intent-filter>
                        <!--
                             * REMOVE THESE FROM YOUR START UP ACTIVITY

                                 <action android:name="android.intent.action.MAIN" />
                                 <category android:name="android.intent.category.LAUNCHER" />

                             *    IF THERE ARE NO OTHER ITEMS INSIDE THE intent-filter
                             *    TAGS, DELETE THE TAGS

                         -->
                    </intent-filter>
                </activity>

              . . .
             </application>

         :emphasis:`Make sure to remove the MAIN action and LAUNCHER category from your previous
         starting activity's :code:`intent-filter`.`

      #. Click the :guilabel:`Run` icon (the one that looks like a Play button) in Android Studio to
         build your app and run it on your device/emulator. After your app is deployed, search
         through your logcat for a message similar to :code:`"IdentityManager: Got user ID:
         us-east-1:abcabcabc-0be6-444e-b101-abcabcabc"`. If you see the log, your app is
         successfully connected to AWS services.

      Your app is now set up to interact with the AWS services you configured in your |AMH| project!

   Android - Kotlin
      #. `Install Android Studio <https://developer.android.com/studio/index.html>`_
         version 3.1 or higher .

      #. Install Android SDK version 7.11 (Nougat), API level 25

         In Android Studio, from the top menu bar choose :guilabel:`Tools > Android > SDK Manager`
         to install an SDK version.

      #. Add the backend service configuration file to your app.`

         #. Open your mobile app project in Android Studio and choose :guilabel:`Project` in the
            left margin to open project view.

         #. Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android
            Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown
            menu.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of the Download Configuration Files button in the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

            Learn more about `Android Studio
            <https://developer.android.com/studio/intro/index.html>`_.

         #. From the location where configuration files were downloaded in a previous step, drag
            :file:`awsconfiguration.json` into the :file:`res/raw` folder.

      #. Add dependencies to the your app/build.gradle.

         Add the following `Android gradle dependencies
         <https://docs.gradle.org/current/userguide/artifact_dependencies_tutorial.html>`_ entries
         and configuration to your :file:`app/build.gradle`. These libraries enable basic AWS
         functions, like credentials, and analytics. Adding `:code:`multidex application`
         <https://developer.android.com/studio/build/multidex.html>`_ configuration ensures that you
         won't run into method count limitations in your app.

         .. code-block:: none
            :emphasize-lines: 6, 18

             dependencies {
               compile 'com.amazonaws:aws-android-sdk-core:2.6.+'
               compile ('com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar')  {transitive = true;}
             }

      #. Create an :code:`Application` class and add the following code to its
         :code:`onCreate` method.

         To create the class, right click on the :file:`java` folder in your Xcode project explorer,
         and then choose :guilabel:`New > Java Class`. Name the class :code:`Application` and choose
         public for :guilabel:`Visibility` and none for :guilabel:`Modifiers`.

         .. code-block:: kotlin

             import com.amazonaws.mobile.config.AWSConfiguration;
             import com.amazonaws.mobile.auth.core.IdentityManager;
             import android.app.Application


             /**
              * Application class responsible for initializing singletons and other
              * common components.
              */
             class ApplicationWrapper : Application() {
               companion object {
                 private val TAG = this::class.java.simpleName
               }

               override fun onCreate() {
                 super.onCreate()
                 initializeAWSSDK()
               }

               private fun initializeAWSSDK() {
                 val config = AWSConfiguration(applicationContext)

                 if (IdentityManager.defaultIdentityManager == null) {
                   IdentityManager.defaultIdentityManager =
                        IdentityManager(applicationContext, config)
                 }
               }
             }

      #. Create a :code:`SplashActivity` class or modify your existing splash activity.

         #. To create the activity, right click on the :file:`java` folder in your Xcode project
            explorer, and then choose :guilabel:`File > New > Activity > Basic Activity`.


            .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
               :scale: 100
               :alt: Image of the Download Configuration Files button in the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-xcode-add-splash-activity.png
                  :scale: 75

         #. Add the following code to the activity's :code:`onCreate` method to establish user
            credentials that enable access to AWS services whenever your app starts.

            .. code-block:: kotlin

                import com.amazonaws.mobile.config.AWSConfiguration;
                import com.amazonaws.mobile.auth.core.IdentityManager;
                import com.amazonaws.mobile.auth.core.StartupAuthResultHandler;
                import com.amazonaws.mobile.auth.core.StartupAuthResult;

                class SplashActivity : AppCompatActivity() {
                    override fun onCreate(savedInstanceState: Bundle?) {
                        super.onCreate(savedInstanceState);
                        setContentView(R.layout.activity_splash);

                        val config = AWSConfiguration(applicationContext)
                        val identityManager = IdentityManager(applicationContext, config)
                        IdentityManager.defaultIdentityManager = identityManager
                        identityManager.doStartupAuth(this) {
                            // User identity is ready
                            intent = Intent(this, :samp:`{MainActivity}`::class.java)
                                .setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)
                            startActivity(intent)
                            finish()
                        }
                    }
                }

      #. Modify your app manifest to add `Android permissions
         <https://developer.android.com/guide/topics/permissions/requesting.html>`_

         Delete the :code:`intent-filter` declarations for the :code:`MAIN` action and and
         :code:`LAUNCHER` category from your original start up activity. If there are no other
         declarations in the :code:`intent-filter`, then also delete the empty
         :code:`<intent-filter></intent-filter>` tags.

         .. code-block:: xml

             <uses-permission android:name="android.permission.INTERNET" />
             <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
             <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
              . . .
             <application
                 android:name="com.:samp:`{yourpackagename}`.Application">
              . . .
                <activity android:name=".SplashActivity" >
                    <intent-filter>
                        <action android:name="android.intent.action.MAIN" />
                        <category android:name="android.intent.category.LAUNCHER" />
                    </intent-filter>
                </activity>
                 <activity android:name=".MainActivity" >
                    <intent-filter>
                        <!--
                             * REMOVE THESE FROM YOUR START UP ACTIVITY

                                 <action android:name="android.intent.action.MAIN" />
                                 <category android:name="android.intent.category.LAUNCHER" />

                             *    IF THERE ARE NO OTHER ITEMS INSIDE THE intent-filter
                             *    TAGS, DELETE THE TAGS

                         -->
                    </intent-filter>
                </activity>

              . . .
             </application>

         :emphasis:`Make sure to remove the MAIN action and LAUNCHER category from your previous
         starting activity's :code:`intent-filter`.`

      #. Click the :guilabel:`Run` icon (the one that looks like a Play button) in Android Studio to
         build your app and run it on your device/emulator. After your app is deployed, search
         through your logcat for a message similar to :code:`"IdentityManager: Got user ID:
         us-east-1:abcabcabc-0be6-444e-b101-abcabcabc"`. If you see the log, your app is
         successfully connected to AWS services.

      Your app is now set up to interact with the AWS services you configured in your |AMH| project!

   iOS - Swift
      #. `Install Xcode <https://developer.apple.com/download/>`_ version 8.0 or later.

      #. Install Cocoapods

         From a terminal window run:

         .. code-block:: none

             sudo gem install cocoapods

      #. Open your app project in Xcode

      #. Create podfile

         From a terminal window, navigate to the directory that contains your project's
         :file:`.xcodeproj` file and run: :code:`pod init`.

         From the same directory, open the :file:`Podfile` this command creates in a text editor.

      #. Add core AWS Mobile SDK components to your build.

         Add the following to build core AWS Mobile service APIs, such as user sign-in, into your
         app.

         .. note:: For :code:`{AWSMobileApp}`, substitute the name of your own app.

         .. code-block:: none

             platform :ios, '9.0'

             target :':samp:`{AWSMobileApp}`' do
               use_frameworks!

                  pod 'AWSAuthCore', '~> 2.6.1'
                  # other pods

             end

      #. From the directory containing the podfile you created in step 4, run the following command
         to fetch and install the dependencies:

         .. code-block:: none

             pod install --repo-update

         After this is done, close your Xcode project and do not use it again. Instead, use the
         :file:`.xcworkspace` file generated by cocoapods for all further development.

      #. Add import statements

         In each scope where you call AWS services, add the following import statements to make core
         AWS Mobile service APIs available to your app.

         .. code-block:: none

             import AWSAuthCore

      #. Add the backend service configuration file to your app.

         From the location where your |AMH| configuration file was downloaded in a previous step,
         drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file
         in your Xcode project.

         Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options
         dialog.

      #. Finally, put the following code in your app's :code:`AppDelegate`.

         .. code-block:: swift
            :emphasize-lines: 16, 26

             import UIKit
             import AWSAuthCore

             @UIApplicationMain

             class AppDelegate: UIResponder, UIApplicationDelegate {

                 // set up the initialized flag
                 var isInitialized = false


                 func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                     let didFinishLaunching = AWSSignInManager.sharedInstance().interceptApplication(
                             application, didFinishLaunchingWithOptions: launchOptions)

                     if (!isInitialized) {
                         AWSSignInManager.sharedInstance().resumeSession(completionHandler: {
                             (result: Any?, error: Error?) in
                             print("Result: \(result) \n Error:\(error)")
                         })
                         isInitialized = true
                     }
                     return didFinishLaunching
                 }

                 // . . .
             }

      #. Click the :guilabel:`Run` icon (the one that looks like a Play button) in the top left
         corner of the Xcode window or type :code:`Command-R` to build and run your app.

      Your app is now set up to interact with the AWS services you configured in your |AMH| project!


   JavaScript
      Use the following steps to add the AWS SDK to your JavaScript web app.

      #. Get the AWS SDK for Javascript

         To make the SDK available to your web app, include a link to the `latest SDK version
         <https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/>`_ placing the following script in
         the head element of your :code:`index.html`.

         .. code-block:: html

             <!DOCTYPE html>
             <html>
             <head>
                 <title>AWS SDK for JavaScript - Sample Application</title>

                 <script src="https://sdk.amazonaws.com/js/{aws-sdk-2.92.0.min.js}"></script>

             </head>
             <body>
              ...

      #. Setup your Web App to Use AWS Services

         Copy the :samp:`aws-config.js` file you downloaded into the same folder as your
         :samp:`index.html`.

      #. Get AWS Credentials for the User

         The following script can be added to :samp:`index.html` to pass the :code:`IdentityPoolId`
         value from :samp:`aws-config.js` to the Amazon Cognito service, which returns temporary
         unauthenticated credentials for the user.

         .. code-block:: javascript

             <script src="https://sdk.amazonaws.com/js/{aws-sdk-2.92.0.min.js}"></script>
             <script> src="aws-config.js"></script>
             <script>
                 function loadIdentity() {

                     console.log("Getting AWS credentials...");
                     var credentials = AWS.config.credentials;

                     credentials.get(function(err) {

                         if (err) {
                             console.log("Error: " + err);
                             document.getElementById("identityId").innerHTML = err.message;
                             return;
                         }

                         console.log("Amazon Cognito Identity ID: " + credentials.identityId);
                         document.getElementById("identityId").innerHTML = "Amazon Cognito Identity ID: " + credentials.identityId;
                     });
                 }
             </script>

      #. Your app is now ready to call other AWS services using the SDK. Read the
         following for more depth, or skip down to :ref:`add-aws-mobile-sdk-next-steps`.

         More information: What did we just do?

         The :samp:`aws-config.js` you downloaded contains identifiers and endpoints that bind
         requests to the AWS services being called. This file is automatically generated and the
         copy in your bucket may be overwritten by Mobile Hub. Remember to get a fresh copy any time
         you alter the configuration of your |AMH| project.

         To access AWS resources, the user needs an identity that AWS recognizes. The following
         fragment shows how :samp:`aws-config.js` establishes AWS credentials by calling the
         :code:`AWS.CognitoIdentityCredentials` method using the :code:`IdentityPoolId` of your
         |AMH| project's AWS.

         .. code-block:: javascript

             // Fragment from aws-config.js generated by Mobile Hub
             AWS.config.region = "us-east-1";
             AWS.config.credentials = new AWS.CognitoIdentityCredentials({
                 IdentityPoolId: ":samp:`{us-east-1:ab01cd34ef-56ab-cd78-90ef-abc123def456}`"
                 });
             AWS.config.update({customUserAgent: 'MobileHub v0.1'});

         :samp:`Index.html` typically includes JavaScript which calls methods to instantiate AWS
         region and credentials objects and to set the user agent string. These are needed when
         accessing AWS services from your web app.

         **Identity Management Details**

         :code:`IdentityPoolId` in the preceding script, is the identifier of the |COG| collection
         of AWS user identities that |AMH| configured for your web app. User pools typically have an
         authenticated role, for users who sign in, and an unauthenticated role for those who don't.
         You can attach an |IAM| policy to each of these roles that grants access to other AWS
         services you have configured to suit your app design and security requirements.

         The preceding fragment shows how :code:`aws-config.js` acquire unauthenticated credentials.
         The AWS SDK for JavaScript also supports authentication by federating sign-in from a range
         of identity providers like Facebook, Google and Active Directory (ADFS), or an AWS-powered
         identity provider you create.

         For more information about |COG|, see `Getting Started <getting-started.html>`_ in the
         :emphasis:`Amazon Cognito Developer Guide`.

         For more information about using the SDK to enable user authentication, see `Using the
         JavaScript SDK <using-amazon-cognito-user-identity-pools-javascript-examples.html>`_.



.. _add-aws-mobile-sdk-next-steps:

Next Steps
==========


.. container:: option

   Android - Java
      :emphasis:`Add other Mobile Hub backend features`


      * :ref:`Add Analytics <add-aws-mobile-analytics-app>`

      * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

      * :ref:`Add Push Notification <add-aws-mobile-push-notifications-app>`

      * :ref:`Add NoSQL Database <add-aws-mobile-nosql-database-app>`

      * :ref:`Add User Data Storage <add-aws-mobile-user-data-storage-app>`

      * :ref:`Add Cloud logic <add-aws-mobile-cloud-logic-app>`

      * :ref:`Add Messaging <add-aws-mobile-messaging>`

      * :ref:`Add Conversational Bots <add-aws-mobile-conversational-bots-app>`

      * :ref:`Add Hosting and Sreaming <add-aws-mobile-hosting-and-streaming-app>`

      * :ref:`Upgrade to the New SDK <aws-mobile-sdk-migrate>`


   iOS - Swift
      :emphasis:`Add other Mobile Hub backend features`


      * :ref:`Add Analytics <add-aws-mobile-analytics-app>`

      * :ref:`Add User Sign-in <add-aws-mobile-user-sign-in>`

      * :ref:`Add Push Notification <add-aws-mobile-push-notifications-app>`

      * :ref:`Add NoSQL Database <add-aws-mobile-nosql-database-app>`

      * :ref:`Add User Data Storage <add-aws-mobile-user-data-storage-app>`

      * :ref:`Add Cloud logic <add-aws-mobile-cloud-logic-app>`

      * :ref:`Add Messaging <add-aws-mobile-messaging>`

      * :ref:`Add Conversational Bots <add-aws-mobile-conversational-bots-app>`

      * :ref:`Add Hosting and Sreaming <add-aws-mobile-hosting-and-streaming-app>`

      * :ref:`Upgrade to the New SDK <aws-mobile-sdk-migrate>`


   JavaScript
      * :ref:`Hosting Your Web App with Mobile Hub <add-aws-mobile-hosting-and-streaming-app>`

      * :ref:`Overview of the Hosting and Streaming Sample App
        <add-aws-mobile-hosting-and-streaming-back-end-setup>`




