.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. highlight:: java

.. _how-to-android-kinesis-data-stream:

#######################################
Android: Process Data Streams with |AK|
#######################################

Overview
========

|AKlong|_ is a fully managed service for real-time processing of streaming data at massive scale.
|AK| can collect and process hundreds of terabytes of data per hour from hundreds of thousands of
sources, so you can write applications that process information in real-time. With |AK|
applications, you can build real-time dashboards, capture exceptions and generate alerts, drive
recommendations, and make other real-time business or operational decisions. You can also easily
send data to other services such as |S3long|, |DDBlong|, and |RSlong|.

The |sdk-android| provides simple, high-level clients designed to help you interface with |AK|. The
Kinesis clients let you store streaming data on disk and then send them all at once.  This is useful
because many mobile applications that use Kinesis will create multiple data requests per second.
Sending one data request for each action could adversely impact battery life. Moreover, the requests
could be lost if the device goes offline. Thus, using the high-level Kinesis client for batching can
preserve both battery life and data.

For information about Kinesis Region availability, see  `AWS Service Region Availability
<http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`__.

To get started using the Amazon Kinesis mobile client, you'll need to integrate the SDK for Android
into your app, set the appropriate permissions, and import the necessary libraries.


What is |AKF|?
--------------

|AKFlong|_ is a fully managed service for delivering real-time streaming data to destinations such
as |S3| and |RS|. With |AKF|, you do not need to write any applications or manage any resources. You
configure your data producers to send data to Firehose and it automatically delivers the data to the
destination that you specified.

:guilabel:`KinesisFirehoseRecorder` is the high level client for |AKF|. Its usage is very similar to
that of :guilabel:`KinesisRecorder`.

For more information about |AKF|, see `Amazon Kinesis Firehose
<http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html>`__.

You can also learn more about how the Kinesis services work together on the following page: `Amazon
Kinesis services <http://aws.amazon.com/kinesis/>`__.

.. _kinesis-getting-started:

Getting Started
===============

Create an Identity Pool
-----------------------

To use AWS services in your mobile application, you must obtain AWS Credentials using |COGID| as
your credential provider. Using a credentials provider allows you to access AWS services without
having to embed your private credentials in your application. This also allows you to set
permissions to control which AWS services your users have access to.

The identities of your application's users are stored and managed by an identity pool, which is a
store of user identity data specific to your account. Every identity pool has roles that specify
which AWS resources your users can access. Typically, a developer will use one identity pool per
application. For more information on identity pools, see the `Cognito Developer Guide
<http://docs.aws.amazon.com/cognito/devguide/identity/identity-pools/>`__.

To create an identity pool for your application:

#. Log in to the :console:`Cognito Console <cognito>` and click :guilabel:`Create new identity
   pool`.

#. Enter a name for your Identity Pool and check the checkbox to enable access to unauthenticated
   identities. Click :guilabel:`Create Pool` to create your identity pool.

#. Click :guilabel:`Allow` to create the roles associated with your identity pool.

The next page displays code that creates a credentials provider so you can easily integrate |COGID|
in your Android application.

For more information on Cognito Identity, see :doc:`how-to-cognito-integrate-an-existing-identity-pool`.

Set IAM Permissions (Amazon Kinesis)
------------------------------------

To use Amazon Kinesis in an application, you must set the correct permissions. The following IAM
policy allows the user to submit records to a Kinesis stream identified by :aws-gr:`ARN
<aws-arns-and-namespaces>`:

.. code-block:: json

    {
        "Statement": [{
            "Effect": "Allow",
            "Action": "kinesis:PutRecords",
            "Resource": "arn:aws:kinesis:us-west-2:111122223333:stream/mystream"
        }]
    }

This policy should be applied to roles assigned to the Cognito identity pool, but you need to
replace the :code:`Resource` value with the correct ARN for your Kinesis stream. You can apply
policies at the `IAM console <https://console.aws.amazon.com/iam/>`__.


Set IAM Permissions (Amazon Kinesis Firehose)
---------------------------------------------

Amazon Kinesis Firehose needs slightly different permission. The following IAM policy allows the
user to submit records to an Amazon Kinesis Firehose stream identified by the Amazon Resource Name
(ARN):

.. code-block:: json

    {
        "Statement": [{
            "Effect": "Allow",
            "Action": "firehose:PutRecordBatch",
            "Resource": "arn:aws:firehose:us-west-2:111122223333:deliverystream/mystream"
        }]
    }

For more information about ARN formatting and example policies, see `Amazon Resource Names for
Amazon Kinesis
<http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-iam.html#kinesis-using-iam-arn-format>`__.

