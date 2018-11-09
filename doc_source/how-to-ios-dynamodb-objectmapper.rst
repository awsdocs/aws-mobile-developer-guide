.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _how-to-ios-dynamodb-objectmapper:

######################################
iOS: Amazon DynamoDB Object Mapper API
######################################

.. list-table::
   :widths: 1

   * - The following reference content only applies to existing apps that were built using the AWS Mobile SDKs for iOS and Android. If you’re building a new mobile or web app, or you're adding cloud capabilities to an existing app, visit the `Amplify Framework <https://amzn.to/am-amplify-docs>`__ website instead. Documentation for the AWS Mobile SDKs for iOS and Android is now part of the Amplify Framework.

.. contents::
   :local:
   :depth: 1

Overview
--------

`Amazon DynamoDB <http://aws.amazon.com/dynamodb/>`__ is a fast, highly scalable,
highly available, cost-effective, non-relational database service. Amazon DynamoDB removes traditional
scalability limitations on data storage while maintaining low latency and predictable
performance.

The AWS Mobile SDK for iOS provides both low-level and high-level libraries for working with
Amazon DynamoDB.

The high-level library described in this section provides Amazon DynamoDB object mapper which lets you map client-side classes to tables. Working within the data model defined on your client you can write simple, readable code that stores and retrieves objects in the cloud.

The :doc:`dynamodb-low-level-client` provides useful ways to perform operations
like conditional writes and batch operations.

Setup
-----

To set your project up to use the AWS SDK for iOS :code:`dynamoDBObjectMapper`, take the following steps.

Set Up the SDK, Credentials, and Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To integrate :code:`dynamoDBObjectMapper` into a new app, follow the steps described in :ref:`Get Started <mobile-getting-started>` to install the AWS Mobile SDK for iOS.


Instantiate the Object Mapper API
---------------------------------

In this section:

.. contents::
   :local:
   :depth: 1

Import the AWSDynamoDB APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following import statement to your project.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                import AWSDynamoDB


        iOS - Objective-C
            .. code-block:: objc

                #import <AWSDynamoDB/AWSDynamoDB.h>

Create Amazon DynamoDB Object Mapper Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the `AWSDynamoDBObjectMapper <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSDynamoDBObjectMapper.html>`__ to map a client-side class to your database. The object mapper supports high-level operations like creating, getting, querying, updating, and deleting records. Create an object mapper as follows.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                dynamoDBObjectMapper = AWSDynamoDBObjectMapper.default()


        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDBObjectMapper *dynamoDBObjectMapper = [AWSDynamoDBObjectMapper defaultDynamoDBObjectMapper];

Object mapper methods return an ``AWSTask`` object. for more information, see :ref:`Working with Asynchronous Tasks <how-to-ios-topics-aysnchronous-tasks>`.

Define a Mapping Class
~~~~~~~~~~~~~~~~~~~~~~

An Amazon DynamoDB database is a collection of tables, and a table can be described as follows:

* A table is a collection of items.
* Each item is a collection of attributes.
* Each attribute has a name and a value.

For the bookstore app, each item in the table represents a book, and each item has
four attributes: :dfn:`Title`, :dfn:`Author`, :dfn:`Price`, and :dfn:`ISBN`.

Each item (Book) in the table has a :guilabel:`Primary key`, in this case, the primary key is ``ISBN``.

To directly manipulate database items through their object representation, map each item in the
Book table to a ``Book`` object in the client-side code, as shown in the following code. Attribute names are case sensitive.


    .. container:: option

        iOS - Swift
            .. code-block:: swift

                import AWSDynamoDB

                class Book : AWSDynamoDBObjectModel, AWSDynamoDBModeling  {
                    @objc var Title:String?
                    @objc var Author:String?
                    @objc var Price:String?
                    @objc var ISBN:String?

                    class func dynamoDBTableName() -> String {
                        return "Books"
                    }

                    class func hashKeyAttribute() -> String {
                        return "ISBN"
                    }
                }

        iOS - Objective-C
            .. code-block:: objc

                #import <AWSDynamoDB/AWSDynamoDB.h>
                #import "Book.h"

                @interface Book : AWSDynamoDBObjectModel <AWSDynamoDBModeling>

                @property (nonatomic, strong) NSString *Title;
                @property (nonatomic, strong) NSString *Author;
                @property (nonatomic, strong) NSNumber *Price;
                @property (nonatomic, strong) NSString *ISBN;

                @end


                @implementation Book

                + (NSString *)dynamoDBTableName {
                    return @"Books";
                }

                + (NSString *)hashKeyAttribute {
                    return @"ISBN";
                }

                @end


