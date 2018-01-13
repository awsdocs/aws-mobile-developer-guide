.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _messaging-and-analytics:

#######################
Messaging and Analytics
#######################


.. meta::
   :description: Use the Messaging and Analytics mobile backend feature to measure user behavior and
      engage with user segments through push notification, SMS, or e-mail.


Choose the |AMHlong| Messaging and Analytics feature to:


* Gather data to understand your app users' behavior


* Use that information to add campaigns to engage with your users through push notification, e-mail,
  and SMS

`Create a free Mobile Hub project and add the Messaging and
Analytics feature. <https://console.aws.amazon.com/mobilehub/home#/>`_

.. _messaging-and-analytics-details:

Feature Details
===============


|AMHlong| Messaging and Analytics (formerly User Engagement) helps you understand how your users use
your app. It enables you to engage them through push notification, e-mail, or SMS. You can tie your
analytics to your messaging so that what you communicate flows from users' behavior.

The following image shows Messaging and Analytics using `Amazon Pinpoint
<http://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html>`_ to collect usage data from a mobile app. Amazon Pinpoint then
sends messaging to selected app users based on the campaign logic designed for the app.

.. image:: images/diagram-abstract-messaging-and-analytics.png

You can configure messaging and analytics functions separately, or use the two together to carry out
campaigns to interact with your users based on the their app usage. You can configure which users
receive a campaign's messaging, as well as the conditions and scheduling logic for sending messages.
You can configure notifications to communicate text or cause a programatic action, such as opening
an application or passing custom JSON to your client.

When you choose :guilabel:`Analytics`, Amazon Pinpoint performs capture, visualization, and analysis of
app usage and campaign data:


* By default, Amazon Pinpoint gathers app usage session data.

* If you configure a campaign, metrics about your campaign are included.

* If you add custom analytics to your app, you can configure Amazon Pinpoint to visualize those metrics
  and use the data as a factor in your campaign behavior. To learn more about integrating custom
  analytics, see `Integrating Amazon Pinpoint With Your App <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-sdk.html>`_ in the
  :title:`Amazon Pinpoint User Guide`.

* Amazon Pinpoint enables you to construct `funnel analytics <http://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-funnels.html>`_, which visualize
  how many users complete each of a series of step you intend them to take in your app.

* To perform more complex analytics tasks, such as merging data from more than one app or making
  flexible queries, you can configure Amazon Pinpoint to stream your data to |AK|. To learn more about
  using Amazon Pinpoint and |AK| together, see `Streaming Amazon Pinpoint Events to Amazon Kinesis
  <http://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-streaming-kinesis.html>`_.

When you choose :guilabel:`Messaging` you can configure your project to enable Amazon Pinpoint to send:


* Send Push Notifications to your Android users, through Firebase/Google Cloud Messaging, or iOS,
  through APNs

* E-mails to your app users using the sender ID and domain of your choice

* SMS messages

Once you have enabled Messaging and Analytics options in your |AMH| project, use the `Amazon
Pinpoint console <https://console.aws.amazon.com/pinpoint/home>`_ to view visualizations of your analytics or configure your user
segments and campaigns. You can also import user segment data into Amazon Pinpoint to use campaigns for
any group of users.


.. _messaging-and-analytics-ataglance:

Messaging and Analytics At a Glance
===================================


.. list-table::
   :widths: 1 6

   * - **AWS services and resources configured**

     - - **Amazon Pinpoint** (see `Amazon Pinpoint Developer Guide <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_)

         `Concepts <http://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html>`_ | `Console <https://console.aws.amazon.com/pinpoint/home>`_

       |AMH|-enabled features use |COG| for authentication and |IAM| for authorization. For more information, see :ref:`User Sign-in <user-sign-in>`.

   * - **Configuration options**

     - This feature enables the following mobile backend capabilities:

       - Gather and visualize analytics of your app users' behavior.

         - Integrate Amazon Pinpoint user engagement campaigns into your mobile app.

         - Communicate to app users using push notifications through APNs, GCM, and FCM.

           - via :guilabel:`Firebase or Google Cloud Messaging (FCM/GCM)` (see `Setting Up Android Push Notifications <http://docs.aws.amazon.com/pinpoint/latest/developerguide/mobile-push-android.html>`_)

           - via :guilabel:`Apple Push Notification service (APNs)` (see `Setting Up iOS Push Notifications <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/push-notifications-details.html#config-push-notifications>`_)

           For more information, see `Configuring Push Notification <https://alpha-docs-aws.amazon.com/pinpoint/latest/developerguide/mobile-push.html>`_.

         - Communicate to app users through e-mail.

         - Communicate to app users through SMS.


   * - **Quickstart app demos**

     - This feature adds :guilabel:`User Engagement` functionality to a quickstart app generated by |AMH|:

       - Demonstrate enabling the app user to receive campaign notifications. The app user can cause events that generate session, custom, campaign and purchase data. Analytics for these events is available in the Amazon Pinpoint console in close to real time.

       - Demonstrate providing the app user with a view of an Amazon Pinpoint data visualization, on their mobile phone.
