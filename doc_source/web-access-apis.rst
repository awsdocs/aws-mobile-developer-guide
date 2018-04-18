.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-access-apis:

################
Access Your APIs
################


.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <web-getting-started>`.


The AWS Mobile CLI and Amplify library make it easy to create and call cloud APIs and their handler logic from your JavaScript.


Set Up Your Backend
===================

Create Your API
---------------

In the following examples you will create an API that is part of a cloud-enabled number guessing app. The CLI will create a serverless handler for the API behind the scenes.

**To enable and configure an API**

#. In the root folder of your app, run:

   .. code:: bash

        awsmobile cloud-api enable --prompt


#. When prompted, name the API :userinput:`Guesses`.

   .. code:: bash

        ? API name: Guesses

#. Name a HTTP path :userinput:`/number`. This maps to a method call in the API handler.

   .. code:: bash

      ? HTTP path name (/items): /number

#. Name your Lambda API handler function :userinput:`guesses`.

   .. code:: bash

        ? Lambda function name (This will be created if it does not already exists): guesses

#. When prompted to add another HTTP path, type :userinput:`N`.

   .. code:: bash

        ? Add another HTTP path (y/N): N

#. The configuration for your Guesses API is now saved locally. Push your configuration to the cloud.

   .. code:: bash

        awsmobile push

**To test your API and handler**

From the command line, run:

.. code:: bash

    awsmobile cloud-api invoke Guesses GET /number

The Cloud Logic API endpoint for the :code:`Guesses` API is now created.


Customize Your API Handler Logic
--------------------------------

The AWS Mobile CLI has generated a Lambda function to handle calls to the :code:`Guesses` API. It is saved locally in :file:`YOUR-APP-ROOT-FOLDER/awsmobilejs/backend/cloud-api/guesses`.  The :file:`app.js` file in that directory contains the definitions and functional code for all of the paths that are handled for your API.

**To customize your API handler**

#. Find the handler for POST requests on the :code:`/number` path. That line starts with :code:`app.post('number',`. Replace the callback function’s body with the following:

   .. code:: javascript

        # awsmobilejs/backend/cloud-api/guesses/app.js
        app.post('/number', function(req, res) {
          const correct = 12;
          let guess = req.body.guess
          let result = ""

          if (guess === correct) {
            result = "correct";
          } else if (guess > correct) {
            result = "high";
          } else if (guess < correct) {
            result = "low";
          }

          res.json({ result })
        });

#. Push your changes to the cloud.

   .. code:: bash

        awsmobile push

The :code:`Guesses` API handler logic that implements your new number guessing functionality is now deployed to the cloud.

Connect to Your Backend
=======================

The examples in this section show how you would integrate AWS Amplify library calls using React (see the `AWS Amplify documentation <https://aws.github.io/aws-amplify/>`__ to use other flavors of Javascript).

The following simple component could be added to a :code:`create-react-app` project to present the number guessing game.

.. list-table::
   :widths: 1

   * - .. code:: javascript

          // Number guessing game app example

          # src/GuessNumber.js

          class GuessNumber extends React.Component {
            state = { answer: null };

            render() {
              let prompt = ""
              const answer = this.state.answer

              switch (answer) {
                case "lower":
                  prompt = "Incorrect. Guess a lower number."
                case "higher":
                  prompt = "Incorrect. Guess a higher number."
                case "correct":
                  prompt = `Correct! The number is ${this.refs.guess.value}!`
                default:
                  prompt = "Guess a number between 1 and 100."
              }

              return (
                <div style={styles}>
                  <h1>Guess The Number</h1>
                  <p>{ prompt }</p>

                  <input ref="guess" type="text" />
                  <button type="submit">Guess</button>
                </div>
              )

            }
          }

          let styles = {
            margin: "0 auto",
            width: "30%"
          };

          export default GuessNumber;

Make a Guess
------------

The :code:`API` module from AWS Amplify allows you to send requests to your Cloud Logic APIs right from your JavaScript application.

**To make a RESTful API call**

#. Import the :code:`API` module from :code:`aws-amplify` in the :code:`GuessNumber` component file.

   .. code:: javascript

        import { API } from 'aws-amplify';

#. Add the :code:`makeGuess` function. This function uses the :code:`API` module’s :code:`post` function to submit a guess to the Cloud Logic API.

   .. code:: javascript

        async makeGuess() {
          const guess = parseInt(this.refs.guess.value);
          const body = { guess }
          const { result } = await API.post('Guesses', '/number', { body });
          this.setState({
            guess: result
          });
        }

#. Change the Guess button in the component’s :code:`render` function to invoke the :code:`makeGuess` function when it is chosen.

   .. code:: javascript

       <button type="submit" onClick={this.makeGuess.bind(this)}>Guess</button>

Open your app locally and test out guessing the number by running :code:`awsmobile run`.


Your entire component should look like the following:

.. list-table::
   :widths: 1

   * - .. code:: javascript

          // Number guessing game app example

          import React from 'react';
          import { API } from 'aws-amplify';

          class GuessNumber extends React.Component {
            state = { guess: null };

            async makeGuess() {
              const guess = parseInt(this.refs.guess.value, 10);
              const body = { guess }
              const { result } = await API.post('Guesses', '/number', { body });
              this.setState({
                guess: result
              });
            }

            render() {
              let prompt = ""

              switch (this.state.guess) {
                case "high":
                  prompt = "Incorrect. Guess a lower number.";
                  break;
                case "low":
                  prompt = "Incorrect. Guess a higher number.";
                  break;
                case "correct":
                  prompt = `Correct! The number is ${this.refs.guess.value}!`;
                  break;
                default:
                  prompt = "Guess a number between 1 and 100.";
              }

              return (
                <div style={styles}>
                  <h1>Guess The Number</h1>
                  <p>{ prompt }</p>

                  <input ref="guess" type="text" />
                  <button type="submit" onClick={this.makeGuess.bind(this)}>Guess</button>
                </div>
              )

            }
          }

          let styles = {
            margin: "0 auto",
            width: "30%"
          };

          export default GuessNumber;

Next Steps
----------

-  Learn how to retrieve specific items and more with the `API module in AWS
   Amplify <https://aws.github.io/aws-amplify/media/developer_guide.html>`__.

-  Learn how to enable more features for your app with the `AWS Mobile CLI <https://aws.github.io/aws-amplify>`__.

-  Learn more about what happens behind the scenes, see `Set up Lambda and API Gateway <https://alpha-docs-aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html>`__.
