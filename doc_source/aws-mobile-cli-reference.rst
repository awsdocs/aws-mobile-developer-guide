
.. _aws-mobile-cli-reference:

#######################
AWS Mobile CLI Reference
#######################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

The AWS Mobile CLI provides a command line interface for frontend JavaScript developers to seamlessly enable AWS services and configure into their apps. With minimal configuration, you can start using all of the functionality provided by the the `AWS Mobile Hub <http://console.aws.amazon.com/mobilehub>`__ from your favorite terminal program.

Installation and Usage
======================

This section details the usage and the core commands of the :code:`awsmobile CLI` for JavaScript.

Install AWS Mobile CLI
-----------------------

#. `Sign up for the AWS Free Tier <https://aws.amazon.com/free/>`__.

#. Install `Node.js <https://nodejs.org/en/download/>`__ with NPM.

#. Install AWS Mobile CLI

   .. code-block:: bash

       npm install -g awsmobile-cli

#. Configure the CLI with your AWS credentials

   To setup permissions for the toolchain used by the CLI, run:

   .. code-block:: bash

      awsmobile configure

   If prompted for credentials, follow the steps provided by the CLI. For more information, see :ref:`provide IAM credentials to AWS Mobile CLI <aws-mobile-cli-credentials>`.



Usage
-----

The AWS Mobile CLI usage is designed to resemble other industry standard command line interfaces.

.. code-block:: bash

  awsmobile <command> [options]

The :code:`help` and :code:`version` options are universal to all the commands. Additional special options for some commands are detailed in the relevant sections.

.. code-block:: bash

  -V, --version  output the version number
  -h, --help     output usage information

For example:

.. code-block:: bash

    awsmobile -help
    or
    awsmobile init --help

Summary of CLI Commands
=======================

The current set of commands supported by the :code:`awsmobile CLI` are listed below.

.. list-table::
   :widths: 3 4

   * - :ref:`awsmobile init <aws-mobile-cli-reference-init>`

     - Initializes a new Mobile Hub project, checks for IAM keys, and pulls the aws-exports.js file

   * - :ref:`awsmobile configure <aws-mobile-cli-reference-configure>`

     - Shows existing keys and allows them to be changed if already set. If keys aren’t set, deep links the user to the IAM console to create keys and then prompts for the access key and secret key. This command helps edit configuration settings for the aws account or the project.

   * - :ref:`awsmobile pull <aws-mobile-cli-reference-pull>`

     - Downloads the latest aws-exports.js, YAML or any other relevant project details from the Mobile Hub project

   * - :ref:`awsmobile push <aws-mobile-cli-reference-push>`

     - Uploads local metadata, Lambda code, Dynamo definitions or any other relevant project details to Mobile Hub

   * - :ref:`awsmobile publish <aws-mobile-cli-reference-publish>`

     - Executes :code:`awsmobile push`, then builds and publishes client-side application to S3 and Cloud Front

   * - :ref:`awsmobile run <aws-mobile-cli-reference-run>`

     - Executes :code:`awsmobile push`, then executes the project's start command to test run the client-side application

   * - :ref:`awsmobile console <aws-mobile-cli-reference-console>`

     - Open the web console of the awsmobile Mobile Hub project in the default browser

   * - :ref:`awsmobile features <aws-mobile-cli-reference-features>`

     - Shows available and enabled features. Toggle to select or de-select features.

   * - :ref:`awsmobile \<feature-name\> enable [--prompt] <aws-mobile-cli-reference-enable>`

     - Enables the feature with the defaults (and prompt for changes)

   * - :ref:`awsmobile \<feature-name\>  disable <aws-mobile-cli-reference-disable>`

     - Disables the feature

   * - :ref:`awsmobile \<feature-name\> configure <aws-mobile-cli-reference-feature-configure>`

     - Contains feature-specific sub commands like add-table, add-api, etc.

   * - :ref:`awsmobile cloud-api invoke \<apiname\> \<method\> \<path\> [init] <aws-mobile-cli-reference-invoke>`

     - Invokes the API for testing locally. This helps quickly test unsigned APIs in your local environment.

   * - :ref:`awsmobile delete <aws-mobile-cli-reference-delete>`

     -  Deletes the Mobile hub project.

   * - :ref:`awsmobile help [cmd] <aws-mobile-cli-reference-help>`

     - Displays help for [cmd].



.. _aws-mobile-cli-reference-init:

init
====

The :code:`awsmobile init` command initializes a new Mobile Hub project, checks for IAM keys, and pulls the aws-exports.js file.

There are two usages of the :code:`awsmobile init` command

