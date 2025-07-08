import pyttsx3
from PyPDF2 import PdfReader


def main():
    #Open the file in read mode
    with open("pdf_file_name.pdf", "rb") as Pdf_read:
        pdfreader = PdfReader(Pdf_read)
        #identify the number of pages in the pdf
        number_of_pages = len(pdfreader.pages)
        #Initialise the text to speech platform
        speaker = pyttsx3.init()
#Go through each page and convert each page from text to speech form.
#remove unwanted spaces and lines during conversion
#Print the content of each page
        for page_num in range(number_of_pages):
            text = pdfreader.pages[page_num].extract_text()
            cleaned_text = text.strip().replace('\n', ' ')
            print(cleaned_text.encode("utf-8"))
            # allow speaker to speak the text & save as mp3 file
            speaker.say(cleaned_text)
            speaker.save_to_file(cleaned_text, 'file_name_to_be_saved.mp3')
            speaker.runAndWait()
            speaker.stop()


if __name__ == "__main__":
    main()