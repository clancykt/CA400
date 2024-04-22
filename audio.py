import tensorflow as tf
import io
import librosa
import speech_recognition as sr
import sounddevice as sd

def convert_bytes_to_audio_tensor(data):
    return tf.audio.decode_wav(data).audio

def load_audio_from_file(file, sample_rate=16000):
    # Load audio file using librosa
    audio_data, _ = librosa.load(file, sr=sample_rate, dtype='float32')
    # Convert to bytes and then decode to audio tensor
    return convert_bytes_to_audio_tensor(audio_data.tobytes())

def load_audio_from_microphone(duration=5, sample_rate=16000):
    # Capture audio from the microphone
    print(f"Recording audio for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Convert to float32 and then to bytes
    audio_data = audio_data.astype('float32')
    return convert_bytes_to_audio_tensor(audio_data.tobytes())

def record_audio(source, sample_rate=16000):
    r = sr.Recognizer()
    with source(sample_rate=sample_rate) as src:
        audio = r.listen(src)
        return convert_bytes_to_audio_tensor(audio.get_wav_data())
