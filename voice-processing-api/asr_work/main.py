import os
from .commands import handle_spoken_command
from .model import train, predict
from .audio import convert_bytes_to_audio_tensor, load_audio_from_file, record_audio
import speech_recognition as sr
import tensorflow as tf
import librosa
import numpy as np
import torchaudio

# paths to data & output dirs
data_dir = "C:\\Users\\Niall\\Documents\\College_Work\\CASE4\CA400\\2023-ca400-clancyk2-egann8\\src\\voice-processing-api\\asr_work\\data"
output_dir = "output"
trained_model = 0

print(os.listdir(data_dir))

def initial_training():
    with tf.device('/cpu:0'):

        # load data
        audio_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".wav")]
        audio_data = load_audio_from_file(audio_files[0])

        # preprocess audio data
        audio_data = convert_bytes_to_audio_tensor(audio_data)
        labels, label_encoder = prepare_labels()

        # train & save model
        global trained_model
        trained_model = train(audio_data, labels, label_encoder)
        trained_model.save(os.path.join(output_dir, "model"))



def call_model(filePath):
        with tf.device('/cpu:0'):

        # initialize microphone & speech recognizer
            mic = sr.Microphone(sample_rate=16000)
            r = sr.Recognizer()
            #with sr.Microphone(sample_rate=16000) as source:
            print('You may begin speaking now...')
            while True:
                try:
                        with sr.AudioFile(filePath) as source:
                            # adjust for ambient noise
                            r.adjust_for_ambient_noise(source)
                            # listen for audio
                            audio = r.listen(source, phrase_time_limit=3)
                            # audio_segment = audio.record_audio(source)
                        audio = np.array(audio)
                        # audio_data = audio.frame_data
                        spectrogram = librosa.feature.melspectrogram(y=audio, sr=16000, n_mels=128)
                        spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
                        spectrogram = np.expand_dims(spectrogram, axis=0)

                        # transcribe audio using model
                        text = trained_model.transcribe_audio(spectrogram)

                        # handling tspoken command
                        # command_detected = commands.handle_spoken_command(text)
                        command_detected = handle_spoken_command(text)
                        print(command_detected)

                        if not command_detected:
                            print(f'Error: command not recognized in {filePath}')
                        
                        # write out spoken input to transcript.txt
                        with open("transcript.txt", "a") as f:
                            f.write(text + '\n')
                        
                        return command_detected

                except sr.WaitTimeoutError:
                    #print('Error: timeout')
                    pass
                
                except Exception as e:
                    print(f'Error: {e}')

def main():
    filePath = './uploads/processedVoiceFile.wav'

    initial_training()
    call_model(filePath)

if __name__ == '__main__':
    main()
