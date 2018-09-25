
.. _tutorial-ios-aws-mobile-notes-data:

#######################################
Add Serverless Backend to the Notes App
#######################################

In the :ref:`previous section <tutorial-ios-aws-mobile-notes-auth>` of this tutorial, we added a simple sign-up / sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, go back and :ref:`start from the beginning <tutorial-ios-aws-mobile-notes-setup>`. In this tutorial, we add a GraphQL API backed by a NoSQL database to our mobile backend, and then configure a basic data access provider to the note-taking app.

You should be able to complete this section of the tutorial in 45-60 minutes.

Add Data Access API to the Backend
----------------------------------

#. In a terminal window, navigate to the root of iOS notes tutorial project folder, and  create a :file:`server` subdirectory.

#. In the :file:`server` directory, create a file called :userinput:`schema-model.graphql` using your favorite text editor.

#. In the :file:`schema-model.graphql` file, copy the following schema definition:

   .. code-block:: graphql

      type Note @model @auth(rules:[{allow: owner}]) {
         id: ID!
         title: String!
         content: String!
      }

#. In the terminal window, enter the following commands:

   .. code-block:: bash

      $ amplify add api

#. When prompted by the CLI, do the following:

   * Select a service type: :userinput:`GraphQL`.
   * Choose an authorization type: :userinput:`Amazon Cognito User Pool`.
   * Do you have an annotated GraphQL schema: :userinput:`Y`.
   * Provide your schema file path: :userinput:`./server/schema-model.graphql`.

#. To deploy the new service, enter the following:

   .. code-block:: bash

      $ amplify push

The AWS CloudFormation template that is generated creates an Amazon DynamoDB table that is protected by Amazon Cognito user pool authentication.  Access is provided by AWS AppSync.  AWS AppSync will tag each record that is inserted into the database with the user ID of the authenticated user.  The authenticated user will only be able to read the records that they own.

In addition to updating the :file:`awsconfiguration.json` file, the Amplify CLI will also generate the :file:`schema.graphql` file under the :file:`./amplify/backend/api/YOURAPI/build` directory. The :file:`schema.graphql` file will be used by the Amplify CLI to run code generation for GraphQL operations.

Generate an API Stub Class
--------------------------

To integrate the iOS notes app with AWS AppSync, we need to generate strongly typed Swift API code based on the GraphQL notes schema and operations. This Swift API code is a class that helps you create native Swift request and response data objects for persisting notes in the cloud.

To interact with AWS AppSync, the iOS client needs to define GraphQL queries and mutations which are converted to strongly typed Swift objects by the Amplify codegen step below.

#. In Xcode, create a new folder called :file:`GraphQLOperations`:

   *  In the Xcode Project Navigator, right-click on the :file:`MyNotes` folder that is a child of the top-level :file:`MyNotes` project. Choose :guilabel:`New Group...`
   *  Enter the name :userinput:`GraphQLOperations`.

#. Under the :file:`GraphQLOperations` folder called :file:`notes-operations.graphql`, create a new file as follows:

   *  In the Xcode Project Navigator, right-click the :file:`GraphQLOperations` folder you created, and choose :guilabel:`New File...`
   *  For :guilabel:`Filter`, enter :userinput:`Empty`.
   *  In the :guilabel:`Other` section, choose :guilabel:`Empty`, and then choose :guilabel:`Next`.
   *  For :guilabel:`Save As`, enter :userinput:`notes-operations.graphql`, and then choose :guilabel:`Create`.

#. In the file you just created, copy the following operations:

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

#. In a terminal window, navigate to your project directory, and run the following command. This tells Amplify CLI to generate the :file:`NotesAPI.swift` file based on the GraphQL schema and our mutations and query operations :file:`notes-operations.graphql` file.

   .. code-block:: none

      $ amplify add codegen

   - The file name pattern of graphql queries: :userinput:`./MyNotes/GraphQLOperations/notes-operations.graphql`
   - The file name for the generated code: :userinput:`NotesAPI.swift`

You should now have a :file:`NotesAPI.swift` file in the root of your project.

.. list-table::
   :widths: 1 6

   * - What is in the :file:`NotesAPI.swift` file?

     - Your mobile app sends GraphQL commands (mutations and queries) to the AWS AppSync service.  These are template commands that are converted to the Swift class :file:`NotesAPI.swift` file that you can use in your application.


Add API Dependencies
--------------------

#. Add the following API dependencies in your project's :file:`Podfile`:

   .. code-block:: none

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


#. In a terminal under your project folder, run the following:

   .. code-block:: none

      $  pod install -–repo-update

Add NotesAPI.swift to Your Xcode Project
----------------------------------------

#. Open your project in Xcode as follows:

   .. code-block:: none

      $ open MyNotes.xcworkspace

#. Drag the :file:`NotesAPI.swift` file from your project folder to the Xcode project. In  :guilabel:`Options`, clear the :guilabel:`Copy items if needed` check box.  By clearing :guilabel:`Copy items if needed` you ensure that the Amplify CLI can re-generate the :file:`NotesAPI.swift` file when we change the schema.

#. Choose :guilabel:`Finish`.

You have now created the AWS resources you need and connected them to your app.

Create an AWS AppSync Authentication Context
--------------------------------------------

