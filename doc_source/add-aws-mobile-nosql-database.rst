.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-nosql-database:

##########################################################
Add NoSQL Database to Your Mobile App with Amazon DynamoDB
##########################################################


.. meta::
   :description: Integrating nosql database


.. _overview:

Overview
==============


The AWS Mobile Hub :ref:`nosqldb` feature uses `Amazon DynamoDB <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`__ to enable you to create database tables
that can store and retrieve data for use by your apps.


.. _setup-your-backend:

Set Up Your Backend
===================


#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before you proceed.

#. Enable :guilabel:`NoSQL Database`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`__ and choose the :guilabel:`NoSQL Database` tile to enable the feature.

#. Follow the console work flow to define the tables you need. See :ref:`config-nosqldb` for details.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the NoSQL Database documentation below to connect to your backend.

#. Download the models required for your app. The data models provide set and get methods for each attribute of a |DDB| table.

.. _add-aws-mobile-nosql-database-app:

Connect to your backend
=======================


**To add AWS Mobile NoSQL Database to your app**

.. container:: option
   Android - Java
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`app/build.gradle` must contain:

            .. code-block:: java
               :emphasize-lines: 2

                dependencies{
                    implementation 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'
                }

         #. For each Activity where you make calls to perform database operations, import the
            following APIs.

            .. code-block:: java
               :emphasize-lines: 1

                import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;

      #. Create a :code:`DynamoDBMapper` client for your app as in the following
         example.

         .. code-block:: java
            :emphasize-lines: 2, 9-13

             // import DynamoDBMapper
             import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;

             public class MainActivity extends AppCompatActivity {

                 // Declare a DynamoDBMapper object
                 DynamoDBMapper dynamoDBMapper;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                     // Instantiate a AmazonDynamoDBMapperClient
                     AmazonDynamoDBClient dynamoDBClient = new AmazonDynamoDBClient(AWSMobileClient.getInstance().getCredentialsProvider());
                     this.dynamoDBMapper = DynamoDBMapper.builder()
                            .dynamoDBClient(dynamoDBClient)
                            .awsConfiguration(AWSMobileClient.getInstance().getConfiguration())
                            .build();
                }
            }

      #. Add the project data model files you downloaded from the
         |AMH| console. The data models provide set and get methods for each attribute of a |DDB|
         table they model.

         #. Copy the data model file(s) you downloaded,
            :file:`./YOUR-PROJECT-NAME-integration-lib-aws-my-sample-app-android/src/main/java/com/amazonaws/models/nosqlYOUR-TABLE-NAMEDO.java` into the Android Studio folder that contains your main activity.


      .. list-table::
         :widths: 1

         * - .. note:: **Use Asynchronous Calls to DynamoDB**

                Since calls to |DDB| are synchronous, they don't belong on your UI thread. Use an
                asynchronous method like the :code:`Runnable` wrapper to call :code:`DynamoDBObjectMapper` in a
                separate thread.

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
                    implementation 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'
                }

         #. For each Activity where you make calls to perform database operations, import the
            following APIs.

            .. code-block:: java
               :emphasize-lines: 1

                import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;

      #. Create a :code:`DynamoDBMapper` client for your app as in the following
         example.

         .. code-block:: kotlin
            :emphasize-lines: 2, 9-13

             // import DynamoDBMapper
             import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;

             class MainActivity : AppCompatActivity() {
               private var dynamoDBMapper: DynamoDBMapper? = null

               override fun onCreate(savedInstanceState: Bundle?) {
                 super.onCreate(savedInstanceState)
                 setContentView(R.layout.activity_main)

                 val client = AmazonDynamoDBClient(AWSMobileClient.getInstance().credentialsProvider)
                 dynamoDBMapper = DynamoDBMapper.builder()
                    .dynamoDBClient(client)
                    .awsConfiguration(AWSMobileClient.getInstance().configuration)
                    .build()
               }
            }

      #. Add the project data model files you downloaded from the
         |AMH| console. The data models provide set and get methods for each attribute of a |DDB|
         table they model.

         #. Copy the data model file(s) you downloaded,
            :file:`./YOUR-PROJECT-NAME-integration-lib-aws-my-sample-app-android/src/main/java/com/amazonaws/models/nosqlYOUR-TABLE-NAMEDO.java` into the Android Studio folder that contains your main activity.


      .. list-table::
         :widths: 1

         * - .. note:: **Use Asynchronous Calls to DynamoDB**

                Since calls to |DDB| are synchronous, they don't belong on your UI thread. Use an
                asynchronous method like the :code:`thread` wrapper to call :code:`DynamoDBObjectMapper` in a
                separate thread.

                .. code-block:: kotlin

                    thread(start = true) {
                        // DynamoDB calls go here
                    }

   iOS - Swift
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                    pod 'AWSDynamoDB', '~> 2.6.13'
                    # other pods
                end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Classes that call |DDB| APIs must use the following import statements:

            .. code-block:: swift

                import AWSCore
                import AWSDynamoDB

      #. From the location where you downloaded the data model file(s), drag and drop each file with the form of :file:`{your-table-name}.swift` into the folder that contains your :file:`AppDelegate.swift`. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

         .. list-table::
            :widths: 1 6


