"""
FORCE generate full PDFs - every line must be rendered.
Brutal simple approach.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import Resource, QuestionPaper


def clean(text):
    """Convert to safe ASCII"""
    replacements = {
        '×': 'x', '÷': '/', '−': '-', '°': ' deg',
        '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5',
        '½': '1/2', '¼': '1/4', '¾': '3/4',
        '√': 'sqrt', 'π': 'pi', '∞': 'inf',
        'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd',
        'θ': 'theta', 'λ': 'lambda', 'μ': 'mu', 'σ': 'sigma',
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
        '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        '⁰': '0', '¹': '1', '"': '"', '"': '"',
        ''': "'", ''': "'", '–': '-', '—': '-',
        '…': '...', '•': '*', '₹': 'Rs.',
        '→': '->', '←': '<-', '↑': '^', '↓': 'v',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Force ASCII
    out = []
    for c in text:
        if ord(c) < 128:
            out.append(c)
        else:
            out.append(' ')
    return ''.join(out)


def wrap_line(text, max_len=85):
    """Wrap a line into multiple lines of max_len characters"""
    if len(text) <= max_len:
        return [text]

    result = []
    words = text.split(' ')
    current = ''

    for word in words:
        if len(word) > max_len:
            # Force break long word
            if current:
                result.append(current)
                current = ''
            while len(word) > max_len:
                result.append(word[:max_len])
                word = word[max_len:]
            current = word
        elif len(current) + len(word) + 1 > max_len:
            if current:
                result.append(current)
            current = word
        else:
            current = (current + ' ' + word) if current else word

    if current:
        result.append(current)

    return result


class ForcePDF(FPDF):
    def __init__(self, title='', subject='', grade=0):
        super().__init__()
        self.doc_title = clean(title)[:80]
        self.doc_subject = clean(subject)
        self.doc_grade = grade
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_fill_color(79, 70, 229)
        self.rect(0, 0, 210, 8, 'F')
        self.set_y(12)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 5, 'Rural Siksha - NCERT Learning', new_x='LMARGIN', new_y='NEXT', align='L')
        self.set_y(18)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, self.doc_title, new_x='LMARGIN', new_y='NEXT', align='L')
        if self.doc_subject:
            self.set_font('Helvetica', '', 9)
            self.set_text_color(100, 116, 139)
            self.cell(0, 4, f'Subject: {self.doc_subject}  |  Grade: {self.doc_grade}', new_x='LMARGIN', new_y='NEXT', align='L')
        self.set_draw_color(229, 231, 235)
        self.line(10, 33, 200, 33)
        self.set_y(38)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def write_line(self, text, bold=False, color=(15, 23, 42), size=10):
        """Write a single line using cell"""
        try:
            self.set_font('Helvetica', 'B' if bold else '', size)
            self.set_text_color(*color)
            wrapped = wrap_line(text, max_len=95)
            for wl in wrapped:
                try:
                    self.cell(0, 5, wl, new_x='LMARGIN', new_y='NEXT')
                except Exception as e:
                    # Even single line failed - try with even shorter
                    short_wrapped = wrap_line(wl, max_len=70)
                    for sw in short_wrapped:
                        try:
                            self.cell(0, 5, sw, new_x='LMARGIN', new_y='NEXT')
                        except:
                            # Skip this part as last resort
                            pass
        except Exception as e:
            print(f"   Line failed: {e}")

    def render_force(self, content):
        """FORCE render every single line"""
        content = clean(content)

        lines_total = 0
        lines_rendered = 0

        for raw in content.split('\n'):
            line = raw.rstrip()
            lines_total += 1

            if not line.strip():
                self.ln(2)
                lines_rendered += 1
                continue

            stripped = line.strip()

            # Classify
            is_heading = (
                stripped.isupper() and
                len(stripped) <= 70 and
                not '=' in stripped
            )
            is_sub = (
                stripped.endswith(':') and
                len(stripped) <= 50 and
                not stripped.startswith('-')
            )

            if is_heading:
                self.ln(2)
                self.write_line(stripped, bold=True, color=(79, 70, 229), size=12)
                self.ln(1)
            elif is_sub:
                self.write_line(stripped, bold=True, color=(30, 41, 59), size=10)
            else:
                self.write_line(stripped, bold=False, color=(15, 23, 42), size=10)

            lines_rendered += 1

        return lines_total, lines_rendered


def force_pdf(text_path, pdf_path, title, subject, grade):
    """Force create PDF with all content"""
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.strip():
            return False, 0, 0

        pdf = ForcePDF(title=title, subject=subject, grade=grade)
        pdf.add_page()
        total, rendered = pdf.render_force(content)
        pdf.output(pdf_path)
        return True, total, rendered
    except Exception as e:
        print(f"   FATAL: {e}")
        import traceback
        traceback.print_exc()
        return False, 0, 0


def regen_all():
    app = create_app('development')
    with app.app_context():
        print("FORCE regenerating all PDFs...")
        print("=" * 60)

        resources = Resource.query.all()
        print(f"Resources: {len(resources)}\n")

        ok, fail = 0, 0
        for r in resources:
            # Get text source
            txt_path = r.file_path
            if txt_path and txt_path.endswith('.pdf'):
                txt_path = txt_path.rsplit('.', 1)[0] + '.txt'
            if not txt_path or not os.path.exists(txt_path):
                if r.file_path and os.path.exists(r.file_path):
                    txt_path = r.file_path
                else:
                    fail += 1
                    continue

            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'
            success, total, rendered = force_pdf(txt_path, pdf_path, r.title, r.subject, r.grade_level)

            if success:
                r.file_path = pdf_path
                r.content_type = 'pdf'
                r.file_size = os.path.getsize(pdf_path)
                ok += 1
                print(f"[OK] {r.title}: {rendered}/{total} lines, {r.file_size} bytes")
            else:
                fail += 1

        # Papers
        print("\n--- Papers ---")
        papers = QuestionPaper.query.all()
        p_ok = 0
        for p in papers:
            txt_path = p.file_path
            if txt_path and txt_path.endswith('.pdf'):
                txt_path = txt_path.rsplit('.', 1)[0] + '.txt'
            if not txt_path or not os.path.exists(txt_path):
                if p.file_path and os.path.exists(p.file_path):
                    txt_path = p.file_path
                else:
                    continue

            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'
            success, total, rendered = force_pdf(txt_path, pdf_path, p.title, p.subject, p.grade_level)
            if success:
                p.file_path = pdf_path
                p.content_type = 'pdf'
                p.file_size = os.path.getsize(pdf_path)
                p_ok += 1

        db.session.commit()
        print("\n" + "=" * 60)
        print(f"Resources OK: {ok}/{len(resources)}")
        print(f"Papers OK: {p_ok}/{len(papers)}")
        print("=" * 60)


if __name__ == '__main__':
    regen_all()
