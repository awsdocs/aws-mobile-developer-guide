.. _auth-setup:

##############################
Setting Up User Authentication
##############################


.. meta::
   :description: Learn how to set up external authentication services for |AMH|.




With |AMHlong|, you can enable a user sign-in feature for your app. User sign-in works with various
user authentication services, including Facebook, Google, and custom authentication. |AMH| helps you
to configure sign-in with Facebook, Google, or your own identity system; however, you may also need
to set up user authentication with the different authentication services you plan to use.

Learn more about how Amazon Cognito performs authentication using external identity providers, see
`Amazon Cognito External Identity Providers
<http://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html>`_.

The topics in this section detail the setup you must complete with various user authentication
services and how to obtain the data values |AMH| needs to configure your sign-in feature.


.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    auth-facebook-setup
    auth-google-setup
    auth-custom-setup
