.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-nosql-integrate-an-existing-table:

###################################
Integrate Your Existing NoSQL Table
###################################


.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-nosql-database>` to install the SDK and integrate features.

The :ref:`Get Started <add-aws-mobile-nosql-database>` section of this guide allows you to create new resources and complete the steps described on this page in minutes. If you want to import existing resources or create them from scratch, the contents of this page will walk you through the steps you need.

The following steps and examples are based on a simple bookstore app. The app tracks the books that are available in the bookstore using an Amazon DynamoDB table.

Set up Your Backend
===================

To manually configure an Amazon DynamoDB table that you can integrate into your mobile app, use the following steps.

.. contents::
   :local:
   :depth: 1

Create an New Table and Index
-----------------------------

* If you already have an Amazon DynamoDB table and know its region, you can skip to :ref:`how-to-nosql-integrate-an-existing-table-identity-pool`.

To create the Books table:

#. Sign in to the `Amazon DynamoDB Console <https://console.aws.amazon.com/dynamodb/home>`__.
#. Choose :guilabel:`Create Table`.
#. Type :userinput:`Books` as the name of the table.
#. Enter :userinput:`ISBN` in the :guilabel:`Partition key` field of the :guilabel:`Primary key` with :guilabel:`String` as their type.
#. Check the :guilabel:`Add sort key` box , then type :userinput:`Category` in the provided field and select :guilabel:`String` as the type.
#. Clear the :guilabel:`Use default settings` checkbox and choose :guilabel:`+ Add Index`.
#. In the :guilabel:`Add Index` dialog type :command:`Author` with :guilabel:`String` as the type.
#. Check the :guilabel:`Add sort key` checkbox and enter :command:`Title` as the sort key value, with :guilabel:`String` as its type.
#. Leave the other values at their defaults. Choose :guilabel:`Add index` to add the :command:`Author-Title-index` index.
#. Set the :guilabel:`Minimum provisioned capacity` for read to 10, and for write to 5.
#. Choose :guilabel:`Create`.Amazon DynamoDB will create your database.
#. Refresh the console and choose your Books table from the list of tables.
#. Open the :guilabel:`Overview` tab and copy or note the Amazon Resource Name (ARN). You need this for the next procedure.


.. _how-to-nosql-integrate-an-existing-table-identity-pool:

Set Up an Identity Pool
-----------------------

To give your users permissions to access your table you'll need an `identity pool <https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html>`__ from Amazon Cognito. That pool has two default IAM roles, one for guest (unauthenticated), and one for signed-in (authenticated) users. The policies you design and attach to the IAM roles determine what each type of user can and cannot do.

:ref:`Import an existing pool <import-an-existing-identity-pool>` or :ref:`create a new pool <create-a-new-identity-pool>` for your app.

Set Permissions
---------------

Attach the following IAM policy to the unauthenticated role for your identity pool. It allows the user to perform the actions on two resources (a table and an index) identified by the `ARN <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of your Amazon DynamoDB table.

    .. code-block:: json

        {
            "Statement": [{
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:Query",
                    "dynamodb:UpdateItem",
                    "dynamodb:BatchWriteItem"
                ],
                "Resource": [
                    "arn:aws:dynamodb:us-west-2:123456789012:table/Books",
                    "arn:aws:dynamodb:us-west-2:123456789012:table/Books/index/*"
                ]
            }]
        }

Apply Permissions
-----------------

Apply this policy to the unauthenticated role assigned to your Amazon Cognito identity pool, replacing the :guilabel:`Resource` values with the correct ARN for the Amazon DynamoDB table:

#. Sign in to the `IAM console <https://console.aws.amazon.com/iam>`__.
#. Choose :guilabel:`Roles` and then choose the "Unauth" role that Amazon Cognito created for you.
#. Choose :guilabel:`Attach Role Policy`.
#. Choose :guilabel:`Custom Policy` and then Choose :guilabel:`Select`.
#. Type a name for your policy and paste in the policy document shown above, replacing the `Resource` values with the ARNs for your table and index. (You can retrieve the table ARN from the :guilabel:`Details` tab of the database; then append :file:`/index/*` to obtain the value for the index ARN.
#. Choose :guilabel:`Apply Policy`.

