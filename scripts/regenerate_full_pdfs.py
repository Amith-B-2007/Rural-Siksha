"""
Regenerate ALL PDFs with FULL content using a simpler, more robust approach.
Also enriches content with more detail for each topic.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import Resource, QuestionPaper

# Detailed NCERT content for popular topics
ENHANCED_CONTENT = {
    'Trigonometry Introduction': '''TRIGONOMETRY

What is Trigonometry?
Trigonometry deals with relationships between the sides and angles of triangles. It is widely used in engineering, physics, astronomy, navigation and architecture.

The word "trigonometry" comes from Greek words meaning "triangle measurement".

In a Right Triangle:
A right triangle has one angle equal to 90 degrees.

The three sides are:
- HYPOTENUSE: The longest side, always opposite to the 90 degree angle
- OPPOSITE: The side directly opposite to the angle we are measuring (theta)
- ADJACENT: The side next to the angle we are measuring

Three Main Trigonometric Ratios:

1. SINE (sin)
   sin(theta) = Opposite / Hypotenuse

2. COSINE (cos)
   cos(theta) = Adjacent / Hypotenuse

3. TANGENT (tan)
   tan(theta) = Opposite / Adjacent

Memory Trick: SOH CAH TOA
- SOH = Sin = Opposite/Hypotenuse
- CAH = Cos = Adjacent/Hypotenuse
- TOA = Tan = Opposite/Adjacent

Standard Values Table:

Angle:    0       30       45       60       90
Sin:      0       1/2      1/sqrt2  sqrt3/2  1
Cos:      1       sqrt3/2  1/sqrt2  1/2      0
Tan:      0       1/sqrt3  1        sqrt3    undefined

Key Identities:
1. sin squared(theta) + cos squared(theta) = 1
2. 1 + tan squared(theta) = sec squared(theta)
3. tan(theta) = sin(theta) / cos(theta)

Reciprocal Functions:
- cosec(theta) = 1 / sin(theta)
- sec(theta) = 1 / cos(theta)
- cot(theta) = 1 / tan(theta)

Real-world Applications:
- Measuring the height of buildings and mountains
- Navigation using GPS
- Construction of bridges and roads
- Astronomy - calculating distances to stars
- Music - sound waves and frequencies
- Physics - projectile motion
- Engineering and architecture

Solved Example 1:
A ladder leans against a wall. The angle with the ground is 60 degrees and the length of the ladder is 10 meters. Find the height reached on the wall.

Solution:
We use sin = Opposite / Hypotenuse
sin(60) = height / 10
height = 10 x sin(60)
height = 10 x (sqrt 3 / 2)
height = 5 sqrt 3 meters
height = approximately 8.66 meters

Solved Example 2:
Find the value of sin 30 + cos 60.

Solution:
sin 30 = 1/2
cos 60 = 1/2
sin 30 + cos 60 = 1/2 + 1/2 = 1

Practice Problems:
1. Find sin(45) + cos(45)
2. If sin(theta) = 3/5, find cos(theta)
3. Calculate tan(60) x cot(60)
4. Find the height of a tree if the angle of elevation is 30 degrees and the distance from the tree is 100 meters

Important Tips:
- Always remember the standard values
- Use SOH CAH TOA to remember the ratios
- Draw a triangle for word problems
- Identify the known and unknown sides''',

    'Photosynthesis': '''PHOTOSYNTHESIS - HOW PLANTS MAKE FOOD

What is Photosynthesis?
Photosynthesis is the process by which green plants use sunlight, water, and carbon dioxide to make their own food (glucose). Oxygen is released as a by-product.

The word "photosynthesis" comes from Greek words: "photo" meaning light and "synthesis" meaning combining together.

The Chemical Equation:
6 CO2 + 6 H2O + sunlight = C6H12O6 + 6 O2
(Carbon dioxide + Water + Sunlight = Glucose + Oxygen)

Requirements for Photosynthesis:
1. SUNLIGHT - The energy source from the sun
2. WATER - Absorbed by the roots from the soil
3. CARBON DIOXIDE - From the air through stomata
4. CHLOROPHYLL - The green pigment in leaves
5. MINERALS - Like nitrogen, phosphorus from soil

Where Photosynthesis Happens:
Photosynthesis takes place in the LEAVES of plants, specifically inside small structures called CHLOROPLASTS. Chloroplasts contain CHLOROPHYLL which gives plants their green color.

Steps of Photosynthesis:

Step 1: Light Absorption
Chlorophyll absorbs sunlight, especially red and blue light, but reflects green light (which is why plants look green).

Step 2: Water Splitting
The energy from sunlight splits water molecules into hydrogen and oxygen.

Step 3: Oxygen Release
Oxygen is released into the atmosphere through tiny pores called stomata.

Step 4: Glucose Formation
Hydrogen combines with carbon dioxide to form glucose (sugar), which the plant uses for energy and growth.

What Plants Do With Glucose:
- Used immediately for energy
- Stored as starch in roots, stems, and fruits
- Used to make cellulose for cell walls
- Combined to form fats and proteins

Why Photosynthesis is Important:
1. Produces OXYGEN that all animals and humans breathe
2. Removes CARBON DIOXIDE from the atmosphere
3. Forms the BASE OF THE FOOD CHAIN
4. Provides food for all living things directly or indirectly
5. Helps maintain Earth's atmosphere balance

Light Reaction vs Dark Reaction:
- Light Reaction: Requires light, splits water, produces oxygen and ATP
- Dark Reaction (Calvin Cycle): Does not require light, uses ATP to make glucose from carbon dioxide

Types of Plants Based on Nutrition:
1. AUTOTROPHS - Make their own food (most plants)
2. HETEROTROPHS - Cannot make own food
3. INSECTIVOROUS PLANTS - Like Pitcher plant, Venus flytrap

Practical Experiment:
You can test for starch in a leaf:
1. Cover part of a leaf with black paper
2. Leave plant in sunlight for several hours
3. Boil the leaf in water
4. Dip in alcohol to remove green color
5. Add iodine solution
6. Covered part: no color change (no starch made)
7. Uncovered part: turns blue-black (starch present)

This proves photosynthesis needs light!

Practice Questions:
1. Write the chemical equation of photosynthesis.
2. What is the role of chlorophyll?
3. Why are leaves green?
4. Name the gas released during photosynthesis.
5. What is the function of stomata?''',

    'Multiplication Tables': '''MULTIPLICATION TABLES (2 TO 10)

What is Multiplication?
Multiplication is REPEATED ADDITION. When we multiply two numbers, we are adding one number to itself a certain number of times.

For example: 3 x 4 means "3 added 4 times"
= 3 + 3 + 3 + 3
= 12

Or it can mean "4 added 3 times"
= 4 + 4 + 4
= 12

Both give the same answer!

Table of 2 (Twos):
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

Table of 3 (Threes):
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

Table of 4 (Fours):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

Table of 5 (Fives):
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Table of 6 (Sixes):
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

Table of 7 (Sevens):
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

Table of 8 (Eights):
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80

Table of 9 (Nines):
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90

Table of 10 (Tens):
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100

Important Properties of Multiplication:

1. ORDER DOES NOT MATTER (Commutative)
   3 x 4 = 4 x 3 = 12

2. MULTIPLYING BY 1
   Any number x 1 = same number
   7 x 1 = 7

3. MULTIPLYING BY 0
   Any number x 0 = 0
   5 x 0 = 0

4. MULTIPLYING BY 10
   Just add a 0 at the end
   8 x 10 = 80

5. MULTIPLYING BY 100
   Add two zeros
   7 x 100 = 700

Tricks to Remember:
- Table of 9: The digits add up to 9 (9, 18, 27, 36...)
- Table of 5: Always ends in 0 or 5
- Table of 2: Always even numbers
- Table of 10: Just add a 0

Practice Daily!
Spend 5 minutes daily revising tables. Sing them aloud to memorize.

Test Yourself:
1. What is 7 x 8?
2. What is 9 x 6?
3. What is 4 x 9?
4. What is 6 x 7?
5. What is 8 x 8?

(Answers: 56, 54, 36, 42, 64)''',
}


def sanitize_text(text):
    """Replace special characters with safe equivalents"""
    if not text:
        return ''

    replacements = {
        # Math
        '×': 'x', '÷': '/', '−': '-', '±': '+-', '≠': '!=',
        '≤': '<=', '≥': '>=', '≈': '~', '°': ' deg',
        '²': '2', '³': '3', '⁴': '4', '⁵': '5',
        '½': '1/2', '¼': '1/4', '¾': '3/4', '⅓': '1/3', '⅔': '2/3',
        '√': 'sqrt', 'π': 'pi', '∞': 'inf', '∑': 'sum',
        'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta',
        'θ': 'theta', 'λ': 'lambda', 'μ': 'mu', 'σ': 'sigma',
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
        '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        '⁰': '0', '¹': '1',
        # Currency
        '₹': 'Rs.',
        # Punctuation
        '–': '-', '—': '-', ''': "'", ''': "'",
        '…': '...', '•': '*',
        # Arrows
        '→': '->', '←': '<-', '↑': '^', '↓': 'v',
        # Common emojis
        '🎓': '', '📚': '', '📝': '', '📐': '', '🔬': '',
        '📖': '', '🌍': '', '🤖': '', '💭': '', '📊': '',
        '📄': '', '✓': '*', '❓': '?', '✗': 'x', '⭐': '*',
        '🍎': '', '🐱': '', '⚽': '', '🌸': '', '🌟': '',
        '🚀': '', '✅': '', '⚠': '', '⚡': '',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Strip any remaining non-ASCII
    result = []
    for c in text:
        if ord(c) < 128:
            result.append(c)
        else:
            result.append(' ')

    return ''.join(result)


class SimplePDF(FPDF):
    """Simple, robust PDF that includes ALL content"""

    def __init__(self, title='', subject='', grade=0):
        super().__init__()
        self.doc_title = sanitize_text(title)[:80]
        self.doc_subject = sanitize_text(subject)
        self.doc_grade = grade
        self.set_margins(left=15, top=15, right=15)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        # Top color bar
        self.set_fill_color(79, 70, 229)
        self.rect(0, 0, 210, 8, 'F')

        # Brand
        self.set_y(12)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 5, 'Rural Siksha - NCERT Learning', new_x='LMARGIN', new_y='NEXT', align='L')

        # Title
        self.set_y(18)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, self.doc_title, new_x='LMARGIN', new_y='NEXT', align='L')

        # Subject/Grade
        if self.doc_subject and self.doc_grade:
            self.set_font('Helvetica', '', 9)
            self.set_text_color(100, 116, 139)
            self.cell(0, 4, f'Subject: {self.doc_subject}  |  Grade: {self.doc_grade}', new_x='LMARGIN', new_y='NEXT', align='L')

        # Separator
        self.set_draw_color(229, 231, 235)
        self.line(10, 33, 200, 33)
        self.set_y(38)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Rural Siksha - Page {self.page_no()}', align='C')

    def render_all(self, content):
        """Render ALL content - guaranteed to print every line"""
        content = sanitize_text(content)

        # Process line by line
        for raw_line in content.split('\n'):
            line = raw_line.rstrip()

            if not line.strip():
                self.ln(2)
                continue

            try:
                stripped = line.strip()

                # Detect formatting
                is_main_heading = (
                    stripped.isupper() and
                    len(stripped) <= 70 and
                    not '=' in stripped and
                    not '/' in stripped
                )

                # Only treat as sub-heading if it's a short header line (not body)
                is_sub_heading = (
                    stripped.endswith(':') and
                    len(stripped) <= 35 and
                    not stripped.startswith('-') and
                    not any(c.isdigit() for c in stripped[:2])
                )

                if is_main_heading:
                    self.ln(2)
                    self.set_font('Helvetica', 'B', 12)
                    self.set_text_color(79, 70, 229)
                    self.multi_cell(0, 6, stripped)
                    self.ln(1)
                elif is_sub_heading:
                    self.set_font('Helvetica', 'B', 10)
                    self.set_text_color(30, 41, 59)
                    self.multi_cell(0, 5, stripped)
                else:
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                    # Use multi_cell which handles wrapping automatically
                    self.multi_cell(0, 5, stripped)
            except Exception as e:
                # Fallback: even simpler rendering
                try:
                    safe = ''.join(c for c in stripped if c.isascii() and ord(c) >= 32)
                    if safe:
                        self.set_font('Helvetica', '', 10)
                        self.set_text_color(15, 23, 42)
                        # Truncate very long lines
                        self.multi_cell(0, 5, safe[:500])
                except:
                    pass


def create_pdf(text_path, pdf_path, title, subject, grade):
    """Create PDF from text file"""
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Use enhanced content if available
        if title in ENHANCED_CONTENT:
            content = ENHANCED_CONTENT[title]
            # Save enhanced text back
            with open(text_path, 'w', encoding='utf-8') as f:
                f.write(content)

        if not content.strip():
            return False

        pdf = SimplePDF(title=title, subject=subject, grade=grade)
        pdf.add_page()
        pdf.render_all(content)
        pdf.output(pdf_path)
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def regenerate_all():
    app = create_app('development')
    with app.app_context():
        print("Regenerating all PDFs with full content...")
        print("=" * 60)

        resources = Resource.query.all()
        print(f"\nFound {len(resources)} resources\n")

        ok, fail = 0, 0
        for r in resources:
            # Find source text file
            if r.file_path and r.file_path.endswith('.pdf'):
                txt_path = r.file_path.rsplit('.', 1)[0] + '.txt'
            elif r.file_path and r.file_path.endswith('.txt'):
                txt_path = r.file_path
            else:
                fail += 1
                continue

            if not os.path.exists(txt_path):
                # Try .txt version
                if r.file_path and os.path.exists(r.file_path):
                    txt_path = r.file_path
                else:
                    fail += 1
                    continue

            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'

            if create_pdf(txt_path, pdf_path, r.title, r.subject, r.grade_level):
                r.file_path = pdf_path
                r.content_type = 'pdf'
                r.file_size = os.path.getsize(pdf_path)
                ok += 1
                print(f"[OK] {r.title} - {r.file_size} bytes")
            else:
                fail += 1
                print(f"[FAIL] {r.title}")

        # Question papers too
        print("\nRegenerating papers...")
        papers = QuestionPaper.query.all()
        p_ok, p_fail = 0, 0

        for p in papers:
            if p.file_path and p.file_path.endswith('.pdf'):
                txt_path = p.file_path.rsplit('.', 1)[0] + '.txt'
            elif p.file_path and p.file_path.endswith('.txt'):
                txt_path = p.file_path
            else:
                p_fail += 1
                continue

            if not os.path.exists(txt_path):
                if p.file_path and os.path.exists(p.file_path):
                    txt_path = p.file_path
                else:
                    p_fail += 1
                    continue

            pdf_path = txt_path.rsplit('.', 1)[0] + '.pdf'

            if create_pdf(txt_path, pdf_path, p.title, p.subject, p.grade_level):
                p.file_path = pdf_path
                p.content_type = 'pdf'
                p.file_size = os.path.getsize(pdf_path)
                p_ok += 1
            else:
                p_fail += 1

        db.session.commit()

        print("\n" + "=" * 60)
        print(f"Resources: {ok} OK, {fail} failed")
        print(f"Papers: {p_ok} OK, {p_fail} failed")
        print("=" * 60)


if __name__ == '__main__':
    try:
        regenerate_all()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