#. Initialize the current project with awsmobilejs features

   .. code-block:: bash

      awsmobile init

   When prompted, set these project configs:

   .. code-block:: bash

      Please tell us about your project:
      ? Where is your project's source directory:  src
      ? Where is your project's distribution directory that stores build artifacts:  build
      ? What is your project's build command:  npm run-script build
      ? What is your project's start command for local test run:  npm run-script start

      ? What awsmobile project name would you like to use:  my-mobile-project


   The source directory is where the the AWS Mobile CLI copies the latest :code:`aws-exports.js` to be easily available for your front-end code. This file is automatically updated everytime features are added or removed. Specifying a wrong / unavailable folder will not copy the file over.

   The Distribution directly is essentially the build directory for your project. This is used during the :code:`awsmobile publish` process.

   The project's build and start values are used during the :code:`awsmobile publish` and :code:`awsmobile run` commands respectively.

   The awsmobile project name is the name of the backend project created in the Mobile hub.

   You can alter the settings about your project by using the :ref:`awsmobile configure project <aws-mobile-cli-reference-configure>` command.


#. Initialize and link to an existing awsmobile project as backend

   .. code-block:: bash

      awsmobile init <awsmobile-project-id>

   The awsmobile-project-id is the id of the existing backend project in the Mobile Hub. This command helps attach an existing backend project to your app.

#. Remove the attached awsmobile project from the backend.

   .. code-block:: bash

      awsmobile init --remove

   This command removes the attached backend project associated with your app and cleans the associated files. This will not alter your app in any way, other than removing the backend project itself.

.. _aws-mobile-cli-reference-configure:

configure
=========

The :code:`awsmobile configure` shows existing keys and allows them to be changed if already set. If keys aren’t set, deep links the user to the IAM console to create keys and then prompts for the access key and secret key. There are two possible usages of this command. Based on the argument selected, this command can be used to set or change the aws account settings OR the project settings.

.. code-block:: bash

    awsmobile configure [aws|project]

#. Configuring the aws account settings using the :code:`aws` argument. This is the default argument for this command

   .. code-block:: bash

       awsmobile configure
       or
       awsmobile configure aws

   You will be prompted with questions to set the aws account credentials as below

   .. code-block:: bash

      configure aws
      ? accessKeyId:  <ACCESS-KEY-ID>
      ? secretAccessKey:  <SECRET-ACCESS-KEY>
      ? region:  <SELECT-REGION-FROM-THE-LIST>


#. Configuring the project settings using the :code:`project` argument

   .. code-block:: bash

      awsmobile configure project

   You will be prompted with questions to configure project as detailed below

   .. code-block:: bash

      ? Where is your project's source directory:  src
      ? Where is your project's distribution directory to store build artifacts:  dist
      ? What is your project's build command:  npm run-script build
      ? What is your project's start command for local test run:  npm run-script start

#. Retrieve and display the aws credentials using the :code:`--list` option

   .. code-block:: bash

      awsmobile configure --list

.. _aws-mobile-cli-reference-pull:

pull
====

The :code:`awsmobile pull` command downloads the latest aws-exports.js, YAML and any relevant cloud / backend artifacts from the Mobile Hub project to the local dev environment. Use this command if you modified the project on the Mobile Hub and want to get the latest on your local environment.

.. code-block:: bash

   awsmobile pull


.. _aws-mobile-cli-reference-push:

push
====

The :code:`awsmobile push` uploads local metadata, Lambda code, Dynamo definitions and any relevant artifacts to Mobile Hub. Use this command when you enable, disable or configure features on your local evironment and want to update the backend project on the Mobile Hub with the relevant updates.

.. code-block:: bash

   awsmobile push

Use :code:`awsmobile push` after using :code:`awsmobile features`, :code:`awsmobile <feature> enable`, :code:`awsmobile <feature> disable` or :code:`awsmobile <feature> configure` to update the backend project appropriately. This can be used either after each of these or once after all of the changes are made locally.


.. _aws-mobile-cli-reference-publish:

publish
=======

The :code:`awsmobile publish` command first executes the awsmobile :code:`push` command, then builds and publishes client-side code to Amazon S3 hosting bucket. This command publishes the client application to s3 bucket for hosting and then opens the browser to show the index page. It checks the timestamps to automatically build the app if necessary before deployment. It checks if the client has selected hosting in their backend project features, and if not, it’ll prompt the client to update the backend with hosting feature.

.. code-block:: bash

  awsmobile publish

The publish command has a number of options to be used.

#. Refresh the Cloud Front distributions

   .. code-block:: bash

      awsmobile publish -c
       or
      awsmobile publish --cloud-front

#. Test the application on AWS Device Farm

   .. code-block:: bash

      awsmobile publish -t
      or
      awsmobile publish --test