.. _add-aws-mobile-nosql-database-crud:

Perform CRUD Operations
=======================

.. contents:: **In this section:**
   :local:
   :depth: 1

Using the Data Model
--------------------

To connect your app to an Amazon DynamoDB table you have created, use a data model generated by |AMH|, or create one in the following form. As an example, the fragments in the following sections are based on a table named :code:`News`. The table's partition key (hash key) is named :code:`userID`, the sort key (range key) is called :code:`articleId` and other attributes, including :code:`author`, :code:`title`, :code:`category`, :code:`content`, and :code:`content`.



.. container:: option

   Android - Java
      In the following example, the :code:`NewsDO` class defines the data model of the :code:`News` table. The class is used by the CRUD methods in this section to access the table and its attributes. The data model file you downloaded from |AMH| in previous steps contains a similar class that defines the model of your table.

      Note that the class is annotated to map it to the Amazon DynamoDB table name. The attribute names, hash key, and range key of the getters in the class are annotated to map them to local variable names used by the app for performing data operations.

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

          @DynamoDBTable(tableName = "nosqlnews-mobilehub-1234567890-News")

          public class NewsDO {
              private String _userId;
              private String _articleId;
              private String _author;
              private String _category;
              private String _content;
              private Double _creationDate;
              private String _title;

              @DynamoDBHashKey(attributeName = "userId")
              @DynamoDBAttribute(attributeName = "userId")
              public String getUserId() {
                  return _userId;
              }

              public void setUserId(final String _userId) {
                  this._userId = _userId;
              }
              @DynamoDBRangeKey(attributeName = "articleId")
              @DynamoDBAttribute(attributeName = "articleId")
              public String getArticleId() {
                  return _articleId;
              }

              public void setArticleId(final String _articleId) {
                  this._articleId = _articleId;
              }
              @DynamoDBAttribute(attributeName = "author")
              public String getAuthor() {
                  return _author;
              }

              public void setAuthor(final String _author) {
                  this._author = _author;
              }

              // setters and getters for other attribues ...

          }

   Android - Kotlin
      In the following example, the :code:`NewsDO` class defines the data model of the :code:`News` table. The class is used by the CRUD methods in this section to access the table and its attributes. The data model file you downloaded from |AMH| in previous steps contains a similar class that defines the model of your table.

      Note that the class is annotated to map it to the Amazon DynamoDB table name. The attribute names, hash key, and range key of the getters in the class are annotated to map them to local variable names used by the app for performing data operations.

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

          @DynamoDBTable(tableName = "nosqlnews-mobilehub-1234567890-News")

          data class NewsDO {
              @DynamoDBHashKey(attributeName = "userId" )
              @DynamoDBAttribute(attributeName = "userId")
              var userId: String?

              @DynamoDBRangeKey(attributeName = "articleId")
              @DynamoDBAttribute(attributeName = "articleId")
              var articleId: String?

              @DynamoDBAttribute(attributeName = "author")
              var author: String?

              // setters and getters for other attribues ...
          }

      If you download the model files, they will be provided in Java.  The model files are equally useable in Kotlin projects.

   iOS - Swift
      In the following example, the :code:`News` class defines the data model of the :code:`News` table. The class is used by the CRUD methods in this section to access the table and its attributes. The data model file you downloaded from |AMH| in previous steps contains a similar class that defines the model of your table.

      Note that the functions of the model class return the Amazon DynamoDB table, hash key attibute, and range key attribute names used by the app for data operations. For example, :code:`dynamoDBTableName()` returns the name of the table object in AWS. The local variable names map to the attribute names of the table. For instance, :code:`userId` is the name of both the local variable and the attribute of the Amazon DynamoDB table.

      This example is slightly simpler than the data model generated by |AMH|, but functionally the same.

      .. code-block:: swift

          // News.swift

          import Foundation
          import UIKit
          import AWSDynamoDB

          class News: AWSDynamoDBObjectModel, AWSDynamoDBModeling {

              @objc var userId: String?
              @objc var articleId: String?
              @objc var author: String?
              @objc var category: String?
              @objc var content: String?
              @objc var creationDate: NSNumber?
              @objc var title: String?

              class func dynamoDBTableName() -> String {

                  return "nosqlnews-mobilehub-1200412570-News"
              }

              class func hashKeyAttribute() -> String {

                  return "userId"
              }

              class func rangeKeyAttribute() -> String {

                  return "articleId"
              }

          }