.. _how-to-integrate-nosql-connect-to-your-backend:

Connect to Your Backend
=======================

.. contents::
   :local:
   :depth: 1

Create Your AWS Configuration File
----------------------------------

Your app is connected to your AWS resources using an :file:`awsconfiguration.json` file which contains the endpoints for the services you use.

#. Create a file with name :file:`awsconfiguration.json` with the following contents:

    .. code-block:: json

        {
          "Version": "1.0",
          "CredentialsProvider": {
            "CognitoIdentity": {
              "Default": {
                "PoolId": "COGNITO-IDENTITY-POOL-ID",
                "Region": "COGNITO-IDENTITY-POOL-REGION"
              }
            }
          },
          "IdentityManager": {
            "Default": {}
          },
          "DynamoDBObjectMapper": {
            "Default": {
              "Region": "DYNAMODB-REGION"
            }
          }
        }

#. Make the following changes to the configuration file.

    * Replace the :code:`DYNAMODB-REGION` with the region the table was created in.

      .. list-table::
         :widths: 1 6

         * - Need to find your table's region?

           - Go to `Amazon DynamoDB Console <https://console.aws.amazon.com/dynamodb>`__. and choose the :guilabel:`Overview` tab for your table. The :guilabel:`Amazon Resource Name (ARN)` item shows the table's ID, which contains its region.

             For example, if your pool ID is
             :code:`arn:aws:dynamodb:us-east-1:012345678901:table/nosqltest-mobilehub-012345678-Books`, then your the table's region value would be :code:`us-east-1`.

             The configuration file value you want is in the form of: :code:`"Region": "REGION-OF-YOU-DYNAMODB-ARN"`. For this example:

             .. code-block:: bash

                "Region": "us-east-1"

    * Replace the :code:`COGNITO-IDENTITY-POOL-ID` with the identity pool ID.

    * Replace the :code:`COGNITO-IDENTITY-POOL-REGION` with the region the identity pool was created in.

        .. list-table::
             :widths: 1 6

             * - Need to find your pool's ID and region?

               - Go to `Amazon Cognito Console <https://console.aws.amazon.com/cognito>`__ and choose :guilabel:`Manage Federated Identities`, then choose your pool and choose :guilabel:`Edit identity pool`. Copy the value of :guilabel:`Identity pool ID`.

                 Insert this region value into the following form to create the value you need for this integration.

                 .. code-block:: bash

                    "Region": "REGION-PREFIX-OF-YOUR-POOL-ID".

                 For example, if your pool ID is :code:`us-east-1:01234567-yyyy-0123-xxxx-012345678901`, then your integration region value would be:

                 .. code-block:: bash

                    "Region": "us-east-1"


Add the AWS Config File
-----------------------

To make the connection between your app and your backend services, add the configuration file.

.. container:: option

    Android - Java
         In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

          .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
             :scale: 100
             :alt: Image of creating a raw directory in Android Studio.

          .. only:: pdf

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 50

          .. only:: kindle

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 75

      Drag the :file:`awsconfiguration.json` you created into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

    Android - Kotlin
         In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

          .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
             :scale: 100
             :alt: Image of creating a raw directory in Android Studio.

          .. only:: pdf

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 50

          .. only:: kindle

             .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                :scale: 75

      Drag the :file:`awsconfiguration.json` you created into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

    iOS - Swift
      Drag the :file:`awsconfiguration.json` into the folder containing your :file:`Info.plist` file in your Xcode project. Choose :guilabel:`Copy items` and :guilabel:`Create groups` in the options dialog.


Add the SDK to your App
-----------------------

