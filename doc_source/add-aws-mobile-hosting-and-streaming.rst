.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-hosting-and-streaming:

############################################################################
Add Hosting and Streaming to Your Mobile App Amazon S3 and Amazon CloudFront
############################################################################


.. meta::
   :description: Integrating hosting and streaming


.. _add-aws-mobile-hosting-and-streaming-overview:

Hosting and Streaming
=====================


The Hosting and Streaming feature enables you to host code and content in the cloud for your web,
native mobile, or hybrid app. A simple sample web app that accesses AWS services is deployed when you
enable this feature.

|AMH| creates a container for your content using an `Amazon S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/>`__ bucket. The content is available publicly on the Internet and you can preview the content directly using a testing URL.

Your content is automatically distributed to a global content delivery network (CDN). `Amazon
CloudFront <https://aws.amazon.com/cloudfront/>`__ also supports media file streaming. To learn more, see `CloudFront Streaming Tutorials <http://docs.aws.amazon.com/mobile-hub/latest/developerguide/url-cf-dev;Tutorials.html>`__.


.. _add-aws-mobile-hosting-and-streaming-back-end-setup:

Set Up Your Backend
===================


.. container:: option

   Android - Java
      #. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the integration steps on this page.

      #. Use |AMHlong| to deploy your backend in minutes.


         #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.

         #. Choose :guilabel:`Create a new project`, type a name for it, and then choose
            :guilabel:`Create project`.

            Or select an existing project.

         #. Choose the :guilabel:`Hosting and Streaming` tile.


            #. Choose the :ref:`hosting-and-streaming` feature.

               .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                  :scale: 100
                  :alt: Image of choosing Hosting and Streaming in the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 75

            #. Check the box to indicate you understand that content hosted by the feature is
               public, and then choose :guilabel:`Enable`.


               .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                  :scale: 100
                  :alt: Image of the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 75

         #. Download your |AMH| project configuration file.

               #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

               #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

                  .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
                     :scale: 100 %
                     :alt: Image of the Mobile Hub console when choosing Download Configuration File.

                  .. only:: pdf

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                        :scale: 50

                  .. only:: kindle

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                        :scale: 75

                  *Remember:*

                  Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use updated files for those features.

   Android - Kotlin
      #. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the integration steps on this page.

      #. Use |AMHlong| to deploy your backend in minutes.


         #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.

         #. Choose :guilabel:`Create a new project`, type a name for it, and then choose
            :guilabel:`Create project`.

            Or select an existing project.

         #. Choose the :guilabel:`Hosting and Streaming` tile.


            #. Choose the :ref:`hosting-and-streaming` feature.

               .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                  :scale: 100
                  :alt: Image of choosing Hosting and Streaming in the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 75

            #. Check the box to indicate you understand that content hosted by the feature is
               public, and then choose :guilabel:`Enable`.


               .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                  :scale: 100
                  :alt: Image of the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 75

         #. Download your |AMH| project configuration file.

               #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

               #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

                  .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
                     :scale: 100 %
                     :alt: Image of the Mobile Hub console when choosing Download Configuration File.

                  .. only:: pdf

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                        :scale: 50

                  .. only:: kindle

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                        :scale: 75

                  *Remember:*

                  Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use updated files for those features.

   iOS - Swift
      #. Complete the :ref:`add-aws-mobile-sdk-basic-setup` steps before using the integration steps on this page.

      #. Deploy your AWS services in minutes using |AMHlong|.


         #. Sign in to the `Mobile Hub console <https://console.aws.amazon.com/mobilehub/home/>`__.

         #. Choose :guilabel:`Create a new project`, type a name for it, and then choose
            :guilabel:`Create project`.

            Or select an existing project.

         #. Choose the :guilabel:`Hosting and Streaming` tile.


            #. Choose the :ref:`hosting-and-streaming` feature.

               .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                  :scale: 100
                  :alt: Image of the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming.png
                     :scale: 75

            #. Check the box to indicate you understand that content hosted by the feature is
               public, and then choose :guilabel:`Enable`.


               .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                  :scale: 100
                  :alt: Image of the |AMH| console.

               .. only:: pdf

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 50

               .. only:: kindle

                  .. image:: images/add-aws-mobile-add-hosting-and-streaming-enable.png
                     :scale: 75

         #. Download your |AMH| project configuration file.

               #. In the |AMH| console, choose your project, and then choose the :guilabel:`Integrate` icon on the left.

               #. Choose :guilabel:`Download Configuration File` to get the :file:`awsconfiguration.json` file that connects your app to your backend.

                  .. image:: images/add-aws-mobile-sdk-download-configuration-file.png
                     :scale: 100 %
                     :alt: Image of the Mobile Hub console when choosing Download Configuration File.

                  .. only:: pdf

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                       :scale: 50

                  .. only:: kindle

                     .. image:: images/add-aws-mobile-sdk-download-nosql-cloud-logic.png
                       :scale: 75

                  *Remember:*

                  Each time you change the |AMH| project for your app, download and use an updated :file:`awsconfiguration.json` to reflect those changes in your app. If NoSQL Database or Cloud Logic are changed, also download and use updated files for those features.


      **About the Hosting and Streaming Sample App**

      .. note::

         When you enable Hosting and Streaming, |AMH| provisions content in the root of your
         source bucket which includes a local copy of the |JSBlong|
         (:file:`aws-min.js`).


         * :file:`aws-sdk.min.js` - An |JSBlong| source file.

         * :file:`aws-config.js,`- A web app configuration file that is generated to contain
           constants for the endpoints for each |AMH| feature you have enabled for this
           project.

         * `index.html` - Which uses a constant formed in :file:`aws-config.js` to request and
           display an AWS guest (unauthenticated) user identity ID from the |COG| service.

         When you enable Hosting and Streaming an |CFlong| global content delivery network (CDN)
         distribution is created and associated with your bucket. When |AMH| propagates the sample
         web app content to the bucket, the content is then propagated to the CDN and becomes
         available from local endpoints around the globe. If you configure `CloudFront streaming
         <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Tutorials.html>`__, then media content you upload to your |S3| bucket can be streamed from
         those endpoints.



