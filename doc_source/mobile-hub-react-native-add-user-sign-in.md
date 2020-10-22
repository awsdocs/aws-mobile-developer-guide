# Add Auth / User Sign\-in<a name="mobile-hub-react-native-add-user-sign-in"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up Your Backend<a name="set-up-your-backend"></a>


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-react-native-getting-started.md)\.  | 

The AWS Mobile CLI components for user authentication include a rich, configurable UI for sign\-up and sign\-in\.

 **To enable the Auth features** 

In the root folder of your app, run:

```
awsmobile user-signin enable

awsmobile push
```

## Connect to Your Backend<a name="connect-to-your-backend"></a>

The AWS Mobile CLI enables you to integrate ready\-made sign\-up/sign\-in/sign\-out UI from the command line\.

 **To add user auth UI to your app** 

1. Install AWS Amplify for React Nativelibrary\.

   ```
   npm install --save aws-amplify
   npm install --save aws-amplify-react-native
   ```


|  |  | 
| --- |--- |
|   **Note**   |  If your react\-native app was not created using `create-react-native-app` or using a version of Expo lower than v25\.0\.0 \(the engine behind `create-react-native-app`\), you need to link libraries in your project for the Auth module on React Native, `amazon-cognito-identity-js`\. To link to the module, you must first eject the project: <pre>npm run eject<br />react-native link amazon-cognito-identity-js</pre>  | 

1. Add the following import in `App.js` \(or other file that runs upon app startup\):

   ```
   import { withAuthenticator } from 'aws-amplify-react-native';
   ```

1. Then change `export default App;` to the following\.

   ```
   export default withAuthenticator(App);
   ```

To test, run `npm start` or `awsmobile run`\.

## Next Steps<a name="next-steps"></a>

Learn more about the AWS Mobile [User Sign\-in](User-Sign-in.md#user-sign-in) feature, which uses [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/welcome.html)\.

Learn about [AWS Mobile CLI](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify)\.