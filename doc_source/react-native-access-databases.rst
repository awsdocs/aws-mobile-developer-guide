.. _react-native-access-databases:


####################
Access Your Database
####################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.


.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <react-native-getting-started>`.

Set Up Your Backend
===================

AWS Mobile :code:`database` feature enables you to create tables customized to your needs. The CLI then guides you to create a custom API to access your database.

Create a table
--------------

**To specify and create a table**

#. In your app root folder, run:

   .. code-block:: none

      awsmobile database enable --prompt

#. Design your table when prompted by the CLI.

   The CLI will prompt you for the table and other table configurations such as columns.

   .. code-block:: none

      Welcome to NoSQL database wizard
      You will be asked a series of questions to help determine how to best construct your NoSQL database table.

      ? Should the data of this table be open or restricted by user? Open
      ? Table name Notes


      You can now add columns to the table.

      ? What would you like to name this column NoteId
      ? Choose the data type string
      ? Would you like to add another column Yes
      ? What would you like to name this column NoteTitle
      ? Choose the data type string
      ? Would you like to add another column Yes
      ? What would you like to name this column NoteContent
      ? Choose the data type string
      ? Would you like to add another column No

   Choose a `Primary Key <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey>`_ that will uniquely identify each item. Optionally, choose a column to be a Sort Key when you will commonly use those values in combination with the Primary Key for sorting or searching your data. You can additional sort keys by adding a `Secondary Index <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes>`_ for each column you will want to sort by.

   .. code-block:: none

      Before you create the database, you must specify how items in your table are uniquely organized. This is done by specifying a Primary key. The primary key uniquely identifies each item in the table, so that no two items can have the same key.
      This could be and individual column or a combination that has "primary key" and a "sort key".
      To learn more about primary key:
      http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey


      ? Select primary key NoteId
      ? Select sort key (No Sort Key)

      You can optionally add global secondary indexes for this table. These are useful when running queries defined by a different column than the primary key.

      To learn more about indexes:

      http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes

      ? Add index No
      Table Notes added

Create a CRUD API
-----------------

AWS Mobile will create a custom API for your app to perform create, read, update, and delete (CRUD) actions on your database.

**To create a CRUD API for your table**

#. Run the following code:

   .. code-block:: bash

       cd YOUR-APP-ROOT-FOLDER

       awsmobile cloud-api enable --prompt

#. When prompted, choose :code:`Create CRUD API for existing Dynamo table`, select the table name from the previous steps, choose the access permissions for the table. Using the example table from the previous section:

   .. code-block:: bash

      This feature will create an API using Amazon API Gateway and AWS Lambda. You can optionally have the lambda function perform CRUD operations against your Amazon DynamoDB table.

#. Update your backend.

   To create the API you have configured, run:

   .. code-block:: java

        awsmobile push

   Until deployment of API to the cloud the has completed, the CLI displays the message: :code:`cloud-api update status: CREATE_IN_PROGRESS`. Once deployed a sucessful creation message :code:`cloud-api update status: CREATE_COMPLETE` is displayed.

   You can view the API that the CLI created by running :code:`awmobile console` and then choosing :guilabel:`Cloud Logic` in the |AMH| console.

Connect to Your Backend
=======================

.. contents::
   :local:
   :depth: 1


**To access to database tables from your app**

In :file:`App.js` import the following.

.. code-block:: java

    import { API } from 'aws-amplify-react-native';


Save an item (create or update)
-------------------------------

**To save an item**

In the part of your app that you want to access the database, such as an event handler in your React component, call the :code:`put` method.

.. code-block:: java
    :emphasize-lines: 2,5

      // Create a new Note according to the columns we defined earlier
      async saveNote() {
        let newNote = {
          "NoteTitle": "My first note!",
          "NoteContent": "This is so cool!",
          "NoteId": "abc123"
        }

        const path = "/Notes";

        // Use the API module to save the note to the database
        const response = await API.put("NotesCRUDAPI", path, newNote)
        console.log(response)
      }

To use the command line to see your saved items in the database run:

.. code-block:: none

   awsmobile cloud-api invoke NotesCRUDAPI GET /Notes


Get a specific item
-------------------

**To query for a specific item**

Call the :code:`get` method using the API path to the item you are querying for.

.. code-block:: java
    :emphasize-lines: 3,4

        //noteId is the primary key of the particular record you want to fetch
        async get(noteId) {
          const path = "/Notes/object/" + noteId;
          const response = await API.get("NotesCRUDAPI", path);
          console.log(response);
        }


Get all items
-------------

**To query for all items for a given user**

Call the :code:`get` method and pass an API path that contains the user's userId.

.. code-block:: javascript

    async getAll(userId) {
      const path = "/Notes/" + userId; // userId is your partition key
      const response = await API.get("NotesCRUDAPI", path);
      console.log(response);
    }


Delete an item
--------------

**To delete an item**

Add this method to your component. Remember to substitute the PATH and JSON from the CLI on the highlighted lines below

.. code-block:: java
    :emphasize-lines: 2,3

        //dbNoteId is the NoteId of the particular record you want to fetch
        async delete(noteId) {
          const path = "/Notes/object" + noteId;
          const response = await API.del("NotesCRUDAPI", path);
          console.log(response);
        }


Next Steps
==========

Learn more about the AWS Mobile :ref:`NoSQL Database <NoSQL-Database>` feature, which uses `Amazon DynamoDB <http://docs.aws.amazon.com/dynamodb/latest/developerguide/welcome.html>`_.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://github.com/aws/aws-amplify/tree/master/packages/aws-amplify-react-native>`_.