.. _add-aws-mobile-nosql-database-crud-create:

Create (Save) an Item
---------------------


Use the following code to create an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java
         :emphasize-lines: 1-18

          public void createNews() {
              final NewsDO newsItem = new NewsDO();

              newsItem.setUserId(unique-user-id);

              newsItem.setArticleId("Article1");
              newsItem.setContent("This is the article content");

              new Thread(new Runnable() {
                  @Override
                  public void run() {
                      dynamoDBMapper.save(newsItem);
                          // Item saved
                  }
              }).start();
          }

   Android - Kotlin
      .. code-block:: kotlin
         :emphasize-lines: 1-11

            fun createNews() {
                val NewsDO newsItem = NewsDO()
                newsItem.userId = "unique-user-id"
                newsItem.articleId = UUID.randomUUID().toString()
                newsItem.author = "Your Name"
                newsItem.content = "This is the article content"

                thread(start = true) {
                    dynamoDBMapper.save(newsItem)
                }
            }

   iOS - Swift
      .. code-block:: swift

          func createNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              // Create data object using data models you downloaded from Mobile Hub
              let newsItem: News = News()

              newsItem.userId = AWSIdentityManager.default().identityId

              newsItem.articleId = "YourArticleId"
              newsItem.title = "YourTitlestring"
              newsItem.author = "YourAuthor"
              newsItem.creationDate = NSDate().timeIntervalSince1970 as NSNumber

              //Save a new item
              dynamoDbObjectMapper.save(newsItem, completionHandler: {
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
         :emphasize-lines: 1-15

          public void readNews() {
              new Thread(new Runnable() {
                  @Override
                  public void run() {

                      NewsDO newsItem = dynamoDBMapper.load(
                              NewsDO.class,
                              unique-user-id,
                              "Article1");

                      // Item read
                      // Log.d("News Item:", newsItem.toString());
                  }
              }).start();
          }

   Android - Kotlin
      .. code-block:: kotlin
         :emphasize-lines: 1-7

            fun readNews(userId: String, articleId: String, callback: (NewsDO?) -> Unit) {
                thread(start = true) {
                    var newsItem = dynamoDBMapper.load(NewsDO::class.java,
                            userId, articleId)
                    runOnUiThread { callback(newsItem) }
                }
            }

   iOS - Swift
      .. code-block:: swift

         func readNews() {
           let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

               // Create data object using data models you downloaded from Mobile Hub
               let newsItem: News = News();
               newsItem.userId = AWSIdentityManager.default().identityId

               dynamoDbObjectMapper.load(
                  News.self,
                  hashKey: newsItem.userId,
                  rangeKey: "YourArticleId",
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
         :emphasize-lines: 1-18

          public void updateNews() {
              final NewsDO newsItem = new NewsDO();

              newsItem.setUserId(unique-user-id);

              newsItem.setArticleId("Article1");
              newsItem.setContent("This is the updated content.");

              new Thread(new Runnable() {
                  @Override
                  public void run() {

                      dynamoDBMapper.save(newsItem);

                      // Item updated
                  }
              }).start();
          }

   Android - Kotlin
      .. code-block:: kotlin
         :emphasize-lines: 1-5

            fun updateNews(updatedNews: NewsDO) {
                thread(start = true) {
                    dynamoDBMapper.save(updatedNews)
                }
            }

   iOS - Swift
      .. code-block:: swift

          func updateNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let newsItem: News = News();

              newsItem.userId = "unique-user-id"

              newsItem.articleId = "YourArticleId"
              newsItem.title = "This is the Title"
              newsItem.author = "B Smith"
              newsItem.creationDate = NSDate().timeIntervalSince1970 as NSNumber
              newsItem.category = "Local News"

              dynamoDbObjectMapper.save(newsItem, completionHandler: {(error: Error?) -> Void in
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
         :emphasize-lines: 1-17

          public void deleteNews() {
              new Thread(new Runnable() {
                  @Override
                  public void run() {

                      NewsDO newsItem = new NewsDO();

                      newsItem.setUserId(unique-user-id);    //partition key

                      newsItem.setArticleId("Article1");  //range (sort) key

                      dynamoDBMapper.delete(newsItem);

                      // Item deleted
                  }
              }).start();
          }

   Android - Kotlin
      .. code-block:: kotlin
         :emphasize-lines: 1-9

          public void deleteNews(userId: String, articleId: String) {
            thread(start = true) {
                val item = NewsDO()
                item.userId = userId
                item.articleId = articleId

                dynamoDBMapper.delete(item)
            }
          }

   iOS - Swift
      .. code-block:: swift

          func deleteNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let itemToDelete = News()
              itemToDelete?.userId = "unique-user-id"
              itemToDelete?.articleId = "YourArticleId"

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
specifying the attributes you are looking for.

The following example code shows querying for news submitted with :CODE:`userId` (hash key) and article ID beginning with :USERINPUT:`Trial` (range key).

.. container:: option

   Android - Java
      .. code-block:: java

         public void queryNews() {

            new Thread(new Runnable() {
                @Override
                public void run() {
                    NewsDO news = new NewsDO();
                    news.setUserId(unique-user-id);
                    news.setArticleId("Article1");

                    Condition rangeKeyCondition = new Condition()
                            .withComparisonOperator(ComparisonOperator.BEGINS_WITH)
                            .withAttributeValueList(new AttributeValue().withS("Trial"));

                    DynamoDBQueryExpression queryExpression = new DynamoDBQueryExpression()
                            .withHashKeyValues(note)
                            .withRangeKeyCondition("articleId", rangeKeyCondition)
                            .withConsistentRead(false);

                    PaginatedList<NewsDO> result = dynamoDBMapper.query(NewsDO.class, queryExpression);

                    Gson gson = new Gson();
                    StringBuilder stringBuilder = new StringBuilder();

                    // Loop through query results
                    for (int i = 0; i < result.size(); i++) {
                        String jsonFormOfItem = gson.toJson(result.get(i));
                        stringBuilder.append(jsonFormOfItem + "\n\n");
                    }

                    // Add your code here to deal with the data result
                    Log.d("Query result: ", stringBuilder.toString());

                    if (result.isEmpty()) {
                        // There were no items matching your query.
                    }
                }
            }).start();
         }

   Android - Kotlin
      .. code-block:: kotlin

         public void queryNews(userId: String, articleId: String, callback: (List<NewsDO>?) -> Unit) {
            thread(start = true) {
                val item = NewsDO()
                item.userId = userId
                item.articleId = articleId

                val rangeKeyCondition = Condition()
                    .withComparisonOperator(ComparisonOperator.BEGINS_WITH)
                    .withAttributeValueList(AttributeValue().withS("Trial"))
                val queryExpression = DynamoDBQueryExpression()
                            .withHashKeyValues(item)
                            .withRangeKeyCondition("articleId", rangeKeyCondition)
                            .withConsistentRead(false);
                val result = dynamoDBMapper.query(NewsDO::class.java, queryExpression)
                runOnUiThread { callback(result) }
            }
         }

   iOS - Swift
      .. code-block:: swift

          func queryNote() {
              // 1) Configure the query
              let queryExpression = AWSDynamoDBQueryExpression()
              queryExpression.keyConditionExpression = "#articleId >= :articleId AND #userId = :userId"

              queryExpression.expressionAttributeNames = [
                   "#userId": "userId",
                  "#articleId": "articleId"
              ]
              queryExpression.expressionAttributeValues = [
                  ":articleId": "SomeArticleId",
                  ":userId": "unique-user-id"
              ]

              // 2) Make the query

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              dynamoDbObjectMapper.query(News.self, expression: queryExpression) { (output: AWSDynamoDBPaginatedOutput?, error: Error?) in
                if error != nil {
                    print("The request failed. Error: \(String(describing: error))")
                }
                if output != nil {
                    for news in output!.items {
                        let newsItem = news as? News
                        print("\(newsItem!.title!)")
                    }
                }
             }
          }