.. note::

   As of SDK version 2.0.16, the ``AWSDynamoDBModel`` mapping class is deprecated and replaced by ``AWSDynamoDBObjectModel``. For information on migrating your legacy code, see :ref:`awsdynamodb-model`.


To conform to the ``AWSDynamoDBModeling`` protocol, implement ``dynamoDBTableName``, which returns the name of the table, and ``hashKeyAttribute``, which returns the name of the primary key. If the table has a range key, implement ``+ (NSString *)rangeKeyAttribute``.

CRUD Operations
---------------

.. contents::
   :local:
   :depth: 1

The Amazon DynamoDB table, mapping class, and object mapper client enable your app to interact with objects in the cloud.

Save an Item
~~~~~~~~~~~~

The `save: <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSDynamoDBObjectMapper.html#//api/name/save:>`__ method saves an object to Amazon DynamoDB, using the default configuration. As a parameter, ``save:`` takes a an object that inherits from ``AWSDynamoDBObjectModel`` and conforms to the ``AWSDynamoDBModeling`` protocol. The properties of this object will be mapped to attributes in Amazon DynamoDB table.

To create the object to be saved take the following steps.

#. Define the object and it's properties to match your table model.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let myBook = Book()
                myBook?.ISBN = "3456789012"
                myBook?.Title = "The Scarlet Letter"
                myBook?.Author = "Nathaniel Hawthorne"
                myBook?.Price = 899 as NSNumber?


        iOS - Objective-C
            .. code-block:: objc

                Book *myBook = [Book new];
                myBook.ISBN = @"3456789012";
                myBook.Title = @"The Scarlet Letter";
                myBook.Author = @"Nathaniel Hawthorne";
                myBook.Price = [NSNumber numberWithInt:899];

#. Pass the object to the ``save:`` method.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

               dynamoDBObjectMapper.save(myBook).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                    } else {
                        // Do something with task.result or perform other operations.
                    }
                })


        iOS - Objective-C
            .. code-block:: objc

                [[dynamoDBObjectMapper save:myBook]
                continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         //Do something with task.result or perform other operations.
                     }
                     return nil;
                 }];

Save Behavior Options
^^^^^^^^^^^^^^^^^^^^^

The AWS Mobile SDK for iOS supports the following save behavior options:

* ``AWSDynamoDBObjectMapperSaveBehaviorUpdate``

  This option does not affect unmodeled attributes on a save operation. Passing a nil value for the modeled attribute removes the attribute from the corresponding item in Amazon DynamoDB. By default, the object mapper uses this behavior.

* ``AWSDynamoDBObjectMapperSaveBehaviorUpdateSkipNullAttributes``

  This option is similar to the default update behavior, except that it ignores any null value attribute(s) and does not remove them from an item in Amazon DynamoDB.

* ``AWSDynamoDBObjectMapperSaveBehaviorAppendSet``

  This option treats scalar attributes (String, Number, Binary) the same as the ``AWSDynamoDBObjectMapperSaveBehaviorUpdateSkipNullAttributes`` option. However, for set attributes, this option  appends to the existing attribute value instead of overriding it. The caller must ensure that the modeled attribute type matches the existing set type; otherwise, a service exception occurs.

* ``AWSDynamoDBObjectMapperSaveBehaviorClobber``

  This option clears and replaces all attributes, including unmodeled ones, on save. Versioned field constraints are be disregarded.

The following code provides an example of setting a default save behavior on the object mapper.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let updateMapperConfig = AWSDynamoDBObjectMapperConfiguration()
                updateMapperConfig.saveBehavior = .updateSkipNullAttributes

        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDBObjectMapperConfiguration *updateMapperConfig = [AWSDynamoDBObjectMapperConfiguration new];
                updateMapperConfig.saveBehavior = AWSDynamoDBObjectMapperSaveBehaviorUpdateSkipNullAttributes;

Use ``updateMapperConfig`` as an argument when calling `save:configuration: <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSDynamoDBObjectMapper.html#//api/name/save:configuration:>`__.

