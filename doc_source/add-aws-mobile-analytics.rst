    .. _add-aws-mobile-analytics:

################################
Add Analytics to your Mobile App
################################


.. meta::
    :description:
        Use |AMH| Messaging and Analytics to Add Analytics to your Mobile App

.. _add-aws-mobile-analytics-overview:

Analytics
=========

Gather the data that helps improve your app's usability, monetization, and engagement with your
users. |AMH| deploys your analytics backend when you enable the :ref:`messaging-and-analytics`
feature, which uses the `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_ service.


.. _add-aws-mobile-analytics-backend-setup:

Set Up Your Backend
===================

#. Complete the :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps before using the integration steps on this page.

#. Use |AMHlong| to deploy your backend.

   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create project` or you can select a previously created project.

   #. Choose the :guilabel:`Messaging and Analytics` tile.

      .. list-table::
         :widths: 1

         * - :emphasis:`Curious about why push notifications, messaging, and analytics are grouped into one Mobile Hub feature? See the` `Amazon Pinpoint User Guide <http://docs.aws.amazon.com/pinpoint/latest/userguide/>`_.

   #. If a green check mark is present on the :guilabel:`Analytics` option button, then the feature is enabled. If not, choose :guilabel:`Analytics`, and then choose :guilabel:`Enable`.

   #. If you changed any settings in your |AMH| project then you need to download your Mobile Hub project configuration file and replace it in your project (see :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` for more information).

.. _add-aws-mobile-analytics-app:

Add the SDK to Your App
=======================

#. Use the following steps to add analytics to your mobile app through AWS Pinpoint.

   .. container:: option

         Android - Java
            #. Set up AWS Mobile SDK components with the following :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps.

               #. :file:`app/build.gradle` must contain:

                  .. code-block:: java
                     :emphasize-lines: 2

                     dependencies{
                        compile 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                     }

            #. Instrument your app to provide event data for Amazon Pinpoint analytics. The Amazon Pinpoint SDK gives you full control of when your sessions are started and stopped. Your app must explicitly start and stop the sessions.

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

            #. Add the backend service configuration file to your app.

               From the location where your |AMH| configuration file was downloaded in a previous step, drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file in your Xcode project.

               Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

#. Build and run your app to see usage metrics in Amazon Pinpoint.

   #. To see visualizations of the analytics coming from your app, open the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`_.

    #. Choose the name of the |AMH| project you created for your backend.

    #. Choose :guilabel:`Analytics` from the icons on the left of the console, and view the graphs of your app's usage. It may take up to 15 minutes for metrics to become visible.

       .. image:: images/getting-started-analytics.png

    `Learn more about Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_.

.. _add-aws-mobile-analytics-enable-custom-data:

Enable Custom App Analytics
===========================

Place analytics events and define their attributes in your code to capture app usage event information that you can use to drive app user experience and monetization improvements. The custom data you capture can be used for `Amazon Pinpoint Funnel Analytics <analytics-funnels.html>`_ or to `stream the data
<analytics-streaming.html>`_ for deeper analysis.

#. Use the following steps to implement Amazon Pinpoint custom analytics for your app.

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

#. Build, run, and try your app, and then `view the Events tab of the Amazon Pinpoint console
   <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/add-aws-mobile-analytics.html#pinpoint-testds>`_
   to see your custom metrics.

.. _add-aws-mobile-analytics-enable-revenue-data:

Enable Revenue Analytics
========================

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



