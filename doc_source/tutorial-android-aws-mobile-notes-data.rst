.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-data:

#######################################
Add Serverless Backend to the Notes App
#######################################

In the :ref:`previous section <tutorial-android-aws-mobile-notes-auth>` of this tutorial , you added a simple sign-up and sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, :ref:`go back to the beginning <tutorial-android-aws-mobile-notes-setup>` and start from
there. In this tutorial, you add a NoSQL
database to the mobile backend, and then configure a basic data access service to the note-taking app.

You should be able to complete this section of the tutorial in 45-60 minutes.

Add a Data Access API to the Backend
------------------------------------

#. In Android Studio, switch to the Project view.
#. Right-click on the project, and then select :guilabel:`New > Directory`.
#. For directory name, enter :userinput:`server`, and then choose :guilabel:`OK`.
#. Right-click on the :file:`server` directory, and then select :guilabel:`New > File`.
#. For file name, enter :userinput:`schema.graphql`, and then choose :guilabel:`OK`.
#. Copy the following code into the :file:`schema.graphql` file:

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
   * Provide your schema file path: :userinput:`./server/schema.graphql`.

#. To deploy the new service, enter the following:

   .. code-block:: bash

      $ amplify push

#. To download the generated GraphQL schema, enter the following:

   .. code-block:: bash

      $ amplify codegen add

The AWS CloudFormation template that is generated creates an Amazon DynamoDB table that is protected by Amazon Cognito user pool authentication.  Access is provided by AWS AppSync.  AWS AppSync tags each record that is inserted into the database with the user ID of the authenticated user.  The authenticated user can read only the records that they own.

In addition to updating the :file:`awsconfiguration.json` file, the Amplify CLI generates the :file:`schema.json` file in the :file:`app/src/main/graphql` directory.  The :file:`schema.json` file is required by the AWS Mobile SDK for Android to run code generation for GraphQL operations.

Add Required Libraries to the Project
-------------------------------------

Edit the project-level :file:`build.gradle` file and add the AWS AppSync plugin path
to the dependencies as follows:

.. code-block:: java

    dependencies {
        classpath "com.android.tools.build:gradle:$gradle_version"
        classpath "com.amazonaws:aws-android-sdk-appsync-gradle-plugin:2.6.+"

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }

Edit the :file:`app/build.gradle` file. Add the AWS AppSync plugin below the other plugins:

.. code-block:: java

    apply plugin: 'com.android.application'
    apply plugin: 'com.amazonaws.appsync'

Add the AWS AppSync dependencies with the other SDKs.

.. code-block:: java

   dependencies {

        // . . .

        // AWS SDK for Android
        def aws_version = '2.6.27'
        implementation "com.amazonaws:aws-android-sdk-core:$aws_version"
        implementation "com.amazonaws:aws-android-sdk-auth-core:$aws_version@aar"
        implementation "com.amazonaws:aws-android-sdk-auth-ui:$aws_version@aar"
        implementation "com.amazonaws:aws-android-sdk-auth-userpools:$aws_version@aar"
        implementation "com.amazonaws:aws-android-sdk-cognitoidentityprovider:$aws_version"
        implementation "com.amazonaws:aws-android-sdk-pinpoint:$aws_version"

        // AWS AppSync SDK
        implementation "com.amazonaws:aws-android-sdk-appsync:2.6.+"
    }

On the upper-right side, choose :guilabel:`Sync Now` to incorporate the dependencies you just declared.

Add Permissions to the AndroidManifest.xml
------------------------------------------

#. In Android Studio, open the project.
#. On the left side of the project, choose :guilabel:`Project` to open the project browser.
#.  To find the app manifest, change the project browser view menu at the top to :guilabel:`Android`, and then open the :file:`app/manifests` folder.
#. Add the :code:`WAKE_LOCK`, :code:`READ_PHONE_STATE`, :code:`WRITE_EXTERNAL_STORAGE`, and
   :code:`READ_EXTERNAL_STORAGE`: permissions to your project's :file:`AndroidManifest.xml` file.

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.amazonaws.mobile.samples.mynotes">

        <uses-permission android:name="android.permission.INTERNET"/>
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
        <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
        <uses-permission android:name="android.permission.WAKE_LOCK" />
        <uses-permission android:name="android.permission.READ_PHONE_STATE" />
        <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
        <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>

        <application
            android:name=".NotesApp"
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            android:roundIcon="@mipmap/ic_launcher_round"
            android:supportsRtl="true"
            android:theme="@style/AppTheme">
        </application>
    </manifest>

Configure Sample Queries and Mutations for Code Generation
----------------------------------------------------------

To interact with AWS AppSync, your client needs to define GraphQL queries and mutations.  These are created as individual files within your application.

