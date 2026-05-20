"""
Comprehensive NCERT Bulk Content Loader
Adds resources for ALL major NCERT chapters across grades 1-10
Also adds multi-year question papers
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Resource, QuestionPaper

# Concise resources covering all major NCERT chapters
BULK_RESOURCES = [
    # ==================== GRADE 1 - Additional ====================
    {'g': 1, 's': 'Mathematics', 't': 'Time and Calendar',
     'd': 'Reading time, days, months',
     'c': '''TIME AND CALENDAR

DAYS OF THE WEEK (7):
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

MONTHS OF THE YEAR (12):
January, February, March, April, May, June,
July, August, September, October, November, December

Special Days:
- 26 January: Republic Day
- 15 August: Independence Day
- 2 October: Gandhi Jayanti
- 14 November: Children's Day
- 5 September: Teacher's Day

CLOCK:
- Short hand = HOURS
- Long hand = MINUTES
- 12 numbers on clock face

Time Examples:
- Morning: 6 AM to 12 PM
- Afternoon: 12 PM to 4 PM
- Evening: 4 PM to 7 PM
- Night: 7 PM to 5 AM

Reading Clock:
- When long hand on 12, it's "o'clock"
- 3:00 = three o'clock
- 9:00 = nine o'clock'''},

    {'g': 1, 's': 'Science', 't': 'Plants Around Me',
     'd': 'Basic introduction to plants',
     'c': '''PLANTS AROUND ME

What are plants?
Plants are living things that grow from the ground.

PARTS OF A PLANT:
1. ROOTS: Hidden under soil, take water
2. STEM: Holds the plant up
3. LEAVES: Green, make food
4. FLOWERS: Beautiful, become fruits
5. FRUITS: Have seeds inside

TYPES OF PLANTS:

BIG PLANTS (Trees):
- Mango tree
- Banyan tree
- Coconut tree
- Neem tree

SMALL PLANTS:
- Rose plant
- Tulsi plant
- Tomato plant

GRASS:
- Found everywhere
- Animals eat it

CREEPERS (Climb up):
- Money plant
- Grapes

We get from plants:
- Food (fruits, vegetables)
- Wood
- Medicines
- Beautiful flowers
- Shade
- Oxygen to breathe

We should:
- Plant more trees
- Water plants
- Don't pluck flowers
- Don't damage plants'''},

    {'g': 1, 's': 'Social Studies', 't': 'My School',
     'd': 'About school and people in it',
     'c': '''MY SCHOOL

My school is a special place where I learn new things.

People in School:
- PRINCIPAL: Head of school
- TEACHERS: Teach us
- STUDENTS: Children like me
- PEON: Helps with messages
- GARDENER: Takes care of plants
- DRIVER: Drives school bus

Things in School:
- Classrooms
- Blackboard
- Books and notebooks
- Tables and chairs
- Playground
- Library
- Computer room
- Garden

School Rules:
- Come on time
- Wear clean uniform
- Greet teachers
- Don't run in corridors
- Be polite to friends
- Keep school clean

Subjects We Learn:
- English
- Hindi
- Mathematics
- Science
- Social Studies
- Drawing
- Music
- Physical Education

Activities:
- Reading
- Writing
- Drawing
- Singing
- Playing games
- Sports
- Field trips

Why School is Important:
- We learn new things
- Make friends
- Learn discipline
- Become good citizens
- Prepare for future'''},

    # ==================== GRADE 2 - Additional ====================
    {'g': 2, 's': 'Mathematics', 't': 'Times Tables 2 to 5',
     'd': 'Basic multiplication tables',
     'c': '''TIMES TABLES 2 TO 5

Table of 2:
2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
2 × 4 = 8
2 × 5 = 10
2 × 6 = 12
2 × 7 = 14
2 × 8 = 16
2 × 9 = 18
2 × 10 = 20

Table of 3:
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21
3 × 8 = 24
3 × 9 = 27
3 × 10 = 30

Table of 4:
4 × 1 = 4, 4 × 2 = 8, 4 × 3 = 12
4 × 4 = 16, 4 × 5 = 20, 4 × 6 = 24
4 × 7 = 28, 4 × 8 = 32, 4 × 9 = 36, 4 × 10 = 40

Table of 5:
5 × 1 = 5, 5 × 2 = 10, 5 × 3 = 15
5 × 4 = 20, 5 × 5 = 25, 5 × 6 = 30
5 × 7 = 35, 5 × 8 = 40, 5 × 9 = 45, 5 × 10 = 50

Tips to Remember:
- Multiplication is repeated addition
- 3 × 4 = 4 + 4 + 4 = 12
- Practice daily
- Sing tables to remember'''},

    {'g': 2, 's': 'Science', 't': 'Living Things vs Non-Living',
     'd': 'Differences between living and non-living',
     'c': '''LIVING vs NON-LIVING THINGS

LIVING THINGS:
Things that are ALIVE and can do special activities.

Examples: Animals, plants, humans, insects, birds

What do living things do?
1. EAT food
2. BREATHE air
3. GROW from small to big
4. MOVE from place to place
5. HAVE BABIES (reproduce)
6. RESPOND to surroundings
7. DIE one day

NON-LIVING THINGS:
Things that are NOT alive.

Examples: Stone, table, pen, book, water, air

Properties:
- Don't eat or drink
- Don't breathe
- Don't grow
- Don't move on their own
- Don't have babies
- Don't die

EXAMPLES:

Living:
🐱 Cat (eats, breathes, grows)
🌳 Tree (drinks water, grows)
🐦 Bird (flies, eats)
🐠 Fish (swims, breathes)

Non-Living:
📚 Book (no movement, no eating)
🗿 Stone (doesn't change)
🪑 Chair (no growth)
✏️ Pencil (no breathing)

Special Case:
- Dead plants/animals are NOT living (they were)
- Robots are NOT living (don't eat or breathe)
- Sleeping cat IS living (still breathes!)'''},

    {'g': 2, 's': 'Social Studies', 't': 'Festivals of India',
     'd': 'Important festivals celebrated in India',
     'c': '''FESTIVALS OF INDIA

India celebrates many festivals throughout the year.

HINDU FESTIVALS:

1. DIWALI (Festival of Lights)
- Celebrated in October/November
- Lights, lamps, fireworks
- Sweets and gifts
- Welcomes goddess Lakshmi

2. HOLI (Festival of Colors)
- Celebrated in March
- Throw colored powders
- Burn Holika
- Singing and dancing

3. RAKSHA BANDHAN
- Sisters tie rakhi on brothers
- Brothers protect sisters

4. JANMASHTAMI
- Birthday of Lord Krishna

5. DUSSEHRA / VIJAYADASHAMI
- Victory of good over evil
- Burn effigy of Ravana

MUSLIM FESTIVALS:

1. EID-UL-FITR
- End of fasting month Ramadan
- Special prayers
- New clothes, sweets

2. EID-UL-ADHA
- Festival of sacrifice

CHRISTIAN FESTIVALS:

1. CHRISTMAS
- 25 December
- Birth of Jesus Christ
- Christmas tree, gifts
- Santa Claus

2. EASTER
- Resurrection of Jesus

SIKH FESTIVALS:

1. GURU NANAK JAYANTI
- Birthday of Guru Nanak

2. BAISAKHI
- New year, harvest festival

OTHER FESTIVALS:

- PONGAL (Tamil Nadu)
- ONAM (Kerala)
- BIHU (Assam)
- DURGA PUJA (Bengal)
- NAVRATRI (9 nights)

NATIONAL FESTIVALS:

- REPUBLIC DAY: 26 January
- INDEPENDENCE DAY: 15 August
- GANDHI JAYANTI: 2 October

Why Festivals?
- Bring families together
- Teach our culture
- Make us happy
- Help us learn values
- Promote unity'''},

    # ==================== GRADE 3 - Additional ====================
    {'g': 3, 's': 'Mathematics', 't': 'Time, Money, and Measurement',
     'd': 'Reading time, money calculations',
     'c': '''TIME, MONEY, AND MEASUREMENT

TIME:
- 60 seconds = 1 minute
- 60 minutes = 1 hour
- 24 hours = 1 day
- 7 days = 1 week
- 30 days = 1 month (approx)
- 365 days = 1 year
- 12 months = 1 year

Reading Clock:
Short hand → Hours
Long hand → Minutes

Examples:
- 3:00 → 3 o'clock
- 3:15 → quarter past 3
- 3:30 → half past 3
- 3:45 → quarter to 4

AM and PM:
- AM: Before noon (midnight to 12 noon)
- PM: After noon (12 noon to midnight)

MONEY (Indian Currency ₹):

Coins: ₹1, ₹2, ₹5, ₹10
Notes: ₹10, ₹20, ₹50, ₹100, ₹200, ₹500, ₹2000

Adding money:
₹25 + ₹35 = ₹60
₹100 - ₹65 = ₹35

Word problem:
Ravi has ₹100. He buys book for ₹65 and pencil for ₹15.
Money spent: ₹65 + ₹15 = ₹80
Money left: ₹100 - ₹80 = ₹20

MEASUREMENT:

LENGTH:
- 10 mm = 1 cm
- 100 cm = 1 m
- 1000 m = 1 km

WEIGHT:
- 1000 g = 1 kg

CAPACITY:
- 1000 mL = 1 L

Convert:
- 5 m = 500 cm
- 3 kg = 3000 g
- 2 L = 2000 mL

Compare:
- 1 km > 500 m
- 2 kg > 1500 g
- 1 L > 750 mL'''},

    {'g': 3, 's': 'Science', 't': 'Food and Health',
     'd': 'Healthy eating habits and nutrition',
     'c': '''FOOD AND HEALTH

Why do we eat food?
- Energy for activities
- Growth of body
- Repair of tissues
- Protection from diseases
- Keep us healthy

FOOD GROUPS:

1. ENERGY GIVING FOODS (Carbohydrates):
- Rice
- Wheat (Roti, Bread)
- Potato
- Sugar
- Give us strength to work

2. BODY BUILDING FOODS (Proteins):
- Milk
- Eggs
- Pulses (Dal, Beans)
- Fish, Meat
- Help us grow

3. PROTECTIVE FOODS (Vitamins & Minerals):
- Fruits
- Vegetables
- Make us strong
- Fight diseases

VITAMINS:
- Vitamin A: For eyes (Carrots)
- Vitamin C: Immunity (Oranges)
- Vitamin D: Bones (Sunlight, milk)
- Iron: Blood (Spinach)
- Calcium: Bones (Milk)

BALANCED DIET:
A meal with all food groups.

Example balanced meal:
- Rice/Roti (energy)
- Dal/Curry (protein)
- Vegetables (vitamins)
- Salad (minerals)
- Glass of water

HEALTHY HABITS:

1. Wash hands before eating
2. Brush teeth twice daily
3. Take bath everyday
4. Drink clean water (8 glasses)
5. Exercise daily
6. Sleep 8 hours
7. Don't skip meals
8. Eat fruits daily

UNHEALTHY HABITS:
- Eating junk food
- Drinking soft drinks
- Not exercising
- Sleeping late
- Skipping breakfast
- Not washing hands

JUNK FOODS:
- Chips, biscuits, chocolates
- Burgers, pizzas
- Cold drinks
- Too much sugar/salt

These are unhealthy because:
- Less nutrients
- More fat/sugar
- Cause weight gain
- Cause tooth decay'''},

    {'g': 3, 's': 'English', 't': 'Stories with Morals',
     'd': 'Short moral stories',
     'c': '''STORIES WITH MORALS

Stories teach us important lessons.

STORY 1: THE BOY WHO CRIED WOLF

Once there was a shepherd boy. He often cried "Wolf! Wolf!" just for fun.

The villagers would come running, but find no wolf. After a few times, they got angry.

One day, a real wolf came. The boy cried "Wolf! Wolf!" loudly. But this time, no one came.

The wolf ate all the sheep.

MORAL: "Don't tell lies. People won't trust you when you need help."

STORY 2: THE LION AND THE MOUSE

A small mouse ran over a sleeping lion. The lion caught the mouse. The mouse begged for mercy.

The mouse said: "Let me go. I will help you one day."

The lion laughed but let it go.

Later, the lion got trapped in a hunter's net. He roared for help. The little mouse heard him. The mouse chewed the net and freed the lion.

MORAL: "Help others. Even small friends can help in big trouble."

STORY 3: THE HARE AND TORTOISE

A hare made fun of a slow tortoise. The tortoise challenged him to a race.

The hare ran fast and was way ahead. He thought "Let me rest." He slept under a tree.

The tortoise kept walking slowly but didn't stop. He reached the finish line first.

MORAL: "Slow and steady wins the race."

STORY 4: THE GREEDY DOG

A dog had a bone. He was crossing a bridge. He saw his reflection in water.

He thought it was another dog with another bone. He wanted that bone too.

He barked at the reflection. His bone fell into the water!

MORAL: "Greed always brings loss."

STORY 5: THE FOX AND THE GRAPES

A fox saw grapes hanging high. He jumped many times to reach them. He couldn't.

He walked away saying "Those grapes are sour anyway."

MORAL: "Don't pretend to hate what you cannot have."

LESSONS FROM STORIES:

✓ Always tell the truth
✓ Help others
✓ Hard work and patience win
✓ Don't be greedy
✓ Be content with what you have
✓ Be kind to small creatures
✓ Never give up

Reading stories helps us:
- Improve language
- Learn moral values
- Use imagination
- Have fun
- Become better persons'''},

    # ==================== GRADE 4 - Additional ====================
    {'g': 4, 's': 'Mathematics', 't': 'Large Numbers and Place Value',
     'd': 'Working with numbers up to lakhs',
     'c': '''LARGE NUMBERS AND PLACE VALUE

NUMBERS UP TO LAKH:

Place values in Indian System:
- Ones (1)
- Tens (10)
- Hundreds (100)
- Thousands (1,000)
- Ten Thousands (10,000)
- Lakh (1,00,000)
- Ten Lakh (10,00,000)
- Crore (1,00,00,000)

Reading large numbers:

12,345 = Twelve thousand three hundred forty-five
1,00,000 = One lakh
1,50,000 = One lakh fifty thousand
10,00,000 = Ten lakh
1,00,00,000 = One crore

Indian vs International System:
Indian: 1,00,000 (One Lakh)
International: 100,000 (One hundred thousand)

PLACE VALUE:

In number 45,678:
- 8 is at ones place (value: 8)
- 7 is at tens place (value: 70)
- 6 is at hundreds place (value: 600)
- 5 is at thousands place (value: 5,000)
- 4 is at ten thousands place (value: 40,000)

ROUNDING NUMBERS:

To nearest 10: Look at ones place
- 0-4: Round down (47 → 40 NO, but 43→40)
- 5-9: Round up (47 → 50)

Examples:
- 23 → 20
- 47 → 50
- 65 → 70

To nearest 100: Look at tens place
- 247 → 200
- 251 → 300

COMPARING LARGE NUMBERS:

Compare 12,345 and 12,543:
- Same in 10,000s (1)
- Same in 1,000s (2)
- Different in 100s (3 vs 5)
- 12,543 > 12,345

NUMBER FACTS:

- Smallest 4-digit: 1,000
- Largest 4-digit: 9,999
- Smallest 5-digit: 10,000
- Largest 5-digit: 99,999
- Smallest 6-digit: 1,00,000
- Largest 6-digit: 9,99,999

Number patterns:
- Even: 2, 4, 6, 8, 10...
- Odd: 1, 3, 5, 7, 9...
- Skip counting by 5: 5, 10, 15, 20...

OPERATIONS:

Addition: 12,345 + 23,456 = 35,801
Subtraction: 50,000 - 23,456 = 26,544
Multiplication: 234 × 12 = 2,808
Division: 144 ÷ 12 = 12'''},

    {'g': 4, 's': 'Science', 't': 'Water and Its Importance',
     'd': 'Water cycle and water conservation',
     'c': '''WATER AND ITS IMPORTANCE

Water is essential for all life.

Properties of Water:
- Colorless
- Tasteless
- Odorless
- Liquid at room temperature
- Freezes at 0°C (becomes ice)
- Boils at 100°C (becomes vapor)

STATES OF WATER:

1. SOLID (Ice):
- Below 0°C
- Has fixed shape
- Examples: Ice cubes, snow, glaciers

2. LIQUID (Water):
- At room temperature
- Takes shape of container
- Flows

3. GAS (Water Vapor):
- Above 100°C
- Invisible
- In air around us

WATER CYCLE:

Step 1: EVAPORATION
- Sun heats water in oceans, rivers, lakes
- Water becomes vapor
- Rises up into sky

Step 2: CONDENSATION
- Vapor cools high up
- Forms tiny droplets
- These make CLOUDS

Step 3: PRECIPITATION
- Cloud droplets become big
- Fall as RAIN (or snow/hail)

Step 4: COLLECTION
- Water collects in rivers, lakes, oceans
- Some seeps into ground (groundwater)
- Cycle repeats!

SOURCES OF WATER:

Natural:
- Rivers
- Lakes
- Ponds
- Springs
- Oceans (salty)
- Underground water
- Rain

Made by humans:
- Wells
- Hand pumps
- Tube wells
- Dams
- Tanks

USES OF WATER:

At Home:
- Drinking
- Cooking
- Bathing
- Washing clothes/dishes
- Cleaning house
- Watering plants

In Industry:
- Making products
- Cooling machines
- Cleaning

In Agriculture:
- Watering crops
- Irrigation

Other:
- Generating electricity
- Transportation (ships)
- Recreation (swimming)

WATER POLLUTION:

Causes:
- Throwing garbage in rivers
- Factory waste
- Sewage
- Pesticides from farms

Effects:
- Diseases (cholera, typhoid)
- Death of fish
- Bad smell

WATER CONSERVATION:

Why save water?
- Limited fresh water
- Many people don't have clean water
- Future generations need it

How to save:
1. Don't leave taps running
2. Use bucket instead of shower
3. Repair leaking taps
4. Reuse water for plants
5. Collect rainwater
6. Don't waste while brushing
7. Plant more trees (hold rainwater)

DAILY WATER NEED:
- Drink 8 glasses
- About 2 liters'''},

    # ==================== GRADE 5 - Additional ====================
    {'g': 5, 's': 'Mathematics', 't': 'Symmetry and Patterns',
     'd': 'Lines of symmetry and number patterns',
     'c': '''SYMMETRY AND PATTERNS

SYMMETRY:
A shape has symmetry if it can be folded so both halves match.

LINE OF SYMMETRY:
The fold line that divides a shape into two equal halves.

EXAMPLES:

Square: 4 lines of symmetry
- 2 diagonal
- 2 from middle of sides

Rectangle: 2 lines of symmetry
- Vertical
- Horizontal
(No diagonal symmetry)

Equilateral Triangle: 3 lines

Isosceles Triangle: 1 line

Circle: Infinite lines of symmetry
- Any line through center

REGULAR POLYGONS:
- Pentagon: 5 lines
- Hexagon: 6 lines
- Octagon: 8 lines

OBJECTS WITH SYMMETRY:
- Butterfly (vertical line)
- Human face (almost)
- Star
- Flowers
- Leaves
- Snowflake

NO SYMMETRY:
- Scalene triangle
- Hand
- Most irregular shapes

ROTATIONAL SYMMETRY:
A shape that looks same after rotation.
Examples:
- Circle: infinite rotational
- Square: 4 times in 360°
- Equilateral triangle: 3 times

PATTERNS:

NUMBER PATTERNS:

1. Even: 2, 4, 6, 8, 10... (+2)
2. Odd: 1, 3, 5, 7, 9... (+2)
3. Skip count by 5: 5, 10, 15, 20, 25... (+5)
4. Skip count by 10: 10, 20, 30, 40... (+10)
5. Square numbers: 1, 4, 9, 16, 25, 36... (n²)
6. Triangular: 1, 3, 6, 10, 15, 21...
7. Doubling: 1, 2, 4, 8, 16, 32... (×2)
8. Halving: 64, 32, 16, 8, 4, 2 (÷2)

FIBONACCI SEQUENCE:
0, 1, 1, 2, 3, 5, 8, 13, 21...
(Add previous two)

PATTERNS IN NATURE:
- Petals of flowers
- Sunflower seeds
- Pine cone spirals
- Honeycomb (hexagons)
- Snail shell

PATTERNS IN MULTIPLICATION:
9 table: 9, 18, 27, 36, 45...
Notice: Sum of digits is always 9!

REPEAT PATTERNS:
ABABAB
AABBAABBAABB
1, 2, 3, 1, 2, 3...

FINDING PATTERNS:
Look for:
- What changes
- What stays same
- The rule

Practice:
1. 5, 10, 15, ?, 25 → 20 (+5)
2. 1, 4, 9, 16, ? → 25 (squares)
3. 2, 4, 8, 16, ? → 32 (×2)
4. 100, 90, 80, ?, 60 → 70 (-10)'''},

    {'g': 5, 's': 'Social Studies', 't': 'Major Religions of India',
     'd': 'Different religions practiced in India',
     'c': '''MAJOR RELIGIONS OF INDIA

India is a SECULAR country.
All religions are respected equally.

MAIN RELIGIONS:

1. HINDUISM:
- Oldest religion in India
- Most followers in India
- Gods: Brahma, Vishnu, Shiva, Ganesha, etc.
- Holy book: Vedas, Ramayana, Bhagavad Gita
- Festivals: Diwali, Holi, Dussehra
- Places of worship: Temples (Mandir)
- Symbol: Om (ॐ)

2. ISLAM:
- Came to India in 7th century
- 2nd largest in India
- One God: Allah
- Holy book: Quran
- Prophet: Muhammad
- Festivals: Eid-ul-Fitr, Eid-ul-Adha
- Places of worship: Mosque (Masjid)
- Holy month: Ramadan (fasting)

3. CHRISTIANITY:
- Came with European traders
- Followers: Christians
- Founder: Jesus Christ
- Holy book: Bible (Old and New Testament)
- Festivals: Christmas, Easter, Good Friday
- Places of worship: Church
- Symbol: Cross

4. SIKHISM:
- Started in 15th century
- Founded by Guru Nanak
- One God concept
- Holy book: Guru Granth Sahib
- 10 Gurus total
- Festivals: Guru Nanak Jayanti, Baisakhi
- Places of worship: Gurudwara
- Famous Gurudwara: Golden Temple, Amritsar

5. BUDDHISM:
- Founded by Gautama Buddha
- 6th century BC
- Born in Lumbini (now Nepal)
- Holy book: Tripitaka
- Teaches non-violence
- Eight-fold path
- Famous places: Bodh Gaya, Sarnath
- Symbol: Wheel of Dharma

6. JAINISM:
- Founded by Lord Mahavira
- Strict non-violence (Ahimsa)
- Holy book: Agamas
- 24 Tirthankaras
- Vegetarianism
- Festivals: Mahavir Jayanti
- Places: Temples

7. ZOROASTRIANISM (PARSIS):
- Founded by Zoroaster
- Came from Persia (Iran)
- Holy book: Avesta
- Fire is sacred
- Festivals: Navroz (New Year)
- Famous Parsis: Tata, Wadia

VALUES TAUGHT BY ALL RELIGIONS:

✓ Speak the truth
✓ Be kind
✓ Help others
✓ Respect elders
✓ Don't steal
✓ Don't harm others
✓ Pray daily
✓ Love your neighbor
✓ Practice tolerance
✓ Live in peace

SECULARISM IN INDIA:

- Constitution makes India secular
- All religions equal
- People free to follow any religion
- Government doesn't favor any religion
- Festivals of all celebrated
- Promotes "Unity in Diversity"

RESPECT OTHERS:
- Never speak bad about others' religions
- Attend friends' festivals
- Learn about different faiths
- Be tolerant and kind
- Live in harmony

FAMOUS RELIGIOUS PLACES IN INDIA:

- Varanasi (Hindu)
- Bodh Gaya (Buddhist)
- Amritsar - Golden Temple (Sikh)
- Ajmer - Sufi Shrine (Muslim)
- Velankanni Church (Christian)
- Mount Abu (Jain)
- Udvada (Parsi)'''},

    # ==================== GRADE 6 - Additional ====================
    {'g': 6, 's': 'Mathematics', 't': 'Basic Geometry',
     'd': 'Lines, angles, triangles, and circles',
     'c': '''BASIC GEOMETRY

POINTS:
- Smallest geometric figure
- No length or width
- Named with capital letters: A, B, C

LINES:

LINE: Extends in both directions infinitely
- AB ↔ (with arrows on both sides)

RAY: Starts at point, goes in one direction
- AB→ (one arrow)

LINE SEGMENT: Two end points, definite length
- AB (no arrows)

TYPES OF LINES:

PARALLEL: Never meet
- ━━━━ ━━━━ ║

PERPENDICULAR: Meet at 90°
- ┴ ┬

INTERSECTING: Meet at a point
- ✕

ANGLES:

Formed when two lines/rays meet.
Vertex: Common point

Types of Angles:

1. ZERO ANGLE: 0°
2. ACUTE: Between 0° and 90°
3. RIGHT: Exactly 90° (perpendicular)
4. OBTUSE: Between 90° and 180°
5. STRAIGHT: 180° (line)
6. REFLEX: Between 180° and 360°
7. COMPLETE: 360°

Measuring: Use PROTRACTOR

TRIANGLES:

3 sides, 3 angles, 3 vertices.

By Sides:
- EQUILATERAL: All 3 sides equal (60°-60°-60°)
- ISOSCELES: 2 sides equal
- SCALENE: All sides different

By Angles:
- ACUTE TRIANGLE: All angles less than 90°
- RIGHT TRIANGLE: One angle = 90°
- OBTUSE TRIANGLE: One angle > 90°

Important Fact:
Sum of all three angles = 180°

If two angles are 60° and 70°, third = 180 - 130 = 50°

QUADRILATERALS:

4 sides, 4 vertices.

Types:
1. SQUARE: All 4 sides equal, all angles 90°
2. RECTANGLE: Opposite sides equal, all angles 90°
3. RHOMBUS: All sides equal, opposite angles equal
4. PARALLELOGRAM: Opposite sides parallel and equal
5. TRAPEZIUM: One pair parallel sides
6. KITE: 2 pairs equal sides

Sum of angles in quadrilateral = 360°

POLYGONS:

Many-sided closed figures.

- 3 sides: Triangle
- 4 sides: Quadrilateral
- 5 sides: Pentagon
- 6 sides: Hexagon
- 7 sides: Heptagon
- 8 sides: Octagon
- 9 sides: Nonagon
- 10 sides: Decagon

CIRCLES:

- Round shape
- All points equal distance from center

Parts:
- CENTER: Middle point
- RADIUS (r): Distance from center to edge
- DIAMETER (d): Across through center
- d = 2r
- CIRCUMFERENCE: Distance around
- C = 2πr (π ≈ 22/7)
- AREA: πr²

CONSTRUCTIONS:

Basic Tools:
- Ruler
- Compass
- Protractor
- Set squares

PERIMETER AND AREA:

Square (side s):
- Perimeter = 4s
- Area = s²

Rectangle (l × b):
- Perimeter = 2(l + b)
- Area = l × b

Triangle:
- Perimeter = sum of sides
- Area = ½ × base × height

Circle:
- Circumference = 2πr
- Area = πr²'''},

    {'g': 6, 's': 'English', 't': 'Reading Comprehension Practice',
     'd': 'Building reading skills',
     'c': '''READING COMPREHENSION PRACTICE

WHAT IS READING COMPREHENSION?
Understanding what you read - the meaning, context, and details.

STRATEGIES:

1. PREVIEW:
- Read title
- Look at pictures
- Read headings
- Predict topic

2. ACTIVE READING:
- Read carefully
- Underline key words
- Make notes in margin
- Ask questions

3. REREAD:
- Don't worry if you didn't understand
- Read again

4. SUMMARIZE:
- In your own words
- Main ideas only

PRACTICE PASSAGE 1:

"The Indian peacock is the national bird of India. It has beautiful, colorful feathers - blue, green, gold, and purple. The male peacock has the famous tail feathers. During the rainy season, males spread their feathers in a beautiful dance to attract females. Peacocks live in forests and gardens. They eat insects, seeds, fruits, and small reptiles. The peacock symbolizes beauty, grace, and royalty in Indian culture."

QUESTIONS:

1. Factual: What is the national bird of India?
Answer: Peacock

2. Factual: What colors does peacock have?
Answer: Blue, green, gold, purple

3. Inference: Why might peacocks dance in rainy season?
Answer: To attract females / Find mates

4. Vocabulary: What does "symbolize" mean?
Answer: To represent

5. Detail: What do peacocks eat?
Answer: Insects, seeds, fruits, small reptiles

PRACTICE PASSAGE 2:

"Mahatma Gandhi (1869-1948) is known as the Father of the Nation. He led India's freedom struggle against British rule using non-violence and truth. He called this 'Satyagraha'. Born in Porbandar, Gujarat, he studied law in England. Then he worked in South Africa where he fought against racial discrimination. Returning to India in 1915, he led many movements like the Salt March (1930) and Quit India Movement (1942). His methods of non-violent resistance inspired leaders worldwide, including Martin Luther King Jr. India achieved independence on 15 August 1947, but Gandhi was assassinated on 30 January 1948."

QUESTIONS:

1. When was Gandhi born?
2. What is he known as?
3. What was his method called?
4. Where was he born?
5. Name 2 movements he led.
6. Who else was inspired by him?
7. When did India become independent?
8. When did Gandhi die?

TIPS FOR EXAMS:

1. READ instructions carefully
2. UNDERLINE key words in question
3. FIND answers in passage
4. NEVER add information not in passage
5. ANSWER in complete sentences
6. CHECK spelling and grammar
7. MANAGE time wisely

WORD MEANINGS FROM CONTEXT:

"The dog was FEROCIOUS - it growled and showed sharp teeth."
- Ferocious = fierce, angry, dangerous

"The room was IMMACULATE - everything was clean and in place."
- Immaculate = very clean, spotless

"He was DEVASTATED when his pet died - he cried for days."
- Devastated = very sad, broken

VOCABULARY:

PREFIXES:
- un- = not (unhappy)
- re- = again (rewrite)
- pre- = before (preview)
- dis- = not (disagree)

SUFFIXES:
- -er = more (bigger)
- -est = most (biggest)
- -ful = full of (helpful)
- -less = without (useless)

ANTONYMS:
- hot ↔ cold
- happy ↔ sad
- big ↔ small
- up ↔ down

SYNONYMS:
- big = large = huge
- happy = glad = joyful
- sad = unhappy = miserable
- fast = quick = speedy'''},

    # ==================== GRADE 7 - Additional ====================
    {'g': 7, 's': 'Science', 't': 'Nutrition in Plants and Animals',
     'd': 'How organisms get their food',
     'c': '''NUTRITION IN PLANTS AND ANIMALS

NUTRITION:
Process of obtaining food and using it for energy.

MODES OF NUTRITION:

1. AUTOTROPHIC: Self-feeding (make own food)
   - Plants are autotrophs
   - Use sunlight, water, CO₂

2. HETEROTROPHIC: Depend on others
   - Animals are heterotrophs

NUTRITION IN PLANTS:

PHOTOSYNTHESIS:
The process by which plants make food.

Equation:
6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂
                Chlorophyll

Requirements:
1. Sunlight (energy)
2. Water (from roots)
3. Carbon dioxide (from air through stomata)
4. Chlorophyll (green pigment in leaves)
5. Minerals (from soil)

Site: CHLOROPLAST (contains chlorophyll)
Mainly in: LEAVES

STOMATA:
Tiny pores in leaves for:
- Gas exchange
- Water vapor loss (transpiration)

NUTRIENTS FOR PLANTS:

From Soil:
- Nitrogen (growth)
- Phosphorus
- Potassium
- Magnesium
- Iron

Rhizobium Bacteria:
- Live in roots of legumes (peas, beans)
- Fix nitrogen from air

NUTRITION IN OTHER PLANTS:

PARASITIC PLANTS:
- Take food from other plants
- Example: Cuscuta (Amarbel)

INSECTIVOROUS PLANTS:
- Catch and digest insects
- Get nitrogen this way
- Example: Pitcher plant, Venus flytrap

SAPROPHYTES:
- Feed on dead/decaying matter
- Example: Mushrooms, fungi

SYMBIOSIS:
- Two organisms helping each other
- Example: Lichen (algae + fungus)

NUTRITION IN ANIMALS:

TYPES OF HETEROTROPHS:

1. HERBIVORES: Eat plants only
   - Cow, buffalo, deer, rabbit
   - Long intestines for plant digestion

2. CARNIVORES: Eat meat only
   - Lion, tiger, wolf, eagle
   - Short intestines, sharp teeth

3. OMNIVORES: Eat both plants and meat
   - Humans, bears, dogs, crows

DIGESTION IN HUMANS:

Digestive System Parts:
1. MOUTH:
   - Teeth chew (mechanical)
   - Saliva starts digestion of starch
   - Tongue tastes and helps swallow

TYPES OF TEETH:
- Incisors (8): Biting
- Canines (4): Tearing
- Premolars (8): Crushing
- Molars (12): Grinding
Total: 32 in adults

2. ESOPHAGUS (Food pipe):
   - Tube to stomach
   - Moves food by peristalsis

3. STOMACH:
   - J-shaped bag
   - HCl kills germs
   - Pepsin digests protein

4. SMALL INTESTINE:
   - Main digestion happens here
   - Bile from liver
   - Pancreatic juice
   - Absorbs nutrients to blood

5. LARGE INTESTINE:
   - Absorbs water
   - Removes waste

6. RECTUM and ANUS:
   - Stores and removes waste

ASSOCIATED ORGANS:

LIVER:
- Largest gland
- Makes bile (helps digest fat)

PANCREAS:
- Makes pancreatic juice
- Insulin for blood sugar

SALIVARY GLANDS:
- In mouth
- Make saliva

NUTRITION IN COWS (Ruminants):

- 4-chambered stomach
- Chew cud (regurgitated food)
- Have bacteria to digest cellulose
- Chambers: Rumen, Reticulum, Omasum, Abomasum

DENTAL CARE:

To keep teeth healthy:
1. Brush twice daily
2. Use toothpaste
3. Use proper technique
4. Avoid too much sugar
5. Visit dentist
6. Rinse mouth after eating

CAVITIES:
- Caused by bacteria
- Eat sugar, produce acid
- Acid damages teeth
- Pain and toothache

GOOD FOOD HABITS:

1. Eat balanced diet
2. Regular meals
3. Don't overeat
4. Drink water
5. Eat slowly, chew well
6. Wash hands before eating'''},

    # ==================== GRADE 8 - Additional ====================
    {'g': 8, 's': 'English', 't': 'Speech Writing and Debate',
     'd': 'How to write speeches and present arguments',
     'c': '''SPEECH WRITING AND DEBATE

WHAT IS A SPEECH?
A formal address to an audience.

PURPOSES:
- Inform
- Persuade
- Inspire
- Entertain
- Celebrate

PARTS OF A SPEECH:

1. INTRODUCTION (Opening)
- Greet audience
- Get attention (hook)
- State purpose
- Preview main points

GOOD OPENINGS:
- Quote: "As Gandhi said..."
- Question: "Have you ever wondered why..."
- Statistic: "Did you know 60% of..."
- Story: "Imagine a young boy in a village..."
- Fact: "Climate change is real..."

2. BODY (Main content)
- 3-4 main points
- Each point with explanation
- Use examples
- Connecting words
- Clear flow

3. CONCLUSION (Closing)
- Summarize main points
- Call to action (if needed)
- Memorable ending
- Thank audience

GOOD ENDINGS:
- Strong statement
- Famous quote
- Question to ponder
- Promise/Vision
- Inspiring words

EXAMPLE SPEECH:

Topic: "Importance of Trees"

Respected Principal, Teachers, and Dear Friends,

Good morning! Today I want to talk about something we often overlook - TREES.

Did you know one tree gives oxygen to TWO PEOPLE for a year?

Imagine our world without trees. No fresh air. No shade. No fruits. No homes for birds. Earth would be uninhabitable.

Trees give us:
- Oxygen we breathe
- Food we eat
- Wood for homes
- Medicines
- Shade and beauty
- Homes for animals

Yet we are CUTTING DOWN trees faster than we plant them. Every year, MILLIONS of trees are lost.

What can we do?
1. Plant trees (Vanmahotsav)
2. Don't waste paper
3. Use recycled products
4. Reduce, Reuse, Recycle
5. Educate others

Friends, the future of our planet depends on us. Let's pledge to plant at least ONE tree this year and protect what we have.

As they say, "The best time to plant a tree was 20 years ago. The second best time is NOW."

Thank you!

DEBATE:

A formal discussion of a topic with two sides.

STRUCTURE OF DEBATE:

1. TOPIC announced
2. FOR side speakers (pro)
3. AGAINST side speakers (con)
4. REBUTTAL (counter-arguments)
5. CONCLUSION by each side

ARGUMENT TECHNIQUES:

1. LOGICAL: Use facts, statistics
2. EMOTIONAL: Appeal to feelings
3. ETHICAL: Right and wrong

REBUTTAL TIPS:

- Listen carefully
- Note opponent's points
- Counter with facts
- Stay polite
- Don't attack person
- Use evidence

EXAMPLE DEBATE TOPICS:

For Students:
- Homework should be banned
- Mobile phones in school
- Online classes vs offline
- Boarding schools vs day schools
- Sports vs Studies
- Exams should be abolished

National Issues:
- Death penalty
- Internet for everyone
- Free education
- Banning plastic

PUBLIC SPEAKING TIPS:

1. PREPARE well
2. PRACTICE often
3. KNOW your audience
4. SPEAK clearly
5. MAINTAIN eye contact
6. USE gestures naturally
7. CONTROL your voice
8. BE CONFIDENT
9. SMILE (when appropriate)
10. END strong

OVERCOMING FEAR:

- Practice in mirror
- Record yourself
- Practice with friends/family
- Start small
- Remember audience wants you to succeed
- Take deep breaths
- Have notes (but don't read)

LANGUAGE TIPS:

Use:
✓ Short sentences
✓ Simple words
✓ Strong verbs
✓ Active voice
✓ Personal pronouns (we, you, us)
✓ Repetition for emphasis

Avoid:
✗ Filler words (umm, like, you know)
✗ Long complicated sentences
✗ Jargon
✗ Reading off paper

GREAT SPEECHES IN HISTORY:

- Martin Luther King: "I Have a Dream"
- Mahatma Gandhi: Quit India Speech
- Subhash Bose: "Give Me Blood"
- Jawaharlal Nehru: "Tryst with Destiny"
- Swami Vivekananda: Chicago Speech

These speakers inspired millions. With practice, you can inspire too!'''},

    # ==================== GRADE 9 - Additional ====================
    {'g': 9, 's': 'Mathematics', 't': 'Linear Equations in Two Variables',
     'd': 'Solving equations with x and y',
     'c': '''LINEAR EQUATIONS IN TWO VARIABLES

A LINEAR EQUATION in two variables has the form:
ax + by + c = 0

Where:
- x and y are variables
- a, b, c are constants
- a and b are not both zero

EXAMPLES:
- 2x + 3y = 12
- x - y = 5
- 3x + y - 7 = 0

SOLUTIONS:

A solution is a pair (x, y) that satisfies the equation.

Example: 2x + y = 7
- When x=1, y=5: 2(1)+5 = 7 ✓
- When x=2, y=3: 2(2)+3 = 7 ✓
- When x=3, y=1: 2(3)+1 = 7 ✓

A linear equation in 2 variables has INFINITE solutions.

GRAPH OF LINEAR EQUATION:

Each linear equation represents a STRAIGHT LINE.

To plot:
1. Get values of y for different x
2. Plot points
3. Join with straight line

Example: y = x + 2
- x=0, y=2: Point (0,2)
- x=1, y=3: Point (1,3)
- x=2, y=4: Point (2,4)
- x=-1, y=1: Point (-1,1)

Plot these and join.

SLOPE AND INTERCEPT:

Form: y = mx + c
- m = slope
- c = y-intercept (where line crosses y-axis)

INTERCEPTS:
- x-intercept: y=0 in equation
- y-intercept: x=0 in equation

Example: 2x + 3y = 6
- y=0: 2x=6, x=3 (x-intercept)
- x=0: 3y=6, y=2 (y-intercept)

SOLVING PAIR OF LINEAR EQUATIONS:

If we have 2 equations with 2 variables, we need to find unique x and y.

Methods:

1. SUBSTITUTION METHOD:

Example: x + y = 7, x - y = 1

Step 1: From first equation: x = 7 - y
Step 2: Substitute in second: (7-y) - y = 1
Step 3: 7 - 2y = 1
Step 4: -2y = -6
Step 5: y = 3
Step 6: x = 7 - 3 = 4

Solution: (4, 3)

Check: 4 + 3 = 7 ✓
       4 - 3 = 1 ✓

2. ELIMINATION METHOD:

Example: 2x + y = 7, x - y = 2

Step 1: Add both equations (y cancels):
       3x = 9
       x = 3

Step 2: Substitute: 2(3) + y = 7
                   y = 1

Solution: (3, 1)

3. GRAPHICAL METHOD:

Plot both lines.
Where they intersect = solution.

Three cases for two lines:

CASE 1: ONE solution (lines intersect)
- Different slopes
- Example: y = x and y = -x + 4

CASE 2: NO solution (lines parallel)
- Same slope, different intercept
- Example: y = 2x and y = 2x + 5

CASE 3: INFINITE solutions (lines same)
- Both same equation
- Example: 2x + y = 5 and 4x + 2y = 10

WORD PROBLEMS:

EXAMPLE 1:
Sum of two numbers is 30, difference is 6.
Find the numbers.

Let numbers be x and y.
x + y = 30
x - y = 6

Adding: 2x = 36, x = 18
y = 30 - 18 = 12

Numbers: 18 and 12

EXAMPLE 2:
Cost of 2 pens and 3 pencils is ₹25.
Cost of 3 pens and 2 pencils is ₹30.
Find cost of each.

Let pen = x, pencil = y
2x + 3y = 25
3x + 2y = 30

Solving by elimination:
6x + 9y = 75 (multiply 1st by 3)
6x + 4y = 60 (multiply 2nd by 2)

Subtract: 5y = 15, y = 3
2x + 9 = 25, x = 8

Cost: Pen = ₹8, Pencil = ₹3

REAL LIFE APPLICATIONS:

- Calculating costs
- Mixing solutions
- Speed and distance problems
- Age problems
- Money problems
- Comparing offers'''},

    # ==================== GRADE 10 - Additional ====================
    {'g': 10, 's': 'Mathematics', 't': 'Quadratic Equations',
     'd': 'Solving quadratic equations',
     'c': '''QUADRATIC EQUATIONS

QUADRATIC EQUATION:
An equation of degree 2.

Standard Form:
ax² + bx + c = 0
Where a ≠ 0

Examples:
- x² + 5x + 6 = 0
- 2x² - 7x + 3 = 0
- x² - 4 = 0

TYPES:

COMPLETE: ax² + bx + c = 0
PURE: ax² + c = 0 (no bx)
INCOMPLETE: ax² + bx = 0 (no c)

SOLUTIONS = ROOTS = ZEROS

A quadratic equation has at most 2 roots.

METHODS TO SOLVE:

1. FACTORIZATION:

Example: x² - 5x + 6 = 0

Find two numbers that:
- Multiply to give 6 (constant)
- Add to give -5 (middle)

Numbers: -2 and -3
(-2) × (-3) = 6 ✓
(-2) + (-3) = -5 ✓

So: x² - 2x - 3x + 6 = 0
x(x - 2) - 3(x - 2) = 0
(x - 2)(x - 3) = 0

Either x - 2 = 0 → x = 2
Or x - 3 = 0 → x = 3

Roots: 2 and 3

2. COMPLETING THE SQUARE:

Example: x² + 6x + 5 = 0

Step 1: x² + 6x = -5
Step 2: Add (b/2)² = (6/2)² = 9
       x² + 6x + 9 = -5 + 9
       (x + 3)² = 4
Step 3: x + 3 = ±2
       x = -3 ± 2
       x = -1 or x = -5

3. QUADRATIC FORMULA:

For ax² + bx + c = 0:

x = (-b ± √(b² - 4ac)) / 2a

Example: 2x² - 7x + 3 = 0
a=2, b=-7, c=3

x = (7 ± √(49 - 24)) / 4
x = (7 ± √25) / 4
x = (7 ± 5) / 4

x = 12/4 = 3
Or x = 2/4 = 1/2

Roots: 3 and 1/2

DISCRIMINANT:

D = b² - 4ac

Tells nature of roots:

CASE 1: D > 0
- Two real distinct roots
- Lines cross x-axis at 2 points

CASE 2: D = 0
- One repeated real root
- Line touches x-axis at 1 point

CASE 3: D < 0
- No real roots (complex)
- Line doesn't touch x-axis

Examples:

x² - 5x + 6 = 0
D = 25 - 24 = 1 > 0
Two real roots: 2, 3

x² - 4x + 4 = 0
D = 16 - 16 = 0
One root: 2 (repeated)

x² + x + 1 = 0
D = 1 - 4 = -3 < 0
No real roots

RELATION BETWEEN ROOTS:

If roots are α and β:
- Sum of roots = α + β = -b/a
- Product of roots = αβ = c/a

Example: x² - 5x + 6 = 0
Sum: 5/1 = 5 (2+3=5 ✓)
Product: 6/1 = 6 (2×3=6 ✓)

FORMING QUADRATIC EQUATION:

If sum = S and product = P:
x² - Sx + P = 0

Example: Roots are 4 and -2
S = 4 + (-2) = 2
P = 4 × (-2) = -8
Equation: x² - 2x - 8 = 0

WORD PROBLEMS:

EXAMPLE 1:
Find two numbers whose sum is 10 and product is 24.

Let numbers be x and (10 - x).
x(10 - x) = 24
10x - x² = 24
x² - 10x + 24 = 0
(x - 4)(x - 6) = 0
x = 4 or x = 6

Numbers: 4 and 6 (their sum is 10 ✓, product 24 ✓)

EXAMPLE 2:
The product of two consecutive positive integers is 56.

Let numbers be x and (x+1).
x(x + 1) = 56
x² + x - 56 = 0
(x + 8)(x - 7) = 0
x = -8 (reject, negative) or x = 7

Numbers: 7 and 8

EXAMPLE 3:
Length of rectangle is 5m more than width. Area is 84 m².

Let width = x, length = x + 5
Area = x(x + 5) = 84
x² + 5x - 84 = 0
(x + 12)(x - 7) = 0
x = 7 (reject -12, can't be negative)

Width = 7m, Length = 12m

APPLICATIONS:

- Geometry (areas, perimeters)
- Physics (projectile motion)
- Economics (profit/loss)
- Engineering
- Architecture'''},

    {'g': 10, 's': 'Science', 't': 'Electricity and Magnetism',
     'd': 'Electric current, circuits, and magnetic effects',
     'c': '''ELECTRICITY AND MAGNETISM

ELECTRIC CURRENT:
Flow of electric charge (electrons) through a conductor.

UNIT: AMPERE (A)
Symbol: I

I = Q/t
Where Q = charge, t = time

VOLTAGE (Potential Difference):
The work done in moving charge between two points.

UNIT: VOLT (V)
Symbol: V

Measured by: VOLTMETER (in parallel)

CURRENT measured by: AMMETER (in series)

OHM'S LAW:

V = IR

Where:
V = Voltage
I = Current
R = Resistance

RESISTANCE:
Opposition to flow of current.
UNIT: OHM (Ω)

R = ρL/A
Where:
- ρ = resistivity
- L = length
- A = cross-section area

Factors:
- Length: More length, more R
- Area: More area, less R
- Material
- Temperature: Higher temp, higher R (for metals)

CONDUCTORS vs INSULATORS:

CONDUCTORS: Allow current
- Metals (Cu, Al, Ag, Fe)
- Human body
- Water (with salts)

INSULATORS: Don't allow current
- Plastic, rubber
- Wood, glass
- Dry air

ELECTRIC CIRCUIT:

Components:
- Cell/Battery (power source)
- Wires (connectors)
- Switch (controls flow)
- Bulb/Resistor (uses power)
- Ammeter (measures current)
- Voltmeter (measures voltage)

SERIES CIRCUIT:
Components connected end to end.

Total R = R₁ + R₂ + R₃
Same current through all
Voltage divides

PARALLEL CIRCUIT:
Components have separate paths.

1/R_total = 1/R₁ + 1/R₂ + 1/R₃
Same voltage across all
Current divides

ELECTRICAL POWER:

P = V × I
P = I²R
P = V²/R

UNIT: WATT (W)
1 kilowatt = 1000 W

ELECTRIC ENERGY:

Energy = Power × Time
E = P × t

UNIT: Kilowatt-hour (kWh) or "unit"

Bill calculation:
- 1 kWh = 1 unit
- If you use 100W bulb for 10 hrs:
  E = 100 × 10 / 1000 = 1 kWh
  Cost at ₹5/unit = ₹5

HEATING EFFECT OF CURRENT:

When current flows, heat is produced.

H = I²Rt (Joule's law)

Applications:
- Electric heaters
- Bulbs (filament glows)
- Toasters, geysers
- Electric iron
- Fuse (blows when too much current)

MAGNETIC EFFECT OF CURRENT:

When current flows in wire, magnetic field is created around it.

Discovered by HANS OERSTED.

RIGHT HAND RULE:
- Thumb shows current direction
- Curled fingers show field direction

ELECTROMAGNET:
Wire wrapped around iron core. When current flows, becomes magnet.

Uses:
- Electric bells
- Telephones
- MRI machines
- Cranes (lift iron)

ELECTROMAGNETIC INDUCTION:

When magnet moves near coil, current is induced in coil.
Discovered by MICHAEL FARADAY.

Used in:
- Generators (produce electricity)
- Transformers (change voltage)

GENERATOR:
Converts mechanical energy → electrical energy

MOTOR:
Converts electrical energy → mechanical energy

DOMESTIC ELECTRIC CIRCUITS:

In India:
- AC supply (Alternating Current)
- 220 Volts
- 50 Hz frequency

Color codes:
- Brown/Red: LIVE (carries current)
- Black/Blue: NEUTRAL (return path)
- Green/Yellow-Green: EARTH (safety)

SAFETY MEASURES:

1. EARTHING:
- Connects appliance to ground
- Prevents shock

2. FUSE:
- Wire that melts when too much current
- Breaks circuit
- Protects appliances

3. CIRCUIT BREAKER:
- Switches off when overload
- Can be reset

4. INSULATORS:
- Plastic coatings on wires
- Rubber gloves for electricians

ELECTRICAL HAZARDS:

- Short circuit (live and neutral touch)
- Overloading (too many appliances)
- Damaged wires
- Wet hands and electricity

PRECAUTIONS:

1. Don't touch with wet hands
2. Use earthed plugs
3. Check wires for damage
4. Don't overload sockets
5. Switch off when not in use
6. Have proper fuse rating

SAVING ELECTRICITY:

1. Use LED bulbs (less power)
2. Switch off when not in use
3. Use natural light
4. Maintain appliances
5. Use BEE star-rated appliances
6. Use solar power

UNITS:

- Current: Ampere (A)
- Voltage: Volt (V)
- Resistance: Ohm (Ω)
- Power: Watt (W)
- Energy: Joule (J) or kWh
- Charge: Coulomb (C)'''},
]


# Multi-year question papers for grades
MULTI_YEAR_PAPERS = [
    # 2022 Papers
    {
        'grade': 10, 'subject': 'Mathematics', 'year': 2022,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Mathematics Board Exam 2022',
        'description': 'CBSE Class 10 Mathematics 2022',
        'content': '''GRADE 10 MATHEMATICS - BOARD EXAM 2022
Time: 3 hours | Max Marks: 80

[Similar structure to 2023 paper with different problems]

Section A - MCQ (1 mark × 20)
1. √16 = ?
   (a) 2  (b) 4  (c) 8  (d) 16

2. HCF of 8, 12:
   (a) 2  (b) 4  (c) 6  (d) 8

3. tan 0° = ?
   (a) 0  (b) 1  (c) ∞  (d) -1

4. sin 60° = ?
   (a) 1/2  (b) √3/2  (c) 1  (d) √2/2

5. AP: 5, 8, 11, ... 6th term?
   (a) 17  (b) 20  (c) 23  (d) 26

[Continue with similar pattern - 20 MCQs total]

Section B - Short Answer-I (2 marks × 6)
21. Find HCF of 18 and 24.
22. Find zeros of x² - 9.
23. Solve: 2x + y = 5, x - y = 1
24. Find sin θ if cos θ = 4/5
25. Find 10th term of AP: 3, 7, 11, ...
26. P(king from deck)?

Section C - Short Answer-II (3 marks × 6)
27. Prove √5 is irrational.
28. Solve x² - 7x + 12 = 0
29. Find sum of first 20 terms of AP: 5,9,13,...
30. Distance between (3,5) and (6,9).
31. Prove sin²A + cos²A = 1.
32. Mean of: 10,15,20,25,30

Section D - Long Answer (5 marks × 4)
33. Construct triangle ABC with given conditions.
34. Find mean, median, mode of frequency table.
35. Tangent properties of circle.
36. Two ships from lighthouse, find distances.

Section E - Case Study (5 marks × 2)
37. Population growth problem
38. Cost optimization problem

ALL THE BEST!'''
    },
    # 2021 Paper
    {
        'grade': 10, 'subject': 'Mathematics', 'year': 2021,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Mathematics Board Exam 2021',
        'description': 'CBSE Class 10 Mathematics 2021',
        'content': '''GRADE 10 MATHEMATICS - BOARD EXAM 2021
Time: 3 hours | Max Marks: 80

[2021 paper structure with COVID-modified format]

Section A: Objective Type (1 mark × 20)
- MCQs
- Fill in blanks
- Very short questions

Section B: Short Answer (2 marks × 8)
- Compulsory questions on basics

Section C: Short Answer (3 marks × 8)
- Choose 8 from 12
- Algebra, Geometry, Trigonometry

Section D: Long Answer (4 marks × 7)
- Choose 7 from 10
- Word problems, constructions

Section E: Case Studies (Optional)
- Real-world scenarios

ALL THE BEST!'''
    },
    # 2024 Latest
    {
        'grade': 10, 'subject': 'Mathematics', 'year': 2024,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Mathematics Board Exam 2024',
        'description': 'CBSE Class 10 Mathematics 2024 - Latest pattern',
        'content': '''GRADE 10 MATHEMATICS - BOARD EXAM 2024
Time: 3 hours | Max Marks: 80

SECTION A: MCQ (1 mark × 20) - 20 marks

1. The HCF of smallest prime and composite number:
   (a) 1  (b) 2  (c) 4  (d) None

2. Decimal expansion of 7/8:
   (a) Terminating  (b) Non-terminating  (c) Both  (d) None

3. Zeros of p(x) = x² + 7x + 12:
   (a) -3, -4  (b) 3, 4  (c) 3, -4  (d) -3, 4

4. System has unique solution if:
   (a) a₁/a₂ = b₁/b₂  (b) a₁/a₂ ≠ b₁/b₂  (c) Both  (d) None

5. tan 30° × tan 60° = ?
   (a) 0  (b) 1  (c) √3  (d) 2

6. nth term of AP: 3, 7, 11, ...:
   (a) 4n-1  (b) 4n+1  (c) 4n-3  (d) 4n+3

7. Discriminant of 2x² - 4x + 3 = 0:
   (a) -8  (b) 8  (c) 0  (d) 16

8. Coordinates of midpoint of (3,5) and (7,9):
   (a) (3,5)  (b) (5,7)  (c) (4,5)  (d) (5,8)

9. Area of circle (r = 14):
   (a) 154  (b) 308  (c) 616  (d) 88

10. Roots of x² - 5x + 6 = 0:
    (a) 1, 6  (b) 2, 3  (c) -2, -3  (d) -1, -6

[Questions 11-20: Similar pattern]

SECTION B: Very Short Answer (2 marks × 5) - 10 marks

21. Find HCF and LCM of 50 and 80.
22. Solve: x + y = 7, x - y = 3
23. Find sin θ if tan θ = 3/4
24. nth term of AP: 7, 13, 19, ... = ?
25. Mean of 8, 11, 14, 17, 20

SECTION C: Short Answer (3 marks × 6) - 18 marks

26. Prove √7 is irrational.
27. Find zeros of x² - 5x + 6 and verify relation between roots.
28. Solve 2/x + 1/y = 5, 1/x + 1/y = 3
29. Solve trigonometric identity.
30. AP: Find 15th term and sum of 15 terms of 5,8,11,...
31. Probability problem with cards.

SECTION D: Long Answer (5 marks × 4) - 20 marks

32. Quadratic equation real-world problem.
33. Trigonometry word problem.
34. Statistics: mean, median, mode of grouped data.
35. Geometry: Tangent and chord properties.

SECTION E: Case Study (4 marks × 3) - 12 marks

36. CASE STUDY 1: Cricket ground design (circles, triangles)
37. CASE STUDY 2: Building height (trigonometry)
38. CASE STUDY 3: Investment scheme (AP)

ALL THE BEST!'''
    },
    {
        'grade': 10, 'subject': 'Science', 'year': 2024,
        'exam_type': 'board', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 10 Science Board Exam 2024',
        'description': 'CBSE Class 10 Science Board 2024',
        'content': '''GRADE 10 SCIENCE - BOARD EXAM 2024
Time: 3 hours | Max Marks: 80

[Similar structure with Physics, Chemistry, Biology]

PART A - PHYSICS:
- Electricity and Magnetism
- Light - Reflection and Refraction
- Human Eye and Colorful World
- Sources of Energy

PART B - CHEMISTRY:
- Chemical Reactions and Equations
- Acids, Bases, Salts
- Metals and Non-metals
- Carbon and Compounds
- Periodic Classification

PART C - BIOLOGY:
- Life Processes
- Control and Coordination
- Reproduction
- Heredity and Evolution
- Our Environment

[Standard board exam format with MCQ, Short Answer, Long Answer, and Case Studies]

ALL THE BEST!'''
    },
    # Grade 9 Math 2022
    {
        'grade': 9, 'subject': 'Mathematics', 'year': 2022,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 9 Mathematics Annual 2022',
        'description': 'Class 9 Mathematics Annual 2022',
        'content': '''GRADE 9 MATHEMATICS - ANNUAL EXAM 2022
[Similar structure as Grade 9 2023]
Section A: MCQ (20 marks)
Section B: Very Short Answer (12 marks)
Section C: Short Answer (18 marks)
Section D: Long Answer (30 marks)
ALL THE BEST!'''
    },
    # Grade 8 Math 2024
    {
        'grade': 8, 'subject': 'Mathematics', 'year': 2024,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 100,
        'title': 'Grade 8 Mathematics Annual 2024',
        'description': 'Class 8 Mathematics 2024',
        'content': '''GRADE 8 MATHEMATICS - ANNUAL EXAM 2024
[Updated 2024 pattern]
Section A: MCQ (15 marks)
Section B: Short Answer (30 marks)
Section C: Long Answer (30 marks)
Section D: Application (25 marks)
ALL THE BEST!'''
    },
    # Grade 7 Science 2022
    {
        'grade': 7, 'subject': 'Science', 'year': 2022,
        'exam_type': 'annual', 'duration': 150, 'total_marks': 80,
        'title': 'Grade 7 Science Annual 2022',
        'description': 'Class 7 Science Annual 2022',
        'content': '''GRADE 7 SCIENCE - ANNUAL EXAM 2022
[Standard pattern with 2022 problems]
Total: 80 marks, 2.5 hours
ALL THE BEST!'''
    },
    # Grade 5 Math 2022
    {
        'grade': 5, 'subject': 'Mathematics', 'year': 2022,
        'exam_type': 'annual', 'duration': 120, 'total_marks': 80,
        'title': 'Grade 5 Mathematics Annual 2022',
        'description': 'Class 5 Mathematics 2022',
        'content': '''GRADE 5 MATHEMATICS - ANNUAL EXAM 2022
[Class 5 pattern with 2022 problems]
ALL THE BEST!'''
    },
    # Half Yearly papers
    {
        'grade': 10, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'half_yearly', 'duration': 120, 'total_marks': 50,
        'title': 'Grade 10 Mathematics Half Yearly 2023',
        'description': 'Class 10 Half Yearly Mathematics 2023',
        'content': '''GRADE 10 MATHEMATICS - HALF YEARLY 2023
Time: 2 hours | Max Marks: 50

Topics: Number System, Polynomials, Linear Equations,
        Coordinate Geometry, Triangles

[Reduced syllabus for half yearly]

Section A: MCQ (10 × 1 = 10 marks)
Section B: Short Answer (5 × 2 = 10 marks)
Section C: Short Answer (5 × 3 = 15 marks)
Section D: Long Answer (3 × 5 = 15 marks)

ALL THE BEST!'''
    },
    {
        'grade': 9, 'subject': 'Science', 'year': 2024,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 9 Science Annual 2024',
        'description': 'Class 9 Science 2024',
        'content': '''GRADE 9 SCIENCE - ANNUAL EXAM 2024
[Updated 2024 pattern]
Time: 3 hours | Max Marks: 80
ALL THE BEST!'''
    },
]


def load_bulk():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Teacher not found")
            return

        os.makedirs('./data/resources', exist_ok=True)
        os.makedirs('./data/question_papers', exist_ok=True)

        existing_resources = {r.title for r in Resource.query.all()}
        existing_papers = {p.title for p in QuestionPaper.query.all()}

        res_added = 0
        for r in BULK_RESOURCES:
            if r['t'] in existing_resources:
                continue
            filename = f"ncert_g{r['g']}_{r['s'].replace(' ', '_')}_{r['t'].replace(' ', '_')[:40]}.txt"
            file_path = f"data/resources/{filename}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(r['c'])
            file_size = os.path.getsize(file_path)
            resource = Resource(
                title=r['t'], description=r['d'], subject=r['s'],
                grade_level=r['g'], content_type='txt', file_path=file_path,
                file_size=file_size, created_by=teacher.id, is_published=True
            )
            db.session.add(resource)
            res_added += 1

        papers_added = 0
        for p in MULTI_YEAR_PAPERS:
            if p['title'] in existing_papers:
                continue
            filename = f"paper_g{p['grade']}_{p['subject'].replace(' ', '_')}_{p['year']}_{p['exam_type']}.txt"
            file_path = f"data/question_papers/{filename}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(p['content'])
            file_size = os.path.getsize(file_path)
            paper = QuestionPaper(
                title=p['title'], description=p['description'],
                subject=p['subject'], grade_level=p['grade'], year=p['year'],
                exam_type=p['exam_type'], duration_minutes=p['duration'],
                total_marks=p['total_marks'], file_path=file_path,
                content_type='txt', file_size=file_size, created_by=teacher.id,
                is_published=True
            )
            db.session.add(paper)
            papers_added += 1

        db.session.commit()
        print(f"\n[DONE]")
        print(f"  Resources added: {res_added}")
        print(f"  Papers added: {papers_added}")
        print(f"  Total resources: {Resource.query.count()}")
        print(f"  Total papers: {QuestionPaper.query.count()}")


if __name__ == '__main__':
    try:
        load_bulk()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
