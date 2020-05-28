.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


.. _reference-mobile-hub-region-overrides:

=========================================
Mobile Hub Project Service Region Hosting
=========================================

.. list-table::
   :widths: 1

   * - **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of `AWS Amplify <https://amzn.to/am-amplify-docs>`__.

       The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI. For existing apps that use AWS Mobile SDK prior to v2.8.0, we highly recommend you migrate your app to use `AWS Amplify <https://amzn.to/am-amplify-docs>`__ and the latest SDK.

The configuration settings of your Mobile Hub project are stored in the AWS US East (Virginia) region.

The AWS services you configure are hosted in the region you select for your project, if they are available in that region. If services are not available in that region, then Mobile hub will host the services in another region.

For more details about regional endpoints, see `AWS Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__.

To understand where services for your project will be hosted, find the region for your project in the following tables.

.. contents:: Select your project's region:
   :depth: 2

US East (Virginia)
------------------

.. csv-table:: If you selected US East (Virginia) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),                   US East (Virginia)
    **Amazon Cognito** (User Sign-in / User File Storage),             US East (Virginia)
    **Amazon DynamoDB** (NoSQL Database),              US East (Virginia)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  US East (Virginia)
    **AWS Lambda** (Cloud Logic),              US East (Virginia)

US East (Ohio)
------------------

.. csv-table:: If you selected US East (Ohio) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         US East (Ohio)
    **Amazon Cognito** (User Sign-in / User File Storage),             US East (Ohio)
    **Amazon DynamoDB** (NoSQL Database),              US East (Ohio)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  US East (Ohio)
    **AWS Lambda** (Cloud Logic),              US East (Ohio)

US West (California)
-------------------

.. csv-table:: If you selected US West (California) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         US West (California)
    **Amazon Cognito** (User Sign-in / User File Storage),             US West (Oregon)
    **Amazon DynamoDB** (NoSQL Database),              US West (California)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  US West (California)
    **AWS Lambda** (Cloud Logic),              US West (California)

US West (Oregon)
----------------

.. csv-table:: If you selected US West (Oregon) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         US West (Oregon)
    **Amazon Cognito** (User Sign-in / User File Storage),             US West (Oregon)
    **Amazon DynamoDB** (NoSQL Database),              US West (Oregon)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  US West (Oregon)
    **AWS Lambda** (Cloud Logic),              US West (Oregon)

EU West (Ireland)
-----------------

.. csv-table:: If you selected EU West (Ireland) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         EU West (Ireland)
    **Amazon Cognito** (User Sign-in / User File Storage),             EU West (Ireland)
    **Amazon DynamoDB** (NoSQL Database),              EU West (Ireland)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  EU West (Ireland)
    **AWS Lambda** (Cloud Logic),              EU West (Ireland)

EU West (London)
----------------

.. csv-table:: If you selected EU West (London) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         EU West (London)
    **Amazon Cognito** (User Sign-in / User File Storage),             EU West (London)
    **Amazon DynamoDB** (NoSQL Database),              EU West (London)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  EU West (London)
    **AWS Lambda** (Cloud Logic),              EU West (London)

EU (Frankfurt)
--------------

.. csv-table:: If you selected West EU (Frankfurt) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         EU (Frankfurt)
    **Amazon Cognito** (User Sign-in / User File Storage),             EU (Frankfurt)
    **Amazon DynamoDB** (NoSQL Database),              EU (Frankfurt)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  EU (Frankfurt)
    **AWS Lambda** (Cloud Logic),              EU (Frankfurt)

Asia Pacific (Tokyo)
--------------------

.. csv-table:: If you selected Asia Pacific (Tokyo) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         Asia Pacific (Tokyo)
    **Amazon Cognito** (User Sign-in / User File Storage),             Asia Pacific (Tokyo)
    **Amazon DynamoDB** (NoSQL Database),              Asia Pacific (Tokyo)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  Asia Pacific (Tokyo)
    **AWS Lambda** (Cloud Logic),              Asia Pacific (Tokyo)

Asia Pacific (Seoul)
--------------------

.. csv-table:: If you selected Asia Pacific (Seoul) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         Asia Pacific (Seoul)
    **Amazon Cognito** (User Sign-in / User File Storage),             Asia Pacific (Seoul)
    **Amazon DynamoDB** (NoSQL Database),              Asia Pacific (Seoul)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  Asia Pacific (Seoul)
    **AWS Lambda** (Cloud Logic),              Asia Pacific (Seoul)

Asia Pacific (Mumbai)
---------------------

.. csv-table:: If you selected Asia Pacific (Mumbai) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         Asia Pacific (Mumbai)
    **Amazon Cognito** (User Sign-in / User File Storage),             Asia Pacific (Mumbai)
    **Amazon DynamoDB** (NoSQL Database),              Asia Pacific (Mumbai)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  Asia Pacific (Mumbai)
    **AWS Lambda** (Cloud Logic),              Asia Pacific (Mumbai)

Asia Pacific (Singapore)
------------------------

.. csv-table:: If you selected Asia Pacific (Singapore) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         Asia Pacific (Singapore)
    **Amazon Cognito** (User Sign-in / User File Storage),             Asia Pacific (Singapore)
    **Amazon DynamoDB** (NoSQL Database),              Asia Pacific (Singapore)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  Asia Pacific (Singapore)
    **AWS Lambda** (Cloud Logic),              Asia Pacific (Singapore)

Asia Pacific (Sydney)
---------------------

.. csv-table:: If you selected Asia Pacific (Sydney) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         Asia Pacific (Sydney)
    **Amazon Cognito** (User Sign-in / User File Storage),             Asia Pacific (Sydney)
    **Amazon DynamoDB** (NoSQL Database),              Asia Pacific (Sydney)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  Asia Pacific (Sydney)
    **AWS Lambda** (Cloud Logic),              Asia Pacific (Sydney)

South America (São Paulo)
-------------------------

.. csv-table:: If you selected South America (São Paulo) as the preferred region for your project:
   :header: "Hosting for these services:", "Is located in:"
   :widths: 1, 4

    **Amazon API Gateway** (Cloud Logic),         South America (São Paulo)
    **Amazon Cognito** (User Sign-in / User File Storage),             US East (Virginia)
    **Amazon DynamoDB** (NoSQL Database),              South America (São Paulo)
    **Amazon Lex** (Conversational Bots),                 US East (Virginia)
    **Amazon Pinpoint** (Messaging and Analytics),    US East (Virginia)
    **Amazon S3** (User File Storage / Messaging and Hosting),                  US East (Virginia)
    **AWS Lambda** (Cloud Logic),              South America (São Paulo)
