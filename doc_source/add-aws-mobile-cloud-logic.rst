
.. _add-aws-mobile-cloud-logic:

########################################################################
Add Cloud APIs to Your Mobile App with Amazon API Gateway and AWS Lambda
########################################################################


.. meta::
   :description: Integrate Cloud Logic into your mobile app to create and call APIs that are handled by serverless Lambda functions.


.. _add-aws-cloud-logic-backend-overview:

Overview
========

.. container:: option

   Android - Java
      .. _android-java:

      Add RESTful APIs handled by your serverless |LAM| functions. The CLI deploys your APIs and handlers using `Amazon API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/>`__ and `AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/>`__.

   Android - Kotlin
      .. _android-kotlin:

      Add RESTful APIs handled by your serverless |LAM| functions. The CLI deploys your APIs and handlers using `Amazon API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/>`__ and `AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/>`__.

   iOS - Swift
      .. _ios-swift:

      Add RESTful APIs handled by your serverless |LAM| functions. The CLI deploys your APIs and handlers using `Amazon API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/>`__ and `AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/>`__.

.. _cloud-backend:

Set Up Your Backend
===================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk>` steps before you proceed.

#. Use the CLI to add api to your cloud-enabled backend and app.

      .. container:: option

         Android - Java
             In a terminal window, navigate to your project folder (the folder that typically contains your project level :file:`build.gradle`), and add the SDK to your app. Note that the friendly name that specified for the `api` category will be the package name of the generated code.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add api

         Android - Kotlin
             In a terminal window, navigate to your project folder (the folder that typically contains your project level build.gradle), and add the SDK to your app. Note that the friendly name that specified for the `api` category will be the package name of the generated code.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add api

         iOS - Swift
             In a terminal window, navigate to your project folder (the folder that contains your app :file:`.xcodeproj` file), and add the SDK to your app.

            .. code-block:: bash

                $ cd ./YOUR_PROJECT_FOLDER
                $ amplify add api

#. Choose :code:`> REST` as your API service.

#. Choose :code:`> Create a new Lambda function`.

#. Choose the :code:`> Serverless express function` template.

#. Restrict API access? Choose :code:`Yes`

#. Who should have access? Choose :code:`Authenticated and Guest users`

#. When configuration of your API is complete, the CLI displays a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

   .. code-block:: none

      $ amplify status
      | Category  | Resource name   | Operation | Provider plugin   |
      | --------- | --------------- | --------- | ----------------- |
      | Function  | lambda01234567  | Create    | awscloudformation |
      | Api       | api012345678    | Create    | awscloudformation |

#. To create your backend AWS resources run:

   .. code-block:: none

      $ amplify push

   Use the steps in the next section to connect your app to your backend.

.. _cloud-logic-connect-to-your-backend:

Connect to Your Backend
=======================

Use the following steps to add Cloud Logic to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies{

                    // other dependencies . . .

                    implementation 'com.amazonaws:aws-android-sdk-apigateway-core:2.7.+'
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                    implementation ('com.amazonaws:aws-android-sdk-auth-userpools:2.7.+@aar') { transitive = true }
                }

      #. Get your API client name.

         The CLI generates a client code file for each API you add. The API client name is the name of that file, without the extension.

         The path of the client code file is :file:`./src/main/java/YOUR_API_RESOURCE_NAME/YOUR_APP_NAME_XXXXClient.java`.

         So, for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file will be :file:`./src/main/java/xyz123/useamplifyabcdClient.java`. The API client name will be :code:`useamplifyabcdClient`.

         - Find the resource name of your API by running :code:`amplify status`.

         - Copy your API client name to use when invoking the API in the following step.

      #. Invoke a Cloud Logic API.

         The following code shows how to invoke a Cloud Logic API using your API's client class,
         model, and resource paths.

         .. code-block:: java

            import android.support.v7.app.AppCompatActivity;
            import android.os.Bundle;
            import android.util.Log;

            import com.amazonaws.http.HttpMethodName;
            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;
            import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
            import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
            import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
            import com.amazonaws.util.IOUtils;
            import com.amazonaws.util.StringUtils;

            import java.io.InputStream;
            import java.util.HashMap;
            import java.util.Map;

            // TODO Replace this with your api friendly name and client class name
            import YOUR_API_RESOURCE_NAME.YOUR_APP_NAME_XXXXClient;

            public class MainActivity extends AppCompatActivity {
                private static final String TAG = MainActivity.class.getSimpleName();

                // TODO Replace this with your client class name
                private YOUR_APP_NAME_XXXXClient apiClient;

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


                    // Create the client
                    apiClient = new ApiClientFactory()
                            .credentialsProvider(AWSMobileClient.getInstance().getCredentialsProvider())
                            .build(YOUR_API_CLIENT_NAME.class);

                    callCloudLogic();
                }

                public void callCloudLogic() {
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
                                Log.d(TAG,
                                        "Invoking API w/ Request : " +
                                                request.getHttpMethod() + ":" +
                                                request.getPath());

                                final ApiResponse response = apiClient.execute(request);

                                final InputStream responseContentStream = response.getContent();

                                if (responseContentStream != null) {
                                    final String responseData = IOUtils.toString(responseContentStream);
                                    Log.d(TAG, "Response : " + responseData);
                                }

                                Log.d(TAG, response.getStatusCode() + " " + response.getStatusText());

                            } catch (final Exception exception) {
                                Log.e(TAG, exception.getMessage(), exception);
                                exception.printStackTrace();
                            }
                        }
                    }).start();
                }
            }

   Android - Kotlin
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies{

                    // other dependencies . . .

                    implementation 'com.amazonaws:aws-android-sdk-apigateway-core:2.7.+'
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.7.+@aar') { transitive = true }
                    implementation ('com.amazonaws:aws-android-sdk-auth-userpools:2.7.+@aar') { transitive = true }

                }

      #. Get your API client name.

         The CLI generates a client code file for each API you add. The API client name is the name of that file, without the extension.

         The path of the client code file is :file:`./src/main/java/YOUR_API_RESOURCE_NAME/YOUR_APP_NAME_XXXXClient.java`.

         So, for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file will be :file:`./src/main/java/xyz123/useamplifyabcdClient.java`. The API client name will be :code:`useamplifyabcdClient`.

         - Find the resource name of your API by running :code:`amplify status`.

         - Copy your API client name to use when invoking the API in the following step.


      #. Invoke a Cloud Logic API.

         The following code shows how to invoke a Cloud Logic API using your API's client class,
         model, and resource paths.

         .. code-block:: java

             import android.os.Bundle
             import android.support.v7.app.AppCompatActivity
             import android.util.Log
             import com.amazonaws.http.HttpMethodName
             import com.amazonaws.mobile.client.AWSMobileClient
             import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory
             import com.amazonaws.mobileconnectors.apigateway.ApiRequest
             import com.amazonaws.util.IOUtils
             import com.amazonaws.util.StringUtils

             // TODO Replace this with your api friendly name and client class name
             import YOUR_API_RESOURCE_NAME.YOUR_APP_NAME_XXXXClient
             import kotlin.concurrent.thread

             class MainActivity : AppCompatActivity() {
                 companion object {
                     private val TAG = MainActivity.javaClass.simpleName
                 }

                 // TODO Replace this with your client class name
                 private var apiClient: YOUR_APP_NAME_XXXXClient? = null

                 override fun onCreate(savedInstanceState: Bundle?) {
                     super.onCreate(savedInstanceState)
                     setContentView(R.layout.activity_main)

                     // Initialize the AWS Mobile Client
                     AWSMobileClient.getInstance().initialize(this) { Log.d(TAG, "AWSMobileClient is instantiated and you are connected to AWS!") }.execute()

                     // Create the client
                     apiClient = ApiClientFactory().credentialsProvider(AWSMobileClient.getInstance().credentialsProvider)
                             // TODO Replace this with your client class name
                             .build(YOUR_APP_NAME_XXXXClient::class.java)

                     callCloudLogic()
                 }

                 fun callCloudLogic() {
                     val body = ""

                     val parameters = mapOf("lang" to "en_US")
                     val headers = mapOf("Content-Type" to "application/json")

                     val request = ApiRequest(apiClient?.javaClass?.simpleName)
                             .withPath("/items")
                             .withHttpMethod(HttpMethodName.GET)
                             .withHeaders(headers)
                             .withParameters(parameters)

                     if (body.isNotEmpty()) {
                         val content = body.toByteArray(StringUtils.UTF8)
                         request.addHeader("Content-Length", content.size.toString())
                                 .withBody(content)
                     }

                     thread(start = true) {
                         try {
                             Log.d(TAG, "Invoking API")
                             val response = apiClient?.execute(request)
                             val responseContentStream = response?.getContent()
                             if (responseContentStream != null) {
                                 val responseData = IOUtils.toString(responseContentStream)
                                 // Do something with the response data here
                                 Log.d(TAG, "Response: $responseData")
                             }
                         } catch (ex: Exception) {
                             Log.e(TAG, "Error invoking API")
                         }
                     }
                 }
             }

   iOS - Swift
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

               platform :ios, '9.0'

               target :'YOUR-APP-NAME' do
                  use_frameworks!

                     # For auth
                     pod 'AWSAuthCore', '~> 2.6.13'
                     pod 'AWSMobileClient', '~> 2.6.13'

                     # For API
                     pod 'AWSAPIGateway', '~> 2.6.13'

                     # other pods

               end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Classes that call |ABP| APIs must use the following import statements:

            .. code-block:: none

                import AWSAuthCore
                import AWSCore
                import AWSAPIGateway
                import AWSMobileClient

         #. Next, import files generated by CLI. The CLI generates a client code file and request-response structure file for each API you add.

         #. Add those files by going to your Xcode Project Navigator project, right-click on project's name in top left corner, and select "Add Files to YOUR_APP_NAME".

         #. Select all the files under :code:`generated-src` folder of your application's root folder and add them to your project.

         #. Next, set the bridging header for Swift in your project settings. Double-click your project name in the Xcode Project Navigator, choose the Build Settings tab and search for  :guilabel:`Objective-C Bridging Header`. Enter :code:`generated-src/Bridging_Header.h`

            This is needed because the AWS generated code has some Objective-C code which requires bridging to be used for Swift.

            .. note::

               If you already have a bridging header in your app, you can just append an extra line to it: :code:`#import "AWSApiGatewayBridge.h"` instead of above step.

      #. Use the files generated by CLI to determine the client name of your API. In the :code:`generated-src` folder, files ending with name :code:`*Client.swift` are the names of your client (without .swift extension).

         The path of the client code file is :file:`./generated-src/YOUR_API_RESOURCE_NAME+YOUR_APP_NAME+Client.swift`.

         So, for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file might be :file:`./generated-src/xyz123useamplifyabcdClient.swift`. The API client name would be :code:`xyz123useamplifyabcdClient`.

         - Find the resource name of your API by running :code:`amplify status`.

         - Copy your API client name to use when invoking the API in the following step.


      #. Invoke a Cloud Logic API.

         To invoke a Cloud Logic API, create code in the following form and substitute your API's
         client class, model, and resource paths. Replace :code:`YOUR_API_CLIENT_NAME` with the value you copied from the previous step.

         .. code-block:: swift

            import UIKit
            import AWSAuthCore
            import AWSCore
            import AWSAPIGateway
            import AWSMobileClient

            // ViewController or application context . . .

              func doInvokeAPI() {
                   // change the method name, or path or the query string parameters here as desired
                   let httpMethodName = "POST"
                   // change to any valid path you configured in the API
                   let URLString = "/items"
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

                  // Create a service configuration
                  let serviceConfiguration = AWSServiceConfiguration(region: AWSRegionType.USEast1,
                        credentialsProvider: AWSMobileClient.sharedInstance().getCredentialsProvider())

                  // Initialize the API client using the service configuration
                  xyz123useamplifyabcdClient.registerClient(withConfiguration: serviceConfiguration!, forKey: "CloudLogicAPIKey")

                  // Fetch the Cloud Logic client to be used for invocation
                  let invocationClient = xyz123useamplifyabcdClient.client(forKey: "CloudLogicAPIKey")

                  invocationClient.invoke(apiRequest).continueWith { (task: AWSTask) -> Any? in
                           if let error = task.error {
                               print("Error occurred: \(error)")
                               // Handle error here
                               return nil
                           }

                           // Handle successful result here
                           let result = task.result!
                           let responseString = String(data: result.responseData!, encoding: .utf8)

                           print(responseString)
                           print(result.statusCode)

                           return nil
                       }
                   }
