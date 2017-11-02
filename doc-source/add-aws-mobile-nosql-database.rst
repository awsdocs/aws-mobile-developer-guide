.. _add-aws-mobile-nosql-database:

#####################################
Add NoSQL Database to Your Mobile App
#####################################


.. meta::
   :description: Integrating nosql database


.. _add-aws-mobile-nosql-database-overview:

NoSQL Database
==============


The AWS Mobile Hub :ref:`nosqldb` feature uses `Amazon DynamoDB <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`_ to enable you to create database tables
that can store and retrieve data for use by your apps.


.. _add-aws-mobile-nosql-database-backend-setup:

Set Up Your Backend
===================


#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the
   integration steps on this page.

#. Use |AMHlong| to deploy and configure your AWS services in minutes.


   #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create
      project`.

      Or select an existing project.

   #. Choose the :guilabel:`NoSQL Database` tile to enable the feature.

   #. Follow the console work flow to define the tables you need. See :ref:`config-nosqldb` for
      details.

   #. Download your |AMH| project configuration file.


      #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon
         on the left.

      #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json`
         file that connects your app to your backend.

         .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
            :scale: 100
            :alt: Image of the Download Configuration Files button in the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
               :scale: 75

      #. Under :guilabel:`NoSQL / Cloud Logic` at the bottom of the page, choose the
         :guilabel:`Downloads` menu, and then choose your platform.

         .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
            :scale: 100
            :alt: Image of the Download Configuration Files button in the |AMH| console.

         .. only:: pdf

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 50

         .. only:: kindle

            .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
               :scale: 75

      :emphasis:`Remember:`

      Each time you change the |AMH| project for your app, download and use an updated
      :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or
      Cloud Logic are changed, also download and use updated files for those features.


.. _add-aws-mobile-nosql-database-app:

Add the SDK to Your App
=======================


