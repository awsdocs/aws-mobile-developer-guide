
.. _mobile-hub-add-aws-mobile-analytics:

#####################################################
Add Analytics to your Mobile App with Amazon Pinpoint
#####################################################


.. meta::
    :description:
        Use |AMH| Messaging and Analytics to Add Analytics to your Mobile App

.. important::

   The following content applies if you are already using the AWS Mobile Hub to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

.. _overview:

Overview
=========

Gather the data that helps improve your app's usability, monetization, and engagement with your
users. |AMH| deploys your analytics backend when you enable the :ref:`Messaging and Analytics <messaging-and-analytics>` feature, which uses the `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__ service.

.. _setup-your-backend:

Set up your Backend
===================
#. Complete the :ref:`Get Started <mobile-hub-getting-started>` steps before your proceed.

#. When you create a project, we enable analytics by default in your backend. You should see a green check mark  present on the :guilabel:`Analytics` tile in your backend, indicating that the feature is enabled. If the check mark is absent, choose :guilabel:`Analytics`, and then choose :guilabel:`Enable`.

  .. image:: images/project-detail-analytics.png
     :scale: 25

.. _mobile-hub-add-aws-mobile-analytics-app:

Connect to your Backend
=======================

Use the following steps to add analytics to your mobile app and monitor the results through Amazon Pinpoint.

Add Analytics
-------------

   .. container:: option

         Android - Java
            #. Set up AWS Mobile SDK components as follows.

               #. Include the following libraries in your :file:`app/build.gradle` dependencies list.

                  .. code-block:: java

                     dependencies{
                        implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.7.+'
                        implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                        // other dependencies . . .
                     }

                  * :code:`aws-android-sdk-pinpoint` library enables sending analytics to Amazon Pinpoint.
                  * :code:`aws-android-sdk-mobile-client` library gives access to the AWS credentials provider and configurations.

               #. Add required permissions to your app manifest.

                  The AWS Mobile SDK required the :code:`INTERNET` and :code:`ACCESS_NETWORK_STATE` permissions.  These are defined in the :code:`AndroidManifest.xml` file.

                  .. code-block:: xml

                     <uses-permission android:name="android.permission.INTERNET"/>
                     <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

            #. Add calls to capture session starts and stops.

               Three typical places to instrument your app session start and stop are:

               * Start a session in the :code:`Application.onCreate()` method.

               * Start a session in the :code:`onCreate()` method of the app's first activity.

               * Start and/or stop a session in the `ActivityLifecycleCallbacks <https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>`__ class.

               The following example shows starting a session in the :code:`OnCreate` event of :code:`MainActivity`.

                  .. code-block:: java

                      import android.support.v7.app.AppCompatActivity;
                      import android.os.Bundle;

                      import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
                      import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
                      import com.amazonaws.mobile.client.AWSMobileClient;

                      public class MainActivity extends AppCompatActivity {

                          public static PinpointManager pinpointManager;

                          @Override
                          protected void onCreate(Bundle savedInstanceState) {
                              super.onCreate(savedInstanceState);
                              setContentView(R.layout.activity_main);

                              // Initialize the AWS Mobile Client
                              AWSMobileClient.getInstance().initialize(this).execute();

                              PinpointConfiguration config = new PinpointConfiguration(
                                      MainActivity.this,
                                      AWSMobileClient.getInstance().getCredentialsProvider(),
                                      AWSMobileClient.getInstance().getConfiguration()
                              );
                              pinpointManager = new PinpointManager(config);
                              pinpointManager.getSessionClient().startSession();
                              pinpointManager.getAnalyticsClient().submitEvents();
                          }
                      }

               To stop the session, use :code:`stopSession()` and :code:`submitEvents()` at the last point in the session you want to capture.

               .. code-block:: java

                  // . . .

                  pinpointManager.getSessionClient().stopSession();
                  pinpointManager.getAnalyticsClient().submitEvents();

                  // . . .

         Android - Kotlin
            #. Set up AWS Mobile SDK components as follows.

               #. Include the following libraries in your :file:`app/build.gradle` dependencies list.

                  .. code-block:: java

                     dependencies {
                        implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.7.+'
                        implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                        // other dependencies . . .
                     }

                  * :code:`aws-android-sdk-pinpoint` library enables sending analytics to Amazon Pinpoint.
                  * :code:`aws-android-sdk-mobile-client` library gives access to the AWS credentials provider and configurations.

               #. Add required permissions to your app manifest.

                  The AWS Mobile SDK required the :code:`INTERNET` and :code:`ACCESS_NETWORK_STATE` permissions.  These are defined in the :code:`AndroidManifest.xml` file.

                  .. code-block:: xml

                     <uses-permission android:name="android.permission.INTERNET"/>
                     <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

            #. Add calls to capture session starts and stops.

               Three typical places to instrument your app session start and stop are:

               * Start a session in the :code:`Application.onCreate()` method.

               * Start a session in the :code:`onCreate()` method of the app's first activity.

               * Start and/or stop a session in the `ActivityLifecycleCallbacks <https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>`__ class.

               The following example shows starting a session in the :code:`OnCreate` event of :code:`MainActivity`.

                  .. code-block:: kotlin

                        import android.support.v7.app.AppCompatActivity;
                        import android.os.Bundle;
                        import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
                        import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
                        import com.amazonaws.mobile.client.AWSMobileClient;

                        class MainActivity : AppCompatActivity() {
                            companion object {
                                var pinpointManager: PinpointManager? = null
                            }

                            override fun onCreate(savedInstanceState: Bundle?) {
                                super.onCreate(savedInstanceState)
                                setContentView(R.layout.activity_main)

                                // Initialize the AWS Mobile client
                                AWSMobileClient.getInstance().initialize(this).execute()

                                with (AWSMobileClient.getInstance()) {
                                    val config = PinpointConfiguration(this, credentialsProvider, configuration)
                                    pinpointManager = PinpointManager(config)
                                }

                                pinpointManager?.sessionClient?.startSession()
                                pinpointManager?.analyticsClient?.submitEvents()
                            }
                        }

               To stop the session, use :code:`stopSession()` and :code:`submitEvents()` at the last point in the session you want to capture.

               .. code-block:: java

                  // . . .

                  pinpointManager?.sessionClient?.stopSession();
                  pinpointManager?.analyticsClient?.submitEvents();

                  // . . .

         iOS - Swift
               #. Set up AWS Mobile SDK components as follows.

               #. The :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

                  .. code-block:: none

                       platform :ios, '9.0'
                       target :'YourAppName' do
                         use_frameworks!

                           pod 'AWSPinpoint', '~> 2.6.13'

                           # other pods

                       end

                  Run :code:`pod install --repo-update` before you continue.

                  If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

               #. Classes that call Amazon Pinpoint APIs must use the following import statements:

                  .. code-block:: none

                       import AWSCore
                       import AWSPinpoint

               #. Insert the following code into the :code:`application(_:didFinishLaunchingWithOptions:)` method of your app's :file:`AppDelegate.swift`.

                  .. code-block:: swift

                       class AppDelegate: UIResponder, UIApplicationDelegate {

                           var pinpoint: AWSPinpoint?

                           func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
                           [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                           //. . .

                           // Initialize Pinpoint
                           pinpoint = AWSPinpoint(configuration:
                                   AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: launchOptions))

                           //. . .
                           }
                       }

Monitor Analytics
-----------------

Build and run your app to see usage metrics in Amazon Pinpoint.

#. To see visualizations of the analytics coming from your app, open your project in the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`__.

