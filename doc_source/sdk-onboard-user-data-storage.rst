.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sdk-onboard-mobile-user-data-storage:

############################
Add Data Storage to your App
############################

.. _sdk-onboard-mobile-user-data-storage-steps:

In this section, we will walk you through a step by step process to setup an S3 bucket, setup authentication for your app and upload/download a file.
We will use Cognito Identity Pools for Authentication, which will provide a set of short-lived access credentials to your app.

Setup the Backend
==================

If you already have a Cognito Identity Pool and have set up its unauthenticated role to have read/write permissions on the S3 bucket, you can skip to the section titled :ref:create-aws-configuration

Create or import the Amazon Cognito Identity Pool
--------------------------------------------------

* Go to `Amazon Cognito Console <https://console.aws.amazon.com/cognito>`__ and choose **Manage Federated Identities**.

* Click **Create new Identity pool** button on the top left of the console.

* Give a name for the Identity pool and check **Enable access to unauthenticated identities** under the **Unauthenticated Identities** section, click **Create pool** button on the bottom right.

* To enable Cognito Identities to access your resources, expand the **View Details** section to see the two roles that are to be created. Make a note of the **unauth** role whose name is of the form **Cognito_<IdentityPoolName>Unauth_Role**. You will need this value at later point in this exercise. Now click **Allow** button in the bottom right of the console to create the roles.

* Under **Get AWSCredentials** section, in the code snippet to create **CognitoCachingCredentialsProvider**, find the Identity pool ID and the AWS region and make note of them. You will need it later.

Set up the required Amazon IAM permissions
-------------------------------------------

* Go to `Amazon IAM Console <https://console.aws.amazon.com/iam/home>`__ and select **Roles**.

* Select the **unauth** role you just created in the previous step, which is of the form **Cognito_<IdentityPoolName>Unauth_Role**.

* Select **Attach Policy**, then find **AmazonS3FullAccess** and select it. Click **Attach Policy** button to attach it to the role.

* Note:  This will grant users in the identity pool full access to all buckets and operations in S3. In a real app, you should restrict users to only have access to the resources they need.

Create or import your existing Amazon S3 bucket
------------------------------------------------

* Go to `Amazon S3 Console <https://console.aws.amazon.com/s3/home>`__ and click **Create bucket**.

* Enter a name for the bucket that is DNS-compliant, for example `com.amazon.mybucket`. See `Bucket Restrictions and Limitations <hhttp://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules>`__ for more information on how to name buckets.

* Choose the region that you want the bucket to be created.

* Click **Create** to create the bucket. Note the name of the bucket and the region that it was created in. The region typically would be of the form `US East (N. Virginia)`. Use the information on `AWS Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ to map that to a string of the form `us-east-1`. Note down this region string. You will need it later.

.. _create-aws-configuration:

Create AWSConfiguration
========================

Create the awsconfiguration.json file
---------------------------------------

* Create a file with name **awsconfiguration.json** with the following contents:

	.. code-block:: json

		{
		    "UserAgent": "MobileHub\/1.0",
		    "Version": "1.0",
		    "CredentialsProvider": {
		        "CognitoIdentity": {
		            "Default": {
		                "PoolId": "COGNITO-IDENTITY-POOL-ID",
		                "Region": "COGNITO-IDENTITY-POOL-REGION"
		            }
		        }
		    },
		    "S3TransferUtility": {
		        "Default": {
		            "Bucket": "S3-BUCKET-NAME",
		            "Region": "S3-REGION"
		        }
		    }
		}

* Replace the `COGNITO-IDENTITY-POOL-ID` with the Cognito Identity Pool ID.

* Replace the `COGNITO-IDENTITY-POOL-REGION` with the region the Cognito Identity Pool was created in.

* Replace the `S3-BUCKET-NAME` with the name of the S3 bucket.

* Replace the `S3-REGION` with the region the S3 bucket was created in.


Add the awsconfiguration.json file to your app
-----------------------------------------------

.. container:: option

    Android - Java
    	Place the `awsconfiguration.json` file you created in the previous step into a `res/raw` `Android Resource Directory <https://developer.android.com/studio/write/add-resources.html>`__ in your Android project.

    iOS - Swift
    	Place the `awsconfiguration.json` into the folder containing your `Info.plist` file in your Xcode project. Select `Copy items` if needed and `Create groups` in the options dialog to make sure the file is actually copied into the Xcode project.


Add the SDK to your App
========================

.. include:: storage/add-aws-mobile-user-data-storage-connect-to-your-backend.rst

Now, you have setup the backend and added the AWS Mobile SDK to your app. Next, let's look at how we upload and download a file.

.. include:: storage/add-aws-mobile-user-data-storage-upload-download.rst