To learn more about Kinesis-specific policies, see
`Controlling Access to Amazon Kinesis Resources with IAM
<http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-iam.html>`__.

To learn more about IAM policies, see `Using IAM
<http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html>`__.

Include the SDK in Your Project
-------------------------------

Follow the instructions on the `Set Up the SDK for Android
<http://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/setup.html>`__ page to include the
proper JAR files for this service and set the appropriate permissions.

Set Permissions in Your Android Manifest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your :file:`AndroidManifest.xml` file, add the following permission:

.. code-block:: java

    <uses-permission android:name="android.permission.INTERNET" />

Add Import Statements
~~~~~~~~~~~~~~~~~~~~~

Add the following imports to the main activity of your app.

.. code-block:: java

    import com.amazonaws.mobileconnectors.kinesis.kinesisrecorder.*;
    import com.amazonaws.auth.CognitoCachingCredentialsProvider;
    import com.amazonaws.regions.Regions;

Instantiate a Kinesis Recorder
==============================

Once you've imported the necessary libraries and have your credentials object, you can instantiate :code:`KinesisRecorder`. :code:`KinesisRecorder` is a high-level client meant for storing PutRecord requests on an Android device. Storing requests on the device lets you retain data when the device is offline, and it can also increase performance and battery efficiency since the network doesn't need to be awakened as frequently.

.. note:: :code:`KinesisRecorder` uses synchronous calls, so you shouldn't call :code:`KinesisRecorder` methods on the main thread.

When you create the :code:`KinesisRecorder` client, you'll pass in a directory and an AWS region. The directory should be empty the first time you instantiate :code:`KinesisRecorder`; it should be private to your application; and, to prevent collision, it should be used only by :code:`KinesisRecorder`.  The following snippet creates a directory and instantiates the :code:`KinesisRecorder` client, passing in a Cognito credentials object (:code:`cognitoProvider`), a region enum, and the directory.

.. container:: option

   Android - Java
      .. code-block:: java

         String kinesisDirectory = "YOUR_UNIQUE_DIRECTORY";
         KinesisRecorder recorder = new KinesisRecorder(
           myActivity.getDir(kinesisDirectory, 0),
           Regions.US_WEST_2,
           credentialsProvider
         );

      You'll use :code:`KinesisRecorder` to save records and then send them in a batch.

      .. code-block:: java

         recorder.saveRecord("MyData".getBytes(),"MyStreamName");
         recorder.submitAllRecords();

      .. note:: For the :code:`saveRecord()` request above to work, you would have to have created a stream named :guilabel:`MyStreamName`. You can create new streams in the `Amazon Kinesis console <https://console.aws.amazon.com/kinesis>`__.

      If :code:`submitAllRecords()` is called while the app is online, requests will be sent and removed from the disk. If :code:`submitAllRecords()` is called while the app is offline, requests will be kept on disk until :code:`submitAllRecords()` is called while online. This applies even if you lose your internet connection midway through a submit. So if you save ten requests, call :code:`submitAllRecords()`, send five, and then lose the Internet connection, you have five requests left on disk. These remaining five will be sent the next time :code:`submitAllRecords()` is invoked online.

      To see how much space the :code:`KinesisRecorder` client is allowed to use, you can call :code:`getDiskByteLimit()`.

      .. code-block:: java

         Long byteLimit = recorder.getDiskByteLimit();
         // Do something with byteLimit

      Alternatively, you can retrieve the same information by getting the :code:`KinesisRecorderConfig` object for the recorder and calling :code:`getMaxStorageSize():`

      .. code-block:: java

         KinesisRecorderConfig kinesisRecorderConfig = recorder.getKinesisRecorderConfig();
         Long maxStorageSize = kinesisRecorderConfig.getMaxStorageSize();
         // Do something with maxStorageSize

   Android - Kotlin
      .. code-block:: kotlin

         val recorder = KinesisRecorder(
                    myActivity.getDir("YOUR_UNIQUE_DIRECTORY", 0),
                    Regions.US_WEST_2,
                    credentialsProvider)

      You'll use :code:`KinesisRecorder` to save records and then send them in a batch.

      .. code-block:: kotlin

         recorder.saveRecord("MyData".getBytes(), "MyStreamName")
         recorder.submitAllRecords()

      .. note:: For the :code:`saveRecord()` request above to work, you would have to have created a stream named :guilabel:`MyStreamName`. You can create new streams in the `Amazon Kinesis console <https://console.aws.amazon.com/kinesis>`__.

      If :code:`submitAllRecords()` is called while the app is online, requests will be sent and removed from the disk. If :code:`submitAllRecords()` is called while the app is offline, requests will be kept on disk until :code:`submitAllRecords()` is called while online. This applies even if you lose your internet connection midway through a submit. So if you save ten requests, call :code:`submitAllRecords()`, send five, and then lose the Internet connection, you have five requests left on disk. These remaining five will be sent the next time :code:`submitAllRecords()` is invoked online.

      To see how much space the :code:`KinesisRecorder` client is allowed to use, you can call :code:`getDiskByteLimit()`.

      .. code-block:: kotlin

         val byteLimit = recorder.diskByteLimit
         // Do something with byteLimit

      Alternatively, you can retrieve the same information by getting the :code:`KinesisRecorderConfig` object for the recorder and calling :code:`getMaxStorageSize():`

      .. code-block:: kotlin

         val maxStorageSize = recorder.kinesisRecorderConfig.maxStorageSize
         // Do something with maxStorageSize

