import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import io
import speech_recognition as sr
from pydub import AudioSegment
import time
import librosa
from IPython.display import Audio
import IPython.display as display
import numpy as np
from scipy.io import wavfile
import logging
import soundfile as sf



#https://huggingface.co/facebook/wav2vec2-base-960h
model_name = "facebook/wav2vec2-base-960h"
tokenizer = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

r = sr.Recognizer()


def wav2vec():
    file_name = "./test.wav"
    input_audio, rate = librosa.load(file_name,sr=16000) #convert the wav file to 16khz
    display.Audio(file_name, rate=rate, autoplay=True)
    inputs = tokenizer(input_audio, return_tensors="pt").input_values
    logits = model(inputs).logits
    tokens = torch.argmax(logits, dim=-1)
    text = tokenizer.batch_decode(tokens)[0]
    user_speech = str(text).lower()


logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

wav2vec()