Retrieve an Item
~~~~~~~~~~~~~~~~

Using an object's primary key, in this case, ``ISBN``, we can load the corresponding item from the database. The following code returns the Book item with an ISBN of ``6543210987``.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

               dynamoDBObjectMapper.load(Book.self, hashKey: "6543210987" rangeKey:nil).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                    } else if let resultBook = task.result as? Book {
                        // Do something with task.result.
                    }
                    return nil
                })


        iOS - Objective-C
            .. code-block:: objc

                [[dynamoDBObjectMapper load:[Book class] hashKey:@"6543210987" rangeKey:nil]
                continueWithBlock:^id(AWSTask *task) {
                    if (task.error) {
                        NSLog(@"The request failed. Error: [%@]", task.error);
                    } else {
                        //Do something with task.result.
                    }
                    return nil;
                }];


The object mapper creates a mapping between the ``Book`` item returned from the database and the ``Book`` object on the client (here, ``resultBook``). Access the title at ``resultBook.Title``.

Since the Books database does not have a range key, ``nil`` was passed to the ``rangeKey`` parameter.

Update an Item
~~~~~~~~~~~~~~

To update an item in the database, just set new attributes and save the objects. The primary
key of an existing item, ``myBook.ISBN`` in the ``Book`` object mapper example, cannot be changed. If you save
an existing object with a new primary key, a new item with the same attributes and the new primary key are created.

Delete an Item
~~~~~~~~~~~~~~

To delete a table row, use the `remove:` method.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let bookToDelete = Book()
                bookToDelete?.ISBN = "4456789012";

               dynamoDBObjectMapper.remove(bookToDelete).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                    } else {
                        // Item deleted.
                    }
                })


        iOS - Objective-C
            .. code-block:: objc

                Book *bookToDelete = [Book new];
                bookToDelete.ISBN = @"4456789012";

                [[dynamoDBObjectMapper remove:bookToDelete]
                 continueWithBlock:^id(AWSTask *task) {

                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         //Item deleted.
                     }
                     return nil;
                 }];

Perform a Scan
--------------

A scan operation retrieves in an undetermined order.

The ``scan:expression:`` method takes two parameters: the class of the resulting object and an instance of ``AWSDynamoDBScanExpression``, which provides options for filtering results.

The following example shows how to create an ``AWSDynamoDBScanExpression`` object, set its ``limit`` property, and then pass the ``Book`` class and the expression object to ``scan:expression:``.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let scanExpression = AWSDynamoDBScanExpression()
                scanExpression.limit = 20

               dynamoDBObjectMapper.scan(Book.self, expression: scanExpression).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                    } else if let paginatedOutput = task.result {
                        for book in paginatedOutput.items as! Book {
                            // Do something with book.
                        }
                    }
                })


        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDBScanExpression *scanExpression = [AWSDynamoDBScanExpression new];
                scanExpression.limit = @10;

                [[dynamoDBObjectMapper scan:[Book class]
                        expression:scanExpression]
                continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         AWSDynamoDBPaginatedOutput *paginatedOutput = task.result;
                         for (Book *book in paginatedOutput.items) {
                             //Do something with book.
                         }
                     }
                     return nil;
                }];

Filter a Scan
~~~~~~~~~~~~~

The output of a scan is returned as an ``AWSDynamoDBPaginatedOutput`` object. The array of returned items is in the ``items`` property.

The ``scanExpression`` method provides several optional parameters. Use ``filterExpression``
and ``expressionAttributeValues`` to specify a scan result for the attribute names and conditions
you define. For more information about the parameters and the API, see
`AWSDynamoDBScanExpression <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSDynamoDBScanExpression.html>`__.

The following code scans the Books table to find books with a price less than 50.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let scanExpression = AWSDynamoDBScanExpression()
                scanExpression.limit = 10
                scanExpression.filterExpression = "Price < :val"
                scanExpression.expressionAttributeValues = [":val": 50]

               dynamoDBObjectMapper.scan(Book.self, expression: scanExpression).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                  if let error = task.error as? NSError {
                      print("The request failed. Error: \(error)")
                  } else if let paginatedOutput = task.result {
                      for book in paginatedOutput.items as! Book {
                          // Do something with book.
                      }
                  }
                })

        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDBScanExpression *scanExpression = [AWSDynamoDBScanExpression new];
                scanExpression.limit = @10;
                scanExpression.filterExpression = @"Price < :val";
                scanExpression.expressionAttributeValues = @{@":val":@50};

                [[dynamoDBObjectMapper scan:[Book class]
                             expression:scanExpression]
                continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         AWSDynamoDBPaginatedOutput *paginatedOutput = task.result;
                         for (Book *book in paginatedOutput.items) {
                             //Do something with book.
                         }
                     }
                     return nil;
                 }];

