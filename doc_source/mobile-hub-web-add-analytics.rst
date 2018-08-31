
.. _web-add-analytics:


#############
Add Analytics
#############


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

Basic Analytics Backend is Enabled for Your App
===============================================

.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <mobile-hub-web-getting-started>`.

When you complete the AWS Mobile CLI setup and launch your app, anonymized session and device demographics data flows to the AWS analytics backend.

**To send basic app usage analytics to AWS**

Launch your app locally by running:

.. code-block:: bash

   npm start

When you use your app the `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`__  service gathers and visualizes analytics data.

**To view the analytics using the Amazon Pinpoint console**

#. Run :code:`npm start`, :code:`awsmobile run`, or :code:`awsmobile publish --test` at least once.

#. Open your project in the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/>`__.

   .. code-block:: bash

      awsmobile console

#. Choose the :guilabel:`Analytics` icon on the left, to navigate to your project in the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__.

#. Choose :guilabel:`Analytics` on the left.

You should see an up-tick in several graphs.


Add Custom Analytics to Your App
================================

You can configure your app so that `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/>`__ gathers data for custom events that you register within the flow of your code.

**To instrument custom analytics in your app**

In the file containing the event you want to track, add the following import:

.. code-block:: java

    import { Analytics } from 'aws-amplify';

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

#. Save the changes and run :code:`npm start`, :code:`awsmobile run`, or :code:`awsmobile publish --test` to launch your app. Use your app so that tracked events are triggered.

#. In the `Amazon Pinpoint console <https://console.aws.amazon.com/pinpoint/>`__, choose :guilabel:`Events` near the top.

#. Select an event in the :guilabel:`Event` dropdown menu on the left.

Custom event data may take a few minutes to become visible in the console.

Next Steps
==========

Learn more about the analytics in AWS Mobile which are part of the :ref:`Messaging and Analytics <messaging-and-analytics>` feature. This feature uses `Amazon Pinpoint <http://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://aws.github.io/aws-amplify>`__.