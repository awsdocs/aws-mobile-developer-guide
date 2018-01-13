.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _add-aws-mobile-conversational-bots:

##########################################################
Add Conversational Bots to Your Mobile App with Amazon Lex
##########################################################


.. meta::
   :description:
       Add |AMH| Conversational Bots to Your Mobile App

.. _conversational-bots-overview:

Overview
==============

Add the natural language understanding that powers Amazon Alexa to your mobile app. The |AMH|
:ref:`conversational-bots` feature provides ready-made bot templates using the `Amazon Lex service
<http://docs.aws.amazon.com/lex/latest/dg/>`_.


.. _setup-your-backend:

Set Up Your Backend
===================

#. Complete the :ref:`Get Started <add-aws-mobile-sdk-basic-setup>` steps before your proceed.

#. Enable :guilabel:`Conversational Bots`: Open your project in `Mobile Hub <https://console.aws.amazon.com/mobilehub>`_ and choose the :guilabel:`Conversational Bots` tile to enable the feature.

   #. Choose one of the sample Bots or import one that you have created in the `Amazon Lex console
      <http://docs.aws.amazon.com/lex/latest/dg/what-is.html>`_.

#. When the operation is complete, an alert will pop up saying "Your Backend has been updated", prompting you to download the latest copy of the cloud configuration file. If you're done configuring the feature, choose the banner to return to the project details page.

   .. image:: images/updated-cloud-config.png

#. From the project detail page, every app that needs to be updated with the latest cloud configuration file will have a flashing :guilabel:`Integrate` button. Choose the button to enter the integrate wizard.

   .. image:: images/updated-cloud-config2.png
      :scale: 25

#. Update your app with the latest copy of the cloud configuration file. Your app now references the latest version of your backend. Choose Next and follow the Cloud API documentation below to connect to your backend.

.. _add-aws-mobile-conversational-bots-app:

Connect to your backend
=======================

**To add AWS Mobile Conversational Bots to your app**

