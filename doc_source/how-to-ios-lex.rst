.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. highlight:: java

.. _how-to-ios-lex:

#########################################
iOS: Use Natural Language with Amazon Lex
#########################################

.. .. list-table::
..    :widths: 1 6

..    * - **Just Getting Started?**

..      - :ref:`Use streamlined steps <add-aws-mobile-conversational-bots>` to install the SDK and integrate Amazon Lex.

.. *Or, use the contents of this page if your app will integrate existing AWS services.*



Overview
========

|LEX| is an AWS service for building voice and text conversational interfaces into applications. With |LEX|, the same natural language understanding engine that powers Amazon Alexa is now available to any
developer, enabling you to build sophisticated, natural language chatbots into your new and existing
applications.

The |sdk-ios| provides an optimized client for interacting with |LEX| runtime APIs,
which support both voice and text input and can return either voice or text. Included are features
like APIs to support detecting when a user finishes speaking and encoding incoming audio to the format
the Amazon Lex service prefers.

|LEX| has built-in integration with AWS Lambda to allow insertion of custom business logic
into your |LEX| processing flow, including all of the extension to other services that Lambda makes possible.

For information on |LEX| concepts and service configuration, see
`How it Works <http://docs.aws.amazon.com/lex/latest/dg/how-it-works.html>`__ in the Amazon Lex Developer Guide.

To get started using the Amazon Lex mobile client for iOS, you'll need to integrate the SDK for iOS
into your app, set the appropriate permissions, and import the necessary libraries.


Setting Up
==========

Include the SDK in Your Project
-------------------------------

Follow the instructions on the `Set Up the SDK for iOS <http://docs.aws.amazon.com/mobile/sdkforios/developerguide/setup.html>`__ page to include the frameworks for this service.

Set IAM Permissions for Amazon Lex
----------------------------------

To use |LEX| in an application, create a role and attach policies as described in Step 1 of
`Getting Started <http://docs.aws.amazon.com/lex/latest/dg/gs-bp-prep.html>`__ in the Amazon Lex Developer Guide.

To learn more about IAM policies, see `Using IAM <http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html>`__.

Configure a Bot
---------------

Use the `Amazon Lex console <https://console.aws.amazon.com/lex/>`__ console to configure a bot that interacts with your mobile app features. To learn more, see `Amazon Lex Developer Guide <https://docs.aws.amazon.com/lex/latest/dg/what-is.html>`__. For a quickstart, see `Getting Started <https://alpha-docs-aws.amazon.com/lex/latest/dg/getting-started.html>`__ .

|LEX| also supports model building APIs, which allow creation of bots, intents, and slots at runtime. This SDK does not currently offer additional support for interacting with |LEX| model building APIs.

Implement Text and Voice Interaction with Amazon Lex
====================================================

Add Permissions and Get Credentials
------------------------------------

Take the following steps to allow your app to access device resources and AWS services.

Add permission to use the microphone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add permission to use the microphone to enable users to speak to Amazon Lex through your app, open your project's :file:`Info.plist` file using :guilabel:`Right-click > Open As > Source Code`, and then add the following entry.

    .. code-block:: xml

        <plist version="1.0">
            . . .
            <dict>
                <key>NSMicrophoneUsageDescription</key>
                <string>For interaction with Amazon Lex</string>
            </dict>
             . . .
        </plist>


Integrating the Interaction Client
----------------------------------

Take the following steps to integrate the Amazon Lex interaction client with your app.

Initialize the `InteractionKit` for voice and text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following code using the name and alias of your Lex bot to initialize an  instance of `InteractionKit`.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let chatConfig = AWSLexInteractionKitConfig.defaultInteractionKitConfig(withBotName: BotName, botAlias: BotAlias)

                // interaction kit for the voice button
                AWSLexInteractionKit.register(with: configuration!, interactionKitConfiguration: chatConfig, forKey: "AWSLexVoiceButton")

                chatConfig.autoPlayback = false

                // interaction kit configuration for the client
                AWSLexInteractionKit.register(with: configuration!, interactionKitConfiguration: chatConfig, forKey: "chatConfig")

        Objective C
            .. code-block:: objectivec

                AWSLexInteractionKitConfig *chatConfig = [AWSLexInteractionKitConfig defaultInteractionKitConfigWithBotName:BotName botAlias:BotAlias];

                chatConfig.autoPlayback = NO;

                [AWSLexInteractionKit registerInteractionKitWithServiceConfiguration:configuration interactionKitConfiguration:chatConfig forKey:AWSLexChatConfigIdentifierKey];