Storage limits
--------------

If you exceed the storage limit for :code:`KinesisRecorder`, requests will not be saved or sent. :code:`KinesisRecorderConfig` has a default :code:`maxStorageSize` of 8 MiB. You can configure the maximum allowed storage via the :code:`withMaxStorageSize()` method of :code:`KinesisRecorderConfig`.

To check the number of bytes currently stored in the directory passed in to the :code:`KinesisRecoder` constructor, call :code:`getDiskBytesUsed()`:

.. container:: option

   Android - Java
      .. code-block:: java

         Long bytesUsed = recorder.getDiskBytesUsed();
         // Do something with bytesUsed

   Android - Kotlin
      .. code-block:: kotlin

         val bytesUsed = recorder.diskBytesUsed
         // Do something with bytesUsed

To learn more about working with Amazon Kinesis, see `Amazon Kinesis Developer Resources <http://aws.amazon.com/kinesis/developer-resources/>`__. To learn more about the Kinesis classes, see the `API Reference for the Android SDK <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/>`__.


Use KinesisFirehoseRecorder
===========================

To use :code:`KinesisFirehoseRecorder`, you need to pass the object in a directory where streaming data is saved. We recommend you use an app private directory because the data is not encrypted.

.. container:: option

   Android - Java
      .. code-block:: java

         // Gets a working directory for the recorder
         File directory = context.getCachedDir();
         // Sets Firehose region
         Regions region = Regions.US_WEST_2;
         // Initialize a credentials provider to access Amazon Kinesis Firehose
         AWSCredentialsProvider provider = new CognitoCachingCredentialsProvider(
              context, "identityPoolId",
              Regions.US_EAST_1); // region of your Amazon Cognito identity pool
         KinesisFirehoseRecorder firehoseRecorder = new KinesisFirehoseRecorder(
              directory, region, provider);

         // Start to save data, either a String or a byte array
         firehoseRecorder.saveRecord("Hello world!\n");
         firehoseRecorder.saveRecord("Streaming data to Amazon S3 via Amazon Kinesis Firehose is easy.\n");

         // Send previously saved data to Amazon Kinesis Firehose
         // Note: submitAllRecords() makes network calls, so wrap it in an AsyncTask.
         new AsyncTask<Void, Void, Void>() {
             @Override
             protected Void doInBackground(Void... v) {
                 try {
                     firehoseRecorder.submitAllRecords();
                 } catch (AmazonClientException ace) {
                     // handle error
                 }
             }
         }.execute();

   Android - Kotlin
      .. code-block:: kotlin

         val firehose = KinesisFirehoseRecorder(
            context.getCachedDir(),     // Working directory for recorder
            Regions.US_WEST_2,          // Region that Kinesis is provisioned in
            credentialsProvider)        // AWS Credentials provider

         // Start to save data, either a String or a byte array
         firehose.saveRecord("Hello world!\n");
         firehose.saveRecord("Streaming data to Amazon S3 via Amazon Kinesis Firehose is easy.\n");

         // Send previously saved data to Amazon Kinesis Firehose
         // Note: submitAllRecords() makes network calls.
         thread(start = true) {
            try {
                firehose.submitAllRecords()
            } catch (ex: AmazonClientException) {
                Log.e(TAG, "Error submitting records")
            }
         }

To learn more about working with Amazon Kinesis Firehose, see `Amazon Kinesis Firehose <http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html>`__.

To learn more about the Kinesis Firehose classes, see the `API Reference for the Android SDK <http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/>`__.

