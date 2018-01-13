.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

###########################################
iOS: Execute Code On Demand with AWS Lambda
###########################################

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-cloud-logic>` to install the SDK and integrate AWS Lambda functions.

*Or, use the contents of this page if your app will integrate existing AWS services.*


.. contents::
   :local:
   :depth: 1

Overview
========

The `AWS Lambda <http://aws.amazon.com/lambda/>`_ service makes it easy to create scalable, secure, and highly available backends for your mobile apps without the need to provision or manage infrastructure.

You can create secure logical functions in the cloud that can be called directly from your iOS app. Your AWS Lambda code, written in C#, Node.js, Python, or Java, can implement standalone logic, extend your app to a range of AWS services, and/or connect to services and applications external to AWS.

The availability and cost of a AWS Lambda function automatically scales to amount of traffic it receives. Functions can also be accessed from an iOS app through `Amazon API Gateway <http://aws.amazon.com/lambda/>`_, giving features like global provisioning, enterprise grade monitoring, throttling and control of access.

Setup
=====

This section provides a step-by-step guide for getting started with AWS Lambda using the AWS Mobile SDK for iOS.

#. Install the SDK

   Add the AWS SDK for iOS to your project and import the APIs you need, by following the steps described
   in :ref:`Set Up the AWS SDK for iOS <setup-aws-sdk-for-ios>`.

#. Configure Credentials

   To use Amazon Cognito to create AWS identities and credentials that give your users access to your app's AWS resources, follow the steps described at :doc:`:ref:`Amazon Cognito Setup for iOS <cognito-auth-aws-identity-for-ios>``.

#. Create and Configure a Lamda Function

    #. Sign in to the `AWS Lambda console <https://console.aws.amazon.com/lambda/>`_.

    #. Choose :guilabel:`Create a Lamda function`.

    #. Choose the :guilabel:`Blank Function` template.

       Note that dozens of function templates that connect to other AWS services are available.

    #. Choose :guilabel:`Next`.

       Note that the console allows you to configure triggers for a function from other AWS services, these won't be used in this walkthrough.

    #. Type a :guilabel:`Name` and select `Node.js` as the :guilabel:`Runtime` language.

    #. Under :guilabel:`Lambda function handler and role`, select :guilabel:`Create new role from template(s)`.
       Type a :guilabel:`Role name`. Select the :guilabel:`Policy template` named :guilabel:`Simple Microservice permissions`.

    #. Choose :guilabel:`Next`.

    #. Choose :guilabel:`Create function`.


Invoking an AWS Lambda Function
=================================

The SDK enables you to call AWS Lambda functions from your iOS mobile apps,
using the `AWSLambdaInvoker <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSLambdaInvoker.html>`_ class. When invoked from this SDK, AWS Lambda functions receive
data about the device and the end user identity through client and identity context objects.
To learn more about using these contexts to create rich, and personalized app experiences,
see :ref:`clientContext` and :ref:`identityContext`.

Import AWS Lambda API
----------------------

To use the `lambdainvoker` API, use the following import statement:

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                import AWSLambda

        Objective C
            .. code-block:: objectivec

                #import <AWSLambda/AWSLambda.h>


Call lambdaInvoker
------------------

``AWSLambdaInvoker`` provides a high-level abstraction for AWS Lambda. When ``invokeFunction``
``JSONObject`` is invoked, the JSON object is serialized into JSON data and sent to the
AWS Lambda service. AWS Lambda returns a JSON encoded response that is deserialized into
a JSON object.

A valid JSON object must have the following properties:

* All objects are instances of string, number, array, dictionary or null objects.
* All dictionary keys are instances of string objects.
* Numbers are not ``NaN`` or ``infinity``.

