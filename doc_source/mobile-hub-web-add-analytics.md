# Add Analytics<a name="mobile-hub-web-add-analytics"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Basic Analytics Backend is Enabled for Your App<a name="basic-analytics-backend-is-enabled-for-your-app"></a>


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-web-getting-started.md)\.  | 

When you complete the AWS Mobile CLI setup and launch your app, anonymized session and device demographics data flows to the AWS analytics backend\.

 **To send basic app usage analytics to AWS** 

Launch your app locally by running:

```
npm start
```

When you use your app the [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/) service gathers and visualizes analytics data\.

 **To view the analytics using the Amazon Pinpoint console** 

1. Run `npm start`, `awsmobile run`, or `awsmobile publish --test` at least once\.

1. Open your project in the [AWS Mobile Hub console](https://console.aws.amazon.com/mobilehub/)\.

   ```
   awsmobile console
   ```

1. Choose the **Analytics** icon on the left, to navigate to your project in the [Amazon Pinpoint console](https://console.aws.amazon.com/pinpoint/)\.

1. Choose **Analytics** on the left\.

You should see an up\-tick in several graphs\.

## Add Custom Analytics to Your App<a name="add-custom-analytics-to-your-app"></a>

You can configure your app so that [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/) gathers data for custom events that you register within the flow of your code\.

 **To instrument custom analytics in your app** 

In the file containing the event you want to track, add the following import:

```
import { Analytics } from 'aws-amplify';
```

Add the a call like the following to the spot in your JavaScript where the tracked event should be fired:

```
componentDidMount() {
   Analytics.record('FIRST-EVENT-NAME');
}
```

Or to relevant page elements:

```
handleClick = () => {
     Analytics.record('SECOND-EVENT-NAME');
}

<button onClick={this.handleClick}>Call request</button>
```

To test:

1. Save the changes and run `npm start`, `awsmobile run`, or `awsmobile publish --test` to launch your app\. Use your app so that tracked events are triggered\.

1. In the [Amazon Pinpoint console](https://console.aws.amazon.com/pinpoint/), choose **Events** near the top\.

1. Select an event in the **Event** dropdown menu on the left\.

Custom event data may take a few minutes to become visible in the console\.

## Next Steps<a name="next-steps"></a>

Learn more about the analytics in AWS Mobile which are part of the [Messaging and Analytics](messaging-and-analytics.md) feature\. This feature uses [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html)\.

Learn about [AWS Mobile CLI](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify)\.