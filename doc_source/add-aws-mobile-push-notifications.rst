.. _add-aws-mobile-push-notifications:

#########################################
Add Push Notifications to Your Mobile App
#########################################


.. meta::
   :description: Integrate AWS Push Notifications into your mobile app.

.. _add-aws-mobile-push-notifications-overview:

Push Notifications
==================

|AMH| deploys your Push Notifications backend services when you enable the
:ref:`messaging-and-analytics` feature using the `Amazon Pinpoint service <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`_. Amazon Pinpoint enables apps to
receive mobile push messages sent from the Apple (APNs) and Google (FCM/GCM) platforms. You can also
create Amazon Pinpoint campaigns that tie user behavior to push or other forms of messaging.

.. _add-aws-push-notifications-backend-setup:

Set Up Your Backend
===================

#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the
   integration steps on this page.

#. Use |AMHlong| to deploy and configure your AWS services in minutes.


   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create
      project`.

      Or select an existing project.

   #. Choose the :guilabel:`Messaging and Analytics` tile

   #. Choose :guilabel:`Mobile push`.

      For Android - Firebase/Google Cloud Messaging (FCM/GCM):

            Choose :guilabel:`Android` and provide your Firebase/Google application API key and Sender ID. To retrieve or create these values, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`_ .

      For iOS - Apple Push Notification Service (APNs):

            Choose :guilabel:`iOS` and provide your Apple app P12 Certificate and, optionally, Certificate password. To retrieve or create these items, see `Setting Up iOS Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/apns-setup.html>`_.

   #. Download your updated |AMH| project configuration file and replace it in your project (see :ref:`Basic Backend Setup <add-aws-mobile-sdk-basic-setup>` for more information).  Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app.

.. _add-aws-mobile-push-notifications-app:

Add the SDK to Your App
=================================


**To add push notification to your app**

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml

                    <uses-permission android:name="android.permission.WAKE_LOCK"/>
                    <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
                    <permission android:name="com.mysampleapp.permission.C2D_MESSAGE"
                                android:protectionLevel="signature" />
                    <uses-permission android:name="com.mysampleapp.permission.C2D_MESSAGE" />

                    <application

                        <!--Add these to your Application declaration
                        to filter for the notification intent-->
                        <receiver
                            android:name="com.google.android.gms.gcm.GcmReceiver"
                            android:exported="true"
                            android:permission="com.google.android.c2dm.permission.SEND" >
                            <intent-filter>
                                <action android:name="com.google.android.c2dm.intent.RECEIVE" />
                                <category android:name="com.mysampleapp" />
                            </intent-filter>
                        </receiver>

                        <service
                            android:name=".PushListenerService"
                            android:exported="false" >
                            <intent-filter>
                                <action android:name="com.google.android.c2dm.intent.RECEIVE" />
                            </intent-filter>
                        </service>

                    </application>

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none
               :emphasize-lines: 0

                dependencies{
                    compile 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                    compile ('com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar')  {transitive = true;}

                    compile 'com.google.android.gms:play-services-iid:11.6.0'
                    compile 'com.google.android.gms:play-services-gcm:11.6.0'
                }

         #. Add the following to your project level :file:`build.gradle`:

            .. code-block:: none
               :emphasize-lines: 0

                buildscript {
                    dependencies {
                        classpath 'com.google.gms:google-services:3.1.1'
                    }
                }

                allprojects {
                    repositories {
                        maven {
                            url "https://maven.google.com"
                        }
                    }
                }

      #. Create an Amazon Pinpoint client in the location of your push notification code.

         .. code-block:: java
            :emphasize-lines: 0

            import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
            import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
            import com.google.android.gms.gcm.GoogleCloudMessaging;
            import com.google.android.gms.iid.InstanceID;

            public class MainActivity extends AppCompatActivity {
                 public static final String LOG_TAG = MainActivity.class.getSimpleName();

                 public static PinpointManager pinpointManager;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                     if (pinpointManager == null) {
                         PinpointConfiguration pinpointConfig = new PinpointConfiguration(
                                 getApplicationContext(),
                                 AWSMobileClient.getInstance().getCredentialsProvider(),
                                 AWSMobileClient.getInstance().getConfiguration());

                         pinpointManager = new PinpointManager(pinpointConfig);

                         new Thread(new Runnable() {
                             @Override
                             public void run() {
                               try {
                                   String deviceToken =
                                     InstanceID.getInstance(MainActivity.this).getToken(
                                         "123456789Your_GCM_Sender_Id",
                                         GoogleCloudMessaging.INSTANCE_ID_SCOPE);
                                   Log.e("NotError", deviceToken);
                                   pinpointManager.getNotificationClient()
                                                  .registerGCMDeviceToken(deviceToken);
                             } catch (Exception e) {
                                 e.printStackTrace();
                             }
                             }
                         }).start();
                     }
                 }
             }


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                    pod  'AWSSPinpoint', '~> 2.6.6'
                    # other pods

                end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call Amazon Pinpoint APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSPinpoint

      #. Add your backend service configuration to the app.

         From the location where your |AMH| configuration file was downloaded in a previous step,
         drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file
         in your Xcode project.

         Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

      #. Create an Amazon Pinpoint client by using the following code into the
         :code:`didFinishLaunchwithOptions` method of your app's :file:`AppDelegate.swift`. This
         will also register your device token with Amazon Pinpoint.

         .. code-block:: swift

             var pinpoint: AWSPinpoint?


             func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
                 [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                 pinpoint =
                     AWSPinpoint(configuration:
                         AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: launchOptions))

                 return true
             }



