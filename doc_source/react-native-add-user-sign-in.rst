.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _react-native-add-user-sign-in:


#######################
Add Auth / User Sign-in
#######################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <react-native-getting-started>`.


Set Up Your Backend
===================

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

#. Install AWS Amplify for React Nativelibrary.

   .. code-block:: bash

      npm install --save aws-amplify
      npm install --save aws-amplify-react-native

.. list-table::
   :widths: 1 6

   * - **Note**

     - If your react-native app was not created using :code:`create-react-native-app` or using a version of Expo lower than v25.0.0 (the engine behind  :code:`create-react-native-app`), you will need to link libraries in your project for the Auth module on React Native,  :code:`amazon-cognito-identity-js`.

       To link to the module, you must first eject the project:

       .. code-block:: bash

            npm run eject
            react-native link amazon-cognito-identity-js


#. Add the following import in :file:`App.js` (or other file that runs upon app startup):

   .. code-block:: java

      import { withAuthenticator } from 'aws-amplify-react-native';

#. Then change :code:`export default App;` to the following.

   .. code-block:: java

      export default withAuthenticator(App);

To test, run :code:`npm start` or :code:`awsmobile run`.


Next Steps
==========

Learn more about the AWS Mobile :ref:`User Sign-in <user-sign-in>` feature, which uses `Amazon Cognito <http://docs.aws.amazon.com/cognito/latest/developerguide/welcome.html>`_.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://aws.github.io/aws-amplify>`_.

