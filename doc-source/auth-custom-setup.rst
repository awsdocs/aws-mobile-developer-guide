.. _auth-custom-setup:

################################
Setting Up Custom Authentication
################################


.. meta::
   :description: Learn about using custom authentication in |AMH|.


You can use your own authentication system, rather than identity federation provided by Facebook or
Google, to register and authenticate your customers. The use of developer-authenticated identities
involves interaction between the end-user device, your authentication back end, and |COG|. For more
information, see the following blog entries:


* `Understanding Amazon Cognito Authentication
  <http://mobile.awsblog.com/post/Tx2UQN4KWI6GDJL/Understanding-Amazon-Cognito-Authentication>`_

* `Understanding Amazon Cognito Authentication Part 2: Developer-Authenticated Identities
  <http://mobile.awsblog.com/post/Tx2FL1QAPDE0UAH/Understanding-Amazon-Cognito-Authentication-Part-2-Developer-Authenticated-Ident>`_



To use your own authentication system, you must implement an identity provider by extending the
:code:`AWSAbstractCognitoIdentityProvider` class and associating your provider with an |COG|
identity pool. For more information, see `Developer Authenticated Identities
<http://docs.aws.amazon.com/cognito/devguide/identity/developer-authenticated-identities/>`_ in the
|COG| Developer Guide.