.. _add-aws-mobile-hosting-and-streaming-app:

Add |AMH| Hosting and Streaming to Your App
===========================================


Use the following steps to add |AMH| Hosting and Streaming to your app.

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml
               :emphasize-lines: 0

                <uses-permission android:name="android.permission.INTERNET" />
                <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
                <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

         #. :file:`app/build.gradle` must contain:

            .. code-block:: none
               :emphasize-lines: 2

                dependencies{
                    implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                }

      #. Add the backend service configuration file to your app.

         In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of creating a raw directory in Android Studio.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         #. From the location where configuration files were downloaded in a previous step, drag
            :file:`awsconfiguration.json` into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

   Android - Kotlin
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. :file:`AndroidManifest.xml` must contain:

            .. code-block:: xml
               :emphasize-lines: 0

                <uses-permission android:name="android.permission.INTERNET" />
                <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
                <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

         #. :file:`app/build.gradle` must contain:

            .. code-block:: none
               :emphasize-lines: 2

                dependencies{
                    implementation 'com.amazonaws:aws-android-sdk-s3:2.6.+'
                }

      #. Add the backend service configuration file to your app.

         In the Android Studio Project Navigator, right-click your app's :file:`res` folder, and then choose :guilabel:`New > Directory`. Type :userinput:`raw` as the directory name and then choose :guilabel:`OK`.

            .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
               :scale: 100
               :alt: Image of creating a raw directory in Android Studio.

            .. only:: pdf

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 50

            .. only:: kindle

               .. image:: images/add-aws-mobile-sdk-android-studio-res-raw.png
                  :scale: 75

         #. From the location where configuration files were downloaded in a previous step, drag
            :file:`awsconfiguration.json` into the :file:`res/raw` folder. Android gives a resource ID to any arbitrary file placed in this folder, making it easy to reference in the app.

   iOS - Swift
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

                platform :ios, '9.0'

                target :'YOUR-APP-NAME' do
                  use_frameworks!

                      pod 'AWSS3', '~> 2.6.13'    # For file transfers
                      pod 'AWSCognito', '~> 2.6.13'    #For data sync
                      # other pods

                end

            Run :code:`pod install --repo-update` before you continue.

            If you encounter an error message that begins ":code:`[!] Failed to connect to GitHub to update the CocoaPods/Specs . . .`", and your internet connectivity is working, you may need to `update openssl and Ruby <https://stackoverflow.com/questions/38993527/cocoapods-failed-to-connect-to-github-to-update-the-cocoapods-specs-specs-repo/48962041#48962041>`__.

         #. Classes that call |S3| APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSS3

      #. Add your backend service configuration to the app.

         From the location where your |AMH| configuration file was downloaded in a previous step,
         drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file
         in your Xcode project.

         Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.







