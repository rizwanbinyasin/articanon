"""
Cavalier Machine Learning, University of Virginia
September 2018
"""
from fpdf import FPDF

class Book(FPDF):
    """
    Takes generated .txt output and converts it into an aesthetic pdf.
    General Workflow of the project:
    1. Train model (train.py)
    2. Model -> generated txt file (articanon.py)
    3. generated txt file -> final pdf (book.py)
    Note that articanon.Articanon should handle most interactions with this code automatically.
    """
    def book_cover(self):
        """
        Assemble the book cover, using figures and fonts from the project folder.
        """
        self.add_font('EB Garamond', '', r"fonts/EBGaramond08-Regular.ttf", uni=True)
        self.set_font('EB Garamond', '', 30)
        self.set_xy(75, 20)
        self.cell(40, 10, "The Arti Canon")
        self.set_font('EB Garamond', '', 16)
        self.set_xy(87, 30)
        self.cell(40, 10, "by 209.51.170.10")
        self.image("./figures/articanon_cover1.jpg", x = 50.5, y = 60, w = 110, h = 180, type = '', link = '')


    def chapter_title(self, num, label):
        """
        Write chapter title in identifiable font.
        """
        self.add_font('EB Garamond', '', r"fonts/EBGaramond08-Regular.ttf", uni=True)
        self.set_font('EB Garamond', '', 15)
        self.set_fill_color(255, 255, 255)
        self.cell(1)
        self.cell(20, 10, 'Chapter %d' % (num), 0, 1, 'C', 1)
        self.set_font('EB Garamond', '', 30)
        self.cell(40)
        self.cell(30, 20, '%s' % (label), 0, 1, 'C', 1)
        self.ln(8)
        self.line(51, 50, 158.5, 50)

    def chapter_body(self, name):
        """
        Places the bulk of the generated text onto the page.
        """
        with open(name, 'rb') as fh:
            txt = fh.read().decode("UTF-8")
        self.set_font('EB Garamond', '', 12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font('EB Garamond', '')
        self.cell(0, 5, '(end of chapter)')

    def print_chapter(self, num, title, name):
        """
        Outputs one chapter of the articanon.
        """
        self.set_margins(50,16,50)
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

    def print_book_cover(self):
        """
        Add cover to pdf
        """
        self.add_page()
        self.book_cover()

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, ' %s' % self.page_no(), 0, 0, 'C')
