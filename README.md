README
Summarizer App
Overview
The Summarizer App is a simple and efficient tool designed to automate the process of summarizing audio files. It is especially useful for condensing information from meetings, interviews, and lectures. The app transcribes audio files and generates a summary with neat and organized notes. This summary can include headings and subheadings, formulated notes, or action plans, depending on the content.

Features
Supports multiple audio file formats such as .mp3, .mp4, .mpeg, .mpga, .m4a, .wav, .webm.
Utilizes GPT-4, a state-of-the-art language model for generating high-quality summaries.
Easy to use with a simple graphical user interface (GUI).
Automatically saves summarized text to the output_files directory.
Prerequisites
Python 3.x
OpenAI API key
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository_link>
Navigate to the project directory:

bash
Copy code
cd <project_directory>
Install the required dependencies:

Copy code
pip install openai
pip install tkinter
Usage
Export your OpenAI API key to the environment variable. Replace your_api_key with your actual API key:

arduino
Copy code
export OPENAI_API_KEY='your_api_key'
Run the app by executing the app.py script:

Copy code
python3 app.py
The app's GUI will open. Click on the Select Audio File button to choose the audio file you want to summarize.

Once you select the file, the app will transcribe the audio and summarize the content. The summarized text will be saved in the output_files directory with a sequential naming pattern summarized_text_#.txt.

Notes
The summarization prompt and system message used by the GPT-4 model are read from summarize_prompt.txt and system_message.txt respectively. The system message instructs the chatbot on how to summarize the content.

The summarization process may take some time depending on the length of the audio file.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
