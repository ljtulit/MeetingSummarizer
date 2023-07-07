import openai
import logging
import traceback
import os


def send_chat_completion_request(model, prompt, system=None, function_definition=None, stream=False):

    if system is None:
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]

    if function_definition is None:
        try:
            return openai.ChatCompletion.create(
                model=model,
                messages=messages
            )
        except Exception as e:
            logging.error(f"Error calling API: {e}\n{traceback.format_exc()}")
            print(f"Exception: {e}\n{traceback.format_exc()}")
            return None
    else:
        try:
            return openai.ChatCompletion.create(
                model=model,
                messages=messages,
                functions=[function_definition],
                stream=stream
            )
        except Exception as e:
            logging.error(f"Error calling API: {e}\n{traceback.format_exc()}")
            print(f"Exception: {e}\n{traceback.format_exc()}")
            return None


def transcribe_audio_file(file_path):
    audio_file = open(file_path, "rb")

    print()
    try:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    except Exception as e:
        logging.error(f"Error calling API: {e}\n{traceback.format_exc()}")
        print(f"Exception: {e}\n{traceback.format_exc()}")
        return None

    return transcription
