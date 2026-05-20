"""
Add many more NCERT-aligned resources covering missing topics
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import User, Resource


def clean(text):
    """Sanitize text for PDF"""
    replacements = {
        '×': 'x', '÷': '/', '−': '-', '°': ' deg',
        '²': '^2', '³': '^3', '√': 'sqrt', 'π': 'pi',
        'θ': 'theta', '–': '-', '—': '-',
        '"': '"', '"': '"', ''': "'", ''': "'",
        '…': '...', '•': '*', '₹': 'Rs.',
        '→': '->', '←': '<-',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    result = []
    for c in text:
        if ord(c) < 128:
            result.append(c)
        else:
            result.append(' ')
    return ''.join(result)


class PDF(FPDF):
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

    def render(self, content):
        content = clean(content)
        for raw in content.split('\n'):
            line = raw.rstrip()
            if not line.strip():
                self.ln(2)
                continue

            stripped = line.strip()
            is_heading = stripped.isupper() and len(stripped) <= 70 and '=' not in stripped
            is_sub = stripped.endswith(':') and len(stripped) <= 50

            try:
                if is_heading:
                    self.ln(2)
                    self.set_font('Helvetica', 'B', 12)
                    self.set_text_color(79, 70, 229)
                    self.multi_cell(0, 6, stripped)
                    self.ln(1)
                elif is_sub:
                    self.set_font('Helvetica', 'B', 10)
                    self.set_text_color(30, 41, 59)
                    self.multi_cell(0, 5, stripped)
                else:
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                    self.multi_cell(0, 5, stripped)
            except Exception:
                try:
                    safe = ''.join(c for c in stripped if c.isascii() and ord(c) >= 32)[:500]
                    if safe:
                        self.set_font('Helvetica', '', 10)
                        self.set_text_color(15, 23, 42)
                        self.multi_cell(0, 5, safe)
                except:
                    pass


def get_youtube(title):
    """Get YouTube link based on title keywords"""
    title_l = title.lower()
    links = {
        'colors': ('https://www.youtube.com/watch?v=YFNyqsiKaH8', 'Pebbles Kids'),
        'days': ('https://www.youtube.com/watch?v=mXMofxtDPUQ', 'Pebbles Kids'),
        'vowels': ('https://www.youtube.com/watch?v=BELlZKpi1Zs', 'Magnet Brains'),
        'birds': ('https://www.youtube.com/watch?v=v3NQ72wOFt8', 'Peekaboo Kidz'),
        'insects': ('https://www.youtube.com/watch?v=p3St51F4kE8', 'Peekaboo Kidz'),
        'light': ('https://www.youtube.com/watch?v=hsXLwsr-aTw', 'Magnet Brains'),
        'sound': ('https://www.youtube.com/watch?v=qV4lR9EWGlY', 'Magnet Brains'),
        'magnet': ('https://www.youtube.com/watch?v=tFzqAEZnDt8', 'Magnet Brains'),
        'cell': ('https://www.youtube.com/watch?v=URUJD5NEXC8', 'Magnet Brains'),
        'climate': ('https://www.youtube.com/watch?v=eS2FDBSCqRk', 'Magnet Brains'),
        'maps': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Magnet Brains'),
        'civics': ('https://www.youtube.com/watch?v=zXxxqxhWvyM', 'Magnet Brains'),
        'gravitation': ('https://www.youtube.com/watch?v=t9pXkmoqkic', 'Magnet Brains'),
        'heredity': ('https://www.youtube.com/watch?v=A21nyMhSDi8', 'Peekaboo Kidz'),
        'energy': ('https://www.youtube.com/watch?v=ru032Mfsfig', 'Magnet Brains'),
        'real numbers': ('https://www.youtube.com/watch?v=qrqj7g0DwHs', 'Magnet Brains'),
        'triangles': ('https://www.youtube.com/watch?v=302eJ3TzJQU', 'Math Antics'),
        'movements': ('https://www.youtube.com/watch?v=cWNF8YErOJg', 'Peekaboo Kidz'),
    }
    for k, v in links.items():
        if k in title_l:
            return v
    return ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains')


def get_ncert(grade, subject, title):
    """Get NCERT link based on grade and subject"""
    title_l = title.lower()
    grade_letter = chr(ord('a') + grade - 1)

    # Specific chapter PDFs for higher grades
    chapters = {
        (9, 'Mathematics', 'real numbers'): ('https://ncert.nic.in/textbook/pdf/iemh101.pdf', 'Chapter 1: Number Systems'),
        (9, 'Mathematics', 'triangles'): ('https://ncert.nic.in/textbook/pdf/iemh107.pdf', 'Chapter 7: Triangles'),
        (9, 'Science', 'cell'): ('https://ncert.nic.in/textbook/pdf/iesc105.pdf', 'Chapter 5: Cell Fundamental Unit of Life'),
        (9, 'Science', 'gravitation'): ('https://ncert.nic.in/textbook/pdf/iesc110.pdf', 'Chapter 10: Gravitation'),
        (10, 'Mathematics', 'real numbers'): ('https://ncert.nic.in/textbook/pdf/jemh101.pdf', 'Chapter 1: Real Numbers'),
        (10, 'Mathematics', 'triangles'): ('https://ncert.nic.in/textbook/pdf/jemh106.pdf', 'Chapter 6: Triangles'),
        (10, 'Science', 'heredity'): ('https://ncert.nic.in/textbook/pdf/jesc109.pdf', 'Chapter 9: Heredity and Evolution'),
        (10, 'Science', 'magnetism'): ('https://ncert.nic.in/textbook/pdf/jesc113.pdf', 'Chapter 13: Magnetic Effects'),
        (10, 'Science', 'energy'): ('https://ncert.nic.in/textbook/pdf/jesc114.pdf', 'Chapter 14: Sources of Energy'),
        (8, 'Science', 'light'): ('https://ncert.nic.in/textbook/pdf/hesc116.pdf', 'Chapter 16: Light'),
        (8, 'Science', 'sound'): ('https://ncert.nic.in/textbook/pdf/hesc113.pdf', 'Chapter 13: Sound'),
        (8, 'Science', 'cell'): ('https://ncert.nic.in/textbook/pdf/hesc108.pdf', 'Chapter 8: Cell Structure'),
        (6, 'Science', 'movements'): ('https://ncert.nic.in/textbook/pdf/fesc108.pdf', 'Chapter 8: Body Movements'),
        (6, 'Social Studies', 'civics'): ('https://ncert.nic.in/textbook/pdf/fess201.pdf', 'Social and Political Life Class 6'),
        (7, 'Social Studies', 'climate'): ('https://ncert.nic.in/textbook/pdf/gess1ps.pdf', 'Our Environment Class 7'),
    }

    for (g, s, kw), val in chapters.items():
        if grade == g and subject == s and kw in title_l:
            return val

    # Default by grade and subject
    defaults = {
        ('Mathematics', 1): ('https://ncert.nic.in/textbook.php?aejm1=0-15', 'Joyful Mathematics Class 1'),
        ('Science', 1): ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        ('English', 1): ('https://ncert.nic.in/textbook.php?aeen1=0-10', 'Mridang Class 1'),
        ('Social Studies', 1): ('https://ncert.nic.in/textbook.php?aekt1=0-12', 'The World Around Us Class 1'),
        ('Mathematics', 6): ('https://ncert.nic.in/textbook.php?femh1=0-14', 'Mathematics Class 6'),
        ('Science', 6): ('https://ncert.nic.in/textbook.php?fesc1=0-16', 'Science Class 6'),
        ('Mathematics', 9): ('https://ncert.nic.in/textbook.php?iemh1=0-15', 'Mathematics Class 9'),
        ('Science', 9): ('https://ncert.nic.in/textbook.php?iesc1=0-15', 'Science Class 9'),
        ('Mathematics', 10): ('https://ncert.nic.in/textbook.php?jemh1=0-15', 'Mathematics Class 10'),
        ('Science', 10): ('https://ncert.nic.in/textbook.php?jesc1=0-13', 'Science Class 10'),
    }
    return defaults.get((subject, grade), ('https://ncert.nic.in/textbook.php', f'NCERT {subject} Class {grade}'))


# Many NEW resources covering missing topics
NEW_RESOURCES = [
    # Grade 1 additions
    {'g': 1, 's': 'English', 't': 'Vowels and Consonants',
     'd': 'Learn vowels A E I O U and consonants',
     'c': '''VOWELS AND CONSONANTS

The English alphabet has 26 letters.
These are divided into two groups: VOWELS and CONSONANTS.

VOWELS (5 letters):
A, E, I, O, U

Sometimes Y is also a vowel.

Examples of words with vowels:
- A: Apple, Ant, Arm
- E: Egg, Elephant, Eye
- I: Ice, Igloo, Ink
- O: Orange, Owl, Open
- U: Umbrella, Up, Uncle

CONSONANTS (21 letters):
B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z

Examples of words with consonants:
- B: Ball, Boy, Bus
- C: Cat, Cap, Cup
- D: Dog, Door, Duck
- F: Fish, Fan, Fox
- G: Goat, Girl, Garden

WHY ARE VOWELS IMPORTANT?
- Every word needs a vowel
- Vowels help us make sounds
- Without vowels, we cannot speak words

Practice:
- Find vowels in: CAT (A)
- Find vowels in: ELEPHANT (E, E, A)
- Find vowels in: APPLE (A, E)

Reading short words:
- 2-letter words: AT, IT, ON, IN
- 3-letter words: CAT, DOG, BIG, RED, SUN
- 4-letter words: FISH, BIRD, BOOK, TREE

Remember:
Every word has at least ONE vowel!'''},

    {'g': 1, 's': 'Mathematics', 't': 'Colors and Shapes Around Us',
     'd': 'Identify colors and basic shapes',
     'c': '''COLORS AND SHAPES AROUND US

COLORS:
We see many colors in our world.

PRIMARY COLORS:
1. RED - like an apple, tomato
2. BLUE - like sky, ocean
3. YELLOW - like sun, banana

SECONDARY COLORS (mix of primary):
- GREEN (Blue + Yellow) - like grass, leaves
- ORANGE (Red + Yellow) - like fruit orange
- PURPLE (Red + Blue) - like brinjal

OTHER COLORS:
- WHITE - like milk, paper
- BLACK - like night, shoes
- BROWN - like soil, chocolate
- PINK - like flower, lips

SHAPES:

1. CIRCLE
- Round shape
- No corners
- Like sun, ball, clock face

2. SQUARE
- 4 equal sides
- 4 corners
- Like chess board, dice face

3. TRIANGLE
- 3 sides
- 3 corners
- Like pizza slice, mountain

4. RECTANGLE
- 4 sides (2 long, 2 short)
- 4 corners
- Like door, book, mobile phone

5. OVAL
- Like egg, lemon

6. STAR
- Has 5 points
- Like a star in sky

Finding Shapes and Colors:
Look around you!
- Find 5 RED things
- Find 5 CIRCLE shapes
- Find a BLUE rectangle
- Find a YELLOW square

Activity:
Draw your own colorful picture using:
- 3 circles
- 2 squares
- 1 triangle
- 4 different colors'''},

    # Grade 2 additions
    {'g': 2, 's': 'Science', 't': 'Birds and Insects',
     'd': 'Learn about birds and insects around us',
     'c': '''BIRDS AND INSECTS

BIRDS:
Animals with feathers, wings, and beaks.

Features of Birds:
- Have 2 wings to fly
- Have 2 legs
- Have feathers
- Have beak (no teeth)
- Lay eggs
- Most can fly

Common Birds:
1. SPARROW - small, brown, found in cities
2. CROW - black, smart bird
3. PIGEON - gray, found everywhere
4. PARROT - colorful, can talk
5. PEACOCK - National Bird of India
6. EAGLE - large, sharp eyes
7. OWL - active at night
8. HEN - gives us eggs
9. DUCK - swims in water

What do birds eat?
- Seeds and grains (sparrow)
- Worms and insects (crow)
- Fish (kingfisher)
- Fruits (parrot)

Birds make nests using:
- Grass
- Twigs
- Mud
- Feathers

INSECTS:
Small creatures with 6 legs.

Features of Insects:
- Have 6 legs
- Have 3 body parts (head, thorax, abdomen)
- Most have wings
- Have antennae
- Compound eyes

Common Insects:

1. BUTTERFLY
- Beautiful, colorful wings
- Drinks nectar from flowers
- Helps in pollination

2. BEE
- Makes honey
- Has stinger
- Lives in beehives
- Important for plants

3. ANT
- Very small but strong
- Lives in colonies
- Works together

4. MOSQUITO
- Very small
- Bites and sucks blood
- Spreads diseases
- Keep away from them

5. HOUSEFLY
- Lives in dirty places
- Spreads disease
- Keep food covered

6. DRAGONFLY
- Big wings
- Found near water

7. LADYBUG
- Small, red with black spots
- Helps farmers (eats bad insects)

8. SPIDER
- NOT an insect (has 8 legs)
- Makes webs to catch insects

Help vs Harm:
HELPFUL:
- Bees (honey, pollination)
- Butterflies (pollination)
- Ladybugs (eat pests)
- Earthworms (good for soil)

HARMFUL:
- Mosquitoes (spread disease)
- Houseflies (carry germs)
- Cockroaches (dirty)
- Some pests (eat crops)

How to Protect from Harmful Insects:
- Keep house clean
- Cover food
- Use mosquito nets
- Don't keep stagnant water'''},

    # Grade 3 additions
    {'g': 3, 's': 'Science', 't': 'Light and Sound',
     'd': 'Understanding light and sound around us',
     'c': '''LIGHT AND SOUND

LIGHT:
Light helps us see things.

Sources of Light:

NATURAL Sources:
- SUN (most important)
- MOON (reflects sun's light)
- STARS
- LIGHTNING
- FIRE
- Glowing insects (firefly)

ARTIFICIAL Sources:
- BULBS
- TUBE LIGHTS
- LED LIGHTS
- CANDLES
- LAMPS
- TORCH

Properties of Light:
1. Light travels in STRAIGHT LINES
2. Light travels very FAST
3. Light helps us SEE
4. Light has 7 colors (Rainbow)

Light passes through:
- TRANSPARENT objects: glass, water (can see through)
- TRANSLUCENT objects: thin paper, ground glass (partially through)
- OPAQUE objects: wood, metal, book (cannot pass)

SHADOWS:
- Made when light is blocked
- Shadow is dark area behind object
- Long shadows in morning and evening
- Short shadows at noon
- No shadow at night (no sunlight)

Activity:
Stand under sun and see your shadow!
- Morning: long shadow
- Noon: short shadow
- Evening: long shadow again

SOUND:
Sound is what we hear.

Sources of Sound:

NATURAL Sounds:
- Wind blowing
- Rain falling
- Thunder
- Birds chirping
- Animals (cow moo, dog bark)
- Waves crashing
- People talking, singing

MADE Sounds:
- Music (radio, TV)
- Vehicles (horn, engine)
- Machines
- Bell ringing
- Crackers

How Sound Travels:
- Sound travels through AIR
- Sound also travels through WATER and SOLIDS
- Sound needs a medium to travel
- In space (no air), there is NO sound

Types of Sounds:
- LOUD sounds: thunder, drums
- SOFT sounds: whisper, leaves rustling
- PLEASANT sounds: music, birds singing
- UNPLEASANT sounds: noise, horns

Animal Sounds:
- Dog: barks (woof woof)
- Cat: meows (meow)
- Cow: moos (moo)
- Lion: roars
- Sheep: bleats (baa)
- Horse: neighs
- Duck: quacks
- Bird: chirps

Our Ears Hear Sound:
- We have 2 ears
- Ears catch sound waves
- Brain understands sounds
- Keep ears clean

Protect Your Ears:
- Don't put anything in ears
- Don't listen to loud sounds
- Don't shout in someone's ear
- Use earbuds carefully

Noise Pollution:
Too much loud sound is bad.
- From vehicles
- From construction
- From loud music
- Causes headache, irritation

How to Reduce Noise:
- Don't use unnecessary horns
- Keep TV/music at moderate volume
- Plant more trees (absorb sound)'''},

    # Grade 4 additions
    {'g': 4, 's': 'Social Studies', 't': 'Maps and Directions',
     'd': 'Learn to read maps and find directions',
     'c': '''MAPS AND DIRECTIONS

MAP:
A drawing of a place from above.

Types of Maps:
1. PHYSICAL MAP - shows mountains, rivers, lakes
2. POLITICAL MAP - shows countries, states, cities
3. WEATHER MAP - shows climate
4. ROUTE MAP - shows roads to travel

Parts of a Map:

1. TITLE
- Tells what the map shows
- Written at top

2. SYMBOLS / LEGEND
- Pictures for places
- Each symbol explained

3. SCALE
- Shows distance
- Real distance vs map distance
- Example: 1 cm = 10 km

4. COMPASS
- Shows directions

DIRECTIONS:

Four Main Directions:
1. NORTH (N) - up
2. SOUTH (S) - down
3. EAST (E) - right (where sun rises)
4. WEST (W) - left (where sun sets)

In-between Directions:
- NORTH-EAST (NE)
- NORTH-WEST (NW)
- SOUTH-EAST (SE)
- SOUTH-WEST (SW)

Sun and Direction:
- Sun RISES in EAST
- Sun SETS in WEST
- At noon, sun is in SOUTH (in India)

Magnetic Compass:
- A tool to find directions
- Has a needle
- Red end points NORTH
- Always shows correct direction

Reading a Map:

Step 1: Look at title - what does it show?
Step 2: Find compass - which way is North?
Step 3: Check legend - what do symbols mean?
Step 4: Use scale - how far are places?
Step 5: Locate places using directions

Common Map Symbols:
- Triangle: Mountain
- Wavy lines: River
- Circle: City
- Star: Capital
- Black line: Road
- Blue: Water
- Green: Forests/Plains
- Brown: Mountains
- Yellow: Desert

Famous Maps in India:
- Map of India
- Map of your state
- World map
- City maps for tourists

Activity:
Draw a map of your classroom or home!
Include:
- Title at top
- Compass showing North
- Symbols for door, window, table
- Scale (1 cm = 1 meter)

Why Maps are Useful:
- Find places you don't know
- Plan trips and travel
- Understand geography
- Find friends' houses

Modern Maps:
- GPS in phones
- Google Maps
- Show roads, traffic
- Voice directions
- Real-time location

Latitude and Longitude:
- IMAGINARY LINES on Earth
- LATITUDES go East-West
- LONGITUDES go North-South
- Used to find exact location
- Like an address for places'''},

    # Grade 5 additions
    {'g': 5, 's': 'Science', 't': 'Force and Energy',
     'd': 'Understanding force, work, and energy',
     'c': '''FORCE AND ENERGY

FORCE:
A push or pull on something.

Effects of Force:
1. Makes things MOVE
2. Makes things STOP
3. Changes DIRECTION
4. Changes SHAPE
5. Changes SPEED

Examples:
- Push a door to open
- Pull a chair to sit
- Kick a ball to play
- Press dough to flatten
- Stretch a rubber band

Types of Force:

1. MUSCULAR FORCE
- Force from our muscles
- Lifting books, pulling cart
- Animals use muscular force

2. GRAVITATIONAL FORCE
- Earth pulls everything DOWN
- That's why things fall
- Discovered by Newton
- Keeps us on ground

3. FRICTIONAL FORCE
- When 2 surfaces touch
- OPPOSES movement
- Helps us walk
- Wears out things

4. MAGNETIC FORCE
- Magnets attract iron
- Magnets attract/repel each other
- Used in compass

5. ELECTROSTATIC FORCE
- Rub a comb on hair
- Attracts small papers
- Static electricity

ENERGY:
The ability to do work.

Forms of Energy:

1. LIGHT ENERGY
- From sun, bulb
- Helps us see
- Plants use for photosynthesis

2. HEAT ENERGY
- From sun, fire, stove
- Makes things warm
- Used to cook

3. SOUND ENERGY
- From music, speech
- Travels through air

4. ELECTRICAL ENERGY
- From batteries, plugs
- Runs TV, fans, lights

5. MECHANICAL ENERGY
- Energy of motion
- Moving cars, flowing water

6. CHEMICAL ENERGY
- Stored in batteries
- Stored in food (we eat)
- In fuels (petrol, gas)

7. KINETIC ENERGY
- Energy of MOTION
- Running, falling water

8. POTENTIAL ENERGY
- Stored energy
- A stretched rubber band
- Object placed high

Energy Cannot be Made or Destroyed:
- It only changes from one form to another
- Sun energy -> Plant food -> Our food -> Energy

Sources of Energy:

RENEWABLE (Can use again):
- Solar (sun)
- Wind
- Water
- Biomass

NON-RENEWABLE (Will finish):
- Coal
- Petroleum
- Natural gas

Use Energy Wisely:
- Turn off lights when not needed
- Don't waste water
- Use bicycles for short trips
- Use natural light
- Plant trees

Activity:
Find energy sources at home:
- Sun: solar heating
- Battery: in remote
- Electricity: bulbs, fans
- Food: gives us energy
- Fuel: in vehicles

Work and Power:
- Work = Force x Distance
- Power = Work / Time
- More power = faster work
- Different machines have different power

Simple Machines:
- LEVER (seesaw)
- PULLEY (lifting water)
- INCLINED PLANE (ramp)
- WHEEL (vehicles)
- SCREW (holds things)
- WEDGE (axe)'''},

    # Grade 6 additions
    {'g': 6, 's': 'Science', 't': 'Body Movements',
     'd': 'Bones, joints and human movements',
     'c': '''BODY MOVEMENTS

How Do We Move?
Our body moves because of BONES, MUSCLES, and JOINTS.

THE SKELETAL SYSTEM:

Total Bones: 206 (in adult)
Total Bones in baby: about 270 (some fuse together)

Functions of Skeleton:
1. Gives SHAPE to body
2. Provides SUPPORT
3. PROTECTS internal organs
4. Helps in MOVEMENT
5. Makes BLOOD CELLS

Important Bones:

SKULL:
- Hard, protects BRAIN
- Has many bones fused together

SPINE / VERTEBRAL COLUMN:
- 33 bones called VERTEBRAE
- Runs from neck to lower back
- Protects spinal cord
- Allows us to stand straight

RIB CAGE:
- 12 pairs of ribs
- Forms cage around heart and lungs
- Protects them

SHOULDER BONES:
- Help arms move

PELVIC GIRDLE:
- Hip bones
- Helps legs move

ARM BONES:
- Upper arm: humerus
- Lower arm: radius and ulna
- Hands: many small bones

LEG BONES:
- Thigh: femur (longest bone)
- Below knee: tibia and fibula
- Feet: small bones

JOINTS:
Where two bones meet.

Types of Joints:

1. BALL AND SOCKET JOINT
- Allows movement in all directions
- Example: SHOULDER, HIP

2. HINGE JOINT
- Allows movement in ONE direction
- Like a door hinge
- Example: KNEE, ELBOW

3. PIVOT JOINT
- Allows rotation
- Example: NECK (head moves)

4. FIXED JOINT
- No movement
- Example: SKULL bones

5. GLIDING JOINT
- Bones slide over each other
- Example: WRIST, ANKLE

MUSCLES:
Help bones move.

Working in Pairs:
- When you bend arm: BICEPS contracts, TRICEPS relaxes
- When you straighten arm: TRICEPS contracts, BICEPS relaxes
- Muscles work in opposite pairs

GAITS - How Different Animals Move:

HUMANS:
- Walk on 2 legs
- Have hands free for work

EARTHWORM:
- Has no bones
- Has muscles and bristles
- Stretches and contracts to move

COCKROACH:
- 6 legs
- 3 pairs of legs
- Has wings

BIRDS:
- 2 legs and 2 wings
- Hollow bones (light)
- Strong chest muscles to flap wings

FISH:
- Streamlined body
- Fins to swim
- Tail to push through water

SNAKES:
- No legs
- Long backbone
- Muscles help move in waves

Caring for Bones:

1. Drink MILK (calcium)
2. Eat fruits and vegetables
3. Get sunlight (Vitamin D)
4. Exercise daily
5. Sit and stand properly
6. Don't carry very heavy weights

Common Injuries:
- FRACTURE: Bone breaks
- SPRAIN: Joint twisted
- DISLOCATION: Bone moves out of joint

First Aid:
- For fracture: Keep still, see doctor
- For sprain: Ice, rest

Posture:
- Sit with back straight
- Walk with shoulders back
- Don't bend over phone too long'''},

    # Grade 7 additions
    {'g': 7, 's': 'Social Studies', 't': 'Climate and Adaptations',
     'd': 'Different climates and how living things adapt',
     'c': '''CLIMATE AND ADAPTATIONS

WEATHER vs CLIMATE:

WEATHER:
- Day-to-day changes
- Temperature, rain, wind
- Changes quickly
- Like today is sunny

CLIMATE:
- Average weather over MANY YEARS (25+)
- Doesn't change quickly
- Like India has hot climate
- A region has specific climate

What Affects Climate?
1. LATITUDE - distance from equator
2. ALTITUDE - height above sea level
3. DISTANCE FROM SEA
4. WIND DIRECTION
5. OCEAN CURRENTS
6. RAINFALL

CLIMATE ZONES:

1. POLAR ZONE
- Near North/South Poles
- Very COLD all year
- Snow and ice
- Examples: Arctic, Antarctica

2. TEMPERATE ZONE
- Between polar and tropical
- Four seasons
- Moderate climate
- Examples: Europe, USA

3. TROPICAL ZONE
- Near equator
- HOT all year
- Lots of rain
- Examples: India, Brazil, Africa

ADAPTATIONS:
How living things change to survive in their climate.

POLAR REGION ANIMALS:

1. POLAR BEAR
- Thick white fur (keeps warm and hides in snow)
- Thick layer of fat
- Large paws to walk on snow
- Strong swimmer

2. PENGUIN
- Layers of feathers (waterproof)
- Fat for warmth
- Huddle together for warmth
- Cannot fly but excellent swimmer

3. SEAL
- Thick fat (blubber)
- Slippery skin
- Streamlined for swimming

4. ARCTIC FOX
- White fur in winter
- Brown fur in summer
- Camouflage

TROPICAL RAINFOREST ANIMALS:

1. MONKEY
- Strong arms to swing
- Long tail for balance
- Lives on trees

2. LION
- Lives in grasslands
- Sharp teeth, claws
- Tan color (camouflage)

3. ELEPHANT
- Large size, thick skin
- Long trunk for water
- Lives in jungles

4. SNAKE
- Skin sheds in hot climate
- Some swallow whole
- Hide in trees/ground

5. TOUCAN
- Large colorful beak
- Bright colors
- Eats fruits in trees

DESERT ADAPTATIONS:

1. CAMEL
- Hump stores fat
- Long eyelashes against sand
- Wide feet on sand
- Can go days without water
- Closed nostrils in sandstorm

2. CACTUS
- Thick stem stores water
- Spines instead of leaves (less water loss)
- Deep roots
- Waxy coating

WATER ANIMALS:

1. FISH
- Gills to breathe in water
- Streamlined body
- Scales
- Fins to swim

2. DOLPHIN
- Lung but lives in water
- Comes up to breathe
- Smooth skin
- Smart and social

INDIA'S CLIMATE:

India has TROPICAL MONSOON climate.

Three Seasons:
1. SUMMER (March-June): Hot, dry
2. RAINY/MONSOON (July-September): Heavy rain
3. WINTER (December-February): Cool

Monsoon Importance:
- Brings rain
- Important for farming
- Filling rivers, lakes
- Drinking water

Climate of Different Regions:

1. NORTHERN PLAINS
- Hot summers, cold winters
- Moderate rainfall

2. RAJASTHAN
- Hot desert
- Very little rain

3. WESTERN GHATS
- Heavy rainfall
- Tropical forests

4. NORTH-EAST (Cherrapunji)
- Wettest place on Earth
- Very heavy rain

5. HIMALAYAS
- Cold throughout year
- Snow at higher altitudes

6. KERALA / COASTAL
- Hot and humid
- Good rainfall

CLIMATE CHANGE:
- Earth getting warmer
- Caused by:
  * Pollution
  * Cutting trees
  * Burning fuels
- Effects:
  * Glaciers melting
  * Sea level rising
  * Extreme weather

What We Can Do:
- Plant trees
- Use bicycles
- Save electricity
- Don't waste water
- Use less plastic
- Recycle'''},

    # Grade 8 additions
    {'g': 8, 's': 'Science', 't': 'Light and Sound Phenomena',
     'd': 'Reflection, refraction, sound waves',
     'c': '''LIGHT AND SOUND PHENOMENA

LIGHT:

What is Light?
Light is a form of energy that helps us see.

Speed of Light:
- 3,00,000 km per second
- Fastest in universe
- From Sun to Earth: 8 minutes

PROPERTIES OF LIGHT:

1. Light travels in STRAIGHT LINES
2. Light can be REFLECTED
3. Light can be REFRACTED
4. Light has SPEED
5. Light is COMPOSED of colors

REFLECTION:
When light bounces back from a surface.

Examples:
- Mirror image
- Seeing yourself in water
- Shiny surfaces

Laws of Reflection:
1. Angle of incidence = Angle of reflection
2. Incident ray, reflected ray, normal in same plane

MIRRORS:

1. PLANE MIRROR
- Flat mirror
- Image: erect, same size
- Image at same distance behind
- Lateral inversion

2. CONCAVE MIRROR
- Curved inward
- Can magnify
- Used in dentist mirror, telescope

3. CONVEX MIRROR
- Curved outward
- Always smaller image
- Used in vehicle side mirrors

REFRACTION:
Light bends when entering different medium.

Examples:
- Pencil looks bent in water
- Mirage in deserts
- Star twinkling
- Lens working

LENSES:

1. CONVEX LENS
- Thicker in middle
- Magnifies things
- Used in: Magnifying glass, microscope, eye glasses (long-sightedness)

2. CONCAVE LENS
- Thinner in middle
- Makes things smaller
- Used in: Glasses for short-sightedness

THE HUMAN EYE:

Parts:
- CORNEA: Front transparent layer
- IRIS: Colored part with hole (pupil)
- PUPIL: Opening, allows light
- LENS: Focuses light
- RETINA: Light-sensitive layer
- OPTIC NERVE: Sends signal to brain

How We See:
1. Light enters through cornea
2. Pupil controls light amount
3. Lens focuses on retina
4. Retina converts to signals
5. Brain interprets the image

EYE DEFECTS:

1. MYOPIA (Short-sightedness)
- Cannot see far things clearly
- Use CONCAVE lens

2. HYPERMETROPIA (Long-sightedness)
- Cannot see near things clearly
- Use CONVEX lens

3. CATARACT
- Lens becomes cloudy
- Surgery needed

DISPERSION:
- White light splits into 7 colors through prism
- Rainbow colors: VIBGYOR
- Violet, Indigo, Blue, Green, Yellow, Orange, Red

SCATTERING:
- Why sky is BLUE
- Why sunset is RED
- Why warning lights are RED

SOUND:

What is Sound?
Sound is a form of energy produced by vibrations.

How Sound Travels:
- Sound needs a MEDIUM
- Travels through air, water, solids
- CANNOT travel through vacuum (space)

Speed of Sound:
- In air: 340 m/s
- In water: 1500 m/s
- In steel: 5000 m/s
- Faster in denser medium

CHARACTERISTICS OF SOUND:

1. PITCH (Frequency)
- High pitch: female voice, whistle
- Low pitch: male voice, drum

2. LOUDNESS (Amplitude)
- Loud: thunder
- Soft: whisper
- Measured in DECIBELS (dB)

3. QUALITY/TIMBRE
- Why violin sounds different from guitar
- Even at same pitch

HUMAN EAR:

Parts:
- OUTER EAR: Catches sound
- MIDDLE EAR: 3 small bones (vibrate)
- INNER EAR: Cochlea, converts to signals
- EARDRUM: Membrane that vibrates

How We Hear:
1. Sound waves enter outer ear
2. Eardrum vibrates
3. 3 bones amplify vibration
4. Cochlea converts to nerve signals
5. Brain interprets the sound

HEARING RANGE:
- Humans: 20 Hz to 20,000 Hz
- Dogs: 40 Hz to 60,000 Hz (hear higher pitches)
- Bats: Up to 1,00,000 Hz (use echo)
- Elephants: Down to 10 Hz

ULTRASOUND:
Sound above 20,000 Hz
Uses:
- Medical scanning (pregnancy)
- Cleaning jewelry
- Detection of cracks
- Echo location

NOISE POLLUTION:
Too much loud sound.
Causes:
- Hearing problems
- Stress
- Headache

Sources:
- Vehicles
- Factories
- Loud music
- Construction

How to Reduce:
- Use silent vehicles
- Don't use horns unnecessarily
- Limit music volume
- Plant more trees

PROTECT YOUR EARS:
- Don't use earphones loudly
- Don't put things in ears
- Avoid loud noise
- Keep ears clean and dry
- Visit doctor if pain'''},

    # Grade 9 additions
    {'g': 9, 's': 'Mathematics', 't': 'Real Numbers and Number Systems',
     'd': 'Types of numbers and their properties',
     'c': '''REAL NUMBERS AND NUMBER SYSTEMS

CLASSIFICATION OF NUMBERS:

1. NATURAL NUMBERS (N)
1, 2, 3, 4, 5, ...
- Counting numbers
- Positive
- No zero

2. WHOLE NUMBERS (W)
0, 1, 2, 3, 4, 5, ...
- Natural numbers + 0
- All non-negative

3. INTEGERS (Z)
... -3, -2, -1, 0, 1, 2, 3, ...
- All positive and negative whole numbers
- Includes zero

4. RATIONAL NUMBERS (Q)
Numbers that can be written as p/q
where p, q are integers and q is not 0.

Examples:
- 1/2, 3/4, -5/7
- 5 (= 5/1)
- 0 (= 0/1)
- 0.5 (= 1/2)
- 0.333... (= 1/3)

Properties:
- Terminating decimals: 0.5, 0.25
- Repeating decimals: 0.333..., 0.142857142857...

5. IRRATIONAL NUMBERS
Cannot be written as p/q
Non-terminating, non-repeating decimals.

Examples:
- sqrt(2) = 1.41421356...
- pi = 3.14159265...
- e = 2.71828...
- sqrt(3) = 1.732...

6. REAL NUMBERS (R)
All rational and irrational numbers combined.

Number Line:
... <---|---|---|---|---|---|---|---> ...
       -3  -2  -1   0   1   2   3

Every real number has a point on number line.

OPERATIONS:

Addition:
2 + 3 = 5
(-2) + 3 = 1
(-2) + (-3) = -5

Subtraction:
5 - 3 = 2
3 - 5 = -2
(-5) - (-3) = -5 + 3 = -2

Multiplication:
(+) x (+) = +
(-) x (-) = +
(+) x (-) = -
(-) x (+) = -

Division:
Same as multiplication rules

EUCLID'S DIVISION LEMMA:
For any two positive integers a and b:
a = bq + r
where 0 <= r < b

Examples:
17 = 5(3) + 2 (a=17, b=5, q=3, r=2)
24 = 6(4) + 0 (24 is divisible by 6)

EUCLID'S DIVISION ALGORITHM:
Used to find HCF of two numbers.

Find HCF of 156 and 88:
Step 1: 156 = 88(1) + 68
Step 2: 88 = 68(1) + 20
Step 3: 68 = 20(3) + 8
Step 4: 20 = 8(2) + 4
Step 5: 8 = 4(2) + 0
HCF = 4

FUNDAMENTAL THEOREM OF ARITHMETIC:
Every composite number can be written as PRODUCT of primes (in only one way).

Examples:
12 = 2 x 2 x 3 = 2^2 x 3
60 = 2 x 2 x 3 x 5 = 2^2 x 3 x 5

HCF and LCM:
HCF(a,b) x LCM(a,b) = a x b

Example: Find HCF and LCM of 12 and 18
12 = 2^2 x 3
18 = 2 x 3^2
HCF = 2 x 3 = 6
LCM = 2^2 x 3^2 = 36
Check: 6 x 36 = 216
       12 x 18 = 216 ✓

DECIMAL EXPANSION:

TERMINATING DECIMALS:
Denominator has only 2 and/or 5 as factors.

Examples:
1/2 = 0.5
3/4 = 0.75
1/5 = 0.2
3/10 = 0.3
7/8 = 0.875

NON-TERMINATING REPEATING DECIMALS:
Denominator has factors other than 2 and 5.

Examples:
1/3 = 0.333... (repeating 3)
1/7 = 0.142857142857... (repeating 142857)
2/11 = 0.181818... (repeating 18)

NON-TERMINATING NON-REPEATING:
These are IRRATIONAL numbers.

Examples:
sqrt(2) = 1.41421356237...
pi = 3.14159265358...

LAWS OF EXPONENTS:

For real numbers a, b and integers m, n:

1. a^m x a^n = a^(m+n)
   Example: 2^3 x 2^4 = 2^7 = 128

2. a^m / a^n = a^(m-n)
   Example: 2^5 / 2^3 = 2^2 = 4

3. (a^m)^n = a^(mn)
   Example: (2^3)^2 = 2^6 = 64

4. (ab)^n = a^n x b^n
   Example: (2 x 3)^2 = 4 x 9 = 36

5. a^0 = 1 (any number to power 0)
   Example: 5^0 = 1

6. a^(-n) = 1/a^n
   Example: 2^(-3) = 1/8

RATIONALIZATION:
Making denominator a rational number.

Example: Rationalize 1/sqrt(2)
1/sqrt(2) = 1/sqrt(2) x sqrt(2)/sqrt(2) = sqrt(2)/2

PROOF: sqrt(2) is IRRATIONAL.

Assume sqrt(2) is rational.
sqrt(2) = p/q (where p, q have no common factor)
Squaring: 2 = p^2/q^2
2q^2 = p^2
So p^2 is even, p is even
Let p = 2k
2q^2 = 4k^2
q^2 = 2k^2
So q^2 is even, q is even

But we said p and q have no common factor!
This is a contradiction.
Therefore, sqrt(2) is IRRATIONAL.'''},

    # Grade 10 additions
    {'g': 10, 's': 'Mathematics', 't': 'Real Numbers and HCF LCM',
     'd': 'Euclid algorithm, HCF, LCM, and irrational numbers',
     'c': '''REAL NUMBERS (CLASS 10)

EUCLID'S DIVISION LEMMA:
For positive integers a and b, there exist unique integers q and r such that:
a = bq + r, where 0 <= r < b

This is the basis for finding HCF.

EUCLID'S DIVISION ALGORITHM:

Steps to find HCF(a, b) where a > b:

Step 1: Divide a by b
a = bq1 + r1

Step 2: If r1 = 0, HCF = b
        Else divide b by r1
b = r1q2 + r2

Step 3: Continue until remainder is 0
The last non-zero remainder is HCF.

Example: Find HCF(196, 38220)

38220 = 196 x 195 + 0
HCF = 196

Example: Find HCF(420, 130)
420 = 130 x 3 + 30
130 = 30 x 4 + 10
30 = 10 x 3 + 0
HCF = 10

FUNDAMENTAL THEOREM OF ARITHMETIC:

Every composite number can be expressed as a PRODUCT of PRIMES, and this factorization is UNIQUE (apart from order).

Examples:
12 = 2 x 2 x 3
36 = 2^2 x 3^2
72 = 2^3 x 3^2

PRIME FACTORIZATION:
Breaking number into prime factors.

Example: Find prime factorization of 8400
8400 = 2 x 4200
     = 2 x 2 x 2100
     = 2 x 2 x 2 x 1050
     = 2 x 2 x 2 x 2 x 525
     = 2^4 x 3 x 175
     = 2^4 x 3 x 5 x 35
     = 2^4 x 3 x 5 x 5 x 7
     = 2^4 x 3 x 5^2 x 7

HCF AND LCM USING PRIME FACTORIZATION:

HCF: Product of COMMON prime factors with LOWEST power.
LCM: Product of ALL prime factors with HIGHEST power.

Example: Find HCF and LCM of 12 and 18
12 = 2^2 x 3
18 = 2 x 3^2

HCF = 2^1 x 3^1 = 6 (taking lowest power)
LCM = 2^2 x 3^2 = 36 (taking highest power)

VERIFICATION:
HCF x LCM = product of numbers
6 x 36 = 216
12 x 18 = 216 ✓

IRRATIONAL NUMBERS:

A number is IRRATIONAL if it cannot be written as p/q.

Examples:
sqrt(2), sqrt(3), sqrt(5)
sqrt(7), pi, e

PROOF THAT sqrt(2) IS IRRATIONAL:

Assumption: sqrt(2) is rational.
Then sqrt(2) = p/q (p, q are coprime, q is not 0)

Squaring both sides:
2 = p^2/q^2
2q^2 = p^2

So p^2 is even, which means p is even.
Let p = 2k for some integer k.
Then p^2 = 4k^2

Substituting:
2q^2 = 4k^2
q^2 = 2k^2

So q^2 is even, which means q is even.

But we assumed p and q are coprime!
If both are even, they have common factor 2.
This is a CONTRADICTION.

Therefore, sqrt(2) is IRRATIONAL.

THEOREM: For prime p, sqrt(p) is irrational.

RATIONAL vs IRRATIONAL:

If x is rational and y is irrational, then:
- x + y is irrational
- x - y is irrational
- x * y is irrational (if x is not 0)
- x / y is irrational (if y is not 0)

Examples:
3 + sqrt(2) is IRRATIONAL
2 * sqrt(3) is IRRATIONAL
1 / sqrt(5) is IRRATIONAL

DECIMAL EXPANSION OF RATIONAL NUMBERS:

A rational number p/q (q != 0) is:

1. TERMINATING DECIMAL
- When q has only 2 and/or 5 as prime factors
Examples:
1/2 = 0.5
3/4 = 0.75
7/8 = 0.875
3/10 = 0.3
11/100 = 0.11

2. NON-TERMINATING REPEATING DECIMAL
- When q has prime factors other than 2 and 5
Examples:
1/3 = 0.333...
1/7 = 0.142857142857...
5/11 = 0.454545...

THEOREM:
Let x = p/q be rational such that prime factorization of q is of form 2^n x 5^m, then x has a terminating decimal expansion.

Otherwise, the decimal is non-terminating and recurring.

WORD PROBLEMS:

Problem 1:
Three bells ring at intervals of 9, 12, and 15 minutes. If they ring together at 8:00 AM, when will they next ring together?

Solution: Find LCM of 9, 12, 15
9 = 3^2
12 = 2^2 x 3
15 = 3 x 5
LCM = 2^2 x 3^2 x 5 = 180 minutes = 3 hours

They will ring together at 11:00 AM.

Problem 2:
Find the largest number that divides 245 and 1029 leaving remainder 5 in each case.

Solution:
245 - 5 = 240
1029 - 5 = 1024
Find HCF(240, 1024)
1024 = 240 x 4 + 64
240 = 64 x 3 + 48
64 = 48 x 1 + 16
48 = 16 x 3 + 0
HCF = 16

The number is 16.

USEFUL TIPS:

- 0 is even
- 1 is neither prime nor composite
- 2 is the only EVEN prime number
- Every number has at least 1 and itself as factors
- Smallest prime: 2
- Smallest composite: 4
- 1 is a factor of every number'''}
]


def add_all():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Teacher not found")
            return

        os.makedirs('./data/resources', exist_ok=True)
        existing = {r.title for r in Resource.query.all()}

        added = 0
        for r in NEW_RESOURCES:
            if r['t'] in existing:
                print(f"[SKIP] {r['t']}")
                continue

            filename = f"ncert_g{r['g']}_{r['s'].replace(' ', '_')}_{r['t'].replace(' ', '_')[:40]}"
            txt_path = f"data/resources/{filename}.txt"
            pdf_path = f"data/resources/{filename}.pdf"

            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(r['c'])

            try:
                pdf = PDF(title=r['t'], subject=r['s'], grade=r['g'])
                pdf.add_page()
                pdf.render(r['c'])
                pdf.output(pdf_path)
            except Exception as e:
                print(f"[PDF ERR] {r['t']}: {e}")
                continue

            file_size = os.path.getsize(pdf_path)
            yt_url, yt_ch = get_youtube(r['t'])
            ncert_url, ncert_ch = get_ncert(r['g'], r['s'], r['t'])

            resource = Resource(
                title=r['t'], description=r['d'], subject=r['s'],
                grade_level=r['g'], content_type='pdf', file_path=pdf_path,
                file_size=file_size, youtube_url=yt_url, youtube_channel=yt_ch,
                ncert_url=ncert_url, ncert_chapter=ncert_ch,
                created_by=teacher.id, is_published=True
            )
            db.session.add(resource)
            added += 1
            print(f"[ADDED] Grade {r['g']} - {r['t']}")

        db.session.commit()
        print(f"\n[DONE] Added {added} new resources. Total: {Resource.query.count()}")


if __name__ == '__main__':
    try:
        add_all()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
