# Access Your APIs<a name="mobile-hub-react-native-access-apis"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up Your Backend<a name="set-up-your-backend"></a>


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-react-native-getting-started.md)\.  | 

The AWS Mobile [Cloud Logic](Cloud-Logic.md#cloud-logic) feature lets you call APIs in the cloud\. API calls are handled by your serverless Lambda functions\.

 **To enable cloud APIs in your app** 

```
awsmobile cloud-api enable

awsmobile push
```

Enabling Cloud Logic in your app adds a sample API, `sampleCloudApi` to your project that can be used for testing\.

You can find the sample handler function for the API by running `awsmobile console` in your app root folder, and then choosing the **Cloud Logic** feature in your Mobile Hub project\.

![\[View your sample cloud API and its lambda function handler.\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/images/web-view-cloud-api.png)

### Quickly Test Your API From the CLI<a name="quickly-test-your-api-from-the-cli"></a>

The `sampleCloudApi` and its handler function allow you to make end to end API calls\.

 **To test invocation of your unsigned APIs in the development environment** 

```
awsmobile cloud-api invoke <apiname> <method> <path> [init]
```

For the `sampleCloudApi` you may use the following examples to test the `post` method

```
awsmobile cloud-api invoke sampleCloudApi post /items '{"body": {"testKey":"testValue"}}'
```

This call will return a response similar to the following\.

```
{ success: 'post call succeed!',
url: '/items',
body: { testKey: 'testValue' } }
```

 **To test the :get method** 

```
awsmobile cloud-api invoke sampleCloudApi get /items
```

This will return a response as follows\.

```
{ success: 'get call succeed!', url: '/items' }
```

## Connect to Your Backend<a name="connect-to-your-backend"></a>

Once you have created your own [Cloud Logic](Cloud-Logic.md#cloud-logic) APIs and Lambda functions, you can call them from your app\.

 **To call APIs from your app** 

In `App.js` \(or other code that runs at launch\-time\), add the following import\.

```
import Amplify, { API } from 'aws-amplify';
import aws_exports from './aws-exports';
Amplify.configure(aws_exports);
```

Then add this to the component that calls your API\.

```
state = { apiResponse: null };

async getSample() {
 const path = "/items"; // you can specify the path
  const apiResponse = await API.get("sampleCloudApi" , path); //replace the API name
  console.log('response:' + apiResponse);
  this.setState({ apiResponse });
}
```

To invoke your API from a UI element, add an API call from within your component’s `render()` method\.

```
<View>
   <Button title="Send Request" onPress={this.getSample.bind(this)} />
   <Text>Response: {this.state.apiResponse && JSON.stringify(this.state.apiResponse)}</Text>
</View>
```

To test, save the changes, run `npm run android` or `npm run ios`` to launch your app\. Then try the UI element that calls your API\.

## Next Steps<a name="next-steps"></a>

Learn more about the AWS Mobile [Cloud Logic](Cloud-Logic.md#cloud-logic) feature which uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)\.

To be guided through creation of an API and it’s handler, run `awsmobile console` to open your app in the Mobile Hub console, and choose **Cloud Logic**\.

Learn about [AWS Mobile CLI](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify/)\.