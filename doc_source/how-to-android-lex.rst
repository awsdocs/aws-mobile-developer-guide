.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. highlight:: java

#############################################
Android: Use Natural Language with Amazon Lex
#############################################

.. list-table::
   :widths: 1 6

   * - **Just Getting Started?**

     - :ref:`Use streamlined steps <add-aws-mobile-conversational-bots>` to install the SDK and integrate Amazon Lex.

*Or, use the content on this page if your app integrates existing AWS services.*

Overview
========


|LEX| is an AWS service for building voice and text conversational interfaces into applications. With |LEX|, the same natural language understanding engine that powers Amazon Alexa is now available to any
developer, enabling you to build sophisticated, natural language chatbots into your new and existing
applications.

The |sdk-android| provides an optimized client for interacting with |LEX| runtime APIs,
which support both voice and text input and can return either voice or text. |LEX| has built-in
integration with AWS Lambda to allow insertion of custom business logic into your |LEX| processing flow, including all of the extension to other services that Lambda makes possible.

For information on |LEX| concepts and service configuration, see
`How it Works <http://docs.aws.amazon.com/lex/latest/dg/how-it-works.html>`_ in the *Lex Developer Guide*.

For information about |LEX| Region availability, see `AWS Service Region Availability <http://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`_.

To get started using the |LEX| mobile client, integrate the SDK for Android
into your app, set the appropriate permissions, and import the necessary libraries.


Setting Up
==========

Include the SDK in Your Project
-------------------------------

Follow the instructions at :doc:`setup-legacy` to include the JAR files for this service and set the appropriate
permissions.


Set Permissions in Your Android Manifest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  In your :file:`AndroidManifest.xml` file, add the following permission:

  .. code-block:: java

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />

Declare |LEX| as a Gradle dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Make sure the following  Gradle build dependency is declared in the :file:`app/build.gradle` file.

  .. code-block:: sh

    compile 'com.amazonaws:aws-android-sdk-lex:2.3.8@aar'

Set IAM Permissions for |LEX|
--------------------------------------------

To use |LEX| in an application, create a role and attach policies as described in Step 1 of
`Getting Started <http://docs.aws.amazon.com/lex/latest/dg/gs-bp-prep.html>`_ in the *Lex Developer Guide*.

To learn more about IAM policies, see `Using IAM <http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html>`_.

Configure a Bot
---------------

 Use the `Amazon Lex console <https://console.aws.amazon.com/lex/>`_ console to configure a bot that interacts with your mobile app features. To learn more, see `Amazon Lex Developer Guide <https://docs.aws.amazon.com/lex/latest/dg/what-is.html>`_. For a quickstart, see `Getting Started <https://alpha-docs-aws.amazon.com/lex/latest/dg/getting-started.html>`_ .

|LEX| also supports model building APIs, which allow creation of bots, intents, and slots at runtime. This SDK does not
currently offer additional support for interacting with |LEX| model building APIs.

Implement Text and Voice Interaction with |LEX|
===============================================

Get AWS User Credentials
------------------------

Both text and voice API calls require validated AWS credentials. To establish Amazon Cognito as the credentials provider,
include the following code in the function where you initialize your |LEX| interaction objects.

  .. code-block:: java

    CognitoCredentialsProvider credentialsProvider = new CognitoCredentialsProvider(
                appContext.getResources().getString(R.string.identity_id_test),
                Regions.fromName(appContext.getResources().getString(R.string.aws_region)));

Integrate Lex Interaction Client
--------------------------------

Perform the following tasks to implement interaction with Lex in your Android app.

Initialize Your Lex Interaction Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Instantiate an :code:`InteractionClient`, providing the following parameters.

    - The application context, credentials provider, and AWS Region
    - :code:`bot_name` - name of the bot as it appears in the |LEX| console
    - :code:`bot_alias` - the name associated with selected version of your bot
    - :code:`InteractionListener` - your app's receiver for text responses from |LEX|
    - :code:`AudioPlaybackListener`  - your app's receiver for voice responses from |LEX|

  .. code-block:: java

    // Create Lex interaction client.
        lexInteractionClient = new InteractionClient(getApplicationContext(),
                credentialsProvider,
                Regions.US_EAST_1,
                <your_bot_name>,
                <your_bot_alias>);
        lexInteractionClient.setAudioPlaybackListener(audioPlaybackListener);
        lexInteractionClient.setInteractionListener(interactionListener);