Use the following steps to add AWS Mobile NoSQL Database to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`app/build.gradle` must contain:

            .. code-block:: java
               :emphasize-lines: 2

                dependencies{

                    // Amazon Cognito dependencies for user access to AWS resources
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                    // AmazonDynamoDB dependencies for NoSQL Database
                    implementation 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'

                    // other dependencies . . .
                }

         #. Add the following permissions to :file:`AndroidManifest.xml`.

            .. code-block:: xml

                 <uses-permission android:name="android.permission.INTERNET"/>
                 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>


      #. Create an :code:`AWSDynamoDBMapper` client in the call back of your call to instantiate :code:`AWSMobileClient`. This will ensure that the AWS credentials needed to connect to Amazon DynamoDB are available, and is typically in :code:`onCreate` function of of your start up activity.

         .. code-block:: java

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;
            import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;

            public class MainActivity extends AppCompatActivity {

                // Declare a DynamoDBMapper object
                DynamoDBMapper dynamoDBMapper;

                @Override
                protected void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.activity_main);

                    // AWSMobileClient enables AWS user credentials to access your table
                    AWSMobileClient.getInstance().initialize(this, new AWSStartupHandler() {

                        @Override
                        public void onComplete(AWSStartupResult awsStartupResult) {

                                // Add code to instantiate a AmazonDynamoDBClient
                                AmazonDynamoDBClient dynamoDBClient = new AmazonDynamoDBClient(AWSMobileClient.getInstance().getCredentialsProvider());
                                this.dynamoDBMapper = DynamoDBMapper.builder()
                                    .dynamoDBClient(dynamoDBClient)
                                    .awsConfiguration(
                                    AWSMobileClient.getInstance().getConfiguration())
                                    .build();

                        }
                    }).execute();

                    // Other functions in onCreate . . .
                }
            }

      .. list-table::
         :widths: 1 6

         * - **Important**

           - **Use Asynchronous Calls to DynamoDB**

             Since calls to |DDB| are synchronous, they don't belong on your UI thread. Use an asynchronous method like the :code:`Runnable` wrapper to call :code:`DynamoDBObjectMapper` in a separate thread.

             .. code-block:: java

                 Runnable runnable = new Runnable() {
                      public void run() {
                        //DynamoDB calls go here
                      }
                 };
                 Thread mythread = new Thread(runnable);
                 mythread.start();

   Android - Kotlin
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`app/build.gradle` must contain:

            .. code-block:: java
               :emphasize-lines: 2

                dependencies{

                    // Amazon Cognito dependencies for user access to AWS resources
                    implementation ('com.amazonaws:aws-android-sdk-mobile-client:2.6.+@aar') { transitive = true }

                    // AmazonDynamoDB dependencies for NoSQL Database
                    implementation 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'

                    // other dependencies . . .
                }

         #. Add the following permissions to :file:`AndroidManifest.xml`.

            .. code-block:: xml

                 <uses-permission android:name="android.permission.INTERNET"/>
                 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>


      #. Create an :code:`AWSDynamoDBMapper` client in the call back of your call to instantiate :code:`AWSMobileClient`. This will ensure that the AWS credentials needed to connect to Amazon DynamoDB are available, and is typically in :code:`onCreate` function of of your start up activity.

         .. code-block:: kotlin

            import com.amazonaws.mobile.client.AWSMobileClient;
            import com.amazonaws.mobile.client.AWSStartupHandler;
            import com.amazonaws.mobile.client.AWSStartupResult;

            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;
            import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;

            class MainActivity : AppCompatActivity() {
                private var dynamoDBMapper: DynamoDBMapper? = null

                override fun onCreate(savedInstanceState: Bundle?) {
                    super.onCreated(savedInstanceState)
                    setContentView(R.layout.activity_main)
                    AWSMobileClient.getInstance().initialize(this) {
                        val dbClient = AmazonDynamoDBClient(AWSMobileClient.getInstance().credentialsProvider)
                        dynamoDBMapper = DynamoDBMapper.builder()
                            .awsConfiguration(AWSMobileClient.getInstance().configuration)
                            .build()
                    }.execute()

                    // Anything else in onCreate()
                }
            }

      .. list-table::
         :widths: 1 6

         * - **Important**

           - **Use Asynchronous Calls to DynamoDB**

             Since calls to |DDB| are synchronous, they don't belong on your UI thread. Use an asynchronous method like the :code:`Runnable` wrapper to call :code:`DynamoDBObjectMapper` in a separate thread.

             .. code-block:: kotlin

                 thread(start = true) {
                    // DynamoDB calls go here
                 }

   iOS - Swift
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. Add the :code:`AWSDynamoDB` pod to your :file:`Podfile` to install the AWS Mobile SDK.

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                    # Enable AWS user credentials
                    pod 'AWSMobileClient', '~> 2.6.13'

                    # Connect to NoSQL database tables
                    pod 'AWSDynamoDB', '~> 2.6.13'

                    # other pods . . .
                end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Classes that call |DDB| APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSDynamoDB

