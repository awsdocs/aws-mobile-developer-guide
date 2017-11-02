.. _auth-google-create-oauth-android-clientid:

###################################
Create an OAuth Android Client ID
###################################

To enable Google Sign-In for your Android app, create an Android OAuth client
ID in the Google Developers Console. This enables your app that can access Google APIs directly and manage token lifecycle through |COG| Identity. This Android OAuth client ID is in addition to the
Web application OAuth client ID you created when following steps to :ref:`auth-google-create-google-project`. You will provide this client ID to |AMH| during the Google
Sign-In configuration.


To create an OAuth Android client ID
====================================


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


#. Choose :guilabel:`New credentials` and then choose :guilabel:`OAuth client ID`.

   .. image:: images/new-credentials.png
      :scale: 100
      :alt: Creating new OAuth client ID credentials in the Google Developers Console

   .. only:: pdf

      .. image:: images/new-credentials.png
         :scale: 65

   .. only:: kindle

      .. image:: images/new-credentials.png
         :scale: 85


#. In :guilabel:`Create client ID`, choose :guilabel:`Android`.

   .. image:: images/create-client-id.png
      :scale: 100
      :alt: Creating an Android client ID in the Google Developers Console

   .. only:: pdf

      .. image:: images/create-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/create-client-id.png
         :scale: 85


#. In :guilabel:`Name`, enter a name in the format :code:`com.amazon.mysampleapp Android client ID`.

#. In :guilabel:`Signing-certificate fingerprint`, enter the SHA-1 fingerprint. For more information
   about Google's process for obtaining your SHA-1 fingerprint, see `this Google support article
   <https://support.google.com/cloud/answer/6158849?hl=en#android>`_.

   .. image:: images/create-android-client-id.png
      :scale: 100
      :alt: Entering the SHA-1 fingerprint for an app in the Google Developers Console

   .. only:: pdf

      .. image:: images/create-android-client-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/create-android-client-id.png
         :scale: 85


#. Use your your SHA-1 fingerprint to ensure that your apps APK are associated with your Google app.
   See instructions at `Generate a key and keystore
   <https://developer.android.com/studio/publish/app-signing.html#generate-key>`_.

#. In :guilabel:`Package name`, enter the package name in the format
   :code:`com.amazon.YOUR-PACKAGE-NAME`.

#. Choose :guilabel:`Create`.

#. In the :guilabel:`OAuth client` pop-up, copy and save the value generated for your Android client
   ID. You will need this client ID to implement Google Sign-In in your |AMH| app. After you copy
   the client ID, choose :guilabel:`OK`.

   .. image:: images/android-oauth-id.png
      :scale: 100
      :alt: Displaying the generated Android client ID in the Google Developers Console

   .. only:: pdf

      .. image:: images/android-oauth-id.png
         :scale: 65

   .. only:: kindle

      .. image:: images/android-oauth-id.png
         :scale: 85


#. Paste the Android client ID value into the |AMH| :guilabel:`Google Android Client ID` field for
   your project.

   .. image:: images/google-client-id-console-entry.png
      :scale: 100
      :alt: Where to paste the Android client ID value from Google into the |AMH| console

   .. only:: pdf

      .. image:: images/google-client-id-console-entry.png
         :scale: 65

   .. only:: kindle

      .. image:: images/google-client-id-console-entry.png
         :scale: 85

