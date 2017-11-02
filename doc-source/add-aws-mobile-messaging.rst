.. _add-aws-mobile-messaging:

################################
Add Messaging to Your Mobile App
################################


.. meta::
   :description: Integrate AWS Mobile analytics into your existing mobile app.


.. _add-aws-mobile-messaging-overview:

Messaging
=========


Engage your users more deeply by tying their app usage behavior to messaging campaigns.

When you enable the AWS Mobile Hub :ref:`messaging-and-analytics` feature, your app is registered with the
Amazon Pinpoint service. You can define User Segments and send E-mail, SMS, and :ref:`Push
Notification <add-aws-mobile-push-notifications>` messages to those recipients through the Amazon Pinpoint
console.

Amazon Pinpoint also enables you to gather and visualize your app's :ref:`Analytics
<add-aws-mobile-analytics>`. The metrics you gather can be as simple as session start and stop data,
or you can customize them to show things like how closely actual behavior matches your predicted model.

You can then algorithmically tie messaging campaigns to user behavior. For instance, send a discount
mail to frequent users, or send a push notification that initiates a data sync for users that have
selected a certain category in a feature of your app.


.. _add-aws-mobile-messaging-backend-setup:

Set Up Your Backend
===================


To set up email or SMS as part of a Amazon Pinpoint campaign take the following steps.

To setup your app to receive Push Notifications from Amazon Pinpoint, see
:ref:`add-aws-mobile-push-notifications`

#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the
   integration steps on this page.

#. Use AWS Mobile Hub to deploy and configure your AWS services in minutes.


   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create
      project`.

      Or select an existing project.

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
         <messages.html#messages-email>`_.

   #. **For SMS**: Choose the :guilabel:`Messaging and Analytics` tile to enable the
      feature.


      #. Choose :guilabel:`SMS`, and then choose :guilabel:`Enable`.

      #. Choose the the :guilabel:`Amazon Pinpoint console` link at the bottom of the descriptive
         text on the left.

      #. Choose :guilabel:`SMS` in the Amazon Pinpoint console :guilabel:`Channels` tab.

      #. Adjust the options for :guilabel:`Default message type`, :guilabel:`Account spend limit`,
         and :guilabel:`Default sender ID`. For more information on these options, see `Updating SMS
         Settings <channels-sms-manage.html#channels-sms-manage-settings>`_.

      #. For information about sending SMS messages from Amazon Pinpoint, see `Sending an SMS Message
         <messages.html#messages-sms>`_.


.. _add-aws-mobile-messaging-app:

Add the SDK to Your App
=======================


The AWS Mobile SDK is not required to receive Email or SMS messages from Amazon Pinpoint.



