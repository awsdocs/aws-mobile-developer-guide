
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

#. Use the CLI to add analytics to your cloud-enabled back-end and app.

    .. container:: option

       Android - Java
           In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

          .. code-block:: bash

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify add analytics

       Android - Kotlin
           In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

          .. code-block:: bash

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify add analytics

       iOS - Swift
           In a terminal window, navigate to your project folder (the folder contains your app :file:`.xcodeproj` file), and add the SDK to your app.

          .. code-block:: bash

              $ cd ./YOUR_PROJECT_FOLDER
              $ amplify add analytics

#. When configuration for analytics is complete, you will see a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

   .. code-block:: bash

       $ amplify status
      | Category  | Resource name   | Operation | Provider plugin   |
      | --------- | --------------- | --------- | ----------------- |
      | Auth      | cognitoabcd0123 | Create    | awscloudformation |
      | Analytics | yourprojectname | Create    | awscloudformation |

#. To create your backend AWS resources run:

     .. code-block:: bash

        $ amplify push


.. _add-aws-mobile-analytics-app:

Connect to Your Backend
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

            #. Add calls to capture session starts and stops. A session is one use of an app by the user. A session begins when an app is launched (or brought to the foreground), and ends when the app is terminated (or goes to the background). To accommodate for brief interruptions, like a text message, an inactivity period of up to 5 seconds is not counted as a new session. :guilabel: `Total daily sessions` shows the number of sessions your app has each day. :guilabel: `Average sessions per daily active user` shows the mean number of sessions per user per day.

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
                          private static final String TAG = MainActivity.class.getSimpleName();

                          public static PinpointManager pinpointManager;

                          @Override
                          protected void onCreate(Bundle savedInstanceState) {
                              super.onCreate(savedInstanceState);
                              setContentView(R.layout.activity_main);

                              // Initialize the AWS Mobile Client
                              AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {
                                  @Override
                                  public void onComplete(AWSStartupResult awsStartupResult) {
                                      Log.d(TAG, "AWSMobileClient is instantiated and you are connected to AWS!");
                                  }
                              }).execute();

                              PinpointConfiguration config = new PinpointConfiguration(
                                      MainActivity.this,
                                      AWSMobileClient.getInstance().getCredentialsProvider(),
                                      AWSMobileClient.getInstance().getConfiguration()
                              );
                              pinpointManager = new PinpointManager(config);
                              pinpointManager.getSessionClient().startSession();
                          }
                      }

               To stop the session, use :code:`stopSession()` and :code:`submitEvents()` at the last point in the session you want to capture. In this example, we are using a single Activity, so the session will stop when the MainActivity is destroyed. :code:`onDestroy()` is usually called when the back button is pressed while in the activity.

               .. code-block:: java

                  @Override
                  protected void onDestroy() {
                      super.onDestroy();

                      pinpointManager.getSessionClient().stopSession();
                      pinpointManager.getAnalyticsClient().submitEvents();
                  }

         Android - Kotlin
            #. Set up AWS Mobile SDK components as follows.

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

            #. Add calls to capture session starts and stops. A session is one use of an app by the user. A session begins when an app is launched (or brought to the foreground), and ends when the app is terminated (or goes to the background). To accommodate for brief interruptions, like a text message, an inactivity period of up to 5 seconds is not counted as a new session. Total daily sessions shows the number of sessions your app has each day. Average sessions per daily active user shows the mean number of sessions per user per day.

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
                                private val TAG = MainActivity.javaClass.simpleName
                                var pinpointManager: PinpointManager? = null
                            }

                            override fun onCreate(savedInstanceState: Bundle?) {
                                super.onCreate(savedInstanceState)
                                setContentView(R.layout.activity_main)

                                // Initialize the AWS Mobile client
                                AWSMobileClient.getInstance().initialize(this) { Log.d(TAG, "AWSMobileClient is instantiated and you are connected to AWS!") }.execute()

                                val config = PinpointConfiguration(
                                        this@MainActivity,
                                        AWSMobileClient.getInstance().credentialsProvider,
                                        AWSMobileClient.getInstance().configuration
                                )

                                pinpointManager = PinpointManager(config)
                                pinpointManager?.sessionClient?.startSession()
                            }
                        }

               To stop the session, use :code:`stopSession()` and :code:`submitEvents()` at the last point in the session that you want to capture. In this example, we are using a single Activity, so the session will stop when the MainActivity is destroyed. :code:`onDestroy()` is usually called when the back button is pressed while in the activity.

               .. code-block:: kotlin

                  override fun onDestroy() {
                      super.onDestroy()

                      pinpointManager?.sessionClient?.stopSession()
                      pinpointManager?.analyticsClient?.submitEvents()
                  }

         iOS - Swift
            #. Set up AWS Mobile SDK components as follows.

               #. The :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

                  .. code-block:: none

                       platform :ios, '9.0'
                       target :'YourAppName' do
                         use_frameworks!

                           pod 'AWSPinpoint', '~> 2.6.13'
                           pod 'AWSMobileClient', '~> 2.6.13'

                           # other pods

                       end

                  Run :code:`pod install --repo-update` before you continue.

                  If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

               #. Classes that call Amazon Pinpoint APIs must use the following import statements:

                  .. code-block:: none

                       /** start code copy **/
                       import AWSCore
                       import AWSPinpoint
                       import AWSMobileClient
                       /** end code copy **/

               #. Replace the return statement with following code into the :code:`application(_:didFinishLaunchingWithOptions:)` method of your app's :file:`AppDelegate.swift`.

                  .. code-block:: swift

                       class AppDelegate: UIResponder, UIApplicationDelegate {

                           /** start code copy **/
                           var pinpoint: AWSPinpoint?
                           /** end code copy **/

                           func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
                           [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                                //. . .

                                // Initialize Pinpoint
                                /** start code copy **/
                                pinpoint = AWSPinpoint(configuration:
                                    AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: launchOptions))

                                // Create AWSMobileClient to connect with AWS
                                return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)
                                /** end code copy **/
                           }
                       }

