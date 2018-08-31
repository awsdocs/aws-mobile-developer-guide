
.. _react-native-host-frontend:

################
Access Your APIs
################

.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.


.. important::

   The following content applies if you are already using the AWS Mobile CLI to configure your backend. If you are building a new mobile or web app, or you're adding cloud capabilities to your existing app, use the new `AWS Amplify CLI <http://aws-amplify.github.io/>`__ instead. With the new Amplify CLI, you can use all of the features described in `Announcing the AWS Amplify CLI toolchain <https://aws.amazon.com/blogs/mobile/announcing-the-aws-amplify-cli-toolchain/>`__, including AWS CloudFormation functionality that provides additional workflows.

Publishing Your Frontend to S3 / CloudFront Distribution
========================================================

You can publish your frontend to the S3 / CloudFront Distribution using a simple command

.. code-block:: java

      awsmobile publish

The Hosting and Streaming feature enables you to host code and content in the cloud for your React app.

Mobile Hub creates a container for your content using an `Amazon S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ bucket. The content is available publicly on the Internet and you can preview the content directly using a testing URL.

Your content is automatically distributed to a global content delivery network (CDN). `Amazon
CloudFront <https://aws.amazon.com/cloudfront/>`__ also supports media file streaming. To learn more, see `CloudFront Streaming
Tutorials <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/url-cf-dev;Tutorials.html>`__.


Configure a Custom Domain for Your Web App
------------------------------------------

 To use your custom domain for linking to your Web app, use the |R53| service to configure DNS
 routing.

 For a web app hosted in a single location, see `Routing Traffic to a Website that Is Hosted in
 an Amazon S3 Bucket <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html>`__.

 For a web app distributed through a global CDN, see `Routing Traffic to an Amazon CloudFront
 Web Distribution by Using Your Domain Name <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloud-fron-distribution.html>`__
