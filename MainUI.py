
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
from ttkbootstrap import Style
import ttkbootstrap as tb


class VoiceRecorder:


    def __init__(self):
        global source
        global target
        # self.root = tk.Tk()
        self.root = tb.Window(themename='darkly')
        self.root.title("Voice Compare")
        self.root.geometry("1000x1000")
        #self.root.resizable(False, False)
        # Apply styling to GUI elements
        # style = Style(theme='darkly')
        # self.button = tk.Button(text="♫", anchor="center", font=("Arial", 120, "bold"), command=self.click_handler)
        # # ttk.Button(create_rec_voice_old, text='Record', command=self.click_handler).pack(padx=5, pady=10)
        # self.button.pack(pady=10, anchor="center")
        self.rec_button = tb.Button(text="♫", style="success, outline", command=self.click_handler)
        self.rec_button.pack(pady=20)
        self.label = tb.Label(text="00:00:00", style="primary")
        self.label.pack(pady=10)
        self.recording = False
        src_label = tb.Label(text="SOURCE FILE",font=("Helvetica", 28), style="default")
        self.label1 = tb.Label(text="SOURCE", font=("Helvetica", 28), style="default")
        self.label1.pack(pady=10)
        # self.source_audio()
        files = os.listdir("./audiofiles/")
        source = tb.Combobox(style="success", values=files)
        source.current(0)

        source.pack()
        self.label2 = tb.Label(text="TARGET", font=("Helvetica", 28), style="default")
        self.label2.pack(pady=10)
        # self.target_audio()
        files = os.listdir("./audiofiles/")
        target = tb.Combobox( style="success", values=files)
        target.current(0)
        target.pack()
        self.compare_button = tb.Button(text="COMPARE", style="success, outline", command=self.compare)
        self.compare_button.pack(pady=20)
        # print(target.get())


        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            print("NOT RECORDING")
            self.recording = False
            # self.label = tk.Label(text="00:00:00")
            self.rec_button.configure(style="default")
        else:
            print("RECORDING")
            self.recording = True
            # self.rec_button.configure(style="warning")
            threading.Thread(target=self.record).start()
        #print(os.path.abspath())
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
            print('Entered While to save')
            if os.path.exists(f"./audiofiles/recording{i}.wav"):
                i += 1
            else:
                exists = False

        sound_file = wave.open(f"./audiofiles/recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()

    # def source_audio(self):
    #     # source = tk.Listbox()
    #
    #
    # def target_audio(self):
        # target = tk.Listbox()


    def compare(self):
        print(source.get())
        print(target.get())
        self.compare_button.clickable = False

        self.my_gauge = tb.Floodgauge(style="success", font=("helvetica", 18), mask="Pos: {}", maximum=100,
                                      orient="horizontal", value=0, mode="indeterminate")
        self.my_gauge.pack(fill = "x", pady=20)
        self.my_gauge.start()

        self.compare_button.clickable = True


        pass


VoiceRecorder()
