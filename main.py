from fpdf import FPDF   # Import FPDF class from fpdf module
import pandas as pd


df = pd.read_csv('topics.csv')

# Create instance of FPDF class
pdf = FPDF(orientation='portrait', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()  # Add a page
    pdf.set_font(family="Times",style="B", size=24)  # Set font for the
    pdf.set_text_color(100, 100, 100)  # Set text color
    pdf.cell(w=0,h=12, txt=row['Topic'],align="L",ln=1)  # Add a cell for header
    pdf.line(10, 21, 200, 21)  # Draw a line


    pdf.ln(265) #add space for the topics
    pdf.set_font(family="Times",style="I", size=8)  # Set font for the
    pdf.set_text_color(180, 180, 180)  # Set text color  
    pdf.cell(w=0,h=10, txt=row['Topic'],align="R")  # Add a cell for footer

    for i in range(row["Pages"] - 1): #add pages from the topics
        pdf.add_page()
        pdf.ln(277) #add space for the topics
        pdf.set_font(family="Times",style="I", size=8)  # Set font for the
        pdf.set_text_color(180, 180, 180)  # Set text color  
        pdf.cell(w=0,h=10, txt=row['Topic'],align="R")  # Add a cell for footer

pdf.output("topics.pdf")  # Output the pdf