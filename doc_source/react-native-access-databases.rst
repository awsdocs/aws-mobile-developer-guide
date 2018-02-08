.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

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

#. In the root folder of your app, run:

   .. code-block:: bash

       awsmobile cloud-api enable --prompt

#. When prompted, choose :code:`Create CRUD API for existing Dynamo table`, select the table name from the previous steps, choose the access permissions for the table. Using the example table from the previous section:

   .. code-block:: bash

      ? Select from one of the choices below.
        Create a new API
      ❯ Create CRUD API for an existing Amazon DynamoDB table

   The prompt response will be:

   .. code-block:: bash

        Path to be used on API for get and remove an object should be like:
        /Notes/object/:NoteId

        Path to be used on API for list objects on get method should be like:
        /Notes/:NoteId

        JSON to be used as data on put request should be like:
        {
          "NoteTitle": "INSERT VALUE HERE",
          "NoteContent": "INSERT VALUE HERE",
          "NoteId": "INSERT VALUE HERE"
        }
        To test the api from the command line (after awsmobile push) use this commands
        awsmobile cloud-api invoke NotesCRUD <method> <path> [init]
        Api NotesCRUD saved

   Copy and keep the path of your API and the JSON for use in your app code.

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

#. In :file:`App.js` import the following.

    .. code-block:: java

          import Amplify, { API } from 'aws-amplify';
          import aws_exports from 'path_to_your_aws-exports';
          Amplify.configure(aws_exports);

#. Add the following :code:`state` to your component.

    .. code-block:: java

          state = {
            apiResponse: null,
            noteId: ''
               };

            handleChangeNoteId = (event) => {
                  this.setState({noteId: event});
          }



Save an item (create or update)
-------------------------------

**To save an item**

In the part of your app where you access the database, such as an event handler in your React component, call the :code:`put` method. Use the JSON and the root path (:code:`/Notes`) of your API that you copied from the CLI prompt response earlier.

.. code-block:: java
    :emphasize-lines: 2,5

      // Create a new Note according to the columns we defined earlier
        async saveNote() {
          let newNote = {
            body: {
              "NoteTitle": "My first note!",
              "NoteContent": "This is so cool!",
              "NoteId": this.state.noteId
            }
          }
          const path = "/Notes";

          // Use the API module to save the note to the database
          try {
            const apiResponse = await API.put("NotesCRUD", path, newNote)
            console.log("response from saving note: " + apiResponse);
            this.setState({apiResponse});
          } catch (e) {
            console.log(e);
          }
        }

To use the command line to see your saved items in the database run:

.. code-block:: none

   awsmobile cloud-api invoke NotesCRUD GET /Notes/object/${noteId}


Get a specific item
-------------------

**To query for a specific item**

Call the :code:`get` method using the API path (copied earlier) to the item you are querying for.

.. code-block:: java
    :emphasize-lines: 3,4

      // noteId is the primary key of the particular record you want to fetch
          async getNote() {
            const path = "/Notes/object/" + this.state.noteId;
            try {
              const apiResponse = await API.get("NotesCRUD", path);
              console.log("response from getting note: " + apiResponse);
              this.setState({apiResponse});
            } catch (e) {
              console.log(e);
            }
          }


Delete an item
--------------

**To delete an item**

Add this method to your component. Use your API path (copied earlier).

.. code-block:: javascript
    :emphasize-lines: 2,3

      // noteId is the NoteId of the particular record you want to delete
          async deleteNote() {
            const path = "/Notes/object/" + this.state.noteId;
            try {
              const apiResponse = await API.del("NotesCRUD", path);
              console.log("response from deleteing note: " + apiResponse);
              this.setState({apiResponse});
            } catch (e) {
              console.log(e);
            }
          }


UI to exercise CRUD calls
-------------------------

The following is and example of how you might construct UI to excercise these operations.

.. code-block:: javascript

    <View style={styles.container}>
            <Text>Response: {this.state.apiResponse && JSON.stringify(this.state.apiResponse)}</Text>
            <Button title="Save Note" onPress={this.saveNote.bind(this)} />
            <Button title="Get Note" onPress={this.getNote.bind(this)} />
            <Button title="Delete Note" onPress={this.deleteNote.bind(this)} />
            <TextInput style={styles.textInput} autoCapitalize='none' onChangeText={this.handleChangeNoteId}/>
    </View>

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
      },
      textInput: {
          margin: 15,
          height: 30,
          width: 200,
          borderWidth: 1,
          color: 'green',
          fontSize: 20,
          backgroundColor: 'black'
       }
    });

Next Steps
==========

Learn more about the AWS Mobile :ref:`NoSQL Database <NoSQL-Database>` feature, which uses `Amazon DynamoDB <http://docs.aws.amazon.com/dynamodb/latest/developerguide/welcome.html>`_.

Learn about :ref:`AWS Mobile CLI <aws-mobile-cli-reference>`.

Learn about `AWS Mobile Amplify <https://github.com/aws/aws-amplify/tree/master/packages/aws-amplify-react-native>`_.

