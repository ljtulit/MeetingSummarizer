import os
import tkinter as tk
from tkinter import filedialog
from api import send_chat_completion_request, transcribe_audio_file


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(
            self, text="Select Audio File", command=self.select_audio_file)
        self.select_button.pack(side="top")

        self.quit_button = tk.Button(
            self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("Audio Files", "*.mp3 *.mp4 *.mpeg *.mpga *.m4a *.wav *.webm"),
            ("All Files", "*.*")
        ])
        text = transcribe_audio_file(file_path)
        summarized_text = summarize_text(text)
        save_summarized_text(summarized_text)


def summarize_text(text):
    # define model
    model = "gpt-4"
    # define prompt
    with open('summarize_prompt.txt', 'r') as f:
        prompt = f.read()

    # define system message
    with open('system_message.txt', 'r') as f:
        system = f.read()

    prompt = f"{prompt}{text}"
    # call api
    response = send_chat_completion_request(model, prompt, system)
    response_text = response['choices'][0]['message']['content']
    # return response
    return response_text


def save_summarized_text(summarized_text):
    output_dir = 'output_files'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sequential naming
    files = os.listdir(output_dir)
    max_index = 0
    for file in files:
        if file.startswith('summarized_text_'):
            index = int(file.split('_')[2].split('.')[0])
            max_index = max(max_index, index)

    output_file = f'summarized_text_{max_index + 1}.txt'
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, 'w') as f:
        f.write(summarized_text)


if __name__ == '__main__':
    main()
