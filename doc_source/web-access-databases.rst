.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-access-databases:


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


The AWS Mobile CLI and Amplify library make it easy to perform create, read, update, and delete ("CRUD") actions against data stored in the cloud through simple API calls in your JavaScript app.

Set Up Your Backend
===================

**To create a database**

#. Enable the NoSQL database feature and configure your table.

   In the root folder of your app, run:

   .. code:: bash

      awsmobile database enable --prompt

#. Choose :code:`Open` to make the data in this table viewable by all users of your application.

   .. code:: bash

      ? Should the data of this table be open or restricted by user?
      ❯ Open
        Restricted

#. For this example type in :userinput:`todos` as your :code:`Table name`.

   .. code:: bash

      ? Table name: todos

Add columns and queries
~~~~~~~~~~~~~~~~~~~~~~~

You are creating a table in a `NoSQL database <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html>`_ and adding an initial set of columns, each of which has a name and a data type. NoSQL lets you add a column any time you store data that contains a new column. NoSQL tables must have one column defined as the Primary Key, which is a unique identifier for each row.

#. For this example, follow the prompts to add three columns: :userinput:`team` (string), :userinput:`todoId` (number), and :userinput:`text` (string).

   .. code:: bash

      ? What would you like to name this column: team
      ? Choose the data type: string

#. When prompted to :code:`? Add another column`, type :userinput:`Y` and then choose enter. Repeat the steps to create :userinput:`todoId` and :userinput:`text` columns.

#. Select :code:`team` as the primary key.

   .. code:: bash

        ? Select primary key
        ❯ team
          todoId
          text

#. Choose :code:`(todoId)` as the sort key and then :code:`no` to adding any more indexes, to keep the example simple.

   .. list-table::
      :widths: 1 6

      * - Sort Keys and Indexes

        - To optimize preformance, you can define a column as a Sort Key. Choose a column to be a Sort Key if it will be frequently used in combination with the Primary key to query your table. You can also create Secondary Indexes to make addtional columns sort keys.

   .. code:: bash

          ? Select sort key
          ❯ todoId
            text
            (No Sort Key)

          ? Add index (Y/n): n
          Table todos saved.

   The :code:`todos` table is now created.

Use a cloud API to do CRUD operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To access your NoSQL database, you will create an API that can be called from your app to perform CRUD operations.

.. list-table::
   :widths: 1 6

   * - Why an API?

     - Using an API to access your database provides a simple coding interface on the frontend and robust flexibility on the backend. Behind the scenes, a call to an `Amazon API Gateway <http://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`_ API end point in the cloud is handled by a serverless `Lambda <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_ function.

**To create a CRUD API**

#. Enable and configure the CLoud Logic featue**

   .. code:: bash

        awsmobile cloud-api enable --prompt

#. Choose  :code:`Create CRUD API for an existing Amazon DynamoDB table` API for an exisitng Amazon DynamoDB table" and then choose enter.

   .. code:: bash

        ? Select from one of the choices below. (Use arrow keys)
          Create a new API
        ❯ Create CRUD API for an existing Amazon DynamoDB table

#. Select the :code:`todos` table created in the previous steps, and choose enter.

   .. code:: bash

        ? Select Amazon DynamoDB table to connect to a CRUD API
        ❯ todos

#. Push your configuration to the cloud. Without this step, the configuration for your database and API is now in place only on your local machine.

   .. code:: bash

        awsmobile push

   The required DynamoDB tables, API Gateway endpoints, and Lambda functions will now be created.

Create your first Todo
~~~~~~~~~~~~~~~~~~~~~~

The AWS Mobile CLI enables you to test your API from the command line.

Run the following command to create your first todo.

.. code:: bash

    awsmobile cloud-api invoke todosCRUD POST /todos '{"body": {"team": "React", "todoId": 1, "text": "Learn more Amplify"}}'

Connect to Your Backend
=======================

The examples in this section show how you would integrate AWS Amplify library calls using React (see the `AWS Amplify documentation <https://aws.github.io/aws-amplify/>`_ to use other flavors of Javascript).

