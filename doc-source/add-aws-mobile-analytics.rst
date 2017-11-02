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

3. Complete the :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps before using the integration steps on this page.

#. Use |AMHlong| to deploy your backend in minutes.

   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create project`.

        Or select an existing project.

   #. Choose the :guilabel:`Messaging and Analytics` tile.

      .. list-table::
         :widths: 1

         * - :emphasis:`Curious about why push notifications, messaging, and analytics are grouped into one Mobile Hub feature? See the` `Amazon Pinpoint User Guide <http://docs.aws.amazon.com/pinpoint/latest/userguide/>`_.

   #. If a green check mark is present on the :guilabel:`Analytics` option button, then the feature is enabled. If not, choose :guilabel:`Analytics`, and then choose :guilabel:`Enable`.

   #. Download your Mobile Hub project configuration file.

      #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

      #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 100 %
            :alt: Image of the Mobile Hub console when choosing Download Configuration File.

         *Remember:*

         Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use updated files for those features.

.. _add-aws-mobile-analytics-app:

Add the SDK to Your App
=======================

#. Use the following steps to add analytics to your mobile app through AWS Pinpoint.

   .. container:: option

         Android - Java
            #. Set up AWS Mobile SDK components with the following :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` steps.

               #. :file:`AndroidManifest.xml` must contain:

                  .. code-block:: xml
                     :emphasize-lines: 1,2,3

                     <uses-permission android:name="android.permission.INTERNET" />
                     <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
                     <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

               #. :file:`app/build.gradle` must contain:

                  .. code-block:: java
                     :emphasize-lines: 2,3

                     dependencies{
                        compile 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                        compile ('com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar') {transitive = true;}
                     }

            #. Add the backend service configuration file to your app.

               #. Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown menu.

                  .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                     :scale: 100
                     :alt: Image of the Download Configuration Files button in the |AMH| console.

                  .. only:: pdf

                     .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                        :scale: 50

                  .. only:: kindle

                     .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                        :scale: 75

               #. From the location where configuration files were downloaded in a previous step, drag :file:`awsconfiguration.json` into the :file:`res/raw` folder.

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

               #. Add the following to the dependencies section of :file`app/build.gradle`:

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

               #. Add the following to :file:`Application.java`:

                  .. code-block:: java
                     :emphasize-lines: 2-8,15,27,30-36, 40-55

                       //. . .
                       import android.support.multidex.MultiDexApplication;
                       import android.util.Log;
                       import com.amazonaws.auth.AWSCredentialsProvider;
                       import com.amazonaws.mobile.config.AWSConfiguration;
                       import com.amazonaws.mobile.auth.core.IdentityManager;
                       import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
                       import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
                       //. . .


                       public class Application extends MultiDexApplication {
                           private static final String LOG_TAG = Application.class.getSimpleName();

                            public static PinpointManager pinpointManager;

                           @Override
                           public void onCreate() {

                               super.onCreate();
                               initializeApplication();
                               // Application initialized
                           }

                           private void initializeApplication() {

                               AWSConfiguration awsConfig = new AWSConfiguration(getApplicationContext());

                              // If IdentityManager is not created, create it
                              if (IdentityManager.getDefaultIdentityManager() == null) {
                                      AWSConfiguration awsConfiguration =
                                           new AWSConfiguration(getApplicationContext());
                                      IdentityManager identityManager =
                                           new IdentityManager(getApplicationContext(), awsConfiguration);
                                      IdentityManager.setDefaultIdentityManager(identityManager);
                                  }

                               // Register identity providers here.
                               // With none registered IdentityManager gets unauthenticated &AWS; credentials

                                final AWSCredentialsProvider credentialsProvider =
                                       IdentityManager.getDefaultIdentityManager().getCredentialsProvider();

                                PinpointConfiguration pinpointConfig = new PinpointConfiguration(
                                   getApplicationContext(),
                                   credentialsProvider,
                                   awsConfig);

                               Application.pinpointManager = new PinpointManager(pinpointConfig);

                               pinpointManager.getSessionClient().startSession();

                               // <replaceable>Choose a meaningful point in your apps lifecycle to mark the end of your session</replaceable>
                               // pinpointManager.getSessionClient().stopSession();
                               // pinpointManager.getAnalyticsClient().submitEvents();

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

                           pod 'AWSPinpoint', '~> 2.6.5'

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
                           [UIApplicationLaunchOptionsKey: Any]?) -&gt; Bool {

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
               :emphasize-lines: 1-22

                   import com.amazonaws.mobileconnectors.pinpoint.analytics.AnalyticsEvent;
                       // . . .
                       // Initialize the floating action button
                       FloatingActionButton addNoteButton = (FloatingActionButton) findViewById(R.id.addNoteButton);
                       addNoteButton.setOnClickListener(new View.OnClickListener() {
                           @Override
                           public void onClick(View view) {
                            // . . .

                       pinpointManager.getSessionClient().startSession();
                           final AnalyticsEvent event =
                              pinpointManager.getAnalyticsClient().createEvent("AddNewNoteClick")
                               .withAttribute("DemoAttribute1", "DemoAttributeValue1")
                               .withAttribute("DemoAttribute2", "DemoAttributeValue2")
                               .withMetric("DemoMetric1", Math.random());

                           pinpointManager.getAnalyticsClient().recordEvent(event);
                           pinpointManager.getSessionClient().stopSession();
                           pinpointManager.getAnalyticsClient().submitEvents();
                           // . . .

                       }
                   });


         iOS - Swift
            .. code-block:: swift
               :emphasize-lines: 9-19

               func applicationDidEnterBackground(_ application: UIApplication) {
                   // Use this method to release shared resources, save user data, invalidate timers,
                   // and store enough application state information to restore your application to its
                   // current state in case it is terminated later.

                   // If your application supports background execution, this method is called instead
                   // of applicationWillTerminate: when the user quits.

                   let pinpointAnalyticsClient =
                       AWSPinpoint(configuration:
                           AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: nil)).analyticsClient

                   let event = pinpointAnalyticsClient.createEvent(withEventType: "EnteredBackGround")
                   event.addAttribute("DemoAttributeValue1", forKey: "DemoAttribute1")
                   event.addAttribute("DemoAttributeValue2", forKey: "DemoAttribute2")
                   event.addMetric(NSNumber.init(value: arc4random() % 65535), forKey: "EnteredBackGround")
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
               :emphasize-lines: 1,12-22

               import com.amazonaws.mobileconnectors.pinpoint.analytics.monetization.AmazonMonetizationEventBuilder;
               // . . .
               /**
                * Purchase something.
                * @param buyItem
               void buyNow(final BuyItem buyItem) {

                   // . . .

                   // This creates an Amazon monetization event.

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

               import UIKit
               class ViewController: UIViewController {

                   // . . .

                   func sendMonetizationEvent(productID: String)
                   {
                       let pinpointClient = AWSPinpoint(configuration:
                           AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: nil))

                       let pinpointAnalyticsClient = pinpointClient.analyticsClient

                       let event =
                           pinpointAnalyticsClient.createVirtualMonetizationEvent(withProductId:
                               productID, withItemPrice: 1.00, withQuantity: 1, withCurrency: "USD")
                       pinpointAnalyticsClient.record(event)
                       pinpointAnalyticsClient.submitEvents()
                   }

                   // . . .
               }



