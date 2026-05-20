"""
Convert all text resources and question papers to PDF format
Uses a robust approach to handle all content
"""

import sys
import os
import re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import Resource, QuestionPaper


def sanitize_text(text):
    """Make text safe for PDF rendering"""
    if not text:
        return ''

    # Replace unicode characters that can't be rendered
    replacements = {
        '–': '-', '—': '-', '"': '"', '"': '"',
        ''': "'", ''': "'", '…': '...', '•': '*',
        '×': 'x', '÷': '/', '≠': '!=', '≤': '<=', '≥': '>=',
        '°': ' deg', '²': '^2', '³': '^3', '√': 'sqrt',
        '½': '1/2', '¼': '1/4', '¾': '3/4',
        'π': 'pi', '∞': 'inf', 'α': 'alpha', 'β': 'beta',
        'θ': 'theta', '₀': '0', '₁': '1', '₂': '2', '₃': '3',
        '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        '🎓': '', '📚': '', '📝': '', '📐': '', '🔬': '', '📖': '',
        '🌍': '', '🤖': '', '💭': '', '📊': '', '📄': '', '✓': '*',
        '❓': '?', '✗': 'x', '⭐': '*', '🍎': '', '🐱': '', '⚽': '',
        '🌸': '', '🌟': '', '₹': 'Rs.', '😀': '', '😊': '', '🚀': '',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove any remaining non-latin1 characters
    try:
        text = text.encode('latin-1', 'replace').decode('latin-1')
    except:
        text = ''.join(c if ord(c) < 256 else '?' for c in text)

    return text


def break_long_lines(text, max_chars=85):
    """Break very long lines that won't fit on the page"""
    result = []
    for line in text.split('\n'):
        if len(line) <= max_chars:
            result.append(line)
        else:
            # Break at spaces if possible
            current = ''
            words = line.split(' ')
            for word in words:
                # If a single word is too long, break it
                if len(word) > max_chars:
                    if current:
                        result.append(current)
                        current = ''
                    while len(word) > max_chars:
                        result.append(word[:max_chars])
                        word = word[max_chars:]
                    current = word
                elif len(current) + len(word) + 1 <= max_chars:
                    current = current + ' ' + word if current else word
                else:
                    result.append(current)
                    current = word
            if current:
                result.append(current)
    return '\n'.join(result)


class NicePDF(FPDF):
    """Custom PDF with header and footer"""

    def __init__(self, title='Rural Siksha', subject='', grade=0):
        super().__init__()
        self.doc_title = sanitize_text(title)[:60]
        self.doc_subject = sanitize_text(subject)
        self.doc_grade = grade
        # Set wider margins to prevent overflow
        self.set_margins(left=15, top=15, right=15)

    def header(self):
        # Top color bar
        self.set_fill_color(79, 70, 229)
        self.rect(0, 0, 210, 8, 'F')

        # Brand
        self.set_y(12)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(79, 70, 229)
        self.cell(0, 5, 'Rural Siksha - NCERT Learning', new_x='LMARGIN', new_y='NEXT', align='L')

        # Title
        self.set_y(18)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(15, 23, 42)
        self.cell(0, 8, self.doc_title, new_x='LMARGIN', new_y='NEXT', align='L')

        # Subject and grade
        if self.doc_subject and self.doc_grade:
            self.set_font('Helvetica', '', 10)
            self.set_text_color(100, 116, 139)
            self.cell(0, 5, f'Subject: {self.doc_subject}  |  Grade: {self.doc_grade}', new_x='LMARGIN', new_y='NEXT', align='L')

        # Separator
        self.set_draw_color(229, 231, 235)
        self.line(10, 35, 200, 35)

        self.set_y(40)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Rural Siksha - Page {self.page_no()}', align='C')

    def add_content(self, content):
        """Add content with simple formatting"""
        content = sanitize_text(content)
        content = break_long_lines(content, max_chars=85)

        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()

            if not stripped:
                self.ln(3)
                continue

            try:
                # Check style based on content
                if stripped.isupper() and len(stripped) < 60 and not any(c in stripped for c in ['=', '*']):
                    # Main heading
                    self.ln(2)
                    self.set_font('Helvetica', 'B', 12)
                    self.set_text_color(79, 70, 229)
                    self.multi_cell(0, 6, stripped)
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                    self.ln(1)
                elif stripped.endswith(':') and len(stripped) < 50:
                    # Sub heading
                    self.set_font('Helvetica', 'B', 10)
                    self.set_text_color(30, 41, 59)
                    self.multi_cell(0, 5, stripped)
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                else:
                    # Normal text
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                    self.multi_cell(0, 5, stripped)
            except Exception as e:
                # If multi_cell fails, just skip this line
                print(f"  Warning: skipped line - {str(e)[:50]}")
                continue


def text_to_pdf(text_path, pdf_path, title, subject, grade):
    """Convert a text file to a PDF"""
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pdf = NicePDF(title=title, subject=subject, grade=grade)
        pdf.set_auto_page_break(auto=True, margin=20)
        pdf.add_page()
        pdf.add_content(content)
        pdf.output(pdf_path)
        return True
    except Exception as e:
        print(f"[ERROR] {text_path}: {e}")
        return False


def convert_all_resources():
    """Convert all text resources to PDFs"""
    app = create_app('development')
    with app.app_context():
        print("=" * 60)
        print("CONVERTING RESOURCES TO PDF")
        print("=" * 60)

        # Get all resources (both txt and pdf - re-convert if needed)
        resources = Resource.query.all()
        print(f"\nFound {len(resources)} resources\n")

        converted = 0
        failed = 0

        for r in resources:
            if not r.file_path:
                continue

            # Check if txt exists
            txt_path = r.file_path
            if not txt_path.endswith('.txt'):
                txt_path = r.file_path.rsplit('.', 1)[0] + '.txt'

            if not os.path.exists(txt_path):
                # Try original
                if not os.path.exists(r.file_path):
                    print(f"[SKIP] {r.title}: file not found")
                    failed += 1
                    continue
                txt_path = r.file_path

            # If already PDF and exists, skip
            if r.file_path.endswith('.pdf') and os.path.exists(r.file_path):
                continue

            # Generate PDF path
            pdf_path = txt_path.replace('.txt', '.pdf')

            # Convert
            if text_to_pdf(txt_path, pdf_path, r.title, r.subject, r.grade_level):
                r.file_path = pdf_path
                r.content_type = 'pdf'
                r.file_size = os.path.getsize(pdf_path)
                converted += 1
                print(f"[OK] {r.title}")
            else:
                failed += 1

        db.session.commit()
        print(f"\n[DONE] Resources: Converted {converted}, Failed {failed}")
        return converted, failed


def convert_all_papers():
    """Convert all question papers to PDFs"""
    app = create_app('development')
    with app.app_context():
        print("\n" + "=" * 60)
        print("CONVERTING QUESTION PAPERS TO PDF")
        print("=" * 60)

        papers = QuestionPaper.query.all()
        print(f"\nFound {len(papers)} papers\n")

        converted = 0
        failed = 0

        for p in papers:
            if not p.file_path:
                continue

            txt_path = p.file_path
            if not txt_path.endswith('.txt'):
                txt_path = p.file_path.rsplit('.', 1)[0] + '.txt'

            if not os.path.exists(txt_path):
                if not os.path.exists(p.file_path):
                    print(f"[SKIP] {p.title}: file not found")
                    failed += 1
                    continue
                txt_path = p.file_path

            if p.file_path.endswith('.pdf') and os.path.exists(p.file_path):
                continue

            pdf_path = txt_path.replace('.txt', '.pdf')

            if text_to_pdf(txt_path, pdf_path, p.title, p.subject, p.grade_level):
                p.file_path = pdf_path
                p.content_type = 'pdf'
                p.file_size = os.path.getsize(pdf_path)
                converted += 1
                print(f"[OK] {p.title}")
            else:
                failed += 1

        db.session.commit()
        print(f"\n[DONE] Papers: Converted {converted}, Failed {failed}")
        return converted, failed


if __name__ == '__main__':
    try:
        r_ok, r_fail = convert_all_resources()
        p_ok, p_fail = convert_all_papers()

        print("\n" + "=" * 60)
        print(f"TOTAL: {r_ok + p_ok} converted to PDF")
        print(f"FAILED: {r_fail + p_fail}")
        print("=" * 60)
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
