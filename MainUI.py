
import os
import wave
import time
import threading
import tkinter as tk
import pyaudio
from PIL import Image
Image.CUBIC = Image.BICUBIC
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox, ttk, END
# from ttkbootstrap import Style
import ttkbootstrap as tb
import requests
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

class VoiceRecorder:


    def __init__(self):
        global source
        global target
        # self.root = tk.Tk()
        self.root = tb.Window(themename='darkly')
        self.root.title("Voice Compare")
        self.root.geometry("1000x1000")

        # main_frame = tk.Frame()
        # main_frame.pack(fill=BOTH, expand=1)
        # my_canvas = tk.Canvas(main_frame)
        # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        # my_scrollbar.pack(side=RIGHT, fill='y')
        # my_canvas.configure(yscrollcommand=my_scrollbar.set)
        # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # second_frame = tk.Frame(my_canvas)
        # my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        self.rec_button = tb.Button(text="♫", style="success, outline", command=self.click_handler)
        self.rec_button.pack(pady=20)
        self.label = tb.Label(text="00:00:00", style="primary")
        self.label.pack(pady=10)
        self.recording = False
        src_label = tb.Label( text="SOURCE FILE",font=("Helvetica", 28), style="default")
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
        self.label3 = tb.Label(text="RESULTS", font=("Helvetica", 28), style="default")
        self.label3.pack(pady=10)

        self.compare_button = tb.Button(text="COMPARE", style="success, outline", command=self.compare)
        self.compare_button.pack(pady=20)
        # print(target.get())
        sf = ScrolledFrame(self.root, autohide=False)
        sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        mfcc1 = tb.Meter(sf, metersize=200, padding=5, amountused=25, metertype="semi", subtext="MFCC", interactive=True)
        # mfcc1.grid(row=1, column=1, padx=10, pady=10)
        mfcc1.place(x=0,y=0)
        SPCENT1 = tb.Meter(sf,metersize=200, padding=5, amountused=25, metertype="semi", subtext="SPCENT", interactive=False)
        SPCENT1.place(x=150,y=0)
        Chroma_Stft = tb.Meter(sf,metersize=200, padding=5, amountused=25, metertype="semi", subtext="Chroma Stft", interactive=False)
        Chroma_Stft.place(x=300,y=0)
        Spec_Bandwidth = tb.Meter(sf,metersize=200, padding=5, amountused=25, metertype="semi", subtext="Spectral Bandwidth", interactive=False)
        Spec_Bandwidth.place(x=450,y=0)
        roll_off = tb.Meter(sf,metersize=200, padding=5, amountused=25, metertype="semi", subtext="Roll Off Frequency", interactive=False)
        roll_off.place(x=600,y=0)
        self.text_box = tk.Text( height=10, width=50)
        self.text_box.pack(pady=10)
        self.my_gauge = tb.Floodgauge(style="success", font=("helvetica", 18), mask="Request: {}", maximum=100,
                                      orient="horizontal", value=0, mode="indeterminate")
        self.my_gauge.pack(fill="x", pady=20)
        mfcc1.configure(amountused=20)
        SPCENT1.configure(amountused=50)
        Chroma_Stft.configure(amountused=70)
        Spec_Bandwidth.configure(amountused=90)
        roll_off.configure(amountused=100)
        # self.mfcc1.grid(row=4,column=0)
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
    #     source = tk.Listbox()
    #
    #
    # def target_audio(self):
        # target = tk.Listbox()


    def compare(self, compare_results=None):
        print(source.get())
        print(target.get())
        self.compare_button.clickable = False
        self.my_gauge.value = 0
        self.my_gauge.start()
        # API request
        r = requests.get('https://api.quotable.io/random')
        data = r.json()
        quote = data['content']
        # deletes all the text that is currently
        # in the TextBox
        self.text_box.delete('1.0', END)

        # inserts new data into the TextBox
        self.text_box.insert(END, quote)

        self.my_gauge.stop()
        # update the amount used directly
        return compare_results



VoiceRecorder()