The following is an example of valid request.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let lambdaInvoker = AWSLambdaInvoker.default()
                let jsonObject: [String: Any] = ["key1" : "value1",
                                         "key2" : 2 ,
                                         "key3" : [1, 2],
                                         "isError" : false]

                lambdaInvoker.invokeFunction("myFunction", jsonObject: jsonObject)
                    .continueWith(block: {(task:AWSTask<AnyObject>) -> Any? in
                    if( task.error != nil) {
                        print("Error: \(task.error!)")
                        return nil
                    }

                    // Handle response in task.result
                    return nil
                })


        Objective C
            .. code-block:: objectivec

                AWSLambdaInvoker *lambdaInvoker = [AWSLambdaInvoker defaultLambdaInvoker];

                [[lambdaInvoker invokeFunction:@"myFunction"
                            JSONObject:@{@"key1" : @"value1",
                                         @"key2" : @2,
                                         @"key3" : [NSNull null],
                                         @"key4" : @[@1, @"2"],
                                         @"isError" : @NO}] continueWithBlock:^id(AWSTask *task) {
                    // Handle response
                    return nil;
                }];


Using function returns
----------------------

On successful execution, `task.result` contains a JSON object. For instance, if `myFunctions` returns a dictionary, you can cast the result to a dictionary object as follows.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                if let JSONDictionary = task.result as? NSDictionary {
                    print("Result: \(JSONDictionary)")
                    print("resultKey: \(JSONDictionary["resultKey"])")
                }

        Objective C
            .. code-block:: objectivec

                if (task.result) {
                    NSLog(@"Result: %@", task.result);
                    NSDictionary *JSONObject = task.result;
                    NSLog(@"result: %@", JSONObject[@"resultKey"]);
                }

Handling service execution errors
---------------------------------

On failed AWS Lambda service execution, `task.error` may contain a `NSError` with `AWSLambdaErrorDomain` domain and the following error code.

    * `AWSLambdaErrorUnknown`
    * `AWSLambdaErrorService`
    * `AWSLambdaErrorResourceNotFound`
    * `AWSLambdaErrorInvalidParameterValue`

On failed function execution, `task.error` may contain a `NSError` with `AWSLambdaInvokerErrorDomain` domain and the following error code:

    * `AWSLambdaInvokerErrorTypeUnknown`
    * `AWSLambdaInvokerErrorTypeFunctionError`

When `AWSLambdaInvokerErrorTypeFunctionError` error code is returned, `error.userInfo` may contain a function error from your AWS Lambda function with `AWSLambdaInvokerFunctionErrorKey` key.

The following code shows error handling.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                if let error = task.error as? NSError {
                    if (error.domain == AWSLambdaInvokerErrorDomain) && (AWSLambdaInvokerErrorType.functionError == AWSLambdaInvokerErrorType(rawValue: error.code)) {
                        print("Function error: \(error.userInfo[AWSLambdaInvokerFunctionErrorKey])")
                    } else {
                        print("Error: \(error)")
                    }
                    return nil
                }

        Objective C
            .. code-block:: objectivec

                if (task.error) {
                    NSLog(@"Error: %@", task.error);
                    if ([task.error.domain isEqualToString:AWSLambdaInvokerErrorDomain]
                        && task.error.code == AWSLambdaInvokerErrorTypeFunctionError) {
                        NSLog(@"Function error: %@", task.error.userInfo[AWSLambdaInvokerFunctionErrorKey]);
                    }
                }

Comprehensive example
---------------------

