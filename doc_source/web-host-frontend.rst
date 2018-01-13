.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-host-frontend:

################
Access Your APIs
################


.. meta::
    :description:
        Learn how to use |AMHlong| (|AMH|) to create, build, test and monitor mobile apps that are
        integrated with AWS services.

.. contents::
   :local:
   :depth: 2


About Hosting and Streaming
===========================

The AWS Mobile :ref:`Hosting and Streaming <hosting-and-streaming>`feature is especially useful to web dvelopers. It uses the ability of `|S3| <>`_ buckets to statically host content and the `|CF| <>`_ content distribution network (CDN) to host on an endpoint close to every user globally. Amazon CLoudFront endpoints can also stream media content.

**About the Hosting and Streaming Sample App**

When you enable Hosting and Streaming , |AMH| provisions content in the root of your
source bucket which includes a local copy of the |JSBlong|
(:file:`aws-min.js`).


* :file:`aws-sdk.min.js` - An |JSBlong| source file.

* :file:`aws-config.js,`- A web app configuration file that is generated to contain constants for the endpoints for each |AMH| feature you have enabled for this project.

* `index.html` - Which uses a constant formed in :file:`aws-config.js` to request and display an AWS guest (unauthenticated) user identity ID from the |COG| service.

When you enable Hosting and Streaming an |CFlong| global content delivery network (CDN)
distribution is created and associated with your bucket. When |AMH| propagates the sample
web app content to the bucket, the content is then propagated to the CDN and becomes
available from local endpoints around the globe. If you configure `CloudFront streaming
<http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Tutorials.html>`_, then media content you upload to your |S3| bucket can be streamed from
those endpoints.

** To view the Hosting and Streaming Sample App

The |AMH| Hosting and Streaming feature creates a sample JavaScript web app that
demonstrates connecting to the AWS resources of your |AMH| project.

The sample app web assets are deployed to an |S3| bucket. The bucket is configured to host
static web content for public access.


#. In the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`_, open your project and then choose the Hosting and Streaming tile.

#. Choose :guilabel:`View from S3`.

   This opens a browser and displays the :file:`index.html` of the sample web app from the |S3| bucket.

    .. image:: images/add-aws-mobile-add-hosting-and-streaming-view-from-s3.png
       :scale: 100
       :alt: Image of the |AMH| console.

    .. only:: pdf

       .. image:: images/add-aws-mobile-add-hosting-and-streaming-view-from-s3.png
          :scale: 50

    .. only:: kindle

       .. image:: images/add-aws-mobile-add-hosting-and-streaming-view-from-s3.png
          :scale: 75


Configure a Custom Domain for Your Web App
==========================================

 To use your custom domain for linking to your Web app, use the |R53| service to configure DNS
 routing.

 For a web app hosted in a single location, see `Routing Traffic to a Website that Is Hosted in
 an Amazon S3 Bucket <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html>`_.

 For a web app distributed through a global CDN, see `Routing Traffic to an Amazon CloudFront
 Web Distribution by Using Your Domain Name <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloud-fron-distribution.html>`_