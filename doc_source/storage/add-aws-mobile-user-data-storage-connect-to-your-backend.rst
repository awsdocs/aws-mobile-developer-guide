**To add User Data Storage to your app**

.. container:: option

   Android - Java
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`app/build.gradle`:

            .. code-block:: none
               :emphasize-lines: 2-3

               dependencies {
                  implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                  implementation 'com.amazonaws:aws-android-sdk-cognito:2.6.+'
               }

            Perform a `Gradle Sync` to download the AWS Mobile SDK components into your app

         #. Add the following to :file:`AndroidManifest.xml`:

            .. code-block:: xml
               :emphasize-lines: 1,7

               <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

               <application ... >

                  <!- . . . ->

                  <service android:name="com.amazonaws.mobileconnectors.s3.transferutility.TransferService" android:enabled="true" />

                  <!- . . . ->

               </application>

         #. For each Activity where you make calls to perform user data storage operations, import the
            following packages.

            .. code-block:: none
               :emphasize-lines: 1-2

               import com.amazonaws.mobile.config.AWSConfiguration;
               import com.amazonaws.mobileconnectors.s3.transferutility.*;

         #. Add the following code to the :code:`onCreate` method of your main or startup activity. This will establish a connection with AWS Mobile. :code:`AWSMobileClient` is a singleton that will be an interface for your AWS services.

            .. code-block:: java

               import com.amazonaws.mobile.client.AWSMobileClient;

                 public class YourMainActivity extends Activity {
                   @Override
                   protected void onCreate(Bundle savedInstanceState) {
                       super.onCreate(savedInstanceState);

                       AWSMobileClient.getInstance().initialize(this).execute();
                    }
                 }


   iOS - Swift
      Set up AWS Mobile SDK components as follows:

         #. Add the following to :file:`Podfile` that you configure to install the AWS Mobile SDK:

            .. code-block:: swift

               platform :ios, '9.0'

                  target :'YOUR-APP-NAME' do
                     use_frameworks!

                     pod 'AWSS3', '~> 2.6.13'   # For file transfers
                     pod 'AWSCognito', '~> 2.6.13'   #For data sync
                     # other pods

                  end

               Run :code:`pod install --repo-update` before you continue.

         #. Add the following imports to the classes that perform user data storage operations:

            .. code-block:: none

               import AWSCore
               import AWSS3

         #. Add the following code to your AppDelegate to establish a run-time connection with AWS Mobile.

            .. code-block:: swift

               import UIKit
               import AWSMobileClient

               @UIApplicationMain
               class AppDelegate: UIResponder, UIApplicationDelegate {

                 func application(_ application: UIApplication,
                       didFinishLaunchingWithOptions launchOptions:

                       [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
                           return AWSMobileClient.sharedInstance().interceptApplication(application, didFinishLaunchingWithOptions: launchOptions)
                 }
               }

