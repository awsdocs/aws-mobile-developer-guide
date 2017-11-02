.. _add-aws-mobile-user-sign-in:

###################################
Add User Sign-in to Your Mobile App
###################################


.. meta::
   :description: Integrating user sign-in

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    Add Email and Password Sign-in <add-aws-mobile-user-sign-in-email-and-password>

    Add Facebook Sign-in <add-aws-mobile-user-sign-in-facebook>

    Add Google Sign-in <add-aws-mobile-user-sign-in-google>

    Authentication-Setup


.. _add-aws-mobile-user-sign-in-overview:

Overview
========


Enable your users to sign in using credentials and a familiar experience from Facebook, Google, or
your own custom user directory. The AWS Mobile Hub :ref:`user-sign-in` feature provides the backend using the
`Amazon Cognito <http://docs.aws.amazon.com/cognito/latest/developerguide/>`_, and the SDK provides the sign-in UI for the identity provider(s) you
configure.


.. _add-aws-mobile-user-sign-in-backend-setup:

Backend Setup for |AMH| User Sign-in
====================================


#. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the integration
   steps on this page.

#. Use AWS Mobile Hub to deploy your backend services.


   #. Sign in to the `AWS Mobile Hub console <https://console.aws.amazon.com/mobilehub>`_

   #. Choose :guilabel:`Create a new project`, type a name for it, and then choose :guilabel:`Create
      project`.

      Or select an existing project.

   #. Choose the :guilabel:`User Sign-in` tile to enable the feature.

#. Choose and configure the sign-in provider(s) you need.

    :ref:`Email and Password Sign-in <add-aws-mobile-user-sign-in-email-and-password>` - Users sign in to your own secure user directory with login rules you define.

    :ref:`Facebook Sign-in <add-aws-mobile-user-sign-in-Facebook>` - Users sign in to your AWS Mobile-backed app using their Facebook login credentials.

    :ref:`Google Sign-in <add-aws-mobile-user-sign-in-google>` - Users sign in to your AWS Mobile-backed app using their Google login credentials.




