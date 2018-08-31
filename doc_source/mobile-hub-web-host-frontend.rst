
.. _web-host-frontend:

#################
Host Your Web App
#################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

.. contents::
   :local:
   :depth: 2


About Hosting and Streaming
===========================


The first time that you push your web app to the cloud, the Hosting and Streaming feature is enabled to statically host your app on the web. Using the AWS Mobile CLI, this happens when you first run:

.. code-block:: bash

   $ awsmobile publish


A container for your content is created using an `Amazon S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ bucket. The content is available publicly on the Internet and you can preview the content directly using a testing URL.

Content placed in your bucket is automatically distributed to a global content delivery network (CDN). `Amazon CloudFront <https://aws.amazon.com/cloudfront/>`__ implements the CDN which can host your app on an endpoint close to every user, globally. These endpoints can also stream media content. To learn more, see `CloudFront Streaming Tutorials <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/url-cf-dev;Tutorials.html>`__.

By default, Hosting and Streaming deploys a simple sample web app that accesses AWS services.

.. _manage-app-assets:

Managing Your App Assets
========================

You can use the AWS Mobile CLI or the |S3| console to manage the content of your bucket.

.. _manage-app-assets-use-cli:

Use the AWS CLI to Manage Your Bucket Contents
----------------------------------------------

AWS CLI allows you to review, upload, move or delete your files stored in your bucket using the command line. To install and configure the AWS CLI client, see `Getting Set Up with the AWS Command Line Interface <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html>`__.

As an example, the sync command enables transfer of files to and from your local folder
(:code:`source`) and your bucket (:code:`destination`).

.. code-block:: bash

   $ aws s3 sync {source destination} [--options]

The following command syncs all files from your current local folder to the folder in your web app's bucket defined by :code:`path`.

.. code-block:: bash

   $ aws s3 sync . s3://my-web-app-bucket/path

To learn more about using AWS CLI to manage Amazon S3, see `Using Amazon S3 with the AWS Command Line Interface <https://docs.aws.amazon.com/cli/latest/userguide/cli-s3.html>`__

.. _manage-app-assets-use-s3-console:

Use the Amazon S3 Console to Manage Your Bucket
-----------------------------------------------

To use the Amazon S3 console to review, upload, move or delete your files stored in your bucket, use the following steps.

#. From the root of your project, run:

   .. code-block:: bash

      awsmobile console

#. Choose the tile with the name of your project, then choose the Hosting and Streaming tile.

#. Choose the link labelled :guilabel:`Manage files` to display the contents of your bucket in the Amazon S3 console.

   .. image:: images/hosting-and-streaming-manage-files-link.png


Other Useful Functions in the AWS Mobile Hub Console
----------------------------------------------------

The |AMH| console also provides convenient ways to browse to your web content, return to the AWS CLI content on this page, and other relevant tasks. These include:

    * The :guilabel:`View from S3` link browses to the web contents of your bucket. When Hosting and Streaming is enabled, the bucket is populated with the files for a default web app files that is viewable immediately.

      .. image:: images/hosting-and-streaming-view-s3-link.png

    * The :guilabel:`View from CloudFront` browses to the web contents that have  propagated from your bucket to CDN. The endpoint propagation is dependent on network conditions. You can expect your content to be distributed and viewable within one hour.

      .. image:: images/hosting-and-streaming-view-cloudfront-link.png

    * The :guilabel:`Sync files with the command line` link takes you to content on this page that describes how to use the command line to manage the web app and streaming media files in your bucket.

      .. image:: images/hosting-and-streaming-cli-sync-files-link.png


Configure a Custom Domain for Your Web App
==========================================

 To use your custom domain for linking to your Web app, use the |R53| service to configure DNS
 routing.

 For a web app hosted in a single location, see `Routing Traffic to a Website that Is Hosted in
 an Amazon S3 Bucket <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html>`__.

 For a web app distributed through a global CDN, see `Routing Traffic to an Amazon CloudFront
 Web Distribution by Using Your Domain Name <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloud-fron-distribution.html>`__