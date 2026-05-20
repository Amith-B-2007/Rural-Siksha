"""
Fix PDFs with full content and add YouTube links to resources
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from sqlalchemy import text
from app import create_app
from extensions import db
from backend.models import Resource, QuestionPaper, User

# YouTube video links for various topics
# Mapped by keywords in title/description
YOUTUBE_LINKS = {
    # Math topics
    'numbers': ('https://www.youtube.com/watch?v=Q4o_M-yJZJk', 'Magnet Brains'),
    'addition': ('https://www.youtube.com/watch?v=AuX7nPBqDts', 'Math & Learning'),
    'subtraction': ('https://www.youtube.com/watch?v=fmwxQ-9TRoo', 'Magnet Brains'),
    'multiplication': ('https://www.youtube.com/watch?v=mvOkMYCABGc', 'Math Antics'),
    'division': ('https://www.youtube.com/watch?v=KGMf314LUc0', 'Math Antics'),
    'fractions': ('https://www.youtube.com/watch?v=AC-2WBP8t3o', 'Math Antics'),
    'decimals': ('https://www.youtube.com/watch?v=BItpeFXC4vA', 'Math Antics'),
    'percentages': ('https://www.youtube.com/watch?v=JeVSmq1Nrpw', 'Math Antics'),
    'percentage': ('https://www.youtube.com/watch?v=JeVSmq1Nrpw', 'Math Antics'),
    'algebra': ('https://www.youtube.com/watch?v=NybHckSEQBI', 'Khan Academy'),
    'algebraic': ('https://www.youtube.com/watch?v=NybHckSEQBI', 'Khan Academy'),
    'geometry': ('https://www.youtube.com/watch?v=302eJ3TzJQU', 'Math Antics'),
    'trigonometry': ('https://www.youtube.com/watch?v=mhd9FXYdf4s', 'The Organic Chemistry Tutor'),
    'integers': ('https://www.youtube.com/watch?v=eVMQAKfPyAA', 'Magnet Brains'),
    'polynomials': ('https://www.youtube.com/watch?v=8FagFcT-NJM', 'Magnet Brains'),
    'quadratic': ('https://www.youtube.com/watch?v=2ZzuZvz33X0', 'Khan Academy'),
    'coordinate': ('https://www.youtube.com/watch?v=Lp1xrwJxLxc', 'Magnet Brains'),
    'shapes': ('https://www.youtube.com/watch?v=OBVGLDmtJfQ', 'Pebbles'),
    'symmetry': ('https://www.youtube.com/watch?v=ScuHzCsZkAo', 'Magnet Brains'),
    'mensuration': ('https://www.youtube.com/watch?v=AAY1bsazcgM', 'Magnet Brains'),
    'time': ('https://www.youtube.com/watch?v=Wgi3KOR0a1c', 'Smile and Learn'),
    'money': ('https://www.youtube.com/watch?v=4MEgs-Pn9HM', 'Pebbles'),
    'measurement': ('https://www.youtube.com/watch?v=GdfqWqUbVZw', 'Pebbles'),
    'rational': ('https://www.youtube.com/watch?v=zKaJqEYC1bM', 'Magnet Brains'),
    'linear': ('https://www.youtube.com/watch?v=ZSk_PpfHnZw', 'Magnet Brains'),
    'statistics': ('https://www.youtube.com/watch?v=MXaJ7sa7q-8', 'Magnet Brains'),
    'probability': ('https://www.youtube.com/watch?v=4y_nmpv-9lI', 'Khan Academy'),
    'data handling': ('https://www.youtube.com/watch?v=MXaJ7sa7q-8', 'Magnet Brains'),
    'large numbers': ('https://www.youtube.com/watch?v=qrqj7g0DwHs', 'Magnet Brains'),
    'place value': ('https://www.youtube.com/watch?v=qrqj7g0DwHs', 'Magnet Brains'),

    # Science topics
    'plant': ('https://www.youtube.com/watch?v=p3St51F4kE8', 'Peekaboo Kidz'),
    'plants': ('https://www.youtube.com/watch?v=p3St51F4kE8', 'Peekaboo Kidz'),
    'photosynthesis': ('https://www.youtube.com/watch?v=8Cd6BiXuyXk', 'Amoeba Sisters'),
    'animals': ('https://www.youtube.com/watch?v=v3NQ72wOFt8', 'Peekaboo Kidz'),
    'body': ('https://www.youtube.com/watch?v=cWNF8YErOJg', 'Peekaboo Kidz'),
    'human body': ('https://www.youtube.com/watch?v=cWNF8YErOJg', 'Peekaboo Kidz'),
    'food': ('https://www.youtube.com/watch?v=MepFD0fS3Cw', 'Magnet Brains'),
    'nutrition': ('https://www.youtube.com/watch?v=MepFD0fS3Cw', 'Magnet Brains'),
    'water': ('https://www.youtube.com/watch?v=PoEhwLpaTrk', 'Magnet Brains'),
    'water cycle': ('https://www.youtube.com/watch?v=PoEhwLpaTrk', 'Magnet Brains'),
    'air': ('https://www.youtube.com/watch?v=K-8t8KMUm6E', 'Magnet Brains'),
    'weather': ('https://www.youtube.com/watch?v=2bzZGNl5VuY', 'Pebbles'),
    'living': ('https://www.youtube.com/watch?v=A6cb2cJWl4w', 'Magnet Brains'),
    'matter': ('https://www.youtube.com/watch?v=eVKlGZbBpcQ', 'Magnet Brains'),
    'states of matter': ('https://www.youtube.com/watch?v=eVKlGZbBpcQ', 'Magnet Brains'),
    'force': ('https://www.youtube.com/watch?v=t9pXkmoqkic', 'Magnet Brains'),
    'pressure': ('https://www.youtube.com/watch?v=t9pXkmoqkic', 'Magnet Brains'),
    'friction': ('https://www.youtube.com/watch?v=Bpdei5VG6Q4', 'Magnet Brains'),
    'acid': ('https://www.youtube.com/watch?v=BgKwSWyU2QU', 'Magnet Brains'),
    'acids': ('https://www.youtube.com/watch?v=BgKwSWyU2QU', 'Magnet Brains'),
    'base': ('https://www.youtube.com/watch?v=BgKwSWyU2QU', 'Magnet Brains'),
    'salts': ('https://www.youtube.com/watch?v=BgKwSWyU2QU', 'Magnet Brains'),
    'chemical': ('https://www.youtube.com/watch?v=jFNWaSGipoY', 'Magnet Brains'),
    'reaction': ('https://www.youtube.com/watch?v=jFNWaSGipoY', 'Magnet Brains'),
    'life processes': ('https://www.youtube.com/watch?v=lXBCpkYrPdU', 'Magnet Brains'),
    'electricity': ('https://www.youtube.com/watch?v=ru032Mfsfig', 'Magnet Brains'),
    'magnetism': ('https://www.youtube.com/watch?v=tFzqAEZnDt8', 'Magnet Brains'),
    'reproduction': ('https://www.youtube.com/watch?v=A21nyMhSDi8', 'Peekaboo Kidz'),
    'components of food': ('https://www.youtube.com/watch?v=MepFD0fS3Cw', 'Magnet Brains'),

    # English topics
    'alphabet': ('https://www.youtube.com/watch?v=hq3yfQnllfQ', 'Cocomelon'),
    'noun': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'nouns': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'verb': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'verbs': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'adjective': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'adjectives': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
    'pronoun': ('https://www.youtube.com/watch?v=4N4hpsX2Up4', 'Magnet Brains'),
    'pronouns': ('https://www.youtube.com/watch?v=4N4hpsX2Up4', 'Magnet Brains'),
    'tense': ('https://www.youtube.com/watch?v=PqZpvJoGyk0', 'Magnet Brains'),
    'tenses': ('https://www.youtube.com/watch?v=PqZpvJoGyk0', 'Magnet Brains'),
    'simple words': ('https://www.youtube.com/watch?v=BELlZKpi1Zs', 'Pebbles'),
    'active': ('https://www.youtube.com/watch?v=mE1KmwUMQ3w', 'Magnet Brains'),
    'passive': ('https://www.youtube.com/watch?v=mE1KmwUMQ3w', 'Magnet Brains'),
    'reading': ('https://www.youtube.com/watch?v=BELlZKpi1Zs', 'Magnet Brains'),
    'sentence': ('https://www.youtube.com/watch?v=BIAS0bWZP9I', 'Magnet Brains'),
    'articles': ('https://www.youtube.com/watch?v=Zr_4Nm0L7DM', 'Magnet Brains'),
    'letter writing': ('https://www.youtube.com/watch?v=A-iLkbdvK_Q', 'Magnet Brains'),
    'speech': ('https://www.youtube.com/watch?v=PXNzZxJWy_4', 'Magnet Brains'),
    'stories': ('https://www.youtube.com/watch?v=ZpwQAGfqgEU', 'T-Series Kids Hut'),

    # Social Studies
    'family': ('https://www.youtube.com/watch?v=FHaObkHEkHQ', 'Pebbles'),
    'school': ('https://www.youtube.com/watch?v=W6IIyMC3M9w', 'Pebbles'),
    'india': ('https://www.youtube.com/watch?v=8VyB8Q5dKog', 'Magnet Brains'),
    'states of india': ('https://www.youtube.com/watch?v=8VyB8Q5dKog', 'Magnet Brains'),
    'freedom': ('https://www.youtube.com/watch?v=ZP4ggcG6GgU', 'Magnet Brains'),
    'gandhi': ('https://www.youtube.com/watch?v=YJ5kCLSwOdY', 'Magnet Brains'),
    'constitution': ('https://www.youtube.com/watch?v=zXxxqxhWvyM', 'Magnet Brains'),
    'government': ('https://www.youtube.com/watch?v=zXxxqxhWvyM', 'Magnet Brains'),
    'medieval': ('https://www.youtube.com/watch?v=Mug7HZl-jHA', 'Magnet Brains'),
    'mughal': ('https://www.youtube.com/watch?v=Mug7HZl-jHA', 'Magnet Brains'),
    'french revolution': ('https://www.youtube.com/watch?v=lTTvKwCylFY', 'Magnet Brains'),
    'nationalism': ('https://www.youtube.com/watch?v=ZP4ggcG6GgU', 'Magnet Brains'),
    'solar system': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Pebbles'),
    'earth': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Pebbles'),
    'planets': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Pebbles'),
    'religions': ('https://www.youtube.com/watch?v=AOyULDgJyAY', 'Educational'),
    'festivals': ('https://www.youtube.com/watch?v=tjsv4Yzj1Xc', 'Pebbles'),
    'neighbourhood': ('https://www.youtube.com/watch?v=zR1eBeIChEU', 'Pebbles'),
    'country': ('https://www.youtube.com/watch?v=8VyB8Q5dKog', 'Magnet Brains'),
}

# Default YouTube link by subject
DEFAULT_LINKS = {
    'Mathematics': ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'),
    'Science': ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'),
    'English': ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'),
    'Social Studies': ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'),
}


def find_youtube_link(title, subject):
    """Find best YouTube link for a resource"""
    title_lower = title.lower()

    # Check by keywords (longest match first)
    sorted_keys = sorted(YOUTUBE_LINKS.keys(), key=len, reverse=True)
    for keyword in sorted_keys:
        if keyword in title_lower:
            return YOUTUBE_LINKS[keyword]

    # Default by subject
    return DEFAULT_LINKS.get(subject, ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'))


def sanitize_text(text):
    """Aggressively sanitize text for PDF"""
    if not text:
        return ''

    # Comprehensive character replacement
    replacements = {
        # Math symbols
        '×': 'x', '÷': '/', '−': '-', '±': '+/-', '≠': '!=',
        '≤': '<=', '≥': '>=', '≈': '~=',
        '°': ' deg', '²': '2', '³': '3', '√': 'sqrt',
        '½': '1/2', '¼': '1/4', '¾': '3/4', '⅓': '1/3', '⅔': '2/3',
        'π': 'pi', '∞': 'inf', '∑': 'sum', '∫': 'integral',
        'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta',
        'θ': 'theta', 'λ': 'lambda', 'μ': 'mu', 'σ': 'sigma',
        # Subscripts/superscripts
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
        '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        '⁰': '0', '¹': '1', '⁴': '4', '⁵': '5',
        # Currency
        '₹': 'Rs.', '$': '$', '€': 'EUR', '£': 'GBP',
        # Punctuation
        '–': '-', '—': '-',
        '"': '"', '"': '"', '«': '"', '»': '"',
        "'": "'", "'": "'",
        '…': '...', '•': '*', '·': '*',
        # Arrows
        '→': '->', '←': '<-', '↑': '^', '↓': 'v',
        '⇒': '=>', '⇐': '<=', '↔': '<->',
        # Common chemicals - already done in models content
        # Spaces
        ' ': ' ',  # non-breaking space
        '​': '',   # zero-width space
        '‌': '',
        '‍': '',
        '﻿': '',   # BOM
        # Emojis (just remove)
        '🎓': '', '📚': '', '📝': '', '📐': '', '🔬': '',
        '📖': '', '🌍': '', '🤖': '', '💭': '', '📊': '',
        '📄': '', '✓': '*', '❓': '?', '✗': 'x', '⭐': '*',
        '🍎': '[apple]', '🐱': '[cat]', '⚽': '[ball]',
        '🌸': '[flower]', '🌟': '[star]', '😀': '', '😊': '',
        '🚀': '', '✅': '[OK]', '⚠️': '[WARN]', '⚡': '',
        '🔵': '[circle]', '⬛': '[square]', '🔺': '[triangle]',
        '⬜': '[square]', '⚪': '[circle]',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Final fallback - replace any remaining non-ASCII chars
    result = []
    for c in text:
        if ord(c) < 128:
            result.append(c)
        else:
            try:
                result.append(c.encode('latin-1').decode('latin-1'))
            except (UnicodeEncodeError, UnicodeDecodeError):
                result.append('?')

    return ''.join(result)


class BetterPDF(FPDF):
    """PDF with better content rendering"""

    def __init__(self, title='', subject='', grade=0):
        super().__init__()
        self.doc_title = sanitize_text(title)[:80]
        self.doc_subject = sanitize_text(subject)
        self.doc_grade = grade
        self.set_margins(left=15, top=15, right=15)
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        # Top bar
        self.set_fill_color(79, 70, 229)
        self.rect(0, 0, 210, 8, 'F')

        self.set_y(12)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 5, 'Rural Siksha - NCERT Learning', new_x='LMARGIN', new_y='NEXT', align='L')

        # Title
        self.set_y(18)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, self.doc_title, new_x='LMARGIN', new_y='NEXT', align='L')

        if self.doc_subject and self.doc_grade:
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
        self.cell(0, 10, f'Rural Siksha - Page {self.page_no()}', align='C')

    def render_content(self, content):
        """Render content with proper formatting and wrapping"""
        content = sanitize_text(content)
        lines = content.split('\n')

        for raw_line in lines:
            line = raw_line.strip()

            if not line:
                self.ln(2)
                continue

            # Determine style
            is_heading = False
            is_subheading = False
            is_bullet = False

            # Main heading (ALL CAPS, short)
            if line.isupper() and len(line) <= 70 and not any(c in line for c in ['=', '|']):
                is_heading = True
            # Sub-heading (ends with :)
            elif line.endswith(':') and len(line) <= 60:
                is_subheading = True
            # Bullet point
            elif line.startswith('-') or line.startswith('*') or line.startswith('•'):
                is_bullet = True

            try:
                if is_heading:
                    self.ln(2)
                    self.set_font('Helvetica', 'B', 12)
                    self.set_text_color(79, 70, 229)
                    self.multi_cell(0, 6, line)
                    self.ln(1)
                elif is_subheading:
                    self.set_font('Helvetica', 'B', 10)
                    self.set_text_color(30, 41, 59)
                    self.multi_cell(0, 5, line)
                else:
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)

                    # Break very long lines to prevent overflow
                    if len(line) > 100:
                        # Split into chunks
                        words = line.split(' ')
                        current = ''
                        for word in words:
                            # Even single words might be too long
                            if len(word) > 90:
                                if current:
                                    self.multi_cell(0, 5, current)
                                    current = ''
                                # Break up long word
                                while len(word) > 90:
                                    self.multi_cell(0, 5, word[:90])
                                    word = word[90:]
                                current = word
                            elif len(current) + len(word) + 1 > 100:
                                self.multi_cell(0, 5, current)
                                current = word
                            else:
                                current = current + ' ' + word if current else word
                        if current:
                            self.multi_cell(0, 5, current)
                    else:
                        self.multi_cell(0, 5, line)
            except Exception as e:
                # Last resort - try aggressive cleaning
                try:
                    cleaned = ''.join(c for c in line if c.isascii() and ord(c) >= 32)
                    if cleaned:
                        self.set_font('Helvetica', '', 10)
                        self.set_text_color(15, 23, 42)
                        self.multi_cell(0, 5, cleaned[:200])
                except:
                    pass


def text_to_pdf(text_path, pdf_path, title, subject, grade):
    """Convert text to PDF"""
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.strip():
            return False

        pdf = BetterPDF(title=title, subject=subject, grade=grade)
        pdf.add_page()
        pdf.render_content(content)
        pdf.output(pdf_path)
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def fix_all():
    app = create_app('development')
    with app.app_context():
        # Add youtube_url column if doesn't exist
        try:
            db.session.execute(text("ALTER TABLE resources ADD COLUMN youtube_url VARCHAR(500)"))
            db.session.commit()
            print("[OK] Added youtube_url column")
        except Exception as e:
            print(f"[INFO] youtube_url column may already exist: {str(e)[:80]}")
            db.session.rollback()

        try:
            db.session.execute(text("ALTER TABLE resources ADD COLUMN youtube_channel VARCHAR(100)"))
            db.session.commit()
            print("[OK] Added youtube_channel column")
        except Exception as e:
            print(f"[INFO] youtube_channel column may already exist: {str(e)[:80]}")
            db.session.rollback()

        print("\n" + "=" * 60)
        print("RECONVERTING ALL RESOURCES TO PDF WITH FULL CONTENT")
        print("=" * 60)

        resources = Resource.query.all()
        print(f"\nFound {len(resources)} resources\n")

        ok, fail = 0, 0

        for r in resources:
            # Find txt source
            txt_path = r.file_path
            if txt_path and not txt_path.endswith('.txt'):
                txt_path = txt_path.rsplit('.', 1)[0] + '.txt'

            if not txt_path or not os.path.exists(txt_path):
                # Try other extensions
                if r.file_path and os.path.exists(r.file_path):
                    txt_path = r.file_path
                else:
                    print(f"[SKIP] {r.title}: no source file")
                    fail += 1
                    continue

            # Generate PDF
            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'

            if text_to_pdf(txt_path, pdf_path, r.title, r.subject, r.grade_level):
                r.file_path = pdf_path
                r.content_type = 'pdf'
                r.file_size = os.path.getsize(pdf_path)

                # Add YouTube link
                yt_url, yt_channel = find_youtube_link(r.title, r.subject)
                r.youtube_url = yt_url
                r.youtube_channel = yt_channel

                ok += 1
                print(f"[OK] {r.title} ({yt_channel})")
            else:
                fail += 1

        db.session.commit()
        print(f"\n[DONE] Resources: {ok} OK, {fail} failed")

        # Also fix papers
        print("\n" + "=" * 60)
        print("RECONVERTING QUESTION PAPERS")
        print("=" * 60)

        papers = QuestionPaper.query.all()
        p_ok, p_fail = 0, 0

        for p in papers:
            txt_path = p.file_path
            if txt_path and not txt_path.endswith('.txt'):
                txt_path = txt_path.rsplit('.', 1)[0] + '.txt'

            if not txt_path or not os.path.exists(txt_path):
                if p.file_path and os.path.exists(p.file_path):
                    txt_path = p.file_path
                else:
                    print(f"[SKIP] {p.title}: no source")
                    p_fail += 1
                    continue

            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'

            if text_to_pdf(txt_path, pdf_path, p.title, p.subject, p.grade_level):
                p.file_path = pdf_path
                p.content_type = 'pdf'
                p.file_size = os.path.getsize(pdf_path)
                p_ok += 1
                print(f"[OK] {p.title}")
            else:
                p_fail += 1

        db.session.commit()
        print(f"\n[DONE] Papers: {p_ok} OK, {p_fail} failed")

        print(f"\n{'=' * 60}")
        print(f"GRAND TOTAL:")
        print(f"  Resources: {ok} PDFs (with YouTube links)")
        print(f"  Papers: {p_ok} PDFs")
        print(f"{'=' * 60}")


if __name__ == '__main__':
    try:
        fix_all()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
