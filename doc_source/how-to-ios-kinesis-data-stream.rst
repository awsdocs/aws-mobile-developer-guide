.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _kinesis-data-stream-processing-for-ios:

#############################################
ios: Process Data Streams with Amazon Kinesis
#############################################

Overview
========

`Amazon Kinesis <http://aws.amazon.com/kinesis/>`_ is a fully managed service for real-time
processing of streaming data at massive scale. `Amazon Kinesis Firehose
<http://aws.amazon.com/kinesis/firehose/>`_ is a fully managed service for delivering real-time
streaming data to destinations such as Amazon Simple Storage Service (Amazon S3) and Amazon
Redshift. With Firehose, you do not need to write any applications or manage any resources. You
configure your data producers to send data to Firehose and it automatically delivers the data to the
destination that you specified.  The tutorial below explains how to integrate Amazon Kinesis and/or
Amazon Kinesis Firehose with your app.


Setup
=====

Prerequisites
-------------

You must complete all of the instructions on the `Set Up the SDK for Android
<http://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/setup.html>`_ page before beginning
this tutorial.


Initialize KinesisRecorder for Amazon Kinesis
=============================================

Pass your initialized Amazon Cognito credentials provider to the :code:`KinesisRecorder` constructor::

    String kinesisDirectory = "YOUR_UNIQUE_DIRECTORY";
    KinesisRecorder recorder = new KinesisRecorder(
        myActivity.getDir(kinesisDirectory, 0), // An empty directory KinesisRecorder can use for storing requests
        Regions.US_WEST_2,  // Region that this Recorder should save and send requests to
        credentialsProvider); // The credentials provider to use when making requests to AWS


Initialize KinesisFirehoseRecorder for Amazon Kinesis Firehose
==============================================================

Pass your initialized Amazon Cognito credentials provider to the :code:`KinesisFirehoseRecorder` constructor::

    String kinesisFirehoseDirectory = "YOUR_UNIQUE_DIRECTORY";
    KinesisFirehoseRecorder recorder = new KinesisFirehoseRecorder(
        myActivity.getDir(kinesisFirehoseDirectory, 0), /* An empty directory KinesisFirehoseRecorder can use for storing requests */
        Regions.US_WEST_2,  /* Region that this Recorder should save and send requests to */
        credentialsProvider); /* The credentials provider to use when making requests to AWS */


Create a Kinesis Stream
=======================

In order to use the Amazon Kinesis recorder, you must first create an Amazon Kinesis stream. You can
create new streams in the `Kinesis Console`_.


Grant Role Access to Your Amazon Kinesis Stream
===============================================

The default IAM role policy grants you access to Amazon Mobile Analytics and Amazon Cognito Sync. To
use Amazon Kinesis in an application, you must allow the IAM roles associated with your Cognito
Identity Pool access to your Kinesis stream. To set this policy:

#. Navigate to the `Identity and Access Management Console`_ and choose :guilabel:`Roles` in the
   left-hand pane.

#. Type your Identity Pool name into the search box. Two roles will be listed: one for
   unauthenticated users and one for authenticated users.

#. Choose the role for unauthenticated users (it will have "unauth" appended to your Identity Pool
   name).

#. Scroll down the web page until you see the :guilabel:`Create Role Policy`. Choose it, select
   :guilabel:`Policy Generator`, and then choose the :guilabel:`Select` button.

#. Select the :guilabel:`Allow` radio button, Amazon Kinesis in the :guilabel:`AWS Service`
   drop-down, PutRecord under :guilabel:`Actions`, and enter the ARN to your Kinesis stream in the
   :guilabel:`Amazon Resource Name (ARN)` text box.

   ::

    "Resource": arn:aws:kinesis:region:account:stream/name
    "Resource": arn:aws:kinesis:us-west-2:111122223333:stream/my-stream

