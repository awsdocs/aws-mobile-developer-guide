.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-ios-aws-mobile-notes-data:

#######################################
Add Online Data Access to the Notes App
#######################################

In the :ref:`previous section <tutorial-ios-aws-mobile-notes-auth>` of this tutorial, we added a simple sign-up / sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-ios-aws-mobile-notes-setup>`. In this tutorial, we will add a NoSQL
database to our mobile backend, then configure a basic data access service to the note-taking app.

The notes app uses iOS `Core Data <https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CoreData/index.html>`__ as a persistence framework. :code:`NotesContentProvider.swift` is custom content provider used as a clean interface for managing your application content locally. In the following steps, you will modify the content provider code to use DynamoDB and sync with the local Core data.

You should be able to complete this section of the tutorial in about 30-45 minutes.

Set Up Your Backend
-------------------

To add User Sign-in to your app you will create the backend resources in your |AMH| project, and then update the configuration file in your app.

Add a NoSQL Database to the AWS Mobile Hub Project
--------------------------------------------------

Before we work on the client-side code, we need to add a NoSQL database
and table to the backend project:

#. Right-click :file:`awsconfiguration.json` in your Xcode Project Navigator, choose :guilabel:`Delete`, and then choose :guilabel:`Move to trash`.
#. Open the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.
#. Select  your project.
#. Scroll down to the :guilabel:`Add More Backend Features` section and then choose the :guilabel:`NoSQL Database` tile.
#. Choose :guilabel:`Enable NoSQL`, choose :guilabel:`Add Table`, and then choose :guilabel:`Example` to start with an example schema.
#. Choose :guilabel:`Notes`, which most closely matches the model we wish to use.
#. Choose :guilabel:`Add attribute`, then fill in the details of the new attribute:

    -  :guilabel:`Attribute name`: :userinput:`updatedDate`
    -  :guilabel:`Type`: :userinput:`number`

#.  Choose :guilabel:`Add index` then fill in the details of the new index:

    -  :guilabel:`Index name`: :userinput:`LastUpdated`
    -  :guilabel:`Partition key`: :userinput:`userId`
    -  :guilabel:`Sort key`: :userinput:`updatedDate`

#. Choose :guilabel:`Create table`
#. Choose :guilabel:`Create table` in the modal dialog.
#. Choose your project name in the upper left and then choose :guilabel:`Integrate` on your iOS app card.
#. Choose :guilabel:`Download Cloud Config` to get an updated :file:`awsconfiguration.json` file.


Connect to Your Backend
-----------------------

To update the linkage between your app and your AWS services:

#. Drag :file:`awsconfiguration.json` from your download location into the Xcode project folder containing :file:`Info.plist`. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog. Choose :guilabel:`Finish`.

Your system may have modified the filename to avoid conflicts. Make sure the file you add to your Xcode project is named :file:`awsconfiguration.json`.

Download the Models
-------------------

To aid in implementing a provider for the table you created, |AMH| generated a data model descriptor file. To add the data model to your project:

#. Choose your project name in the upper left and then choose :guilabel:`Integrate` on the iOS app card.
#. Choose :guilabel:`Swift Models` under :guilabel:`Download Models`.
#. Unpack the downloaded ZIP file.
#. Find :file:`Notes.swift`, and then drag and drop it into the folder in Xcode that contains file:`Info.plist`. Select :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog. Choose :guilabel:`Finish`.

Add NoSQL Data Dependencies
---------------------------

#. Add the following NoSQL Data  dependencies in your project's :file:`Podfile`

   .. code-block:: bash

      platform :ios, '9.0'
      target :'MyNotes' do
          use_frameworks!

            # Analytics dependency
            pod 'AWSPinpoint', '~> 2.6.5'

            # Auth dependencies
            pod 'AWSUserPoolsSignIn', '~> 2.6.5'
            pod 'AWSAuthUI', '~> 2.6.5'
            pod 'AWSMobileClient', '~> 2.6.5'

            # NoSQL Data dependencies
            pod 'AWSDynamoDB', '~> 2.6.5'

          # other pods
      end

   Then, in a terminal run:

   .. code-block:: bash

      pod install --repo-update


Implement Mutation Methods
--------------------------

:code:`NotesContentProvider` is the basic interface the app uses to communicate with Core data and your NoSQL table in Amazon DynamoDB. Mutation events handle the CRUD operations when you call its :code:`insertNoteDDB`, :code:`updateNoteDDB`, and :code:`deleteNoteDDB` methods.

To add these mutation methods to the :code:`NotesContentProvider` class, add the following import statement to the file.

.. code-block:: swift

   import AWSDynamoDB
   import AWSAuthCore

Then add CRUD functions (insert, update, and delete) to the NotesContentProvider to the class as follows.

.. code-block:: swift

   public class NotesContentProvider  {

            // . . .

      //Insert a note using Amazon DynamoDB
      func insertNoteDDB(noteId: String, noteTitle: String, noteContent: String) -> String {

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              // Create a Note object using data model you downloaded from Mobile Hub
              let noteItem: Notes = Notes()

              noteItem._userId = AWSIdentityManager.default().identityId
              noteItem._noteId = noteId
              noteItem._title = emptyTitle
              noteItem._content = emptyContent
              noteItem._creationDate = NSDate().timeIntervalSince1970 as NSNumber

              //Save a new item
              dynamoDbObjectMapper.save(noteItem, completionHandler: {
                  (error: Error?) -> Void in

                  if let error = error {
                      print("Amazon DynamoDB Save Error on new note: \(error)")
                      return
                  }
                  print("New note was saved to DDB.")
              })

              return noteItem._noteId!
          }

      //Insert a note using Amazon DynamoDB
      func updateNoteDDB(noteId: String, noteTitle: String, noteContent: String)  {

              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let noteItem: Notes = Notes()

              noteItem._userId = AWSIdentityManager.default().identityId
              noteItem._noteId = noteId

              if (!noteTitle.isEmpty){
                  noteItem._title = noteTitle
              } else {
                  noteItem._title = emptyTitle
              }

              if (!noteContent.isEmpty){
                  noteItem._content = noteContent
              } else {
                  noteItem._content = emptyContent
              }

              noteItem._updatedDate = NSDate().timeIntervalSince1970 as NSNumber
              let updateMapperConfig = AWSDynamoDBObjectMapperConfiguration()
              updateMapperConfig.saveBehavior = .updateSkipNullAttributes //ignore any null value attributes and does not remove in database
              dynamoDbObjectMapper.save(noteItem, configuration: updateMapperConfig, completionHandler: {(error: Error?) -> Void in
                  if let error = error {
                      print(" Amazon DynamoDB Save Error on note update: \(error)")
                      return
                  }
                  print("Existing note updated in DDB.")
              })
          }

      //Insert a note using Amazon DynamoDB
      func deleteNoteDDB(noteId: String) {
              let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

              let itemToDelete = Notes()
              itemToDelete?._userId = AWSIdentityManager.default().identityId
              itemToDelete?._noteId = noteId

              dynamoDbObjectMapper.remove(itemToDelete!, completionHandler: {(error: Error?) -> Void in
              if let error = error {
                  print(" Amazon DynamoDB Save Error: \(error)")
              return
              }
                  print("An note was deleted in DDB.")
              })
          }
   }



Implement Query Methods
-----------------------

This application always asks for the entire data set that the user is
entitled to see, so there is no need to implement complex query
management. This simplifies the :code:`query()` method considerably. The
:code:`query()` method returns a :code:`Cursor` (which is a standard mechanism
for iterating over data sets returned from databases).

Add the following query function to the NotesContentProvider class:


.. code-block:: swift

    func getNotesFromDDB() {
            // 1) Configure the query looking for all the notes created by this user (userId => Cognito identityId)
            let queryExpression = AWSDynamoDBQueryExpression()

            queryExpression.keyConditionExpression = "#userId = :userId"

            queryExpression.expressionAttributeNames = [
                "#userId": "userId",
            ]
            queryExpression.expressionAttributeValues = [
                ":userId": AWSIdentityManager.default().identityId
            ]

            // 2) Make the query
            let dynamoDbObjectMapper = AWSDynamoDBObjectMapper.default()

            dynamoDbObjectMapper.query(Notes.self, expression: queryExpression) { (output: AWSDynamoDBPaginatedOutput?, error: Error?) in
                if error != nil {
                    print("DynamoDB query request failed. Error: \(String(describing: error))")
                }
                if output != nil {
                    print("Found [\(output!.items.count)] notes")
                    for notes in output!.items {
                        let noteItem = notes as? Notes
                        print("\nNoteId: \(noteItem!._noteId!)\nTitle: \(noteItem!._title!)\nContent: \(noteItem!._content!)")
                    }
                }
            }
        }

Add Data Access Calls
---------------------

Calls to insert, update, delete, and query data stored in Amazon DynamoDB are made in :code:`MasterViewController` and :code:`DetailsViewController`.


#. To create a note in Amazon DynamoDB , add the following line in to the *insert* portion of the :code:`autoSave()` function of :code:`DetailViewController`.

    .. code-block:: javascript

       noteContentProvider?.insertNoteDDB(noteId: noteId!, noteTitle: "", noteContent: "")

#. To update a note from Amazon DynamoDB , add the following line in to the *upate* portion of the :code:`autoSave()` function of :code:`DetailViewController`.

    .. code-block:: javascript

       noteContentProvider?.updateNoteDDB(noteId: noteId!, noteTitle: noteTitle!, noteContent: noteContent!)


   .. list-table:
      :widths: 1

      * - The full :code:`autoSave()` function should look like the following.

           .. code-block:: swift

              func autoSave() {

                  // If this is a NEW note, set the Note Id
                  if (DetailViewController.noteId == nil) // Insert
                  {
                              let id = noteContentProvider?.insert(noteTitle: "", noteContent: "")

                      //Insert note in your Amazon DynamoDB table
                      _noteContentProvider?.insertNoteDDB(noteId: id!, noteTitle: "", noteContent: "")

                              DetailViewController.noteId = id
                  }
                  else // Update
                  {
                              let noteId = DetailViewController.noteId
                              let noteTitle = self.noteTitle.text
                              let noteContent = self.noteContent.text

                     //Update a note in your Amazon DynamoDB table
                     _noteContentProvider?.updateNoteDDB(noteId: noteId!, noteTitle: noteTitle!, noteContent: noteContent!)

                              noteContentProvider?.update(noteId: noteId!, noteTitle: noteTitle!, noteContent: noteContent!)

                 }


              }

#. To delete a note from Amazon DynamoDB, add the following function  in the :code:`MasterViewController`.

    .. code-block:: swift

        override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
                if editingStyle == .delete {
                    let context = fetchedResultsController.managedObjectContext
                    let noteObj = fetchedResultsController.object(at: indexPath)
                    let noteId = fetchedResultsController.object(at: indexPath).noteId

                    //Delete Note Locally
                    noteContentProvider?.delete(managedObjectContext: context, managedObj: noteObj, noteId: noteObj.noteId) //Core Data Delete

                    //Delete Note in DynamoDB
                    _noteContentProvider?.deleteNoteDDB(noteId: noteId!)
                }
            }

#. To query for all notes from Amazon DynamoDB, add the following line to the :code:`viewDidLoad()` function  in the MasterViewController:

    .. code-block:: swift

        noteContentProvider?.getNotesFromDDB()

.. list-table::
   :widths: 1 6

   * - **Note**

     - Differences from a real implementation

       We've taken a simplified approach for this content provider to demonstrate the CRUD
       implementation. A real implementation would need to deal with online
       state and handle caching of the data, plus handle appropriate query
       capabilities as required by the application.


Run the App and Validate Results
--------------------------------

You must be online in order to run this application. Run the application
in the emulator. Note that the initial startup after logging in is
slightly longer (due to reading the data from the remote database).

Data is available immediately in the mobile backend. Create a few notes,
then view the records within the AWS Console:

1. Open the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.
2. Choose your project.
3. Choose **Resources** on the upper right.
4. Choose the link for your Amazon DynamoDB table.
5. Choose the **Items** tab.

When you  insert, edit or delete notes in the app, you should be able to see the data on the server reflect your actions almost immediately.

Next Steps
----------

-  Learn about `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__.


