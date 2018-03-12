.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-add-storage:

###########
Add Storage
###########

.. meta::
   :description:
        Learn how to use |AMHlong| to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. list-table::
   :widths: 1 6

   * - **BEFORE YOU BEGIN**

     - The steps on this page assume you have already completed the steps on :ref:`Get Started <web-getting-started>`.


The AWS Mobile CLI and AWS Amplify library make it easy to store and manage files in the cloud from your JavaScript app.

Set Up the Backend
------------------

Enable the User File Storage feature by running the following commands in the root folder of your app.

.. code:: bash

    awsmobile user-files enable

    awsmobile push

Connect to the Backend
----------------------

The examples in this section show how you would integrate AWS Amplify library calls using React (see the `AWS Amplify documentation <https://aws.github.io/aws-amplify>`__ to use other flavors of Javascript).

The following simple component could be added to a :code:`create-react-app` project to present an interface that uploads images and download them for display.


.. list-table::
   :widths: 1

   * - .. code:: javascript

          // Image upload and download for display example component
          // src/ImageViewer.js

          import React, { Component } from 'react';

          class ImageViewer extends Component {
            render() {
              return (
                <div>
                  <p>Pick a file</p>
                  <input type="file" />
                </div>
              );
            }
          }

          export default ImageViewer;

Upload a file
~~~~~~~~~~~~~

The :code:`Storage` module enables you to upload files to the cloud. All uploaded files are publicly viewable by default.

Import the :code:`Storage` module in your component file.

.. code:: javascript

    // ./src/ImageViewer.js

    import { Storage } from 'aws-amplify';

Add the following function to use the :code:`put` function on the :code:`Storage` module to upload the file to the cloud, and set your component’s state to the name of the file.

.. code:: javascript

    uploadFile(event) {
      const file = event.target.files[0];
      const name = file.name;

      Storage.put(key, file).then(() => {
        this.setState({ file: name });
      });
    }

Place a call to the :code:`uploadFile` function in the :code:`input` element of the component’s render function, to start upload when a user selects a file.

.. code:: javascript

      render() {
        return (
          <div>
            <p>Pick a file</p>
            <input type="file" onChange={this.uploadFile.bind(this)} />
          </div>
        );
      }

Display an image
~~~~~~~~~~~~~~~~

To display an image, this example shows the use of the  :code:`S3Image` component of the AWS Amplify for React library.

#. From a terminal, run the following command in the root folder of your app.

   .. code-block:: bash

      npm install --save aws-amplify-react

#. Import the :code:`S3Image` module in your component.

   .. code:: javascript

    import { S3Image } from 'aws-amplify-react';

Use the S3Image component in the render function. Update your render function to look like the following:

.. code:: javascript

    render() {
      return (
         <div>
           <p>Pick a file</p>
           <input type="file" onChange={this.handleUpload.bind(this)} />
           { this.state && <S3Image path={this.state.path} /> }
         </div>
      );
    }


.. list-table::
   :widths: 1

   * - Put together, the entire component should look like this:


       .. code:: javascript

          // Image upload and download for display example component

          import React, { Component } from 'react';
          import { Storage } from 'aws-amplify';
          import { S3Image } from 'aws-amplify-react';

          class ImageViewer extends Component {

            handleUpload(event) {
              const file = event.target.files[0];
              const path = file.name;
              Storage.put(path, file).then(() => this.setState({ path }) );
            }

            render() {
              return (
                <div>
                  <p>Pick a file</p>
                  <input type="file" onChange={this.handleUpload.bind(this)} />
                  { this.state && <S3Image path={this.state.path} /> }
                </div>
              );
            }
          }

          export default ImageViewer;


Next Steps
==========

-  Learn how to do private file storage and more with the
   `Storage module in AWS Amplify <https://aws.github.io/aws-amplify/media/developer_guide.html>`__.

-  Learn how to enable more features for your app with the `AWS Mobile CLI <https://aws.github.io/aws-amplify>`__.

-  Learn how to use those features in your app with the `AWS Amplify library <https://aws.github.io/aws-amplify>`__.

-  Learn more about the `analytics for the User File Storage feature <https://alpha-docs-aws.amazon.com/pinpoint/latest/developerguide/welcome.html>`__.

-  Learn more about how your files are stored on `Amazon Simple Storage Service <https://aws.amazon.com/documentation/s3/>`__.
