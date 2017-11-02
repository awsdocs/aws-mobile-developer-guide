.. _auth-google-create-google-project:

############################################################
Create a Google Developers Project and OAuth Web Client ID
############################################################

To enable Google Sign-In in your mobile or web app, create a project in the Google Developers
Console. If you are making versions of your mobile app for more than one platform
(iOS, Android, or web), create a single Google project to manage Google authentication for all of the platform instances.

For all platforms, enable the Google+ API for and an OAuth web client ID for your Google project. |COG| federates the web client ID to enable your app(s) to use Google authentication to grant access to your AWS resources.

To create a Google Developers project and OAuth web client ID
=============================================================


#. Go to the Google Developers Console at https://console.developers.google.com.

#. If you have not created a project yet, choose :guilabel:`Select a project` from the menu bar, and
   then choose :guilabel:`Create a project...`.

   .. image:: images/google_create_new_project.png
      :scale: 100
      :alt: Choosing Create a New Project in the Google Developers Console

   .. only:: pdf

      .. image:: images/google_create_new_project.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google_create_new_project.png
         :scale: 85


#. Complete the form that is displayed to create your new project.

#. In the :guilabel:`Dashboard` for your project, go to the :guilabel:`Use Google APIs` section and
   then choose :guilabel:`Enable and manage APIs`.

   .. image:: images/google_use_google_apis.png
      :scale: 100
      :alt: Choosing Enable and manage APIs for Google API in the Google Developers Console

   .. only:: pdf

      .. image:: images/google_use_google_apis.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google_use_google_apis.png
         :scale: 85


#. In the API Manager, in the :guilabel:`Social APIs` section, choose :guilabel:`Google+ API`.

   .. image:: images/api-manager-googleplus.png
      :scale: 100
      :alt: Choosing Google+ API to enable it in the Google Developers Console

   .. only:: pdf

      .. image:: images/api-manager-googleplus.png
         :scale: 65

   .. only:: kindle

      .. image:: images/api-manager-googleplus.png
         :scale: 85


#. In the :guilabel:`Overview` for Google+ API, choose :guilabel:`Enable API`.

   .. image:: images/google_enable_api.png
      :scale: 100
      :alt: Enabling the Google+ API for a new app in the Google Developers Console

   .. only:: pdf

      .. image:: images/google_enable_api.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google_enable_api.png
         :scale: 85


#. A message appears to inform you that the API is enabled but that it requires credentials before
   you can use it. Choose :guilabel:`Go to Credentials`.

   .. image:: images/go-to-credentials.png
      :scale: 100
      :alt: Adding Credentials to the enabled Google+ API in the Google Developers Console

   .. only:: pdf

      .. image:: images/go-to-credentials.png
         :scale: 65

   .. only:: kindle

      .. image:: images/go-to-credentials.png
         :scale: 85


#. Your |AMH| sample app authenticates users through |COG| Identity, so you need an OAuth web
   application client ID for |COG|. In :guilabel:`Credentials`, choose :guilabel:`client ID` from
   the links in the first step.

   .. image:: images/add-credentials.png
      :scale: 100
      :alt: Choosing to add client ID credentials for the Google+ API in the Google Developers Console

   .. only:: pdf

      .. image:: images/add-credentials.png
         :scale: 65

   .. only:: kindle

      .. image:: images/add-credentials.png
         :scale: 85


#. A message appears to inform you that you must set a product name. Choose :guilabel:`Configure
   consent screen`.

   .. image:: images/consent-screen-alert.png
      :scale: 100
      :alt: Configuring the consent screen for client ID credentials in the Google Developers Console

   .. only:: pdf

      .. image:: images/consent-screen-alert.png
         :scale: 65

   .. only:: kindle

      .. image:: images/consent-screen-alert.png
         :scale: 85

#. In :guilabel:`OAuth consent screen`, enter the name of your app in :guilabel:`Product name shown
   to users`. Leave the remaining fields blank. Then choose :guilabel:`Save`.

   .. image:: images/oauth-consent-screen.png
      :scale: 100
      :alt: Providing a name for a new app in the OAuth consent screen in the Google Developers Console

   .. only:: pdf

      .. image:: images/oauth-consent-screen.png
         :scale: 65

   .. only:: kindle

      .. image:: images/oauth-consent-screen.png
         :scale: 85


#. In :guilabel:`Create client ID`, choose :guilabel:`Web application`.

   .. image:: images/create-client-id.png
      :scale: 100
      :alt: Creating a client ID for a web application in the Google Developers Console

   .. only:: pdf

      .. image:: images/create-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/create-client-id.png
         :scale: 85


#. In :guilabel:`Name`, enter a name for the web client credentials for your app. Leave the
   :guilabel:`Authorized JavaScript origins` and :guilabel:`Authorized Redirect URIs` fields blank.
   |AMH| configures this information indirectly through |COG| Identity integration. Choose
   :guilabel:`Create`.

   .. image:: images/create-web-client-id.png
      :scale: 100
      :alt: Naming newly created web application credentials in the Google Developers Console

   .. only:: pdf

      .. image:: images/create-web-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/create-web-client-id.png
         :scale: 85


#. In the :guilabel:`OAuth client` pop-up, copy and save the value that was generated for your
   client ID. You will need the client ID to implement Google Sign-In in your |AMH| app. After you
   copy the client ID, choose :guilabel:`OK`.

   .. image:: images/oauth-client-id.png
      :scale: 100
      :alt: Displaying the generated client ID in the Google Developers Console

   .. only:: pdf

      .. image:: images/oauth-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/oauth-client-id.png
         :scale: 85


#. Paste the web application client ID value into the |AMH| :guilabel:`Google Web App Client ID`
   field for your project.

   .. image:: images/google-client-id-console-entry.png
      :scale: 100
      :alt: Where to paste the web application client ID value from Google into the |AMH| console

   .. only:: pdf

      .. image:: images/google-client-id-console-entry.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google-client-id-console-entry.png
         :scale: 85