Implement `InteractionKit` delegate methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Declare and implement the following methods in the class where you intend to use your `InteractionKit`:

- :code:`interactionKit` is called to begin a conversation. When passed :code:`interactionKit`, :code:`switchModeInput`, and :code:`completionSource`, the function should set the mode of interaction (audio or text input and output)  and pass the :code:`SwitchModeResponse` to the :code:`completionSource`. On error, the `interactionKit:onError` method is called.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                public func interactionKit(_ interactionKit: AWSLexInteractionKit, switchModeInput:
                  AWSLexSwitchModeInput, completionSource: AWSTaskCompletionSource<AWSLexSwitchModeResponse>?)

                public func interactionKit(_ interactionKit: AWSLexInteractionKit, onError error: Error)

        Objective C
            .. code-block:: objectivec

                - (void)interactionKit:(AWSLexInteractionKit *)interactionKit
                    switchModeInput:(AWSLexSwitchModeInput *)switchModeInput
                  completionSource:(AWSTaskCompletionSource<AWSLexSwitchModeResponse *> *)completionSource

                - (void)interactionKit:(AWSLexInteractionKit *)interactionKit
                  onError:(NSError *)error`

- :code:`interactionKitContinue` is called to continue an ongoing conversation with its transaction state and metadata maintained.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                func interactionKitContinue(withText interactionKit: AWSLexInteractionKit, completionSource: AWSTaskCompletionSource<NSString>){
                    textModeSwitchingCompletion = completionSource
                }

        Objective C
            .. code-block:: objectivec

                - (void)interactionKitContinueWithText:(AWSLexInteractionKit *)interactionKit
                    completionSource:(AWSTaskCompletionSource<NSString *> *)completionSource{
                 textModeSwitchingCompletion = completionSource;
                }

  Alternatively, you can explicitly set `SwitchModeResponse` to a selected mode.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                let switchModeResponse = AWSLexSwitchModeResponse()
                switchModeResponse.interactionMode = AWSLexInteractionMode.text
                switchModeResponse.sessionAttributes = switchModeInput.sessionAttributes
                completionSource?.setResult(switchModeResponse)

        Objective C
            .. code-block:: swift

                AWSLexSwitchModeResponse *switchModeResponse = [AWSLexSwitchModeResponse new];
                [switchModeResponse setInteractionMode:AWSLexInteractionModeText];
                [switchModeResponse setSessionAttributes:switchModeInput.sessionAttributes];
                [completionSource setResult:switchModeResponse];


Begin or Continue a Conversation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you call :code:`InteractionKit` to provide input for a conversation, check if the conversation is already in progress by examining the state of :code:`AWSTaskCompletionSource`. The following example illustrates the case where :code:`textModeSwitchingCompletion` is an :code:`AWSTaskCompletionSource` instance and the desired result is that a new conversation will be in the :code:`texttInTextOut` mode.

    .. container:: option

        iOS - Swift
            .. code-block:: swift

                if let textModeSwitchingCompletion = textModeSwitchingCompletion {
                        textModeSwitchingCompletion.setResult(text)
                        self.textModeSwitchingCompletion = nil
                    }
                    else {
                        self.interactionKit?.textInTextOut(text)
                    }

        Objective C
            .. code-block:: objectivec

                if(textModeSwitchingCompletion){
                    [textModeSwitchingCompletion setResult:text];
                    textModeSwitchingCompletion = nil;
                  }else{
                    [self.interactionKit textInTextOut:text];
                }

Integrating Voice Conversation
------------------------------

Perform the following tasks to implement voice interaction with Amazon Lex in your iOS app.

Add a voice button and bind it to the Lex SDK UI component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a voice UIView into your storyboard scene or xib file, add a voice button (the UI element that enables users to speak to Amazon Lex). Map the voice button to the SDK button component by setting the `class` for the voice UIView to `AWSLexVoiceButton` as illustrated in the following image.

.. image:: images/conversational-bots-voice-ui.png