The following code shows invoking an AWS Lambda call and handling returns and errors all together.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let lambdaInvoker = AWSLambdaInvoker.default()

                let jsonObject: [String: Any] = ["key1" : "value1",
                                       "key2" : 2,
                                       "key3" : [1, 2],
                                       "isError" : false]

                lambdaInvoker.invokeFunction("myFunction", jsonObject: jsonObject).continueWith(block: {(task:AWSTask<AnyObject>) -> Any? in
                    if let error = task.error as? NSError {
                        if (error.domain == AWSLambdaInvokerErrorDomain) && (AWSLambdaInvokerErrorType.functionError == AWSLambdaInvokerErrorType(rawValue: error.code) {
                            print("Function error: \(error.userInfo[AWSLambdaInvokerFunctionErrorKey])")
                        } else {
                            print("Error: \(error)")
                        }
                        return nil
                    }

                    // Handle response in task.result
                    if let JSONDictionary = task.result as? NSDictionary {
                        print("Result: \(JSONDictionary)")
                        print("resultKey: \(JSONDictionary["resultKey"])")
                    }
                    return nil
                })

        Objective C
            .. code-block:: objectivec

                AWSLambdaInvoker *lambdaInvoker = [AWSLambdaInvoker defaultLambdaInvoker];

                [[lambdaInvoker invokeFunction:@"myFunction"
                            JSONObject:@{@"key1" : @"value1",
                                         @"key2" : @2,
                                         @"key3" : [NSNull null],
                                         @"key4" : @[@1, @"2"],
                                         @"isError" : @NO}] continueWithBlock:^id(AWSTask *task) {
                    if (task.error) {
                        NSLog(@"Error: %@", task.error);
                        if ([task.error.domain isEqualToString:AWSLambdaInvokerErrorDomain]
                            && task.error.code == AWSLambdaInvokerErrorTypeFunctionError) {
                            NSLog(@"Function error: %@", task.error.userInfo[AWSLambdaInvokerFunctionErrorKey]);
                        }
                    }
                    if (task.result) {
                        NSLog(@"Result: %@", task.result);
                        NSDictionary *JSONObject = task.result;
                        NSLog(@"result: %@", JSONObject[@"resultKey"]);
                    }
                    return nil;
                }];

.. _clientContext:

Client Context
==============

Calls to AWS Lambda using this SDK provide your functions with data about the calling device
and app using the `ClientContext` class.

You can access the client context in your lambda function as follows.

    .. container:: option

        JavaScript
            .. code-block:: javascript

                exports.handler = function(event, context) {
                    console.log("installation_id = " + context.clientContext.client.installation_id);
                    console.log("app_version_code = " + context.clientContext.client.app_version_code);
                    console.log("app_version_name = " + context.clientContext.client.app_version_name);
                    console.log("app_package_name = " + context.clientContext.client.app_package_name);
                    console.log("app_title = " + context.clientContext.client.app_title);
                    console.log("platform_version = " + context.clientContext.env.platform_version);
                    console.log("platform = " + context.clientContext.env.platform);
                    console.log("make = " + context.clientContext.env.make);
                    console.log("model = " + context.clientContext.env.model);
                    console.log("locale = " + context.clientContext.env.locale);

                    context.succeed("Your platform is " + context.clientContext.env.platform;
                }

ClientContext has the following fields:

client.installation_id
        Auto-generated UUID that is created the first time the app is launched. This is stored in the keychain on the device. In case the keychain is wiped a new installation ID will be generated.

client.app_version_code
        `CFBundleShortVersionString <https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-111349>`_

client.app_version_name
        `CFBundleVersion <https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102364>`_

client.app_package_name
        `CFBundleIdentifier <https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102070>`_

client.app_title
        `CFBundleDisplayName <https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-110725>`_

env.platform_version
        `systemVersion <https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/index.html#//apple_ref/occ/instp/UIDevice/systemVersion>`_

env.platform
        `systemName <https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/index.html#//apple_ref/occ/instp/UIDevice/systemName>`_

env.make
        Hardcoded as "apple"

env.model
        `Model of the device <https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/index.html#//apple_ref/occ/instp/UIDevice/model>`_

env.locale
        `localeIdentifier <https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/index.html#//apple_ref/occ/instp/NSLocale/localeIdentifier>`_ from `autoupdatingCurrentLocale <https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSLocale_Class/index.html#//apple_ref/occ/clm/NSLocale/autoupdatingCurrentLocale>`_

.. _identityContext:

Identity Context
================

The `IdentityContext` class of the SDK passes Amazon Cognito credentials making the AWS identity of the end user available to your function. You can access the Identity ID as follows.

    .. container:: option

        JavaScript
            .. code-block:: javascript

                exports.handler = function(event, context) {
                    console.log("clientID = " + context.identity);

                    context.succeed("Your client ID is " + context.identity);
                }

For more about Amazon Cognito in the AWS Mobile SDK for iOS, see :doc:`:ref:`Amazon Cognito Setup for iOS <cognito-auth-aws-identity-for-ios>``.

.. _Cognito Console: https://console.aws.amazon.com/cognito/home
