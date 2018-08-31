
.. _web-add-user-sign-in:


#######################
Add Auth / User Sign-in
#######################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.


Set Up Your Backend
===================

.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <mobile-hub-web-getting-started>`.

The AWS Mobile CLI components for user authentication include a rich, configurable  UI for sign-up and sign-in.

**To enable the Auth features**

In the root folder of your app, run:

.. code-block:: java

      awsmobile user-signin enable

      awsmobile push

Connect to Your Backend
=======================

The AWS Mobile CLI enables you to integrate ready-made sign-up/sign-in/sign-out UI from the command line.

**To add user auth UI to your app**

#. Install AWS Amplify for React library.

   .. code-block:: bash

       npm install --save aws-amplify-react


#. Add the following import in :file:`App.js` (or other file that runs upon app startup):

   .. code-block:: java

      import { withAuthenticator } from 'aws-amplify-react';

#. Then change :code:`export default App;` to the following.

   .. code-block:: java

      export default withAuthenticator(App);

To test, run :code:`npm start`, :code:`awsmobile run`, or :code:`awsmobile publish --test`.


Next Steps
==========

Learn more about the AWS Mobile :ref:`User Sign-in <user-sign-in>` feature, which uses `Amazon Cognito <http://docs.aws.amazon.com/cognito/latest/developerguide/welcome.html>`__.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://aws.github.io/aws-amplify>`__.