#. Suppress the tests on AWS Device Farm

   .. code-block:: bash

      awsmobile publish -n

#. Publish the front end only without updating the backend

   .. code-block:: bash

      awsmobile publish -f
      or
      awsmobile publish --frontend-only

.. _aws-mobile-cli-reference-run:

run
===

The :code:`awsmobile run` command first executes the :code:`awsmobile push` command, then executes the start command you set in the project configuration, such as :code:`npm run start` or :code:`npm run ios`. This can be used to conveniently test run your application locally with the latest backend development pushed to the cloud.

.. code-block:: bash

   awsmobile run

.. _aws-mobile-cli-reference-console:

console
=======

The :code:`awsmobile console` command opens the web console of the awsmobile Mobile Hub project in the default browser

.. code-block:: bash

   awsmobile console


.. _aws-mobile-cli-reference-features:

features
========

The :code:`awsmobile features` command displays all the available awsmobile  features, and allows you to individually enable/disable them locally. Use the arrow key to scroll up and down, and use the space key to enable/disable each feature. Please note that the changes are only made locally, execute awsmobile push to update the awsmobile project in the cloud.

.. code-block:: bash

   awsmobile features

The features supported by the AWS Mobile CLI are:

* user-signin (|COG|)

* user-files (|S3|)

* cloud-api (|LAM| / |ABP|)

* database (|DDB|)

* analytics (Amazon Pinpoint)

* hosting (|S3| and |CF|)

.. code-block:: bash

    ? select features:  (Press <space> to select, <a> to toggle all, <i> to inverse selection)
    ❯◯ user-signin
     ◯ user-files
     ◯ cloud-api
     ◯ database
     ◉ analytics
     ◉ hosting

Use caution when disabling a feature. Disabling the feature will delete all the related objects (APIs, Lambda functions, tables etc). These artifacts can not be recovered locally, even if you re-enable the feature.

Use :code:`awsmobile push` after using :code:`awsmobile <feature> disable` to update the backend project on the AWS Mobile Hub project with the selected features.


.. _aws-mobile-cli-reference-enable:

enable
======

The :code:`awsmobile <feature> enable` enables the specified feature with the default settings. Please note that the changes are only made locally, execute :code:`awsmobile` push to update the AWS Mobile project in the cloud.

.. code-block:: bash

   awsmobile <feature> enable

The features supported by the AWS Mobile CLI are:

* user-signin (|COG|)

* user-files (|S3|)

* cloud-api (|LAM| / |ABP|)

* database (|DDB|)

* analytics (Amazon Pinpoint)

* hosting (|S3| and |CF|)


The :code:`awsmobile <feature> enable --prompt` subcommand allows user to specify the details of the mobile hub feature to be enabled, instead of using the default settings. It prompts the user to answer a list of questions to specify the feature in detail.

.. code-block:: bash

   awsmobile <feature> enable -- prompt

Enabling the :code:`user-signin` feature will prompt you to change the way it is enabled, configure advanced settings or disable sign-in feature to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

    awsmobile user-signin enable --prompt

    ? Sign-in is currently disabled, what do you want to do next (Use arrow keys)
    ❯ Enable sign-in with default settings
      Go to advance settings


Enabling the :code:`user-files` feature with the :code:`--prompt` option will prompt you to confirm usage of S3 for user files.

.. code-block:: bash

   awsmobile user-files enable --prompt

   ? This feature is for storing user files in the cloud, would you like to enable it? Yes

Enabling the :code:`cloud-api` feature with the :code:`--prompt` will prompt you to create, remove or edit an API related to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

   awsmobile cloud-api enable --prompt

    ? Select from one of the choices below. (Use arrow keys)
    ❯ Create a new API

Enabling the :code:`database` feature with the :code:`--prompt` will prompt you to with initial questions to specify your database table details related to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

    awsmobile database enable --prompt

    ? Should the data of this table be open or restricted by user? (Use arrow keys)
    ❯ Open
      Restricted

Enabling the :code:`analytics` feature with the :code:`--prompt` will prompt you to confirm usage of Pinpoint Analytics.

.. code-block:: bash

   awsmobile analytics enable --prompt

  ? Do you want to enable Amazon Pinpoint analytics? (y/N)

Enabling the :code:`hosting` feature with the :code:`--prompt` will prompt you to confirm hosting and streaming on CloudFront distribution.

.. code-block:: bash

    awsmobile hosting enable --prompt

    ? Do you want to host your web app including a global CDN? (y/N)


Execute :code:`awsmobile push` after using :code:`awsmobile <feature> enable` to to update the awsmobile project in the cloud.

.. _aws-mobile-cli-reference-disable:

disable
=======

