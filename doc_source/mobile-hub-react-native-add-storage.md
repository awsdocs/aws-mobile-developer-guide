# Add Storage<a name="mobile-hub-react-native-add-storage"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up Your Backend<a name="react-native-add-storage-setup"></a>

The AWS Mobile CLI [User File Storage](User-Data-Storage.md#user-data-storage) feature enables apps to store user files in the cloud\.


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-react-native-getting-started.md)\.  | 

 **To configure your app’s cloud storage location** 

In your app root folder, run:

```
awsmobile user-files enable

awsmobile push
```

## Connect to Your Backend<a name="react-native-add-storage-connect"></a>

 **To add User File Storage to your app** 

In your component where you want to transfer files:

Import the `Storage` module from aws\-amplify and configure it to communicate with your backend\.

```
import { Storage } from 'aws-amplify';
```

Now that the Storage module is imported and ready to communicate with your backend, implement common file transfer actions using the code below\.

### Upload a file<a name="react-native-add-storage-upload"></a>

 **To upload a file to storage** 

Add the following methods to the component where you handle file uploads\.

```
async uploadFile() {
  let file = 'My upload text';
  let name = 'myFile.txt';
  const access = { level: "public" }; // note the access path
  Storage.put(name, file, access);
}
```

### Get a specific file<a name="react-native-add-storage-get"></a>

 **To download a file from cloud storage** 

Add the following code to a component where you display files\.

```
async getFile() {
  let name = 'myFile.txt';
  const access = { level: "public" };
  let fileUrl = await Storage.get(name, access);
  // use fileUrl to get the file
}
```

### List all files<a name="react-native-add-storage-list"></a>

 **To list the files stored in the cloud for your app** 

Add the following code to a component where you list a collection of files\.

```
async componentDidMount() {
  const path = this.props.path;
  const access = { level: "public" };
  let files = await Storage.list(path, access);
   // use file list to get single files
}
```

Use the following code to fetch file attributes such as the size or time of last file change\.

```
file.Size; // file size
file.LastModified.toLocaleDateString(); // last modified date
file.LastModified.toLocaleTimeString(); // last modified time
```

### Delete a file<a name="react-native-add-storage-remove"></a>

Add the following state to the element where you handle file transfers\.

```
async deleteFile(key) {
  const access = { level: "public" };
  Storage.remove(key, access);
}
```

## Next Steps<a name="next-steps"></a>

Learn more about the analytics in AWS Mobile which are part of the [User File Storage](User-Data-Storage.md#user-data-storage) feature\. This feature uses [Amazon Simple Storage Service \(S3\)](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)\.

Learn about [AWS Mobile CLI](aws-mobile-cli-reference.md)\.

Learn about [AWS Mobile Amplify](https://aws.github.io/aws-amplify)\.