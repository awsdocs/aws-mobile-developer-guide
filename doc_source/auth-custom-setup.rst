.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

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
  <http://mobile.awsblog.com/post/Tx2UQN4KWI6GDJL/Understanding-Amazon-Cognito-Authentication>`__

* `Understanding Amazon Cognito Authentication Part 2: Developer-Authenticated Identities
  <http://mobile.awsblog.com/post/Tx2FL1QAPDE0UAH/Understanding-Amazon-Cognito-Authentication-Part-2-Developer-Authenticated-Ident>`__



To use your own authentication system, you must implement an identity provider by extending the
:code:`AWSAbstractCognitoIdentityProvider` class and associating your provider with an |COG|
identity pool. For more information, see `Developer Authenticated Identities
<http://docs.aws.amazon.com/cognito/devguide/identity/developer-authenticated-identities/>`__ in the
|COG| Developer Guide.



