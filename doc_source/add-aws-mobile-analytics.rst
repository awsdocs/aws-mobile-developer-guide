    .. _add-aws-mobile-analytics:

################################
Add Analytics to your Mobile App
################################


.. meta::
    :description:
        Use |AMH| Messaging and Analytics to Add Analytics to your Mobile App

.. _overview:

Overview
=========

Gather the data that helps improve your app's usability, monetization, and engagement with your
users. |AMH| deploys your analytics backend when you enable the :ref:`messaging-and-analytics`
feature, which uses the `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_ service.

.. _setup-your-backend:

Set up your Backend
===================
#. Complete the :ref:`Get Started <getting-started>` steps before your proceed.

#. When you create a project, we enable analytics by default in your backend. You should see a green check mark  present on the :guilabel:`Analytics` tile in your backend, indicating that the feature is enabled. If the check mark is absent, choose :guilabel:`Analytics`, and then choose :guilabel:`Enable`.

  .. image:: images/project-detail-analytics.png
     :scale: 25

.. _add-aws-mobile-analytics-app:

Connect to your Backend
=======================

Use the following steps to add analytics to your mobile app through AWS Pinpoint.

   .. container:: option

         Android - Java
            #. Set up AWS Mobile SDK components with the following :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps.

               #. :file:`app/build.gradle` must contain:

                  .. code-block:: java
                     :emphasize-lines: 2

                     dependencies{
                        compile 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                     }

            #. Instrument your app to provide basic session data for Amazon Pinpoint analytics. The Amazon Pinpoint SDK gives you full control of when your sessions are started and stopped. Your app must explicitly start and stop the sessions. The following example shows one way to handle this by instrumenting a public class that extends `MultidexApplication <https://developer.android.com/studio/build/multidex.html>`_. :code:`StartSession()` is called during the :code:`OnCreate` event.

               #. Add the following to :file:`app/build.gradle`:

                  .. code-block:: java
                     :emphasize-lines: 4

                       android {
                           defaultConfig {
                               ...
                               multiDexEnabled = true
                           }
                       }

               #. Add the following to the dependencies section of :file:`app/build.gradle`:

                  .. code-block:: none
                     :emphasize-lines: 1

                       compile 'com.android.support:multidex:1.0.+'

               #. Add the following to :file:`AndroidManifest.xml`:

                  .. code-block:: xml
                     :emphasize-lines: 3,4

                       <application
                       ..
                       android:theme="@style/AppTheme"
                       android:name="com.YourApplication.Application">
                       ..
                       </application>

               #. Add the following to your activity:

                  .. code-block:: java
                     :emphasize-lines: 2-3,8,15-27

                       //. . .
                       import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
                       import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
                       //. . .

                       public class MainActivity extends AppCompatActivity {

                          public static PinpointManager pinpointManager;

                           @Override
                           public void onCreate() {

                               super.onCreate();

                               PinpointConfiguration pinpointConfig = new PinpointConfiguration(
                                       getApplicationContext(),
                                       AWSMobileClient.getInstance().getCredentialsProvider(),
                                       AWSMobileClient.getInstance().getConfiguration());

                               pinpointManager = new PinpointManager(pinpointConfig);

                               // Start a session with Pinpoint
                               pinpointManager.getSessionClient().startSession();

                               // Stop the session and submit the default app started event
                               pinpointManager.getSessionClient().stopSession();
                               pinpointManager.getAnalyticsClient().submitEvents();
                           }

                       }


         iOS - Swift
            #. Set up AWS Mobile SDK components with the following :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps.

               #. The :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

                  .. code-block:: none
                     :emphasize-lines: 4

                       platform :ios, '9.0'
                       target :'YourAppName' do
                         use_frameworks!

                           pod 'AWSPinpoint', '~> 2.6.6'

                           # other pods

                       end

                  Run :code:`pod install --repo-update` before you continue.

               #. Classes that call Amazon Pinpoint APIs must use the following import statements:

                  .. code-block:: none
                     :emphasize-lines: 1,2

                       import AWSCore
                       import AWSPinpoint

               #. Insert the following code into the :code:`didFinishLaunchwithOptions` method of your app's :file:`AppDelegate.swift`.

                  .. code-block:: swift
                     :emphasize-lines: 3-12

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

Build and run your app to see usage metrics in Amazon Pinpoint.

#. To see visualizations of the analytics coming from your app, open your project in the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`_.

#. Choose :guilabel:`Analytics` on the upper right to open the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`_.

  .. image:: images/analytics-link-mhconsole.png
     :alt: |AMH| console link to your project in the Amazon Pinpoint console.

#. Choose :guilabel:`Analytics` from the icons on the left of the console, and view the graphs of your app's usage. It may take up to 15 minutes for metrics to become visible.

  .. image:: images/getting-started-analytics.png

  `Learn more about Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_.

.. _add-aws-mobile-analytics-enable-custom-data:

Enable Custom App Analytics
---------------------------

Instrument your code to capture app usage event information, including attributes you define.  Use graphs of your custom usage event data  in the Amazon Pinpoint console. Visualize how your users' behavior aligns with a model you design using `Amazon Pinpoint Funnel Analytics <analytics-funnels.html>`_, Or use `stream the data <analytics-streaming.html>`_ for deeper analysis.

Use the following steps to implement Amazon Pinpoint custom analytics for your app.

   .. container:: option

       Android - Java
          .. code-block:: java
             :emphasize-lines: 1-15

                 import com.amazonaws.mobileconnectors.pinpoint.analytics.AnalyticsEvent;

                 public void logEvent() {
                     pinpointManager.getSessionClient().startSession();
                     final AnalyticsEvent event =
                         pinpointManager.getAnalyticsClient().createEvent("EventName")
                             .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                             .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                             .withMetric("DemoMetric1", Math.random());

                     pinpointManager.getAnalyticsClient().recordEvent(event);
                     pinpointManager.getSessionClient().stopSession();
                     pinpointManager.getAnalyticsClient().submitEvents();
                 }

       iOS - Swift
          .. code-block:: swift
             :emphasize-lines: 9-19

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

.. _add-aws-mobile-analytics-enable-revenue-data:

Enable Revenue Analytics
------------------------

Amazon Pinpoint supports the collection of monetization event data. Use the following steps to place
and design analytics related to purchases through your app.

   .. container:: option

         Android - Java
            .. code-block:: java
               :emphasize-lines: 1-17

               import com.amazonaws.mobileconnectors.pinpoint.analytics.monetization.AmazonMonetizationEventBuilder;

               public void logMonetizationEvent() {
                   pinpointManager.getSessionClient().startSession();

                   final AnalyticsEvent event =
                       AmazonMonetizationEventBuilder.create(pinpointManager.getAnalyticsClient())
                           .withFormattedItemPrice("$10.00")
                           .withProductId("DEMO_PRODUCT_ID")
                           .withQuantity(1.0)
                           .withProductId("DEMO_TRANSACTION_ID").build();

                   pinpointManager.getAnalyticsClient().recordEvent(event);
                   pinpointManager.getSessionClient().stopSession();
                   pinpointManager.getAnalyticsClient().submitEvents();
               }

         iOS - Swift
            .. code-block:: swift
               :emphasize-lines: 1-12

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



