.. Template for description of a CloudTrail supported service that lives in the services's guide.
   Because of .rst limitations, substitutions won't work in headings or links, so:

   - where you see "{{SERVICENAME_SPELLED_OUT}}" - replace with the full text of your service name.
   - where you see "|SERVICENAME|" - replace with the substitution (entity) for your service name.

.. _cloudtrail-logging-all-actions-aws-mobile:

####################################################
Logging AWS Mobile CLI API Calls with AWS CloudTrail
####################################################

.. meta::
    :description:
       Learn about logging AWS Mobile CLI with |CTlong|.

The AWS Mobile CLI is integrated with |CTlong|, a service that provides a record of actions taken by a user, role, or an AWS service in the CLI. |CT| captures all API calls for the CLI as events, including calls from code calls to the CLI APIs. If you create a trail, you can enable continuous delivery of |CT| events to an |S3| bucket, including events for the CLI. If you don't configure a trail, you can still view the most recent events in the |CT| console in :guilabel:`Event history`.  Using the information collected by |CT|, you can determine the request that was made to the CLI, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about |CT|, see the `AWS CloudTrail User Guide <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html>`__.

 .. service-name-info-in-cloudtrail.

AWS Mobile CLI Information in CloudTrail
========================================

|CT| is enabled on your AWS account when you create the account. When activity occurs in AWS Mobile CLI, that activity is recorded in a |CT| event along with other AWS service events in :guilabel:`Event history`. You can view, search, and download recent events in your AWS account. For more information, see `Viewing Events with CloudTrail Event History <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html>`__.

For an ongoing record of events in your AWS account, including events for AWS Mobile CLI, create a trail. A trail enables |CT| to deliver log files to an |S3| bucket. By default, when you create a trail in the console, the trail applies to all regions. The trail logs events from all regions in the AWS partition and delivers the log files to the |S3| bucket that you specify.  Additionally, you can configure other AWS services to further analyze and act upon the event data collected in |CT| logs. For more information, see:

  * `Overview for Creating a Trail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html>`__

  * `CloudTrail Supported Services and Integrations <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations>`__

  * `Configuring Amazon SNS Notifications for CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html>`__

  * `Receiving CloudTrail Log Files from Multiple Regions <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html>`__ and `Receiving CloudTrail Log Files from Multiple Accounts <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html>`__


.. ACTIONS you list in this paragraph should be 1 or more examples that a user of your service's API will be familiar with. In the following section, describe the logging results for each example you give.

All AWS Mobile CLI actions are logged by |CT| and are documented in the :ref:`AWS Mobile CLI  API Reference <aws-mobile-cli-reference>`. For example, calls to the :code:`awsmobile init`, :code:`awsmobile pull` and :code:`awsmobile push` generate entries in the |CT| log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:

  * Whether the request was made with root or |IAMlong| (|IAM|) user credentials.

  * Whether the request was made with temporary security credentials for a role or federated user.

  * Whether the request was made by another AWS service.

For more information, see the `CloudTrail userIdentity Element <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html>`__.

.. _understanding-YOUR_SERVICE_NAME-entries:

Understanding AWS Mobile ClI Log File Entries
=============================================

A trail is a configuration that enables delivery of events as log files to an |S3| bucket that you specify. |CT| log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. |CT| log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order.

The following example shows a |CT| log entry that demonstrates the :code:`ListProjects` action.

.. code-block:: json

    {
        "eventVersion": "1.05",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "ABCDEFGHIJK0123456789",
            "arn": "arn:aws:iam::012345678901:user/Administrator",
            "accountId": "012345678901",
            "accessKeyId": "ABCDEFGHIJK0123456789",
            "userName": "YOUR_ADMIN_USER_NAME"
        },
        "eventTime": "2017-12-18T23:10:13Z",
        "eventSource": "mobilehub.amazonaws.com",
        "eventName": "ListProjects",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "111.111.111.111",
        "userAgent": "aws-cli/1.11.140 Python/2.7.13 Darwin/15.6.0 botocore/1.6.7 ",
        "requestParameters": {
            "maxResults": 0
        },
        "responseElements": {
            "projects": [{
                "name": "YOUR_PROJECT_NAME-0123456789012",
                "projectId": "abcd0123-0123-0123-0123-abcdef012345"
            }]
        },
        "requestID": "abcd0123-0123-0123-0123-abcdef012345",
        "eventID": "abcd0123-0123-0123-0123-abcdef012345",
        "eventType": "AwsApiCall",
        "recipientAccountId": "012345678901"
    }


