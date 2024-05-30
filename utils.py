import re
from fpdf import FPDF
   

def clean_text(text):
    # if new line if followed by - join the lines
    text = text.replace("-\n\n", "")
    # if new line if followed by - join the lines
    text = text.replace("-\n", "")
    # replace double new lines with a whitespace
    text = text.replace("\n\n", " ")
    # # remove new lines
    text = text.replace("\n", "")
    # clean for 'Crime and Punishment'
    text = text.replace("Crime and Punishment", "")
    # clean 'Download free eBooks of classic literature, books and novels at Planet eBook.' 
    text = text.replace("Download free eBooks of classic literature, books and novels at Planet eBook.", "")
    # clean Subscribe to our free eBooks blog and email newsletter.
    text = text.replace("Subscribe to our free eBooks blog and email newsletter.", "")
    # check if there is any number on the right of 'Free eBooks at Planet eBook.com' if so remove it
    text = re.sub(r'Free eBooks at Planet eBook.com\s+\d+', '', text)
    # clean Free eBooks at Planet eBook.com
    text = text.replace("Free eBooks at Planet eBook.com", "")
    # remove all characters like \x181
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    # remove double or more spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def create_pdf(summary):
    

    # Define the PDF document
    class PDF(FPDF):
        def footer(self):
            self.set_y(-15)
            self.set_x(-5)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    # Create instance of FPDF class
    pdf = PDF()
    pdf.set_left_margin(22)
    pdf.set_right_margin(22)
    pdf.add_page()

    # add title and author in the center of first page
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Summary of Crime and Punishment', 0, 1, 'C')
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 1, 'by Fyodor Dostoevsky', 0, 1, 'C')

    # add space between title and content
    pdf.ln(8)

    # Add content
    pdf.set_font('Arial', '', 13)
    pdf.multi_cell(0, 10, summary)

    # Saving the PDF file
    pdf_output_path = 'Crime_and_Punishment_Summary.pdf'
    pdf.output(pdf_output_path)

    pdf_output_path