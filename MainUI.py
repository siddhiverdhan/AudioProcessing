
import os
import wave
import time
import threading
import tkinter as tk
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox, ttk
#from ttkbootstrap import Style


class VoiceRecorder:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voice Recorder")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        # Apply styling to GUI elements
        # style = Style(theme='superhero')
        # style.configure('TLabel', font=('TkDefaultFont', 18))
        # style.configure('TButton', font=('TkDefaultFont', 16))
        # Notebook widget to manage tabs
        # self.notebook = ttk.Notebook(self.root)
        # self.notebook.pack(fill='both', expand=True)
        # Record Voice Tab
        # create_rec_voice = ttk.Frame(self.notebook)
        # self.notebook.add(create_rec_voice, text="Record Voice")
        # tk.Button(create_rec_voice, text='Record Audio').pack(padx=5, pady=10)
        # ttk.Label(create_rec_voice, text='Time:').pack(padx=5, pady=10)
        # Record Voice Tab Old
        # create_rec_voice_old = ttk.Frame(self.notebook)
        # self.notebook.add(create_rec_voice_old, text="Record Voice Old")
        self.button = tk.Button(text="♫", anchor="center", font=("Arial", 120, "bold"), command=self.click_handler)
        # ttk.Button(create_rec_voice_old, text='Record', command=self.click_handler).pack(padx=5, pady=10)
        self.button.pack(pady=70, anchor="center")
        self.label = tk.Label(text="00:00:00", fg="black")
        self.label.pack(pady=10)
        self.recording = False
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            print("NOT RECORDING", self.button.configure().keys())
            self.recording = False
            self.button.configure(fg="red")
        else:
            print("RECORDING", self.button.configure().keys())
            self.recording = True
            self.button.configure(fg="black")
            threading.Thread(target=self.record).start()
        print(os.path.abspath())
    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

        frames = []

        start = time.time()

        while self.recording:
            data = stream.read(1024)
            frames.append(data)

            passed = time.time() - start
            secs = passed % 60
            minis = passed // 60
            hours = minis // 60
            self.label.config(text=f"{int(hours):02d}:{int(minis):02d}:{int(secs):02d}")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        exists = True
        i = 1
        while exists:

            if os.path.exists(f"recording{i}.wav"):
                i += 1
            else:
                exists = False

        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()

        # sound_file = wave.open(f"recording{i}.wav")
        # signal_wave = sound_file.readframes(-1)
        # t_audio = sound_file.getnframes() / sound_file.getframerate()
        # signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        # n_samples = sound_file.getnframes()
        # sound_file.close()
        # times = np.linspace(0, t_audio, num=n_samples)
        #
        # plt.figure(figsize=(15, 5))
        # plt.plot(times, signal_array)
        # plt.title("Audio")
        # plt.ylabel("sign wave")
        # plt.xlabel("Time (s)")
        # plt.xlim(0, t_audio)


VoiceRecorder()
