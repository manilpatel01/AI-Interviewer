import boto3
import streamlit as st
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

Session = boto3.Session(
        aws_access_key_id = st.secrets['key'],
        aws_secret_access_key = st.secrets['value'],
        region_name = "us-east-1"
    )

# def synthesize_speech(text):
#     Polly = Session.client("polly")
#     response = Polly.synthesize_speech(
#         Text=text,
#         OutputFormat="mp3",
#         VoiceId="Joanna")
#     if "AudioStream" in response:
#         with closing(response["AudioStream"]) as stream:
#             output = os.path.join(gettempdir(), "temp_audio.mp3")

#             try:
#                 with open(output, "wb") as file:
#                     file.write(stream.read())
#             except IOError as error:
#                 print(error)
#                 sys.exit(-1)
#     else:
#         print("Could not stream audio")
#         sys.exit(-1)

#      # Play the audio using the platform's default player
#     if sys.platform == "win32":
#         os.startfile(output)
#     else:
#         # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
#         opener = "open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, output])
        
#     return output

def synthesize_speech(text):
    
    print(text)

    Polly = Session.client("polly")
    
    try:
        response = Polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna")
        
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "temp_audio.mp3")
                print(output)
                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                    return output
                except IOError as error:
                    print("Error writing audio file:", error)
        else:
            print("Could not stream audio. Response:", response)
    except Exception as e:
        print("Error synthesizing speech:", e)
    
    return None
