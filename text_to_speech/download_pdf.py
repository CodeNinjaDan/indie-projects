from fpdf import FPDF

ocean_content = """
"""

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(80)
        self.cell(30, 10, 'Ocean Facts', 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Create PDF object
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 12)


pdf.multi_cell(0, 10, ocean_content.encode('latin-1', 'replace').decode('latin-1'))

pdf.output('Ocean_Facts.pdf', 'F')

print("Success! 'Ocean_Facts.pdf' has been created in your current folder.")