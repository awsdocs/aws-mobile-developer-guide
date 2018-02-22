.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-add-user-sign-in:


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

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <web-getting-started>`.


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