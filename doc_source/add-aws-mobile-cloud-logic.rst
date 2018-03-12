.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


.. _add-aws-mobile-cloud-logic:

########################################################################
Add Cloud APIs to Your Mobile App with Amazon API GateWay and AWS Lambda
########################################################################


.. meta::
   :description: Integrate Cloud Logic into your mobile app to create and call APIs that are handled by serverless Lambda functions.


.. _add-aws-cloud-logic-backend-overview:

Cloud Logic Overview
====================

Add RESTful APIs handled by your serverless |LAM| functions to extend your mobile app to the range
of AWS services and beyond. In |AMH|, enabling the :ref:`cloud-logic` feature uses `Amazon API
Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/>`__ and `AWS Lambda <http://docs.aws.amazon.com/lambda/latest/dg/>`__ services to provide these capabilities.


.. _cloud-backend:

Set Up Your Backend
===================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before your proceed.

#. Enable :guilabel:`Cloud Logic`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`Cloud Logic` tile to enable the feature.

#. Create a new API or import one that you created in the `API Gateway console <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__.

   #. To create a new API choose :guilabel:`Create an API`.

   #. Type an :guilabel:`API Name` and :guilabel:`Description`.

   #. Configure your :guilabel:`Paths`. Paths are locations to the serverless |LAMlong| functions that handle requests to your API.

      Choose :guilabel:`Create API` to deploy a default API and its associated handler function. The default handler is a Node.js function that echoes JSON input that it receives. For more information, see `Using AWS Lambda with Amazon API Gateway <with-on-demand-https.html>`__.

#. When you are done configuring the feature and the last operation is complete, choose your project name in the upper left to go the project details page. The banner that appears also links there.

   .. image:: images/updated-cloud-config.png

#. Choose :guilabel:`Integrate` on the app card.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

   If you have created apps for more than one platform, the :guilabel:`Integrate` button of each that is affected by your project changes will flash, indicating that there is an updated configuration file available for each of those versions.

#. Choose :guilabel:`Download Cloud Config` and replace the old the version of :code:`awsconfiguration.json` with the new download. Your app now references the latest version of your backend.

#. Choose  :guilabel:`Swift Models` to download API models that were generated for your app. These files provide access to the request surface for the API Gateway API you just created. Choose :guilabel:`Next` and follow the Cloud API documentation below to connect to your backend.

.. _cloud-logic-connect-to-your-backend:

Connect to Your Backend
=======================

Use the following steps to add AWS Cloud Logic to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none

                dependencies{

                    // other dependencies . . .

                    compile 'com.amazonaws:aws-android-sdk-apigateway-core:2.6.+'

                }

         #. For each Activity where you make calls to |ABP|, declare the following imports. Replace the portion of the first declaration, denoted here as   :code:`idABCD012345.NAME-OF-YOUR-API-MODEL-CLASS`, with class id and name of the API model that you downloaded from your |AMH| project.

            You can find these values at the top of the :file:`./src/main/java/com/amazonaws/mobile/api/API-CLASS-ID/TestMobileHubClient.java` file of the download.

            .. code-block:: java

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

         #. The location where you downloaded the API model file(s) contains a folder for each Cloud Logic API you created in your |AMH| project. The folders are named for the class ID assigned to the API by |ABP|. For each folder:


            #. In a text editor, open :file:`./src/main/java/com/amazonaws/mobile/api/YOUR-API-CLASS-ID/YOUR-API-CLASS-NAMEMobileHubClient.java`.

            #. Copy the package name at the top of the file with the form: :code:`com.amazonaws.mobile.api.{api-class-id}`.

            #. In Android Studio, right-choose :file:`app/java`, and then choose :guilabel:`New > Package`.

            #. Paste the package name you copied in a previous step and choose :guilabel:`OK`.

            #. Drag and drop the contents of the API class folder into the newly created package. The contents include :file:`YOUR-API-CLASS-NAMEMobileHubClient.java` and the :file:`model` folder.

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

             import com.amazonaws.mobileconnectors.api.YOUR-API-CLASS-ID.YOUR-API-CLASS-NAMEMobilehubClient;
             import com.amazonaws.mobileconnectors.apigateway.ApiClientFactory;
             import com.amazonaws.mobileconnectors.apigateway.ApiRequest;
             import com.amazonaws.mobileconnectors.apigateway.ApiResponse;
             import com.amazonaws.util.StringUtils;


             public class MainActivity extends AppCompatActivity {
                 private static final String LOG_TAG = MainActivity.class.getSimpleName();

                 private YOUR-API-CLASS-NAMEMobileHubClient apiClient;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                      // Create the client
                      apiClient = new ApiClientFactory()
                                     .credentialsProvider(AWSMobileClient.getInstance().getCredentialsProvider())
                                     .build(YOUR-API-CLASS-NAMEMobileHubClient.class);
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


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

               platform :ios, '9.0'

               target :'YOUR-APP-NAME' do
                  use_frameworks!

                     pod 'AWSAuthCore', '~> 2.6.13'
                     pod 'AWSAPIGateway', '~> 2.6.13'
                     # other pods

               end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |ABP| APIs must use the following import statements:

            .. code-block:: none

                import AWSAuthCore
                import AWSCore
                import AWSAPIGateway

         #. Add the backend service configuration and API model files that you downloaded from the |AMH|
            console, The API model files provide an API calling surface for each |ABP| API they model.

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

                     YOUR-API-CLASS-NAMEMobileHubClient.register(with: serviceConfiguration!, forKey: "CloudLogicAPIKey")

                     // Fetch the Cloud Logic client to be used for invocation
                     let invocationClient =
                         YOUR-API-CLASS-NAMEMobileHubClient(forKey: "CloudLogicAPIKey")

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
