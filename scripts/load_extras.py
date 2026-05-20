"""
Loads:
1. Additional NCERT resources for all grades
2. Sample previous year question papers
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Resource, QuestionPaper

# ============================================================
# EXTRA NCERT RESOURCES
# ============================================================

EXTRA_RESOURCES = [
    # Grade 1
    {'grade': 1, 'subject': 'English', 'title': 'Simple Words and Reading',
     'desc': 'Learn simple 3-letter words',
     'content': '''SIMPLE WORDS AND READING

Three-Letter Words (CVC pattern):

Words with 'a':
- cat, bat, hat, mat, rat, sat
- can, fan, man, pan, ran, tan
- bag, tag, rag, jag

Words with 'e':
- bed, fed, led, red, wed
- ten, men, pen, hen, den
- bet, get, let, met, net, pet

Words with 'i':
- big, dig, pig, fig, jig
- bit, fit, hit, kit, sit, pit
- pin, fin, win, bin, tin

Words with 'o':
- box, fox, log, dog, fog
- pot, dot, got, hot, lot, not
- mop, hop, top, cop

Words with 'u':
- bus, sun, fun, run, gun
- but, cut, hut, nut, put
- mug, jug, bug, hug, rug

Reading Practice:
- The cat sat on the mat.
- A big pig ran fast.
- I see a red hen.
- The dog has a bone.
- Mom put the pot on top.

Sight Words (memorize):
the, a, and, is, in, it, of, to, you, I, we, my, see, can, go, no'''},

    # Grade 2
    {'grade': 2, 'subject': 'Mathematics', 'title': 'Money and Measurement',
     'desc': 'Indian currency and basic measurements',
     'content': '''MONEY AND MEASUREMENT

INDIAN CURRENCY:

Coins: 1, 2, 5, 10 rupees
Notes: 10, 20, 50, 100, 200, 500, 2000 rupees

Symbol: ₹ (Indian Rupee)

Simple Addition with Money:
- ₹5 + ₹10 = ₹15
- ₹20 + ₹50 = ₹70
- ₹100 + ₹500 = ₹600

Word Problems:
1. Ravi has ₹50. He buys a pencil for ₹10.
   How much money is left? = ₹50 - ₹10 = ₹40

2. Sita has ₹20 and gets ₹30 more.
   Total = ₹20 + ₹30 = ₹50

MEASUREMENT:

LENGTH:
- 1 meter (m) = 100 centimeters (cm)
- 1 kilometer (km) = 1000 meters

Compare:
- Pencil length: cm
- Door height: m
- Distance between cities: km

WEIGHT:
- 1 kilogram (kg) = 1000 grams (g)

Compare:
- Pencil: grams (g)
- Bag of rice: kilograms (kg)

CAPACITY:
- 1 liter (L) = 1000 milliliters (mL)

Compare:
- Glass of water: mL
- Bucket: L

TIME:
- 1 minute = 60 seconds
- 1 hour = 60 minutes
- 1 day = 24 hours
- 1 week = 7 days
- 1 month = 30 days (approx)
- 1 year = 12 months

Reading Clock:
- Short hand shows hours
- Long hand shows minutes'''},

    # Grade 2
    {'grade': 2, 'subject': 'Science', 'title': 'Air Water and Weather',
     'desc': 'Importance of air, water and weather changes',
     'content': '''AIR, WATER AND WEATHER

AIR:
- Air is all around us
- We can't see air but we can feel it
- Air is needed to BREATHE
- Air helps planes fly
- Wind is moving air

Uses of Air:
- Breathing for humans, animals, plants
- Drying wet clothes
- Flying kites
- Producing wind power

WATER:
- Water has no color, smell or taste
- Found in rivers, oceans, ponds, lakes
- Comes as RAIN from sky
- Three forms:
  * SOLID (ice)
  * LIQUID (water)
  * GAS (water vapor)

Uses of Water:
- Drinking
- Cooking
- Bathing
- Washing clothes
- Growing plants
- Generating electricity

Save Water:
- Don't leave taps open
- Reuse water for plants
- Fix leaking taps

WEATHER:
Weather changes daily.

Types:
- SUNNY: Bright sunlight
- CLOUDY: Sky has clouds
- RAINY: Water falls from clouds
- WINDY: Air moves fast
- SNOWY: Snow falls (cold places)
- STORMY: Heavy wind and rain

SEASONS in India:
1. SUMMER (March-June): Hot
2. RAINY/MONSOON (July-September): Rainfall
3. WINTER (December-February): Cold

Clothes by Weather:
- Summer: Light cotton clothes
- Winter: Warm woolen clothes
- Rainy: Raincoat, umbrella'''},

    # Grade 3
    {'grade': 3, 'subject': 'English', 'title': 'Stories and Pictures',
     'desc': 'Reading short stories with morals',
     'content': '''STORIES AND PICTURES

THE THIRSTY CROW (Famous fable):

Once upon a time, on a hot summer day, a crow was very thirsty. He flew everywhere looking for water. After flying for long, he saw a pot.

The crow flew down to drink. But the water was very low in the pot. He could not reach it. He thought hard.

He saw some pebbles nearby. He picked one pebble and dropped it in the pot. He kept dropping pebbles one by one. The water came up slowly.

Soon, the water reached the top. The crow drank the water happily and flew away.

MORAL: "Where there is a will, there is a way."

THE LION AND THE MOUSE:

A lion was sleeping. A small mouse ran over his face. The lion woke up and caught the mouse. The mouse begged, "Please don't eat me. One day I might help you."

The lion laughed but let the mouse go.

Later, the lion got caught in a hunter's net. He roared loudly. The mouse heard him. The mouse came and chewed the net with his sharp teeth. The lion was free!

MORAL: "Small friends can also be great helpers."

THE HARE AND THE TORTOISE:

A hare and tortoise had a race. The hare ran very fast. He thought, "I have plenty of time. Let me rest."

He slept under a tree. The tortoise walked slowly but kept moving. The tortoise reached the finish line first!

MORAL: "Slow and steady wins the race."

STORY ELEMENTS:
- CHARACTERS: People/animals in story
- SETTING: Where and when
- PLOT: What happens
- LESSON: What we learn

Reading Tips:
1. Read slowly
2. Understand each sentence
3. Look at pictures
4. Find the lesson
5. Tell story in your own words'''},

    # Grade 4
    {'grade': 4, 'subject': 'Mathematics', 'title': 'Geometry Basics',
     'desc': 'Lines, angles, and basic shapes',
     'content': '''GEOMETRY BASICS

LINES:

Point: A small dot . (no size)

Line: Goes on forever in both directions
Line Segment: Has two end points
Ray: Starts at a point, goes forever in one direction

Types of Lines:
1. STRAIGHT LINE: ━━━━━
2. CURVED LINE: ∽
3. HORIZONTAL: ━ (left-right)
4. VERTICAL: ┃ (up-down)
5. PARALLEL: Two lines that never meet ║
6. PERPENDICULAR: Lines that meet at 90° ┴

ANGLES:

An angle is formed when two lines meet.

Types:
1. ACUTE ANGLE: Less than 90° (small)
2. RIGHT ANGLE: Exactly 90° (corner of book)
3. OBTUSE ANGLE: Between 90° and 180°
4. STRAIGHT ANGLE: Exactly 180° (straight line)
5. REFLEX ANGLE: More than 180°

Measuring tool: PROTRACTOR

SHAPES:

2D Shapes (Flat):
- CIRCLE: Round, no corners, no sides
- TRIANGLE: 3 sides, 3 corners
- SQUARE: 4 equal sides, 4 right angles
- RECTANGLE: 4 sides (2 long, 2 short), 4 right angles
- PENTAGON: 5 sides
- HEXAGON: 6 sides
- OCTAGON: 8 sides

Triangle Types:
- Equilateral: All 3 sides equal
- Isosceles: 2 sides equal
- Scalene: All sides different
- Right: One angle is 90°

3D Shapes (Solid):
- CUBE: 6 square faces (dice)
- CUBOID: 6 rectangular faces (book)
- SPHERE: Round like ball
- CYLINDER: Like a pipe
- CONE: Pointy on top (ice cream cone)
- PYRAMID: Triangle faces

PERIMETER:
Total distance around a shape
- Square: 4 × side
- Rectangle: 2 × (length + breadth)
- Triangle: side1 + side2 + side3

AREA:
Space inside a shape
- Square: side × side
- Rectangle: length × breadth

Examples:
Square side = 5cm
- Perimeter = 4 × 5 = 20 cm
- Area = 5 × 5 = 25 cm²

Rectangle 6cm × 4cm
- Perimeter = 2(6+4) = 20 cm
- Area = 6 × 4 = 24 cm²

SYMMETRY:
If you fold a shape and both sides match, it has symmetry.

Symmetric shapes:
- Square: 4 lines of symmetry
- Rectangle: 2 lines
- Circle: Infinite
- Equilateral triangle: 3'''},

    # Grade 5
    {'grade': 5, 'subject': 'Science', 'title': 'Plants - Reproduction and Adaptation',
     'desc': 'How plants reproduce and adapt to environments',
     'content': '''PLANTS - REPRODUCTION AND ADAPTATION

PLANT REPRODUCTION:

Plants reproduce in different ways:

1. SEEDS:
- Most common method
- Inside fruits or pods
- Examples: Mango, apple, pea, beans

Parts of a Seed:
- Seed coat (outer covering)
- Embryo (baby plant)
- Cotyledon (food storage)

Seed Dispersal Methods:
- By WIND: Light seeds (cotton, dandelion)
- By WATER: Floating seeds (coconut)
- By ANIMALS: Fruits eaten (mango, guava)
- By BURSTING: Pods explode (pea, beans)

2. STEMS:
- Potato grows from stem pieces
- Sugarcane from stem cuttings

3. ROOTS:
- Sweet potato grows from roots
- Carrot, radish

4. LEAVES:
- Some plants like Bryophyllum

5. SPORES:
- Ferns, mosses use spores
- Not seeds

PARTS OF A FLOWER:

- SEPALS: Green, protect the bud
- PETALS: Colored, attract bees
- STAMEN: Male part (anther + filament)
- PISTIL: Female part (stigma + style + ovary)

POLLINATION:
- Transfer of pollen from male to female part
- Done by bees, butterflies, wind, water

FERTILIZATION:
- After pollination, seeds form inside ovary
- Ovary becomes fruit

ADAPTATION:

Plants adapt to their environment:

DESERT PLANTS (like Cactus):
- Thick stem to store water
- Spiny leaves (less water loss)
- Deep roots
- Examples: Cactus, Aloe vera

WATER PLANTS:
- Float on water
- Light, hollow stems
- Examples: Lotus, water lily

MOUNTAIN PLANTS:
- Cone-shaped (snow slides off)
- Strong roots
- Examples: Pine, fir

RAINFOREST PLANTS:
- Drip-tip leaves
- Climb up trees for sunlight
- Examples: Vines, orchids

GRASSLAND PLANTS:
- Short and grow quickly
- Examples: Grass, wheat

INSECTIVOROUS PLANTS:
- Catch insects for nutrition
- Examples: Pitcher plant, Venus flytrap

USEFUL PLANTS:

For Food: Wheat, rice, vegetables, fruits
For Medicine: Tulsi, neem, aloe vera
For Wood: Teak, sal
For Cloth: Cotton, jute, hemp
For Air: All plants give oxygen
For Beauty: Roses, jasmine

CONSERVATION:
- Don't waste paper (saves trees)
- Plant trees
- Don't pluck flowers
- Reduce, Reuse, Recycle'''},

    # Grade 6
    {'grade': 6, 'subject': 'English', 'title': 'Articles and Pronouns',
     'desc': 'Using a, an, the and pronouns correctly',
     'content': '''ARTICLES AND PRONOUNS

ARTICLES:

Articles are words: A, AN, THE

INDEFINITE ARTICLES: A, AN
- Used for any one (not specific)

USE OF "A":
- Before consonant sounds
- A book, a cat, a tree, a school, a teacher

USE OF "AN":
- Before vowel sounds (a, e, i, o, u)
- An apple, an egg, an ink, an orange, an umbrella
- An hour (silent h)
- An honest man (silent h)

USE OF "THE":
- Before specific things
- The sun, the moon (only one)
- The Ganga, the Himalayas (specific names)
- The teacher (we know which teacher)
- Before superlatives: the best, the tallest

NO ARTICLE:
- Before proper nouns: India, Ravi, Delhi
- Before plurals when general: Books are useful
- Before mass nouns: Water is precious

Examples:
- I saw a dog. (any dog)
- The dog is mine. (specific dog)
- He is an honest boy.
- The sun rises in the east.

PRONOUNS:

A pronoun replaces a noun.

Without pronoun: Ravi went to Ravi's school because Ravi was late.
With pronoun: Ravi went to HIS school because HE was late.

TYPES OF PRONOUNS:

1. PERSONAL PRONOUNS:

| Person | Singular | Plural |
|--------|----------|--------|
| 1st | I, me, my | we, us, our |
| 2nd | you, your | you, your |
| 3rd | he, him, his (male) | they, them, their |
|     | she, her, hers (female) | |
|     | it, its (thing/animal) | |

2. POSSESSIVE PRONOUNS:
- mine, yours, his, hers, its, ours, theirs
- This book is mine.
- That bag is yours.

3. REFLEXIVE PRONOUNS:
- myself, yourself, himself, herself
- itself, ourselves, yourselves, themselves
- I hurt myself.
- She did it herself.

4. DEMONSTRATIVE PRONOUNS:
- this, that (singular)
- these, those (plural)
- This is my pen.
- Those are big trees.

5. INTERROGATIVE PRONOUNS:
- who, whom, whose, what, which
- Who is at the door?
- What is your name?

6. RELATIVE PRONOUNS:
- who, whom, whose, which, that
- Joins two sentences
- The boy who is tall is my brother.
- The book that I bought is good.

7. INDEFINITE PRONOUNS:
- someone, anyone, everyone, no one
- something, anything, everything, nothing
- Someone is calling you.
- Nothing is impossible.

PRONOUN AGREEMENT:

Pronoun must match the noun:
- Ravi loves HIS dog. (not her)
- Sita reads HER book. (not his)
- The children play with THEIR toys. (not its)

Common Mistakes:
✗ Me and Ravi went.
✓ Ravi and I went.

✗ Between you and I
✓ Between you and me

✗ Himself did it.
✓ He did it himself.'''},

    # Grade 7
    {'grade': 7, 'subject': 'Mathematics', 'title': 'Fractions and Decimals',
     'desc': 'Operations on fractions and decimal numbers',
     'content': '''FRACTIONS AND DECIMALS

FRACTIONS:

A fraction has two parts:
- NUMERATOR (top): number of parts taken
- DENOMINATOR (bottom): total parts

Example: 3/4
- 3 is numerator
- 4 is denominator
- Means 3 parts out of 4

TYPES OF FRACTIONS:

1. PROPER: Numerator < Denominator
   Examples: 1/2, 3/4, 5/7

2. IMPROPER: Numerator ≥ Denominator
   Examples: 5/3, 7/4, 9/8

3. MIXED: Whole number + fraction
   Examples: 1½, 2¾, 3⅓

CONVERTING:
Improper to Mixed:
9/4 = 2¼ (9÷4 = 2 remainder 1)

Mixed to Improper:
2¾ = (2×4 + 3)/4 = 11/4

EQUIVALENT FRACTIONS:
Same value, different numbers
- 1/2 = 2/4 = 3/6 = 4/8
- Multiply or divide both top and bottom by same number

COMPARING FRACTIONS:
Same denominator: bigger numerator wins
3/5 > 2/5

Different denominators: Make denominators same (LCM)
1/2 vs 1/3
1/2 = 3/6
1/3 = 2/6
So 1/2 > 1/3

ADDING/SUBTRACTING FRACTIONS:

Same Denominator:
1/4 + 2/4 = 3/4
5/8 - 2/8 = 3/8

Different Denominators (use LCM):
1/2 + 1/3
LCM of 2,3 = 6
3/6 + 2/6 = 5/6

MULTIPLYING FRACTIONS:
(a/b) × (c/d) = (a×c)/(b×d)
1/2 × 2/3 = 2/6 = 1/3

DIVIDING FRACTIONS:
(a/b) ÷ (c/d) = (a/b) × (d/c)
Flip second fraction and multiply!
1/2 ÷ 1/4 = 1/2 × 4/1 = 4/2 = 2

DECIMALS:

Decimal point separates whole and fractional parts.

12.345
Whole: 12
Decimal: 345

Place Values:
- Tens, Ones . Tenths, Hundredths, Thousandths

CONVERTING:

Fraction to Decimal:
- Divide numerator by denominator
- 1/2 = 0.5
- 3/4 = 0.75
- 1/5 = 0.2

Decimal to Fraction:
0.5 = 5/10 = 1/2
0.25 = 25/100 = 1/4
0.125 = 125/1000 = 1/8

OPERATIONS ON DECIMALS:

Addition (line up decimal points):
  12.50
+  3.25
-------
  15.75

Subtraction:
  20.00
-  5.75
-------
  14.25

Multiplication:
Count total decimal places in factors
2.5 × 1.3 = 3.25 (2 decimal places total)

Division:
Move decimal points to make divisor whole
6.25 ÷ 2.5 = 62.5 ÷ 25 = 2.5

PERCENTAGE:
Per cent = per 100

50% = 50/100 = 0.5 = 1/2
25% = 25/100 = 0.25 = 1/4
75% = 0.75 = 3/4

To find %:
50% of 80 = (50/100) × 80 = 40

To convert:
0.6 as % = 0.6 × 100 = 60%
3/4 as % = 0.75 × 100 = 75%'''},

    # Grade 8
    {'grade': 8, 'subject': 'Mathematics', 'title': 'Data Handling and Graphs',
     'desc': 'Statistics, charts, and graph reading',
     'content': '''DATA HANDLING AND GRAPHS

DATA:
Information collected for some purpose.
Example: Marks of students, weights of fruits

RAW DATA:
Data in original form
Example: 45, 67, 78, 89, 56, 67, 78, 90

ORGANIZED DATA:
Arranged for easier understanding

FREQUENCY:
How many times something occurs

TYPES OF GRAPHS:

1. BAR GRAPH:
- Uses rectangular bars
- Vertical or horizontal
- Bars of equal width
- Heights show value

Example: Sales per month
Jan: ████ 40
Feb: █████ 50
Mar: ██████ 60

2. PIE CHART:
- Circle divided into sectors
- Each sector = portion of total
- Total = 360°

To find degree for each part:
(Part/Total) × 360°

Example: Class has 30 students
- Boys: 12 → (12/30) × 360 = 144°
- Girls: 18 → (18/30) × 360 = 216°

3. LINE GRAPH:
- Points joined by lines
- Shows trends over time
- Good for changes

4. HISTOGRAM:
- Like bar graph but for grouped data
- No gaps between bars

MEASURES OF CENTRAL TENDENCY:

MEAN (Average):
Mean = Sum of all values / Number of values

Example: 5, 10, 15, 20
Mean = (5+10+15+20)/4 = 50/4 = 12.5

MEDIAN:
Middle value when data is arranged in order

Odd number of values:
Example: 3, 5, 7, 9, 11
Median = 7 (middle one)

Even number of values:
Example: 2, 4, 6, 8
Median = (4+6)/2 = 5

MODE:
Most frequently occurring value

Example: 3, 5, 7, 5, 9, 5, 2
Mode = 5 (appears 3 times)

RANGE:
Highest - Lowest

Example: 5, 8, 10, 15, 20
Range = 20 - 5 = 15

PROBABILITY:

Chance of an event happening.

Probability = Favorable outcomes / Total outcomes

Examples:

Coin toss:
- 2 outcomes (Heads or Tails)
- P(Heads) = 1/2 = 0.5 = 50%

Dice roll:
- 6 outcomes (1,2,3,4,5,6)
- P(getting 4) = 1/6
- P(even number) = 3/6 = 1/2

Cards (deck of 52):
- P(getting red card) = 26/52 = 1/2
- P(getting King) = 4/52 = 1/13

Range: 0 (impossible) to 1 (certain)
- 0 = no chance
- 0.5 = equal chance
- 1 = certain

REAL-LIFE APPLICATIONS:
- Weather forecasting
- Sports statistics
- Survey results
- Election predictions
- Sales analysis
- Health monitoring'''},

    # Grade 9
    {'grade': 9, 'subject': 'Mathematics', 'title': 'Coordinate Geometry',
     'desc': 'Cartesian plane and points',
     'content': '''COORDINATE GEOMETRY

CARTESIAN PLANE:
A flat surface with two number lines.

- X-AXIS: Horizontal line (left-right)
- Y-AXIS: Vertical line (up-down)
- ORIGIN (0,0): Where axes meet

QUADRANTS:
The plane is divided into 4 quadrants.

         Y
         |
    II   |   I
   (-,+) | (+,+)
─────────┼─────── X
   (-,-) | (+,-)
    III  |   IV
         |

Quadrant I: x positive, y positive (+,+)
Quadrant II: x negative, y positive (-,+)
Quadrant III: x negative, y negative (-,-)
Quadrant IV: x positive, y negative (+,-)

COORDINATES:
A point is named by (x, y)
- x = horizontal distance
- y = vertical distance

PLOTTING POINTS:

Plot (3, 4):
- Move 3 units right (x = 3)
- Then 4 units up (y = 4)
- Mark the point

Plot (-2, 5):
- Move 2 units left (x = -2)
- Then 5 units up (y = 5)

Plot (0, 0): Origin
Plot (5, 0): On x-axis
Plot (0, 3): On y-axis

DISTANCE FORMULA:

Distance between (x₁, y₁) and (x₂, y₂):
d = √[(x₂-x₁)² + (y₂-y₁)²]

Example: Distance from (1,2) to (4,6)
d = √[(4-1)² + (6-2)²]
d = √[9 + 16]
d = √25 = 5

MIDPOINT FORMULA:

Midpoint of (x₁,y₁) and (x₂,y₂):
Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2)

Example: Midpoint of (2,3) and (6,9)
= ((2+6)/2, (3+9)/2)
= (4, 6)

SLOPE OF A LINE:

Slope (m) = (y₂-y₁)/(x₂-x₁)

Example: Slope through (1,2) and (3,8)
m = (8-2)/(3-1) = 6/2 = 3

- Positive slope: line goes up
- Negative slope: line goes down
- Zero slope: horizontal line
- Undefined: vertical line

EQUATION OF LINE:

Slope-intercept form:
y = mx + c
- m is slope
- c is y-intercept

Example: y = 2x + 3
- Slope = 2
- y-intercept = 3 (line crosses y-axis at 3)

Point-slope form:
y - y₁ = m(x - x₁)

GRAPH OF EQUATIONS:

y = x (passes through origin, slope 1)
y = 2x (steeper line)
y = x + 2 (line shifted up)
y = -x (slope is -1)
y = 0 (horizontal x-axis)
x = 0 (vertical y-axis)

APPLICATIONS:

- GPS coordinates (latitude, longitude)
- Maps
- Computer graphics
- Sports field positions
- Architecture
- Astronomy (planet positions)

EXAMPLES:

1. Find distance from (0,0) to (3,4):
d = √(9+16) = √25 = 5

2. Plot (2, -3): Quadrant IV
   (2 right, 3 down)

3. Line y = 2x + 1:
   When x=0: y=1
   When x=1: y=3
   When x=2: y=5'''},

    # Grade 10
    {'grade': 10, 'subject': 'Mathematics', 'title': 'Statistics and Probability',
     'desc': 'Advanced statistics and probability calculations',
     'content': '''STATISTICS AND PROBABILITY

STATISTICS:
Study of collection, analysis, and interpretation of data.

MEASURES OF CENTRAL TENDENCY:

1. MEAN (Arithmetic Average):
For ungrouped data:
Mean (x̄) = Σx / n

Example: Marks 70, 80, 90, 60, 50
Mean = (70+80+90+60+50)/5 = 350/5 = 70

For grouped data:
Mean = Σ(fx) / Σf
where f = frequency, x = mid value

Direct Method, Assumed Mean Method, Step-Deviation Method.

2. MEDIAN:
Middle value of arranged data.

For ungrouped:
- Odd n: middle value
- Even n: average of two middle values

Example: 12, 15, 18, 22, 25, 30, 35
n = 7 (odd)
Median = 4th value = 22

For grouped:
Median = L + [(n/2 - cf)/f] × h
- L = lower limit of median class
- n = total frequency
- cf = cumulative frequency before median class
- f = frequency of median class
- h = class width

3. MODE:
Most frequent value.

For grouped:
Mode = L + [(f₁-f₀)/(2f₁-f₀-f₂)] × h
- L = lower limit of modal class
- f₁ = frequency of modal class
- f₀ = frequency of class before
- f₂ = frequency of class after
- h = class width

EMPIRICAL RELATION:
Mode = 3 × Median - 2 × Mean

CUMULATIVE FREQUENCY:
Running total of frequencies.

OGIVE: Graph of cumulative frequency.

GRAPHICAL REPRESENTATION:
- Bar Graph
- Histogram
- Frequency Polygon
- Pie Chart
- Ogive

PROBABILITY:

Probability of event E:
P(E) = Number of favorable outcomes / Total outcomes

Range: 0 ≤ P(E) ≤ 1
- P(impossible event) = 0
- P(sure event) = 1

P(not E) + P(E) = 1

EXPERIMENTAL vs THEORETICAL:

Experimental: Based on actual trials
Theoretical: Based on equally likely outcomes

TOSSING A COIN:

Sample space: {H, T}
P(H) = 1/2
P(T) = 1/2

Tossing 2 coins:
Sample space: {HH, HT, TH, TT}
P(2 heads) = 1/4
P(1 head exactly) = 2/4 = 1/2
P(at least 1 head) = 3/4

ROLLING A DIE:

Sample space: {1,2,3,4,5,6}
P(2) = 1/6
P(even) = 3/6 = 1/2
P(prime) = 3/6 = 1/2 (2, 3, 5)
P(greater than 4) = 2/6 = 1/3 (5, 6)

PLAYING CARDS:
Total cards: 52
- 4 suits (hearts ♥, diamonds ♦, clubs ♣, spades ♠)
- Each suit: 13 cards
- Face cards: J, Q, K (3 per suit = 12 total)
- Aces: 4

P(red card) = 26/52 = 1/2
P(king) = 4/52 = 1/13
P(red king) = 2/52 = 1/26
P(face card) = 12/52 = 3/13

PROBABILITY OF COMPLEMENTARY EVENTS:

If P(A) = probability of event A
P(not A) = 1 - P(A)

Example: If P(rain) = 0.3
P(no rain) = 1 - 0.3 = 0.7

INDEPENDENT EVENTS:
Events that don't affect each other.

If A and B are independent:
P(A and B) = P(A) × P(B)

Example: Tossing 2 coins
P(2 heads) = P(H) × P(H) = 1/2 × 1/2 = 1/4

APPLICATIONS:
- Weather prediction
- Insurance calculations
- Quality control
- Sports analytics
- Medical testing
- Stock markets
- Lottery odds'''},

    # Grade 10 English
    {'grade': 10, 'subject': 'English', 'title': 'Reading Comprehension and Writing',
     'desc': 'Advanced reading and writing skills',
     'content': '''READING COMPREHENSION AND WRITING

READING SKILLS:

1. SKIMMING: Fast reading for main idea
2. SCANNING: Fast reading for specific info
3. DETAILED READING: Slow careful reading
4. CRITICAL READING: Analyzing deeply

UNDERSTANDING PASSAGES:

Steps:
1. Read title and any sub-headings
2. Skim once for general idea
3. Read questions
4. Read passage carefully
5. Underline key information
6. Answer questions referring to passage

TYPES OF QUESTIONS:

1. FACTUAL: Direct from passage
   "What year did this happen?"

2. INFERENCE: Reading between lines
   "Why might the author feel this way?"

3. VOCABULARY: Word meanings in context
   "What does 'meticulous' mean here?"

4. MAIN IDEA: Central theme
   "What is the passage mostly about?"

5. AUTHOR'S PURPOSE: Why was it written
   "Is this to inform, persuade, or entertain?"

WRITING SKILLS:

1. PARAGRAPH WRITING:

Structure:
- Topic sentence (main idea)
- Supporting sentences (details, examples)
- Concluding sentence

Tips:
- One main idea per paragraph
- Use linking words: however, moreover, therefore
- Vary sentence length
- Use transition phrases

Example Paragraph:

"Education is the key to a successful life. Through education, people gain knowledge and skills needed for various careers. It teaches critical thinking, problem-solving, and communication. Educated individuals contribute more to society and have better job opportunities. Furthermore, education helps in personal growth and broadens our perspective. Therefore, everyone should have access to quality education."

2. ESSAY WRITING:

Introduction:
- Catchy opening
- Background info
- Thesis statement

Body (2-4 paragraphs):
- One idea per paragraph
- Examples and explanations
- Logical flow

Conclusion:
- Summarize main points
- Restate thesis differently
- Final thought

Essay Topics:
- My Favorite Book
- Importance of Education
- Pollution and Solutions
- Role of Women in Society
- My Dream Career

3. LETTER WRITING:

FORMAL LETTER (Application, Complaint, Business):

Sender's address
Date

Recipient's Designation
Address

Subject: [Brief topic]

Sir/Madam,

[Body in 2-3 paragraphs]

Yours faithfully/sincerely,
NAME

INFORMAL LETTER (To family, friends):

Address
Date

Dear [Name],

[Body in friendly tone]

Yours lovingly,
[Name]

4. NOTICE WRITING:

[Inside a box]
ORGANIZATION NAME
NOTICE
Date

HEADING

Body (3-4 lines)

Signature
Designation

5. ARTICLE WRITING:

For school magazines/newspapers.

Format:
- Title
- By [author name]
- Introduction (catch reader)
- Body (organized points)
- Conclusion

6. STORY WRITING:

Elements:
- Setting (where, when)
- Characters
- Plot (beginning, middle, end)
- Conflict and resolution
- Theme/Lesson

VOCABULARY BUILDING:

ROOTS:
- Bio- (life): biology, biography
- Geo- (earth): geography, geology
- Tele- (far): telephone, television
- Photo- (light): photograph, photosynthesis

PREFIXES:
- Un- (not): unfair, unable
- Pre- (before): preview, predict
- Re- (again): rewrite, return
- Dis- (not): dishonest, disagree
- Mis- (wrong): mistake, misread

SUFFIXES:
- -tion (action): action, education
- -ness (state): happiness, kindness
- -ful (full of): useful, beautiful
- -less (without): careless, useless
- -ly (way): quickly, slowly

COMMON CONFUSIONS:

Their/There/They're:
- Their = belonging to them (their book)
- There = at that place (over there)
- They're = they are (they're here)

Your/You're:
- Your = belonging to you (your bag)
- You're = you are (you're nice)

Its/It's:
- Its = belonging to it (its tail)
- It's = it is (it's raining)

To/Two/Too:
- To = preposition (go to school)
- Two = number (two books)
- Too = also/very (too much)

TIPS FOR GOOD WRITING:

1. Plan before writing
2. Use simple, clear language
3. Vary sentence structures
4. Check grammar and spelling
5. Use active voice mostly
6. Read your work aloud
7. Edit and revise'''}
]


# ============================================================
# QUESTION PAPERS
# ============================================================

QUESTION_PAPERS = [
    # Grade 5 Papers
    {
        'grade': 5, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 120, 'total_marks': 80,
        'title': 'Grade 5 Mathematics Annual 2023',
        'description': 'Full annual examination paper for Class 5 Mathematics',
        'content': '''GRADE 5 MATHEMATICS - ANNUAL EXAMINATION
Year: 2023
Time: 2 hours
Maximum Marks: 80

Section A - Multiple Choice (Each 1 mark) - Total: 10 marks

1. What is 245 + 367?
   (a) 612    (b) 622    (c) 602    (d) 632

2. What is 1/2 of 60?
   (a) 20    (b) 25    (c) 30    (d) 35

3. Which is greater?
   (a) 0.5    (b) 0.25    (c) 0.75    (d) 1

4. How many sides does a hexagon have?
   (a) 4    (b) 5    (c) 6    (d) 7

5. 1 hour = ___ minutes
   (a) 30    (b) 45    (c) 60    (d) 90

6. 50% of 200 = ?
   (a) 50    (b) 100    (c) 150    (d) 200

7. What is the place value of 5 in 4521?
   (a) 5    (b) 50    (c) 500    (d) 5000

8. 1 kilometer = ___ meters
   (a) 100    (b) 500    (c) 1000    (d) 10000

9. Perimeter of square with side 4 cm?
   (a) 8 cm    (b) 12 cm    (c) 16 cm    (d) 20 cm

10. 7 × 8 = ?
    (a) 49    (b) 54    (c) 56    (d) 63

Section B - Short Answer (Each 3 marks) - Total: 30 marks

11. Find the sum: 1234 + 5678
12. Subtract: 9000 - 4567
13. Multiply: 234 × 5
14. Divide: 144 ÷ 12
15. Convert 3/4 to a decimal
16. Find 25% of 80
17. Add: 12.5 + 3.75
18. Subtract: 20.50 - 8.25
19. Find perimeter of rectangle 8 cm × 5 cm
20. Find area of square with side 6 cm

Section C - Long Answer (Each 5 marks) - Total: 25 marks

21. A shopkeeper sells 25 chocolates per day. How many will he sell in 30 days?

22. Ravi has ₹500. He buys books worth ₹350. How much money is left?

23. Convert these fractions to decimals: 1/2, 1/4, 3/4, 1/5

24. A rectangle has length 12 cm and breadth 8 cm. Find:
    (a) Perimeter
    (b) Area

25. Find the missing values:
    (a) 25 × ? = 100
    (b) ? ÷ 5 = 15
    (c) 36 + ? = 50

Section D - Application (15 marks)

26. A water tank holds 5000 liters. If 1200 liters is used,
    how much water is left?

27. A train leaves at 6:30 AM and reaches at 11:45 AM.
    How long did the journey take?

28. Draw a clock showing 3:30 PM. Mark hour and minute hands.

29. A school has 600 students. 1/3 are boys.
    How many boys and girls are there?

ALL THE BEST!'''},

    {
        'grade': 5, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 60,
        'title': 'Grade 5 Science Annual 2023',
        'description': 'Annual Science examination for Class 5',
        'content': '''GRADE 5 SCIENCE - ANNUAL EXAMINATION
Year: 2023
Time: 1.5 hours
Maximum Marks: 60

Section A - Multiple Choice (Each 1 mark) - Total: 10 marks

1. Which organ pumps blood?
   (a) Brain    (b) Lungs    (c) Heart    (d) Kidney

2. How many bones in adult human?
   (a) 100    (b) 156    (c) 206    (d) 300

3. Plants make food through?
   (a) Respiration    (b) Digestion    (c) Photosynthesis    (d) Excretion

4. We breathe out?
   (a) Oxygen    (b) Carbon dioxide    (c) Nitrogen    (d) Hydrogen

5. Which is a herbivore?
   (a) Tiger    (b) Lion    (c) Cow    (d) Cat

6. Earth rotates in?
   (a) 12 hours    (b) 24 hours    (c) 365 days    (d) 1 hour

7. Which is the largest planet?
   (a) Earth    (b) Mars    (c) Jupiter    (d) Saturn

8. Sun is a?
   (a) Planet    (b) Moon    (c) Star    (d) Asteroid

9. Photosynthesis happens in?
   (a) Root    (b) Stem    (c) Leaves    (d) Flower

10. Three states of matter?
    (a) Solid only    (b) Solid, liquid    (c) Solid, liquid, gas    (d) Just liquid

Section B - Fill in the Blanks (Each 1 mark) - Total: 10 marks

11. The center of solar system is the _____.
12. Plants need _____ for photosynthesis.
13. _____ is the longest river in India.
14. Our heart has _____ chambers.
15. The smallest unit of life is _____.
16. _____ is also known as red planet.
17. Carnivores eat _____.
18. Earth's only natural satellite is _____.
19. We get Vitamin D from _____.
20. _____ is needed by plants to grow.

Section C - Short Answer (Each 3 marks) - Total: 30 marks

21. Name 5 organs in human body and their functions.

22. What are the differences between plants and animals?

23. Name parts of a flower.

24. What is the water cycle? Draw and explain.

25. Why do we need to save water?

26. What are renewable and non-renewable resources?

27. Explain photosynthesis equation.

28. List 5 differences between solid, liquid, and gas.

29. Name 5 planets in order from sun.

30. What is air pollution? How can we prevent it?

Section D - Long Answer (10 marks)

31. Draw and explain human digestive system.

32. Write 5 differences between herbivores, carnivores, and omnivores with examples.

ALL THE BEST!'''},

    # Grade 8 Papers
    {
        'grade': 8, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 150, 'total_marks': 100,
        'title': 'Grade 8 Mathematics Annual 2023',
        'description': 'Complete annual examination for Class 8 Math',
        'content': '''GRADE 8 MATHEMATICS - ANNUAL EXAMINATION
Year: 2023
Time: 2.5 hours
Maximum Marks: 100

Section A - MCQ (1 mark each) - Total: 15 marks

1. (-5) + (-3) = ?
   (a) 8    (b) -8    (c) -2    (d) 2

2. Simplify: 2x + 3x
   (a) 5x    (b) 6x    (c) 5    (d) 6x²

3. LCM of 4 and 6 = ?
   (a) 12    (b) 24    (c) 10    (d) 8

4. (a+b)² = ?
   (a) a²+b²    (b) a²-b²    (c) a²+2ab+b²    (d) a²-2ab+b²

5. Area of triangle with base 6, height 4:
   (a) 10    (b) 12    (c) 24    (d) 14

6. 25% of 200 = ?
   (a) 50    (b) 75    (c) 100    (d) 25

7. Solve: 2x + 5 = 17
   (a) x=4    (b) x=5    (c) x=6    (d) x=7

8. Cube of 5 = ?
   (a) 25    (b) 75    (c) 125    (d) 100

9. (-3)² = ?
   (a) -9    (b) 9    (c) -6    (d) 6

10. Median of 3, 5, 7, 9, 11:
    (a) 5    (b) 7    (c) 9    (d) 8

11. P(getting even on die) = ?
    (a) 1/6    (b) 1/3    (c) 1/2    (d) 2/3

12. Perimeter of rectangle 8×5:
    (a) 13    (b) 26    (c) 40    (d) 30

13. 1 km = ___ m
    (a) 100    (b) 1000    (c) 10000    (d) 10

14. Volume of cube with side 4:
    (a) 16    (b) 32    (c) 64    (d) 48

15. Compound interest formula:
    (a) P+R+T    (b) PRT/100    (c) P(1+R/100)^T    (d) None

Section B - Short Answer (3 marks each) - Total: 30 marks

16. Solve: 3x - 7 = 14
17. Factor: x² + 5x + 6
18. Simplify: (2x+3)(x-1)
19. Find HCF of 24 and 36
20. Find compound interest on ₹1000 at 5% for 2 years
21. Simplify: 2(x+3) - 3(x-1)
22. Find area of circle with radius 7 cm
23. Calculate: 0.5 × 0.4
24. Find x: x/5 + 3 = 8
25. Mean of 12, 15, 18, 21, 24

Section C - Long Answer (5 marks each) - Total: 30 marks

26. Solve and verify: 3(2x+1) = 4x + 7

27. The sum of three consecutive numbers is 51. Find the numbers.

28. Find the surface area of a cuboid 10cm × 5cm × 4cm

29. A rectangular field is 30m long and 20m wide. Calculate:
    (a) Area
    (b) Perimeter
    (c) Cost of fencing at ₹50/m

30. Solve: x/2 + x/3 = 10

31. Find compound interest on ₹5000 at 10% per annum for 2 years.

Section D - Application Based (5 marks each) - Total: 25 marks

32. A shopkeeper bought 100 oranges for ₹500. He sold them at ₹6 each.
    (a) Find total selling price
    (b) Find profit
    (c) Find profit percentage

33. A car travels 240 km in 4 hours. Find its speed.
    Also find time to travel 360 km at same speed.

34. A water tank is 10m long, 6m wide, 3m deep.
    (a) Find capacity in liters (1m³ = 1000L)
    (b) If full and 2000 liters used, how much left?

35. In a class of 40 students, 25 like cricket, 18 like football.
    10 like both.
    (a) How many like only cricket?
    (b) How many like neither?

36. Construct a square with side 6 cm. Find its diagonal.

ALL THE BEST!'''},

    # Grade 10 - Math
    {
        'grade': 10, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Mathematics Board Exam 2023',
        'description': 'CBSE Class 10 Mathematics Board Examination',
        'content': '''GRADE 10 MATHEMATICS - BOARD EXAMINATION
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - Total: 20 marks

1. Which is irrational?
   (a) √4    (b) √9    (c) √7    (d) √16

2. HCF of 12, 16:
   (a) 2    (b) 4    (c) 8    (d) 16

3. p(x) = x² - 4 has zeros:
   (a) 0,1    (b) 2,-2    (c) 4,-4    (d) 1,-1

4. sin 30° = ?
   (a) 0    (b) 1/2    (c) √3/2    (d) 1

5. tan 45° = ?
   (a) 0    (b) 1    (c) √3    (d) ∞

6. cos²θ + sin²θ = ?
   (a) 0    (b) 1    (c) 2    (d) tan θ

7. AP: 2,5,8,11,... common difference = ?
   (a) 1    (b) 2    (c) 3    (d) 4

8. 5th term of AP: 3,7,11,...:
   (a) 15    (b) 19    (c) 23    (d) 27

9. Discriminant of x² - 5x + 6 = 0:
   (a) 1    (b) 5    (c) -1    (d) 0

10. Roots of x² - 5x + 6 = 0:
    (a) 1,6    (b) 2,3    (c) 3,4    (d) 1,5

11. Distance between (0,0) and (3,4):
    (a) 4    (b) 5    (c) 6    (d) 7

12. Slope of line y = 3x + 2:
    (a) 1    (b) 2    (c) 3    (d) 4

13. Mean of 10,20,30,40:
    (a) 20    (b) 25    (c) 30    (d) 35

14. Mode of 2,3,5,3,7,3,9:
    (a) 2    (b) 3    (c) 5    (d) 7

15. P(head in coin toss):
    (a) 0    (b) 1/4    (c) 1/2    (d) 1

16. Area of circle (r=7):
    (a) 49    (b) 154    (c) 49π    (d) 22/7

17. Volume of sphere = ?
    (a) 4πr²    (b) (4/3)πr³    (c) πr²h    (d) πr³

18. 1° = ___ minutes
    (a) 30    (b) 60    (c) 90    (d) 100

19. Median of grouped data:
    (a) L+[(n/2-cf)/f]h    (b) L+(f-cf)h    (c) 2(M-X)/X    (d) None

20. Standard form quadratic:
    (a) ax+b=0    (b) ax²+bx+c=0    (c) y=mx+c    (d) None

Section B - Short Answer-I (2 marks each) - Total: 12 marks

21. Find HCF and LCM of 6 and 20.

22. Find zeros of x² - 4x + 3.

23. Solve: 2x + 3y = 8, 4x + 6y = 16

24. Find sin θ if cos θ = 3/5.

25. Find AP whose 1st term is 5, common difference 3. Find 10th term.

26. Find probability of getting prime number on die roll.

Section C - Short Answer-II (3 marks each) - Total: 18 marks

27. Prove √3 is irrational.

28. Divide 3x³ + x² + 2x + 5 by x² + 2x + 1.

29. Find 11th term and sum of first 11 terms of AP: 7, 12, 17, 22,...

30. Find roots of quadratic equation: x² - 7x + 12 = 0

31. Find distance between (4,7) and (1,3).
    Find midpoint also.

32. Prove: (1+tan²θ)(1-sin θ)(1+sin θ) = 1

Section D - Long Answer (5 marks each) - Total: 20 marks

33. Prove: Tangents from external point to circle are equal.

34. Find mean, median, mode of:
    Marks: 20-30, 30-40, 40-50, 50-60, 60-70
    Frequency: 5, 10, 20, 8, 7

35. A ladder 13m long reaches a window 12m high.
    Find distance of foot of ladder from wall.

36. Two players A and B throw a die alternately starting with A.
    Find probability A wins (game ends when someone gets 6).

Section E - Case Study (5 marks each) - Total: 10 marks

37. In a sale, prices reduce by 20%. A shirt's original price is ₹500.
    (a) Find sale price
    (b) Calculate savings
    (c) If you have ₹1000, how many shirts can you buy?

38. A tower casts a shadow of 10m at angle 30° to ground.
    (a) Find height of tower
    (b) Find length of slope from sun to ground

ALL THE BEST!'''},

    # Grade 10 - Science
    {
        'grade': 10, 'subject': 'Science', 'year': 2023,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Science Board Exam 2023',
        'description': 'CBSE Class 10 Science Board Examination',
        'content': '''GRADE 10 SCIENCE - BOARD EXAMINATION
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - Total: 20 marks

1. Photosynthesis happens in:
   (a) Mitochondria  (b) Chloroplast  (c) Nucleus  (d) Vacuole

2. Heart has ___ chambers:
   (a) 2  (b) 3  (c) 4  (d) 5

3. Xylem transports:
   (a) Food  (b) Water  (c) Air  (d) Both food and water

4. Photosynthesis equation:
   (a) CO2+H2O→glucose+O2  (b) O2+glucose→CO2+H2O  (c) Both  (d) None

5. Insulin is produced by:
   (a) Liver  (b) Heart  (c) Pancreas  (d) Kidney

6. SI unit of force:
   (a) Pascal  (b) Newton  (c) Joule  (d) Watt

7. Atomic number of carbon:
   (a) 4  (b) 5  (c) 6  (d) 7

8. Symbol of sodium:
   (a) S  (b) So  (c) Na  (d) Sa

9. pH of neutral solution:
   (a) 0  (b) 7  (c) 10  (d) 14

10. Rusting of iron is:
    (a) Physical  (b) Chemical  (c) Both  (d) None

11. Charge of electron:
    (a) Positive  (b) Negative  (c) Zero  (d) Variable

12. SI unit of electric current:
    (a) Watt  (b) Volt  (c) Ohm  (d) Ampere

13. Magnification of plane mirror:
    (a) 0  (b) 1  (c) 2  (d) Infinite

14. White light is made of:
    (a) 3 colors  (b) 5 colors  (c) 7 colors  (d) 10 colors

15. Renewable energy source:
    (a) Coal  (b) Petroleum  (c) Solar  (d) Natural gas

16. Mendel was famous for:
    (a) Physics  (b) Chemistry  (c) Genetics  (d) Astronomy

17. Photosynthesis byproduct:
    (a) CO2  (b) Water  (c) Oxygen  (d) Hydrogen

18. Force of attraction between molecules:
    (a) Friction  (b) Gravity  (c) Cohesion  (d) Adhesion

19. Power formula:
    (a) V×I  (b) V/I  (c) IR  (d) All correct (V=IR)

20. Stomata are found in:
    (a) Roots  (b) Stem  (c) Leaves  (d) Flowers

Section B - Very Short Answer (2 marks each) - Total: 12 marks

21. Define photosynthesis. Write its chemical equation.

22. Differentiate between aerobic and anaerobic respiration.

23. Balance: Fe + O2 → Fe2O3

24. Define power of accommodation of eye.

25. State Ohm's Law.

26. Why is iron called transition element?

Section C - Short Answer (3 marks each) - Total: 18 marks

27. Explain how blood circulates in human heart.

28. What is rusting? How can we prevent it?

29. Explain reflection of light by spherical mirrors.

30. Difference between AC and DC current.

31. What are the three R's of waste management?

32. Explain why arteries have thick walls compared to veins.

Section D - Long Answer (5 marks each) - Total: 20 marks

33. Describe the structure and function of human heart with diagram.

34. Explain types of chemical reactions with examples.
    Give one example each of:
    (a) Combination
    (b) Decomposition
    (c) Displacement
    (d) Double displacement

35. Describe reflex action with examples and pathway.

36. Explain electromagnetic induction. State Faraday's law.

Section E - Case Study (5 marks each) - Total: 10 marks

37. A student observes a tree losing leaves in dry season.
    (a) Why do plants lose leaves?
    (b) Is this beneficial? How?
    (c) Name 2 such plants

38. An electric heater is used for 2 hours daily at 1000W.
    (a) Find energy consumed in kWh
    (b) Calculate monthly cost at ₹5/kWh (30 days)
    (c) Suggest 3 ways to save electricity

ALL THE BEST!'''},

    # Grade 10 - English
    {
        'grade': 10, 'subject': 'English', 'year': 2023,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 English Board Exam 2023',
        'description': 'CBSE Class 10 English Board Examination',
        'content': '''GRADE 10 ENGLISH - BOARD EXAMINATION
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - Reading (20 marks)

Read the passage and answer questions:

"Climate change is one of the most pressing challenges of our time. Rising global temperatures are causing ice caps to melt, sea levels to rise, and weather patterns to become increasingly unpredictable. Forest fires, droughts, and floods are becoming more frequent. This is largely due to human activities like burning fossil fuels, deforestation, and industrial pollution. We must take immediate action by using renewable energy, planting trees, reducing waste, and adopting sustainable lifestyles. Every small action counts. If we don't act now, future generations will face severe consequences."

1. What is the passage mainly about? (2 marks)

2. List two effects of climate change mentioned. (2 marks)

3. What are the main causes? (2 marks)

4. Suggest three actions individuals can take. (3 marks)

5. What is meant by "sustainable lifestyles"? (2 marks)

6. Find a word from the passage that means "urgent/important". (1 mark)

7. Find an antonym for "increase" from the passage. (1 mark)

Passage 2: (7 marks)

[Another reading passage with 4-5 questions on factual recall and inference]

Section B - Writing (20 marks)

8. (5 marks)
You are Ravi/Riya, a student of Class 10. Write a letter to the editor of a newspaper expressing concern about increasing pollution in your city and suggesting solutions.

9. (5 marks)
Write a notice for your school notice board about the upcoming Annual Sports Day.

10. (5 marks)
Write an article on "Importance of Reading Books" for the school magazine.

11. (5 marks)
You are the school captain. Write a paragraph on "My Role as School Captain."

Section C - Grammar (10 marks)

12. Fill in the blanks with correct verb forms: (2 marks)
   (a) She _____ (go) to school yesterday.
   (b) They _____ (play) cricket now.

13. Change to passive voice: (2 marks)
    "Ravi wrote a letter."

14. Combine the sentences: (2 marks)
    "He worked hard. He passed."

15. Convert to direct/indirect speech: (2 marks)
    She said, "I am happy."

16. Find errors and correct: (2 marks)
    "Me and my friend goes to school daily."

Section D - Literature (30 marks)

(Questions on prescribed textbook lessons - First Flight & Footprints)

17. Answer briefly: (Each 2 marks - 10 marks total)
    Five questions on themes, characters, and events from chapters.

18. Long answer: (Each 5 marks - 10 marks total)
    Two detailed analytical questions on literary works.

19. Poetry analysis: (Each 5 marks - 10 marks total)
    Two questions on prescribed poems.

ALL THE BEST!'''},

    # Grade 7 Paper
    {
        'grade': 7, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 120, 'total_marks': 80,
        'title': 'Grade 7 Mathematics Annual 2023',
        'description': 'Annual examination for Class 7 Mathematics',
        'content': '''GRADE 7 MATHEMATICS - ANNUAL EXAMINATION
Year: 2023
Time: 2 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - Total: 10 marks

1. (-7) + (+3) = ?
   (a) 10  (b) -10  (c) 4  (d) -4

2. 3/4 + 1/4 = ?
   (a) 1  (b) 2  (c) 4/8  (d) 1/2

3. 25% of 80 = ?
   (a) 15  (b) 20  (c) 25  (d) 30

4. 2x + 5 = 11, x = ?
   (a) 2  (b) 3  (c) 4  (d) 8

5. Acute angle is:
   (a) >90°  (b) =90°  (c) <90°  (d) =180°

6. Perimeter of square (side=5):
   (a) 10  (b) 20  (c) 25  (d) 30

7. Area of triangle base=6, height=4:
   (a) 10  (b) 12  (c) 24  (d) 14

8. 0.5 = ?
   (a) 1/2  (b) 1/4  (c) 5/10  (d) Both A and C

9. Probability of head in toss:
   (a) 1  (b) 1/2  (c) 1/3  (d) 0

10. LCM of 6 and 8:
    (a) 12  (b) 18  (c) 24  (d) 48

Section B - Short Answer (3 marks each) - Total: 30 marks

11. Find: (-8) + (-5) + 12

12. Solve: x/3 = 9

13. Simplify: 2a + 3b - 5a + 4b

14. Find LCM of 12, 16

15. Add fractions: 2/3 + 3/4

16. Multiply: 3/4 × 8/9

17. Find: 30% of 250

18. Find area of rectangle 8cm × 6cm

19. Convert 7/8 to decimal

20. Find perimeter of triangle: sides 5, 7, 8 cm

Section C - Long Answer (5 marks each) - Total: 25 marks

21. Solve: 4x - 7 = 9

22. The angles of a triangle are in ratio 1:2:3. Find each angle.

23. A car travels 360 km in 6 hours. Find its speed.
    How far will it go in 9 hours?

24. Find compound interest on ₹2000 at 5% for 2 years.

25. Find HCF and LCM of 24 and 36.

Section D - Application (15 marks)

26. (5 marks) A man is 5 times as old as his son. 5 years ago, he was 9 times older. Find their present ages.

27. (5 marks) A rectangular field has length 30m and width 20m.
    (a) Find perimeter
    (b) Find area
    (c) Cost of grass at ₹10/m²

28. (5 marks) In a class of 50 students:
    - 20 like Math
    - 25 like Science
    - 15 like both
    How many like only Math? Only Science? Neither?

ALL THE BEST!'''},
]


def load_extras():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found.")
            return

        os.makedirs('./data/resources', exist_ok=True)
        os.makedirs('./data/question_papers', exist_ok=True)

        # Load extra resources
        existing_resources = {r.title for r in Resource.query.all()}
        res_added = 0

        for res_data in EXTRA_RESOURCES:
            if res_data['title'] in existing_resources:
                continue

            filename = f"ncert_g{res_data['grade']}_{res_data['subject'].replace(' ', '_')}_{res_data['title'].replace(' ', '_').replace('/', '_')[:40]}.txt"
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
            res_added += 1
            print(f"[RES] Grade {res_data['grade']} {res_data['subject']}: {res_data['title']}")

        # Load question papers
        db.create_all()  # Ensure question_papers table exists
        existing_papers = {p.title for p in QuestionPaper.query.all()}
        papers_added = 0

        for paper_data in QUESTION_PAPERS:
            if paper_data['title'] in existing_papers:
                continue

            filename = f"paper_g{paper_data['grade']}_{paper_data['subject'].replace(' ', '_')}_{paper_data['year']}.txt"
            file_path = f"data/question_papers/{filename}"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(paper_data['content'])

            file_size = os.path.getsize(file_path)

            paper = QuestionPaper(
                title=paper_data['title'],
                description=paper_data['description'],
                subject=paper_data['subject'],
                grade_level=paper_data['grade'],
                year=paper_data['year'],
                exam_type=paper_data['exam_type'],
                duration_minutes=paper_data['duration'],
                total_marks=paper_data['total_marks'],
                file_path=file_path,
                content_type='txt',
                file_size=file_size,
                created_by=teacher.id,
                is_published=True
            )
            db.session.add(paper)
            papers_added += 1
            print(f"[PAPER] Grade {paper_data['grade']} {paper_data['subject']} {paper_data['year']}")

        db.session.commit()

        print(f"\n========================================")
        print(f"[COMPLETE]")
        print(f"  Resources added: {res_added}")
        print(f"  Question papers added: {papers_added}")
        print(f"  Total resources: {Resource.query.count()}")
        print(f"  Total quizzes: still 80")
        print(f"  Total question papers: {QuestionPaper.query.count()}")
        print(f"========================================")


if __name__ == '__main__':
    try:
        load_extras()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
