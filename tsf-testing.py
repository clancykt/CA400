from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
import librosa as lb
import torch

# Initialize the tokenizer
tokenizer = Wav2Vec2CTCTokenizer.from_pretrained('facebook/wav2vec2-base-960h')

# Initialize the model
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')

# Read the sound file
waveform, rate = lb.load('./order.wav', sr = 16000)

# Tokenize the waveform
input_values = tokenizer(waveform, return_tensors='pt').input_values

# Retrieve logits from the model
logits = model(input_values).logits

# Take argmax value and decode into transcription
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.batch_decode(predicted_ids)

# Print the output
print(transcription)