Monitor Analytics
-----------------

Build and run your app to see usage metrics in Amazon Pinpoint. By running the previous code samples, the console will show a "Session" logged.

#. To see visualizations of the analytics coming from your app, open your project in the Amazon Pinpoint console by running:

   .. code-block:: none

      $ amplify console analytics

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

                /**
                 * Call this method to log a custom event to the analytics client.
                 */
                 public void logEvent() {
                     final AnalyticsEvent event =
                         pinpointManager.getAnalyticsClient().createEvent("EventName")
                             .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                             .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                             .withMetric("DemoMetric1", Math.random());

                     pinpointManager.getAnalyticsClient().recordEvent(event);
                 }

       Android - Kotlin
          .. code-block:: kotlin

                import com.amazonaws.mobileconnectors.pinpoint.analytics.AnalyticsEvent;

                /**
                 * Call this method to log a custom event to the analytics client.
                 */
                fun logEvent() {
                    pinpointManager?.analyticsClient?.let {
                        val event = it.createEvent("EventName")
                            .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                            .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                            .withMetric("DemoMetric1", Math.random());
                        it.recordEvent(event)
                }

       iOS - Swift
          .. code-block:: swift

             // You can add this function in desired part of your app. It will be used to log events to the backend.
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

              /**
               * Call this method to log a monetized event to the analytics client.
               */
               public void logMonetizationEvent() {
                   final AnalyticsEvent event =
                       AmazonMonetizationEventBuilder.create(pinpointManager.getAnalyticsClient())
                           .withCurrency("USD")
                           .withItemPrice(10.00)
                           .withProductId("DEMO_PRODUCT_ID")
                           .withQuantity(1.0)
                           .withProductId("DEMO_TRANSACTION_ID").build();

                   pinpointManager.getAnalyticsClient().recordEvent(event);
               }

         Android - Kotlin
            .. code-block:: kotlin

                import com.amazonaws.mobileconnectors.pinpoint.analytics.monetization.AmazonMonetizationEventBuilder

                /**
                 * Call this method to log a monetized event to the analytics client.
                 */
                fun logMonetizationEvent() {
                    pinpointManager?.analyticsClient?.let {
                        val event = AmazonMonetizationEventBuilder.create(it)
                                .withCurrency("USD")
                                .withItemPrice(10.00)
                                .withProductId("DEMO_PRODUCT_ID")
                                .withQuantity(1.0)
                                .withProductId("DEMO_TRANSACTION_ID").build();
                        it.recordEvent(event)
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