Begin or Continue a Conversation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  To begin a new conversation with |LEX|, we recommend that you clear any history of previous text interactions, and that
  you maintain a :code:`inConversation` flag to make your app aware of when a conversation is in progress.

  If :code:`inConversation` is false when user input is ready to be sent as |LEX| input,  then make a call using the
  :code:`textInForTextOut`, :code:`textInForAudioOut`, :code:`audioInForTextOut`, or :code:`audioInForAudioOut` method
  of an :code:`InteractionClient` instance. These calls are in the form of:

  .. code-block:: java

    lexInteractionClient.textInForTextOut(String text, Map<String, String> sessionAttributes)

  If :code:`inConversation` is true, then the input should be passed to an instance of :code:`LexServiceContinuation`
  using the :code:`continueWithTextInForTextOut`, :code:`continueWithTextInForAudioOut`, :code:`continueWithAudioInForTextOut`,
  :code:`continueWithAudioInForAudioOut` method. Continuation enables |LEX| to persist the state and metadata of an ongoing conversation across multiple interactions.

Interaction Response Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  :code:`InteractionListener` captures a set of |LEX| response events that include:

  - :code:`onReadyForFulfillment(final Response response)`

    This response means that Lex has the information it needs to co fulfill the intent of the user and considers the
    transaction complete. Typically, your app would set your :code:`inConversation` flag to false when this response arrives.

  - :code:`promptUserToRespond(final Response response, final LexServiceContinuation continuation)`

    This response means that |LEX| is providing the next piece of information needed in the conversation flow. Typically
    your app would pass the received continuation on to your |LEX| client.

  - :code:`onInteractionError(final Response response, final Exception e)`

    This response means that |LEX| is providing an identifier for the exception that has occured.

Microphone Events
~~~~~~~~~~~~~~~~~

  :code:`MicrophoneListener` captures events related to the microphone used for interaction with |LEX| that include:

  - :code:`startedRecording()`

    This event occurs when the user has started recording their voice input to |LEX|.

  - :code:`onRecordingEnd()`

    This event occurs when the user has finished recording their voice input to |LEX|.

  - :code:`onSoundLevelChanged(double soundLevel)`

    This event occurs when the volume level of audio being recorded changes.

  - :code:`onMicrophoneError(Exception e)`

    The event returns an exception when an error occurs while recording sound through the microphone.

Audio Playback Events
~~~~~~~~~~~~~~~~~~~~~

  :code:`AudioPlaybackListener` captures a set of events relatedto |LEX| voice responses that include:

  - :code:`onAudioPlaybackStarted()`

    This event occurs when playback of a |LEX| voice response starts.

  - :code:`onAudioPlayBackCompleted()`

    This event occurs when playback of a |LEX| voice response finishes.

  - :code:`onAudioPlaybackError(Exception e)`

    This event returns an exception when an error occurs duringplayback of an |LEX| voice response.


Add Voice Interactons
---------------------

Perform the following tasks to implement voice interaction with |LEX| in your Android app.

:code:`InteractiveVoiceView` simplifies the acts of receiving and playing voice responses from Lex by internally
using the :code:`InteractionClient` methods and both :code:`MicrophoneListener` and :code:`AudioPlaybackListener` events
described in the preceding sections. You can use those interfaces directly instead of instantiating
:code:`InteractiveVoiceView`.

Add a :code:`voice-component` Layout Element to Your Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  In the layout for your activity class that contains the voice interface for your app, include the following element.

  .. code-block:: xml

     <include
        android:id="@+id/voiceInterface"
        layout="@layout/voice_component"
        android:layout_width="200dp"
        android:layout_height="200dp"
         />

Initialize Your Voice Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  In your activity class that contains the voice interface for your app, have the base class implement
  :code:`InteractiveVoiceView.InteractiveVoiceListener`.

  The following code shows initialization of :code:`InteractiveVoiceView`.

  .. code-block:: java

    private void init() {
        appContext = getApplicationContext();
        voiceView = (InteractiveVoiceView) findViewById(R.id.voiceInterface);
        voiceView.setInteractiveVoiceListener(this);
        CognitoCredentialsProvider credentialsProvider = new CognitoCredentialsProvider(
            <your_conginto_identity_pool_id>,
            Regions.fromName(<your_aws_region>)));
        voiceView.getViewAdapter().setCredentialProvider(credentialsProvider);
        voiceView.getViewAdapter().setInteractionConfig(
            new InteractionConfig(<your_bot_name>),
                <your_bot_alias>));
        voiceView.getViewAdapter().setAwsRegion(<your_aws_region>));
    }

