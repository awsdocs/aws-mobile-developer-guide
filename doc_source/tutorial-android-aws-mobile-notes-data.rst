.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-android-aws-mobile-notes-data:

#######################################
Add Online Data Access to the Notes App
#######################################

In the :ref:`previous section <tutorial-android-aws-mobile-notes-auth>` of this tutorial , we added a simple sign-up / sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-android-aws-mobile-notes-setup>`. In this tutorial, we will add a NoSQL
database to our mobile backend, then configure a basic data access service to the note-taking app.

The Notes sample app uses a
`ContentProvider <https://developer.android.com/guide/topics/providers/content-providers.html>`__
(called :code:`NotesContentProvider`) to provide access to a local SQLite
database that is used to store the notes that you enter into the app. We
will replace the code within the :code:`ContentProvider` with code that uses
DynamoDB instead of SQLite.

You should be able to complete this section of the tutorial in 30-45 minutes.

Add a NoSQL database to the AWS Mobile Hub project
--------------------------------------------------

Before we work on the client-side code, we need to add a NoSQL database
and table to the backend project:

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
#. Choose :guilabel:`Create table` in the modal dialog. It will take a few moments for AWS to create the table.

    You have just created a NoSQL table in the `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__ service.

#. When the table is ready, choose your project name in the upper left and then choose :guilabel:`Integrate` on your Android app card.
#. Choose :guilabel:`Download Cloud Config` to get an  :file:`awsconfiguration.json` file updated with the new services.
#. Choose :guilabel:`Next` and then choose :guilabel:`Done`.

.. list-table::
   :widths: 1 6

   * - **Remember**

     - Whenever you update the AWS Mobile Hub project, a new AWS configuration file for your app is generated.

Connect to Your Backend
-----------------------

Replace the :file:`awsconfiguration.json` file in :file:`app/src/main/res/raw` directory with the updated version.

Your system may have modified the filename to avoid conflicts. Make sure the file you add to your Android Studio project is named :file:`awsconfiguration.json`.

Download the Models
-------------------

To aid in implementing a provider for the table you created, |AMH| generated a data model descriptor file. To add the data model to your project:

#. Choose your project name in the upper left and then choose :guilabel:`Integrate` on the Android app card.
#. Choose :guilabel:`Android Models` under :guilabel:`Download Models`.
#. Unpack the downloaded ZIP file and copy the files under :file:`src/main/java/com/amazonaws/models/nosql` to your Android Studio project in :file:`app/src/main/java/com/amazonaws/mobile/samples/mynotes/data`. One file (:file:`NotesDO.java`) should be copied.
#. Edit the :file:`data/NotesDO.java` file and change the package setting:

.. code-block:: java

    package com.amazonaws.mobile.samples.mynotes.data;

Add required libraries to the project
-------------------------------------

Edit the :file:`app/build.gradle` file and add the DynamoDB libraries to the
dependencies:

.. code-block:: java

   dependencies {

        // . . .

        implementation 'com.amazonaws:aws-android-sdk-core:2.6.+'
        implementation 'com.amazonaws:aws-android-sdk-auth-core:2.6.+@aar'
        implementation 'com.amazonaws:aws-android-sdk-auth-ui:2.6.+@aar'
        implementation 'com.amazonaws:aws-android-sdk-auth-userpools:2.6.+@aar'
        implementation 'com.amazonaws:aws-android-sdk-cognitoidentityprovider:2.6.+'
        implementation 'com.amazonaws:aws-android-sdk-pinpoint:2.6.+'

        // Amazon DynamoDB for NoSQL tables
        implementation 'com.amazonaws:aws-android-sdk-ddb:2.6.+'
        implementation 'com.amazonaws:aws-android-sdk-ddb-mapper:2.6.+'
    }

#. Choose :guilabel:`Sync Now` on the upper right to incorporate the dependencies you just declared.

Add Data access methods to the AWSProvider class
------------------------------------------------

To implement data synchronization, we need two explicit methods: a
method to upload changes and a method to download updates from the
server.

**To add data access methods**

#. Import :code:`DynamoDBMapper` and :code:`AmazonDynamoDBClient` in :file:`AWSProvider.java`.

   .. code-block:: java

       import com.amazonaws.auth.AWSCredentialsProvider;
       import com.amazonaws.mobile.auth.core.IdentityManager;
       import com.amazonaws.mobile.auth.userpools.CognitoUserPoolsSignInProvider;
       import com.amazonaws.mobile.config.AWSConfiguration;
       import com.amazonaws.mobile.samples.mynotes.data.NotesDO;
       import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
       import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;

       // Add DynamoDBMapper and AmazonDynamoDBClient to support data access methods
       import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;
       import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;

#. Add private :code:`DynamoDBMapper` and :code:`AmazonDynamoDBClient` variables to the :code:`AWSProvider` class:

   .. code-block:: java

      public class AWSProvider {
          private static AWSProvider instance = null;
          private Context context;
          private AWSConfiguration awsConfiguration;
          private PinpointManager pinpointManager = null;

          // Declare DynamoDBMapper and AmazonDynamoDBClient private variables
          // to support data access methods
          private AmazonDynamoDBClient dbClient = null;
          private DynamoDBMapper dbMapper = null;

          public static AWSProvider getInstance() {
                return instance;
          }
      }


#. Add the following method to the class:

   .. code-block:: java

        public DynamoDBMapper getDynamoDBMapper() {
            if (dbMapper == null) {
                final AWSCredentialsProvider cp = getIdentityManager().getCredentialsProvider();
                dbClient = new AmazonDynamoDBClient(cp);
                dbMapper = DynamoDBMapper.builder()
                        .awsConfiguration(getConfiguration())
                        .dynamoDBClient(dbClient)
                        .build();
            }
            return dbMapper;
        }

Implement Mutation Methods
--------------------------

The `ContentProvider <https://developer.android.com/guide/topics/providers/content-providers.html>`__
is the basic interface that Android uses to communicate with databases
on Android. It uses four methods that match the basic CRUD (create, read,
update, delete) methods.