#. Choose :guilabel:`Analytics` on the upper right to open the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__.

  .. image:: images/analytics-link-mhconsole.png
     :alt: |AMH| console link to your project in the Amazon Pinpoint console.

#. Choose :guilabel:`Analytics` from the icons on the left of the console, and view the graphs of your app's usage. It may take up to 15 minutes for metrics to become visible.

  .. image:: images/getting-started-analytics.png

  `Learn more about Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

.. _mobile-hub-add-aws-mobile-analytics-enable-custom-data:

Enable Custom App Analytics
===========================

Instrument your code to capture app usage event information, including attributes you define.  Use graphs of your custom usage event data  in the Amazon Pinpoint console. Visualize how your users' behavior aligns with a model you design using `Amazon Pinpoint Funnel Analytics <https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-funnels.html>`__, or use `stream the data <https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-streaming.html>`__ for deeper analysis.

Use the following steps to implement Amazon Pinpoint custom analytics for your app.

   .. container:: option

       Android - Java
          .. code-block:: java

                 import com.amazonaws.mobileconnectors.pinpoint.analytics.AnalyticsEvent;

                 public void logEvent() {
                     final AnalyticsEvent event =
                         pinpointManager.getAnalyticsClient().createEvent("EventName")
                             .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                             .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                             .withMetric("DemoMetric1", Math.random());

                     pinpointManager.getAnalyticsClient().recordEvent(event);
                     pinpointManager.getAnalyticsClient().submitEvents();
                 }

       Android - Kotlin
          .. code-block:: kotlin

                import com.amazonaws.mobileconnectors.pinpoint.analytics.AnalyticsEvent;

                fun logEvent() {
                    pintpointManager?.analyticsClient?.let {
                        val event = it.createEvent("EventName")
                            .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                            .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                            .withMetric("DemoMetric1", Math.random());
                        it.recordEvent(event)
                        it.submitEvents()
                }

       iOS - Swift
          .. code-block:: swift

             func logEvent() {

                 let pinpointAnalyticsClient =
                     AWSPinpoint(configuration:
                         AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: nil)).analyticsClient

                 let event = pinpointAnalyticsClient.createEvent(withEventType: "EventName")
                 event.addAttribute("DemoAttributeValue1", forKey: "DemoAttribute1")
                 event.addAttribute("DemoAttributeValue2", forKey: "DemoAttribute2")
                 event.addMetric(NSNumber.init(value: arc4random() % 65535), forKey: "EventName")
                 pinpointAnalyticsClient.record(event)
                 pinpointAnalyticsClient.submitEvents()

             }

Build, run, and try your app, and then view your custom events in the :guilabel:`Events` tab of the Amazon Pinpoint console (use your |AMH| project / :guilabel:`Analytics` > Amazon Pinpoint console / :guilabel:`Analytics` > :guilabel:`Events`). Look for the name of your event in the :guilabel:`Events` dropdown menu.

.. _mobile-hub-add-aws-mobile-analytics-enable-revenue-data:

Enable Revenue Analytics
------------------------

Amazon Pinpoint supports the collection of monetization event data. Use the following steps to place
and design analytics related to purchases through your app.

   .. container:: option

         Android - Java
            .. code-block:: java

               import com.amazonaws.mobileconnectors.pinpoint.analytics.monetization.AmazonMonetizationEventBuilder;

               public void logMonetizationEvent() {
                   final AnalyticsEvent event =
                       AmazonMonetizationEventBuilder.create(pinpointManager.getAnalyticsClient())
                           .withFormattedItemPrice("$10.00")
                           .withProductId("DEMO_PRODUCT_ID")
                           .withQuantity(1.0)
                           .withProductId("DEMO_TRANSACTION_ID").build();

                   pinpointManager.getAnalyticsClient().recordEvent(event);
                   pinpointManager.getAnalyticsClient().submitEvents();
               }

         Android - Kotlin
            .. code-block:: kotlin

                import com.amazonaws.mobileconnectors.pinpoint.analytics.monetization.AmazonMonetizationEventBuilder;

                public void logMonetizationEvent() {
                    pinpointManager?.analyticsClient?.let {
                        val event = AmazonMonetizationEventBuilder.create(it)
                           .withFormattedItemPrice("$10.00")
                           .withProductId("DEMO_PRODUCT_ID")
                           .withQuantity(1.0)
                           .withProductId("DEMO_TRANSACTION_ID").build();
                        it.recordEvent(event)
                        it.submitEvents()
                    }
                }

         iOS - Swift
            .. code-block:: swift

                  func sendMonetizationEvent()
                   {
                       let pinpointClient = AWSPinpoint(configuration:
                           AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: nil))

                       let pinpointAnalyticsClient = pinpointClient.analyticsClient

                       let event =
                           pinpointAnalyticsClient.createVirtualMonetizationEvent(withProductId:
                               "DEMO_PRODUCT_ID", withItemPrice: 1.00, withQuantity: 1, withCurrency: "USD")
                       pinpointAnalyticsClient.record(event)
                       pinpointAnalyticsClient.submitEvents()
                   }



