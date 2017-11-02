.. _add-aws-mobile-cloud-logic:

##################################
Add Cloud Logic to Your Mobile App
##################################


.. meta::
   :description: Integrating Cloud Logic into your mobile app


.. _add-aws-cloud-logic-backend-overview:

Cloud Logic
===========


Add RESTful APIs handled by your serverless |LAM| functions to extend your mobile app to the range
of AWS services and beyond. In |AMH|, enabling the :ref:`cloud-logic` feature uses `Amazon API
Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/>`_ and `AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/>`_ services to provide these capabilities.


.. _add-aws-cloud-logic-backend-setup:

Set Up Your Backend
===================


#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the integration steps on this page.

#. Use |AMHlong| to deploy your back end in minutes.


   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create
      project`.

      Or select an existing project.

   #. Choose the :guilabel:`Cloud Logic` tile to enable the feature.

   #. Create a new API or import one that you created in the `API Gateway console <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`_.


      #. To create a new API choose :guilabel:`Create an API`.

      #. Type an :guilabel:`API Name` and :guilabel:`Description`.

      #. Configure your :guilabel:`Paths`. Paths are locations to the serverless |LAMlong| functions
         that handle requests to your API.

         Choose :guilabel:`Create API` to deploy a default API and its associated handler function.
         The default handler is a Node.js function that echoes JSON input that it receives. For more
         information, see `Using AWS Lambda with Amazon API Gateway <with-on-demand-https.html>`_.

   #. Download your |AMH| project configuration file.

      #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

      #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 100 %
            :alt: Image of the Mobile Hub console when choosing Download Configuration File.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 75

      #. Under :guilabel:`NoSQL / Cloud Logic` ßat the bottom of the page, choose
         :guilabel:`Downloads`, and then choose your platform to get model files for your |ABP|
         APIs.


         .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
            :scale: 100
            :alt: Image of the Download Configuration Files button in the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 75

         *Remember:*

         Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use updated files for those features.


.. _add-aws-mobile-cloud-logic-app:

Add the SDK to Your App
=======================


Use the following steps to add AWS Cloud Logic to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml
               :emphasize-lines: 1,2

                <uses-permission android:name="android.permission.INTERNET" />
                <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

         #. :file:`app/build.gradle` must contain:

            .. code-block:: none
               :emphasize-lines: 4

                dependencies{
                    // . . .
                    compile 'com.amazonaws:aws-android-sdk-apigateway-core:2.6.+'
                    // . . .
                }

         #. For each Activity where you make calls to |ABP|, declare the following imports. Replace the portion of the first declaration, denoted here as   :code:`idABCD012345.NAME-OF-YOUR-API-MODEL-CLASS`, with class id and name of the API model that you downloaded from your |AMH| project.

            You can find these values at the top of the :file:`./src/main/java/com/amazonaws/mobile/api/API-CLASS-ID/TestMobileHubClient.java` file of the download.

            .. code-block:: java
               :emphasize-lines: 1-8

                // This statement imports the model class you download from |AMH|.
                import com.amazonaws.mobile.api.idABCD012345.NAME-OF-YOUR-API-MODEL-CLASSMobileHubClient;

                import com.amazonaws.mobile.auth.core.IdentityManager;
                import com.amazonaws.mobile.config.AWSConfiguration;
                import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
                import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
                import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
                import com.amazonaws.util.IOUtils;
                import com.amazonaws.util.StringUtils;
                import java.io.InputStream;

         #. Add the project configuration file and API model files you downloaded from the |AMH|
            console. The API model files provide access to the API request surface for each |ABP| API
            they model.

            #. Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android
               Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown
               menu.

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 100
                  :alt: Image of the Download Configuration Files button in the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                     :scale: 75

            #. From the location where configuration files were downloaded in a previous step, drag
               :file:`awsconfiguration.json` into the :file:`res/raw` folder.

            #. The location where you downloaded the API model file(s) contains a folder for each
               Cloud Logic API you created in your |AMH| project. The folders are named for the
               class ID assigned to the API by |ABP|. For each folder:


               #. In a text editor, open
                  :file:`./src/main/java/com/amazonaws/mobile/api/YOUR-API-CLASS-ID/YOUR-API-CLASS-NAMEMobileHubClient.java`.

               #. Copy the package name at the top of the file with the form:
                  :code:`com.amazonaws.mobile.api.{api-class-id}`.

               #. In Android Studio, right-click on :file:`app/java`, and then choose :guilabel:`New >
                  Package`.

               #. Paste the package name you copied in a previous step and choose :guilabel:`OK`.

               #. Drag and drop the contents of the API class folder into the newly created package.
                  The contents include :file:`YOUR-API-CLASS-NAMEMobileHubClient.java` and the :file:`model`
                  folder.

      #. Invoke a Cloud Logic API.

         The following code shows how to invoke a Cloud Logic API using your API's client class,
         model, and resource paths.

         .. code-block:: java

             package your.package.name;

             import com.amazonaws.mobileconnectors.api.YOUR-API-CLASS-ID.YOUR-API-CLASS-NAMEMobilehubClient;
             import android.support.v7.app.AppCompatActivity;
             import android.os.Bundle;
             import android.util.Log;
             import android.view.View;

             import com.amazonaws.auth.AWSCredentialsProvider;
             import com.amazonaws.http.HttpMethodName;
             import com.amazonaws.mobile.auth.core.IdentityManager;
             import com.amazonaws.mobile.auth.core.StartupAuthResult;
             import com.amazonaws.mobile.auth.core.StartupAuthResultHandler;
             import com.amazonaws.mobile.config.AWSConfiguration;
             import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
             import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
             import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
             import com.amazonaws.util.IOUtils;
             import com.amazonaws.util.StringUtils;

             import java.io.InputStream;
             import java.util.HashMap;
             import java.util.Map;
             import java.util.concurrent.CountDownLatch;
             import java.util.concurrent.TimeUnit;

             public class MainActivity extends AppCompatActivity {
                 private static final String LOG_TAG = MainActivity.class.getSimpleName();

                 private YOUR-API-CLASS-NAMEMobileHubClientMobileHubClient apiClient;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                     final AWSCredentialsProvider credentialsProvider =
                                     IdentityManager.getDefaultIdentityManager().getCredentialsProvider();

                      // Create the client
                      apiClient = new ApiClientFactory()
                                     .credentialsProvider(credentialsProvider)
                                     .build(HelloMobileHubClient.class);
                         }
                     });
                 }

                 public void onClick(View view) {
                     // Create components of api request
                     final String method = "GET";

                     final String path = "/items";

                     final String body = "";
                     final byte[] content = body.getBytes(StringUtils.UTF8);

                     final Map parameters = new HashMap<>();
                     parameters.put("lang", "en_US");

                     final Map headers = new HashMap<>();

                     // Use components to create the api request
                     ApiRequest localRequest =
                             new ApiRequest(apiClient.getClass().getSimpleName())
                                     .withPath(path)
                                     .withHttpMethod(HttpMethodName.valueOf(method))
                                     .withHeaders(headers)
                                     .addHeader("Content-Type", "application/json")
                                     .withParameters(parameters);

                     // Only set body if it has content.
                     if (body.length() > 0) {
                         localRequest = localRequest
                                 .addHeader("Content-Length", String.valueOf(content.length))
                                 .withBody(content);
                     }

                     final ApiRequest request = localRequest;

                     // Make network call on background thread
                     new Thread(new Runnable() {
                         @Override
                         public void run() {
                             try {
                                 Log.d(LOG_TAG,
                                 "Invoking API w/ Request : " +
                                 request.getHttpMethod() + ":" +
                                 request.getPath());

                                 final ApiResponse response =
                                     apiClient.execute(request);

                                 final InputStream responseContentStream = response.getContent();

                                 if (responseContentStream != null) {
                                     final String responseData = IOUtils.toString(responseContentStream);
                                     Log.d(LOG_TAG, "Response : " + responseData);
                                 }

                                 Log.d(LOG_TAG, response.getStatusCode() + " " + response.getStatusText());

                             } catch (final Exception exception) {
                                 Log.e(LOG_TAG, exception.getMessage(), exception);
                                 exception.printStackTrace();
                             }
                         }
                     }).start();
                 }
             }


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

               platform :ios, '9.0'

               target :'YourAppTarget' do
                  use_frameworks!

                     pod 'AWSAuthCore', '~> 2.6.5'
                     pod 'AWSAPIGateway', '~> 2.6.5'
                     # other pods

               end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |ABP| APIs must use the following import statements:

            .. code-block:: none
               :emphasize-lines: 0

                import AWSAuthCore
                import AWSCore
                import AWSAPIGateway

         #. Add the backend service configuration and API model files that you downloaded from the |AMH|
            console, The API model files provide an API calling surface for each |ABP| API they model.


            #. From the location where your |AMH| configuration file was downloaded in a previous
               step, drag :file:`awsconfiguration.json` into the folder containing your
               :file:`info.plist` file in your Xcode project.

               Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

            #. From the location where you downloaded the data model file(s), drag and drop the
               :file:`./AmazonAws/API` folder into the Xcode project folder that contains
               :file:`AppDelegate.swift`.

               Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

               If your Xcode project already contains a :file:`Bridging_Header.h` file then open
               :file:`./AmazonAws/Bridging_Header.h`, copy the import statement it contains, and
               paste it into your version of the file.

               If your Xcode project does not contain a :file:`Bridging_Header.h` file then:

               #. Drag and drop :file:`./AmazonAws/Bridging_Header.h` into the Xcode project folder
                  that contains :file:`AppDelegate.swift`.

               #. Choose your project root in Xcode, then choose :guilabel:`Build Settings`, and
                  search for "bridging headers"

               #. Choose :guilabel:`Objective-C Bridging Header`, press your :emphasis:`return` key,
                  and type the path within your Xcode project:

                  :file:`{your-project-name/.../}Bridging_Header.h`

      #. Invoke a Cloud Logic API.

         To invoke a Cloud Logic API, create code in the following form and substitute your API's
         client class, model, and resource paths.

         .. code-block:: swift

             class InvokeAPI {

             func doInvoke() {
                 // change the method name, or path or the query string parameters here as desired
                 let httpMethodName = "POST"
                 let URLString = "{/items}"
                 let queryStringParameters = ["key1":"{value1}"]
                 let headerParameters = [
                     "Content-Type": "application/json",
                     "Accept": "application/json"
                 ]

                 let httpBody = "{ \n  " +
                         "\"key1\":\"value1\", \n  " +
                         "\"key2\":\"value2\", \n  " +
                         "\"key3\":\"value3\"\n}"

                 // Construct the request object
                 let apiRequest = AWSAPIGatewayRequest(httpMethod: httpMethodName,
                         urlString: URLString,
                         queryParameters: queryStringParameters,
                         headerParameters: headerParameters,
                         httpBody: httpBody)

                 // Create a service configuration object for the region your AWS API was created in
                 let serviceConfiguration = AWSServiceConfiguration(
                     region: {.USEast1},
                     credentialsProvider: AWSIdentityManager.default().credentialsProvider)

                     APIGatewayClientID.register(
                         with: serviceConfiguration!, forKey: "{MyCloudLogicConfig}")

                     // Fetch the Cloud Logic client to be used for invocation
                     //
                     let invocationClient =
                         AWSAPI_{api-class-id}_{your-api-name}MobileHubClient(
                               forkey: "{MyCloudLogicConfig}")

                     invocationClient?.invoke(apiRequest).continueWith { (
                         task: AWSTask) -> Any? in
                         guard let strongSelf = self else { return nil }

                         if let error = task.error {
                             print("Error occurred: \(error)")
                             // Handle error here
                             return nil
                         }

                         // Handle successful result here
                         let result = task.result!
                         let responseString =
                             String(data: result.responseData!, encoding: .utf8)

                         print(responseString)
                         print(result.statusCode)

                         return nil
                     })
                 }
             }




