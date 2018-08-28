
    .. _add-aws-mobile-analytics:

#####################################################
Add Analytics to Your Mobile App with Amazon Pinpoint
#####################################################


.. meta::
    :description:
        Use |AMH| Messaging and Analytics to Add Analytics to your Mobile App

.. _overview:

Overview
=========

.. container:: option

   Android - Java
      .. _android-java:

      Gather the data that helps improve your app's usability, monetization, and engagement with your users. The CLI deploys your analytics backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

   Android - Kotlin
      .. _android-kotlin:

      Gather the data that helps improve your app's usability, monetization, and engagement with your users. The CLI deploys your analytics backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

   iOS - Swift
      .. _ios-swift:

      Gather the data that helps improve your app's usability, monetization, and engagement with your users. The CLI deploys your analytics backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

.. _setup-your-backend:

Set Up Your Backend
===================
#. Complete the :ref:`Get Started <getting-started>` steps before you proceed.

#. In a terminal window, navigate to the root of your app files, and then add the analytics category to your app. The CLI will prompt you for configuration parameters.

     .. code-block:: bash

        $ cd ./ROOT_OF_YOUR_APP_FILES
        $ amplify analytics add

#. When you complete configuration for analytics, you will see a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

   .. code-block:: bash

       $ amplify status
      | Category  | Resource name   | Operation | Provider plugin   |
      | --------- | --------------- | --------- | ----------------- |
      | Auth      | cognitoabcd0123 | Create    | awscloudformation |
      | Analytics | yourprojectname | Create    | awscloudformation |

#. To create your backend AWS resources run:

     .. code-block:: bash

        $ amplify push

#. Copy and save the URL labeled :code:`Pinpoint URL to track events:`. This link opens your app project in the Amazon Pinpoint console where you can monitor usage events in near real time.


   Use the steps in the next section to connect your app to your backend.


.. _add-aws-mobile-analytics-app:

Connect to Your Backend
=======================

Use the following steps to add analytics to your mobile app and monitor the results through Amazon Pinpoint.

Add Analytics
-------------

   .. container:: option

         Android - Java
            #. Set up AWS Mobile SDK components by following the :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps. These include:

               #. Include the following libraries in your :file:`app/build.gradle` dependencies list.

                  .. code-block:: java

                     dependencies{
                        implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                        implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
                        // other dependencies . . .
                     }

                  * :code:`aws-android-sdk-pinpoint` library enables sending analytics to Amazon Pinpoint.
                  * :code:`aws-android-sdk-mobile-client` library gives access to the AWS credentials provider and configurations.

               #. Add required permissions to your app manifest.

                  The AWS Mobile SDK requires the :code:`INTERNET` and :code:`ACCESS_NETWORK_STATE` permissions.  These are defined in the :code:`AndroidManifest.xml` file.

                  .. code-block:: xml

                     <uses-permission android:name="android.permission.INTERNET"/>
                     <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

            #. Add calls to capture session starts and stops.

               Three typical places to instrument your app session start and stop are:

               * Start a session in the :code:`Application.onCreate()` method.

               * Start a session in the :code:`onCreate()` method of the app's first activity.

               * Start or stop a session in the `ActivityLifecycleCallbacks <https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>`__ class.

               The following example shows how to start a session in the :code:`OnCreate` event of :code:`MainActivity`.

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
            #. Set up AWS Mobile SDK components by following the :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps. These include:

               #. Include the following libraries in your :file:`app/build.gradle` dependencies list.

                  .. code-block:: java

                     dependencies {
                        implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                        implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }
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

               * Start or stop a session in the `ActivityLifecycleCallbacks <https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>`__ class.

               The following example shows how to start a session in the :code:`OnCreate` event of :code:`MainActivity`.

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

               To stop the session, use :code:`stopSession()` and :code:`submitEvents()` at the last point in the session that you want to capture.

               .. code-block:: java

                  // . . .

                  pinpointManager?.sessionClient?.stopSession();
                  pinpointManager?.analyticsClient?.submitEvents();

                  // . . .

         iOS - Swift
            #. Set up AWS Mobile SDK components with the following :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps.

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

#. To see visualizations of the analytics coming from your app, open your project in the Amazon Pinpoint console by running:

   .. code-block:: none

      $ amplify analytics console

#. Choose :guilabel:`Analytics` from the icons on the left of the console, and view the graphs of your app's usage. It may take up to 15 minutes for metrics to become visible.

  .. image:: images/getting-started-analytics.png

  `Learn more about Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

.. _add-aws-mobile-analytics-enable-custom-data:

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

Build, run, and use your app. Then, view your custom events on the :guilabel:`Events` tab of the Amazon Pinpoint console (Amazon Pinpoint console / :guilabel:`Analytics` > :guilabel:`Events`). Look for the name of your event in the :guilabel:`Events` menu.

.. _add-aws-mobile-analytics-enable-revenue-data:

Enable Revenue Analytics
========================

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



