.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _react-native-getting-started:

###########
Get Started
###########


.. meta::
    :description:
        Learn how to use React Native and |AMHlong| to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. toctree::
     :titlesonly:
     :maxdepth: 1
     :hidden:

     Add Analytics <react-native-add-analytics>
     Add User Sign-in <react-native-add-user-sign-in>
     Add NoSQL Database <react-native-access-databases>
     Add User Data Storage <react-native-add-storage>
     Add Cloud Logic <react-native-access-apis>


.. _react-native-getting-started_overview:

Overview
========

The AWS Mobile CLI provides a command line experience that allows frontend JavaScript developers to quickly create and integrate AWS backend resources into their mobile apps.

.. _react-native-getting-started_prerequisites:

Prerequisites
=============

#. `Sign up for the AWS Free Tier <https://aws.amazon.com/free/>`_ to learn and prototype at little or no cost.

#. Install `Node.js <https://nodejs.org/en/download/>`_ with NPM.

#. Install the AWS Mobile CLI

   .. code-block:: bash

       npm install --global awsmobile-cli

#. Configure the CLI with your AWS credentials

   To setup permissions for the toolchain used by the CLI, run:

   .. code-block:: bash

      awsmobile configure

   If prompted for credentials, follow the steps provided by the CLI. For more information, see :ref:`Provide IAM credentials to AWS Mobile CLI <aws-mobile-cli-credentials>`.


.. _react-native-getting-started-create-or-integrate:

Set Up Your Backend
===================

.. list-table::
   :widths: 1

   * - Need to create a quick sample React Native app? See `Create a React Native App <https://facebook.github.io/react-native/docs/getting-started.html>`_.

**To configure backend features for your app**

#. In the root folder of your app, run:

   .. code-block:: bash

        awsmobile init

   The :code:`init` command creates a backend project for your app. By default, analytics and web hosting are enabled in your backend and this configuration is automatically pulled into your app when you initialize.

#. When prompted, provide the source directory for your project. The CLI will generate :file:`aws-exports.js` in this location. This file contains the configuration and endpoint metadata used to link your frontend to your backend services.

   .. code-block:: bash

      ? Where is your projects's source directory:  /


   Then respond to further prompts with the following values.

   .. code-block:: bash

      Please tell us about your project:
      ? Where is your project's source directory:  /
      ? Where is your project's distribution directory that stores build artifacts:  build
      ? What is your project's build command:  npm run-script build
      ? What is your project's start command for local test run:  npm run-script start

 .. _react-native-getting-started-configure-aws-amplify:

Connect to Your Backend
=======================


AWS Mobile uses the open source `AWS Amplify library <https://github.com/aws/aws-amplify>`_ to link your code to the AWS features configured for your app.

**To connect the app to your configured AWS services**

#. Install AWS Amplify for React Native library.

   .. code-block:: bash

       npm install --save aws-amplify


#. In :file:`App.js` (or in other code that runs at launch-time), add the following imports.

   .. code-block:: javascript

        import Amplify from 'aws-amplify';

        import aws_exports from './YOUR-PATH-TO/aws-exports';

#. Then add the following code.

   .. code-block:: javascript

        Amplify.configure(aws_exports);


Run Your App Locally
--------------------

Your app is now ready to launch and use the default services configured by AWS Mobile.

**To launch your app locally**

Use the command native to the React Native tooling you are using. For example, if you made your app using :code:`create-react-native-app` then run:

.. code-block:: bash

    npm run android

    # OR

    npm run ios

Anytime you launch your app, :ref:`app usage analytics are gathered and can be visualized<react-native-add-analytics>` in an AWS console.

.. list-table::
   :widths: 1 6

   * - AWS Free Tier

     - Initializing your app or adding features through the CLI will cause AWS services to be configured on your behalf. The `pricing for AWS Mobile services <http://aws.amazon.com/mobile/pricing>`_ enables you to learn and prototype at little or no cost using the `AWS Free Tier <http://aws.amazon.com/free>`_.


.. _react-native-getting-started-deploying-and-testing:

Next Steps
==========

.. _react-native-getting-started-add-features:

Add Features
------------

Add the following AWS Mobile features to your mobile app using the CLI.

    * :ref:`Analytics <react-native-add-analytics>`

    * :ref:`User Sign-in <react-native-add-user-sign-in>`

    * :ref:`NoSQL Database <react-native-access-databases>`

    * :ref:`User Data Storage <react-native-add-storage>`

    * :ref:`Cloud Logic <react-native-access-apis>`

Learn more
----------

To learn more about the commands and usage of the AWS Mobile CLI, see the :ref:`AWS Mobile CLI reference<aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://aws.github.io/aws-amplify>`_.