Add Data Models to Your App
---------------------------

To connect your app to your table create a data model object in the following form. In this example, the model is based on the :code:`Books` table you created in a previous step. The partition key (hash key) is called :code:`ISBN` and the sort key (rangekey) is called :code:`Category`.

.. container:: option

   Android - Java
     In the Android Studio project explorer right-click the folder containing your main activity, and choose :guilabel:`New > Java Class`. Type the :guilabel:`Name` you will use to refer to your data model. In this example the name would be :userinput:`BooksDO`. Add code in the following form.

     .. code-block:: java

            package com.amazonaws.models.nosql;

            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBAttribute;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBHashKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBIndexHashKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBIndexRangeKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBRangeKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBTable;

            import java.util.List;
            import java.util.Map;
            import java.util.Set;

            @DynamoDBTable(tableName = "Books")

            public class BooksDO {
                private String _isbn;
                private String _category;
                private String _title;
                private String _author;

                @DynamoDBHashKey(attributeName = "ISBN")
                @DynamoDBAttribute(attributeName = "ISBN")
                public String getIsbn() {
                    return _isbn;
                }

                public void setIsbn(final String _isbn) {
                    this._isbn = _isbn;
                }

                @DynamoDBRangeKey (attributeName = "Category")
                @DynamoDBAttribute(attributeName = "Category")
                public String getCategory() {
                    return _category;
                }

                public void setCategory(final String _category) {
                    this._category= _category;
                }

                @DynamoDBIndexHashKey(attributeName = "Author", globalSecondaryIndexName = "Author")
                public String getAuthor() {
                    return _author;
                }

                public void setAuthor(final String _author) {
                    this._author = _author;
                }

                @DynamoDBIndexRangeKey(attributeName = "Title", globalSecondaryIndexName = "Title")
                public String getTitle() {
                    return _title;
                }

                public void setTitle(final String _title) {
                    this._title = _title;
                }

            }

  Android - Kotlin
     In the Android Studio project explorer right-click the folder containing your main activity, and choose :guilabel:`New > Java Class`. Type the :guilabel:`Name` you will use to refer to your data model. In this example the name would be :userinput:`BooksDO`. Add code in the following form.

     .. code-block:: kotlin

            package com.amazonaws.models.nosql;

            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBAttribute;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBHashKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBIndexHashKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBIndexRangeKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBRangeKey;
            import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBTable;

            import java.util.List;
            import java.util.Map;
            import java.util.Set;

            @DynamoDBTable(tableName = "Books")
            data class BooksDO {
                @DynamoDBHashKey(attributeName = "ISBN")
                @DynamoDBAttribute(attributeName = "ISBN")
                var isbn

                @DynamoDBRangeKey (attributeName = "Category")
                @DynamoDBAttribute(attributeName = "Category")
                var category

                @DynamoDBIndexHashKey(attributeName = "Author", globalSecondaryIndexName = "Author")
                var author

                @DynamoDBIndexRangeKey(attributeName = "Title", globalSecondaryIndexName = "Title")
                var title
            }


   iOS - Swift
     In the Xcode project explorer,  right-click the folder containing your app delegate, and choose :guilabel:`New File > Swift File > Next`. Type the name you will use to refer to your data model as the filenam. In this example the name would be :userinput:`Books`. Add code in the following form.

    .. code-block:: swift


       import Foundation
       import UIKit
       import AWSDynamoDB

       class Books: AWSDynamoDBObjectModel, AWSDynamoDBModeling {

            var _isbn: String?
            var _category: String?
            var _author: String?
            var _title: String?

            class func dynamoDBTableName() -> String {
                return "Books"
            }

            class func hashKeyAttribute() -> String {
                return "_isbn"
            }

            class func rangeKeyAttribute() -> String {
                return "_category"
            }

            override class func jsonKeyPathsByPropertyKey() -> [AnyHashable: Any] {
                return [
                    "_isbn" : "ISBN",
                    "_category" : "Category",
                    "_author" : "Author",
                    "_title" : "Title",
                ]
            }
      }


