.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-react-native-aws-mobile-notes-data:

#######################################
Add Online Data Access to the Notes App
#######################################

In the :ref:`previous section <tutorial-android-aws-mobile-notes-auth>` of this tutorial, we added a simple sign-up / sign-in flow to the sample note-taking app with email validation. This tutorial assumes you have completed the previous tutorials. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-android-aws-mobile-notes-setup>`. In this tutorial, we will add a NoSQL
database to our mobile backend, then configure a basic data access service to the note-taking app.

.. list-table::
   :widths: 1 6

   * - **Used in this Section**

     - `AWS AppSync <https://aws.amazon.com/appsync/>`__ allows you to expose data within `Amazon DynamoDB <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html>` _, `Amazon ElasticSearch Service <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/what-is-amazon-elasticsearch-service.html>`__, or other data sources so that it can be accessed using `GraphQL <https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html>`__.


Setup Your Data Backend
-----------------------

#. Open the `AWS AppSync console <https://console.aws.amazon.com/appsync/home>`__.
#. Choose :guilabel:`Create API` and type :userinput:`NotesApp` or other suitabe name.
#. Choose Custom Schema.
#. Choose :guilabel:`Create`.
#. Choose :guilabel:`Schema` on the left.
#. Copy and paste the following GraphQL schema into the text window provided.

   .. code-block:: json

      type Note {
          noteId: ID!
          title: String!
          content: String!
      }

      type Query {
          getNote(noteId: ID!): Note
          allNote(count: Int, nextToken: String): [Note]
      }

      type Mutation {
          putNote(noteId: ID!, title: String!, content: String!): Note
          deleteNote(noteId: ID!): Note
      }

      schema {
        query:Query
        mutation:Mutation
      }

#. Choose :guilabel:`Save`.
#. Choose :guilabel:`Create Resources`.
#. To select a type, choose :guilabel:`Note` in the drop-down.
#. Scroll to the bottom of the page, and then choose :guilabel:`Create.`
#. Wait for the Amazon DynamoDB *create table* operation to complete.

To try out some operations, choose :guilabel:`Queries` on the left. Replace the content of the queries editor with the following code. These are the GraphQL commands that our application will execute.

.. code-block:: json


    query ListAllNotes {
        allNote {
            noteId, title
        }
    }

    query GetNote($noteId:ID!) {
        getNote(noteId:$noteId) {
            noteId, title, content
        }
    }

    mutation SaveNote($noteId:ID!,$title:String!,$content:String!) {
        putNote(noteId:$noteId, title:$title, content:$content) {
            noteId, title, content
        }
    }

    mutation DeleteNote($noteId:ID!) {
        deleteNote(noteId:$noteId) {
            noteId
        }
    }

Choose :guilabel:`Query Variables` at the bottom of the queries editor to expand the variable edit field, and then copy paste the following.

.. code-block:: json

    {
      "noteId": "4c34d384-b715-4258-9825-1d34e8e6003b",
      "title": "Console Test",
      "content": "A test from the console"
    }

You can run each command by using the play button at the top of the queries editor. Then, you can select the query or mutation that you want to perform. For example, use :code:`SaveNote`, then :code:`ListAllNotes` to list the note you just saved. Don’t forget to change the :code:`noteId` between successive :code:`SaveNote` runs because the :code:`noteId` must be unique.

Link AWS AppSync to your App
----------------------------

The next step is to link the data source that you’ve just created to the app you’re working on.

#. Go to the AWS AppSync console.
#. Choose your API.
#. Scroll down to the :guilabel:`Integrate your GraphQL API` section and choose :guilabel:`React Native`, and Choose :guilabel:`Download`.
#. Save the downloaded :file:`AppSync.js` to your app's :file:`./src` directory.
#. Add the following libraries to your project.

    .. code-block:: bash

        yarn add react-apollo graphql-tag aws-sdk aws-appsync aws-appsync-react

