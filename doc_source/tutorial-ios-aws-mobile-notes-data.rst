.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-ios-aws-mobile-notes-data:

#######################################
Add Serverless Backend to the Notes App
#######################################

In the :ref:`previous section <tutorial-ios-aws-mobile-notes-auth>` of this tutorial, we added a simple sign-up / sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-ios-aws-mobile-notes-setup>`. In this tutorial, we will add a NoSQL
database to our mobile backend, then configure a basic data access provider to the note-taking app.

The notes app uses iOS `Core Data <https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CoreData/index.html>`__ as a persistence framework. :code:`NotesContentProvider.swift` is custom content provider used as a clean interface for managing your application content locally. In the following steps, you will modify the content provider code to use DynamoDB and sync with the local Core data.

You should be able to complete this section of the tutorial in about 45 minutes.

Add data access API to the backend
----------------------------------

#. In a terminal window, create a :file:`server` directory under the root of iOS notes tutorial project folder.

   .. code-block:: bash

      $ cd ~/aws-mobile-ios-notes-tutorial-master/
      $ mkdir server
      $ cd ~/aws-mobile-ios-notes-tutorial-master/server/

#. Inside the :file:`server` directory, create a new file called :userinput:`schema-model.graphql` using your favorite text editor.
   e.g. ~/aws-mobile-ios-notes-tutorial-master/server/schema-model.graphql

#. Copy the following code into the :file:`schema-model.graphql` file:

   .. code-block:: none

      type Note @model @auth(rules:[{allow: owner}]) {
         id: ID!
         title: String!
         content: String!
      }

#. In the terminal window, enter the following commands:

   .. code-block:: bash

      $ amplify api add

#. When prompted by the CLI, do the following:

   * Select a service type: :userinput:`GraphQL`.
   * Choose an authorization type: :userinput:`Amazon Cognito User Pool`.
   * Do you have an annotated GraphQL schema: :userinput:`Y`.
   * Provide your schema file path: :userinput:`./server/schema-model.graphql`.

#. To deploy the new service, enter the following:

   .. code-block:: bash

      $ amplify push

The AWS CloudFormation template that is generated creates an Amazon DynamoDB table that is protected by Amazon Cognito user pool authentication.  Access is provided by AWS AppSync.  AWS AppSync will tag each record that is inserted into the database with the user ID of the authenticated user.  The authenticated user will only be able to read the records that they own.

In addition to updating the :file:`awsconfiguration.json` file, the Amplify CLI will also generate the :file:`schema.graphql` file under the :file:`./aws-mobile-ios-notes-tutorial-master/amplify/backend/api/YOURAPI/build` directory. The :file:`schema.graphql` file will be used by the Amplify CLI to run code generation for GraphQL operations.

Code Generation for the API
---------------------------

To integrate our iOS notes app with AWS AppSync, we need to generate strongly typed Swift API code based on the GraphQL notes schema and operations. This Swift API code is a class that helps you create native Swift request and response data objects for persisting notes in the cloud.

To interact with AWS AppSync, our iOS client needs to define GraphQL queries and mutations which are converted to strongly typed Swift objects by the Amplify codegen step below.

#. In your project folder, create a new folder called :file:`GraphQLOperations`:

   *  Right-click on :file:`MyNotes` in the Xcode project navigation, and choose :guilabel:`New Group...`
   *  Enter the name :userinput:`GraphQLOperations`.

#. Create a new file under the :file:`GraphQLOperations` folder called :file:`notes-operations.graphql`:

   *  Right-click on :file:`GraphQLOperations` in the Xcode project navigation, and choose :guilabel:`New File...`
   *  Enter :userinput:`Empty` in the :guilabel:`Filter` box.
   *  Choose :guilabel:`Empty` under :guilabel:`Other`, then choose :guilabel:`Next`.
   *  Enter :userinput:`notes-operations.graphql` in the :guilabel:`Save As` field, then choose :guilabel:`Create`.

#. Paste the following operations into the newly created file.

   .. code-block:: graphql

      query GetNote($id:ID!) {
        getNote(id:$id) {
            id
            title
            content
        }
      }

      query ListNotes($limit:Int,$nextToken:String) {
        listNotes(limit:$limit,nextToken:$nextToken) {
            items {
                id
                title
                content
            }
            nextToken
        }
      }

      mutation CreateNote($input:CreateNoteInput!) {
        createNote(input:$input) {
            id
            title
            content
        }
      }

      mutation UpdateNote($input:UpdateNoteInput!) {
        updateNote(input:$input) {
            id
            title
            content
        }
      }

      mutation DeleteNote($id:ID!) {
        deleteNote(input: { id: $id }) {
            id
        }
      }

#. In your project folder, type the following command in terminal, telling Amplify CLI to generate the :file:`NotesAPI.swift` file based on the GraphQL schema and our mutations and query operations :file:`notes-operations.graphql` file.

   .. code-block:: bash

      $ amplify codegen add

   Provide the path to :file:`notes-operations.graphql` when asked for the queries, mutations, and subscriptions. Enter :file:`NotesAPI.swift` when prompted for generated code file name.
   When asked if ou want to generate code, choose Yes.

You should now have a :file:`NotesAPI.swift` file in the root of your project.

.. list-table::
   :widths: 1 6

   * - What is in the :file:`NotesAPI.swift` file?

     - Your mobile app sends GraphQL commands (mutations and queries) to the AWS AppSync service.  These are template commands that are converted to the Swift class :file:`NotesAPI.swift` file that you can use in your application.


Add API Dependencies
--------------------

#. Add the following API dependencies in your project's :file:`Podfile`

   .. code-block:: bash

      platform :ios, '9.0'
      target :'MyNotes' do
          use_frameworks!

            # Analytics dependency
            pod 'AWSPinpoint'

            # Auth dependencies
            pod 'AWSUserPoolsSignIn'
            pod 'AWSAuthUI'
            pod 'AWSMobileClient'

            # API dependency
            pod 'AWSAppSync'

          # other pods
      end

#. In a terminal under your project folder, run:

   .. code-block:: bash

      $ pod install

Add NotesAPI.swift to your Xcode project
----------------------------------------

#. Open your project in Xcode

   .. code-block:: bash

      $ open MyNotes.xcworkspace

#. Drag the :file:`NotesAPI.swift` file from your project folder into the Xcode project. Uncheck :guilabel:`Copy items if needed` and :guilabel:`Create groups` in the options dialog.
   Note: We are unchecking :guilabel:`Copy items if needed` as we only want a reference to :file:`NotesAPI.swift` file in your Xcode project so the Amplify CLI can keep it in sync if backend API changes are made.

#. Choose :guilabel:`Finish`.

You have now created the AWS resources you need and connected them to your app.

AWS AppSync Client Configuration
--------------------------------

#. Create a new Swift class called :file:`MyCognitoUserPoolsAuthProvider.swift` and paste in the following code:

   .. code-block:: swift

      import AWSUserPoolsSignIn
      import AWSAppSync

      class MyCognitoUserPoolsAuthProvider: AWSCognitoUserPoolsAuthProvider {

         func getLatestAuthToken() -> String {
             var token: String? = nil
             AWSCognitoUserPoolsSignInProvider.sharedInstance().getUserPool().currentUser()?.getSession().continueOnSuccessWith(block: { (task) -> Any? in
                token = task.result!.idToken!.tokenString
                return nil
             }).waitUntilFinished()
             return token!
         }
      }

#. Add the following imports to the top of the :file:`AppDelegate.swift` class file:

   .. code-block:: swift

      import UIKit
      import CoreData

      // Anaytics imports
      import AWSCore
      import AWSPinpoint

      // Auth imports
      import AWSMobileClient

      // AppSync
      import AWSAppSync

#. Add the :code:`AWSAppSyncClient` definition at the top of your :file:`AppDelegate.swift` class:

   .. code-block:: swift

      var window: UIWindow?
      var pinpoint: AWSPinpoint?

      // AWS AppSync Client
      var appSyncClient: AWSAppSyncClient?

#. Initialize the :code:`appSyncClient` in the :code:`didFinishLaunchingWithOptions` function of your :file:`AppDelegate.swift` class:

   .. code-block:: swift

      // Place immediately after the pinpoint definition and before the return statement of the :code:`didFinishLaunchingWithOptions` function.
      let database_name = "appsync.db"
      let databaseURL = URL(fileURLWithPath:NSTemporaryDirectory()).appendingPathComponent(database_name)

      do {
         // Initialize the AWS AppSync configuration
         let appSyncConfig = try AWSAppSyncClientConfiguration(appSyncClientInfo: AWSAppSyncClientInfo(),
                                                               userPoolsAuthProvider: MyCognitoUserPoolsAuthProvider(),
                                                               databaseURL:databaseURL)

         // Initialize the AWS AppSync client
         appSyncClient = try AWSAppSyncClient(appSyncConfig: appSyncConfig)
      } catch {
         print("Error initializing appsync client. \(error)")
      }

      return didFinishLaunching

#. Adjust the :code:`splitViewController()` method in :code:`AppDelegate.swift` as follows:

   .. code-block:: swift


#. Add the following imports to the top of the :file:`Data/NotesContentProvider.swift` file:

   .. code-block:: swift

      // . . .

      // AWS AppSync
      import AWSAppSync
      import AWSAuthCore

#. Add the :code:`AWSAppSyncClient` definition and init() code near the top of the :file:`Data/NotesContentProvider.swift` class:

   .. code-block:: swift

      var appSyncClient: AWSAppSyncClient?

      public init() {
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        appSyncClient = appDelegate.appSyncClient
      }

Add the Create, Update, and Delete Mutations
--------------------------------------------

:code:`Data/NotesContentProvider` is the basic interface the app uses to communicate with your API data. Mutation events handle the CRUD operations when you call its :code:`createNote`, :code:`updateNote`, and :code:`deleteNote` functions.

#. Add insert, update, and delete functions to the NotesContentProvider class as follows:

   .. code-block:: swift

      // Insert note
      func insertNote(completionHandler: @escaping ((String?, Error?) -> Void)) {
            var noteId = ""
            let noteTitle = " "
            let noteContent = " "
            let createNoteInput = CreateNoteInput(title: noteTitle, content: noteContent)
            let mutation = CreateNoteMutation(input: createNoteInput)
            appSyncClient?.perform(mutation: mutation, resultHandler: { (result, error) in
                if let result = result {
                    guard result.data?.createNote?.id != nil else {
                        return
                    }
                    noteId = (result.data?.createNote?.id)!
                    self.sendNoteEvent(noteId: noteId, eventType: noteEventType.AddNote.rawValue)
                    completionHandler(noteId, nil)
                } else if let error = error {
                    print(error.localizedDescription)
                }
            })
      }

      // Update note
      func updateNote(noteId: String, noteTitle: String, noteContent: String)  {

            let updateNoteInput = UpdateNoteInput(id: noteId, title: noteTitle, content: noteContent)
            let mutation = UpdateNoteMutation(input: updateNoteInput)

            appSyncClient?.perform(mutation: mutation, resultHandler: { (result, error) in
                if let result = result {
                } else if let error = error {
                    print(error.localizedDescription)
                }
            })
       }

      // Delete note
      public func deleteNote(noteId: String!, completionHandler: @escaping (Error?) -> Void)  {

            let mutation = DeleteNoteMutation(id: noteId)

            appSyncClient?.perform(mutation: mutation, resultHandler: { (result, error) in
                if let result = result {
                    self.sendNoteEvent(noteId: noteId, eventType: noteEventType.DeleteNote.rawValue)
                    completionHandler(nil)
                } else if let error = error {
                    print(error.localizedDescription)
                    completionHandler(error)
                }
            })
      }


Add the GraphQL query functions
-------------------------------

Add the following query functions just below the init() function in the :file:`Data/NotesContentProvider.swift` class:

.. code-block:: swift

   func getNote(id: String) -> GetNoteQuery.Data.GetNote {
        var myNote: GetNoteQuery.Data.GetNote? = nil
        appSyncClient?.fetch(query: GetNoteQuery(id: id)) { (result, error) in
            if error != nil {
                print(error?.localizedDescription)
                return
            }
            myNote = (result?.data?.getNote)!
            print("myNote: \(myNote)")
        }
        return myNote!
   }

   func loadNotes(completionHandler: @escaping ([ListNotesQuery.Data.ListNote.Item?]?, Error? ) -> Void) {
        var myNotes: [ListNotesQuery.Data.ListNote.Item?] = []
        appSyncClient?.fetch(query: ListNotesQuery(), cachePolicy: .returnCacheDataDontFetch) { (result, error) in
            if error != nil {
                print(error?.localizedDescription)
                return
            }
            myNotes = (result?.data?.listNotes?.items)!
            completionHandler(myNotes, nil)
            print("myNotes: \(myNotes)")
        }
   }

    func loadNotesFromNetwork(completionHandler: @escaping ([ListNotesQuery.Data.ListNote.Item?]?, Error? ) -> Void) {
        var myNotes: [ListNotesQuery.Data.ListNote.Item?] = []
        appSyncClient?.fetch(query: ListNotesQuery(), cachePolicy: .fetchIgnoringCacheData) { (result, error) in
            if error != nil {
                print(error?.localizedDescription)
                return
            }
            myNotes = (result?.data?.listNotes?.items)!
            completionHandler(myNotes, nil)
            print("myNotes: \(myNotes)")
        }
    }

Update the local operations for remote GraphQL calls
----------------------------------------------------

Calls to insert, update, delete, and query are made in :code:`MasterViewController` and :code:`DetailsViewController` classes.

#. Replace :code:`autoSave()` function code in the :code:`DetailViewController` class with the following:

   .. code-block:: swift

      func autoSave() {
        // If this is a NEW note, set the Note Id
        if (self.noteId == nil) // Insert
        {
            noteContentProvider?.insertNote() { (noteId, error) in
                if error == nil {
                    self.noteId = noteId!
                }
            }
        }
        else // Update
        {
            let noteId = self.noteId
            let noteTitle = self.noteTitle.text
            let noteContent = self.noteContent.text
            noteContentProvider?.updateNote(noteId: noteId!, noteTitle: noteTitle!, noteContent: noteContent!)
        }
    }

#. Replace the :code:`configureView()` function code in the :code:`DetailViewController` class with the following:

    .. code-block:: swift

       // Display the note title and content
       func configureView() {
            DispatchQueue.main.async {
                self.noteTitle?.text = self.appsyncNote?.title
                self.noteContent.text = self.appsyncNote?.content
            }
       }

#. Remove the static reference to :code:`noteId` and add a new definition for :code:`appsyncNote` at the top of the :code:`DetailViewController` class

   .. code-block:: swift

   var noteId: String?

   // AppSync version of the note
   var appsyncNote: ListNotesQuery.Data.ListNote.Item? {
       didSet {
           self.noteId = appsyncNote?.id
           configureView()
       }
   }

#. Remove the definition for :code:`myNote` in the :code:`DetailViewController` class:

   .. code-block:: swift

      //    var myNote: Note? {
      //        didSet {
      //            // Set the note Id if passed in from the MasterView
      //            DetailViewController.noteId = myNote?.value(forKey: "noteId") as? String
      //            // Update the view with passed in note title and content.
      //            configureView()
      //        }
      //    }

#. Replace the :code:`viewWillDisappear` and :code:`viewDidDisappear` functions in the :code:`DetailViewController` class as follows:

    .. code-block:: swift

       override func viewWillDisappear(_ animated: Bool) {
            // Stop the auto-save timer
            if autoSaveTimer != nil {
                autoSaveTimer.invalidate()
            }

            // Update the note one last time unless a note was never created
            let noteId = self.noteId
            if  noteId != nil {
                noteContentProvider?.updateNote(noteId: (noteId)!, noteTitle: self.noteTitle.text!, noteContent: self.noteContent.text!) //Core Data
            }
       }

       override func viewDidDisappear(_ animated: Bool) {
            self.noteId = nil
       }

#. Replace the prepare segue in the :code:`MasterViewController` class with the follwoing:

   .. code-block:: swift

      override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "showDetail" {
            if let sender = sender as? ListNotesQuery.Data.ListNote.Item {
                let controller = (segue.destination as! UINavigationController).topViewController as! DetailViewController
                let appsyncNote = sender
                controller.appsyncNote = appsyncNote
                controller.navigationItem.leftBarButtonItem = splitViewController?.displayModeButtonItem
                controller.navigationItem.leftItemsSupplementBackButton = true
            }
        }
      }

#. At the top of the :code:`MasterViewController.swift` class, add the following code:

   .. code-block:: swift

      var notes: [NSManagedObject] = []
      var notesList: [ListNotesQuery.Data.ListNote.Item?]? = [] {
        didSet {
            tableView.reloadData()
        }
      }

#. Add this new function to :code:`MasterViewController.swift` class just before the configureCell function

   .. code-block:: swift

      func loadNotesFromNetwork() {
         _noteContentProvider?.loadNotesFromNetwork() { (notes, error) in
             DispatchQueue.main.async {
                 self.notesList = notes
            }
         }
      }

#. Update the :code:`viewDidLoad()` function in the :code:`MasterViewController.swift` class by adding the following code to the bottom of the :code:`viewDidLoad()` function:

   .. code-block:: swift

      _noteContentProvider?.loadNotes() { (notes, error) in
            DispatchQueue.main.async {
                self.notesList = notes
            }
      }
      self.tableView.dataSource = self
      self.tableView.delegate = self

#. Replace the :code:`tableView()` used for handling note deletion in the :code:`MasterViewController.swift` class wtih the following:

   .. code-block:: swift

      override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
            if editingStyle == .delete {
                let noteId = notesList![indexPath.row]?.id
                _noteContentProvider?.deleteNote(noteId: noteId!) { (error) in
                    if error == nil {
                        self.loadNotesFromNetwork()
                    }
                }

            }
      }

#. Replace the :code:`configureCell()` function in the :code:`MasterViewController.swift` class with the following:

   .. code-block:: swift

      func configureCell(_ cell: UITableViewCell, withEvent note: ListNotesQuery.Data.ListNote.Item) {
        cell.textLabel!.text = "Title: " + note.title
        cell.detailTextLabel?.text = note.content
      }

#. Replace the following functions in the :code:`MasterViewController.swift` class:

   .. code-block:: swift

      override func numberOfSections(in tableView: UITableView) -> Int {
            return 1
      }

      override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return notesList?.count ?? 0
      }

      override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
          let cellIdentifier = "ElementCell"
          let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier)
                    ?? UITableViewCell(style: .subtitle, reuseIdentifier: cellIdentifier)
          let note = notesList![indexPath.row]!
          configureCell(cell, withEvent: note)
          return cell
      }

#. Replace the controller for the table in the :code:`MasterViewController.swift` class:

   .. code-block:: swift

      // Called when user swipes and selects "Delete"
      func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {
          switch type {
              case .insert:
                  tableView.insertRows(at: [newIndexPath!], with: .fade)
              case .delete:
                  tableView.deleteRows(at: [indexPath!], with: .fade)
              case .update:
                  configureCell(tableView.cellForRow(at: indexPath!)!, withEvent: anObject as! ListNotesQuery.Data.ListNote.Item)
              case .move:
                  configureCell(tableView.cellForRow(at: indexPath!)!, withEvent: anObject as! ListNotesQuery.Data.ListNote.Item)
                  tableView.moveRow(at: indexPath!, to: newIndexPath!)
          }
      }

Run the application
-------------------

Run the application in an iOS simulator. Note: You must be online in order to run this application.

#. Open the `DynamoDB console <https://console.aws.amazon.com/dynamodb/home/>`__.
#. Choose :guilabel:`Tables` in the left-hand menu.
#. Choose the table for your project.  It will be based on the API name you set.
#. Choose the :guilabel:`Items` tab.

When you insert, edit or delete notes in the app, you should be able to see the data on the server reflect your actions almost immediately.

Next Steps
----------

-  Learn about `AWS AppSync <https://aws.amazon.com/appsync/>`__.
-  Learn about `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__.


