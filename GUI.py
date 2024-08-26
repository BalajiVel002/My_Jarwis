import tkinter as tk
import speech_recognition as sr

class VoiceRecognitionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Voice Recognition")

        self.label = tk.Label(master, text="Listening for speech...", font=("Helvetica", 14), fg="blue")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(master, width=50, font=("Helvetica", 12))
        self.text_entry.pack(pady=10)

        self.recognize_speech()

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, text)
                self.master.after(100, self.recognize_speech)  # Start recognizing again after 100ms
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                self.master.after(100, self.recognize_speech)  # Start recognizing again after 100ms
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                self.master.after(100, self.recognize_speech)  # Start recognizing again after 100ms

def main():
    root = tk.Tk()
    app = VoiceRecognitionGUI(root)
    root.configure(bg="lightgray")
    root.mainloop()

if __name__ == "__main__":
    main()