.. container:: option

   Android - Java
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.

         #. Add the following permissions to your :file:`AndroidManifest.xml`:

            .. code-block:: xml
               :emphasize-lines: 1-2

                <uses-permission android:name="android.permission.RECORD_AUDIO" />
                <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

         #. Add the following to your :file:`app/build.gradle`:

            .. code-block:: none
               :emphasize-lines: 2

                dependencies{
                    compile ('com.amazonaws:aws-android-sdk-lex:2.6.+@aar') {transitive = true;}
                }

         #. For each Activity where you make calls to |LEXlong|, import the following APIs.

            .. code-block:: none
               :emphasize-lines: 1-3

                import com.amazonaws.mobileconnectors.lex.interactionkit.Response;
                import com.amazonaws.mobileconnectors.lex.interactionkit.config.InteractionConfig;
                import com.amazonaws.mobileconnectors.lex.interactionkit.ui.InteractiveVoiceView;

      #. Add a voice button to an activity or fragment layout

         #. Add a :code:`voice_component` to your layout file.

            .. code-block:: xml
               :emphasize-lines: 1-5

                <com.amazonaws.mobileconnectors.lex.interactionkit.ui.InteractiveVoiceView
                android:id="@+id/voiceInterface"
                layout="@layout/voice_component"
                android:layout_width="200dp"
                android:layout_height="200dp"/>

         #. In your :file:`strings.xml` file add the region for your bot. :emphasis:`Note: Currently bots are
            only supported in US Virginia East (us-east-1).`

            .. code-block:: xml
               :emphasize-lines: 1

                <string name="aws_region">us-east-1</string>

         #. Initialize the voice button

            In the :code:`onCreate()` of the activity where your Bot will be used, call
            :code:`init()`.

            .. code-block:: java
               :emphasize-lines: 1-39

                public void init(){
                        InteractiveVoiceView voiceView =
                            (InteractiveVoiceView) findViewById(R.id.voiceInterface);

                        voiceView.setInteractiveVoiceListener(
                            new InteractiveVoiceView.InteractiveVoiceListener() {

                            @Override
                            public void dialogReadyForFulfillment(Map slots, String intent) {
                                Log.d(TAG, String.format(
                                        Locale.US,
                                        "Dialog ready for fulfillment:\n\tIntent: %s\n\tSlots: %s",
                                        intent,
                                        slots.toString()));
                            }

                            @Override
                            public void onResponse(Response response) {
                                Log.d(TAG, "Bot response: " + response.getTextResponse());
                            }

                            @Override
                            public void onError(String responseText, Exception e) {
                                Log.e(TAG, "Error: " + responseText, e);
                            }
                        });

                        voiceView.getViewAdapter().setCredentialProvider(AWSMobileClient.getInstance().getCredentialsProvider());

                        //replace parameters with your botname, bot-alias
                        voiceView.getViewAdapter()
                                 .setInteractionConfig(
                                      new InteractionConfig("YOUR-BOT-NAME","$LATEST"));

                        voiceView.getViewAdapter()
                                 .setAwsRegion(getApplicationContext()
                                 .getString(R.string.aws_region));
                    }


   iOS - Swift
      #. Set up AWS Mobile SDK components with the following :ref:`add-aws-mobile-sdk-basic-setup` steps.


         #. :file:`Podfile` that you configure to install the AWS Mobile SDK must contain:

            .. code-block:: none

               platform :ios, '9.0'

                target :'YOUR-APP-NAME`' do
                  use_frameworks!

                     pod 'AWSLex', '~> 2.6.6'
                     # other pods

               end

            Run :code:`pod install --repo-update` before you continue.

         #. Classes that call |LEXlong| APIs must use the following import statements:

            .. code-block:: none

                import AWSCore
                import AWSLex

      #. Add permissions to your :file:`info.plist` that allow the app to use the  microphone of a device.

         .. code-block:: xml

             <plist version = "1.0"></plist>
                <dict>
                   <!-- . . . -->
                   <key>NSMicrophoneUsageDescription</key>
                   <string>For demonstration of conversational bots</string>
                   <!-- . . . -->
                </dict>

      #. Add your backend service configuration to the app.

         From the location where your |AMH| configuration file was downloaded in a previous step,
         drag :file:`awsconfiguration.json` into the folder containing your :file:`info.plist` file
         in your Xcode project.

         Select :guilabel:`Copy items if needed` and :guilabel:`Create groups`, if these options are offered.

      #. Add a voice button UI element that will let your users speak to Amazon Lex to an activity.


         #. Create a :code:`UIView` in a storyboard or :file:`xib` file.

         #. Map the :code:`UIView` to the :code:`AWSLexVoiceButton` class of the AWS Mobile SDK.

         #. Link the :code:`UIView` to your :code:`ViewController`.


         .. image:: images/aws-mobile-xcode-lex-voice-button.png
            :scale: 100
            :alt: Image of creating a button and mapping it to the AWS Mobile SDK in Xcode.

         .. only:: pdf

            .. image:: images/aws-mobile-xcode-lex-voice-button.png
               :scale: 50

         .. only:: kindle

            .. image:: images/aws-mobile-xcode-lex-voice-button.png
               :scale: 75

      #. Register the voice button.

         The following code shows how use the :code:`viewDidLoad` method of your View Controller to
         enable your voice button to respond to |LEXlong| success and error messages The code conforms the
         class to :code:`AWSLexVoiceButtonDelegate`. It initializes the button by binding it to the
         bot you configured in your |AMH| project, and registers the button as the
         :code:`AWSLexVoiceButtonKey` of your |LEXlong| voice interaction client.

         .. code-block:: swift

             import UIKit
             import AWSLex
             import AWSAuthCore

             class VoiceChatViewController: UIViewController, AWSLexVoiceButtonDelegate {
               override func viewDidLoad() {

                     // Set the bot configuration details
                     // You can use the configuration constants defined in AWSConfiguration.swift file
                     let botName = "YOUR-BOT-NAME"
                     let botRegion: AWSRegionType = "YOUR-BOT-REGION"
                     let botAlias = "$LATEST"

                     // set up the configuration for AWS Voice Button
                     let configuration = AWSServiceConfiguration(region: botRegion, credentialsProvider: AWSMobileClient.sharedInstance().getCredentialsProvider())
                     let botConfig = AWSLexInteractionKitConfig.defaultInteractionKitConfig(withBotName: YOUR-BOT-NAME, botAlias: :YOUR-BOT-ALIAS)

                     // register the interaction kit client for the voice button using the AWSLexVoiceButtonKey constant defined in SDK
                     AWSLexInteractionKit.register(with: configuration!, interactionKitConfiguration: botConfig, forKey: AWSLexVoiceButtonKey)
                     super.viewDidLoad()
                     (self.voiceButton as AWSLexVoiceButton).delegate = self
                 }
             }

      #. Handle |LEXlong| success and error messages by adding the following delegate methods for the Voice Button in your View Controller.

         .. code-block:: swift

             func voiceButton(_ button: AWSLexVoiceButton, on response: AWSLexVoiceButtonResponse) {
                 // handle response from the voice button here
                 print("on text output \(response.outputText)")
             }

             func voiceButton(_ button: AWSLexVoiceButton, onError error: Error) {
                 // handle error response from the voice button here
                 print("error \(error)")
             }