#. Create the GraphQL documents file :file:`./src/graphql.js` for your app, containing the following contents.

   .. code-block:: bash

      import gql from 'graphql-tag';
      import { graphql } from 'react-apollo';

      export const ListAllNotes = gql`query ListAllNotes {
          allNote {
              noteId, title
          }
      }`;

      export const GetNote = gql`query GetNote($noteId:ID!) {
          getNote(noteId:$noteId) {
              noteId, title, content
          }
      }`;

      export const SaveNote = gql`mutation SaveNote($noteId:ID!,$title:String!,$content:String!) {
          putNote(noteId:$noteId, title:$title, content:$content) {
              noteId, title, content
          }
      }`;

      export const DeleteNote = gql`mutation DeleteNote($noteId:ID!) {
          deleteNote(noteId:$noteId) {
              noteId
          }
      }`;

      export const operations = {
          ListAllNotes: graphql(ListAllNotes, {
              options: {
                  fetchPolicy: 'network-only'
              },
              props: ({ data }) => {
                  return {
                      loading: data.loading,
                      notes: data.allNote
                  };
              }
          }),

           GetNote: graphql(GetNote, {
              options: props => {
                  return {
                      fetchPolicy: 'network-only',
                      variables: { noteId: props.navigation.state.params.noteId }
                  };
              },
              props: ({ data }) => {
                  return {
                      loading: data.loading,
                      note: data.getNote
                  }
              }
          }),

          DeleteNote: graphql(DeleteNote, {
                options: {
                    refetchQueries: [ { query: ListAllNotes } ]
                },
                props: props => ({
                    deleteNote: (noteId) => {
                        return props.mutate({
                            variables: { noteId },
                            optimisticResponse: {
                                deleteNote: { noteId, __typename: 'Note' }
                            }
                        })
                    }
                })
            }),

            SaveNote: graphql(SaveNote, {
              options: {
                  refetchQueries: [ { query: ListAllNotes } ]
              },
              props: props => ({
                  saveNote: (note) => {
                      return props.mutate({
                          variables: note,
                          optimisticResponse: {
                              putNote: { ...note, __typename: 'Note' }
                          }
                      })
                  }
              })
          })
      };

   Note that the GraphQL documents are identical to the ones that are used inside the AWS AppSync console for running the queries and mutations manually. This block binds the GraphQL queries and mutations to function props on the React-Native components.

#. Update the imports in :file:`App.js` with the following to instantiate the AppSync connection.

   .. code-block:: bash

      // import { Provider } from 'react-redux';
      // import { PersistGate } from 'redux-persist/es/integration/react';
      // import { persistor, store } from './src/redux/store';

      import AWSAppSyncClient from 'aws-appsync';
      import { Rehydrated } from 'aws-appsync-react';
      import { ApolloProvider } from 'react-apollo';
      import appsyncConfig from './src/AppSync';

      const appsyncClient = new AWSAppSyncClient({
        url: appsyncConfig.graphqlEndpoint,
        region: appsyncConfig.region,
        auth: { type: appsyncConfig.authenticationType, apiKey: appsyncConfig.apiKey }
      });

   The commented-out imports are used by React Redux to provide a local store. We no longer need them because we’re using a GraphQL-based store. If you’re integrating into your own app and still need access to the Redux store in addition to the GraphQL store, see the React Apollo documentation on how to do this.

#. Replace the return value from the App component of :file:`App.js` with the following.

   .. code-block:: bash

        return (
          <ApolloProvider client={appsyncClient}>
            <Rehydrated>
              <Navigator/>
            </Rehydrated>
          </ApolloProvider>
        );

#. To remove Redux connectivity in the screens, update :file:`./src/screens/NoteListScreen.js and :file:`./src/screens/NoteDetailsScreen.js`. In each file:

   * Comment out the Redux imports and replace them with AppSync imports as follows.

   .. code-block:: bash

        // BEGIN-REDUX
        // import { connect } from 'react-redux';
        // import actions from '../redux/actions';
        // END-REDUX

        // BEGIN APPSYNC
        import { compose } from 'react-apollo';
        import * as GraphQL from '../graphql';
        // END APPSYNC

   * Then, at the bottom of the file, comment out blocks between the //BEGIN-REDUX and //END-REDUX comments. This includes the ones containing:

      * :code:`mapStateToProps`
      * :code:`mapDispatchToProps`
      * :code:`connect`


#. Add the following code block to the bottom of the :file:`./src/screens/NoteListScreen.js` file, just before the export default line:

   .. code-block:: bash

       const NoteListScreen = compose(
         GraphQL.operations.ListAllNotes,
         GraphQL.operations.DeleteNote
       )(NoteList);

#. Add the following code block to the bottom of the ./src/screens/NoteDetailsScreen.js file:

   .. code-block:: bash

      const NoteDetailsScreen = compose(
        GraphQL.operations.GetNote,
        GraphQL.operations.SaveNote
      )(NoteDetails);

#. Run the application. Use the app to add and delete some notes.
#. Go to the DynamoDB console and check the table for your connection. You should see a representation of the current set of notes.

Controlling Offline Access
----------------------------

You can move from online access to offline access by changing the fetchPolicy within the operations block of ./src/graphql.js from ‘network-only’ (which is to say – it always querys the backend server) to one of the other possible options:

    * ‘cache-first’ always returns data from the cache if the data is available. Data is fetched from the network only if a cached result isn’t available.
    * ‘cache-and-network’ always queries the network for data, regardless of whether the full data is in your cache. It returns the cache if it’s available. This option is for returning data quickly, but keeping the cached data consistent with the server (note that it might result in some UI “flipping of data” issues).
    * ‘network-only’ ignores the cache.
    * ‘cache-only’ ignores the network.

The most reasonable option is ‘cache-and-network’ for this use case. For more details on using AWS AppSync in an offline mode, see the `AWS AppSync documentation <https://docs.aws.amazon.com/appsync/latest/devguide/building-a-client-app-reactnative.html#offline-settings>`__.