Add the following methods to the ``NotesContentProvider`` class:

.. code-block:: java

        private NotesDO toNotesDO(ContentValues values) {
            final NotesDO note = new NotesDO();
            note.setContent(values.getAsString(NotesContentContract.Notes.CONTENT));
            note.setCreationDate(values.getAsDouble(NotesContentContract.Notes.CREATED));
            note.setNoteId(values.getAsString(NotesContentContract.Notes.NOTEID));
            note.setTitle(values.getAsString(NotesContentContract.Notes.TITLE));
            note.setUpdatedDate(values.getAsDouble(NotesContentContract.Notes.UPDATED));
            note.setUserId(AWSProvider.getInstance().getIdentityManager().getCachedUserID());
            return note;
        }

        private Object[] fromNotesDO(NotesDO note) {
            String[] fields = NotesContentContract.Notes.PROJECTION_ALL;
            Object[] r = new Object[fields.length];
            for (int i = 0 ; i < fields.length ; i++) {
                if (fields[i].equals(NotesContentContract.Notes.CONTENT)) {
                    r[i] = note.getContent();
                } else if (fields[i].equals(NotesContentContract.Notes.CREATED)) {
                    r[i] = note.getCreationDate();
                } else if (fields[i].equals(NotesContentContract.Notes.NOTEID)) {
                    r[i] = note.getNoteId();
                } else if (fields[i].equals(NotesContentContract.Notes.TITLE)) {
                    r[i] = note.getTitle();
                } else if (fields[i].equals(NotesContentContract.Notes.UPDATED)) {
                    r[i] = note.getUpdatedDate();
                } else {
                    r[i] = new Integer(0);
                }
            }
            return r;
        }

These functions convert object attributes when they are passed between :code:`ContentValues` of the app and the :code:`NotesDO` object, which required by the Amazon DynamoDB service.

