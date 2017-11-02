.. _tutorial-ios-aws-mobile-notes-data:

#######################################
Add Online Data Access to the Notes App
#######################################

In the :ref:`previous section of this tutorial <authentication.mdtutorial-ios-aws-mobile-notes-auth>`aking app with email
validation. This tutorial assumes you have completed the previous
tutorials. If you jumped to this step, please go back and `start from
the beginning :ref:<tutorial-ios-aws-mobile-notes-setup>`_. In this tutorial, we will add a NoSQL
database to our mobile backend, then configure a basic data access
service to the note-taking app.

The Notes sample app uses a
`ContentProvider <https://developer.android.com/guide/topics/providers/content-providers.html>`_
(called :code:`NotesContentProvider`) to provide access to a local SQLite
database that is used to store the notes that you enter into the app. We
will replace the code within the :code:`ContentProvider` with code that uses
DynamoDB instead of SQLite.

You should be able to complete this section of the tutorial in 30-45 minutes.

Add a NoSQL database to the AWS Mobile Hub project
--------------------------------------------------

Before we work on the client-side code, we need to add a NoSQL database
and table to the backend project:

1. Open the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_.
2. Select  your project.
3. Choose the :guilabel:`NoSQL Database` tile.
4. Choose :guilabel:`Enable NoSQL`.
5. Choose :guilabel:`Add Table`.
6. Choose :guilabel:`Example` to start with an example schema.
7. Choose :guilabel:`Notes`, which most closely matches the model we wish to use.
8. Choose :guilabel:`Add attribute`, then fill in the details of the new attribute:

    -  :guilabel:`Attribute name`: :userinput:`updatedDate`
    -  :guilabel:`Type`: :userinput:`number`

9.  Choose:guilabel:`Add index` then fill in the details of the new index:

    -  :guilabel:`Index name: :userinput:`LastUpdated`
    -  :guilabel:`Partition key: :userinput:`userId`
    -  :guilabel:`Sort key: :userinput:`updatedDate`

10. Choose :guilabel:`Create table`
11. Choose :guilabel:`Create table` in the modal dialog.

Download the updated AWS configuration file.
--------------------------------------------

Whenever you update the AWS Mobile Hub project, a new AWS configuration
file for your app is generated. To download:

1. Choose :guilabel:`Integrate` in the left hand menu.
2. Choose :guilabel:`Download` in step 1.

If you previously downloaded this file, it may be named differently to
avoid filename conflicts. Add this file to your Android project by
replacing the :file:`awsconfiguration.json` file in the
:file:`app/src/main/res/raw` directory.

Download the Models
-------------------

To aid in implementing a provider for the DynamoDB table, AWS Mobile Hub
generates POCO models for each table. Download these and copy them to
your project:

1. Choose **Integrate** in the left hand menu.
2. Choose **Download** under the **NoSQL / Cloud Logic** heading, then
   select **Android**.
3. Unpack the downloaded ZIP file.
4. Copy the files under :file:`src/main/java/com/amazonaws/models/nosql` to
   your Android Studio project in
   :file:`app/src/main/java/com/amazonaws/mobile/samples/mynotes/data`. One
   file (file:`NotesDO.java`) should be copied.

Once copied, edit the :file:`data/NodesDO.java` file and change the package
setting:

.. code-block:: java

    package com.amazonaws.mobile.samples.mynotes.data;

Add required libraries to the project
-------------------------------------

Edit the :file`app/build.gradle` file and add the DynamoDB libraries to the
dependencies:

    .. code-block:: none
       :emphasize-lines: 8,9

       dependencies {
            # Other libraries are here
            compile 'com.amazonaws:aws-ios-sdk-core:2.6.+'
            compile 'com.amazonaws:aws-ios-sdk-auth-core:2.6.+@aar'
            compile 'com.amazonaws:aws-ios-sdk-auth-ui:2.6.+@aar'
            compile 'com.amazonaws:aws-ios-sdk-auth-userpools:2.6.+@aar'
            compile 'com.amazonaws:aws-ios-sdk-cognitoidentityprovider:2.6.+'
            compile 'com.amazonaws:aws-ios-sdk-ddb:2.6.+'
            compile 'com.amazonaws:aws-ios-sdk-ddb-mapper:2.6.+'
            compile 'com.amazonaws:aws-ios-sdk-pinpoint:2.6.+'
        }

Add Data access methods to the AWSProvider class
------------------------------------------------

To implement data synchronization, we need two explicit methods: a
method to upload changes and a method to download updates from the
server. Edit :file:`AWSProvider.java`. Add the following to the imports
section:

.. code-block:: none
   :emphasize-lines: 1,5,6,9

    import com.amazonaws.auth.AWSCredentialsProvider;
    import com.amazonaws.mobile.auth.core.IdentityManager;
    import com.amazonaws.mobile.auth.userpools.CognitoUserPoolsSignInProvider;
    import com.amazonaws.mobile.config.AWSConfiguration;
    import com.amazonaws.mobile.samples.mynotes.data.NotesDO;
    import com.amazonaws.mobileconnectors.dynamodbv2.dynamodbmapper.DynamoDBMapper;
    import com.amazonaws.mobileconnectors.pinpoint.PinpointConfiguration;
    import com.amazonaws.mobileconnectors.pinpoint.PinpointManager;
    import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient;

Add the following private variables:

.. code-block:: java
   :emphasize-lines: 1,5,6,9

    public class AWSProvider {
        private static AWSProvider instance = null;
        private Context context;
        private AWSConfiguration awsConfiguration;
        private PinpointManager pinpointManager = null;
        private AmazonDynamoDBClient dbClient = null;
        private DynamoDBMapper dbMapper = null;

        public static AWSProvider getInstance() {
            return instance;
        }


Add the following methods to the class:

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

The
`ContentProvider <https://developer.android.com/guide/topics/providers/content-providers.html>`_
is the basic interface that Android uses to communicate with databases
on Android. It uses four methods that match the basic CRUD (create, read,
update, delete) methods.