.. _add-aws-mobile-nosql-database-crud:

Perform CRUD Operations
=======================

The fragments below consume the :code:`BooksDO` data model class created in a previous step.

.. contents::
   :local:
   :depth: 1


.. _add-aws-mobile-nosql-database-crud-create:

Create (Save) an Item
---------------------

Use the following code to create an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java

            public void createBooks() {
                final com.amazonaws.models.nosql.BooksDO booksItem = new com.amazonaws.models.nosql.BooksDO();

                booksItem.setIsbn("ISBN1");
                booksItem.setAuthor("Frederick Douglas");
                booksItem.setTitle("Escape from Slavery");
                booksItem.setCategory("History");

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        dynamoDBMapper.save(booksItem);
                        // Item saved
                    }
                }).start();
            }

   Android - Kotlin
      .. code-block:: kotlin

         fun createBooks() {
            val item = BooksDO().apply {
                isbn = "ISBN1"
                author = "Frederick Douglas"
                title = "Escape from Slavery"
                category = "History"
            }

            thread(start = true) {
                dynamoDBMapper.save(item)
            }
         }

   iOS - Swift
      .. code-block:: swift

            func createBooks() {
                let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

                let booksItem: Books = Books()

                booksItem._isbn = "1234"
                booksItem._category = "History"
                booksItem._author = "Harriet Tubman"
                booksItem._title = "My Life"

                //Save a new item
                dynamoDbObjectMapper.save(booksItem, completionHandler: {
                    (error: Error?) -> Void in

                    if let error = error {
                        print("Amazon DynamoDB Save Error: \(error)")
                        return
                    }
                    print("An item was saved.")
                })
            }

.. _add-aws-mobile-nosql-database-crud-read:

Read (Load) an Item
-------------------


Use the following code to read an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java

            public void readBooks() {
                new Thread(new Runnable() {
                    @Override
                    public void run() {

                        com.amazonaws.models.nosql.BooksDO booksItem = dynamoDBMapper.load(
                                com.amazonaws.models.nosql.BooksDO.class,
                                "ISBN1",       // Partition key (hash key)
                                "History");    // Sort key (range key)

                        // Item read
                         Log.d("Books Item:", booksItem.toString());
                    }
                }).start();
            }

   Android - Kotlin
      .. code-block:: kotlin

         fun readBooks() {
            thread(start = true) {
                val item = dynamoDBMapper.load(BooksDO::class.java, "ISBN1", "History")
                runOnUiThread { updateUI(item) }
            }
        }

   iOS - Swift
      .. code-block:: swift

         func readBooks() {
            let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

            // Create data object using data model you created
            let booksItem: Books = Books();

            dynamoDbObjectMapper.load(
                Books.self,
                hashKey: "1234",
                rangeKey: "Harriet Tubman",
                completionHandler: {
                    (objectModel: AWSDynamoDBObjectModel?, error: Error?) -> Void in
                    if let error = error {
                        print("Amazon DynamoDB Read Error: \(error)")
                        return
                    }
                    print("An item was read.")
            })
         }

