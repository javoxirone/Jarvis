import pvporcupine
from pvrecorder import PvRecorder
from playsound import playsound
import webbrowser
from constants import BASE_DIR, FIREFOX_PATH
from utils import generate_random_voice


webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(FIREFOX_PATH))

hello_random = generate_random_voice('hello')
playsound("voice/hello/" + f"{hello_random}.wav")

porcupine = pvporcupine.create(access_key="eBmGI+vRC2cGrSFdhAVW7APhiap+o3l2ppnMUGt98Aulv8b1YK1YfQ==",
                               keyword_paths=['keywords/Jarvis_en_windows_v2_2_0.ppn',
                                              'keywords/at-crow-browser_en_windows_v2_2_0.ppn',
                                              'keywords/at-crow-you-tube_en_windows_v2_2_0.ppn'],
                               model_path='models/porcupine_params.pv')
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recoder.start()

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index == 0:
            playsound("voice/yes_sir/" + f"{generate_random_voice('yes_sir')}.wav")
        elif keyword_index == 1:
            webbrowser.get("firefox").open("https://www.google.com")
            playsound("voice/done/" + f"{generate_random_voice('done')}.wav")
        elif keyword_index == 2:
            webbrowser.get("firefox").open("https://www.youtube.com")
            playsound("voice/done/" + f"{generate_random_voice('done')}.wav")


except KeyboardInterrupt:
    recoder.stop()

finally:
    porcupine.delete()
    recoder.delete()
