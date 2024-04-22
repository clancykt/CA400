import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor # pre-trained model for SR
import speech_recognition as sr # provides interface to record audio from microphone
import io # i/o handling
import soundfile as sf
from pydub import AudioSegment # converts audio data to compatible form for processing by model
import glob

# initialize pre-trained model
tokenizer = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-large-960h-lv60-self')
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-large-960h-lv60-self')

# target words & phrases
target_words = ['print', 'hello', 'world', 'for', 'in', 'range', 'colon', 'indent', 'variable', 'function', 'return', 'add', 'subtract', 'multiply', 'divide', 'arithmetic', 'operation', 'argument', 'if', 'else', 'comparison', 'operator', 'equal', 'not equal', 'less than', 'greater than', 'boolean', 'true', 'false', 'and', 'or', 'comment', 'hashtag', 'quote', 'parenthesis', 'brackets', 'curly brackets', 'integer', 'float', 'string']

'''
# loading python command dataset
python_audios = glob.glob('path/to/dataset')

# loading audio files from dataset
for file in python_audios:
    with sf.SoundFile(file, 'rb') as f:
        audio_data = f.read()

    # convert audio data to pydub AudioSegment
    audio = AudioSegment(
        audio_data.tobytes(),
        frame_rate=f.samplerate,
        sample_width=f.subtype.itemsize,
        channels=f.channels
    )
'''
# creating new object
r = sr.Recognizer()

with sr.Microphone(sample_rate=16000) as source:
    print('You may begin speaking now...')

    while True:
        try:
            # recorded audio is converted to an obj 'BytesIO' -> 'pydub' -> 'AudioSegment'
            audio = r.listen(source) #pyaudio object
            data = io.BytesIO(audio.get_wav_data()) # array of bytes
            clip = AudioSegment.from_file(data) # numpy array
            x = torch.FloatTensor(clip.get_array_of_samples()) # tensor

            # convert AudioSegment to tensor
            x = torch.FloatTensor(audio.get_array_of_samples())

            # wav2vec2 processor tokenizes the audio for the model
            inputs = tokenizer(x, sampling_rate=16000, return_tensors='pt', padding='longest').input_values
            logits = model(inputs).logits
            tokens = torch.argmax(logits, axis=-1) # get the distribution of each timestamp
            # converts token ID's to text
            text = tokenizer.batch_decode(tokens) # puts tokens into string

            # handling the spoken commands
            command_detected = False
            for word in target_words:
                if word in str(text).lower():
                    if word == 'indent':
                        print('    ', end='')
                    else:
                        print(word + ' ', end='')
                    command_detected = True
                    break

            if not command_detected:
                print(f'Error: command not recognized in {audio_file}')

        # except block for program execution interruptions
        except Exception as e:
            print(f'Error: {e}')
