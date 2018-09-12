.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-messaging:

#####################################################
Add Messaging to Your Mobile App with Amazon Pinpoint
#####################################################


.. meta::
   :description: Integrate AWS Mobile analytics into your existing mobile app.

.. _add-aws-mobile-messaging-overview:

Overview
========


Engage your users more deeply by tying their app usage behavior to Push Notification, email, or SMS messaging campaigns.

When you enable the Amplify CLI Analytics category, your app is registered with Amazon Pinpoint. You can define user segments and send messages to those recipients through the Amazon Pinpoint console.

Amazon Pinpoint also enables you to gather and visualize your app's :ref:`Analytics
<add-aws-mobile-analytics>`. The metrics you gather can be as simple as session start and stop data,
or you can customize them to show things like how closely actual behavior matches your predicted model.

You can then algorithmically tie messaging campaigns to user behavior. For instance, send a discount
mail to frequent users, or send a push notification that initiates a data sync for users that have
selected a certain category in a feature of your app.


.. _add-aws-mobile-messaging-set-up-backend:

Set Up Your Backend
===================

To set up your app to receive Push Notifications from Amazon Pinpoint, see :ref:`Add Push Notifications to Your Mobile App with Amazon Pinpoint <add-aws-mobile-push-notifications>`.

To set up email or SMS as part of an Amazon Pinpoint campaign perform the following steps.

To set up your app to receive Push Notifications from Amazon Pinpoint, see
:ref:`add-aws-mobile-push-notifications`.

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` and :ref:`Add Analytics <add-aws-mobile-analytics>` steps before you proceed.

#. **For Email**:

   #. In a terminal window, use the following command to open the project for your app by in the Amazon Pinpoint console.

      .. code-block:: none

         $ cd YOUR_APP_PROJECT_FOLDER
         $ amplify console analytics

   #. In the Amazon Pinpoint console, navigate to :guilabel:`Settings` on the left, choose the :guilabel:`Channels` tab, and then choose  :guilabel:`Email`.

   #. Choose the :guilabel:`Enable email channel` check box, choose :guilabel:`Email address`, type the address that you want your messages to come from, and then choose :guilabel:`verify`.

      The email account you enter will receive an email requesting your approval for
      Amazon Pinpoint to use that account as the sender address for emails sent by the system. The status of :guilabel:`Pending Verification` is
      displayed in the console entry field until Amazon Pinpoint has processed your approval.

   #. Choose :guilabel:`Email domain`, type the domain that you want your messages to come from, and then choose :guilabel:`verify`.

      A dialog box displays the name and value of the TXT record you must add to the
      domain's settings. The status of :code:`Pending Verification` is displayed in the entry
      field until the console processes your approval.

      Add a default user name to :guilabel:`Default from address`.

   #. Choose :guilabel:`Save`.

   #. For information about sending mail from Amazon Pinpoint, see `Sending an Email Message
      <https://docs.aws.amazon.com/pinpoint/latest/userguide/messages.html#messages-email>`__.

#. **For SMS**:

   #. In a terminal window, use the following command to open the project for your app by in the Amazon Pinpoint console.

      .. code-block:: none

         $ cd YOUR_APP_PROJECT_FOLDER
         $ amplify console analytics

   #. Navigate to Settings in the left-hand navigation, choose :guilabel:`SMS`, and then choose :guilabel:`Enable SMS channel`.

   #. Navigate to Direct messaging in the left-hand navigation and chose SMS.

   #. Adjust the options for :guilabel:`Default message type`, :guilabel:`Account spend limit`,
      and :guilabel:`Default sender ID`. For more information about these options, see `Updating SMS
      Settings <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-manage.html>`__.

   #. For information about sending SMS messages from Amazon Pinpoint, see `Sending an SMS Message
      <https://docs.aws.amazon.com/pinpoint/latest/userguide/messages.html#messages-sms>`__.


.. _connect-to-your-backend:

Connect to Your Backend
=======================


The AWS Mobile SDK is not required to receive email or SMS messages from Amazon Pinpoint.
