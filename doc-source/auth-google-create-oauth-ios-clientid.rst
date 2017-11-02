.. _auth-google-create-oauth-ios-clientid:

###############################
Create an OAuth iOS Client ID
###############################


To enable Google Sign-In for your iOS app, create an iOS OAuth client ID in the Google Developers Console. This enables your app to access Google APIs directly and to manage token lifecycle through |COG| Identity. This iOS OAuth client ID is in addition to the web application OAuth client ID that you created when following steps to :ref:`auth-google-create-google-project`. You will provide this client ID to |AMH| during the Google Sign-In
configuration.


To create an OAuth iOS client ID
================================


#. Go to the Google Developers Console at https://console.developers.google.com.

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


#. In the API Manager, choose :guilabel:`Credentials` in the left side menu.

   .. image:: images/api-credentials.png
      :scale: 100
      :alt: Choosing Credentials from the API Manager in the Google Developers Console

   .. only:: pdf

      .. image:: images/api-credentials.png
         :scale: 65

   .. only:: kindle

      .. image:: images/api-credentials.png
         :scale: 85


#. Choose :guilabel:`New Credentials` and then choose :guilabel:`OAuth client ID`.

   .. image:: images/new-credentials.png
      :scale: 100
      :alt: Creating new OAuth client ID credentials in the Google Developers Console

   .. only:: pdf

      .. image:: images/new-credentials.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-credentials.png
         :scale: 85


#. In :guilabel:`Create client ID`, choose :guilabel:`iOS`.

   .. image:: images/create-client-id.png
      :scale: 100
      :alt: Creating an iOS client ID in the Google Developers Console

   .. only:: pdf

      .. image:: images/create-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/create-client-id.png
         :scale: 85


#. In :guilabel:`Name`, enter a name in the format :code:`com.amazon.YOUR-APP-NAME YOUR-iOS-CLIENT-ID`.

#. In :guilabel:`Bundle ID`, enter the bundle name in the format :code:`com.amazon.YOUR-APP-NAME`.

   .. image:: images/ios-oauth-id.png
      :scale: 100
      :alt: Entering the bundle ID for an iOS app in the Google Developers Console

   .. only:: pdf

      .. image:: images/ios-oauth-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/ios-oauth-id.png
         :scale: 85


#. Choose :guilabel:`Create`.

#. In the :guilabel:`OAuth client` pop-up, copy and save the value that was generated for your iOS
   client ID. You will need these values to implement Google Sign-In in your |AMH| app. After you
   copy the client ID, choose :guilabel:`OK`.

   .. image:: images/android-oauth-id.png
      :scale: 100
      :alt: Displaying the generated client ID in the Google Developers Console

   .. only:: pdf

      .. image:: images/android-oauth-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/android-oauth-id.png
         :scale: 85


#. Paste the iOS client ID value into the |AMH| :guilabel:`Google iOS Client ID` field for your
   project.

   .. image:: images/google-client-id-console-entry.png
      :scale: 100
      :alt: Where to paste the iOS client ID value from Google into the |AMH| console

   .. only:: pdf

      .. image:: images/google-client-id-console-entry.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google-client-id-console-entry.png
         :scale: 85