#. In Android Studio, switch to the :guilabel:`Project` view.
#. Expand the :file:`app/src/main/graphql` folder.
#. Right-click the :file:`graphql` folder and choose :guilabel:`New > Directory`.
#. For directory name, enter :userinput:`com/amazonaws/mobile/samples/mynotes`, and then choose :guilabel:`OK`.
#. Right-click the newly created :file:`mynotes` folder and choose :guilabel:`New > File`.
#. For file name, enter :file:`operations.graphql`, and then choose :guilabel:`OK`.
#. Copy the following contents into the file you just created:

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

.. list-table::
   :widths: 1 6

   * - What is in this file?

     - Your mobile app sends GraphQL commands (mutations and queries) to the AWS AppSync service.  These are template commands that are then converted (using a code generation plugin that we added to the :file:`build.gradle` file) to Java classes that you can use in your application.

Before continuing, perform a build to generate the appropriate classes through code generation.  You can do this by using the :guilabel:`Build > Make project` option.

Create an AWSDataService Class
------------------------------

Data access is proxied through a class that implements the :code:`DataService` interface.  At this point, the data access is provided by the :code:`MockDataService` class that stores a number of notes in memory.  In this section, you replace this class with an :code:`AWSDataService` class that provides access to the API that you recently deployed.

#. Right-click on the :file:`services/aws` folder, and then select :guilabel:`New > Java Class`.
#. For class name, enter :file:`AWSDataService`, and then choose :guilabel:`OK`.
#. Replace the contents of the file with the following:

   .. code-block:: java

        package com.amazonaws.mobile.samples.mynotes.services.aws;

        import android.content.Context;
        import android.util.Log;

        import com.amazonaws.mobile.config.AWSConfiguration;
        import com.amazonaws.mobile.samples.mynotes.CreateNoteMutation;
        import com.amazonaws.mobile.samples.mynotes.DeleteNoteMutation;
        import com.amazonaws.mobile.samples.mynotes.GetNoteQuery;
        import com.amazonaws.mobile.samples.mynotes.ListNotesQuery;
        import com.amazonaws.mobile.samples.mynotes.UpdateNoteMutation;
        import com.amazonaws.mobile.samples.mynotes.models.Note;
        import com.amazonaws.mobile.samples.mynotes.models.PagedListConnectionResponse;
        import com.amazonaws.mobile.samples.mynotes.models.ResultCallback;
        import com.amazonaws.mobile.samples.mynotes.services.DataService;
        import com.amazonaws.mobileconnectors.appsync.AWSAppSyncClient;
        import com.amazonaws.mobileconnectors.appsync.fetcher.AppSyncResponseFetchers;
        import com.amazonaws.mobileconnectors.appsync.sigv4.BasicCognitoUserPoolsAuthProvider;
        import com.amazonaws.mobileconnectors.cognitoidentityprovider.CognitoUserPool;
        import com.apollographql.apollo.GraphQLCall;
        import com.apollographql.apollo.api.Error;
        import com.apollographql.apollo.api.Response;
        import com.apollographql.apollo.exception.ApolloException;

        import java.util.ArrayList;
        import java.util.List;
        import java.util.Locale;

        import javax.annotation.Nonnull;

        import type.CreateNoteInput;
        import type.UpdateNoteInput;

        import static com.amazonaws.mobile.auth.core.internal.util.ThreadUtils.runOnUiThread;

        public class AWSDataService implements DataService {
            private static final String TAG = "AWSDataService";
            private AWSAppSyncClient client;

            public AWSDataService(Context context, AWSService awsService) {
                // Create an AppSync client from the AWSConfiguration
                AWSConfiguration config = awsService.getConfiguration();
                CognitoUserPool userPool = new CognitoUserPool(context, awsService.getConfiguration());
                client = AWSAppSyncClient.builder()
                        .context(context)
                        .awsConfiguration(config)
                        .cognitoUserPoolsAuthProvider(new BasicCognitoUserPoolsAuthProvider(userPool))
                        .build();
            }

            @Override
            public void loadNotes(int limit, String after, ResultCallback<PagedListConnectionResponse<Note>> callback) {
                // Load notes will go here
            }

            @Override
            public void getNote(String noteId, ResultCallback<Note> callback) {
                // Get note will go here
            }

            @Override
            public void deleteNote(String noteId, ResultCallback<Boolean> callback) {
                // Delete note will go here
            }

            @Override
            public void createNote(String title, String content, ResultCallback<Note> callback) {
                // Create note will go here
            }

            @Override
            public void updateNote(Note note, ResultCallback<Note> callback) {
                // Update note will go here
            }

            private void showErrors(List<Error> errors) {
                Log.e(TAG, "Response has errors:");
                for (Error e : errors) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error: %s", e.message()));
                }
                Log.e(TAG, "End of Response errors");
            }
        }

