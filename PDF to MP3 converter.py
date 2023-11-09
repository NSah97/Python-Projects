import os
import PyPDF2
import pyttsx3

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, language='de'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust the volume (0.0 to 1.0)
    engine.save_to_file(text, 'Enter_Name_of_MP3_File.mp3') # Here you can adjust the name of the output file
    engine.runAndWait()

def pdf_to_speech(pdf_path):
    text = pdf_to_text(pdf_path)
    text_to_speech(text, language='de')

if __name__ == "__main__":
    # Bestimme den Pfad des aktuellen Ordners (funktioniert nur, wenn py.script und PDf im gleichen Ordner gespeichert sind)
    current_folder = os.path.dirname(os.path.abspath(__file__))

    pdf_file = os.path.join(current_folder, "insert/any/pdf/file.pdf")

    pdf_to_speech(pdf_file)

    # Öffne die generierte MP3-Datei mit dem Standard-Audioplayer
    os.system('start output.mp3')
