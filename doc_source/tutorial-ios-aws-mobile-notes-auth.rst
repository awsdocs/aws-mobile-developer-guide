.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _tutorial-ios-aws-mobile-notes-auth:

###################################
Add Authentication to the Notes App
###################################

In the :ref:`previous section <tutorial-ios-aws-mobile-notes-analytics>` of this tutorial, we created a mobile backend project using the AWS Amplify CLI, then added analytics to the sample note-taking app. This section assumes you have completed those steps. If you jumped to this step, please go back and :ref:`start from
the beginning <tutorial-ios-aws-mobile-notes-setup>`. In this tutorial, we will configure a sign-up / sign-in flow in our mobile backend. We will then add a new authentication activity to our note-taking app.

You should be able to complete this section of the tutorial in 20-30 minutes.

Set Up Your Backend
------------------

Before we work on the client-side code, we need to add User Sign-in to
the backend project.  These steps assume you have already completed the :ref:`analytics <tutorial-ios-aws-mobile-notes-analytics>` portion of this tutorial.

1. In a terminal window, enter the following commands to add User Sign-in to the backend project:

   .. code-block:: bash

      $ amplify auth update

   When prompted, use the default configuration.

2. Deploy your new resources with the following command:

   .. code-block:: bash

      $ amplify push

The :code:`amplify auth update` command updates the existing Amazon Cognito user pool configured for analytics, allowing for username and password authentication with email verification of the sign-up and forgot password flows.  You can adjust this to include multi-factor authentication, TOTP, phone number sign-up and more.

Add Auth Dependencies
---------------------

#. Add the following Auth dependencies in your project's :file:`Podfile`

   .. code-block:: bash

      platform :ios, '9.0'
      target :'MyNotes' do
          use_frameworks!

            # Analytics dependency
            pod 'AWSPinpoint'

            # Auth dependencies
            pod 'AWSUserPoolsSignIn'
            pod 'AWSAuthUI'
            pod 'AWSMobileClient'

          # other pods
      end

   Then, in a terminal run:

   .. code-block:: bash

      $ pod install

   If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.


Create an AWSMobileClient and Initialize the SDK
------------------------------------------------

Import :code:`AWSMobileClient` and add the following function into the :file:`AppDelegate.swift` class. This will create an instance of :code:`AWSMobileClient`.

.. code-block:: swift

   import UIKit
   import CoreData

   // Anaytics imports
   import AWSCore
   import AWSPinpoint

   // Auth imports
   import AWSMobileClient

   @UIApplicationMain
   class AppDelegate: UIResponder, UIApplicationDelegate {

       // . . .

       //Instantiate the AWSMobileClient
       func application(_ application: UIApplication, open url: URL,
           sourceApplication: String?, annotation: Any) -> Bool {

           return AWSMobileClient.sharedInstance().interceptApplication(
               application, open: url,
               sourceApplication: sourceApplication,
               annotation: annotation)
       }

       // . . .
   }

In the :code:`didFinishLaunching` function of the :file:`AppDelegate.swift` class, add :code:`AWSMobileClient` to register your user pool as the identity provider that enables users to access your app's AWS resources.

.. code-block:: swift

   func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions:
        [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

        // . . .

        // Initialize AWSMobileClient
        let didFinishLaunching = AWSMobileClient.sharedInstance().interceptApplication(
            application, didFinishLaunchingWithOptions:
            launchOptions)

        // Initialize Pinpoint to enable session analytics
        pinpoint = AWSPinpoint(configuration:
            AWSPinpointConfiguration.defaultPinpointConfiguration(
                launchOptions: launchOptions))

        return didFinishLaunching
   }

.. list-table::
   :widths: 1 6

   * - What did this do?

     - This will register your sign in providers and fetch the user pool you created and fetch an identity that enables a user to access your app's AWS resources. In this case, the provider is an `Amazon Cognito user pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__, but federating Facebook, Google, SAML and other identity providers is also supported.


Implement Your Sign-in UI
-------------------------

The AWS Mobile SDK provides a library that creates a customizable sign-in UI in your app. To create your sign-in UI, add the following imports and then call the library in the :code:`viewDidLoad()` function of :file:`MasterViewController.swift`
.

.. code-block:: swift

   import UIKit
   import CoreData
   import Foundation
   import AWSAuthCore
   import AWSAuthUI

   class MasterViewController: UITableViewController, NSFetchedResultsControllerDelegate {

        // . . .

        override func viewDidLoad() {
            super.viewDidLoad()

            // Instantiate sign-in UI from the SDK library
            if !AWSSignInManager.sharedInstance().isLoggedIn {
                AWSAuthUIViewController
                    .presentViewController(with: self.navigationController!,
                        configuration: nil,
                        completionHandler: { (provider: AWSSignInProvider, error: Error?) in
                        if error != nil {
                            print("Error occurred: \(String(describing: error))")
                        } else {
                            // Sign in successful.
                        }
                })
            }
            // . . .
        }
    }

Run the App and Validate Results
--------------------------------

Build and run the project in a simulator. You should see a sign-in
screen upon launch. Choose the :guilabel:`Create new account` button to create a new account.
Once the information is submitted, you will be sent a confirmation code
via email. Enter the confirmation code to complete registration, then
sign-in with your new account.

.. list-table::
   :widths: 1 6

   * - **Tip**

     - Use Amazon WorkMail as a test email account

       If you do not want to use your own email account as a test account, create an
       `Amazon WorkMail <https://aws.amazon.com/workmail/>`__ service within AWS for test accounts. You can get started for free with a 30-day trial for up to 25 accounts.

.. image:: images/tutorial-ios-notes-authentication-anim.gif
   :scale: 75
   :alt: Demo of Notes tutorial app with user sign-in added.


Next steps
----------

-  Learn more about `Amazon Cognito <https://aws.amazon.com/cognito/>`__.