#. In the Xcode project explorer, right-click the :file:`MyNotes` directory, and then choose :guilabel:`New File...`
#. Choose :guilabel:`Swift File`, and then choose :guilabel:`Next`.
#. Enter the name :userinput:`MyCognitoUserPoolsAuthProvider.swift`, and then choose :guilabel:`Create`.
#. In the file you just created, copy the following code:

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
             if token != nil {
               return token!
            } else {
               return ""
            }
         }
      }

Create an AWS AppSync DataService Class
---------------------------------------

All data access is already routed through a :file:`DataService` protocol, which has a concrete implementation in :file:`MockDataService.swift`.  We will now replace the mock data service with an implementation that reads and writes data to AWS AppSync.

#. In the Xcode project explorer, right-click the :file:`MyNotes` directory, and then choose :guilabel:`New File...`
#. Choose :guilabel:`Swift File`, and then choose :guilabel:`Next`.
#. Enter the name :userinput:`AWSDataService.swift`, and then choose :guilabel:`Create`.
#.  In the file you just created, copy the following code:

   .. code-block:: swift

      import AWSCore
      import AWSAppSync

      class AWSDataService : DataService {

          // AWS AppSync Client
          var appSyncClient: AWSAppSyncClient?
          let databaseURL = URL(fileURLWithPath:NSTemporaryDirectory()).appendingPathComponent("appsync.db")

          // Notes
          var notes = [Note]()

          init() {
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
          }

          // DynamoDB does not accept blanks, so we use a space instead - this converts back to blanks
          func convertNote(id: String?, title: String?, content: String?) -> Note {
              var note = Note()
              note.id = id
              note.title = (title == " ") ? "" : title
              note.content = (content == " ") ? "" : content
              return note
          }

          func getNote(_ noteId: String, onCompletion: @escaping (Note?, Error?) -> Void) {
              appSyncClient?.fetch(query: GetNoteQuery(id: noteId)) { (result, error) in
                  if let result = result {
                      onCompletion(self.convertNote(id: result.data?.getNote?.id, title: result.data?.getNote?.title, content:    result.data?.getNote?.content), nil)
                  } else {
                      onCompletion(nil, error)
                  }
              }
          }

          func loadNotes(onCompletion: @escaping ([Note]?, Error?) -> Void) {
              var myNotes: [Note]? = nil
              appSyncClient?.fetch(query: ListNotesQuery(), cachePolicy: .fetchIgnoringCacheData) { (result, error) in
                  if let result = result {
                      myNotes = [Note]()
                      for item in (result.data?.listNotes?.items)! {
                          let note = self.convertNote(id: item?.id, title: item?.title, content: item?.content)
                          myNotes?.append(note)
                      }
                      onCompletion(myNotes, nil)
                  } else {
                      onCompletion(nil, error)
                  }
              }
          }

          func updateNote(_ note: Note, onCompletion: @escaping (Note?, Error?) -> Void) {
              // DynamoDB doesn't accept empty values, so check first and add an extra space if empty
              let noteTitle = (note.title ?? "").isEmpty ? " " : note.title
              let noteContent = (note.content ?? "").isEmpty ? " " : note.content

              if (note.id == nil) { // Create
                  let createNoteInput = CreateNoteInput(title: noteTitle!, content: noteContent!)
                  let createMutation = CreateNoteMutation(input: createNoteInput)
                  appSyncClient?.perform(mutation: createMutation, resultHandler: { (result, error) in
                      if let result = result {
                          let item = result.data?.createNote
                          onCompletion(self.convertNote(id: item?.id, title: item?.title, content: item?.content), nil)
                      } else if let error = error {
                          onCompletion(nil, error)
                      }
                  })
              } else { // Update
                  let updateNoteInput = UpdateNoteInput(id: note.id!, title: noteTitle, content: noteContent)
                  let updateMutation = UpdateNoteMutation(input: updateNoteInput)
                  appSyncClient?.perform(mutation: updateMutation, resultHandler: { (result, error) in
                      if let result = result {
                          let item = result.data?.updateNote
                          onCompletion(self.convertNote(id: item?.id, title: item?.title, content: item?.content), nil)
                      } else if let error = error {
                          onCompletion(nil, error)
                      }
                  })
              }
          }

          func deleteNote(_ noteId: String, onCompletion: @escaping (Error?) -> Void) {
              let deleteMutation = DeleteNoteMutation(id: noteId)
              appSyncClient?.perform(mutation: deleteMutation, resultHandler: { (result, error) in
                  if result != nil {
                      onCompletion(nil)
                  } else if let error = error {
                      onCompletion(error)
                  }
              })
          }
      }

Register the AWS Data Service
-----------------------------

Register the new data service in the :file:`AppDelegate.swift` file as follows:

.. code-block:: swift

    // Initialize the analytics service
    // analyticsService = LocalAnalyticsService()
    analyticsService = AWSAnalyticsService()

    // Initialize the data service
    // dataService = MockDataService()
    dataService = AWSDataService()

Run the Application
-------------------

Run the application in an iOS simulator and perform some operations.  Create a couple of notes and delete a note.

**Note**: You must be online in order to run this application.

#. Open the `DynamoDB console <https://console.aws.amazon.com/dynamodb/home/>`__.
#. In the left navigation, choose :guilabel:`Tables`.
#. Choose the table for your project.  It will be based on the API name you set.
#. Choose the :guilabel:`Items` tab.

When you insert, edit, or delete notes in the app, you should be able to see the data on the server reflect your actions almost immediately.

Next Steps
----------

-  Learn about `AWS AppSync <https://aws.amazon.com/appsync/>`__.
-  Learn about `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__.


