# Access Your APIs<a name="mobile-hub-web-access-apis"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up Your Backend<a name="set-up-your-backend"></a>

The AWS Mobile CLI and Amplify library make it easy to create and call cloud APIs and their handler logic from your JavaScript\.


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-web-getting-started.md)\.  | 

### Create Your API<a name="create-your-api"></a>

In the following examples you will create an API that is part of a cloud\-enabled number guessing app\. The CLI will create a serverless handler for the API behind the scenes\.

 **To enable and configure an API** 

1. In the root folder of your app, run:

   ```
   awsmobile cloud-api enable --prompt
   ```

1. When prompted, name the API `Guesses`\.

   ```
   ? API name: Guesses
   ```

1. Name a HTTP path `/number`\. This maps to a method call in the API handler\.

   ```
   ? HTTP path name (/items): /number
   ```

1. Name your Lambda API handler function `guesses`\.

   ```
   ? Lambda function name (This will be created if it does not already exists): guesses
   ```

1. When prompted to add another HTTP path, type `N`\.

   ```
   ? Add another HTTP path (y/N): N
   ```

1. The configuration for your Guesses API is now saved locally\. Push your configuration to the cloud\.

   ```
   awsmobile push
   ```

 **To test your API and handler** 

From the command line, run:

```
awsmobile cloud-api invoke Guesses GET /number
```

The Cloud Logic API endpoint for the `Guesses` API is now created\.

### Customize Your API Handler Logic<a name="customize-your-api-handler-logic"></a>

The AWS Mobile CLI has generated a Lambda function to handle calls to the `Guesses` API\. It is saved locally in `YOUR-APP-ROOT-FOLDER/awsmobilejs/backend/cloud-api/guesses`\. The `app.js` file in that directory contains the definitions and functional code for all of the paths that are handled for your API\.

 **To customize your API handler** 

1. Find the handler for POST requests on the `/number` path\. That line starts with `app.post('number',`\. Replace the callback function’s body with the following:

   ```
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
   ```

1. Push your changes to the cloud\.

   ```
   awsmobile push
   ```

The `Guesses` API handler logic that implements your new number guessing functionality is now deployed to the cloud\.

## Connect to Your Backend<a name="connect-to-your-backend"></a>

The examples in this section show how you would integrate AWS Amplify library calls using React \(see the [AWS Amplify documentation](https://aws.github.io/aws-amplify/) to use other flavors of Javascript\)\.

The following simple component could be added to a `create-react-app` project to present the number guessing game\.


|  | 
| --- |
|  <pre>// Number guessing game app example<br /><br /># src/GuessNumber.js<br /><br />class GuessNumber extends React.Component {<br />  state = { answer: null };<br /><br />  render() {<br />    let prompt = ""<br />    const answer = this.state.answer<br /><br />    switch (answer) {<br />      case "lower":<br />        prompt = "Incorrect. Guess a lower number."<br />      case "higher":<br />        prompt = "Incorrect. Guess a higher number."<br />      case "correct":<br />        prompt = `Correct! The number is ${this.refs.guess.value}!`<br />      default:<br />        prompt = "Guess a number between 1 and 100."<br />    }<br /><br />    return (<br />      <div style={styles}><br />        <h1>Guess The Number</h1><br />        <p>{ prompt }</p><br /><br />        <input ref="guess" type="text" /><br />        <button type="submit">Guess</button><br />      </div><br />    )<br /><br />  }<br />}<br /><br />let styles = {<br />  margin: "0 auto",<br />  width: "30%"<br />};<br /><br />export default GuessNumber;</pre>  | 

### Make a Guess<a name="make-a-guess"></a>

The `API` module from AWS Amplify allows you to send requests to your Cloud Logic APIs right from your JavaScript application\.

 **To make a RESTful API call** 

1. Import the `API` module from `aws-amplify` in the `GuessNumber` component file\.

   ```
   import { API } from 'aws-amplify';
   ```

1. Add the `makeGuess` function\. This function uses the `API` module’s `post` function to submit a guess to the Cloud Logic API\.

   ```
   async makeGuess() {
     const guess = parseInt(this.refs.guess.value);
     const body = { guess }
     const { result } = await API.post('Guesses', '/number', { body });
     this.setState({
       guess: result
     });
   }
   ```

1. Change the Guess button in the component’s `render` function to invoke the `makeGuess` function when it is chosen\.

   ```
   <button type="submit" onClick={this.makeGuess.bind(this)}>Guess</button>
   ```

Open your app locally and test out guessing the number by running `awsmobile run`\.

Your entire component should look like the following:


|  | 
| --- |
|  <pre>// Number guessing game app example<br /><br />import React from 'react';<br />import { API } from 'aws-amplify';<br /><br />class GuessNumber extends React.Component {<br />  state = { guess: null };<br /><br />  async makeGuess() {<br />    const guess = parseInt(this.refs.guess.value, 10);<br />    const body = { guess }<br />    const { result } = await API.post('Guesses', '/number', { body });<br />    this.setState({<br />      guess: result<br />    });<br />  }<br /><br />  render() {<br />    let prompt = ""<br /><br />    switch (this.state.guess) {<br />      case "high":<br />        prompt = "Incorrect. Guess a lower number.";<br />        break;<br />      case "low":<br />        prompt = "Incorrect. Guess a higher number.";<br />        break;<br />      case "correct":<br />        prompt = `Correct! The number is ${this.refs.guess.value}!`;<br />        break;<br />      default:<br />        prompt = "Guess a number between 1 and 100.";<br />    }<br /><br />    return (<br />      <div style={styles}><br />        <h1>Guess The Number</h1><br />        <p>{ prompt }</p><br /><br />        <input ref="guess" type="text" /><br />        <button type="submit" onClick={this.makeGuess.bind(this)}>Guess</button><br />      </div><br />    )<br /><br />  }<br />}<br /><br />let styles = {<br />  margin: "0 auto",<br />  width: "30%"<br />};<br /><br />export default GuessNumber;</pre>  | 

### Next Steps<a name="next-steps"></a>
+ Learn how to retrieve specific items and more with the [API module in AWS Amplify](https://aws.github.io/aws-amplify/media/developer_guide.html)\.
+ Learn how to enable more features for your app with the [AWS Mobile CLI](https://aws.github.io/aws-amplify)\.
+ Learn more about what happens behind the scenes, see [Set up Lambda and API Gateway](https://alpha-docs-aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)\.