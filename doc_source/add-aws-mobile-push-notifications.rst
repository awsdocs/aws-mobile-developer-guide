
.. _add-aws-mobile-push-notifications:

##############################################################
Add Push Notifications to Your Mobile App with Amazon Pinpoint
##############################################################

.. meta::
   :description: Integrate AWS Push Notifications into your mobile app.

.. _overview:

Overview
==========================

.. container:: option

   Android - Java
      .. _android-java:

      Enable your users to receive mobile push messages sent from the Apple (APNs) and Google (FCM/GCM) platforms. The CLI deploys a push notification backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`__. You can also create Amazon Pinpoint campaigns that tie user behavior to push or other forms of messaging.

   Android - Kotlin
      .. _android-kotlin:

      Enable your users to receive mobile push messages sent from the Apple (APNs) and Google (FCM/GCM) platforms. The CLI deploys a push notification backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`__. You can also create Amazon Pinpoint campaigns that tie user behavior to push or other forms of messaging.

   iOS - Swift
      .. _ios-swift:

      Enable your users to receive mobile push messages sent from the Apple (APNs) and Google (FCM/GCM) platforms. The CLI deploys your push notification backend using `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`__. You can also create Amazon Pinpoint campaigns that tie user behavior to push or other forms of messaging.

.. _setup-your-backend:

Set Up Your Backend
===================

#. Complete the :ref:`Get Started <getting-started>` steps before you proceed.

#. In a terminal window, navigate to the your app project folder, and add notifications.

   .. code-block:: none

      $ cd YOUR_PROJECT FOLDER
      $ amplify notifications add

#. Set up your backend to support receiving push notifications:

   .. container:: option

       Android - Java
          - Choose Firebase Cloud Messaging (FCM).

            .. code-block:: none

               > FCM

          - Provide your ApiKey. For information on getting an FCM ApiKey, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`__

       Android - Kotlin
          - Choose Firebase Cloud Messaging (FCM).

            .. code-block:: none

               > FCM

          - Provide your ApiKey. For information on getting an FCM ApiKey, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`__

       iOS - Swift
          - Choose Apple Push Notification Service (APNs).

            .. code-block:: none

               > APNS

          - Choose Certificate as your authentication method.

            .. code-block:: none

               > Certificate

          - Provide the path to your P12 certificate. For information on creating your APNs certificate, see `Setting Up iOS Push Notifications. <http://docs.aws.amazon.com/pinpoint/latest/developerguide/apns-setup.html>`__

   Use the steps in the next section to connect your app to your backend.

.. _add-aws-mobile-push-notifications-app:

Connect to Your Backend
=======================

