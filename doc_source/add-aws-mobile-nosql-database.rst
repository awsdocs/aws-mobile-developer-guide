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


The AWS Mobile Hub :ref:`nosqldb` feature uses `Amazon DynamoDB <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`_ to enable you to create database tables
that can store and retrieve data for use by your apps.


.. _setup-your-backend:

Set Up Your Backend
===================


#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before your proceed.

#. Enable :guilabel:`NoSQL Database`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`_ and choose the :guilabel:`NoSQL Database` tile to enable the feature.

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
                    compile 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'
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

             public class MainActivity extends AppCompatActivity {
                 DynamoDBMapper dynamoDBMapper;

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

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

         #. From the location where you downloaded the data model file(s), drag and drop each file
            with the form of
            :file:`./YOUR-PROJECT-NAME-integration-lib-aws-my-sample-app-android/src/main/java/com/amazonaws/models/nosqlYOUR-TABLE-NAMEDO.java`
            into the folder that contains your main activity.

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


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                    pod 'AWSDynamoDB', '~> 2.6.6'
                    # other pods
                end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |DDB| APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSDynamoDB

      #. From the location where you downloaded the data model file(s), drag and drop each file with the form of :file:`{your-table-name}.swift` into the folder that contains your :file:`AppDelegate.swift`. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.


.. _add-aws-mobile-nosql-database-crud:

Perform CRUD Operations
=======================



.. contents:: **In this section:**
   :local:
   :depth: 1

.. _add-aws-mobile-nosql-database-crud-create:

Create (Save) an Item
---------------------


Use the following code to create an item in your NoSQL Database table.

.. container:: option

   Android - Java
      These fragments are based on a table named :code:`News`, with a partition key called
      :code:`userID` and a sort key (rangekey) called :code:`articleId`. The source of the
      :code:`NewsDO` object is a data model file downloaded from a |AMH| project that enables a News
      table.

      .. code-block:: java
         :emphasize-lines: 1-18

          public void createNews() {
              final NewsDO newsItem = new NewsDO();

              newsItem.setUserId(identityManager.getCachedUserID());

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


   iOS - Swift
      These fragments are based on a table named :code:`News`, with a partition key called
      :code:`userID` and a sort key (rangekey) called :code:`articleId`. The source of the
      :code:`NewsDO` object is a data model file downloaded from a |AMH| project that enables a News
      table.

      .. code-block:: swift

          func createNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              // Create data object using data models you downloaded from Mobile Hub
              let newsItem: News = News()

              newsItem._userId = AWSIdentityManager.default().identityId

              newsItem._articleId = "YourArticleId"
              newsItem._title = "YourTitlestring"
              newsItem._author = "YourAuthor"
              newsItem._creationDate = NSDate().timeIntervalSince1970 as NSNumber

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
                              identityManager.getCachedUserID(),
                              "Article1");

                      // Item read
                      // Log.d("News Item:", newsItem.toString());
                  }
              }).start();
          }


   iOS - Swift
      .. code-block:: swift

         func readNews() {
           let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

               // Create data object using data models you downloaded from Mobile Hub
               let newsItem: News = News();
               newsItem._userId = AWSIdentityManager.default().identityId

               dynamoDbObjectMapper.load(
                  News.self,
                  hashKey: newsItem._userId,
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

              newsItem.setUserId(identityManager.getCachedUserID());

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


   iOS - Swift
      .. code-block:: swift

          func updateNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let newsItem: News = News();

              newsItem._userId = AWSIdentityManager.default().identityId

              newsItem._articleId = "YourArticleId"
              newsItem._title = "This is the Title"
              newsItem._author = "B Smith"
              newsItem._creationDate = NSDate().timeIntervalSince1970 as NSNumber
              newsItem._category = "Local News"

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

                      newsItem.setUserId(identityManager.getCachedUserID());    //partition key

                      newsItem.setArticleId("Article1");  //range (sort) key

                      dynamoDBMapper.delete(newsItem);

                      // Item deleted
                  }
              }).start();
          }


   iOS - Swift
      .. code-block:: swift

          func deleteNews() {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let itemToDelete = News()
              itemToDelete?._userId = AWSIdentityManager.default().identityId
              itemToDelete?._articleId = "YourArticleId"

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
         :emphasize-lines: 1-38

         public void queryNote() {

            new Thread(new Runnable() {
                @Override
                public void run() {
                    NewsDO note = new NewsDO();
                    note.setUserId(identityManager.getCachedUserID());
                    note.setArticleId("Article1");

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
                    updateOutput(stringBuilder.toString());

                    if (result.isEmpty()) {
                        // There were no items matching your query.
                    }
                }
            }).start();
         }


   iOS - Swift
      .. code-block:: swift
         :emphasize-lines: 0

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
                  ":userId": AWSIdentityManager.default().identityId
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
                        print("\(newsItem!._title!)")
                    }
                }
             }
          }




