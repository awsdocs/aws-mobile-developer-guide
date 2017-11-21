.. _react-native-add-analytics:


#############
Add Analytics
#############


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.


.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <react-native-getting-started>`.

Basic Analytics Backend is Enabled for Your App
===============================================

When you complete the AWS Mobile CLI setup and launch your app, anonymized session and device demographics data flows to the AWS analytics backend.

**To send basic app usage analytics to AWS**

Launch your app locally by running:

.. code-block:: bash

   npm run android

   # Or

   npm run ios

When you use your app the `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`_  service gathers and visualizes analytics data.

**To view the analytics using the Amazon Pinpoint console**

#. Run :code:`npm start` or :code:`awsmobile run` at least once.

#. Open your project in the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`_.

   .. code-block:: bash

      awsmobile console

#. Choose the :guilabel:`Analytics` icon on the left, to navigate to your project in the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`_.

#. Choose :guilabel:`Analytics` on the left.

You should see an up-tick in several graphs.


Add Custom Analytics to Your App
================================

You can configure your app so that `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`_ gathers data for custom events that you register within the flow of your code.

**To instrument custom analytics in your app**

In the file containing the event you want to track, add the following import:

.. code-block:: java

    import { Analytics } from 'aws-amplify-react-native';

Add the a call like the following to the spot in your JavaScript where the tracked event should be fired:

.. code-block:: javascript

   componentDidMount() {
      Analytics.record('FIRST-EVENT-NAME');
   }

Or to relevant page elements:

.. code-block:: html

    handleClick = () => {
         Analytics.record('SECOND-EVENT-NAME');
    }

    <button onClick={this.handleClick}>Call request</button>

To test:

#. Save the changes and run :code:`npm start` or :code:`awsmobile run` to launch your app. Use your app so that tracked events are triggered.

#. In the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`_, choose :guilabel:`Events` near the top.

#. Select an event in the :guilabel:`Event` dropdown menu on the left.

Custom event data may take a few minutes to become visible in the console.

Next Steps
==========

Learn more about the analytics in AWS Mobile which are part of the :ref:`Messaging and Analytics <messaging-and-analytics>` feature. This feature uses `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`_.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about the `AWS Amplify for React Native library <https://aws.github.io/aws-amplify>`_.
