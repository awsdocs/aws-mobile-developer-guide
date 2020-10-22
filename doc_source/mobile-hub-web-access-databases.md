# Access Your Database<a name="mobile-hub-web-access-databases"></a>

**Important**  
The following content applies if you are already using the AWS Mobile CLI to configure your backend\. If you are building a new mobile or web app, or you’re adding cloud capabilities to your existing app, use the new [AWS Amplify CLI](http://aws-amplify.github.io/) instead\. With the new Amplify CLI, you can use all of the features described in [Announcing the AWS Amplify CLI toolchain](http://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/), including AWS CloudFormation functionality that provides additional workflows\.

## Set Up Your Backend<a name="set-up-your-backend"></a>

The AWS Mobile CLI and Amplify library make it easy to perform create, read, update, and delete \(“CRUD”\) actions against data stored in the cloud through simple API calls in your JavaScript app\.


|  |  | 
| --- |--- |
|   **BEFORE YOU BEGIN**   |  The steps on this page assume you have already completed the steps on [Get Started](mobile-hub-web-getting-started.md)\.  | 

 **To create a database** 

1. Enable the NoSQL database feature and configure your table\.

   In the root folder of your app, run:

   ```
   awsmobile database enable --prompt
   ```

1. Choose `Open` to make the data in this table viewable by all users of your application\.

   ```
   ? Should the data of this table be open or restricted by user?
   ❯ Open
     Restricted
   ```

1. For this example type in `todos` as your `Table name`\.

   ```
   ? Table name: todos
   ```

### Add columns and queries<a name="add-columns-and-queries"></a>

You are creating a table in a [NoSQL database](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html) and adding an initial set of columns, each of which has a name and a data type\. NoSQL lets you add a column any time you store data that contains a new column\. NoSQL tables must have one column defined as the Primary Key, which is a unique identifier for each row\.

1. For this example, follow the prompts to add three columns: `team` \(string\), `todoId` \(number\), and `text` \(string\)\.

   ```
   ? What would you like to name this column: team
   ? Choose the data type: string
   ```

1. When prompted to `? Add another column`, type `Y` and then choose enter\. Repeat the steps to create `todoId` and `text` columns\.

1. Select `team` as the primary key\.

   ```
   ? Select primary key
   ❯ team
     todoId
     text
   ```

1. Choose `(todoId)` as the sort key and then `no` to adding any more indexes, to keep the example simple\.    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/mobile-hub-web-access-databases.html)

   ```
   ? Select sort key
   ❯ todoId
     text
     (No Sort Key)
   
   ? Add index (Y/n): n
   Table todos saved.
   ```

   The `todos` table is now created\.

### Use a cloud API to do CRUD operations<a name="use-a-cloud-api-to-do-crud-operations"></a>

To access your NoSQL database, you will create an API that can be called from your app to perform CRUD operations\.