.. _add-aws-mobile-push-notifications-targeting:

Add Amazon Pinpoint Targeted and Campaign Push Messaging
========================================================


`Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`_ enables you to target your app users with push messaging. You can send individual messages or configure campaigns that target a group of users that match a profile that you define. For instance, you could email users that have not used the app in 30 days, or send an SMS to those that frequently use a given feature of your app.

.. container:: option

   Android - Java
      The following 2 steps show how to receive push notifications targeted for your app.

      * Add a Push Listener Service to Your App.

         The name of the class must match the push listener service name used in the app manifest.
         :code:`pinpointManager` is a reference to the static PinpointManager variable declared in
         the MainActivity shown in a previous step. Use the following steps to set up Push
         Notification listening in your app.


         #. The following push listener code assumes that the app's MainActivity is configured using
            the manifest setup described in a previous section.

            .. code-block:: java

                import android.content.Intent;
                import android.os.Bundle;
                import android.support.v4.content.LocalBroadcastManager;
                import android.util.Log;

                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationClient;
                import com.google.android.gms.gcm.GcmListenerService;

                public class YOUR-PUSH-LISTENER-SERVICE-NAME extends GcmListenerService {
                    public static final String LOGTAG = PushListenerService.class.getSimpleName();

                    // Intent action used in local broadcast
                    public static final String ACTION_PUSH_NOTIFICATION = "push-notification";
                    // Intent keys
                    public static final String INTENT_SNS_NOTIFICATION_FROM = "from";
                    public static final String INTENT_SNS_NOTIFICATION_DATA = "data";

                    /**
                     * Helper method to extract push message from bundle.
                     *
                     * @param data bundle
                     * @return message string from push notification
                     */
                    public static String getMessage(Bundle data) {
                        // If a push notification is sent as plain
                        // text, then the message appears in "default".
                        // Otherwise it's in the "message" for JSON format.
                        return data.containsKey("default") ? data.getString("default") : data.getString(
                                "message", "");
                    }

                    private void broadcast(final String from, final Bundle data) {
                        Intent intent = new Intent(ACTION_PUSH_NOTIFICATION);
                        intent.putExtra(INTENT_SNS_NOTIFICATION_FROM, from);
                        intent.putExtra(INTENT_SNS_NOTIFICATION_DATA, data);
                        LocalBroadcastManager.getInstance(this).sendBroadcast(intent);
                    }

                    @Override
                    public void onMessageReceived(final String from, final Bundle data) {
                        Log.d(LOGTAG, "From:" + from);
                        Log.d(LOGTAG, "Data:" + data.toString());

                        final NotificationClient notificationClient =
                            MainActivity.pinpointManager.getNotificationClient();

                        NotificationClient.CampaignPushResult pushResult =
                                notificationClient.handleGCMCampaignPush(from, data, this.getClass());

                        if (!NotificationClient.CampaignPushResult.NOT_HANDLED.equals(pushResult)) {
                            // The push message was due to a Pinpoint campaign.
                            // If the app was in the background, a local notification was added
                            // in the notification center. If the app was in the foreground, an
                            // event was recorded indicating the app was in the foreground,
                            // for the demo, we will broadcast the notification to let the main
                            // activity display it in a dialog.
                            if (
                                NotificationClient.CampaignPushResult.APP_IN_FOREGROUND.equals(pushResult)) {
                                    // Create a message that will display the raw
                                    //data of the campaign push in a dialog.
                                    data.putString("
                                        message",
                                        String.format("Received Campaign Push:\n%s", data.toString()));
                                    broadcast(from, data);
                            }
                            return;
                        }
                    }
                }

         #. Add code to react to your push listener service.

            The following code can be placed where your app will react to incoming notifications.

            .. code-block:: java
               :emphasize-lines: 0

                import android.app.Activity;
                import android.app.AlertDialog;
                import android.content.BroadcastReceiver;
                import android.content.Context;
                import android.content.Intent;
                import android.content.IntentFilter;
                import android.support.v4.content.LocalBroadcastManager;
                import android.support.v7.app.AppCompatActivity;
                import android.os.Bundle;
                import android.util.Log;

                public class MainActivity extends AppCompatActivity {
                    public static final String LOG_TAG = MainActivity.class.getSimpleName();

                    @Override
                    protected void onPause() {
                        super.onPause();

                        // unregister notification receiver
                        LocalBroadcastManager.getInstance(this).unregisterReceiver(notificationReceiver);
                    }

                    @Override
                    protected void onResume() {
                        super.onResume();

                        // register notification receiver
                        LocalBroadcastManager.getInstance(this).registerReceiver(notificationReceiver,
                                new IntentFilter(PushListenerService.ACTION_PUSH_NOTIFICATION));
                    }

                    private final BroadcastReceiver notificationReceiver = new BroadcastReceiver() {
                        @Override
                        public void onReceive(Context context, Intent intent) {
                            Log.d(LOG_TAG, "Received notification from local broadcast. Display it in a dialog.");

                            Bundle data = intent.getBundleExtra(PushListenerService.INTENT_SNS_NOTIFICATION_DATA);
                            String message = PushListenerService.getMessage(data);

                            new AlertDialog.Builder(MainActivity.this)
                                    .setTitle("Push notification")
                                    .setMessage(message)
                                    .setPositiveButton(android.R.string.ok, null)
                                    .show();
                        }
                    };

                }


   iOS - Swift
      #. In your :code:`AppDelegate` with :code:`PinpointManager` instantiated, make sure the push
         listening code exists in the following functions.

         .. code-block:: swift
            :emphasize-lines: 0

             // . . .

                 func application(
                     _ application: UIApplication,
                                    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

                         pinpoint!.notificationManager.interceptDidRegisterForRemoteNotifications(
                                 withDeviceToken: deviceToken)
                 }

                 func application(
                     _ application: UIApplication,
                                    didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                                    fetchCompletionHandler completionHandler:
                                         @escaping (UIBackgroundFetchResult) -> Void) {

                         pinpoint!.notificationManager.interceptDidReceiveRemoteNotification(
                                 userInfo, fetchCompletionHandler: completionHandler)

                     if (application.applicationState == .active) {
                         let alert = UIAlertController(title: "Notification Received",
                                                       message: userInfo.description,
                                                       preferredStyle: .alert)
                         alert.addAction(UIAlertAction(title: "Ok", style: .default, handler: nil))

                         UIApplication.shared.keyWindow?.rootViewController?.present(
                             alert, animated: true, completion:nil)
                     }
                 }
             // . . .
             }

      #. Add the following code in the :code:`ViewController` where you request notification
         permissions.

         .. code-block:: swift

             var userNotificationTypes : UIUserNotificationType
             userNotificationTypes = [.alert , .badge , .sound]
             let notificationSettings = UIUserNotificationSettings.init(types: userNotificationTypes, categories: nil)
             UIApplication.shared.registerUserNotificationSettings(notificationSettings)
             UIApplication.shared.registerForRemoteNotifications()

      #. In Xcode, choose your app target in the Project Navigator, choose :guilabel:`Capabilities`,
         turn on :guilabel:`Push Notifications`.

         .. image:: images/xcode-turn-on-push-notification.png
            :scale: 100
            :alt: Image of turning on Push Notifications capabilities in Xcode.

         .. only:: pdf

            .. image:: images/xcode-turn-on-push-notification.png
               :scale: 50

         .. only:: kindle

            .. image:: images/xcode-turn-on-push-notification.png
               :scale: 75

      #. Build and run your app using information at `Building the Sample iOS App From AWS Mobile
         Hub <http://docs.aws.amazon.com/pinpoint/latest/developerguide/getting-started-ios-sampleapp.html>`_.




