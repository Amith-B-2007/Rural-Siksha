"""
Add official NCERT textbook links to all resources
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from app import create_app
from extensions import db
from backend.models import Resource

# NCERT Resources - Official links
# Grade letters: a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10
# Class 6-10 have direct chapter PDFs

NCERT_LINKS = {
    # ==================== GRADE 1 ====================
    (1, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
        'numbers': ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
        'shapes': ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
        'time': ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
        'money': ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
    },
    (1, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        'body': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        'plants': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
    },
    (1, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?aeen1=0-10', 'Mridang Class 1'),
        'alphabet': ('https://ncert.nic.in/textbook.php?aeen1=0-10', 'Mridang Class 1'),
        'simple words': ('https://ncert.nic.in/textbook.php?aeen1=0-10', 'Mridang Class 1'),
    },
    (1, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        'family': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        'school': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        'helpers': ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
    },

    # ==================== GRADE 2 ====================
    (2, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?bejm1=0-15', 'Joyful Mathematics Class 2'),
        'addition': ('https://ncert.nic.in/textbook.php?bejm1=0-15', 'Joyful Mathematics Class 2'),
        'times tables': ('https://ncert.nic.in/textbook.php?bejm1=0-15', 'Joyful Mathematics Class 2'),
        'money': ('https://ncert.nic.in/textbook.php?bejm1=0-15', 'Joyful Mathematics Class 2'),
        'measurement': ('https://ncert.nic.in/textbook.php?bejm1=0-15', 'Joyful Mathematics Class 2'),
    },
    (2, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'plants': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'air water': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'senses': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'living': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
    },
    (2, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?been1=0-10', 'Mridang Class 2'),
        'nouns': ('https://ncert.nic.in/textbook.php?been1=0-10', 'Mridang Class 2'),
    },
    (2, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'neighbourhood': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
        'festivals': ('https://ncert.nic.in/textbook.php?bekt1=0-12', 'The World Around Us Class 2'),
    },

    # ==================== GRADE 3 ====================
    (3, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?cejm1=0-15', 'Math Mela Class 3'),
        'multiplication': ('https://ncert.nic.in/textbook.php?cejm1=0-15', 'Math Mela Class 3'),
        'time money': ('https://ncert.nic.in/textbook.php?cejm1=0-15', 'Math Mela Class 3'),
    },
    (3, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
        'living': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
        'states of matter': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
        'food': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
        'air water': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
    },
    (3, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?ceen1=0-10', 'Marigold Class 3'),
        'verbs': ('https://ncert.nic.in/textbook.php?ceen1=0-10', 'Marigold Class 3'),
        'stories': ('https://ncert.nic.in/textbook.php?ceen1=0-10', 'Marigold Class 3'),
    },
    (3, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
        'country india': ('https://ncert.nic.in/textbook.php?cekt1=0-12', 'Looking Around Class 3'),
    },

    # ==================== GRADE 4 ====================
    (4, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
        'division': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
        'fractions': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
        'geometry': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
        'numbers': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
        'roman': ('https://ncert.nic.in/textbook.php?dejm1=0-15', 'Math Mela Class 4'),
    },
    (4, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
        'nutrition': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
        'food': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
        'water': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
    },
    (4, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?deen1=0-10', 'Marigold Class 4'),
        'adjectives': ('https://ncert.nic.in/textbook.php?deen1=0-10', 'Marigold Class 4'),
    },
    (4, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
        'states': ('https://ncert.nic.in/textbook.php?dekt1=0-12', 'Looking Around Class 4'),
    },

    # ==================== GRADE 5 ====================
    (5, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?eemh1=0-14', 'Math-Magic Class 5'),
        'decimals': ('https://ncert.nic.in/textbook/pdf/eemh106.pdf', 'Math-Magic Ch 10: Tenths and Hundredths'),
        'percentages': ('https://ncert.nic.in/textbook/pdf/eemh106.pdf', 'Math-Magic Ch 10: Tenths and Hundredths'),
        'profit': ('https://ncert.nic.in/textbook.php?eemh1=0-14', 'Math-Magic Class 5'),
        'symmetry': ('https://ncert.nic.in/textbook.php?eemh1=0-14', 'Math-Magic Class 5'),
    },
    (5, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
        'body': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
        'plants': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
    },
    (5, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?eemt1=0-10', 'Marigold Class 5'),
        'tenses': ('https://ncert.nic.in/textbook.php?eemt1=0-10', 'Marigold Class 5'),
    },
    (5, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
        'freedom': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
        'religions': ('https://ncert.nic.in/textbook.php?eeap1=0-22', 'Looking Around Class 5'),
    },

    # ==================== GRADE 6 ====================
    (6, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?femh1=0-14', 'Mathematics Class 6'),
        'integers': ('https://ncert.nic.in/textbook/pdf/femh106.pdf', 'Chapter 6: Integers'),
        'numbers': ('https://ncert.nic.in/textbook/pdf/femh101.pdf', 'Chapter 1: Knowing Our Numbers'),
        'geometry': ('https://ncert.nic.in/textbook/pdf/femh104.pdf', 'Chapter 4: Basic Geometrical Ideas'),
        'fractions': ('https://ncert.nic.in/textbook/pdf/femh107.pdf', 'Chapter 7: Fractions'),
        'ratio': ('https://ncert.nic.in/textbook.php?femh1=0-14', 'Mathematics Class 6'),
    },
    (6, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?fesc1=0-16', 'Science Class 6'),
        'food': ('https://ncert.nic.in/textbook/pdf/fesc102.pdf', 'Chapter 2: Components of Food'),
        'components of food': ('https://ncert.nic.in/textbook/pdf/fesc102.pdf', 'Chapter 2: Components of Food'),
    },
    (6, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?feen1=0-10', 'Honeysuckle Class 6'),
        'articles': ('https://ncert.nic.in/textbook.php?feen1=0-10', 'Honeysuckle Class 6'),
        'pronouns': ('https://ncert.nic.in/textbook.php?feen1=0-10', 'Honeysuckle Class 6'),
        'reading': ('https://ncert.nic.in/textbook.php?feen1=0-10', 'Honeysuckle Class 6'),
    },
    (6, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?fess1=0-12', 'Social Studies Class 6'),
        'earth': ('https://ncert.nic.in/textbook.php?fess1=0-12', 'Social Studies Class 6'),
        'solar system': ('https://ncert.nic.in/textbook.php?fess1=0-12', 'Social Studies Class 6'),
    },

    # ==================== GRADE 7 ====================
    (7, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?gemh1=0-15', 'Mathematics Class 7'),
        'integers': ('https://ncert.nic.in/textbook/pdf/gemh101.pdf', 'Chapter 1: Integers'),
        'fractions': ('https://ncert.nic.in/textbook/pdf/gemh102.pdf', 'Chapter 2: Fractions and Decimals'),
        'algebra': ('https://ncert.nic.in/textbook/pdf/gemh112.pdf', 'Chapter 12: Algebraic Expressions'),
        'algebraic': ('https://ncert.nic.in/textbook/pdf/gemh112.pdf', 'Chapter 12: Algebraic Expressions'),
    },
    (7, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?gesc1=0-18', 'Science Class 7'),
        'acids': ('https://ncert.nic.in/textbook/pdf/gesc105.pdf', 'Chapter 5: Acids, Bases and Salts'),
        'bases': ('https://ncert.nic.in/textbook/pdf/gesc105.pdf', 'Chapter 5: Acids, Bases and Salts'),
        'salts': ('https://ncert.nic.in/textbook/pdf/gesc105.pdf', 'Chapter 5: Acids, Bases and Salts'),
        'heat': ('https://ncert.nic.in/textbook/pdf/gesc104.pdf', 'Chapter 4: Heat'),
        'nutrition': ('https://ncert.nic.in/textbook/pdf/gesc101.pdf', 'Chapter 1: Nutrition in Plants'),
    },
    (7, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?geen1=0-10', 'Honeycomb Class 7'),
        'active': ('https://ncert.nic.in/textbook.php?geen1=0-10', 'Honeycomb Class 7'),
        'passive': ('https://ncert.nic.in/textbook.php?geen1=0-10', 'Honeycomb Class 7'),
    },
    (7, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?gess3=0-10', 'Our Pasts Class 7'),
        'medieval': ('https://ncert.nic.in/textbook.php?gess3=0-10', 'Our Pasts Class 7'),
    },

    # ==================== GRADE 8 ====================
    (8, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?hemh1=0-13', 'Mathematics Class 8'),
        'rational': ('https://ncert.nic.in/textbook/pdf/hemh101.pdf', 'Chapter 1: Rational Numbers'),
        'linear': ('https://ncert.nic.in/textbook/pdf/hemh102.pdf', 'Chapter 2: Linear Equations'),
        'mensuration': ('https://ncert.nic.in/textbook/pdf/hemh111.pdf', 'Chapter 11: Mensuration'),
        'data handling': ('https://ncert.nic.in/textbook/pdf/hemh105.pdf', 'Chapter 5: Data Handling'),
        'compound interest': ('https://ncert.nic.in/textbook/pdf/hemh108.pdf', 'Chapter 8: Comparing Quantities'),
    },
    (8, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?hesc1=0-18', 'Science Class 8'),
        'force': ('https://ncert.nic.in/textbook/pdf/hesc108.pdf', 'Chapter 8: Force and Pressure'),
        'pressure': ('https://ncert.nic.in/textbook/pdf/hesc108.pdf', 'Chapter 8: Force and Pressure'),
        'friction': ('https://ncert.nic.in/textbook/pdf/hesc109.pdf', 'Chapter 9: Friction'),
    },
    (8, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?heen1=0-10', 'Honeydew Class 8'),
        'speech': ('https://ncert.nic.in/textbook.php?heen1=0-10', 'Honeydew Class 8'),
        'reading comprehension': ('https://ncert.nic.in/textbook.php?heen1=0-10', 'Honeydew Class 8'),
    },
    (8, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?hess1=0-11', 'Social Studies Class 8'),
        'constitution': ('https://ncert.nic.in/textbook.php?hess3=0-10', 'Social and Political Life Class 8'),
        'government': ('https://ncert.nic.in/textbook.php?hess3=0-10', 'Social and Political Life Class 8'),
    },

    # ==================== GRADE 9 ====================
    (9, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?iemh1=0-15', 'Mathematics Class 9'),
        'polynomials': ('https://ncert.nic.in/textbook/pdf/iemh102.pdf', 'Chapter 2: Polynomials'),
        'coordinate geometry': ('https://ncert.nic.in/textbook/pdf/iemh103.pdf', 'Chapter 3: Coordinate Geometry'),
        'linear equations': ('https://ncert.nic.in/textbook/pdf/iemh104.pdf', 'Chapter 4: Linear Equations in Two Variables'),
        'linear equations in two variables': ('https://ncert.nic.in/textbook/pdf/iemh104.pdf', 'Chapter 4: Linear Equations in Two Variables'),
    },
    (9, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?iesc1=0-15', 'Science Class 9'),
        'matter': ('https://ncert.nic.in/textbook/pdf/iesc101.pdf', 'Chapter 1: Matter in Our Surroundings'),
        'atoms': ('https://ncert.nic.in/textbook/pdf/iesc103.pdf', 'Chapter 3: Atoms and Molecules'),
        'molecules': ('https://ncert.nic.in/textbook/pdf/iesc103.pdf', 'Chapter 3: Atoms and Molecules'),
    },
    (9, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?ieen1=0-10', 'Beehive Class 9'),
        'sentence': ('https://ncert.nic.in/textbook.php?ieen1=0-10', 'Beehive Class 9'),
        'literature': ('https://ncert.nic.in/textbook.php?ieen1=0-10', 'Beehive Class 9'),
    },
    (9, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?iess3=0-8', 'India and Contemporary World Class 9'),
        'french revolution': ('https://ncert.nic.in/textbook.php?iess3=0-8', 'India and Contemporary World Class 9'),
    },

    # ==================== GRADE 10 ====================
    (10, 'Mathematics'): {
        'default': ('https://ncert.nic.in/textbook.php?jemh1=0-15', 'Mathematics Class 10'),
        'trigonometry': ('https://ncert.nic.in/textbook/pdf/jemh108.pdf', 'Chapter 8: Introduction to Trigonometry'),
        'quadratic': ('https://ncert.nic.in/textbook/pdf/jemh104.pdf', 'Chapter 4: Quadratic Equations'),
        'statistics': ('https://ncert.nic.in/textbook/pdf/jemh114.pdf', 'Chapter 14: Statistics'),
        'probability': ('https://ncert.nic.in/textbook/pdf/jemh115.pdf', 'Chapter 15: Probability'),
        'coordinate': ('https://ncert.nic.in/textbook/pdf/jemh107.pdf', 'Chapter 7: Coordinate Geometry'),
    },
    (10, 'Science'): {
        'default': ('https://ncert.nic.in/textbook.php?jesc1=0-13', 'Science Class 10'),
        'chemical reactions': ('https://ncert.nic.in/textbook/pdf/jesc101.pdf', 'Chapter 1: Chemical Reactions and Equations'),
        'life processes': ('https://ncert.nic.in/textbook/pdf/jesc106.pdf', 'Chapter 6: Life Processes'),
        'electricity': ('https://ncert.nic.in/textbook/pdf/jesc112.pdf', 'Chapter 12: Electricity'),
        'magnetism': ('https://ncert.nic.in/textbook/pdf/jesc113.pdf', 'Chapter 13: Magnetic Effects of Current'),
        'light': ('https://ncert.nic.in/textbook/pdf/jesc110.pdf', 'Chapter 10: Light - Reflection and Refraction'),
        'reflection': ('https://ncert.nic.in/textbook/pdf/jesc110.pdf', 'Chapter 10: Light - Reflection and Refraction'),
        'refraction': ('https://ncert.nic.in/textbook/pdf/jesc110.pdf', 'Chapter 10: Light - Reflection and Refraction'),
    },
    (10, 'English'): {
        'default': ('https://ncert.nic.in/textbook.php?jeff1=0-10', 'First Flight Class 10'),
        'letter writing': ('https://ncert.nic.in/textbook.php?jeff1=0-10', 'First Flight Class 10'),
        'reading comprehension': ('https://ncert.nic.in/textbook.php?jeff1=0-10', 'First Flight Class 10'),
    },
    (10, 'Social Studies'): {
        'default': ('https://ncert.nic.in/textbook.php?jess3=0-8', 'India and Contemporary World Class 10'),
        'nationalism': ('https://ncert.nic.in/textbook.php?jess3=0-8', 'India and Contemporary World Class 10'),
    },
}


def find_ncert_link(grade, subject, title):
    """Find best NCERT link for a resource"""
    key = (grade, subject)
    if key not in NCERT_LINKS:
        # Fallback to general NCERT page
        return ('https://ncert.nic.in/textbook.php',
                f'NCERT {subject} Class {grade}')

    topic_map = NCERT_LINKS[key]
    title_lower = title.lower()

    # Look for keyword match (longest first)
    sorted_keys = sorted([k for k in topic_map.keys() if k != 'default'], key=len, reverse=True)
    for keyword in sorted_keys:
        if keyword in title_lower:
            return topic_map[keyword]

    # Use default for this grade/subject
    return topic_map['default']


def add_ncert_links():
    app = create_app('development')
    with app.app_context():
        # Add columns if they don't exist
        try:
            db.session.execute(text("ALTER TABLE resources ADD COLUMN ncert_url VARCHAR(500)"))
            db.session.commit()
            print("[OK] Added ncert_url column")
        except Exception as e:
            db.session.rollback()
            print(f"[INFO] ncert_url: {str(e)[:60]}")

        try:
            db.session.execute(text("ALTER TABLE resources ADD COLUMN ncert_chapter VARCHAR(200)"))
            db.session.commit()
            print("[OK] Added ncert_chapter column")
        except Exception as e:
            db.session.rollback()
            print(f"[INFO] ncert_chapter: {str(e)[:60]}")

        print("\nAdding NCERT links to all resources...")
        print("=" * 60)

        resources = Resource.query.all()
        updated = 0

        for r in resources:
            ncert_url, ncert_chapter = find_ncert_link(r.grade_level, r.subject, r.title)
            r.ncert_url = ncert_url
            r.ncert_chapter = ncert_chapter
            updated += 1
            print(f"[OK] Grade {r.grade_level} {r.subject}: {r.title}")
            print(f"     -> {ncert_chapter}")

        db.session.commit()
        print("\n" + "=" * 60)
        print(f"Updated {updated} resources with NCERT links")
        print("=" * 60)


if __name__ == '__main__':
    try:
        add_ncert_links()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