#. Choose the :guilabel:`Add Statement` button, the :guilabel:`Next Step` button, and the
   :guilabel:`Apply Policy` button.

To learn more about Kinesis-specific policies, see `Controlling Access to Amazon Kinesis Resources
with IAM <http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-iam.html>`_.


Grant Role Access to Your Kinesis Firehose Delivery Stream
==========================================================

The default IAM role policy grants you access to Amazon Mobile Analytics and Amazon Cognito Sync. To
use Kinesis Firehose in an application, you must allow the IAM roles associated with your Amazon
Cognito Identity Pool access to your Kinesis Firehose delivery stream. To set this policy:

#. Navigate to the `Identity and Access Management Console`_ and choose :guilabel:`Roles` in the
   left-hand pane.

#. Type your Identity Pool name into the search box. Two roles will be listed: one for
   unauthenticated users and one for authenticated users.

#. Choose the role for unauthenticated users (it will have "unauth" appended to your Identity Pool
   name).

#. Scroll down the web page until you see the :guilabel:`Create Role Policy`. Choose it, select
   :guilabel:`Policy Generator`, and then choose the :guilabel:`Select` button.

#. Select the :guilabel:`Allow` radio button, Amazon Kinesis in the :guilabel:`AWS Service`
   drop-down, PutRecord under :guilabel:`Actions`, and enter the ARN to your Kinesis stream in the
   :guilabel:`Amazon Resource Name (ARN)` text box.

   ::

    "Resource": arn:aws:firehose:region:account:stream/name
    "Resource": arn:aws:firehose:us-west-2:111122223333:deliverystream/my-stream

#. Choose the :guilabel:`Add Statement` button, the :guilabel:`Next Step` button, and the
   :guilabel:`Apply Policy` button.

To learn more about Kinesis Firehose-specific policies, see `Controlling Access to Amazon Kinesis
Firehose <http://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html>`_.


Configure the Kinesis Service Client
====================================

Use the :code:`KinesisRecorder` class to interact with the Kinesis service. The following snippet
creates an instance of the Kinesis service client::

    String kinesisDirectory = "YOUR_UNIQUE_DIRECTORY";
    KinesisRecorder recorder = new KinesisRecorder(
        myActivity.getDir(kinesisDirectory, 0),
        Regions.US_WEST_2,
        credentialsProvider);

:code:`YOUR_UNIQUE_DIRECTORY` is a folder that should be exclusive to the Kinesis Recorder and will
be used to store records. The region here should match the region you specified in the console.

.. note:: :code:`KinesisRecorder` uses synchronous calls, so you shouldn't call
   :code:`KinesisRecorder` methods on the main thread.


Save Records to Local Storage
=============================

With :code:`KinesisRecorder` created and configured, you can use :code:`saveRecord()` to save
records to local storage::

   recorder.saveRecord("MyData".getBytes(),"MyStreamName");


Submit Records to Kinesis Stream
================================

Use the :code:`submitAllRecords` synchronous method on the :code:`KinesisRecorder` object to send
all locally saved records to your Kinesis stream.

::

       recorder.submitAllRecords();

To learn more about working with Amazon Kinesis, see the `Amazon Kinesis Developer Resources
<http://aws.amazon.com/kinesis/developer-resources/>`_.

To learn more about working with Amazon Kinesis Firehose, see the `Amazon Kinesis Firehose
Documentation <http://aws.amazon.com/documentation/firehose/>`_.

To learn more about the Kinesis classes, see the `class reference for AWSKinesisRecorder
<http://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobileconnectors/kinesis/kinesisrecorder/KinesisRecorder.html>`_.

.. _Cognito Console: https://console.aws.amazon.com/cognito/home
.. _Kinesis Console: https://console.aws.amazon.com/kinesis/home
.. _Kinesis Firehose Console: https://console.aws.amazon.com/firehose/home
.. _Identity and Access Management Console: https://console.aws.amazon.com/iam/home