.. _add-aws-mobile-nosql-database-crud-update:

Update an Item
--------------

Use the following code to update an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java

          public void updateBooks() {
              final com.amazonaws.models.nosql.BooksDO booksItem = new com.amazonaws.models.nosql.BooksDO();


              booksItem.setIsbn("ISBN1");
              booksItem.setCategory("History");
              booksItem.setAuthor("Frederick M. Douglas");
              //  booksItem.setTitle("Escape from Slavery");

              new Thread(new Runnable() {
                  @Override
                  public void run() {


                      // Using .save(bookItem) with no Title value makes that attribute value equal null
                      // The .Savebehavior shown here leaves the existing value as is
                      dynamoDBMapper.save(booksItem, new DynamoDBMapperConfig(DynamoDBMapperConfig.SaveBehavior.UPDATE_SKIP_NULL_ATTRIBUTES));

                      // Item updated
                  }
              }).start();
          }

   Android - Kotlin
      .. code-block:: kotlin

         fun updateBook(item: BooksDO) {
             thread(start = true) {
                val config = DynamoDBMapperConfig(DynamoDBMapperConfig.SaveBehavior.UPDATE_SKIP_NULL_ATTRIBUTES))
                dynamoDBMapper.save(item, config)
             }
         }

   iOS - Swift
      .. code-block:: swift

         func updateBooks() {
            let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

            let booksItem: Books = Books()

            booksItem._isbn = "1234"
            booksItem._category = "History"
            booksItem._author = "Harriet Tubman"
            booksItem._title = "The Underground Railroad"


            dynamoDbObjectMapper.save(booksItem, completionHandler: {(error: Error?) -> Void in
                if let error = error {
                    print(" Amazon DynamoDB Save Error: \(error)")
                    return
                }
                print("An item was updated.")
            })
         }


.. _add-aws-mobile-nosql-database-crud-delete:

Delete an Item
--------------

Use the following code to delete an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java

            public void deleteBooks() {
                new Thread(new Runnable() {
                    @Override
                    public void run() {

                        com.amazonaws.models.nosql.BooksDO booksItem = new com.amazonaws.models.nosql.BooksDO();
                        booksItem.setIsbn("ISBN1");       //partition key
                        booksItem.setCategory("History"); //range key

                        dynamoDBMapper.delete(booksItem);

                        // Item deleted
                    }
                }).start();
            }

   Android - Kotlin
      .. code-block:: kotlin

         fun deleteBook(item: BooksDO) {
            thread(start = true) {
                dynamoDBMapper.delete(item)
            }
         }

   iOS - Swift
      .. code-block:: swift

         func deleteBooks() {
            let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

            let itemToDelete = Books()
            itemToDelete?._isbn = "1234"
            itemToDelete?._category = "History"

            dynamoDbObjectMapper.remove(itemToDelete!, completionHandler: {(error: Error?) -> Void in
                if let error = error {
                    print(" Amazon DynamoDB Save Error: \(error)")
                    return
                }
                print("An item was deleted.")
            })
         }

.. _add-aws-mobile-nosql-database-query:

Perform a Query
===============


A query operation enables you to find items in a table. You must define a query using both the hash key
(partition key) and range key (sort key) attributes of a table. You can filter the results by
specifying the attributes you are looking for. For more information about :code:`DynamoDBQueryExpression`, see the `AWS Mobile SDK for Android API reference <The AWS Mobile SDK pattern used for Amazon DynamoDB queries matches the `https://docs.aws.amazon.com/AWSAndroidSDK/latest/javadoc/com/amazonaws/mobileconnectors/dynamodbv2/dynamodbmapper/DynamoDBQueryExpression.html>`__.

