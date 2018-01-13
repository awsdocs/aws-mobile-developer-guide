.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

#####################################
iOS: Amazon DynamoDB Low-level Client
#####################################

.. contents::
   :local:
   :depth: 1

Overview
--------

`Amazon DynamoDB <http://aws.amazon.com/dynamodb/>`_ is a fast, highly scalable,
highly available, cost-effective, nonrelational database service. Amazon DynamoDB removes traditional
scalability limitations on data storage while maintaining low latency and predictable
performance.

The AWS Mobile SDK for iOS provides both low-level and high-level libraries for working Amazon DynamoDB.

The low-level client described in this section allows the kind of direct access to Amazon DynamoDB tables useful for NoSQL and other non-relational data designs. The low-level client also supports conditional data writes to mitigate simultaneous write conflicts and batch data writes.

The high-level library includes :doc:`dynamodb-object-mapper`, which lets you map client-side classes to access and manipulate Amazon Dynamo tables.

Setup
-----

To set your project up to use the AWS SDK for iOS TransferUtility, take the following steps.

1. Setup the SDK, Credentials, and Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the low-level DynamoDB mobile client in a new app, follow the steps described in `Get Started <http://docs.aws.amazon.com/aws-mobile/latest/developerguide/getting-started.html>`_ to install the AWS Mobile SDK for iOS.

For apps that use an SDK version prior to 2.6.0, follow the steps on :doc:`setup-options-for-aws-sdk-for-ios` to install the AWS Mobile SDK for iOS. Then use the steps on :doc:`cognito-auth-identity-for-ios-legacy` to configure user credentials, and permissions.


2. Create or Use an Existing Amazon DynamoDB Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps on :doc:`<dynamodb-setup-for-ios-legacy>` to create a table.

3. Import the AWSDynamoDB APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following import statement to your project.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                import AWSDynamoDB


        iOS - Objective-C
            .. code-block:: objc

                #import <AWSDynamoDB/AWSDynamoDB.h>

Conditional Writes Using the Low-Level Client
---------------------------------------------

In a multi-user environment, multiple clients can access the same item and attempt to modify its attribute values at the same time. To help clients coordinate writes to data items, the Amazon DynamoDB low-level client supports conditional writes for `PutItem`, `DeleteItem`, and `UpdateItem` operations. With a conditional write, an operation succeeds only if the item attributes meet one or more expected conditions; otherwise, it returns an error.

In the following example, we update the price of an item in the ``Books`` table if the ``Price`` attribute of the item has a value of ``999``.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                Amazon DynamoDB = AWSDynamoDB.default()
                let updateInput = AWSDynamoDBUpdateItemInput()

                let hashKeyValue = AWSDynamoDBAttributeValue()
                hashKeyValue?.s = "4567890123"

                updateInput?.tableName = "Books"
                updateInput?.key = ["ISBN": hashKeyValue!]

                let oldPrice = AWSDynamoDBAttributeValue()
                oldPrice?.n = "999"

                let expectedValue = AWSDynamoDBExpectedAttributeValue()
                expectedValue?.value = oldPrice

                let newPrice = AWSDynamoDBAttributeValue()
                newPrice?.n = "1199"

                let valueUpdate = AWSDynamoDBAttributeValueUpdate()
                valueUpdate?.value = newPrice
                valueUpdate?.action = .put

                updateInput?.attributeUpdates = ["Price": valueUpdate!]
                updateInput?.expected = ["Price": expectedValue!]
                updateInput?.returnValues = .updatedNew

               Amazon DynamoDB.updateItem(updateInput!).continueWith { (task:AWSTask<AWSDynamoDBUpdateItemOutput>) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                        return nil
                    }

                    // Do something with task.result

                    return nil
                }


        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDB *dynamoDB = [AWSDynamoDB defaultDynamoDB];
                AWSDynamoDBUpdateItemInput *updateInput = [AWSDynamoDBUpdateItemInput new];

                AWSDynamoDBAttributeValue *hashKeyValue = [AWSDynamoDBAttributeValue new];
                hashKeyValue.S = @"4567890123";

                updateInput.tableName = @"Books";
                updateInput.key = @{ @"ISBN" : hashKeyValue };

                AWSDynamoDBAttributeValue *oldPrice = [AWSDynamoDBAttributeValue new];
                oldPrice.N = @"999";

                AWSDynamoDBExpectedAttributeValue *expectedValue = [AWSDynamoDBExpectedAttributeValue new];
                expectedValue.value = oldPrice;

                AWSDynamoDBAttributeValue *newPrice = [AWSDynamoDBAttributeValue new];
                newPrice.N = @"1199";

                AWSDynamoDBAttributeValueUpdate *valueUpdate = [AWSDynamoDBAttributeValueUpdate new];
                valueUpdate.value = newPrice;
                valueUpdate.action = AWSDynamoDBAttributeActionPut;

                updateInput.attributeUpdates = @{@"Price": valueUpdate};
                updateInput.expected = @{@"Price": expectedValue};
                updateInput.returnValues = AWSDynamoDBReturnValueUpdatedNew;

                [[dynamoDB updateItem:updateInput]
                 continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else {
                         //Do something with task.result.
                     }
                     return nil;
                 }];

