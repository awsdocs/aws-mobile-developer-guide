
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

#. Use the CLI to add push notifications to your cloud-enabled backend and app.

      .. container:: option

         Android - Java
             In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add notifications

         Android - Kotlin
             In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add notifications

         iOS - Swift
             In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`xcodeproj` file), and add the SDK to your app.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add notifications

#. Set up your backend to support receiving push notifications:

   .. container:: option

       Android - Java
          - Choose Firebase Cloud Messaging (FCM).

            .. code-block:: none

               > FCM

          - Provide your ApiKey. The FCM console refers to this value as :guilabel:`ServerKey`. For information on getting an FCM ApiKey, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`__

       Android - Kotlin
          - Choose Firebase Cloud Messaging (FCM).

            .. code-block:: none

               > FCM

          - Provide your ApiKey. The FCM console refers to this value as "ServerKey". For information on getting an FCM ApiKey, see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`__

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

         #. Add the following dependencies and plugin to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies {
                    // Overrides an auth dependency to ensure correct behavior
                    implementation 'com.google.android.gms:play-services-auth:15.0.1'

                    implementation 'com.google.firebase:firebase-core:16.0.1'
                    implementation 'com.google.firebase:firebase-messaging:17.3.0'

                    implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.7.+'
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                }

                apply plugin: 'com.google.gms.google-services'

         #. Add the following to your project level :file:`build.gradle`. Make sure that you specify the `google` repository:

            .. code-block:: none

                buildscript {
                    dependencies {
                        classpath 'com.google.gms:google-services:4.0.1'
                    }
                }

                allprojects {
                    repositories {
                        google()
                    }
                }

         #. :file:`AndroidManifest.xml` must contain the definition of the following service for PushListenerService in the application tag:

            .. code-block:: xml

                <service
                    android:name=".PushListenerService">
                    <intent-filter>
                        <action android:name="com.google.firebase.MESSAGING_EVENT"/>
                    </intent-filter>
                </service>

      #. Create an Amazon Pinpoint client in the location of your push notification code.

         .. code-block:: java

            import android.content.BroadcastReceiver;
            import android.content.Context;
            import android.content.Intent;
            import android.content.IntentFilter;
            import android.os.Bundle;
            import android.support.annotation.NonNull;
            import android.support.v4.content.LocalBroadcastManager;
            import android.support.v7.app.AlertDialog;
            import android.support.v7.app.AppCompatActivity;
            import android.util.Log;

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;
            import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
            import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
            import com.google.android.gms.tasks.OnCompleteListener;
            import com.google.android.gms.tasks.Task;
            import com.google.firebase.iid.FirebaseInstanceId;
            import com.google.firebase.iid.InstanceIdResult;

            public class MainActivity extends AppCompatActivity {
                public static final String TAG = MainActivity.class.getSimpleName();

                private static PinpointManager pinpointManager;

                public static PinpointManager getPinpointManager(final Context applicationContext) {
                    if (pinpointManager == null) {
                        PinpointConfiguration pinpointConfig = new PinpointConfiguration(
                                applicationContext,
                                AWSMobileClient.getInstance().getCredentialsProvider(),
                                AWSMobileClient.getInstance().getConfiguration());

                        pinpointManager = new PinpointManager(pinpointConfig);

                        FirebaseInstanceId.getInstance().getInstanceId()
                                .addOnCompleteListener(new OnCompleteListener<InstanceIdResult>() {
                                    @Override
                                    public void onComplete(@NonNull Task<InstanceIdResult> task) {
                                        final String token = task.getResult().getToken();
                                        Log.d(TAG, "Registering push notifications token: " + token);
                                        pinpointManager.getNotificationClient().registerDeviceToken(token);
                                    }
                                });
                    }
                    return pinpointManager;
                }

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

                    // Initialize PinpointManager
                    getPinpointManager(getApplicationContext());
                }
            }

   Android - Kotlin
      #. Set up AWS Mobile SDK components as follows.

         #. Add the following dependencies and plugin to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies {
                    // Overrides an auth dependency to ensure correct behavior
                    implementation 'com.google.android.gms:play-services-auth:15.0.1'

                    implementation 'com.google.firebase:firebase-core:16.0.1'
                    implementation 'com.google.firebase:firebase-messaging:17.3.0'

                    implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.7.+'
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                }

                apply plugin: 'com.google.gms.google-services'

         #. Add the following to your project level :file:`build.gradle`. Make sure that you specify the `google` repository:

            .. code-block:: none

                buildscript {
                    dependencies {
                        classpath 'com.google.gms:google-services:4.0.1'
                    }
                }

                allprojects {
                    repositories {
                        google()
                    }
                }

         #. :file:`AndroidManifest.xml` must contain the definition of the following service for PushListenerService in the application tag:

            .. code-block:: xml

                    <service
                        android:name=".PushListenerService">
                        <intent-filter>
                            <action android:name="com.google.firebase.MESSAGING_EVENT"/>
                        </intent-filter>
                    </service>

      #. Create an Amazon Pinpoint client in the location of your push notification code.

         .. code-block:: kotlin

            import android.content.BroadcastReceiver
            import android.content.Context
            import android.content.Intent
            import android.content.IntentFilter
            import android.support.v7.app.AppCompatActivity
            import android.os.Bundle
            import android.support.v4.content.LocalBroadcastManager
            import android.support.v7.app.AlertDialog
            import android.util.Log
            import com.amazonaws.mobile.client.AWSMobileClient
            import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration
            import com.amazonaws.mobileconnectors.pinpoint.PinpointManager
            import com.google.firebase.iid.FirebaseInstanceId

            class MainActivity : AppCompatActivity() {

                private val notificationReceiver = object : BroadcastReceiver() {
                    override fun onReceive(context: Context, intent: Intent) {
                        Log.d(TAG, "Received notification from local broadcast. Display it in a dialog.")

                        val bundle = intent.extras
                        val message = PushListenerService.getMessage(bundle!!)

                        AlertDialog.Builder(this@MainActivity)
                                .setTitle("Push notification")
                                .setMessage(message)
                                .setPositiveButton(android.R.string.ok, null)
                                .show()
                    }
                }

                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreate(savedInstanceState)
                    setContentView(R.layout.activity_main)

                    // Initialize the AWS Mobile Client
                    AWSMobileClient.getInstance().initialize(this) { Log.d(TAG, "AWSMobileClient is instantiated and you are connected to AWS!") }.execute()

                    // Initialize PinpointManager
                    getPinpointManager(applicationContext)
                }

                override fun onPause() {
                    super.onPause()

                    // Unregister notification receiver
                    LocalBroadcastManager.getInstance(this).unregisterReceiver(notificationReceiver)
                }

                override fun onResume() {
                    super.onResume()

                    // Register notification receiver
                    LocalBroadcastManager.getInstance(this).registerReceiver(notificationReceiver,
                            IntentFilter(PushListenerService.ACTION_PUSH_NOTIFICATION))
                }

                companion object {
                    val TAG = MainActivity.javaClass.simpleName

                    private var pinpointManager: PinpointManager? = null

                    fun getPinpointManager(applicationContext: Context): PinpointManager? {
                        if (pinpointManager == null) {
                            val pinpointConfig = PinpointConfiguration(
                                    applicationContext,
                                    AWSMobileClient.getInstance().credentialsProvider,
                                    AWSMobileClient.getInstance().configuration)

                            pinpointManager = PinpointManager(pinpointConfig)

                            FirebaseInstanceId.getInstance().instanceId
                                    .addOnCompleteListener { task ->
                                        val token = task.result.token
                                        Log.d(TAG, "Registering push notifications token: $token")
                                        pinpointManager!!.notificationClient.registerDeviceToken(token)
                                    }
                        }
                        return pinpointManager
                    }
                }
            }

   iOS - Swift
       #. Set up AWS Mobile SDK components as follows.

         #. The :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                    pod  'AWSPinpoint', '~> 2.6.13'

                    # other pods . . .

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

         Note: If you have already integrated :code:`Analytics`, you can skip this step.

         .. code-block:: swift

             /** start code copy **/
             var pinpoint: AWSPinpoint?
             /** end code copy **/


             func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
                 [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                 /** start code copy **/
                 pinpoint = AWSPinpoint(configuration:
                         AWSPinpointConfiguration.defaultPinpointConfiguration(launchOptions: launchOptions))
                 /** end code copy **/

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
         the MainActivity shown in a previous step. Use the following steps to detect and display Push
         Notification in your app.


         #. The following push listener code assumes that the app's MainActivity is configured using
            the manifest setup described in a previous section.

            .. code-block:: java

                import android.content.Intent;
                import android.os.Bundle;
                import android.support.v4.content.LocalBroadcastManager;
                import android.util.Log;

                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationClient;
                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationDetails;
                import com.google.firebase.messaging.FirebaseMessagingService;
                import com.google.firebase.messaging.RemoteMessage;

                import java.util.HashMap;

                public class PushListenerService extends FirebaseMessagingService {
                    public static final String TAG = PushListenerService.class.getSimpleName();

                    // Intent action used in local broadcast
                    public static final String ACTION_PUSH_NOTIFICATION = "push-notification";
                    // Intent keys
                    public static final String INTENT_SNS_NOTIFICATION_FROM = "from";
                    public static final String INTENT_SNS_NOTIFICATION_DATA = "data";

                    @Override
                    public void onNewToken(String token) {
                        super.onNewToken(token);

                        Log.d(TAG, "Registering push notifications token: " + token);
                        MainActivity.getPinpointManager(getApplicationContext()).getNotificationClient().registerDeviceToken(token);
                    }

                    @Override
                    public void onMessageReceived(RemoteMessage remoteMessage) {
                        super.onMessageReceived(remoteMessage);
                        Log.d(TAG, "Message: " + remoteMessage.getData());

                        final NotificationClient notificationClient = MainActivity.getPinpointManager(getApplicationContext()).getNotificationClient();

                        final NotificationDetails notificationDetails = NotificationDetails.builder()
                                .from(remoteMessage.getFrom())
                                .mapData(remoteMessage.getData())
                                .intentAction(NotificationClient.FCM_INTENT_ACTION)
                                .build();

                        NotificationClient.CampaignPushResult pushResult = notificationClient.handleCampaignPush(notificationDetails);

                        if (!NotificationClient.CampaignPushResult.NOT_HANDLED.equals(pushResult)) {
                            /**
                               The push message was due to a Pinpoint campaign.
                               If the app was in the background, a local notification was added
                               in the notification center. If the app was in the foreground, an
                               event was recorded indicating the app was in the foreground,
                               for the demo, we will broadcast the notification to let the main
                               activity display it in a dialog.
                            */
                            if (NotificationClient.CampaignPushResult.APP_IN_FOREGROUND.equals(pushResult)) {
                                /* Create a message that will display the raw data of the campaign push in a dialog. */
                                final HashMap<String, String> dataMap = new HashMap<>(remoteMessage.getData());
                                broadcast(remoteMessage.getFrom(), dataMap);
                            }
                            return;
                        }
                    }

                    private void broadcast(final String from, final HashMap<String, String> dataMap) {
                        Intent intent = new Intent(ACTION_PUSH_NOTIFICATION);
                        intent.putExtra(INTENT_SNS_NOTIFICATION_FROM, from);
                        intent.putExtra(INTENT_SNS_NOTIFICATION_DATA, dataMap);
                        LocalBroadcastManager.getInstance(this).sendBroadcast(intent);
                    }

                    /**
                     * Helper method to extract push message from bundle.
                     *
                     * @param data bundle
                     * @return message string from push notification
                     */
                    public static String getMessage(Bundle data) {
                        return ((HashMap) data.get("data")).toString();
                    }
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

                import android.content.Intent
                import android.os.Bundle
                import android.support.v4.content.LocalBroadcastManager
                import android.util.Log

                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationClient
                import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationDetails
                import com.google.firebase.messaging.FirebaseMessagingService
                import com.google.firebase.messaging.RemoteMessage

                import java.util.HashMap

                class PushListenerService : FirebaseMessagingService() {

                    override fun onNewToken(token: String?) {
                        super.onNewToken(token)

                        Log.d(TAG,"Registering push notifications token: " + token!!)
                        MainActivity.getPinpointManager(applicationContext)?.notificationClient?.registerDeviceToken(token)
                    }

                    override fun onMessageReceived(remoteMessage: RemoteMessage?) {
                        super.onMessageReceived(remoteMessage)
                        Log.d(TAG,"Message: " + remoteMessage?.data)

                        val notificationClient = MainActivity.getPinpointManager(applicationContext)?.notificationClient

                        val notificationDetails = NotificationDetails.builder()
                                .from(remoteMessage?.from)
                                .mapData(remoteMessage?.data)
                                .intentAction(NotificationClient.FCM_INTENT_ACTION)
                                .build()

                        val pushResult = notificationClient?.handleCampaignPush(notificationDetails)

                        if (NotificationClient.CampaignPushResult.NOT_HANDLED != pushResult) {
                            /**
                             * The push message was due to a Pinpoint campaign.
                             * If the app was in the background, a local notification was added
                             * in the notification center. If the app was in the foreground, an
                             * event was recorded indicating the app was in the foreground,
                             * for the demo, we will broadcast the notification to let the main
                             * activity display it in a dialog.
                             */
                            if (NotificationClient.CampaignPushResult.APP_IN_FOREGROUND == pushResult) {
                                /* Create a message that will display the raw data of the campaign push in a dialog. */
                                val dataMap = HashMap(remoteMessage?.data)
                                broadcast(remoteMessage?.from, dataMap)
                            }
                            return
                        }
                    }

                    private fun broadcast(from: String?, dataMap: HashMap<String, String>) {
                        val intent = Intent(ACTION_PUSH_NOTIFICATION)
                        intent.putExtra(INTENT_SNS_NOTIFICATION_FROM, from)
                        intent.putExtra(INTENT_SNS_NOTIFICATION_DATA, dataMap)
                        LocalBroadcastManager.getInstance(this).sendBroadcast(intent)
                    }

                    companion object {
                        val TAG = PushListenerService.javaClass.simpleName

                        // Intent action used in local broadcast
                        val ACTION_PUSH_NOTIFICATION = "push-notification"
                        // Intent keys
                        val INTENT_SNS_NOTIFICATION_FROM = "from"
                        val INTENT_SNS_NOTIFICATION_DATA = "data"

                        /**
                         * Helper method to extract push message from bundle.
                         *
                         * @param data bundle
                         * @return message string from push notification
                         */
                        fun getMessage(data: Bundle): String {
                            return (data.get("data") as HashMap<*, *>).toString()
                        }
                    }
                }

   iOS - Swift
      #. To receive Amazon Pinpoint push notification to your app, instantiate :code:`pinpoint!.notificationManager` to intercept the registration of the app for notifications in the :code:`didRegisterForRemoteNotificationsWithDeviceToken` application call back in :code:`AppDelegate`.

         Then add and call a function like :code:`registerForPushNotifications()` to prompt permission from the user for the app to use notifications. The following example uses the :code:`UNUserNotification` framework, which is available in iOS 10.0+. Choose the right location in your app to prompt the user for permissions. In the following example the call is implemented in the :code:`application(_:didFinishLaunchingWithOptions:)` event in :code:`AppDelegate`. This causes the prompt to appear when the app launches.

         .. code-block:: swift

            import UserNotifications
            import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationClient
            import com.amazonaws.mobileconnectors.pinpoint.targeting.notification.NotificationDetails
            // Other imports . . .

            class AppDelegate: UIResponder, UIApplicationDelegate {

                // Other app delegate methods . . .

                func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

                    // Other didFinishLaunching code . . .

                    registerForPushNotifications()
                    return true
                }

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

                // Resquest for user to grant permissions for the app to use notifications
                func registerForPushNotifications() {
                    UNUserNotificationCenter.current().delegate = self
                    UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) {
                        (granted, error) in
                        print("Permission granted: \(granted)")
                        // 1. Check if permission granted
                        guard granted else { return }
                        // 2. Attempt registration for remote notifications on the main thread
                        DispatchQueue.main.async {
                            UIApplication.shared.registerForRemoteNotifications()
                        }
                    }
                }

                // Other app delegate methods . . .

            }

         .. note::

            If you already have push notification delegate methods, you can just add the :code:`interceptDidRegisterForRemoteNotifications` and :code:`interceptDidReceiveRemoteNotification` callbacks to Pinpoint client.


      #. In Xcode Project Navigator, choose your app name at the top, choose your app name under :guilabel:`Targets`, choose the :guilabel:`Capabilities` tab, and then turn on :guilabel:`Push Notifications`.

         .. image:: images/xcode-turn-on-push-notification.png
            :scale: 100
            :alt: Image of turning on Push Notifications capabilities in Xcode.

         .. only:: pdf

            .. image:: images/xcode-turn-on-push-notification.png
               :scale: 50

         .. only:: kindle

            .. image:: images/xcode-turn-on-push-notification.png
               :scale: 75

      #. Configure the app to run in the :guilabel:`Release` profile instead of the default :guilabel:`Debug` profile. Perform the following steps to get a notification to the device:

         #. For your app target, go to the :guilabel:`General` tab of project configuration and make sure :guilabel:`Automatically Manage Signing` check box is not selected.

         #. In the :guilabel:`Signing(Release)` section, choose the production provisioning profile you created on Apple developer console. For testing push notifications on a device, you will need an `Ad Hoc Provisioining Profile <https://help.apple.com/xcode/mac/current/#/dev4335bfd3d>`__ configured with a Production AppStore and Ad Hoc certificate, and with the device(s) to be used for testing.

         #. In the top left corner of Xcode (where your app name is displayed next to the current build target device), choose on your app name and then select :guilabel:`Edit Scheme`, and then set :guilabel:`Build configuration` to :code:`Release`

            Run your app on an iPhone device to test. Push notifications are not supported on simulators.

         #. Xcode will give an error that it could not run the app, this is due to production profile apps not being allowed to debug. Click :code:`Ok` and launch the app directly from the device.

         #. When prompted, chose to allow notifications for the device.

         #. To create a new campaign to send notifications to your app from the Amazon Pinpoint console run the following command from your app project folder.

            .. code-block:: none

               $ cd YOUR_APP_PROJECT_FOLDER
               $ amplify notifications console

         #. Provide a campaign name, choose :guilabel:`Next`, choose :guilabel:`Filter by standard attributes`, and then choose iOS as the platform.

         #. You should see 1 device as a targeted endpoint, which is the app we are running on the iPhone device. Choose the option and then choose :guilabel:`Next Step`.

         #. Provide text for a sample title and body for push notification, and then choose :guilabel:`Next Step`.

         #. Choose :guilabel:`Immediate`, and then choose :guilabel:`Next Step`.

         #. Review the details on the screen, and then choose :guilabel:`Launch Campaign`.

         #. A notification should appear on the iPhone device. You may want to try testing your app receiving notifications when it is in the foreground and when closed.