|  |  | 
| --- |--- |
|  Why an API?  |  Using an API to access your database provides a simple coding interface on the front end and robust flexibility on the backend\. Behind the scenes, a call to an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) API end point in the cloud is handled by a serverless [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function\.  | 

 **To create a CRUD API** 

1. Enable and configure the Cloud Logic feature\*\*

   ```
   awsmobile cloud-api enable --prompt
   ```

1. Choose `Create CRUD API for an existing Amazon DynamoDB table` API for an existing Amazon DynamoDB table” and then choose enter\.

   ```
   ? Select from one of the choices below. (Use arrow keys)
     Create a new API
   ❯ Create CRUD API for an existing Amazon DynamoDB table
   ```

1. Select the `todos` table created in the previous steps, and choose enter\.

   ```
   ? Select Amazon DynamoDB table to connect to a CRUD API
   ❯ todos
   ```

1. Push your configuration to the cloud\. Without this step, the configuration for your database and API is now in place only on your local machine\.

   ```
   awsmobile push
   ```

   The required DynamoDB tables, API Gateway endpoints, and Lambda functions will now be created\.

### Create your first Todo<a name="create-your-first-todo"></a>

The AWS Mobile CLI enables you to test your API from the command line\.

Run the following command to create your first todo\.

```
awsmobile cloud-api invoke todosCRUD POST /todos '{"body": {"team": "React", "todoId": 1, "text": "Learn more Amplify"}}'
```

## Connect to Your Backend<a name="connect-to-your-backend"></a>

The examples in this section show how you would integrate AWS Amplify library calls using React \(see the [AWS Amplify documentation](https://aws.github.io/aws-amplify/) to use other flavors of Javascript\)\.

The following component is a simple Todo list that you might add to a `create-react-app` project\. The Todos component currently adds and displays `todos` to and from an in memory array\.


|  | 
| --- |
|  <pre>// To Do app example<br /><br />import React from 'react';<br /><br />class Todos extends React.Component {<br />  state = { team: "React", todos: [] };<br /><br />  render() {<br />    let todoItems = this.state.todos.map(({todoId, text}) => {<br />      return <li key={todoId}>{text}</li>;<br />    });<br /><br />    return (<br />      <div style={styles}><br />        <h1>{this.state.team} Todos</h1><br />        <ul><br />          {todoItems}<br />        </ul><br /><br />        <form><br />          <input ref="newTodo" type="text" placeholder="What do you want to do?" /><br />          <input type="submit" value="Save" /><br />        </form><br />      </div><br />    );<br />  }<br />}<br /><br />let styles = {<br />  margin: "0 auto",<br />  width: "25%"<br />};<br /><br />export default Todos;</pre>  | 

### Displaying todos from the cloud<a name="displaying-todos-from-the-cloud"></a>

The `API` module from AWS Amplify allows you connect to DynamoDB through API Gateway endpoints\.

 **To retrieve and display items in a database** 

1. Import the `API` module from `aws-amplify` at the top of the Todos component file\.

   ```
   import { API } from 'aws-amplify';
   ```

1. Add the following `componentDidMount` to the `Todos` component to fetch all of the `todos`\.

   ```
   async componentDidMount() {
     let todos = await API.get('todosCRUD', `/todos/${this.state.team}`);
     this.setState({ todos });
   }
   ```

When the `Todos` component mounts it will fetch all of the `todos` stored in your database and display them\.

### Saving todos to the cloud<a name="saving-todos-to-the-cloud"></a>

The following fragment shows the `saveTodo` function for the Todo app\.

```
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
```

Update the `form` element in the component’s render function to invoke the `saveTodo` function when the form is submitted\.

```
<form onSubmit={this.saveTodo.bind(this)}>
```

Your entire component should look like the following:


|  | 
| --- |
|  <pre>// To Do app example<br /><br />import React from 'react';<br />import { API } from 'aws-amplify';<br /><br />class Todos extends React.Component {<br />  state = { team: "React", todos: [] };<br /><br />  async componentDidMount() {<br />    const todos = await API.get('todosCRUD', `/todos/${this.state.team}`)<br />    this.setState({ todos });<br />  }<br /><br />  async saveTodo(event) {<br />    event.preventDefault();<br /><br />    const { team, todos } = this.state;<br />    const todoId = todos.length + 1;<br />    const text = this.refs.newTodo.value;<br /><br />    const newTodo = {team, todoId, text};<br />    await API.post('todosCRUD', '/todos', { body: newTodo });<br />    todos.push(newTodo);<br />    this.refs.newTodo.value = '';<br />    this.setState({ todos, team });<br />  }<br /><br />  render() {<br />    let todoItems = this.state.todos.map(({todoId, text}) => {<br />      return <li key={todoId}>{text}</li>;<br />    });<br /><br />    return (<br />      <div style={styles}><br />        <h1>{this.state.team} Todos</h1><br />        <ul><br />          {todoItems}<br />        </ul><br /><br />        <form onSubmit={this.saveTodo.bind(this)}><br />          <input ref="newTodo" type="text" placeholder="What do you want to do?" /><br />          <input type="submit" value="Save" /><br />        </form><br />      </div><br />    );<br />  }<br />}<br /><br />let styles = {<br />  margin: "0 auto",<br />  width: "25%"<br />}<br /><br />export default Todos;</pre>  | 

#### Next Steps<a name="next-steps"></a>
+ Learn how to retrieve specific items and more with the [API module in AWS Amplify](https://aws.github.io/aws-amplify/media/developer_guide.html)\.
+ Learn how to enable more features for your app with the [AWS Mobile CLI](https://aws.github.io/aws-amplify)\.