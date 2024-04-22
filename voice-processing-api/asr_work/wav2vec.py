import torch
import speech_recognition as sr
import tensorflow as tf
import librosa
import numpy as np
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import os

model_name = "facebook/wav2vec2-base-960h"
tokenizer = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def call_model(filePath):
    input_audio, rate = librosa.load(filePath,sr=16000) #convert the wav file to 16khz
    inputs = tokenizer(input_audio, return_tensors="pt").input_values
    logits = model(inputs).logits
    tokens = torch.argmax(logits, dim=-1)
    text = tokenizer.batch_decode(tokens)[0]
    user_speech = str(text).lower()
    return user_speech