The following component is a simple Todo list that you might add to a :code:`create-react-app` project. The Todos component currently adds and displays :code:`todos` to and from an in memory array.

.. list-table::
   :widths: 1

   * - .. code:: javascript

          // To Do app example

          import React from 'react';

          class Todos extends React.Component {
            state = { team: "React", todos: [] };

            render() {
              let todoItems = this.state.todos.map(({todoId, text}) => {
                return <li key={todoId}>{text}</li>;
              });

              return (
                <div style={styles}>
                  <h1>{this.state.team} Todos</h1>
                  <ul>
                    {todoItems}
                  </ul>

                  <form>
                    <input ref="newTodo" type="text" placeholder="What do you want to do?" />
                    <input type="submit" value="Save" />
                  </form>
                </div>
              );
            }
          }

          let styles = {
            margin: "0 auto",
            width: "25%"
          };

          export default Todos;

Displaying todos from the cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :code:`API` module from AWS Amplify allows you connect to DynamoDB through |ABP| endpoints.

**To retrieve and display items in a database**

#. Import the :code:`API` module from :code:`aws-amplify` at the top of the Todos component file.

   .. code:: javascript

        import { API } from 'aws-amplify';

#. Add the following :code:`componentDidMount` to the :code:`Todos` component to fetch all of the :code:`todos`.

   .. code:: javascript

        async componentDidMount() {
          let todos = await API.get('todosCRUD', `/todos/${this.state.team}`);
          this.setState({ todos });
        }

When the :code:`Todos` component mounts it will fetch all of the :code:`todos` stored in your database and display them.

Saving todos to the cloud
~~~~~~~~~~~~~~~~~~~~~~~~~

The following fragment shows the :code:`saveTodo` function for the Todo app.

.. code:: javascript

        async saveTodo(event) {
          event.preventDefault();

          const { team, todos } = this.state;
          const todoId = todos.length + 1;
          const text = this.refs.newTodo.value;

          const newTodo = {team, todoId, text};
          await API.post('todosCRUD', '/todos', { body: newTodo });
          todos.push(newTodo);
          this.refs.newTodo.value = '';
          this.setState({ todos, team });
        }

Update the :code:`form` element in the component's render function to invoke
the :code:`saveTodo` function when the form is submitted.

.. code:: javascript

    <form onSubmit={this.saveTodo.bind(this)}>

Your entire component should look like the following:

.. list-table::
   :widths: 1

   * - .. code:: javascript

          // To Do app example

          import React from 'react';
          import { API } from 'aws-amplify';

          class Todos extends React.Component {
            state = { team: "React", todos: [] };

            async componentDidMount() {
              const todos = await API.get('todosCRUD', `/todos/${this.state.team}`)
              this.setState({ todos });
            }

            async saveTodo(event) {
              event.preventDefault();

              const { team, todos } = this.state;
              const todoId = todos.length + 1;
              const text = this.refs.newTodo.value;

              const newTodo = {team, todoId, text};
              await API.post('todosCRUD', '/todos', { body: newTodo });
              todos.push(newTodo);
              this.refs.newTodo.value = '';
              this.setState({ todos, team });
            }

            render() {
              let todoItems = this.state.todos.map(({todoId, text}) => {
                return <li key={todoId}>{text}</li>;
              });

              return (
                <div style={styles}>
                  <h1>{this.state.team} Todos</h1>
                  <ul>
                    {todoItems}
                  </ul>

                  <form onSubmit={this.saveTodo.bind(this)}>
                    <input ref="newTodo" type="text" placeholder="What do you want to do?" />
                    <input type="submit" value="Save" />
                  </form>
                </div>
              );
            }
          }

          let styles = {
            margin: "0 auto",
            width: "25%"
          }

          export default Todos;


Next Steps
----------

-  Learn how to retrieve specific items and more with the `API module in AWS Amplify <https://aws.github.io/aws-amplify/media/developer_guide.html>`_.

-  Learn how to enable more features for your app with the `AWS Mobile CLI <https://aws.github.io/aws-amplify>`_.

