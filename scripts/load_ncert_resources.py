"""
Load NCERT-aligned text resources for grades 1-10
Creates text-based reading materials for offline access
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Resource

NCERT_RESOURCES = [
    # Grade 1
    {'title': 'Counting Numbers 1-100', 'subject': 'Mathematics', 'grade': 1,
     'desc': 'Learn to count from 1 to 100 with simple examples and pictures',
     'content': '''COUNTING NUMBERS 1 TO 100

Let's learn to count!

1, 2, 3, 4, 5, 6, 7, 8, 9, 10
11, 12, 13, 14, 15, 16, 17, 18, 19, 20

Counting in Tens:
10, 20, 30, 40, 50, 60, 70, 80, 90, 100

Number Names:
1 - One       11 - Eleven
2 - Two       12 - Twelve
3 - Three     13 - Thirteen
4 - Four      14 - Fourteen
5 - Five      15 - Fifteen
6 - Six       16 - Sixteen
7 - Seven     17 - Seventeen
8 - Eight     18 - Eighteen
9 - Nine      19 - Nineteen
10 - Ten      20 - Twenty

Practice: Count objects around you - how many fingers? How many books?'''},

    {'title': 'My Body Parts', 'subject': 'Science', 'grade': 1,
     'desc': 'Learn about the parts of our body',
     'content': '''MY BODY PARTS

Our body has many parts. Each part has a function.

HEAD: Has our brain inside. We use it to think.

EYES: We use eyes to SEE. We have 2 eyes.

EARS: We use ears to HEAR. We have 2 ears.

NOSE: We use nose to SMELL and BREATHE.

MOUTH: We use mouth to EAT and TALK.

HANDS: We have 2 hands. Each hand has 5 fingers.

LEGS: We have 2 legs. We use legs to WALK and RUN.

Keep your body clean!
- Wash hands before eating
- Brush teeth daily
- Take a bath every day
- Drink clean water'''},

    # Grade 2
    {'title': 'Addition Made Easy', 'subject': 'Mathematics', 'grade': 2,
     'desc': 'Step-by-step guide to addition',
     'content': '''ADDITION

Addition means putting together!

Example 1: 2 + 3 = 5
If you have 2 apples and get 3 more, you have 5 apples.

Addition Facts:
1 + 1 = 2
2 + 2 = 4
3 + 3 = 6
4 + 4 = 8
5 + 5 = 10

Adding Two-Digit Numbers:
  25
+ 13
----
  38

Steps:
1. Add ones: 5 + 3 = 8
2. Add tens: 2 + 1 = 3
3. Answer: 38

Practice Problems:
1. 15 + 4 = ?
2. 22 + 7 = ?
3. 30 + 10 = ?

Remember: Always start adding from the ones place!'''},

    # Grade 3
    {'title': 'Multiplication Tables 2-10', 'subject': 'Mathematics', 'grade': 3,
     'desc': 'Complete times tables',
     'content': '''MULTIPLICATION TABLES

Table of 2:
2 x 1 = 2     2 x 6 = 12
2 x 2 = 4     2 x 7 = 14
2 x 3 = 6     2 x 8 = 16
2 x 4 = 8     2 x 9 = 18
2 x 5 = 10    2 x 10 = 20

Table of 3:
3 x 1 = 3     3 x 6 = 18
3 x 2 = 6     3 x 7 = 21
3 x 3 = 9     3 x 8 = 24
3 x 4 = 12    3 x 9 = 27
3 x 5 = 15    3 x 10 = 30

Table of 4:
4 x 1 = 4     4 x 6 = 24
4 x 2 = 8     4 x 7 = 28
4 x 3 = 12    4 x 8 = 32
4 x 4 = 16    4 x 9 = 36
4 x 5 = 20    4 x 10 = 40

Table of 5:
5 x 1 = 5     5 x 6 = 30
5 x 2 = 10    5 x 7 = 35
5 x 3 = 15    5 x 8 = 40
5 x 4 = 20    5 x 9 = 45
5 x 5 = 25    5 x 10 = 50

Tip: Multiplication is repeated addition!
3 x 4 means 3 + 3 + 3 + 3 = 12'''},

    {'title': 'States of Matter', 'subject': 'Science', 'grade': 3,
     'desc': 'Solid, Liquid, and Gas',
     'content': '''STATES OF MATTER

Everything around us is made of matter. Matter exists in three states:

1. SOLID
- Has fixed shape and size
- Cannot flow
- Examples: Stone, ice, wood, book

2. LIQUID
- Has fixed size but no fixed shape
- Can flow
- Takes shape of container
- Examples: Water, milk, oil, juice

3. GAS
- No fixed shape or size
- Can flow easily
- Spreads in all directions
- Examples: Air, oxygen, water vapor

Changing States:
- Ice (solid) + Heat = Water (liquid) - MELTING
- Water (liquid) + Heat = Vapor (gas) - EVAPORATION
- Vapor (gas) - Cool = Water (liquid) - CONDENSATION
- Water (liquid) - Cool = Ice (solid) - FREEZING

Activity: Watch ice melt at room temperature!'''},

    # Grade 5
    {'title': 'Decimals Explained', 'subject': 'Mathematics', 'grade': 5,
     'desc': 'Understanding decimal numbers',
     'content': '''DECIMALS

A decimal number has two parts separated by a dot (.):
- WHOLE part (before dot)
- DECIMAL part (after dot)

Example: 25.75
- 25 is whole part
- 75 is decimal part
- Read as "twenty-five point seven five"

Place Values:
25.75
| | | |__ Hundredths (0.01)
| | |____ Tenths (0.1)
| |______ Ones
|________ Tens

Converting Fractions to Decimals:
1/2 = 0.5
1/4 = 0.25
3/4 = 0.75
1/5 = 0.2
1/10 = 0.1

Adding Decimals:
  12.50
+  3.25
-------
  15.75

Tips:
- Line up the decimal points
- Add zeros if needed
- Carry over normally'''},

    {'title': 'Indian Freedom Movement', 'subject': 'Social Studies', 'grade': 5,
     'desc': 'How India got independence',
     'content': '''INDIAN FREEDOM MOVEMENT

India was ruled by the British for about 200 years (from 1757 to 1947).

Important Leaders:

1. MAHATMA GANDHI (1869-1948)
- Father of the Nation
- Used Non-Violence (Ahimsa)
- Led Salt March in 1930
- Led Quit India Movement in 1942

2. JAWAHARLAL NEHRU (1889-1964)
- First Prime Minister of India
- Wrote "Discovery of India"

3. SARDAR PATEL (1875-1950)
- Iron Man of India
- United all princely states

4. SUBHASH CHANDRA BOSE (1897-1945)
- Led Indian National Army (INA)
- Said "Give me blood, I will give you freedom"

5. BHAGAT SINGH (1907-1931)
- Young revolutionary
- Sacrificed life for freedom

Important Dates:
- 15 August 1947: Independence Day
- 26 January 1950: Republic Day
- 2 October: Gandhi Jayanti

India became Independent on 15 August 1947 and a Republic on 26 January 1950.'''},

    # Grade 7
    {'title': 'Introduction to Algebra', 'subject': 'Mathematics', 'grade': 7,
     'desc': 'Variables, expressions and equations',
     'content': '''INTRODUCTION TO ALGEBRA

Algebra uses LETTERS to represent UNKNOWN numbers.

Variables:
- Letters like x, y, z that represent unknown values
- Example: If 2 + x = 5, then x = 3

Expressions:
- Combine numbers and variables
- Examples: 2x + 3, 5y - 7, x² + 4

Equations:
- Statements showing two things are equal
- Have an = sign
- Example: 3x + 2 = 11

Solving Simple Equations:
Find x: 2x + 4 = 10

Step 1: Subtract 4 from both sides
2x + 4 - 4 = 10 - 4
2x = 6

Step 2: Divide both sides by 2
2x / 2 = 6 / 2
x = 3

CHECK: 2(3) + 4 = 6 + 4 = 10 ✓

Like Terms:
- Same variable with same power
- Example: 3x and 5x are like terms
- 3x + 5x = 8x

Practice:
1. Solve: x + 7 = 15
2. Solve: 3y = 21
3. Simplify: 2a + 3a - a'''},

    # Grade 10
    {'title': 'Trigonometry Introduction', 'subject': 'Mathematics', 'grade': 10,
     'desc': 'Sin, Cos, Tan and ratios',
     'content': '''TRIGONOMETRY

Trigonometry deals with relationships between sides and angles of triangles.

In a Right Triangle:
- Hypotenuse: Longest side (opposite to 90°)
- Opposite: Side opposite to angle θ
- Adjacent: Side next to angle θ

Three Main Ratios:
SIN θ = Opposite / Hypotenuse
COS θ = Adjacent / Hypotenuse
TAN θ = Opposite / Adjacent

Standard Values:
Angle:    0°    30°    45°    60°    90°
Sin:      0     1/2    √2/2   √3/2   1
Cos:      1     √3/2   √2/2   1/2    0
Tan:      0     1/√3   1      √3     undefined

Key Identity:
sin²θ + cos²θ = 1

Real-world Applications:
- Measuring heights of buildings
- Navigation
- Construction
- Astronomy
- Music waves

Example:
A ladder leans against a wall.
- Angle with ground = 60°
- Length of ladder = 10 m
- Height reached = 10 × sin(60°) = 10 × 0.866 = 8.66 m

Practice Problems:
1. Find sin(30°) + cos(60°)
2. If sin θ = 1/2, find θ
3. Calculate tan(45°)'''},

    {'title': 'Life Processes Overview', 'subject': 'Science', 'grade': 10,
     'desc': 'Essential life processes in organisms',
     'content': '''LIFE PROCESSES

All living organisms perform certain basic processes to stay alive.

1. NUTRITION
Process of getting food for energy and growth.
Two types:
- Autotrophic: Plants make their own food (photosynthesis)
- Heterotrophic: Animals depend on others

Photosynthesis:
6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂

2. RESPIRATION
Breaking down food to release energy.
- Aerobic: Uses oxygen (in humans, animals)
- Anaerobic: Without oxygen (in yeast)

In humans:
Glucose + Oxygen → Carbon dioxide + Water + Energy

3. TRANSPORTATION
Moving materials to all parts of body.
- In humans: Blood through heart
- In plants: Water through xylem, food through phloem

4. EXCRETION
Removing waste products.
- In humans: Kidneys filter waste, sent out as urine
- In plants: Through stomata (gases), leaves (water)

5. CONTROL AND COORDINATION
- In humans: Brain and nervous system
- In plants: Hormones (like auxin)

The HEART pumps blood:
- Right side: Receives impure blood
- Left side: Pumps pure blood
- Has 4 chambers: 2 atria + 2 ventricles

Important Organs:
- Heart: Pumps blood
- Lungs: Exchange gases
- Kidney: Filter blood
- Liver: Detoxify, make bile
- Brain: Control everything'''},
]


def load_resources():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found.")
            return

        # Create resources directory
        os.makedirs('./data/resources', exist_ok=True)

        existing_titles = {r.title for r in Resource.query.all()}
        added = 0

        for res_data in NCERT_RESOURCES:
            if res_data['title'] in existing_titles:
                continue

            # Save text content as file
            filename = f"ncert_{res_data['grade']}_{res_data['subject'].replace(' ', '_')}_{res_data['title'].replace(' ', '_').replace(':', '')[:30]}.txt"
            file_path = f"data/resources/{filename}"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(res_data['content'])

            file_size = os.path.getsize(file_path)

            resource = Resource(
                title=res_data['title'],
                description=res_data['desc'],
                subject=res_data['subject'],
                grade_level=res_data['grade'],
                content_type='txt',
                file_path=file_path,
                file_size=file_size,
                created_by=teacher.id,
                is_published=True
            )
            db.session.add(resource)
            added += 1
            print(f"[OK] Added: Grade {res_data['grade']} - {res_data['title']}")

        db.session.commit()
        print(f"\n[DONE] Added {added} NCERT resources")
        print(f"Total resources in system: {Resource.query.count()}")


if __name__ == '__main__':
    try:
        load_resources()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
