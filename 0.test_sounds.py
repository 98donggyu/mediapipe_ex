# pip install simpleaudio
import simpleaudio as sa

filename = 'assets/alarm.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()