The following example code shows querying for books with partition key (hash key) :code:`ISBN` and sort key (range key) Category beginning with :code:`History`.

.. container:: option

   Android - Java
      .. code-block:: swift

           public void queryBook() {

                new Thread(new Runnable() {
                    @Override
                    public int hashCode() {
                        return super.hashCode();
                    }

                    @Override
                    public void run() {
                        com.amazonaws.models.nosql.BooksDO book = new com.amazonaws.models.nosql.BooksDO();
                        book.setIsbn("ISBN1");       //partition key
                        book.setCategory("History"); //range key


                        Condition rangeKeyCondition = new Condition()
                                .withComparisonOperator(ComparisonOperator.BEGINS_WITH)
                                .withAttributeValueList(new AttributeValue().withS("History"));
                        DynamoDBQueryExpression queryExpression = new DynamoDBQueryExpression()
                                .withHashKeyValues(book)
                                .withRangeKeyCondition("Category", rangeKeyCondition)
                                .withConsistentRead(false);

                        PaginatedList<BooksDO> result = dynamoDBMapper.query(com.amazonaws.models.nosql.BooksDO.class, queryExpression);

                        Gson gson = new Gson();
                        StringBuilder stringBuilder = new StringBuilder();

                        // Loop through query results
                        for (int i = 0; i < result.size(); i++) {
                            String jsonFormOfItem = gson.toJson(result.get(i));
                            stringBuilder.append(jsonFormOfItem + "\n\n");
                        }

                        // Add your code here to deal with the data result
                        Log.d("Query results: ", stringBuilder.toString());

                        if (result.isEmpty()) {
                            // There were no items matching your query.
                        }
                    }
                }).start();
            }

   Android - Kotlin
      .. code-block:: kotlin

         fun queryBooks() {
            thread(start = true) {
                val item = BooksDO().apply {
                    isbn = "ISBN1"
                    category = "History"
                }

                val rangeKeyCondition = Condition()
                        .withComparisonOperator(ComparisonOperator.BEGINS_WITH)
                        .withAttributeValueList(AttributeValue().withS("History"))
                val queryExpression = DynamoDBQueryExpression()
                        .withHashKeyValues(item)
                        .withRangeKeyCondition("Category", rangeKeyCondition)
                        .withConsistentRead(false)
                val result = dynamoDBMapper.query(BooksDO::class.java, queryExpression)
                runOnUiThread {
                    updateUI(result)    // result is a PaginatedList<BooksDO>
                }
            }
         }

   iOS - Swift
      .. code-block:: swift

         func queryBooks() {

            // 1) Configure the query
            let queryExpression = AWSDynamoDBQueryExpression()
             queryExpression.keyConditionExpression = "#isbn = :ISBN AND #category = :Category"

            queryExpression.expressionAttributeNames = [
                "#isbn": "ISBN",
                "#category": "Category"
            ]

            queryExpression.expressionAttributeValues = [
                ":ISBN" : "1234",
                ":Category" : "History"
            ]

            // 2) Make the query
            let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

            dynamoDbObjectMapper.query(Books.self, expression: queryExpression) { (output: AWSDynamoDBPaginatedOutput?, error: Error?) in
                if error != nil {
                    print("The request failed. Error: \(String(describing: error))")
                }
                if output != nil {
                    for books in output!.items {
                        let booksItem = books as? Books
                        print("\(booksItem!._title!)")
                    }
                }
            }
         }

Next Steps
----------


* To learn more about IAM policies, see `Using IAM <http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html>`__.

* To learn more about creating fine-grained access policies for Amazon DynamoDB, see `DynamoDB on Mobile – Part 5: Fine-Grained Access Control <https://aws.amazon.com/blogs/mobile/dynamodb-on-mobile-part-5-fine-grained-access-control/>`__.
