.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _reference-s3-security:

############################################
|S3| Security Considerations for |AMH| Users
############################################


.. meta::
   :description: Describes |S3long| (|S3|) security considerations for |AMHlong| users.


.. list-table::
   :widths: 1

   * - **Looking for the AWS SDKs for iOS and Android?** These SDKs and their docs are now part of `AWS Amplify <https://amzn.to/am-amplify-docs>`__.

       The content on this page applies only to apps that were configured using AWS Mobile Hub or awsmobile CLI. For existing apps that use AWS Mobile SDK prior to v2.8.0, we highly recommend you migrate your app to use `AWS Amplify <https://amzn.to/am-amplify-docs>`__ and the latest SDK.

When you enable the |AMH| User File Storage or Hosting and Streaming features, it creates an |S3|
bucket in your account. This topic describes the key |S3| security-related features that you might
want to use for this bucket. Hosting and Streaming also configures a |CF| distribution that caches
the assets stored in the bucket it creates. For the same type of information regarding the
distribution, see :ref:`cloudfront-security`.

.. _s3-security-access:

Access management
=================


By default, access to |S3| buckets and related objects are private: only the resource owner can
access a bucket or assets contained in it. The administrator of a bucket can grant access that suits
their design by attaching resource-based policies, such as bucket policy or access control lists
(ACLs) to grant access to users or groups of users.

The Amazon S3 configuration provisioned by the AWS Mobile Hub :ref:`hosting-and-streaming` feature is example
of setting bucket policy to a allow access to all users. This access policy makes sense in the
context of publicly hosting a web app through this feature. We recommend, if it meets app design
criteria, that developers also add the :ref:`user-sign-in` feature so that only authenticated users
have access to an app's AWS resources like buckets and database.

For more information, see `Managing Access Permissions to Your Amazon S3 Resources
<http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the :title:`Amazon S3 Developer Guide`.


.. _s3-security-lifecycle:

Object Lifecycle Management
===========================


You can use object lifecycle management to have |S3| take actions on files (also referred to in |S3|
as :emphasis:`objects`) in a bucket based on specific criteria. For example, after a specific amount
of time since a mobile app user uploaded a file to the bucket, you might want to permanently delete
that file or move it to |GLlong|. You might want to do this to reduce the amount of data in files
that other mobile app users can potentially access. You might also want to manage your costs by
deleting or archiving files that you know you or mobile app users no longer need.

For more information, see `Object Lifecycle Management <http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`__ in the
:title:`Amazon S3 Developer Guide`.


.. _s3-security-encryption:

Object Encryption
=================


Object encryption helps increase the protection of the data in files while they are traveling to and
from a bucket as well as while they are in a bucket. You can use |S3| to encrypt the files, or you
can encrypt the files yourself. Files can be encrypted with an |S3|-managed encryption key, a key
managed by |KMSlong| (|KMS|), or your own key.

For more information, see the `Protecting Data Using Encryption <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html>`__ section in
the :title:`Amazon S3 Developer Guide`.


.. _s3-security-versioning:

Object Versioning
=================


Object versioning helps you recover data in files more easily after unintended mobile app user
actions and mobile app failures. Versioning enables you to store multiple states of the same file in
a bucket. You can uniquely access each version by its related file name and version ID. To help
manage your costs, you can delete or archive older versions that you no longer need, or you can
suspend versioning.

For more information, see the `Using Versioning <http://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html>`__ section in the
:title:`Amazon S3 Developer Guide`.


.. _s3-security-logging:

Bucket Logging
==============


Bucket logging helps you learn more about your app users, helps you meet your organization's audit
requirements, and helps you understand your |S3| costs. Each access log record provides details
about a single access request, such as the requester, bucket name, request time, request action,
response status, and error code, if any. You can store logs in the same bucket or in a different
one. To help manage your costs, you can delete logs that you no longer need, or you can suspend
logging.

For more information, see `Managing Bucket Logging <http://docs.aws.amazon.com/AmazonS3/latest/user-guide/ManagingBucketLogging.html>`__ in the
:title:`Amazon S3 User Guide`.