Add the following method to the ``NotesContentProvider`` class:

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

This converts the ``ContentValues`` object which is passed into the
ContentProvider with a ``NotesDO`` object, required by the DynamoDB
service.

Mutation events handle the create, update, and delete methods:

.. code-block:: java
   :emphasize-lines: 5-15,26-34,49-55

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        int uriType = sUriMatcher.match(uri);
        switch (uriType) {
            case ALL_ITEMS:
                DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
                final NotesDO newNote = toNotesDO(values);
                dbMapper.save(newNote);
                Uri item = new Uri.Builder()
                        .appendPath(NotesContentContract.CONTENT_URI.toString())
                        .appendPath(newNote.getNoteId())
                        .build();
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
management. This simplifies the `:code:`query()` method considerably. The
:code:`query()` method returns a :code:`Cursor` (which is a standard mechanism
for iterating over data sets returned from databases).

.. code-block:: java

    @Nullable
    @Override
    public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection, @Nullable String[] selectionArgs, @Nullable String sortOrder) {
        int uriType = sUriMatcher.match(uri);

        DynamoDBMapper dbMapper = AWSProvider.getInstance().getDynamoDBMapper();
        MatrixCursor cursor = new MatrixCursor(NotesContentContract.Notes.PROJECTION_ALL);

        switch (uriType) {
            case ALL_ITEMS:
                // In this (simplified) version of a content provider, we only allow searching
                // for all records that the user owns
                DynamoDBQueryExpression<NotesDO> queryExpression;
                queryExpression = new DynamoDBQueryExpression<>();
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
                final NotesDO note = dbMapper.load(NotesDO.class, uri.getLastPathSegment());
                if (note != null) {
                    Object[] columnValues = fromNotesDO(note);
                    cursor.addRow(columnValues);
                }
                break;
        }

        cursor.setNotificationUri(getContext().getContentResolver(), uri);
        return cursor;
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

.. note:: Differences from a real implementation

    We've taken a
    simplified approach for this content provider to demonstrate the CRUD
    implementation. A real implementation would need to deal with online
    state and handle caching of the data, plus handle appropriate query
    capabilities as required by the application.

Convert the CRUD methods to Async
---------------------------------

The in-built SQLite driver has asynchronous wrappers so that you don't
need to think about what the content provider is actually doing.
However, network connections cannot happen on the UI thread. In the
absence of an asynchronous wrapper, you must provide your own. This
affects the create, update, and delete operations. The loader framework
that is used to load the data from the server is already asynchronous
and so does not have this problem.

Inserts and updates are done in the :code:`NoteDetailFragment.java` class.
Deletes are done in the :code:`NoteListActivity.java` class. Start with the
:code:`NoteDetailFragment.java` class. Adjust the :code:`saveData()` method as
follows:

.. code-block:: java
   :emphasize-lines: 18-29,30,32,34

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
                queryHandler.startUpdate(1, null, itemUri, values, null, null);
            } else {
                queryHandler.startInsert(1, null, NotesContentContract.Notes.CONTENT_URI, values);
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


The :code:`AsyncQueryHandler` provides a wrapper to make the calls run on a
non-UI thread asynchronously. Adjust the :code:`remove()` method in
:file:`NoteListActivity.java` similarly as follows:

\`\`\`java hl\_lines="15 16 17 18 19 20 21 22 23 24 25" void
remove(final NoteViewHolder holder) { if (mTwoPane) { // Check to see if
the current fragment is the record we are deleting Fragment
currentFragment =
NoteListActivity.this.getSupportFragmentManager().findFragmentById(R.id.note\_detail\_container);
if (currentFragment instanceof NoteDetailFragment) { String deletedNote
= holder.getNote().getNoteId(); String displayedNote =
((NoteDetailFragment) currentFragment).getNote().getNoteId(); if
(deletedNote.equals(displayedNote)) {
getSupportFragmentManager().beginTransaction().remove(currentFragment).commit();
} } }

::

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
        Uri itemUri = ContentUris.withAppendedId(NotesContentContract.Notes.CONTENT_URI, holder.getNote().getId());
        queryHandler.startDelete(1, null, itemUri, null, null);
    }

\`\`\`

If you need to do a query (for example, to respond to a search request),
then you can use a similar technique to wrap the ``query()`` method.

Run the application
-------------------

You must be online in order to run this application. Run the application
in the emulator. Note that the initial startup after logging in is
slightly longer (due to reading the data from the remote database).

Data is available immediately in the mobile backend. Create a few notes,
then view the records within the AWS Console:

1. Open the [AWS Mobile Hub console][mobile-console].
2. Choose your project.
3. Choose **Resources** in the left hand menu.
4. Choose the link for your DynamoDB table.
5. Choose the **Items** tab.

You should be able to insert, edit and delete notes. The data on the
server will be reflected almost immediately.

Next Steps
----------

-  Learn about data synchronization by reading about the Android `Sync
   Framework <https://developer.android.com/guide/topics/providers/sync-adapters.html>`__.
-  Learn about [Amazon DynamoDB].

.. raw:: html

   <!-- Links -->

{!shared/services.md!}