Mutation events handle the :code:`insert`, :code:`update`, and :code:`delete` methods:

.. code-block:: java

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        int uriType = sUriMatcher.match(uri);
        switch (uriType) {
            case ALL_ITEMS:
                DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
                final NotesDO newNote = toNotesDO(values);
                dbMapper.save(newNote);
                Uri item = NotesContentContract.Notes.uriBuilder(newNote.getNoteId());
                notifyAllListeners(item);
                return item;
            default:
                throw new IllegalArgumentException("Unsupported URI: " + uri);
        }
    }

    @Override
    public int delete(@NonNull Uri uri, @Nullable String selection, @Nullable String[] selectionArgs) {
        int uriType = sUriMatcher.match(uri);
        int rows;

        switch (uriType) {
            case ONE_ITEM:
                DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
                final NotesDO note = new NotesDO();
                note.setNoteId(uri.getLastPathSegment());
                note.setUserId(AWSProvider.getInstance().getIdentityManager().getCachedUserID());
                dbMapper.delete(note);
                rows = 1;
                break;
            default:
                throw new IllegalArgumentException("Unsupported URI: " + uri);
        }
        if (rows > 0) {
            notifyAllListeners(uri);
        }
        return rows;
    }

    @Override
    public int update(@NonNull Uri uri, @Nullable ContentValues values, @Nullable String selection, @Nullable String[] selectionArgs) {
        int uriType = sUriMatcher.match(uri);
        int rows;

        switch (uriType) {
            case ONE_ITEM:
                DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
                final NotesDO updatedNote = toNotesDO(values);
                dbMapper.save(updatedNote);
                rows = 1;
                break;
            default:
                throw new IllegalArgumentException("Unsupported URI: " + uri);
        }
        if (rows > 0) {
            notifyAllListeners(uri);
        }
        return rows;
    }

Implement Query Methods
-----------------------

This application always asks for the entire data set that the user is
entitled to see, so there is no need to implement complex query
management. This simplifies the :code:`query()` method considerably. The
:code:`query()` method returns a :code:`Cursor` (which is a standard mechanism
for iterating over data sets returned from databases).

.. code-block:: java

    @Nullable
    @Override
    public Cursor query(
                  @NonNull Uri uri,
                  @Nullable String[] projection,
                  @Nullable String selection,
                  @Nullable String[] selectionArgs,
                  @Nullable String sortOrder) {
        int uriType = sUriMatcher.match(uri);

        DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
        MatrixCursor cursor = new MatrixCursor(NotesContentContract.Notes.PROJECTION_ALL);
        String userId = AWSProvider.getInstance().getIdentityManager().getCachedUserID();

        switch (uriType) {
            case ALL_ITEMS:
                // In this (simplified) version of a content provider, we only allow searching
                // for all records that the user owns.  The first step to this is establishing
                // a template record that has the partition key pre-populated.
                NotesDO template = new NotesDO();
                template.setUserId(userId);
                // Now create a query expression that is based on the template record.
                DynamoDBQueryExpression<NotesDO> queryExpression;
                queryExpression = new DynamoDBQueryExpression<NotesDO>()
                        .withHashKeyValues(template);
                // Finally, do the query with that query expression.
                List<NotesDO> result = dbMapper.query(NotesDO.class, queryExpression);
                Iterator<NotesDO> iterator = result.iterator();
                while (iterator.hasNext()) {
                    final NotesDO note = iterator.next();
                    Object[] columnValues = fromNotesDO(note);
                    cursor.addRow(columnValues);
                }

                break;
            case ONE_ITEM:
                // In this (simplified) version of a content provider, we only allow searching
                // for the specific record that was requested
                final NotesDO note = dbMapper.load(NotesDO.class, userId, uri.getLastPathSegment());
                if (note != null) {
                    Object[] columnValues = fromNotesDO(note);
                    cursor.addRow(columnValues);
                }
                break;
        }

        cursor.setNotificationUri(getContext().getContentResolver(), uri);
        return cursor;
    }