**To add AWS Mobile NoSQL Database to your app**

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following
         :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml
               :emphasize-lines: 0

                <uses-permission android:name="android.permission.INTERNET" />
                <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
                <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

         #. :file:`app/build.gradle` must contain:

            .. code-block:: java
               :emphasize-lines: 2

                dependencies{
                    compile 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'
                }

         #. For each Activity where you make calls to perform database operations, import the
            following APIs.

            .. code-block:: java
               :emphasize-lines: 0

                import com.amazonaws.mobile.config.AWSConfiguration;
                import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;
                import static com.amazonaws.auth.policy.actions.DynamoDBv2Actions.Query;

      #. Create a :code:`DynamoDBMapper` client for your app as in the following
         example.

         .. code-block:: java
            :emphasize-lines: 0, 6, 24

             import static com.amazonaws.auth.policy.actions.DynamoDBv2Actions.Query;

             public class MainActivity extends AppCompatActivity {
                 DynamoDBMapper dynamoDBMapper;

                 String userId = "";

                 @Override
                 protected void onCreate(Bundle savedInstanceState) {
                     super.onCreate(savedInstanceState);
                     setContentView(R.layout.activity_main);

                     Context appContext = getApplicationContext();

                     final AWSCredentialsProvider credentialsProvider = AWSIdentityManager.getDefault().getCredentialsProvider();
                     userId = identityManager.getCachedUserID();
                     AmazonDynamoDBClient dynamoDBClient = new AmazonDynamoDBClient(credentialsProvider);
                     this.dynamoDBMapper = DynamoDBMapper.builder()
                                                         .dynamoDBClient(dynamoDBClient)
                                                         .awsConfiguration(awsConfig)
                                                         .build();
             }

      #. Add the project configuration and data model files you downloaded from the
         |AMH| console. The data models provide set and get methods for each attribute of a |DDB|
         table they model.

         #. Right-click your app's :file:`res` folder, and then choose :guilabel:`New > Android
            Resource Directory`. Select :guilabel:`raw` in the :guilabel:`Resource type` dropdown
            menu.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of the Download Configuration Files button in the |AMH| console.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         #. From the location where configuration files were downloaded in a previous step, drag
            :file:`awsconfiguration.json` into the :file:`res/raw` folder.

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

                    pod 'AWSDynamoDB', '~> 2.6.5'
                    # other pods
                end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |DDB| APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSDynamoDB

      #. Add the backend service configuration and data model files you downloaded from the |AMH|
         console, The data object files provide set and get methods for each attribute of a |DDB|
         table they model.


         #. From the location where your |AMH| configuration file was downloaded in a previous step,
            drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist`
            file in your Xcode project.

            Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

         #. From the location where you downloaded the data model file(s), drag and drop each file
            with the form of :file:`{your-table-name}.swift` into the folder that contains your
            :file:`AppDelegate.swift`.

            Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.



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
         :emphasize-lines: 2, 8

          public void createNews() {
                  final NewsDO newsItem = new NewsDO();

                  // Use IdentityManager to get the user identity id.
                  newsItem.setUserId(this.userId);

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

          @IBAction func addButton(_ sender: Any) {

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              //Create data object using data models you downloaded from Mobile Hub
              let newsItem: News = News();

              // Use AWSIdentityManager.default().identityId here to get the user identity id.
              newsItem.setUserId({"us-east-1:01234567-89ab-123c-4de5-fab678cde901"});

              newsItem._articleId = "YourArticleId"
              newsItem._title = "YourTitlestring"
              newsItem._author = "YourAuthor"
              newsItem._creationDate = "YourCreateDate"

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
         :emphasize-lines: 12, 20

          public void readNews() {
              new Thread(new Runnable() {
                  @Override
                  public void run() {


                      NewsDO newsItem = dynamoDBMapper.load(
                              NewsDO.class,

                              // Use IdentityManager to get the user identity id.
                              userId,

                              "Article1");

                      // Item read
                      // Log.d("News Item:", newsItem.toString());
                  }
              }).start();
          }


   iOS - Swift
      .. code-block:: swift

         @IBAction func readButton(_ sender: Any) {

           let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

               //Create data object using data models you downloaded from Mobile Hub
               let newsItem: News = News();

               dynamoDbObjectMapper.load(
                  // Use AWSIdentityManager.default().identityId here to get the user identity id.
                  newsItem.setUserId("us-east-1:01234567-89ab-123c-4de5-fab678cde901"),
                  News.self,
                  hashKey: userId,
                  rangeKey: rangeKey,
                  completionHandler: {
                      (error: Error?) -> Void in

                     if let error = error {
                          print("Amazon DynamoDB Save Error: \(error)")
                          return
                      }
                      print("An item was saved.")
                  })
          }



.. _add-aws-mobile-nosql-database-crud-update:

Update an Item
--------------


Use the following code to update an item in your NoSQL Database table.

.. container:: option

   Android - Java
      .. code-block:: java
         :emphasize-lines: 2, 8

          public void updateNews() {
              final NewsDO newsItem = new NewsDO();

              // Use IdentityManager.getUserIdentityId() here to get the user identity id.
              newsItem.setUserId(userId);

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

          @IBAction func UpdateButton(_ sender: Any) {

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let newsItem: News = News();

              // Use AWSIdentityManager.default().identityId here to get the user identity id.
              newsItem._userId = {"us-east-1:01234567-89ab-123c-4de5-fab678cde901"}

              newsItem._articleId = "article1"
              newsItem._title = "This is the Title"
              newsItem._author = "B Smith"
              newsItem._creationDate = "04/21/1978"
              newsItem._category = "Local News"


              print("Start updating an item.")

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
         :emphasize-lines: 2, 16

          public void deleteNews() {
              new Thread(new Runnable() {
                  @Override
                  public void run() {

                      NewsDO newsItem = new NewsDO();

                      // Use IdentityManager.getUserIdentityId() here to get the user identity id.
                      newsItem.setUserId(userId);    //partition key

                      newsItem.setArticleId("Article1");  //range (sort) key

                      dynamoDBMapper.delete(newsItem);

                      // Item deleted
                  }
              }).start();
          }


   iOS - Swift
      .. code-block:: swift

          @IBAction func deleteButton(_ sender: Any) {

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let itemToDelete = News()

              // Use IdentityManager to get the user identity id.
              itemToDelete?._userId = "us-east-1:01234567-89ab-123c-4de5-fab678cde901"

              itemToDelete?._title = "This is the Title"
              itemToDelete?._articleId = "Article1"


              dynamoDbObjectMapper.remove(itemToDelete!, completionHandler: {(error: Error?) -> Void in
                  if let error = error {
                      print(" Amazon DynamoDB Save Error: \(error)")
                      return
                  }
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
         :emphasize-lines: 14, 30, 82, 92

         public void queryNote() {

            new Thread(new Runnable() {
                @Override
                public void run() {
                    NewsDO note = new NewsDO();
                    note.setUserId(this.userId);
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

                    updateOutput(stringBuilder.toString());

                    if (result.isEmpty()) {
                        // There were no items matching your query.
                    }
                }
            }).start();
         }


   iOS - Swift
      .. code-block:: swift
         :emphasize-lines: 8, 40

          @IBAction func queryButton(_ sender: Any) {

              // 1) Configure the query

                  let queryExpression = AWSDynamoDBQueryExpression()

                  queryExpression.keyConditionExpression = "#articleId > :articleId AND #userId = :userId"

                  queryExpression.filterExpression = "#author = :author"
                  queryExpression.expressionAttributeNames = [
                      "#userId": "userId",
                      "#articleId": "articleId"
                  ]
                  queryExpression.expressionAttributeValues = [
                      ":articleId": "SomeArticleId",
                      ":userId": "us-east-1:12312:213123123:Sdfsdfds:sdfdsfsd:23123"
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




