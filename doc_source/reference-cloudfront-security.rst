.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-cloudfront-security:

################################################
|CFlong| Security Considerations for |AMH| Users
################################################


.. meta::
   :description: Describes |CFlong| security considerations for |AMHlong| users.


When you enable the AWS Mobile Hub :ref:`hosting-and-streaming` feature, an `Amazon CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/>`__
distribution is created in your account. The distribution caches the web assets you store within an
associated Amazon S3 bucket throughout a global network of Amazon edge servers. This provides your
customers with fast local access to the web assets.

This topic describes the key |CF| security-related features that you might want to use for your
distribution. For the same type of information regarding the source bucket, see :ref:`s3-security`.

.. _cloudfront-security-access:

Access management
=================


Hosting and Streaming makes assets in a distribution publically available. While this is the normal
security policy for Internet based resources, you should consider restricting access to the assets
if this is not the case. The best practice for security is to follow a ?minimal permissions? model
and restrict access to resources as much as possible. You may want to modify resource-based
policies, such as the distribution policy or access control lists (ACLs), to grant access only to
some users or groups of users.

To protect access to any AWS resources associated with a Hosting and Streaming web app, such as
buckets and database tables, we recommend restricting access to only authenticated users. You can
add this restriction to your |AMH| project by enabling the :ref:`user-sign-in` feature, with the
sign-in required option.

For more information, see `Authentication and Access Control for CloudFront
<http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/auth-and-access-control.html>`__ in the :title:`Amazon CloudFront Developer Guide`.


.. _cloudfront-security-https:

Requiring the HTTPS Protocol
============================


|CF| supports use of the HTTPS protocol to encrypt communications to and from a distribution. This
highly recommended practice for protects both the user and the service. |CF| enables you to require
HTTPS both between customers and your distribution endpoints, and |CF| between your distribution's
caches and the source bucket where your assets originate. Global redirection of HTTP traffic to
HTTPS, use of HTTPS for custom domains and other options are also supported.

For more information, see `Using HTTPS with CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html>`__ in the
:title:`Amazon CloudFront Developer Guide`.


.. _cloudfront-security-private:

Securing Private Content
========================


|CF| supports a range of methods for protecting private content in a distribution cache. These
include the use of signed cookies and signed URLs to restrict access to authenticated, authorized
users.

A best practice is to use techniques like these on both the connection between the user and the
distribution endpoint and between the distribution and the content |S3| source bucket.

For more information, see the `Serving Private Content through CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
section in the :emphasis:`Amazon CloudFront Developer Guide`.


.. _cloudfront-security-logging:

Distribution Access Logging
===========================


Distribution logging helps you learn more about your app users, helps you meet your organization's
audit requirements, and helps you understand your |CF| costs. Each access log record provides
details about a single access request, such as the requester, distribution name, request time,
request action, response status, and error code, if any. You can store logs in an |S3| bucket. To
help manage your costs, you can delete logs that you no longer need, or you can suspend logging.

For more information, see `Access Logs for CloudFront <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>`__ in the
:title:`Amazon CloudFront Developer Guide`.