You can also use the ``projectionExpression` property to specify the attributes to retrieve from the ``Books`` table. For example adding ``scanExpression.projectionExpression = @"ISBN, Title, Price";``  in the previous code snippet retrieves only those three properties in the book object. The ``Author`` property in the book object will always be nil.

Perform a Query
---------------

The query API enables you to query a table or a secondary index. The ``query:expression:`` method takes two parameters: the class of the resulting object and an instance of ``AWSDynamoDBQueryExpression``.

To query an index, you must also specify the ``indexName``. You must specify the ``hashKeyAttribute`` if you query a global secondary with a different ``hashKey``. If the table or index has a range key, you can optionally refine the results by providing a range key value and a condition.

The following example illustrates querying the `Books` index table to find all books whose author is "John Smith", with a price less than 50.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let queryExpression = AWSDynamoDBQueryExpression()
                queryExpression.indexName = "Author-Price-index"

                queryExpression.keyConditionExpression = @"Author = :authorName AND Price < :val";
                queryExpression.expressionAttributeValues = @{@":authorName": @"John Smith", @":val": @50};

               dynamoDBObjectMapper.query(Book.self, expression: queryExpression).continueWith(block: { (task:AWSTask<AnyObject>!) -> Any? in
                    if let error = task.error as? NSError {
                          print("The request failed. Error: \(error)")
                    } else if let paginatedOutput = task.result {
                        for book in paginateOutput.items as! Book {
                            // Do something with book.
                        }
                    }
                    return nil
                })

        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDBQueryExpression *queryExpression = [AWSDynamoDBQueryExpression new];

                queryExpression.indexName = @"Author-Price-index";

                queryExpression.keyConditionExpression = @"Author = :authorName AND Price < :val";

                queryExpression.expressionAttributeValues = @{@":authorName": @"John Smith", @":val":@50};

                [[dynamoDBObjectMapper query:[Book class]
                        expression:queryExpression]
                continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         AWSDynamoDBPaginatedOutput *paginatedOutput = task.result;
                         for (Book *book in paginatedOutput.items) {
                             //Do something with book.
                         }
                     }
                     return nil;
                 }];

In the preceding example, ``indexName`` is specified to demonstrate querying an index.
The query expression is specified using ``keyConditionExpression`` and the values used in the
expression using ``expressionAttributeValues``.

You can also provide ``filterExpression`` and ``projectionExpression`` in ``AWSDynamoDBQueryExpression``. The syntax is the same as that used in a scan operation.

For more information, see `AWSDynamoDBQueryExpression <http://docs.aws.amazon.com/AWSiOSSDK/latest/Classes/AWSDynamoDBQueryExpression.html>`__.

.. _awsdynamodb-model:

:guilabel:`Migrating AWSDynamoDBModel to AWSDynamoDBObjectModel`

As of SDK version 2.0.16, the ``AWSDynamoDBModel`` mapping class is deprecated and replaced by ``AWSDynamoDBObjectModel``.The deprecated ``AWSDynamoDBModel`` used `NSArray` to represent
multi-valued types (``String Set``, ``Number Set``, and ``Binary Set``); it did not support
``Boolean``, ``Map``, or ``List`` types. The new ``AWSDynamoDBObjectModel`` uses ``NSSet`` for
multi-valued types and supports ``Boolean``, ``Map``, and ``List``. For the ``Boolean`` type,
you create an ``NSNumber`` using ``[NSNumber numberWithBool:YES]`` or using the shortcuts
``@YES`` and ``@NO``. For the Map type, create using ``NSDictionary``. For the List type, create
using ``NSArray``.

Additional Resources
--------------------

* `Amazon DynamoDB Developer Guide <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`__
* `Amazon DynamoDB API Reference <http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/>`__