Conditional writes are idempotent. In other words, if a conditional write request is made multiple times, the update will be performed only in the first instance unless the content of the request changes. In the preceding example, sending the same request a second time results in a `ConditionalCheckFailedException`, because the expected condition is not met after the first update.

.. _batch-operations:

Batch Operations Using the Low-Level Client
-------------------------------------------

The Amazon DynamoDB low-level client provides batch write operations to put items in the database and delete items from the database. You can also use batch get operations to return the attributes of one or more items from one or more tables.

The following example shows a batch write operation.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                Amazon DynamoDB = AWSDynamoDB.default()

                //Write Request 1
                let hashValue1 = AWSDynamoDBAttributeValue()
                hashValue1?.s = "3210987654"
                let otherValue1 = AWSDynamoDBAttributeValue()
                otherValue1?.s = "Some Title"

                let writeRequest = AWSDynamoDBWriteRequest()
                writeRequest?.putRequest = AWSDynamoDBPutRequest()
                writeRequest?.putRequest?.item = ["ISBN": hashValue1!, "Title": otherValue1!]

                //Write Request 2
                let hashValue2 = AWSDynamoDBAttributeValue()
                hashValue2?.s = "8901234567"
                let otherValue2 = AWSDynamoDBAttributeValue()
                otherValue2?.s = "Another Title"

                let writeRequest2 = AWSDynamoDBWriteRequest()
                writeRequest2?.putRequest = AWSDynamoDBPutRequest()
                writeRequest2?.putRequest?.item = ["ISBN": hashValue2!, "Title": otherValue2!]

                let batchWriteItemInput = AWSDynamoDBBatchWriteItemInput()
                batchWriteItemInput?.requestItems = ["Books": [writeRequest!, writeRequest2!]]

               Amazon DynamoDB.batchWriteItem(batchWriteItemInput!).continueWith { (task:AWSTask<AWSDynamoDBBatchWriteItemOutput>) -> Any? in
                    if let error = task.error as? NSError {
                        print("The request failed. Error: \(error)")
                        return nil
                    }

                    // Do something with task.result

                    return nil
                }

        iOS - Objective-C
            .. code-block:: objc

                AWSDynamoDB *dynamoDB = [AWSDynamoDB defaultDynamoDB];

                //Write Request 1
                AWSDynamoDBAttributeValue *hashValue1 = [AWSDynamoDBAttributeValue new];
                hashValue1.S = @"3210987654";
                AWSDynamoDBAttributeValue *otherValue1 = [AWSDynamoDBAttributeValue new];
                otherValue1.S = @"Some Title";

                AWSDynamoDBWriteRequest *writeRequest = [AWSDynamoDBWriteRequest new];
                writeRequest.putRequest = [AWSDynamoDBPutRequest new];
                writeRequest.putRequest.item = @{
                                                 @"ISBN" : hashValue1,
                                                 @"Title" : otherValue1
                                                 };

                //Write Request 2
                AWSDynamoDBAttributeValue *hashValue2 = [AWSDynamoDBAttributeValue new];
                hashValue2.S = @"8901234567";
                AWSDynamoDBAttributeValue *otherValue2 = [AWSDynamoDBAttributeValue new];
                otherValue2.S = @"Another Title";

                AWSDynamoDBWriteRequest *writeRequest2 = [AWSDynamoDBWriteRequest new];
                writeRequest2.putRequest = [AWSDynamoDBPutRequest new];
                writeRequest2.putRequest.item = @{
                                                @"ISBN" : hashValue2,
                                                @"Title" : otherValue2
                                                };

                AWSDynamoDBBatchWriteItemInput *batchWriteItemInput = [AWSDynamoDBBatchWriteItemInput new];
                batchWriteItemInput.requestItems = @{@"Books": @[writeRequest,writeRequest2]};

                [[dynamoDB batchWriteItem:batchWriteItemInput]
                 continueWithBlock:^id(AWSTask *task) {
                     if (task.error) {
                         NSLog(@"The request failed. Error: [%@]", task.error);
                     } else  {
                        //Do something with task.result.
                    }
                    return nil;
                }];

Additional Resources
--------------------

* `Amazon DynamoDB Developer Guide <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/>`_
* `Amazon DynamoDB API Reference <http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/>`_

