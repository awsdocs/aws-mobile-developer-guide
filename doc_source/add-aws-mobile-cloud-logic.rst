
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

#. In a terminal window, navigate to the root of your app files, and then add the storage category to your app. The CLI will prompt you for configuration parameters.

   .. code-block:: none

      $ cd ./ROOT_OF_YOUR_APP_FILES
      $ amplify api add

#. Choose :code:`> REST` as your API service.

#. Choose :code:`>  Create a new Lambda function`.

#. Choose the :code:`> Serverless express function` template.

#. When you complete configuration of your API, the CLI displays a message confirming that you have configured local CLI metadata for this category. You can confirm this by viewing status.

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

                    implementation 'com.amazonaws:aws-android-sdk-apigateway-core:2.6.+'

                }

      #. Get your API client name.

         The CLI generates a client code file for each API you add. The API client name is the name of that file, without the extension.

         The path of the client code file is :file:`./src/main/java/YOUR_API_RESOURCE_NAME/YOUR_APP_NAME_XXXXClient.java`.

         So for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file might be :file:`./src/main/java/xyz123/useamplifyabcdClient.java`. The API client name would be :code:`useamplifyabcdClient`.

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
             import java.io.InputStream;
             import java.util.HashMap;

             import com.amazonaws.mobile.client.AWSMobileClient;
             import com.amazonaws.mobileconnectors.api.YOUR-API-RESOURCE_NAME.YOUR-API-CLIENT-NAME;
             import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
             import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
             import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
             import com.amazonaws.util.StringUtils;


             public class MainActivity extends AppCompatActivity {
                 private static final String LOG_TAG = MainActivity.class.getSimpleName();

                 private YOUR_API_CLIENT_NAME apiClient;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                      // Create the client
                      apiClient = new ApiClientFactory()
                                     .credentialsProvider(AWSMobileClient.getInstance().getCredentialsProvider())
                                     .build(YOUR_API_CLIENT_NAME.class);
                 }


                 public callCloudLogic() {
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

                                 final ApiResponse response = apiClient.execute(request);

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

   Android - Kotlin
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies{

                    // other dependencies . . .

                    implementation 'com.amazonaws:aws-android-sdk-apigateway-core:2.6.+'

                }

      #. Get your API client name.

         The CLI generates a client code file for each API you add. The API client name is the name of that file, without the extension.

         The path of the client code file is :file:`./src/main/java/YOUR_API_RESOURCE_NAME/YOUR_APP_NAME_XXXXClient.java`.

         So for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file might be :file:`./src/main/java/xyz123/useamplifyabcdClient.java`. The API client name would be :code:`useamplifyabcdClient`.

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
             import java.io.InputStream;
             import java.util.HashMap;

             import com.amazonaws.mobile.client.AWSMobileClient;
             import com.amazonaws.mobileconnectors.api.YOUR-API-RESOURCE_NAME.YOUR-API-CLIENT-NAME;
             import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
             import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
             import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
             import com.amazonaws.util.StringUtils;


             public class MainActivity extends AppCompatActivity {
                 private static final String LOG_TAG = MainActivity.class.getSimpleName();

                 private YOUR_API_CLIENT_NAME apiClient;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                      // Create the client
                      apiClient = new ApiClientFactory()
                                     .credentialsProvider(AWSMobileClient.getInstance().getCredentialsProvider())
                                     .build(YOUR_API_CLIENT_NAME::class.java);
                 }

                fun callCloudLogic(body: String) {
                    val parameters = mapOf("lang" to "en_US")
                    val headers = mapOf("Content-Type" to "application/json")

                    val request = ApiRequest(apiClient::class.java.simpleName)
                        .withPath("/items")
                        .withHttpMethod(HttpMethod.GET)
                        .withHeaders(headers)
                        .withParameters(parameters)
                    if (body.isNotEmpty()) {
                        val content = body.getBytes(StringUtils.UTF8)
                        request
                            .addHeader("Content-Length", String.valueOf(content.length))
                            .withBody(content)
                    }

                    thread(start = true) {
                        try {
                            Log.d(TAG, "Invoking API")
                            val response = apiClient.execute(request)
                            val responseContentStream = response.getContent()
                            if (responseContentStream != null) {
                                val responseData = IOUtils.toString(responseContentStream)
                                // Do something with the response data here
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

                     pod 'AWSAuthCore', '~> 2.6.13'
                     pod 'AWSAPIGateway', '~> 2.6.13'
                     pod 'AWSMobileClient', '~> 2.6.13'
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

      #. The CLI generates a client code file for each API you add. The API client name is the name of that file, without the extension.

         The path of the client code file is :file:`./generated-src/YOUR_API_RESOURCE_NAME+YOUR_APP_NAME+Client.swift`.

         So for an app named :code:`useamplify` with an API resource named :code:`xyz123`, the path of the code file might be :file:`./generated-src/xyz123useamplifyabcdClient.swift`. The API client name would be :code:`xyz123useamplifyabcdClient`.

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

                   // Create a service configuration object for the region your AWS API was created in
                   let serviceConfiguration = AWSServiceConfiguration(
                       region: AWSRegionType.USEast1,
                       credentialsProvider: AWSMobileClient.sharedInstance().getCredentialsProvider())

                       YOUR_API_CLIENT_NAME.register(with: serviceConfiguration!, forKey: "CloudLogicAPIKey")

                       // Fetch the Cloud Logic client to be used for invocation
                       let invocationClient =
                            YOUR_API_CLIENT_NAME(forKey: "CloudLogicAPIKey")

                       invocationClient.invoke(apiRequest).continueWith { (
                           task: AWSTask) -> Any? in

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
                       }
                   }
