# Add Storage<a name="mobile-hub-web-add-storage"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up the Backend<a name="set-up-the-backend"></a>

The AWS Mobile CLI and AWS Amplify library make it easy to store and manage files in the cloud from your JavaScript app\.


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-web-getting-started.md)\.  | 

Enable the User File Storage feature by running the following commands in the root folder of your app\.

```
awsmobile user-files enable

awsmobile push
```

## Connect to the Backend<a name="connect-to-the-backend"></a>

The examples in this section show how you would integrate AWS Amplify library calls using React \(see the [AWS Amplify documentation](https://aws.github.io/aws-amplify) to use other flavors of Javascript\)\.

The following simple component could be added to a `create-react-app` project to present an interface that uploads images and download them for display\.


|  | 
| --- |
|  <pre>// Image upload and download for display example component<br />// src/ImageViewer.js<br /><br />import React, { Component } from 'react';<br /><br />class ImageViewer extends Component {<br />  render() {<br />    return (<br />      <div><br />        <p>Pick a file</p><br />        <input type="file" /><br />      </div><br />    );<br />  }<br />}<br /><br />export default ImageViewer;</pre>  | 

### Upload a file<a name="upload-a-file"></a>

The `Storage` module enables you to upload files to the cloud\. All uploaded files are publicly viewable by default\.

Import the `Storage` module in your component file\.

```
// ./src/ImageViewer.js

import { Storage } from 'aws-amplify';
```

Add the following function to use the `put` function on the `Storage` module to upload the file to the cloud, and set your component’s state to the name of the file\.

```
uploadFile(event) {
  const file = event.target.files[0];
  const name = file.name;

  Storage.put(key, file).then(() => {
    this.setState({ file: name });
  });
}
```

Place a call to the `uploadFile` function in the `input` element of the component’s render function, to start upload when a user selects a file\.

```
render() {
  return (
    <div>
      <p>Pick a file</p>
      <input type="file" onChange={this.uploadFile.bind(this)} />
    </div>
  );
}
```

### Display an image<a name="display-an-image"></a>

To display an image, this example shows the use of the `S3Image` component of the AWS Amplify for React library\.

1. From a terminal, run the following command in the root folder of your app\.

   ```
   npm install --save aws-amplify-react
   ```

1. Import the `S3Image` module in your component\.

   ```
   import { S3Image } from 'aws-amplify-react';
   ```

Use the S3Image component in the render function\. Update your render function to look like the following:

```
render() {
  return (
     <div>
       <p>Pick a file</p>
       <input type="file" onChange={this.handleUpload.bind(this)} />
       { this.state && <S3Image path={this.state.path} /> }
     </div>
  );
}
```


|  | 
| --- |
|  Put together, the entire component should look like this: <pre>// Image upload and download for display example component<br /><br />import React, { Component } from 'react';<br />import { Storage } from 'aws-amplify';<br />import { S3Image } from 'aws-amplify-react';<br /><br />class ImageViewer extends Component {<br /><br />  handleUpload(event) {<br />    const file = event.target.files[0];<br />    const path = file.name;<br />    Storage.put(path, file).then(() => this.setState({ path }) );<br />  }<br /><br />  render() {<br />    return (<br />      <div><br />        <p>Pick a file</p><br />        <input type="file" onChange={this.handleUpload.bind(this)} /><br />        { this.state && <S3Image path={this.state.path} /> }<br />      </div><br />    );<br />  }<br />}<br /><br />export default ImageViewer;</pre>  | 

#### Next Steps<a name="next-steps"></a>
+ Learn how to do private file storage and more with the [Storage module in AWS Amplify](https://aws.github.io/aws-amplify/media/developer_guide.html)\.
+ Learn how to enable more features for your app with the [AWS Mobile CLI](https://aws.github.io/aws-amplify)\.
+ Learn how to use those features in your app with the [AWS Amplify library](https://aws.github.io/aws-amplify)\.
+ Learn more about the [analytics for the User File Storage feature](https://alpha-docs-aws.amazon.com/pinpoint/latest/developerguide/welcome.html)\.
+ Learn more about how your files are stored on [Amazon Simple Storage Service](https://aws.amazon.com/documentation/s3/)\.