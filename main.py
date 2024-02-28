from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
data_frame = pd.read_csv("topics.csv")

for index, row in data_frame.iterrows():
    # set header
    pdf.add_page()
    pdf.set_font(family="courier", style="B", size=24)
    pdf.set_text_color(52, 158, 121)
    pdf.cell(w=0, h=12, ln=1, txt=(row['Topic']), align='l')

    # printing horizontal lines
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # set footer
    pdf.ln(265)
    pdf.set_font(family="courier", style="I", size=12)
    pdf.set_text_color(122, 140, 134)
    pdf.cell(w=0, h=12, ln=1, txt=row['Topic'], align='r')

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # printing horizontal lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
        # set footer
        pdf.ln(277)
        pdf.set_font(family="courier", style="I", size=12)
        pdf.set_text_color(122, 140, 134)
        pdf.cell(w=0, h=12, ln=1, txt=row['Topic'], align='r')


pdf.output("out.pdf")