The :code:`awsmobile <feature> disable` disables the feature in their backend project. Use caution when disabling a feature. Disabling the feature will delete all the related objects (APIs, Lambda functions, tables etc). These artifacts can not be recovered locally, even if you re-enable the feature.

.. code-block:: bash

   awsmobile <feature> disable

The features supported by the AWS Mobile CLI are:

* user-signin (|COG|)

* user-files (|S3|)

* cloud-api (|LAM| / |ABP|)

* database (|DDB|)

* analytics (Amazon Pinpoint)

* hosting `

Use :code:`awsmobile push` after using :code:`awsmobile <feature> disable` to update the backend project on the AWS Mobile Hub project with the disabled features.

.. _aws-mobile-cli-reference-feature-configure:

configure
=========

The :code:`awsmobile <feature> configure` configures the objects in the selected feature. The configuration could mean adding, deleting or updating a particular artifact. This command can be used only if the specfic feature is already enabled.

.. code-block:: bash

   awsmobile <feature> configure

The features supported by the AWS Mobile CLI are:

* user-signin (|COG|)

* user-files (|S3|)

* cloud-api (|LAM| / |ABP|)

* database (|DDB|)

* analytics (Amazon Pinpoint)

* hosting (|S3| and |CF|)

Configuring the :code:`user-signin` feature will prompt you to change the way it is enabled, configure advanced settings or disable sign-in feature to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

    awsmobile user-signin configure

    ? Sign-in is currently enabled, what do you want to do next (Use arrow keys)
    ❯ Configure Sign-in to be required (Currently set to optional)
      Go to advance settings
      Disable sign-in


Configuring the :code:`user-files` feature will prompt you to confirm usage of S3 for user files.

.. code-block:: bash

   awsmobile user-files configure

  ? This feature is for storing user files in the cloud, would you like to enable it? (Y/n)

Configuring the :code:`cloud-api` feature will prompt you to create, remove or edit an API related to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

    awsmobile cloud-api configure

    ? Select from one of the choices below. (Use arrow keys)
    ❯ Create a new API
      Remove an API from the project
      Edit an API from the project

Configuring the :code:`database` feature will prompt you to create, remove or edit a table related to the project. Selecting the desired option may prompt you with further questions.

.. code-block:: bash

  awsmobile database configure

    ? Select from one of the choices below. (Use arrow keys)
    ❯ Create a new table
      Remove table from the project
      Edit table from the project

Configuring the :code:`analytics` feature will prompt you to confirm usage of Pinpoint Analytics.

.. code-block:: bash

   awsmobile analytics configure

   ? Do you want to enable Amazon Pinpoint analytics? Yes

Configuring the :code:`hosting` feature will prompt you to confirm hosting and streaming on CloudFront distribution.

.. code-block:: bash

   awsmobile hosting configure

   ? Do you want to host your web app including a global CDN? Yes


Use :code:`awsmobile push` after using :code:`awsmobile <feature> configure` to update the backend project on the AWS Mobile Hub project with the configured features.

.. _aws-mobile-cli-reference-invoke:

invoke
======

The :code:`awsmobile cloud-api invoke` invokes the API for testing locally. This helps quickly test the unsigned API locally by passing the appropritate arguments. This is intended to be used for the development environment or debugging of your API / Lambda function.

.. code-block:: bash

   awsmobile cloud-api invoke <apiname> <method> <path> [init]

For example you could invoke the sampleCloudApi post method as shown below

.. code-block:: bash

   awsmobile cloud-api invoke sampleCloudApi post /items '{"body":{"test-key":"test-value"}}'

The above test will return a value that looks like

.. code-block:: bash

    { success: 'post call succeed!',
      url: '/items',
      body: { 'test-key': 'test-value' } }


Similarly, you could invoke the sampleCloudApi get method as shown below

.. code-block:: bash

   awsmobile cloud-api invoke sampleCloudApi get /items

The above test will return a value that looks like

.. code-block:: bash

   { success: 'get call succeed!', url: '/items' }

.. _aws-mobile-cli-reference-delete:

delete
======

The :code:`awsmobile delete` command deletes the Mobile hub project in the cloud. Use extra caution when you decide to execute this command, as it can irrevocably affect your team’s work, the mobile hub project will be delete and cannot be recovered once this command is executed.

.. code-block:: bash

   awsmobile delete

.. _aws-mobile-cli-reference-help:

help
====

The :code:`awsmobile help` command can be used as a standalone command or the command name that you need help in can be passed as an argument. This gives the usage information for that command including any options that can be used with it.

For Example:

.. code-block:: bash

    awsmobile help
    or
    awsmobile help init


The :code:`--help` option detailing at the beginning of this page and the :code:`awsmobile help` command provide the same level of detail. The difference is in the usage.