Register the AWSDataService with the Injection Service
------------------------------------------------------

Similar to the :file:`AWSService` class, the :file:`AWSDataService` class should be instantiated as a singleton object.  You use the :file:`Injection` service to do this.  Open the :file:`Injection` class, and replace the :code:`initialize()` method with the following code:

.. code-block:: java

   public static synchronized void initialize(Context context) {
     if (awsService == null) {
       awsService = new AWSService(context);
     }

     if (analyticsService == null) {
       analyticsService = new AWSAnalyticsService(context, awsService);
     }

     if (dataService == null) {
       dataService = new AWSDataService(context, awsService);
     }

     if (notesRepository == null) {
       notesRepository = new NotesRepository(dataService);
     }
   }

You should also add the :file:`AWSDataService` class to the list of imports for the class.  You can easily do this using Alt-Enter within the editor.

Add the Create, Update, and Delete Mutations
-------------------------------------------

We added some placeholder methods in the :file:`AWSDataService`.  These placeholders should contain the API calls to the backend.  Mutations follow a pattern:

#. Create an input object to represent the arguments that are required to perform the mutation.
#. Create a request object with the input object.
#. Enqueue the request with the AppSync client object.
#. When the request returns, handle the response on the UI thread.

Use the following code for the :code:`createNote()` and :code:`updateNote()` methods:

.. code-block:: java

    @Override
    public void createNote(String title, String content, ResultCallback<Note> callback) {
        CreateNoteInput input = CreateNoteInput.builder()
            .title(title.isEmpty() ? " " : title)
            .content(content.isEmpty() ? " " : content)
            .build();
        CreateNoteMutation mutation = CreateNoteMutation.builder().input(input).build();

        client.mutate(mutation)
            .enqueue(new GraphQLCall.Callback<CreateNoteMutation.Data>() {
                @Override
                public void onResponse(@Nonnull Response<CreateNoteMutation.Data> response) {
                    if (response.hasErrors()) {
                        showErrors(response.errors());
                        runOnUiThread(() -> callback.onResult(null));
                    } else {
                        CreateNoteMutation.CreateNote item = response.data().createNote();
                        final Note returnedNote = new Note(item.id());
                        returnedNote.setTitle(item.title().equals(" ") ? "" : item.title());
                        returnedNote.setContent(item.content().equals(" ") ? "" : item.content());
                        runOnUiThread(() -> callback.onResult(returnedNote));
                    }
                }

                @Override
                public void onFailure(@Nonnull ApolloException e) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error during GraphQL Operation: %s", e.getMessage()), e);
                }
            });
    }

    @Override
    public void updateNote(Note note, ResultCallback<Note> callback) {
        UpdateNoteInput input = UpdateNoteInput.builder()
            .id(note.getNoteId())
            .title(note.getTitle().isEmpty() ? " " : note.getTitle())
            .content(note.getContent().isEmpty() ? " " : note.getContent())
            .build();
        UpdateNoteMutation mutation = UpdateNoteMutation.builder().input(input).build();

        client.mutate(mutation)
            .enqueue(new GraphQLCall.Callback<UpdateNoteMutation.Data>() {
                @Override
                public void onResponse(@Nonnull Response<UpdateNoteMutation.Data> response) {
                    if (response.hasErrors()) {
                        showErrors(response.errors());
                        runOnUiThread(() -> callback.onResult(null));
                    } else {
                        UpdateNoteMutation.UpdateNote item = response.data().updateNote();
                        final Note returnedNote = new Note(item.id());
                        returnedNote.setTitle(item.title().equals(" ") ? "" : item.title());
                        returnedNote.setContent(item.content().equals(" ") ? "" : item.content());
                        runOnUiThread(() -> callback.onResult(returnedNote));
                    }
                }

                @Override
                public void onFailure(@Nonnull ApolloException e) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error during GraphQL Operation: %s", e.getMessage()), e);
                }
            });
    }

The classes for the input, mutation, and response data are all generated from the information within the :file:`schema.json` and :file:`operations.graphql` files.  The names of the classes are based on the query or mutation name within the file.

Note that Amazon DynamoDB does not allow blank string values.  The code here ensures that blanks are replaced with something that is not blank for the purposes of storage.

The code for the :code:`deleteNote()` method is similar to the :code:`createNote()` and :code:`deleteNote()` methods.  However, the :code:`DeleteNote` operation does not take an input object as an argument. We can feed the :code:`noteId` directly into the mutation operation object:

.. code-block:: java

    @Override
    public void deleteNote(String noteId, ResultCallback<Boolean> callback) {
        DeleteNoteMutation mutation = DeleteNoteMutation.builder().id(noteId).build();

        client.mutate(mutation)
            .enqueue(new GraphQLCall.Callback<DeleteNoteMutation.Data>() {
                @Override
                public void onResponse(@Nonnull Response<DeleteNoteMutation.Data> response) {
                    runOnUiThread(() -> callback.onResult(true));
                }

                @Override
                public void onFailure(@Nonnull ApolloException e) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error during GraphQL Operation: %s", e.getMessage()), e);
                    callback.onResult(false);
                }
            });
    }

Add the LoadNotes and GetNote Queries
-------------------------------------

Queries operate very similarly to the mutations.  However, you have to take care to convert all the records that are received to the proper form for the application, and you have to deal with caching.  The AWS Mobile SDK performs caching for you, but you have to select the appropriate cache policy.

*  :code:`CACHE_ONLY` consults the cache only and never requests data from the backend.  This is useful in an offline scenario.
*  :code:`NETWORK_ONLY` is the reverse of :code:`CACHE_ONLY`. It consults the backend only and never uses the cache.
*  :code:`CACHE_FIRST` fetches the data from the cache if available, and fetches from the backend if it is not available in the cache.
*  :code:`NETWORK_FIRST` fetches the data from the network.  If the network is unavailable, it uses the cache.
*  :code:`CACHE_AND_NETWORK` consults both the cache and network for data. If both are available, you get two callbacks.

In the sample application, you use a :code:`NETWORK_FIRST` cache policy.  This guarantees that the callback is only called once, but it still uses the cache when the application goes offline.

The :code:`getNote()` method looks very similar to the mutations covered earlier:

.. code-block:: java

    @Override
    public void getNote(String noteId, ResultCallback<Note> callback) {
        GetNoteQuery query = GetNoteQuery.builder().id(noteId).build();
        client.query(query)
            .responseFetcher(AppSyncResponseFetchers.NETWORK_FIRST)
            .enqueue(new GraphQLCall.Callback<GetNoteQuery.Data>() {
                @Override
                public void onResponse(@Nonnull Response<GetNoteQuery.Data> response) {
                    GetNoteQuery.GetNote item = response.data().getNote();
                    final Note note = new Note(noteId);
                    note.setTitle(item != null ? (item.title().equals(" ") ? "" : item.title()) : "");
                    note.setContent(item != null ? (item.content().equals(" ") ? "" : item.content()) : "");
                    runOnUiThread(() -> callback.onResult(note));
                }

                @Override
                public void onFailure(@Nonnull ApolloException e) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error during GraphQL Operation: %s", e.getMessage()), e);
                }
            });
    }

You need to convert the return value to the internal representation prior to returning the data to the main application.  The :code:`loadNotes()` method is a little more involved because the return value is a complex type that needs to be decoded before returning:

.. code-block:: java

    @Override
    public void loadNotes(int limit, String after, ResultCallback<PagedListConnectionResponse<Note>> callback) {
        ListNotesQuery query = ListNotesQuery.builder().limit(limit).nextToken(after).build();
        client.query(query)
            .responseFetcher(AppSyncResponseFetchers.NETWORK_FIRST)
            .enqueue(new GraphQLCall.Callback<ListNotesQuery.Data>() {
                @Override
                public void onResponse(@Nonnull Response<ListNotesQuery.Data> response) {
                    String nextToken = response.data().listNotes().nextToken();
                    List<ListNotesQuery.Item> rItems = response.data().listNotes().items();

                    List<Note> items = new ArrayList<>();
                    for (ListNotesQuery.Item item : rItems) {
                        Note n = new Note(item.id());
                        n.setTitle(item.title().equals(" ") ? "" : item.title());
                        n.setContent(item.content().equals(" ") ? "" : item.content());
                        items.add(n);
                    }
                    runOnUiThread(() -> callback.onResult(new PagedListConnectionResponse<>(items, nextToken)));
                }

                @Override
                public void onFailure(@Nonnull ApolloException e) {
                    Log.e(TAG, String.format(Locale.ENGLISH, "Error during GraphQL Operation: %s", e.getMessage()), e);
                }
            });
    }

Run the Application
-------------------

You must be online in order to run this application. Run the application in the emulator. Note that the initial startup after logging in is slightly longer. This is happens because it's reading the data from the remote database.

Data is available immediately in the mobile backend. Create a few notes, and then view the records in the AWS Console:

#. Open the `DynamoDB console <https://console.aws.amazon.com/dynamodb/home>`__.
#. In the left navigation, choose :guilabel:`Tables`.
#. Choose the table for your project. It will be based on the API name you set.
#. Choose the :guilabel:`Items` tab.

When you  insert, edit, or delete notes in the app, you should be able to see that the data on the server reflect your actions immediately.

Next Steps
----------

-  Learn about `AWS AppSync  <https://aws.amaozn.com/appsync/>`__.
-  Learn about `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__.


