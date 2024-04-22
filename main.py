import os
import commands
import model
from model import train, predict
from audio import convert_bytes_to_audio_tensor, load_audio_from_file, record_audio
import tensorflow as tf
import librosa
import numpy as np
import torchaudio

# paths to data & output dirs
data_dir = "/Users/katieclancy/Desktop/data_dir/training"
output_dir = "/Users/katieclancy/Desktop/CASE4/CA400/asr/model.py"

def main():
    with tf.device('/cpu:0'):

        # load data
        audio_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".wav")]
        audio_data = load_data(audio_files)

        # preprocess audio data
        audio_data = preprocess_data(audio_data)
        labels, label_encoder = prepare_labels()

        # train & save model
        trained_model = train(audio_data, labels, label_encoder)
        trained_model.save(os.path.join(output_dir, "model"))


        # initialize microphone & speech recognizer
        mic = sr.Microphone(sample_rate=16000)
        r = sr.Recognizer()
        #with sr.Microphone(sample_rate=16000) as source:
        print('You may begin speaking now...')
        while True:
            try:
                    with mic as source:
                        # adjust for ambient noise
                        r.adjust_for_ambient_noise(source)
                        # listen for audio
                        audio = r.listen(source, phrase_time_limit=3)
                    #audio_segment = audio.record_audio(source)
                    #audio = np.array(audio_segment.get_array_of_samples())
                    audio_data = audio.frame_data
                    spectrogram = librosa.feature.melspectrogram(y=audio, sr=16000, n_mels=128)
                    spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
                    spectrogram = np.expand_dims(spectrogram, axis=0)

                    # transcribe audio using model
                    text = trained_model.transcribe_audio(spectrogram)

                    # handling tspoken command
                    command_detected = commands.handle_spoken_command(text)

                    if not command_detected:
                        print(f'Error: command not recognized in {audio_file}')
                    
                    with open("transcript.txt", "a") as f:
                        f.write(text + '\n')

            except sr.WaitTimeoutError:
                 #print('Error: timeout')
                 pass
            
            except Exception as e:
                print(f'Error: {e}')

if __name__ == '__main__':
    main()