.. list-table::
   :widths: 1 6

   * - **Note**

     - Differences from a real implementation

       We've taken a simplified approach for this content provider to demonstrate the CRUD
       implementation. A real implementation would need to deal with online
       state and handle caching of the data, plus handle appropriate query
       capabilities as required by the application.

Convert the CRUD methods to Async
---------------------------------

The in-built SQLite driver has asynchronous wrappers so that you don't
need to think about what the content provider is actually doing.
However, network connections cannot happen on the UI thread. In the
absence of an asynchronous wrapper, you must provide your own. This
affects the create, update, and delete operations. There is no need to add code to
load the data from the server, as that operation is already asynchronous.

Inserts and updates are done in the :code:`NoteDetailFragment.java` class.
Deletes are done in the :code:`NoteListActivity.java` class.

In the :code:`OnCreate()` method of the :code:`NoteDetailFragment.java` class, replace the following :code:`if` statement that calls local cursor functions:

.. code-block:: java

        if (arguments != null && arguments.containsKey(ARG_ITEM_ID)) {
            String itemId = getArguments().getString(ARG_ITEM_ID);
            itemUri = NotesContentContract.Notes.uriBuilder(itemId);
            Cursor data = contentResolver.query(itemUri, NotesContentContract.Notes.PROJECTION_ALL, null, null, null);
            if (data != null) {
                data.moveToFirst();
                mItem = Note.fromCursor(data);
                isUpdate = true;
            }
        } else {
            mItem = new Note();
            isUpdate = false;
        }

With the following constants and statement that establishes an :code:`AsyncQueryHandler`, which provides a wrapper to make the calls run on a non-UI thread asynchronously:

.. code-block:: java

    // Constants used for async data operations
    private static final int QUERY_TOKEN = 1001;
    private static final int UPDATE_TOKEN = 1002;
    private static final int INSERT_TOKEN = 1003;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Get the ContentResolver
        contentResolver = getContext().getContentResolver();

        // Unbundle the arguments if any.  If there is an argument, load the data from
        // the content resolver aka the content provider.
        Bundle arguments = getArguments();
        mItem = new Note();
        if (arguments != null && arguments.containsKey(ARG_ITEM_ID)) {
            String itemId = getArguments().getString(ARG_ITEM_ID);
            itemUri = NotesContentContract.Notes.uriBuilder(itemId);


            // Replace local cursor methods with async query handling
            AsyncQueryHandler queryHandler = new AsyncQueryHandler(contentResolver) {
                @Override
                protected void onQueryComplete(int token, Object cookie, Cursor cursor) {
                    super.onQueryComplete(token, cookie, cursor);
                    cursor.moveToFirst();
                    mItem = Note.fromCursor(cursor);
                    isUpdate = true;

                    editTitle.setText(mItem.getTitle());
                    editContent.setText(mItem.getContent());
                }
            };
            queryHandler.startQuery(QUERY_TOKEN, null, itemUri, NotesContentContract.Notes.PROJECTION_ALL, null, null, null);


        } else {
            isUpdate = false;
        }

        // Start the timer for the delayed start
        timer.postDelayed(timerTask, 5000);
    }

In the :code:`saveData()` method, replace the following local cursor methods:

.. code-block:: java

    // Convert to ContentValues and store in the database.
    if (isUpdated) {
        ContentValues values = mItem.toContentValues();
        if (isUpdate) {
            contentResolver.update(itemUri, values, null, null);
        } else {
            itemUri = contentResolver.insert(NotesContentContract.Notes.CONTENT_URI, values);
            isUpdate = true;    // Anything from now on is an update
            itemUri = NotesContentContract.Notes.uriBuilder(mItem.getNoteId());
        }
    }

with an :code:`AsyncQueryHandler`:

.. code-block:: java

    private void saveData() {
        // Save the edited text back to the item.
        boolean isUpdated = false;
        if (!mItem.getTitle().equals(editTitle.getText().toString().trim())) {
            mItem.setTitle(editTitle.getText().toString().trim());
            mItem.setUpdated(DateTime.now(DateTimeZone.UTC));
            isUpdated = true;
        }
        if (!mItem.getContent().equals(editContent.getText().toString().trim())) {
            mItem.setContent(editContent.getText().toString().trim());
            mItem.setUpdated(DateTime.now(DateTimeZone.UTC));
            isUpdated = true;
        }

        // Replace local cursor methods with an async query handler
        // Convert to ContentValues and store in the database.
        if (isUpdated) {
            ContentValues values = mItem.toContentValues();

            AsyncQueryHandler queryHandler = new AsyncQueryHandler(contentResolver) {
                @Override
                protected void onInsertComplete(int token, Object cookie, Uri uri) {
                    super.onInsertComplete(token, cookie, uri);
                    Log.d("NoteDetailFragment", "insert completed");
                }

                @Override
                protected void onUpdateComplete(int token, Object cookie, int result) {
                    super.onUpdateComplete(token, cookie, result);
                    Log.d("NoteDetailFragment", "update completed");
                }
            };
            if (isUpdate) {
                queryHandler.startUpdate(UPDATE_TOKEN, null, itemUri, values, null, null);
            } else {
                queryHandler.startInsert(INSERT_TOKEN, null, NotesContentContract.Notes.CONTENT_URI, values);
                isUpdate = true;    // Anything from now on is an update

                // Send Custom Event to Amazon Pinpoint
                final AnalyticsClient mgr = AWSProvider.getInstance()
                        .getPinpointManager()
                        .getAnalyticsClient();
                final AnalyticsEvent evt = mgr.createEvent("AddNote")
                        .withAttribute("noteId", mItem.getNoteId());
                mgr.recordEvent(evt);
                mgr.submitEvents();
            }


        }
    }


Replace the :code:`remove()` method in :file:`NoteListActivity.java` with the following.

.. code-block:: java

    private static final int DELETE_TOKEN = 1004;

    void remove(final NoteViewHolder holder) {
        if (mTwoPane ){
            // Check to see if the current fragment is the record we are deleting
            Fragment currentFragment = NoteListActivity.this.getSupportFragmentManager().findFragmentById(R.id.note_detail_container);
            if (currentFragment instanceof NoteDetailFragment) {
                String deletedNote = holder.getNote().getNoteId();
                String displayedNote = ((NoteDetailFragment) currentFragment).getNote().getNoteId();
                if (deletedNote.equals(displayedNote)) {
                    getSupportFragmentManager().beginTransaction().remove(currentFragment).commit();
                }
            }
        }

        // Remove the item from the database
        final int position = holder.getAdapterPosition();
        AsyncQueryHandler queryHandler = new AsyncQueryHandler(getContentResolver()) {
            @Override
            protected void onDeleteComplete(int token, Object cookie, int result) {
                super.onDeleteComplete(token, cookie, result);
                notifyItemRemoved(position);
                Log.d("NoteListActivity", "delete completed");
            }
        };
    }

If you need to do a query (for example, to respond to a search request),
then you can use a similar technique to wrap the :code:`query()` method.

Run the application
-------------------

You must be online in order to run this application. Run the application
in the emulator. Note that the initial startup after logging in is
slightly longer (due to reading the data from the remote database).

Data is available immediately in the mobile backend. Create a few notes,
then view the records within the AWS Console:

1. Open the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.
2. Choose your project.
3. Choose **Resources** in the left hand menu.
4. Choose the link for your DynamoDB table.
5. Choose the **Items** tab.

When you  insert, edit or delete notes in the app, you should be able to see the data on the server reflect your actions almost immediately.

Next Steps
----------

-  Learn about data synchronization by reading about the Android `Sync
   Framework <https://developer.android.com/training/sync-adapters/index.html>`__.
-  Learn about `Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`__.