Use the following steps to connect add push notification backend services to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components as follows.


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

                dependencies{
                    implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                    implementation ('com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar')  {transitive = true;}

                    implementation 'com.google.android.gms:play-services-iid:11.6.0'
                    implementation 'com.google.android.gms:play-services-gcm:11.6.0'
                }

         #. Add the following to your project level :file:`build.gradle`:

            .. code-block:: none

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

   Android - Kotlin
      #. Set up AWS Mobile SDK components as follows.

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

                dependencies{
                    implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'
                    implementation ('com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar')  {transitive = true;}

                    implementation 'com.google.android.gms:play-services-iid:11.6.0'
                    implementation 'com.google.android.gms:play-services-gcm:11.6.0'
                }

         #. Add the following to your project level :file:`build.gradle`:

            .. code-block:: none

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

         .. code-block:: kotlin

            import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
            import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
            import com.google.android.gms.gcm.GoogleCloudMessaging;
            import com.google.android.gms.iid.InstanceID;

            class MainActivity : AppCompatActivity() {
                companion object {
                    private val LOG_TAG = this::class.java.getSimpleName
                    var pinpointManager: PinpointManager? = null
                }

                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)
                    setContentView(R.layout.activity_main)

                    AWSMobileClient.getInstance().initialize(this).execute()
                    with (AWSMobileClient.getInstance()) {
                        if (pinpointManager == null) {
                            val config = PinpointConfiguration(applicationContext, credentialsProvider, configuration)
                            pinpointManager = PinpointManager(config)
                        }
                    }

                    thread(start = true) {
                        try {
                            val deviceToken = InstanceID.getInstance(this@MainActivity)
                                .getToken("YOUR-GCM-SENDER-ID", GoogleCloudMessaging.INSTANCE_ID_SCOPE)
                            Log.i(LOG_TAG, "GCM DeviceToken = $deviceToken")
                            pinpointManager?.notificationClient?.registerGCMDeviceToken(deviceToken)
                        } catch (e: Exception) {
                            e.printStackTrace()
                        }
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

                    pod  'AWSPinpoint', '~> 2.6.13'
                    # other pods

                end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Classes that call Amazon Pinpoint APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSPinpoint

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
===========================

The `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__ enables you to target your app users with push messaging. You can send individual messages or configure campaigns that target a group of users that match a profile that you define. For instance, you could email users that have not used the app in 30 days, or send an SMS to those that frequently use a given feature of your app.

.. container:: option

   Android - Java
      The following steps show how to receive push notifications targeted for your app.

      #. Add a push listener service to your app.

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

            Place the following code where you want your app to react to incoming notifications.

            .. code-block:: java

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

   Android - Kotlin
      The following steps show how to receive push notifications targeted for your app.

      #. Add a push listener service to your app.

         The name of the class must match the push listener service name used in the app manifest.
         :code:`pinpointManager` is a reference to the static PinpointManager variable declared in
         the MainActivity shown in a previous step. Use the following steps to set up Push
         Notification listening in your app.


         #. The following push listener code assumes that the app's MainActivity is configured using
            the manifest setup described in a previous section.

            .. code-block:: kotlin

                import android.content.Intent;
                import android.os.Bundle;
                import android.support.v4.content.LocalBroadcastManager;
                import android.util.Log;

                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationClient;
                import com.google.android.gms.gcm.GcmListenerService;

                class YOUR-PUSH-LISTENER-SERVICE-NAME : GcmListenerService() {
                    companion object {
                        private val LOG_TAG = this::class.java.simpleName
                        const val ACTION_PUSH_NOTIFICATION: String = "push-notification"
                        const val INTENT_SNS_NOTIFICATION_FROM: String = "from"
                        const val INTENT_SNS_NOTIFICATION_DATA: String = "data"

                        // Helper method to extract push message from bundle.
                        fun getMessage(data: Bundle) =
                            if (data.containsKey("default")
                                data.getString("default")
                            else
                                data.getString("message", "")
                    }

                    private fun broadcast(from: String, data: Bundle) {
                        val intent = Intent(ACTION_PUSH_NOTIFICATION).apply {
                            putExtra(INTENT_SNS_NOTIFICATION_FROM, from)
                            putExtra(INTENT_SNS_NOTIFICATION_DATA, data)
                        }
                        LocalBroadcastManager.getInstance(this).sendBroadcast(intent)
                    }

                    override fun onMessageReceived(from: String?, data: Bundle?) {
                        Log.d(LOG_TAG, "From: $from")
                        Log.d(LOG_TAG, "Data: $data")

                        val notificationClient = MainActivity.pinpointManager!!.notificationClient!!
                        val pushResult = notificationClient.handleGCMCampaignPush(from, data, this::class.java)
                        if (pushResult != NotificationClient.CampaignPushResult.NOT_HANDLED) {
                            // The push message was due to a Pinpoint campaign
                            // If the app was in the background, a local notification was added
                            // in the notification center. If the app was in the foreground, an
                            // event was recorded indicating the app was in the foreground,
                            // for the demo, we will broadcast the notification to let the main
                            // activity display it in a dialog.
                            if (pushResult == NotificationClient.CampaignPushResult.APP_IN_FOREGROUND) {
                                data.putString("message", "Received Campaign Push:\n$data")
                                broadcast(from, data)
                            }
                            return
                        }
                    }
                }

         #. Add code to react to your push listener service.

            Place the following code where you want your app to react to incoming notifications.

            .. code-block:: kotlin

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

                class MainActivity : AppCompatActivity() {
                    companion object {
                        // ...

                        val notificationReceiver = object : BroadcastReceiver() {
                            override fun onReceive(context: Context, intent: Intent) {
                                Log.d(LOG_TAG, "Received notification from local broadcast.")

                                val data = intent.getBundleExtra(PushListenerService.INTENT_SNS_NOTIFICATION_DATA)
                                val message = PushListenerService.getMessage(data)

                                // Uses anko library to display an alert dialog
                                alert(message) {
                                    title = "Push notification"
                                    positiveButton("OK") { /* Do nothing */ }
                                }.show()
                            }
                        }
                    }

                    override fun onPause() {
                        super.onPause()
                        LocalBroadcastManager.getInstance(this).unregisterReceiver(notificationReceiver)
                    }

                    override fun onResume() {
                        super.onResume()
                        LocalBroadcastManager.getInstance(this).registerReceiver(notificationReceiver,
                            IntentFilter(PushListenerService.ACTION_PUSH_NOTIFICATION))
                    }

                    // ...
                }

   iOS - Swift
      #. In your :code:`AppDelegate` with :code:`PinpointManager` instantiated, make sure the push
         listening code exists in the following functions.

         .. code-block:: swift

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
         Hub <http://docs.aws.amazon.com/pinpoint/latest/developerguide/getting-started-ios-sampleapp.html>`__.




