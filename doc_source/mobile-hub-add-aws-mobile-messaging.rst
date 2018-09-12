
.. _mobile-hub-add-aws-mobile-messaging:

#####################################################
Add Messaging to Your Mobile App with Amazon Pinpoint
#####################################################


.. meta::
   :description: Integrate AWS Mobile analytics into your existing mobile app.

.. important::

   The following content applies if you are already using the AWS Mobile Hub to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

.. _mobile-hub-add-aws-mobile-messaging-overview:

Overview
========


Engage your users more deeply by tying their app usage behavior to messaging campaigns.

When you enable the AWS Mobile Hub :ref:`messaging-and-analytics` feature, your app is registered with the
Amazon Pinpoint service. You can define User Segments and send E-mail, SMS, and :ref:`Push
Notification <mobile-hub-add-aws-mobile-push-notifications>` messages to those recipients through the Amazon Pinpoint
console.

Amazon Pinpoint also enables you to gather and visualize your app's :ref:`Analytics
<mobile-hub-add-aws-mobile-analytics>`. The metrics you gather can be as simple as session start and stop data,
or you can customize them to show things like how closely actual behavior matches your predicted model.

You can then algorithmically tie messaging campaigns to user behavior. For instance, send a discount
mail to frequent users, or send a push notification that initiates a data sync for users that have
selected a certain category in a feature of your app.


.. _mobile-hub-add-aws-mobile-messaging-set-up-backend:

Set Up Your Backend
===================

To set up email or SMS as part of a Amazon Pinpoint campaign take the following steps.

To setup your app to receive Push Notifications from Amazon Pinpoint, see
:ref:`mobile-hub-add-aws-mobile-push-notifications`

#. Complete the :ref:`Get Started <mobile-hub-add-aws-mobile-sdk-basic-setup>` steps before your proceed.

#. **For Email**: Choose the :guilabel:`Messaging and Analytics` tile to enable the
      feature.

      #. Choose :guilabel:`Email`, and then choose :guilabel:`Enable`.

      #. Choose the :guilabel:`Amazon Pinpoint console` link at the bottom of the descriptive
         text on the left.

      #. Choose :guilabel:`Email` in the Amazon Pinpoint console :guilabel:`Channels` tab.

      #. Choose :guilabel:`Email address`, type the address your messages should come from, and then
         choose :guilabel:`verify` at the end of the entry field.

         The email account you enter will receive an email requesting your approval for
         Amazon Pinpoint to use that account as the sender address for emails sent by the system. The status of :guilabel:`Pending Verification` is
         displayed in the console entry field until Amazon Pinpoint has processed your approval.

      #. Choose :guilabel:`Email domain`, type the domain your messages should come from, and then
         choose :guilabel:`verify` at the end of the entry field.

         A dialog is displayed providing the name and value of the TXT record you must add to the
         domain's settings. The status of :code:`Pending Verification` is displayed in the entry
         field until the console processes your approval.

         Add a default user name to :guilabel:`Default from address`.

      #. Choose :guilabel:`Save`.

      #. For information about sending mail from Amazon Pinpoint, see `Sending an Email Message
         <https://docs.aws.amazon.com/pinpoint/latest/userguide/messages.html#messages-email>`__.

   #. **For SMS**: Choose the :guilabel:`Messaging and Analytics` tile to enable the
      feature.


      #. Choose :guilabel:`SMS`, and then choose :guilabel:`Enable`.

      #. Choose the :guilabel:`Amazon Pinpoint console` link at the bottom of the descriptive
         text on the left.

      #. Choose :guilabel:`SMS` in the Amazon Pinpoint console :guilabel:`Channels` tab.

      #. Adjust the options for :guilabel:`Default message type`, :guilabel:`Account spend limit`,
         and :guilabel:`Default sender ID`. For more information on these options, see `Updating SMS
         Settings <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-manage.html>`__.

      #. For information about sending SMS messages from Amazon Pinpoint, see `Sending an SMS Message
         <https://docs.aws.amazon.com/pinpoint/latest/userguide/messages.html#messages-sms>`__.


.. _connect-to-your-backend:

Connect to your backend
=======================


The AWS Mobile SDK is not required to receive Email or SMS messages from Amazon Pinpoint.



