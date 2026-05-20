"""
Complete NCERT Content Loader
Creates resources AND matching quizzes for ALL grades 1-10
All 4 subjects: Mathematics, Science, English, Social Studies

Each topic includes:
- A text resource with study material
- A matching quiz testing the resource content
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Quiz, QuizQuestion, Resource

# ============================================================
# COMPLETE NCERT CONTENT - Resources + Matching Quizzes
# ============================================================

NCERT_TOPICS = [
    # ==================== GRADE 1 ====================
    {
        'grade': 1, 'subject': 'Mathematics', 'title': 'Numbers 1 to 100',
        'description': 'Learn to count, read and write numbers from 1 to 100',
        'content': '''NUMBERS 1 TO 100

Counting Numbers:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
11, 12, 13, 14, 15, 16, 17, 18, 19, 20

Tens:
10, 20, 30, 40, 50, 60, 70, 80, 90, 100

Number Names:
1-One, 2-Two, 3-Three, 4-Four, 5-Five
6-Six, 7-Seven, 8-Eight, 9-Nine, 10-Ten

Comparing Numbers:
- Greater than (>): 5 > 3
- Less than (<): 2 < 7
- Equal to (=): 4 = 4

Before and After:
- Number before 5 is 4
- Number after 5 is 6
- Between 3 and 5 is 4

Odd and Even:
- Even: 2, 4, 6, 8, 10 (can be split into pairs)
- Odd: 1, 3, 5, 7, 9''',
        'quiz_questions': [
            {'q': 'What comes after 9?', 'a': '8', 'b': '10', 'c': '11', 'd': '7', 'correct': 'B'},
            {'q': 'Which is greater: 7 or 4?', 'a': '7', 'b': '4', 'c': 'Same', 'd': 'None', 'correct': 'A'},
            {'q': 'What is the number name for 5?', 'a': 'Three', 'b': 'Four', 'c': 'Five', 'd': 'Six', 'correct': 'C'},
            {'q': 'Which is an even number?', 'a': '3', 'b': '7', 'c': '8', 'd': '5', 'correct': 'C'},
            {'q': 'What comes between 6 and 8?', 'a': '5', 'b': '7', 'c': '9', 'd': '10', 'correct': 'B'},
        ]
    },
    {
        'grade': 1, 'subject': 'Mathematics', 'title': 'Shapes Around Us',
        'description': 'Learn basic shapes: circle, square, triangle, rectangle',
        'content': '''SHAPES AROUND US

Basic Shapes:

1. CIRCLE - Round shape, no corners
   Examples: Ball, Coin, Sun, Wheel

2. SQUARE - 4 equal sides, 4 corners
   Examples: Chess board, Dice, Table mat

3. TRIANGLE - 3 sides, 3 corners
   Examples: Pizza slice, Mountain, Roof

4. RECTANGLE - 4 sides (2 long, 2 short), 4 corners
   Examples: Door, Book, Phone, Window

Finding Shapes:
- Look around your room
- Identify shapes in everyday objects
- A clock face is a CIRCLE
- A blackboard is a RECTANGLE

Solid Shapes:
- Sphere (like a ball)
- Cube (like a dice)
- Cylinder (like a pipe)
- Cone (like an ice-cream cone)''',
        'quiz_questions': [
            {'q': 'How many sides does a triangle have?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'B'},
            {'q': 'Which shape has no corners?', 'a': 'Square', 'b': 'Triangle', 'c': 'Circle', 'd': 'Rectangle', 'correct': 'C'},
            {'q': 'A dice is shaped like a?', 'a': 'Sphere', 'b': 'Cube', 'c': 'Cylinder', 'd': 'Cone', 'correct': 'B'},
            {'q': 'A square has ___ equal sides', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'C'},
        ]
    },
    {
        'grade': 1, 'subject': 'Science', 'title': 'My Body',
        'description': 'Learn about parts of the human body and their functions',
        'content': '''MY BODY

External Parts of Body:

HEAD: Has eyes, ears, nose, mouth
- Eyes: To SEE (we have 2 eyes)
- Ears: To HEAR (we have 2 ears)
- Nose: To SMELL and BREATHE
- Mouth: To EAT and SPEAK
- Tongue: To TASTE

HANDS: 2 hands, each with 5 fingers
- Used to hold, write, eat

LEGS: 2 legs to walk, run, jump

SKIN: Covers our whole body, helps us feel touch

Keeping Body Healthy:
1. Bathe daily
2. Brush teeth twice a day
3. Wash hands before eating
4. Eat fruits and vegetables
5. Drink lots of water
6. Sleep 8 hours daily
7. Exercise regularly

Sense Organs:
- Eyes - See
- Ears - Hear
- Nose - Smell
- Tongue - Taste
- Skin - Touch''',
        'quiz_questions': [
            {'q': 'How many eyes do we have?', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'correct': 'B'},
            {'q': 'Which organ helps us taste?', 'a': 'Eyes', 'b': 'Ears', 'c': 'Tongue', 'd': 'Nose', 'correct': 'C'},
            {'q': 'How many fingers on one hand?', 'a': '4', 'b': '5', 'c': '6', 'd': '10', 'correct': 'B'},
            {'q': 'We breathe through our?', 'a': 'Ears', 'b': 'Eyes', 'c': 'Nose', 'd': 'Mouth', 'correct': 'C'},
            {'q': 'Which sense organ is our skin?', 'a': 'Sight', 'b': 'Hearing', 'c': 'Touch', 'd': 'Smell', 'correct': 'C'},
        ]
    },
    {
        'grade': 1, 'subject': 'English', 'title': 'The Alphabet A-Z',
        'description': 'Learn all letters of English alphabet with examples',
        'content': '''THE ENGLISH ALPHABET

The English alphabet has 26 letters.

Capital Letters: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Small Letters: a b c d e f g h i j k l m n o p q r s t u v w x y z

Vowels (5 letters): A E I O U
Consonants (21 letters): All others

Letter Examples:
A is for Apple
B is for Ball
C is for Cat
D is for Dog
E is for Elephant
F is for Fish
G is for Goat
H is for House
I is for Ice
J is for Jug
K is for Kite
L is for Lion
M is for Mango
N is for Nest
O is for Orange
P is for Parrot
Q is for Queen
R is for Rabbit
S is for Sun
T is for Tree
U is for Umbrella
V is for Violin
W is for Window
X is for Xylophone
Y is for Yak
Z is for Zebra''',
        'quiz_questions': [
            {'q': 'How many letters in English alphabet?', 'a': '24', 'b': '25', 'c': '26', 'd': '27', 'correct': 'C'},
            {'q': 'How many vowels are there?', 'a': '3', 'b': '4', 'c': '5', 'd': '6', 'correct': 'C'},
            {'q': 'Which letter comes after M?', 'a': 'L', 'b': 'N', 'c': 'O', 'd': 'P', 'correct': 'B'},
            {'q': 'Which is a vowel?', 'a': 'B', 'b': 'C', 'c': 'E', 'd': 'F', 'correct': 'C'},
            {'q': 'Z is for ___', 'a': 'Yak', 'b': 'Zebra', 'c': 'Xylophone', 'd': 'Window', 'correct': 'B'},
        ]
    },
    {
        'grade': 1, 'subject': 'Social Studies', 'title': 'My Family',
        'description': 'Learn about family members and relationships',
        'content': '''MY FAMILY

A family is a group of people who live together and care for each other.

Members of Family:

NUCLEAR FAMILY (Small family):
- Father
- Mother
- Children (brothers, sisters)

JOINT FAMILY (Big family):
Same as nuclear plus:
- Grandfather (father's father)
- Grandmother (father's mother)
- Uncles, Aunts
- Cousins

Relationships:
- Father's father = Grandfather
- Father's mother = Grandmother
- Father's brother = Uncle (Chacha)
- Father's sister = Aunt (Bua)
- Mother's brother = Uncle (Mama)
- Mother's sister = Aunt (Maasi)

Family Helps Each Other:
- Parents earn money and take care
- Children study and help in homework
- Everyone shares love and respect

Importance of Family:
1. Provides love and care
2. Teaches values
3. Helps in difficult times
4. Celebrates happiness together''',
        'quiz_questions': [
            {'q': 'Father\'s mother is your?', 'a': 'Aunt', 'b': 'Sister', 'c': 'Grandmother', 'd': 'Cousin', 'correct': 'C'},
            {'q': 'A family with parents and children only is?', 'a': 'Joint', 'b': 'Nuclear', 'c': 'Big', 'd': 'Extended', 'correct': 'B'},
            {'q': 'Mother\'s brother is called?', 'a': 'Chacha', 'b': 'Mama', 'c': 'Bua', 'd': 'Maasi', 'correct': 'B'},
            {'q': 'Who earns money in family?', 'a': 'Only father', 'b': 'Only mother', 'c': 'Parents', 'd': 'Children', 'correct': 'C'},
        ]
    },

    # ==================== GRADE 2 ====================
    {
        'grade': 2, 'subject': 'Mathematics', 'title': 'Addition and Subtraction',
        'description': 'Master addition and subtraction with carrying and borrowing',
        'content': '''ADDITION AND SUBTRACTION

ADDITION (+) means putting together

Example 1: 5 + 3 = 8
If you have 5 apples and get 3 more, you have 8 apples.

Adding 2-digit numbers:
  25
+ 14
----
  39

Steps:
1. Add ones: 5 + 4 = 9
2. Add tens: 2 + 1 = 3
3. Write answer: 39

Addition with Carrying:
  28
+ 15
----
  43

Steps:
1. Add ones: 8 + 5 = 13, write 3, carry 1
2. Add tens: 2 + 1 + 1 = 4
3. Answer: 43

SUBTRACTION (-) means taking away

Example: 10 - 4 = 6
If you have 10 candies and eat 4, you have 6 left.

Subtraction with Borrowing:
  32
-  7
----
  25

Steps:
1. Cannot subtract 7 from 2
2. Borrow 1 from tens
3. Now 12 - 7 = 5
4. 2 in tens (since we borrowed)
5. Answer: 25''',
        'quiz_questions': [
            {'q': '15 + 7 = ?', 'a': '21', 'b': '22', 'c': '23', 'd': '24', 'correct': 'B'},
            {'q': '30 - 12 = ?', 'a': '15', 'b': '17', 'c': '18', 'd': '20', 'correct': 'C'},
            {'q': '25 + 36 = ?', 'a': '51', 'b': '61', 'c': '71', 'd': '81', 'correct': 'B'},
            {'q': '50 - 28 = ?', 'a': '12', 'b': '22', 'c': '32', 'd': '42', 'correct': 'B'},
            {'q': 'What is the symbol for addition?', 'a': '-', 'b': '+', 'c': '×', 'd': '÷', 'correct': 'B'},
        ]
    },
    {
        'grade': 2, 'subject': 'Science', 'title': 'Plants Around Us',
        'description': 'Different types of plants and their importance',
        'content': '''PLANTS AROUND US

Types of Plants:

1. TREES - Big plants with thick stems
   Examples: Mango, Banyan, Neem, Coconut

2. SHRUBS - Smaller than trees, bushy
   Examples: Rose, Hibiscus, Tulsi

3. HERBS - Soft, small plants
   Examples: Mint, Coriander, Wheat

4. CREEPERS - Grow along ground
   Examples: Pumpkin, Watermelon

5. CLIMBERS - Grow up with support
   Examples: Money plant, Grapes

Parts of a Plant:
- ROOT: Underground, takes water from soil
- STEM: Holds the plant, carries water
- LEAVES: Make food using sunlight
- FLOWERS: Beautiful, become fruits
- FRUITS: Contain seeds

What Plants Give Us:
- Food: Fruits, vegetables, grains
- Oxygen: To breathe
- Wood: For furniture
- Medicines: From neem, tulsi
- Beauty: Flowers, decoration
- Shade: From trees

Plants Need:
- Water
- Sunlight
- Air
- Soil''',
        'quiz_questions': [
            {'q': 'Big plants with thick stems are?', 'a': 'Herbs', 'b': 'Shrubs', 'c': 'Trees', 'd': 'Creepers', 'correct': 'C'},
            {'q': 'Which part makes food in plants?', 'a': 'Roots', 'b': 'Stem', 'c': 'Leaves', 'd': 'Flowers', 'correct': 'C'},
            {'q': 'Plants give us ___ to breathe', 'a': 'Carbon dioxide', 'b': 'Oxygen', 'c': 'Nitrogen', 'd': 'Hydrogen', 'correct': 'B'},
            {'q': 'Money plant is a?', 'a': 'Tree', 'b': 'Shrub', 'c': 'Climber', 'd': 'Herb', 'correct': 'C'},
            {'q': 'Plants need ___ to grow', 'a': 'Only water', 'b': 'Only soil', 'c': 'Water, sunlight, air, soil', 'd': 'Only sun', 'correct': 'C'},
        ]
    },
    {
        'grade': 2, 'subject': 'English', 'title': 'Naming Words (Nouns)',
        'description': 'Learn about nouns - names of persons, places, things',
        'content': '''NAMING WORDS (NOUNS)

A NOUN is a naming word - it names a person, place, animal, or thing.

Types of Nouns:

1. PERSON: Mom, teacher, doctor, Ravi, friend
2. PLACE: School, park, home, India, garden
3. ANIMAL: Cat, dog, lion, tiger, bird
4. THING: Book, ball, chair, pen, table

Examples in sentences:
- Ravi is my friend. (Ravi - person, friend - person)
- I go to SCHOOL. (school - place)
- A DOG barks. (dog - animal)
- I read a BOOK. (book - thing)

Common Nouns vs Proper Nouns:
- COMMON: city, river, boy, girl (general)
- PROPER: Delhi, Ganga, Ravi, Sita (specific names)
- Proper nouns start with CAPITAL letter

Singular and Plural Nouns:
- 1 book → many books (add s)
- 1 baby → many babies (y becomes ies)
- 1 child → many children (special)
- 1 man → many men (special)

Practice:
Find nouns: "The cat sat on the mat with mom."
Nouns: cat, mat, mom''',
        'quiz_questions': [
            {'q': 'Which is a noun?', 'a': 'Run', 'b': 'Book', 'c': 'Big', 'd': 'Quickly', 'correct': 'B'},
            {'q': 'Plural of "boy"?', 'a': 'Boyes', 'b': 'Boys', 'c': 'Boyies', 'd': 'Boy', 'correct': 'B'},
            {'q': 'Which is a proper noun?', 'a': 'city', 'b': 'Delhi', 'c': 'river', 'd': 'school', 'correct': 'B'},
            {'q': 'Plural of "baby"?', 'a': 'Babys', 'b': 'Babies', 'c': 'Babyes', 'd': 'Baby', 'correct': 'B'},
            {'q': 'Which noun names a place?', 'a': 'Teacher', 'b': 'Park', 'c': 'Dog', 'd': 'Pen', 'correct': 'B'},
        ]
    },
    {
        'grade': 2, 'subject': 'Social Studies', 'title': 'My Neighbourhood',
        'description': 'Learn about your neighbourhood and community helpers',
        'content': '''MY NEIGHBOURHOOD

A neighbourhood is the area around our home.

Places in Neighbourhood:
- Houses and apartments
- Shops and markets
- Schools
- Hospital
- Post office
- Police station
- Park
- Temple/Mosque/Church
- Bank

Community Helpers (People who help us):

1. DOCTOR - Treats sick people
2. TEACHER - Teaches us in school
3. POLICEMAN - Keeps us safe
4. POSTMAN - Delivers letters
5. FARMER - Grows food for us
6. SHOPKEEPER - Sells things we need
7. CARPENTER - Makes furniture
8. PLUMBER - Fixes water pipes
9. ELECTRICIAN - Fixes electrical things
10. SWEEPER - Keeps area clean

We Should:
- Respect all community helpers
- Be polite to everyone
- Keep our neighbourhood clean
- Help neighbours when needed
- Use roads carefully
- Throw garbage in dustbin

Good Neighbours:
- Live peacefully together
- Help during emergencies
- Share happy moments
- Respect different cultures''',
        'quiz_questions': [
            {'q': 'Who treats sick people?', 'a': 'Teacher', 'b': 'Doctor', 'c': 'Farmer', 'd': 'Postman', 'correct': 'B'},
            {'q': 'Who delivers letters?', 'a': 'Postman', 'b': 'Doctor', 'c': 'Plumber', 'd': 'Sweeper', 'correct': 'A'},
            {'q': 'Who grows food for us?', 'a': 'Shopkeeper', 'b': 'Carpenter', 'c': 'Farmer', 'd': 'Banker', 'correct': 'C'},
            {'q': 'Where should we throw garbage?', 'a': 'Road', 'b': 'Dustbin', 'c': 'River', 'd': 'Anywhere', 'correct': 'B'},
        ]
    },

    # ==================== GRADE 3 ====================
    {
        'grade': 3, 'subject': 'Mathematics', 'title': 'Multiplication Tables',
        'description': 'Complete multiplication tables 2 to 10',
        'content': '''MULTIPLICATION TABLES

Multiplication is repeated addition.
3 × 4 means 3 + 3 + 3 + 3 = 12 (or 4 + 4 + 4 = 12)

Table of 2:
2×1=2, 2×2=4, 2×3=6, 2×4=8, 2×5=10
2×6=12, 2×7=14, 2×8=16, 2×9=18, 2×10=20

Table of 3:
3×1=3, 3×2=6, 3×3=9, 3×4=12, 3×5=15
3×6=18, 3×7=21, 3×8=24, 3×9=27, 3×10=30

Table of 4:
4×1=4, 4×2=8, 4×3=12, 4×4=16, 4×5=20
4×6=24, 4×7=28, 4×8=32, 4×9=36, 4×10=40

Table of 5:
5×1=5, 5×2=10, 5×3=15, 5×4=20, 5×5=25
5×6=30, 5×7=35, 5×8=40, 5×9=45, 5×10=50

Table of 6:
6×1=6, 6×2=12, 6×3=18, 6×4=24, 6×5=30
6×6=36, 6×7=42, 6×8=48, 6×9=54, 6×10=60

Table of 7:
7×1=7, 7×2=14, 7×3=21, 7×4=28, 7×5=35
7×6=42, 7×7=49, 7×8=56, 7×9=63, 7×10=70

Table of 8:
8×1=8, 8×2=16, 8×3=24, 8×4=32, 8×5=40
8×6=48, 8×7=56, 8×8=64, 8×9=72, 8×10=80

Properties:
- Any number × 0 = 0
- Any number × 1 = same number
- a × b = b × a (order doesn't matter)''',
        'quiz_questions': [
            {'q': '7 × 8 = ?', 'a': '54', 'b': '56', 'c': '58', 'd': '60', 'correct': 'B'},
            {'q': '6 × 6 = ?', 'a': '30', 'b': '36', 'c': '42', 'd': '48', 'correct': 'B'},
            {'q': '9 × 4 = ?', 'a': '32', 'b': '34', 'c': '36', 'd': '38', 'correct': 'C'},
            {'q': '8 × 7 = ?', 'a': '49', 'b': '54', 'c': '56', 'd': '63', 'correct': 'C'},
            {'q': 'Any number multiplied by 0 = ?', 'a': '1', 'b': '0', 'c': 'Same number', 'd': '10', 'correct': 'B'},
            {'q': '5 × 9 = ?', 'a': '40', 'b': '45', 'c': '50', 'd': '55', 'correct': 'B'},
        ]
    },
    {
        'grade': 3, 'subject': 'Science', 'title': 'Living and Non-Living Things',
        'description': 'Differences between living and non-living things',
        'content': '''LIVING AND NON-LIVING THINGS

LIVING THINGS:
Things that are alive. Examples: humans, animals, plants

Characteristics of Living Things:
1. NEED FOOD - Plants, animals, humans
2. BREATHE - Take in oxygen
3. GROW - Become bigger over time
4. REPRODUCE - Have babies/seeds
5. MOVE - Animals move, plants grow toward sunlight
6. RESPOND - React to environment
7. EXCRETE - Remove waste
8. DIE - Eventually

Examples:
- Humans, dogs, cats, birds (animals)
- Trees, flowers, grass (plants)
- Bacteria, fish, insects

NON-LIVING THINGS:
Things that are NOT alive. Don't have life processes.

Characteristics:
- Don't need food
- Don't breathe
- Don't grow naturally
- Don't reproduce
- Don't die

Examples:
- Stone, table, chair
- Pen, book, mobile
- Mountain, building, road
- Water, air (these are needed by living things)

Things to Remember:
- A dead plant or animal is NOT living
- A piece of paper is non-living (even though made from tree)
- A robot is non-living (even though it moves)
- Movement alone doesn't mean alive''',
        'quiz_questions': [
            {'q': 'Which is a living thing?', 'a': 'Stone', 'b': 'Plant', 'c': 'Pen', 'd': 'Table', 'correct': 'B'},
            {'q': 'Living things need ___', 'a': 'Food only', 'b': 'Water only', 'c': 'Air only', 'd': 'All of these', 'correct': 'D'},
            {'q': 'A robot is?', 'a': 'Living', 'b': 'Non-living', 'c': 'Half-living', 'd': 'Both', 'correct': 'B'},
            {'q': 'Which characteristic do living things have?', 'a': 'Growth', 'b': 'Don\'t reproduce', 'c': 'Made of metal', 'd': 'Never move', 'correct': 'A'},
            {'q': 'Which is NOT a living thing?', 'a': 'Cat', 'b': 'Tree', 'c': 'Chair', 'd': 'Bird', 'correct': 'C'},
        ]
    },
    {
        'grade': 3, 'subject': 'English', 'title': 'Action Words (Verbs)',
        'description': 'Learn about verbs - words that show action',
        'content': '''ACTION WORDS (VERBS)

A VERB is a word that shows action or a state of being.

Examples of Action Verbs:
- Walk, Run, Jump, Eat, Drink
- Sleep, Read, Write, Play, Sing
- Dance, Laugh, Cry, Talk, Listen

In Sentences:
- Birds FLY in the sky.
- Cat DRINKS milk.
- We PLAY in the park.
- She SINGS beautifully.

Verbs change with TIME (Tenses):

PRESENT (now):
- I eat
- She runs
- They play

PAST (already happened):
- I ate
- She ran
- They played

FUTURE (will happen):
- I will eat
- She will run
- They will play

Common Past Tenses:
- Go → Went
- Come → Came
- Eat → Ate
- See → Saw
- Take → Took
- Do → Did
- Have → Had

Helping Verbs:
- is, am, are, was, were
- has, have, had
- do, does, did

Practice:
Find verbs: "She reads a book and writes notes."
Verbs: reads, writes''',
        'quiz_questions': [
            {'q': 'Which is a verb?', 'a': 'Happy', 'b': 'Run', 'c': 'Book', 'd': 'Red', 'correct': 'B'},
            {'q': 'Past tense of "go"?', 'a': 'Goed', 'b': 'Went', 'c': 'Gone', 'd': 'Going', 'correct': 'B'},
            {'q': '"She sings" is which tense?', 'a': 'Past', 'b': 'Present', 'c': 'Future', 'd': 'None', 'correct': 'B'},
            {'q': 'Past tense of "eat"?', 'a': 'Eaten', 'b': 'Ate', 'c': 'Eats', 'd': 'Eating', 'correct': 'B'},
            {'q': 'Which is a helping verb?', 'a': 'Run', 'b': 'Book', 'c': 'Is', 'd': 'Happy', 'correct': 'C'},
        ]
    },
    {
        'grade': 3, 'subject': 'Social Studies', 'title': 'Our Country India',
        'description': 'Basic facts about India - geography, symbols, leaders',
        'content': '''OUR COUNTRY INDIA

INDIA - Bharat

Capital: New Delhi
Largest City: Mumbai
National Language: Hindi (official)
Other Languages: 22 official languages

National Symbols:
- National Flag: Tiranga (3 colors)
  Saffron (top): Courage
  White (middle): Peace
  Green (bottom): Growth
  Ashoka Chakra in middle (24 spokes)
- National Anthem: Jana Gana Mana (by Rabindranath Tagore)
- National Song: Vande Mataram (by Bankim Chandra)
- National Animal: TIGER
- National Bird: PEACOCK
- National Flower: LOTUS
- National Fruit: MANGO
- National Tree: BANYAN

Geography:
- Located in South Asia
- 7th largest country
- Surrounded by oceans on 3 sides
- Himalayas in the north
- 28 states and 8 Union Territories

Important Rivers:
- Ganga (most sacred)
- Yamuna
- Brahmaputra
- Krishna
- Godavari

Important Festivals:
- Diwali, Holi, Eid, Christmas
- Republic Day (26 Jan)
- Independence Day (15 Aug)
- Gandhi Jayanti (2 Oct)

National Heroes:
- Mahatma Gandhi (Father of Nation)
- Jawaharlal Nehru (First PM)
- APJ Abdul Kalam (Scientist, President)''',
        'quiz_questions': [
            {'q': 'Capital of India?', 'a': 'Mumbai', 'b': 'New Delhi', 'c': 'Kolkata', 'd': 'Chennai', 'correct': 'B'},
            {'q': 'National animal of India?', 'a': 'Lion', 'b': 'Elephant', 'c': 'Tiger', 'd': 'Cow', 'correct': 'C'},
            {'q': 'Who wrote National Anthem?', 'a': 'Gandhi', 'b': 'Tagore', 'c': 'Nehru', 'd': 'Kalam', 'correct': 'B'},
            {'q': 'How many spokes in Ashoka Chakra?', 'a': '20', 'b': '22', 'c': '24', 'd': '26', 'correct': 'C'},
            {'q': 'Republic Day is on?', 'a': '15 Aug', 'b': '26 Jan', 'c': '2 Oct', 'd': '14 Nov', 'correct': 'B'},
            {'q': 'Most sacred river of India?', 'a': 'Yamuna', 'b': 'Ganga', 'c': 'Krishna', 'd': 'Brahmaputra', 'correct': 'B'},
        ]
    },

    # ==================== GRADE 4 ====================
    {
        'grade': 4, 'subject': 'Mathematics', 'title': 'Division and Fractions',
        'description': 'Understanding division and basic fractions',
        'content': '''DIVISION AND FRACTIONS

DIVISION (÷):
Division means sharing equally.
12 ÷ 3 = 4 (12 divided into 3 equal parts = 4 in each)

Division Facts:
- Dividend ÷ Divisor = Quotient
- Example: 20 ÷ 5 = 4
  - 20 is dividend
  - 5 is divisor
  - 4 is quotient

Rules:
- Any number ÷ 1 = same number (10 ÷ 1 = 10)
- Same number ÷ same number = 1 (8 ÷ 8 = 1)
- 0 ÷ any number = 0 (0 ÷ 5 = 0)
- Cannot divide by 0

Long Division:
84 ÷ 4 = ?
   21
 4)84
   8
   --
    4
    4
    --
    0

So 84 ÷ 4 = 21

FRACTIONS:
A fraction shows part of a whole.

Example: 1/2 (one half)
- 1 is numerator (top)
- 2 is denominator (bottom)
- Means 1 part out of 2 equal parts

Common Fractions:
- 1/2 = One half = 0.5
- 1/3 = One third
- 1/4 = One quarter = 0.25
- 3/4 = Three quarters = 0.75
- 1/5 = One fifth

Comparing Fractions:
- 1/2 > 1/4 (half is more than quarter)
- 1/3 > 1/5

Adding Fractions (same denominator):
1/4 + 2/4 = 3/4

A whole = 4/4 = 2/2 = 1''',
        'quiz_questions': [
            {'q': '36 ÷ 6 = ?', 'a': '4', 'b': '5', 'c': '6', 'd': '7', 'correct': 'C'},
            {'q': '1/2 of 20 = ?', 'a': '5', 'b': '10', 'c': '15', 'd': '20', 'correct': 'B'},
            {'q': 'In 3/4, what is numerator?', 'a': '3', 'b': '4', 'c': '7', 'd': '1', 'correct': 'A'},
            {'q': '0 ÷ 7 = ?', 'a': '0', 'b': '7', 'c': '1', 'd': 'Cannot be done', 'correct': 'A'},
            {'q': '1/4 + 2/4 = ?', 'a': '3/4', 'b': '3/8', 'c': '1/4', 'd': '2/4', 'correct': 'A'},
            {'q': '100 ÷ 10 = ?', 'a': '5', 'b': '10', 'c': '15', 'd': '20', 'correct': 'B'},
        ]
    },
    {
        'grade': 4, 'subject': 'Science', 'title': 'Food and Nutrition',
        'description': 'Healthy eating, food groups and balanced diet',
        'content': '''FOOD AND NUTRITION

We need food for ENERGY, GROWTH, and HEALTH.

NUTRIENTS in Food:

1. CARBOHYDRATES - Give energy
   Sources: Rice, wheat, bread, sugar, potato

2. PROTEINS - Build body, repair tissues
   Sources: Milk, eggs, fish, pulses (dal), nuts

3. FATS - Store energy, keep warm
   Sources: Butter, oil, ghee, cheese

4. VITAMINS - Keep body healthy
   - Vitamin A: Eyes (carrots, papaya)
   - Vitamin C: Immunity (oranges, lemon)
   - Vitamin D: Bones (sunlight, milk)
   - Vitamin K: Blood clotting

5. MINERALS - For bones, blood
   - Calcium: Strong bones (milk)
   - Iron: Blood (green vegetables)
   - Iodine: Brain (salt)

6. WATER - Most important
   - 8 glasses daily
   - Removes waste

7. FIBER - Helps digestion
   Sources: Fruits, vegetables, whole grains

BALANCED DIET:
A meal with all nutrients in right amounts.

Food Groups:
- Body Building (proteins)
- Energy Giving (carbs, fats)
- Protective (vitamins, minerals)

Deficiency Diseases:
- Lack of Vitamin A = Night blindness
- Lack of Vitamin C = Scurvy
- Lack of Vitamin D = Rickets
- Lack of Iron = Anemia
- Lack of Iodine = Goitre

Tips for Healthy Eating:
1. Eat fruits daily
2. Eat green vegetables
3. Drink plenty of water
4. Avoid too much junk food
5. Eat at regular times
6. Wash hands before eating''',
        'quiz_questions': [
            {'q': 'Carbohydrates give us?', 'a': 'Growth', 'b': 'Energy', 'c': 'Beauty', 'd': 'Sleep', 'correct': 'B'},
            {'q': 'Source of Vitamin C?', 'a': 'Rice', 'b': 'Bread', 'c': 'Oranges', 'd': 'Oil', 'correct': 'C'},
            {'q': 'Calcium is needed for?', 'a': 'Eyes', 'b': 'Bones', 'c': 'Hair', 'd': 'Skin', 'correct': 'B'},
            {'q': 'Lack of Vitamin A causes?', 'a': 'Anemia', 'b': 'Goitre', 'c': 'Night blindness', 'd': 'Cold', 'correct': 'C'},
            {'q': 'Proteins are found in?', 'a': 'Sugar', 'b': 'Oil', 'c': 'Milk', 'd': 'Salt', 'correct': 'C'},
            {'q': 'How many glasses of water daily?', 'a': '2', 'b': '4', 'c': '6', 'd': '8', 'correct': 'D'},
        ]
    },
    {
        'grade': 4, 'subject': 'English', 'title': 'Adjectives and Descriptive Words',
        'description': 'Learn adjectives - words that describe nouns',
        'content': '''ADJECTIVES AND DESCRIPTIVE WORDS

An ADJECTIVE is a word that describes a noun (person, place, thing).

Examples:
- A BIG house
- A RED car
- A HAPPY child
- A TALL tree
- A BEAUTIFUL flower

Types of Adjectives:

1. SIZE: big, small, tall, short, tiny, huge
2. COLOR: red, blue, green, yellow, black, white
3. SHAPE: round, square, triangular, oval
4. TASTE: sweet, sour, bitter, salty, spicy
5. TOUCH: soft, hard, smooth, rough, hot, cold
6. FEELING: happy, sad, angry, excited, scared
7. NUMBER: one, two, many, few, all, some
8. QUALITY: good, bad, beautiful, ugly, brave

Comparing with Adjectives:

POSITIVE: big, small, fast
COMPARATIVE (compares 2): bigger, smaller, faster
SUPERLATIVE (compares 3+): biggest, smallest, fastest

Examples:
- Ravi is TALL.
- Ravi is TALLER than Sita.
- Ravi is the TALLEST in the class.

Special Comparisons:
- Good → Better → Best
- Bad → Worse → Worst
- Many → More → Most
- Little → Less → Least

Rules:
- Short adjectives: add -er, -est
- Long adjectives: use more, most
  - Beautiful → More beautiful → Most beautiful

Practice:
Find adjectives: "The cute brown dog ran fast on the green grass."
Adjectives: cute, brown, fast, green''',
        'quiz_questions': [
            {'q': 'Which is an adjective?', 'a': 'Run', 'b': 'Happy', 'c': 'Book', 'd': 'Quickly', 'correct': 'B'},
            {'q': 'Comparative of "tall"?', 'a': 'Taller', 'b': 'Tallest', 'c': 'More tall', 'd': 'Tall', 'correct': 'A'},
            {'q': 'Superlative of "good"?', 'a': 'Gooder', 'b': 'Better', 'c': 'Best', 'd': 'Goodest', 'correct': 'C'},
            {'q': 'In "red ball", what is adjective?', 'a': 'red', 'b': 'ball', 'c': 'both', 'd': 'none', 'correct': 'A'},
            {'q': 'Comparative of "beautiful"?', 'a': 'Beautifuler', 'b': 'More beautiful', 'c': 'Beautifulest', 'd': 'Beautify', 'correct': 'B'},
        ]
    },
    {
        'grade': 4, 'subject': 'Social Studies', 'title': 'States of India',
        'description': 'Indian states, capitals, and their specialties',
        'content': '''STATES OF INDIA

India has 28 STATES and 8 UNION TERRITORIES.

Major States and Capitals:

NORTH INDIA:
- Jammu & Kashmir: Srinagar/Jammu
- Punjab: Chandigarh
- Haryana: Chandigarh
- Uttar Pradesh: Lucknow
- Uttarakhand: Dehradun
- Rajasthan: Jaipur
- Himachal Pradesh: Shimla

EAST INDIA:
- Bihar: Patna
- West Bengal: Kolkata
- Jharkhand: Ranchi
- Odisha: Bhubaneswar

WEST INDIA:
- Maharashtra: Mumbai
- Gujarat: Gandhinagar
- Goa: Panaji

SOUTH INDIA:
- Karnataka: Bangalore
- Kerala: Thiruvananthapuram
- Tamil Nadu: Chennai
- Andhra Pradesh: Amaravati
- Telangana: Hyderabad

CENTRAL INDIA:
- Madhya Pradesh: Bhopal
- Chhattisgarh: Raipur

NORTH-EAST:
- Assam: Dispur
- Arunachal Pradesh: Itanagar
- Manipur: Imphal
- Meghalaya: Shillong
- Mizoram: Aizawl
- Nagaland: Kohima
- Tripura: Agartala
- Sikkim: Gangtok

UNION TERRITORIES:
- Delhi (Capital)
- Chandigarh
- Puducherry
- Andaman & Nicobar Islands
- Lakshadweep
- Daman & Diu
- Ladakh
- Jammu & Kashmir

Each state has:
- Its own language
- Cultural traditions
- Special food
- Famous places
- Local festivals''',
        'quiz_questions': [
            {'q': 'Capital of Maharashtra?', 'a': 'Pune', 'b': 'Mumbai', 'c': 'Nagpur', 'd': 'Nashik', 'correct': 'B'},
            {'q': 'Capital of Karnataka?', 'a': 'Mysore', 'b': 'Bangalore', 'c': 'Hubli', 'd': 'Mangalore', 'correct': 'B'},
            {'q': 'How many states in India?', 'a': '26', 'b': '27', 'c': '28', 'd': '29', 'correct': 'C'},
            {'q': 'Capital of Tamil Nadu?', 'a': 'Chennai', 'b': 'Coimbatore', 'c': 'Madurai', 'd': 'Salem', 'correct': 'A'},
            {'q': 'How many Union Territories?', 'a': '6', 'b': '7', 'c': '8', 'd': '9', 'correct': 'C'},
            {'q': 'Capital of West Bengal?', 'a': 'Patna', 'b': 'Kolkata', 'c': 'Ranchi', 'd': 'Bhubaneswar', 'correct': 'B'},
        ]
    },

    # ==================== GRADE 5 ====================
    {
        'grade': 5, 'subject': 'Mathematics', 'title': 'Decimals and Percentages',
        'description': 'Working with decimals and converting to percentages',
        'content': '''DECIMALS AND PERCENTAGES

DECIMALS:
Numbers with a decimal point separating whole and fractional parts.

Example: 25.75
- 25 is whole part
- 75 is decimal part

Place Values:
12.345
- 1 is Tens
- 2 is Ones
- 3 is Tenths (1/10)
- 4 is Hundredths (1/100)
- 5 is Thousandths (1/1000)

Common Decimals:
- 0.5 = 1/2
- 0.25 = 1/4
- 0.75 = 3/4
- 0.1 = 1/10
- 0.01 = 1/100

Adding Decimals:
  12.50
+  3.75
-------
  16.25

(Line up decimal points!)

Subtracting Decimals:
  20.00
-  7.25
-------
  12.75

PERCENTAGES (%):
Per cent means "out of 100"

50% = 50/100 = 1/2 = 0.5
25% = 25/100 = 1/4 = 0.25
100% = whole

Converting:
- Fraction to %: Multiply by 100
  1/4 = 25%
- Decimal to %: Multiply by 100
  0.5 = 50%
- % to decimal: Divide by 100
  75% = 0.75

Finding %:
- 50% of 200 = 100
- 25% of 80 = 20
- 10% of 50 = 5

Real-life uses:
- Discount in shops: 20% off
- Marks: 85% in exam
- Battery: 50% charged''',
        'quiz_questions': [
            {'q': '0.75 equals which fraction?', 'a': '1/2', 'b': '1/4', 'c': '3/4', 'd': '1/3', 'correct': 'C'},
            {'q': '50% of 200 = ?', 'a': '50', 'b': '100', 'c': '150', 'd': '200', 'correct': 'B'},
            {'q': '2.5 + 1.5 = ?', 'a': '3', 'b': '3.5', 'c': '4', 'd': '4.5', 'correct': 'C'},
            {'q': '25% as decimal?', 'a': '0.025', 'b': '0.25', 'c': '2.5', 'd': '25', 'correct': 'B'},
            {'q': '10% of 50 = ?', 'a': '3', 'b': '5', 'c': '10', 'd': '15', 'correct': 'B'},
            {'q': '0.1 = ?', 'a': '1/10', 'b': '1/100', 'c': '1', 'd': '10', 'correct': 'A'},
        ]
    },
    {
        'grade': 5, 'subject': 'Science', 'title': 'Human Body Systems',
        'description': 'Major organ systems and their functions',
        'content': '''HUMAN BODY SYSTEMS

The human body has many systems working together.

1. SKELETAL SYSTEM (Bones)
- 206 bones in adult body
- Gives shape and support
- Protects internal organs
- Skull protects brain
- Ribs protect heart and lungs
- Spine supports body

2. MUSCULAR SYSTEM (Muscles)
- More than 600 muscles
- Help us move
- Voluntary muscles (we control)
- Involuntary muscles (work automatically)

3. CIRCULATORY SYSTEM (Heart, Blood)
- Heart pumps blood
- Heart beats 72 times per minute
- Blood carries oxygen and food
- Blood vessels: arteries, veins, capillaries

4. RESPIRATORY SYSTEM (Lungs)
- We breathe in oxygen
- We breathe out carbon dioxide
- 2 lungs in chest
- Air passes through nose → trachea → lungs

5. DIGESTIVE SYSTEM (Stomach, Intestines)
- Mouth chews food
- Stomach digests food
- Small intestine absorbs nutrients
- Large intestine removes waste
- Liver helps digestion

6. NERVOUS SYSTEM (Brain, Spinal Cord)
- Brain is the control center
- Spinal cord connects brain to body
- Nerves carry messages
- Controls all body functions

7. EXCRETORY SYSTEM (Kidneys)
- 2 kidneys filter blood
- Remove waste as urine
- Maintain water balance

5 Sense Organs:
- Eyes (vision)
- Ears (hearing)
- Nose (smell)
- Tongue (taste)
- Skin (touch)

Keeping Healthy:
- Eat balanced diet
- Exercise daily
- Get enough sleep
- Stay hygienic
- Drink water''',
        'quiz_questions': [
            {'q': 'How many bones in adult human?', 'a': '156', 'b': '206', 'c': '256', 'd': '300', 'correct': 'B'},
            {'q': 'Which organ pumps blood?', 'a': 'Lungs', 'b': 'Brain', 'c': 'Heart', 'd': 'Liver', 'correct': 'C'},
            {'q': 'We breathe out?', 'a': 'Oxygen', 'b': 'Carbon dioxide', 'c': 'Nitrogen', 'd': 'Hydrogen', 'correct': 'B'},
            {'q': 'Brain is part of which system?', 'a': 'Digestive', 'b': 'Nervous', 'c': 'Respiratory', 'd': 'Circulatory', 'correct': 'B'},
            {'q': 'Number of lungs?', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'correct': 'B'},
            {'q': 'Heart beats how many times per minute?', 'a': '52', 'b': '62', 'c': '72', 'd': '92', 'correct': 'C'},
        ]
    },
    {
        'grade': 5, 'subject': 'English', 'title': 'Tenses - Past, Present, Future',
        'description': 'Understanding the three tenses in English',
        'content': '''TENSES IN ENGLISH

Tense tells us WHEN something happens.

THREE MAIN TENSES:

1. PRESENT TENSE (Now)
Things happening NOW or regularly.

Simple Present:
- I play cricket.
- She reads books.
- They go to school.
- He works hard.

Present Continuous (-ing):
- I am playing cricket.
- She is reading a book.
- They are going to school.

Present Perfect (have/has + past):
- I have played cricket.
- She has read the book.

2. PAST TENSE (Already happened)
Things that happened BEFORE now.

Simple Past:
- I played cricket yesterday.
- She read the book last week.
- They went to school.

Past Continuous:
- I was playing.
- She was reading.
- They were going.

Common Past Forms:
- Go → Went
- Come → Came
- Eat → Ate
- See → Saw
- Take → Took
- Make → Made
- Have → Had
- Do → Did
- Run → Ran
- Sit → Sat

3. FUTURE TENSE (Will happen)
Things that will happen LATER.

Simple Future:
- I will play cricket tomorrow.
- She will read the book.
- They will go to school.

Helping Verbs:
- am, is, are (present)
- was, were (past)
- will, shall (future)
- have, has, had (perfect)

Practice:
- "I eat" (present) → "I ate" (past) → "I will eat" (future)
- "She sings" → "She sang" → "She will sing"''',
        'quiz_questions': [
            {'q': '"She is singing" is which tense?', 'a': 'Past', 'b': 'Present continuous', 'c': 'Future', 'd': 'Past perfect', 'correct': 'B'},
            {'q': 'Past tense of "see"?', 'a': 'Seed', 'b': 'Saw', 'c': 'Seen', 'd': 'Seeing', 'correct': 'B'},
            {'q': '"They will play" is which tense?', 'a': 'Present', 'b': 'Past', 'c': 'Future', 'd': 'Perfect', 'correct': 'C'},
            {'q': 'Past of "come"?', 'a': 'Comed', 'b': 'Came', 'c': 'Coming', 'd': 'Come', 'correct': 'B'},
            {'q': '"I have eaten" is which tense?', 'a': 'Simple past', 'b': 'Present perfect', 'c': 'Future', 'd': 'Present continuous', 'correct': 'B'},
            {'q': 'Helping verb for future?', 'a': 'is', 'b': 'has', 'c': 'will', 'd': 'was', 'correct': 'C'},
        ]
    },
    {
        'grade': 5, 'subject': 'Social Studies', 'title': 'Indian Freedom Movement',
        'description': 'How India achieved independence from British rule',
        'content': '''INDIAN FREEDOM MOVEMENT

The British ruled India for nearly 200 years (1757-1947).

Why Indians Wanted Freedom:
- Heavy taxes on Indians
- Exploitation of resources
- Unfair laws
- Racial discrimination
- Poverty and hunger

KEY EVENTS:

1857 - First War of Independence
- First major revolt against British
- Led by Mangal Pandey, Rani Lakshmibai
- British called it "Sepoy Mutiny"

1885 - Indian National Congress formed
- Political party for independence

1919 - Jallianwala Bagh Massacre
- General Dyer ordered firing
- Hundreds killed peacefully protesting

1920 - Non-Cooperation Movement
- Led by Gandhi
- Boycott of British goods

1930 - Salt March (Dandi March)
- Gandhi walked 240 miles to Dandi
- Made salt from sea water
- Broke British salt law

1942 - Quit India Movement
- Demand: British leave India
- "Do or Die" slogan by Gandhi

1947 - INDEPENDENCE
- 15 August 1947
- India became free
- But also Partition (India + Pakistan)

GREAT LEADERS:

MAHATMA GANDHI (Bapu)
- Father of the Nation
- Non-violence (Ahimsa)
- Satyagraha (truth force)
- Born: 2 October 1869
- Killed: 30 January 1948

JAWAHARLAL NEHRU
- First Prime Minister
- "Tryst with Destiny" speech
- Children call him "Chacha Nehru"
- Birthday (14 Nov) is Children's Day

SARDAR PATEL
- Iron Man of India
- United 565 princely states
- Statue of Unity built for him

BHAGAT SINGH (1907-1931)
- Young revolutionary
- Hanged at age 23
- Inspired youth

SUBHASH CHANDRA BOSE
- "Netaji"
- Formed Indian National Army
- "Give me blood, I'll give you freedom"

DR. B. R. AMBEDKAR
- Father of Constitution
- Fought for equality

Important Dates:
- 15 Aug: Independence Day
- 26 Jan: Republic Day
- 2 Oct: Gandhi Jayanti
- 23 Mar: Bhagat Singh Martyrdom
- 14 Nov: Children's Day''',
        'quiz_questions': [
            {'q': 'India got independence in?', 'a': '1945', 'b': '1947', 'c': '1949', 'd': '1950', 'correct': 'B'},
            {'q': 'Father of the Nation?', 'a': 'Nehru', 'b': 'Gandhi', 'c': 'Patel', 'd': 'Bose', 'correct': 'B'},
            {'q': 'Salt March was in?', 'a': '1920', 'b': '1925', 'c': '1930', 'd': '1942', 'correct': 'C'},
            {'q': 'Who said "Give me blood"?', 'a': 'Gandhi', 'b': 'Nehru', 'c': 'Bose', 'd': 'Bhagat Singh', 'correct': 'C'},
            {'q': 'Father of Constitution?', 'a': 'Nehru', 'b': 'Gandhi', 'c': 'Ambedkar', 'd': 'Patel', 'correct': 'C'},
            {'q': 'Statue of Unity is of?', 'a': 'Gandhi', 'b': 'Nehru', 'c': 'Patel', 'd': 'Bose', 'correct': 'C'},
            {'q': 'First Prime Minister of India?', 'a': 'Gandhi', 'b': 'Nehru', 'c': 'Patel', 'd': 'Shastri', 'correct': 'B'},
        ]
    },

    # ==================== GRADE 6 ====================
    {
        'grade': 6, 'subject': 'Mathematics', 'title': 'Integers and Number System',
        'description': 'Understanding positive and negative numbers',
        'content': '''INTEGERS AND NUMBER SYSTEM

INTEGERS include:
- Positive numbers: 1, 2, 3, ...
- Zero: 0
- Negative numbers: -1, -2, -3, ...

Number Line:
... -4 -3 -2 -1 0 +1 +2 +3 +4 ...

Negative numbers used for:
- Temperature below zero: -5°C
- Below sea level: -100 m
- Debt or loss: -₹500

OPERATIONS ON INTEGERS:

Addition:
(+3) + (+5) = +8 (both positive)
(-3) + (-5) = -8 (both negative)
(+5) + (-3) = +2 (subtract, take sign of larger)
(-5) + (+3) = -2

Subtraction:
Change sign of second number, then add
(+5) - (+3) = (+5) + (-3) = +2
(+5) - (-3) = (+5) + (+3) = +8
(-5) - (+3) = (-5) + (-3) = -8

Multiplication:
- (+) × (+) = (+)
- (-) × (-) = (+)
- (+) × (-) = (-)
- (-) × (+) = (-)
Examples:
3 × 4 = 12
(-3) × (-4) = 12
3 × (-4) = -12

NUMBER PROPERTIES:

LCM (Least Common Multiple):
Smallest number divisible by both
LCM of 4 and 6:
- Multiples of 4: 4, 8, 12, 16, 20...
- Multiples of 6: 6, 12, 18, 24...
- LCM = 12

HCF (Highest Common Factor):
Biggest number that divides both
HCF of 12 and 18:
- Factors of 12: 1, 2, 3, 4, 6, 12
- Factors of 18: 1, 2, 3, 6, 9, 18
- HCF = 6

Prime Numbers:
Numbers with only 2 factors (1 and itself)
2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Composite Numbers:
Have more than 2 factors
4, 6, 8, 9, 10, 12, 14, 15

Note: 1 is neither prime nor composite''',
        'quiz_questions': [
            {'q': '(-5) + (-3) = ?', 'a': '-8', 'b': '-2', 'c': '+2', 'd': '+8', 'correct': 'A'},
            {'q': '(-4) × (-3) = ?', 'a': '-12', 'b': '+12', 'c': '-7', 'd': '+7', 'correct': 'B'},
            {'q': 'LCM of 4 and 6?', 'a': '8', 'b': '12', 'c': '16', 'd': '24', 'correct': 'B'},
            {'q': 'HCF of 12 and 18?', 'a': '4', 'b': '6', 'c': '8', 'd': '12', 'correct': 'B'},
            {'q': 'Smallest prime number?', 'a': '0', 'b': '1', 'c': '2', 'd': '3', 'correct': 'C'},
            {'q': 'Is 1 prime or composite?', 'a': 'Prime', 'b': 'Composite', 'c': 'Neither', 'd': 'Both', 'correct': 'C'},
        ]
    },
    {
        'grade': 6, 'subject': 'Science', 'title': 'Components of Food',
        'description': 'Nutrients in food and their importance',
        'content': '''COMPONENTS OF FOOD

Our food contains different NUTRIENTS:

1. CARBOHYDRATES
- Main source of energy
- Sources: Rice, wheat, bread, sugar, potatoes
- Types: Starch, sugar

2. PROTEINS
- Body-building nutrients
- Help in growth and repair
- Sources:
  Plant: Pulses (dal), beans, soybean
  Animal: Eggs, fish, meat, milk

3. FATS
- Provide energy
- Help in vitamin absorption
- Keep body warm
- Sources:
  Plant: Oils (mustard, sunflower)
  Animal: Butter, ghee, cream

4. VITAMINS
Small amounts needed for health.

Vitamin A: Eyes, skin
Sources: Carrots, papaya, milk
Deficiency: Night blindness

Vitamin B: Energy, nerves
Sources: Yeast, eggs, liver

Vitamin C: Immunity, gums
Sources: Oranges, lemon, amla
Deficiency: Scurvy

Vitamin D: Strong bones
Sources: Sunlight, milk, eggs
Deficiency: Rickets

Vitamin K: Blood clotting
Sources: Green vegetables

5. MINERALS

Calcium: Bones, teeth
Sources: Milk, cheese

Iron: Blood (hemoglobin)
Sources: Spinach, jaggery
Deficiency: Anemia

Iodine: Brain, thyroid
Sources: Iodised salt, seafood
Deficiency: Goitre

Phosphorus: Bones

6. DIETARY FIBRE
- Cannot be digested
- Helps clear waste
- Sources: Whole grains, fruits, vegetables

7. WATER
- Most important
- Maintains body temperature
- Removes waste
- Drink 8 glasses daily

BALANCED DIET:
Food with right amounts of ALL nutrients.

Tests for Nutrients:
- Starch: Iodine turns blue-black
- Protein: Copper sulphate + caustic soda = violet
- Fat: Oil stain on paper

Deficiency Diseases:
- Protein: Kwashiorkor, Marasmus
- Vitamin A: Night blindness
- Vitamin C: Scurvy
- Vitamin D: Rickets
- Iron: Anemia
- Iodine: Goitre''',
        'quiz_questions': [
            {'q': 'Main source of energy?', 'a': 'Protein', 'b': 'Carbohydrates', 'c': 'Fat', 'd': 'Vitamin', 'correct': 'B'},
            {'q': 'Vitamin C is found in?', 'a': 'Rice', 'b': 'Oranges', 'c': 'Oil', 'd': 'Sugar', 'correct': 'B'},
            {'q': 'Calcium is needed for?', 'a': 'Eyes', 'b': 'Skin', 'c': 'Bones', 'd': 'Hair', 'correct': 'C'},
            {'q': 'Lack of iron causes?', 'a': 'Scurvy', 'b': 'Anemia', 'c': 'Goitre', 'd': 'Rickets', 'correct': 'B'},
            {'q': 'Test for starch uses?', 'a': 'Vinegar', 'b': 'Iodine', 'c': 'Salt', 'd': 'Lemon', 'correct': 'B'},
            {'q': 'Source of iodine?', 'a': 'Sugar', 'b': 'Iodised salt', 'c': 'Oil', 'd': 'Bread', 'correct': 'B'},
        ]
    },
    {
        'grade': 6, 'subject': 'Social Studies', 'title': 'Earth and Solar System',
        'description': 'Our planet, the Sun and other planets',
        'content': '''EARTH AND SOLAR SYSTEM

THE UNIVERSE:
Contains stars, planets, galaxies, and everything.

SOLAR SYSTEM:
The Sun and all objects revolving around it.

THE SUN:
- A STAR (not planet)
- Center of solar system
- Source of light and heat
- 1.5 crore km from Earth
- 109 times bigger than Earth

8 PLANETS (in order from Sun):

1. MERCURY - Closest to Sun, smallest
2. VENUS - Hottest, brightest (Morning Star)
3. EARTH - Our home (only with life)
4. MARS - Red Planet
5. JUPITER - Largest planet
6. SATURN - Has beautiful rings
7. URANUS - Sideways rotation
8. NEPTUNE - Farthest, blue

(Memory: My Very Educated Mother Just Served Us Noodles)

THE EARTH:
- 3rd planet from Sun
- Only planet with life
- Has water, air, suitable temperature
- Has 1 natural satellite: MOON

Earth's Movements:
1. ROTATION - On its axis
   - Takes 24 hours (1 day)
   - Causes day and night

2. REVOLUTION - Around the Sun
   - Takes 365¼ days (1 year)
   - Causes seasons

Tilt: Earth tilts 23.5°
- Causes seasons

THE MOON:
- Earth's natural satellite
- Reflects sunlight (no own light)
- Takes about 27 days to revolve around Earth
- Phases: New, Crescent, Half, Full

ASTEROIDS:
Small rocky objects between Mars and Jupiter

COMETS:
Icy objects with long tails

STARS:
- Self-luminous
- Made of hot gases
- Sun is our nearest star
- Other stars look small (very far)

CONSTELLATIONS:
Groups of stars forming patterns
- Ursa Major (Saptarishi)
- Orion (Hunter)

THE MILKY WAY:
Our galaxy with billions of stars

Space Exploration:
- First man in space: Yuri Gagarin (1961)
- First moon landing: Neil Armstrong (1969)
- First Indian in space: Rakesh Sharma (1984)
- ISRO: Indian Space Agency
- Chandrayaan: India's moon mission''',
        'quiz_questions': [
            {'q': 'How many planets in solar system?', 'a': '7', 'b': '8', 'c': '9', 'd': '10', 'correct': 'B'},
            {'q': 'Closest planet to Sun?', 'a': 'Venus', 'b': 'Earth', 'c': 'Mercury', 'd': 'Mars', 'correct': 'C'},
            {'q': 'Largest planet?', 'a': 'Saturn', 'b': 'Jupiter', 'c': 'Earth', 'd': 'Uranus', 'correct': 'B'},
            {'q': 'Earth\'s natural satellite?', 'a': 'Sun', 'b': 'Moon', 'c': 'Mars', 'd': 'Venus', 'correct': 'B'},
            {'q': 'How long Earth takes to rotate once?', 'a': '12 hours', 'b': '24 hours', 'c': '30 days', 'd': '365 days', 'correct': 'B'},
            {'q': 'First Indian in space?', 'a': 'Kalpana Chawla', 'b': 'Rakesh Sharma', 'c': 'Sunita Williams', 'd': 'APJ Kalam', 'correct': 'B'},
        ]
    },

    # ==================== GRADE 7 ====================
    {
        'grade': 7, 'subject': 'Mathematics', 'title': 'Algebraic Expressions',
        'description': 'Introduction to algebra with variables and equations',
        'content': '''ALGEBRAIC EXPRESSIONS

ALGEBRA uses letters (variables) to represent numbers.

VARIABLES:
Letters like x, y, z, a, b that represent unknown values.

CONSTANTS:
Fixed numbers like 2, 5, -3, π

TERMS:
Parts of expression separated by + or -
In 3x + 2y - 5: terms are 3x, 2y, -5

COEFFICIENT:
Number in front of variable
In 5x: coefficient is 5

ALGEBRAIC EXPRESSIONS:
Combination of variables and numbers with operations.
Examples: 2x + 5, 3y - 7, x² + 4x + 4

TYPES:
- Monomial: 1 term (3x)
- Binomial: 2 terms (3x + 5)
- Trinomial: 3 terms (x² + 3x + 5)
- Polynomial: many terms

LIKE TERMS:
Same variable with same power
- 3x and 5x are like terms
- 3x and 5y are NOT like terms
- 3x² and 5x are NOT like terms

ADDING LIKE TERMS:
3x + 5x = 8x
2y + 7y - 3y = 6y

MULTIPLYING:
x × x = x²
2x × 3x = 6x²
(2x)(3y) = 6xy

EVALUATING EXPRESSIONS:
If x = 3, find 2x + 5
= 2(3) + 5
= 6 + 5
= 11

EQUATIONS:
Expression with = sign
Example: 2x + 3 = 11

SOLVING EQUATIONS:
Find value of variable that makes equation true.

Example: x + 5 = 12
Step 1: Subtract 5 from both sides
x + 5 - 5 = 12 - 5
x = 7
Check: 7 + 5 = 12 ✓

Example: 3x = 21
Step 1: Divide both sides by 3
x = 7
Check: 3(7) = 21 ✓

Example: 2x + 4 = 10
Step 1: Subtract 4: 2x = 6
Step 2: Divide by 2: x = 3
Check: 2(3) + 4 = 10 ✓

GOLDEN RULE:
Whatever you do to one side, do to the other side!''',
        'quiz_questions': [
            {'q': 'If x = 4, then 2x + 3 = ?', 'a': '7', 'b': '9', 'c': '11', 'd': '13', 'correct': 'C'},
            {'q': '3a + 5a = ?', 'a': '8a', 'b': '8a²', 'c': '15a', 'd': '15a²', 'correct': 'A'},
            {'q': 'Solve: x + 7 = 15', 'a': '7', 'b': '8', 'c': '15', 'd': '22', 'correct': 'B'},
            {'q': 'Coefficient in 5y?', 'a': '5', 'b': 'y', 'c': '5y', 'd': '1', 'correct': 'A'},
            {'q': '2x × 3x = ?', 'a': '5x', 'b': '6x', 'c': '5x²', 'd': '6x²', 'correct': 'D'},
            {'q': 'Solve: 3x = 21', 'a': 'x = 3', 'b': 'x = 7', 'c': 'x = 9', 'd': 'x = 21', 'correct': 'B'},
        ]
    },
    {
        'grade': 7, 'subject': 'Science', 'title': 'Acids, Bases and Salts',
        'description': 'Chemistry of acids, bases, and the pH scale',
        'content': '''ACIDS, BASES AND SALTS

ACIDS:
Substances with sour taste.

Properties:
- Taste sour
- Turn blue litmus to RED
- pH less than 7
- Conduct electricity in water

Common Acids:
Natural:
- Lemon juice (Citric acid)
- Vinegar (Acetic acid)
- Curd (Lactic acid)
- Tomato (Oxalic acid)
- Tamarind (Tartaric acid)

Mineral/Strong Acids:
- Hydrochloric acid (HCl) - in stomach
- Sulphuric acid (H2SO4) - in car batteries
- Nitric acid (HNO3)

BASES:
Substances that feel bitter and soapy.

Properties:
- Taste bitter
- Feel slippery/soapy
- Turn red litmus to BLUE
- pH greater than 7

Common Bases:
- Soap, detergent
- Baking soda (Sodium bicarbonate)
- Lime water (Calcium hydroxide)
- Caustic soda (Sodium hydroxide)
- Toothpaste
- Milk of magnesia

INDICATORS:
Substances that change color in acids/bases.

Natural Indicators:
- Litmus paper (red ↔ blue)
- Turmeric (yellow → red in base)
- China rose (red → green in base)
- Cabbage juice

Universal Indicator: Shows exact pH

pH SCALE (0 to 14):
- 0-6: Acid (lower = stronger acid)
- 7: Neutral (water)
- 8-14: Base (higher = stronger base)

Examples:
- HCl: pH 1 (strong acid)
- Lemon: pH 2
- Vinegar: pH 3
- Tomato: pH 4
- Water: pH 7
- Baking soda: pH 9
- Soap: pH 10
- Caustic soda: pH 14

NEUTRALIZATION:
Acid + Base → Salt + Water

Example: HCl + NaOH → NaCl + H2O
(Hydrochloric acid + Sodium hydroxide → Salt + Water)

SALTS:
Formed by neutralization.

Common Salts:
- Common salt (NaCl) - table salt
- Baking soda (NaHCO3)
- Washing soda (Na2CO3)
- Plaster of Paris

APPLICATIONS:

Daily Life:
- Antacid for acidity (uses base)
- Soap to clean (uses base)
- Vinegar in cooking (acid)

Soil:
- Acidic soil: Add lime (base)
- Basic soil: Add gypsum (acid)

Factory Waste:
- Often acidic, must be neutralized before release

Stings/Bites:
- Bee sting (acid): Apply baking soda
- Wasp sting (base): Apply vinegar''',
        'quiz_questions': [
            {'q': 'Lemon juice is?', 'a': 'Acid', 'b': 'Base', 'c': 'Salt', 'd': 'Neutral', 'correct': 'A'},
            {'q': 'pH of pure water?', 'a': '0', 'b': '5', 'c': '7', 'd': '14', 'correct': 'C'},
            {'q': 'Acids turn blue litmus to?', 'a': 'Green', 'b': 'Red', 'c': 'Yellow', 'd': 'White', 'correct': 'B'},
            {'q': 'Common salt is?', 'a': 'HCl', 'b': 'NaOH', 'c': 'NaCl', 'd': 'H2O', 'correct': 'C'},
            {'q': 'Acid + Base = ?', 'a': 'Only water', 'b': 'Only salt', 'c': 'Salt + Water', 'd': 'Acid', 'correct': 'C'},
            {'q': 'pH > 7 means?', 'a': 'Acid', 'b': 'Base', 'c': 'Neutral', 'd': 'Salt', 'correct': 'B'},
            {'q': 'Stomach acid is?', 'a': 'HCl', 'b': 'H2SO4', 'c': 'HNO3', 'd': 'NaOH', 'correct': 'A'},
        ]
    },
    {
        'grade': 7, 'subject': 'English', 'title': 'Active and Passive Voice',
        'description': 'Converting sentences between active and passive voice',
        'content': '''ACTIVE AND PASSIVE VOICE

ACTIVE VOICE:
Subject does the action.
Structure: Subject + Verb + Object

Examples:
- Ravi eats an apple. (Ravi does the action)
- She writes a letter.
- The dog chases the cat.

PASSIVE VOICE:
Subject receives the action.
Structure: Object + form of "be" + past participle + by + Subject

Examples:
- An apple is eaten by Ravi.
- A letter is written by her.
- The cat is chased by the dog.

CHANGING ACTIVE TO PASSIVE:

Step 1: Object becomes subject
Step 2: Use correct "be" form (is/am/are/was/were)
Step 3: Use past participle (3rd form) of verb
Step 4: Subject becomes "by + subject"

PRESENT TENSE:

Active: She drinks milk.
Passive: Milk is drunk by her.

Active: They play cricket.
Passive: Cricket is played by them.

PAST TENSE:

Active: He wrote a poem.
Passive: A poem was written by him.

Active: We saw a movie.
Passive: A movie was seen by us.

FUTURE TENSE:

Active: I will finish the work.
Passive: The work will be finished by me.

Active: She will buy a book.
Passive: A book will be bought by her.

COMMON VERB FORMS (3rd form):
- See → Saw → Seen
- Write → Wrote → Written
- Eat → Ate → Eaten
- Do → Did → Done
- Take → Took → Taken
- Make → Made → Made
- Buy → Bought → Bought
- Catch → Caught → Caught
- Teach → Taught → Taught

WHEN TO USE PASSIVE:
1. When doer is unknown: "The window was broken."
2. When doer is obvious: "The thief was arrested."
3. When focus is on action: "Sugar is made from cane."
4. Formal/scientific writing

QUESTIONS:

Active: Did she write the letter?
Passive: Was the letter written by her?

Active: Will you finish it?
Passive: Will it be finished by you?''',
        'quiz_questions': [
            {'q': 'Passive of "She eats an apple"?', 'a': 'An apple eats her', 'b': 'An apple is eaten by her', 'c': 'She is eating apple', 'd': 'She ate apple', 'correct': 'B'},
            {'q': 'Third form of "write"?', 'a': 'Wrote', 'b': 'Writed', 'c': 'Written', 'd': 'Writing', 'correct': 'C'},
            {'q': 'Active: He bought a car. Passive?', 'a': 'A car is bought by him', 'b': 'A car was bought by him', 'c': 'Car bought him', 'd': 'He is buying car', 'correct': 'B'},
            {'q': 'Active voice uses?', 'a': 'Subject does action', 'b': 'Subject receives action', 'c': 'No subject', 'd': 'No action', 'correct': 'A'},
            {'q': 'Third form of "see"?', 'a': 'Saw', 'b': 'Seen', 'c': 'Seeing', 'd': 'Sees', 'correct': 'B'},
            {'q': 'Active: They will play. Passive?', 'a': 'Played by them', 'b': 'It will be played by them', 'c': 'They play', 'd': 'Will play be', 'correct': 'B'},
        ]
    },
    {
        'grade': 7, 'subject': 'Social Studies', 'title': 'Medieval Indian History',
        'description': 'Important dynasties and rulers of medieval India',
        'content': '''MEDIEVAL INDIAN HISTORY

Period: 8th to 18th century

MAJOR DYNASTIES:

DELHI SULTANATE (1206-1526):

1. Slave Dynasty (1206-1290)
- Founded by Qutubuddin Aibak
- Built Qutub Minar
- Razia Sultana (first woman ruler)

2. Khilji Dynasty (1290-1320)
- Alauddin Khilji
- Defeated Mongols
- Market control system

3. Tughlaq Dynasty (1320-1414)
- Muhammad Bin Tughlaq
- Moved capital to Daulatabad
- Introduced copper coins

4. Sayyid Dynasty (1414-1451)

5. Lodi Dynasty (1451-1526)
- Ibrahim Lodi defeated by Babur

MUGHAL EMPIRE (1526-1857):

1. BABUR (1526-1530)
- Founder
- Battle of Panipat (1526)
- Defeated Ibrahim Lodi

2. HUMAYUN (1530-1556)
- Lost to Sher Shah Suri
- Regained throne later

3. AKBAR THE GREAT (1556-1605)
- Greatest Mughal
- Religious tolerance
- Nine Gems (Navratnas)
- Built Fatehpur Sikri
- Started Din-i-Ilahi
- Land revenue system

4. JAHANGIR (1605-1627)
- Married Nur Jahan
- Famous for justice

5. SHAH JAHAN (1628-1658)
- Built Taj Mahal (for wife Mumtaz)
- Red Fort, Jama Masjid
- Peacock Throne

6. AURANGZEB (1658-1707)
- Last great Mughal
- Strict, religious
- Empire weakened after him

VIJAYANGARA EMPIRE (South India):
- Founded by Harihara and Bukka
- Krishnadevaraya - greatest king
- Capital: Hampi

MARATHA EMPIRE:
- Shivaji Maharaj (1627-1680)
- Founder of Maratha Empire
- Built strong navy
- Crowned at Raigad
- Symbol of bravery

Other Important Rulers:
- Sher Shah Suri: Built Grand Trunk Road, introduced Rupiya
- Tipu Sultan: Tiger of Mysore, fought British
- Maharana Pratap: Rajput hero
- Rani Lakshmibai: Queen of Jhansi, 1857 revolt

ARCHITECTURE:
- Taj Mahal: Shah Jahan
- Red Fort: Shah Jahan
- Qutub Minar: Qutubuddin Aibak
- Charminar: Quli Qutub Shah
- Fatehpur Sikri: Akbar
- Humayun's Tomb: First Mughal tomb

ART AND CULTURE:
- Painting flourished under Mughals
- Urdu language developed
- Music: Tansen (Akbar's court)
- Hindi-Islamic culture mixed

BHAKTI MOVEMENT:
Saints spread love and devotion
- Kabir, Tulsidas, Mirabai
- Guru Nanak (founder of Sikhism)
- Tukaram, Eknath

SUFI MOVEMENT:
- Khwaja Moinuddin Chishti
- Nizamuddin Auliya''',
        'quiz_questions': [
            {'q': 'Founder of Mughal Empire?', 'a': 'Babur', 'b': 'Akbar', 'c': 'Humayun', 'd': 'Aurangzeb', 'correct': 'A'},
            {'q': 'Taj Mahal was built by?', 'a': 'Akbar', 'b': 'Shah Jahan', 'c': 'Aurangzeb', 'd': 'Babur', 'correct': 'B'},
            {'q': 'First woman ruler of Delhi?', 'a': 'Nur Jahan', 'b': 'Razia Sultana', 'c': 'Mumtaz', 'd': 'Roshan', 'correct': 'B'},
            {'q': 'Qutub Minar built by?', 'a': 'Akbar', 'b': 'Babur', 'c': 'Qutubuddin Aibak', 'd': 'Shah Jahan', 'correct': 'C'},
            {'q': 'Greatest Maratha king?', 'a': 'Tipu Sultan', 'b': 'Shivaji', 'c': 'Pratap', 'd': 'Tansen', 'correct': 'B'},
            {'q': 'Founder of Sikhism?', 'a': 'Kabir', 'b': 'Tulsidas', 'c': 'Guru Nanak', 'd': 'Mirabai', 'correct': 'C'},
            {'q': 'Battle of Panipat (first) was in?', 'a': '1526', 'b': '1556', 'c': '1576', 'd': '1605', 'correct': 'A'},
        ]
    },

    # ==================== GRADE 8 ====================
    {
        'grade': 8, 'subject': 'Mathematics', 'title': 'Linear Equations and Mensuration',
        'description': 'Linear equations and calculating area, volume',
        'content': '''LINEAR EQUATIONS AND MENSURATION

LINEAR EQUATIONS:
An equation in which the highest power of variable is 1.

Examples:
- 2x + 3 = 7
- 5y - 8 = 12
- x/3 + 2 = 5

SOLVING LINEAR EQUATIONS:

Example 1: 2x + 5 = 17
Step 1: 2x = 17 - 5 = 12
Step 2: x = 12/2 = 6
Check: 2(6) + 5 = 17 ✓

Example 2: 3y - 7 = 14
Step 1: 3y = 14 + 7 = 21
Step 2: y = 21/3 = 7

Example 3: 5x + 3 = 2x + 12
Step 1: 5x - 2x = 12 - 3
Step 2: 3x = 9
Step 3: x = 3

WORD PROBLEMS:
1. Read carefully
2. Identify variable (let it be x)
3. Form equation
4. Solve

Example: Sum of two numbers is 30. One is twice the other. Find them.
Let smaller = x
Larger = 2x
x + 2x = 30
3x = 30
x = 10
So numbers are 10 and 20.

MENSURATION (Measurement):

PERIMETER:
Total length around a shape.

- Square: 4 × side
- Rectangle: 2(length + breadth)
- Triangle: sum of all sides
- Circle: 2πr (circumference)

AREA:
Space inside a shape.

- Square: side × side = side²
- Rectangle: length × breadth
- Triangle: ½ × base × height
- Circle: πr²
- Parallelogram: base × height

VOLUME:
Space occupied by a 3D shape.

- Cube: side × side × side = side³
- Cuboid: length × breadth × height
- Cylinder: πr²h
- Sphere: (4/3)πr³

UNITS:
- Length: meter (m), cm, km
- Area: m², cm²
- Volume: m³, cm³, liters

CONVERSIONS:
- 1 m = 100 cm
- 1 km = 1000 m
- 1 m² = 10000 cm²
- 1 liter = 1000 ml = 1000 cm³

π (PI):
- Approximate value: 22/7 or 3.14
- Used for circles

EXAMPLES:

Find area of rectangle 5m × 3m:
Area = 5 × 3 = 15 m²

Find perimeter of square side 4cm:
Perimeter = 4 × 4 = 16 cm

Find area of circle radius 7cm:
Area = π × r² = (22/7) × 7 × 7 = 154 cm²

Volume of cube side 5cm:
Volume = 5³ = 125 cm³''',
        'quiz_questions': [
            {'q': 'Solve: 2x + 5 = 17', 'a': 'x = 4', 'b': 'x = 6', 'c': 'x = 8', 'd': 'x = 11', 'correct': 'B'},
            {'q': 'Area of rectangle (5×4)?', 'a': '9', 'b': '18', 'c': '20', 'd': '25', 'correct': 'C'},
            {'q': 'Perimeter of square side 6?', 'a': '12', 'b': '24', 'c': '36', 'd': '48', 'correct': 'B'},
            {'q': 'Area of triangle base=4, height=6?', 'a': '10', 'b': '12', 'c': '20', 'd': '24', 'correct': 'B'},
            {'q': 'Volume of cube side 4?', 'a': '12', 'b': '16', 'c': '32', 'd': '64', 'correct': 'D'},
            {'q': 'Solve: 3x - 4 = 11', 'a': 'x = 3', 'b': 'x = 5', 'c': 'x = 7', 'd': 'x = 15', 'correct': 'B'},
        ]
    },
    {
        'grade': 8, 'subject': 'Science', 'title': 'Force, Friction and Pressure',
        'description': 'Understanding physical forces and their effects',
        'content': '''FORCE, FRICTION AND PRESSURE

FORCE:
A push or pull on an object.

Examples:
- Pushing a door
- Pulling a rope
- Kicking a ball
- Lifting a weight

SI Unit of Force: NEWTON (N)
Named after Sir Isaac Newton

Effects of Force:
1. Changes position (start/stop motion)
2. Changes direction
3. Changes speed
4. Changes shape (squeezing dough)
5. Changes size (stretching rubber band)

TYPES OF FORCES:

1. CONTACT FORCES:
- Muscular force (using muscles)
- Friction force (when surfaces touch)
- Mechanical force (machines)

2. NON-CONTACT FORCES:
- Gravitational force (Earth pulls everything)
- Magnetic force (between magnets)
- Electrostatic force (between charges)

GRAVITATIONAL FORCE:
- Earth pulls everything towards it
- That's why things fall down
- Discovered by Newton (apple story)
- Weight = mass × gravity

FRICTION:
Force that opposes motion between two surfaces in contact.

Types:
1. Static friction (object at rest)
2. Sliding friction (object sliding)
3. Rolling friction (object rolling)

Rolling friction < Sliding friction < Static friction

Why Friction:
- Roughness of surfaces (even smooth ones)
- Interlocking of irregularities

Useful Friction:
- Walking (without friction we slip)
- Writing on paper
- Brakes on vehicles
- Holding objects
- Lighting matchstick

Harmful Friction:
- Wears out machine parts
- Wastes energy as heat
- Slows down vehicles

Reducing Friction:
- Oil/grease (lubrication)
- Ball bearings
- Polished surfaces
- Streamlined shapes
- Wheels (rolling friction is less)

Increasing Friction:
- Rough soles on shoes
- Treaded tyres
- Sand on icy roads

PRESSURE:
Force acting on per unit area.

Pressure = Force / Area

SI Unit: PASCAL (Pa)
1 Pa = 1 N/m²

Why same force gives different pressure:
- Small area = More pressure
- Large area = Less pressure

Examples:
- Knife is sharp (small area, more pressure to cut)
- Nail has pointed tip (more pressure)
- Camel has wide feet (less pressure, doesn't sink in sand)
- Foundation of building is wide (less pressure on ground)
- Bag straps wide (less pressure on shoulders)

ATMOSPHERIC PRESSURE:
- Pressure exerted by air around us
- At sea level: 1 atm = 1,01,325 Pa
- Decreases with altitude

That's why:
- Difficult to breathe at high altitudes
- Pen ink leaks in flight
- Suction works

LIQUID PRESSURE:
- Increases with depth
- Same at same depth
- Acts in all directions

That's why:
- Dams are thicker at bottom
- Deep sea divers need pressure suits

BUOYANCY:
Upward force by liquid on objects in it.
- Wood floats (less dense than water)
- Iron sinks (more dense than water)

Archimedes' Principle:
Buoyant force = weight of liquid displaced''',
        'quiz_questions': [
            {'q': 'SI unit of force?', 'a': 'Pascal', 'b': 'Newton', 'c': 'Joule', 'd': 'Watt', 'correct': 'B'},
            {'q': 'Pressure = ?', 'a': 'Force × Area', 'b': 'Force / Area', 'c': 'Area / Force', 'd': 'Mass × Force', 'correct': 'B'},
            {'q': 'Friction always?', 'a': 'Helps motion', 'b': 'Opposes motion', 'c': 'Stops motion', 'd': 'No effect', 'correct': 'B'},
            {'q': 'Why nails have pointed tips?', 'a': 'Looks good', 'b': 'More pressure on small area', 'c': 'Strong', 'd': 'Cheap', 'correct': 'B'},
            {'q': 'Least friction?', 'a': 'Static', 'b': 'Sliding', 'c': 'Rolling', 'd': 'All same', 'correct': 'C'},
            {'q': 'SI unit of pressure?', 'a': 'Newton', 'b': 'Pascal', 'c': 'Joule', 'd': 'Watt', 'correct': 'B'},
            {'q': 'Atmospheric pressure at sea level (in atm)?', 'a': '0.5', 'b': '1', 'c': '2', 'd': '10', 'correct': 'B'},
        ]
    },
    {
        'grade': 8, 'subject': 'Social Studies', 'title': 'Indian Constitution and Government',
        'description': 'Structure of Indian government and constitutional rights',
        'content': '''INDIAN CONSTITUTION AND GOVERNMENT

THE CONSTITUTION:
Supreme law of India.

Key Facts:
- Adopted: 26 November 1949
- Effective: 26 January 1950
- Longest written constitution in world
- Drafted by Constituent Assembly
- Chairman of Drafting Committee: Dr. B.R. Ambedkar
- Father of Indian Constitution: Dr. B.R. Ambedkar

PREAMBLE:
Introduction declaring India as:
- SOVEREIGN
- SOCIALIST
- SECULAR
- DEMOCRATIC
- REPUBLIC

FEATURES:
1. Federal system
2. Single citizenship
3. Independent judiciary
4. Fundamental Rights
5. Universal Adult Franchise (everyone 18+ can vote)

FUNDAMENTAL RIGHTS (6):

1. RIGHT TO EQUALITY
- Equal before law
- No discrimination by religion, caste, sex
- Equal opportunity

2. RIGHT TO FREEDOM
- Speech and expression
- Movement
- Profession
- Form associations

3. RIGHT AGAINST EXPLOITATION
- No forced labour
- No child labour under 14
- No human trafficking

4. RIGHT TO FREEDOM OF RELIGION
- Practice any religion
- Propagate religion
- All religions equal

5. CULTURAL AND EDUCATIONAL RIGHTS
- Minorities protected
- Right to preserve language and culture

6. RIGHT TO CONSTITUTIONAL REMEDIES
- Approach Supreme Court if rights violated
- Called "Heart of Constitution" by Ambedkar

FUNDAMENTAL DUTIES (11):
- Respect Constitution and Flag
- Cherish freedom movement ideals
- Protect sovereignty
- Defend country
- Promote harmony
- Preserve heritage
- Protect environment
- Develop scientific temper
- Safeguard public property
- Strive for excellence
- Provide education (added later)

THREE BRANCHES OF GOVERNMENT:

1. LEGISLATIVE (Parliament) - Makes laws
- Lok Sabha (Lower House): 545 members, elected
- Rajya Sabha (Upper House): 245 members
- President is part of Parliament

2. EXECUTIVE - Implements laws
- President (Head of State)
- Prime Minister (Head of Government)
- Council of Ministers
- Bureaucracy

3. JUDICIARY - Interprets laws
- Supreme Court (highest)
- High Courts (state level)
- District Courts
- Independent of executive

PRESIDENT OF INDIA:
- Head of state
- Supreme Commander of Armed Forces
- Elected by elected representatives
- Term: 5 years
- Lives in: Rashtrapati Bhavan

PRIME MINISTER:
- Real head of government
- Leader of party with majority in Lok Sabha
- Chairs Council of Ministers
- Term: 5 years (unless dissolved)

ELECTIONS:
- Held every 5 years
- Election Commission conducts
- EVM (Electronic Voting Machine) used
- Secret ballot
- Universal Adult Franchise

LEVELS OF GOVERNMENT:
1. Central (Union) Government - PM, President
2. State Government - CM, Governor
3. Local Government - Panchayat (village), Municipality (city)

SECULARISM:
India treats all religions equally.
- No state religion
- Citizens can practice any faith
- No religious discrimination''',
        'quiz_questions': [
            {'q': 'When did Constitution come into effect?', 'a': '15 Aug 1947', 'b': '26 Nov 1949', 'c': '26 Jan 1950', 'd': '2 Oct 1950', 'correct': 'C'},
            {'q': 'Father of Indian Constitution?', 'a': 'Gandhi', 'b': 'Nehru', 'c': 'Ambedkar', 'd': 'Patel', 'correct': 'C'},
            {'q': 'How many Fundamental Rights?', 'a': '4', 'b': '5', 'c': '6', 'd': '7', 'correct': 'C'},
            {'q': 'Head of Indian government?', 'a': 'President', 'b': 'Prime Minister', 'c': 'Chief Justice', 'd': 'Speaker', 'correct': 'B'},
            {'q': 'Voting age in India?', 'a': '16', 'b': '18', 'c': '21', 'd': '25', 'correct': 'B'},
            {'q': 'Lower house of Parliament?', 'a': 'Rajya Sabha', 'b': 'Lok Sabha', 'c': 'Council', 'd': 'Cabinet', 'correct': 'B'},
            {'q': 'India is a ___', 'a': 'Monarchy', 'b': 'Republic', 'c': 'Dictatorship', 'd': 'Empire', 'correct': 'B'},
        ]
    },
    {
        'grade': 8, 'subject': 'English', 'title': 'Reading Comprehension Skills',
        'description': 'Understanding passages and answering questions',
        'content': '''READING COMPREHENSION SKILLS

Reading comprehension means understanding what you read.

STEPS TO READ A PASSAGE:

1. SKIM the passage quickly
2. READ carefully
3. UNDERLINE key points
4. UNDERSTAND main idea
5. RE-READ if needed
6. ANSWER questions

TYPES OF QUESTIONS:

1. FACTUAL: Direct from text
   Example: "When did the event happen?"

2. INFERENCE: Read between lines
   Example: "Why did he leave?"

3. VOCABULARY: Word meanings
   Example: "What does 'magnificent' mean?"

4. MAIN IDEA: Central theme
   Example: "What is the passage about?"

5. ANALYSIS: Why/How questions

KEY READING SKILLS:

1. SKIMMING: Fast reading for general idea
2. SCANNING: Fast reading for specific info
3. CRITICAL READING: Understanding deeply

VOCABULARY BUILDING:

PREFIXES (Beginning):
- un- (not): unhappy, unable
- re- (again): redo, return
- pre- (before): preview, prepare
- dis- (not): dislike, disagree
- mis- (wrong): mistake, misread

SUFFIXES (Endings):
- -ful (full of): beautiful, helpful
- -less (without): careless, hopeless
- -er (more/person): bigger, teacher
- -est (most): biggest, fastest
- -ly (way): quickly, sadly

SYNONYMS (Same meaning):
- Happy = Joyful = Glad = Cheerful
- Big = Large = Huge = Enormous
- Sad = Unhappy = Gloomy = Miserable
- Smart = Intelligent = Clever = Wise

ANTONYMS (Opposite):
- Hot ↔ Cold
- Big ↔ Small
- Fast ↔ Slow
- Strong ↔ Weak
- Hard ↔ Soft

CONTEXT CLUES:
Guess word meaning from surroundings.
"The dog was very FEROCIOUS - it growled and showed its sharp teeth."
(Ferocious = fierce, dangerous)

MAIN IDEA vs DETAILS:

Main Idea: What the passage is mostly about
Details: Facts that support main idea

CONNECTING WORDS:
- because, since (reason)
- therefore, so (result)
- but, however (contrast)
- and, also (addition)
- first, then, finally (sequence)

TIPS FOR EXAMS:
1. Read questions first
2. Then read passage with questions in mind
3. Stay within passage info
4. Don't add your own thoughts
5. Quote directly when asked
6. Manage time

PRACTICE PASSAGE:
"The Great Banyan Tree in Kolkata is one of the largest trees in the world. It is over 250 years old. The main trunk had to be cut down due to disease, but its 3,500 aerial roots are still alive and the tree covers about 4 acres of land."

Questions:
1. Where is the Great Banyan Tree? (Kolkata)
2. How old is it? (Over 250 years)
3. Why was main trunk cut? (Disease)
4. How many aerial roots? (3,500)
5. What area does it cover? (4 acres)''',
        'quiz_questions': [
            {'q': 'Prefix "un-" means?', 'a': 'Again', 'b': 'Not', 'c': 'Wrong', 'd': 'Before', 'correct': 'B'},
            {'q': 'Synonym of "happy"?', 'a': 'Sad', 'b': 'Angry', 'c': 'Joyful', 'd': 'Tired', 'correct': 'C'},
            {'q': 'Antonym of "fast"?', 'a': 'Quick', 'b': 'Slow', 'c': 'Run', 'd': 'Speed', 'correct': 'B'},
            {'q': 'Skimming means?', 'a': 'Slow reading', 'b': 'Fast reading for general idea', 'c': 'No reading', 'd': 'Memorizing', 'correct': 'B'},
            {'q': 'Suffix "-less" means?', 'a': 'More', 'b': 'Without', 'c': 'Full of', 'd': 'Most', 'correct': 'B'},
            {'q': 'Synonym of "big"?', 'a': 'Tiny', 'b': 'Small', 'c': 'Huge', 'd': 'Short', 'correct': 'C'},
        ]
    },

    # ==================== GRADE 9 ====================
    {
        'grade': 9, 'subject': 'Mathematics', 'title': 'Polynomials',
        'description': 'Understanding polynomials and their operations',
        'content': '''POLYNOMIALS

A POLYNOMIAL is an algebraic expression with one or more terms.

Examples:
- 2x + 3 (linear)
- x² + 5x + 6 (quadratic)
- x³ + 2x² + x + 1 (cubic)

TYPES BY DEGREE:

Degree = highest power of variable

1. CONSTANT: degree 0
   Example: 5

2. LINEAR: degree 1
   Example: 2x + 3
   Form: ax + b

3. QUADRATIC: degree 2
   Example: x² - 4x + 4
   Form: ax² + bx + c

4. CUBIC: degree 3
   Example: 2x³ - x + 5
   Form: ax³ + bx² + cx + d

TYPES BY TERMS:

1. MONOMIAL: 1 term
   Examples: 3x, 5, -2y²

2. BINOMIAL: 2 terms
   Examples: x + 5, 2y - 7

3. TRINOMIAL: 3 terms
   Examples: x² + 2x + 1

OPERATIONS ON POLYNOMIALS:

ADDITION:
(2x² + 3x + 1) + (x² + 2x + 5)
= 3x² + 5x + 6

SUBTRACTION:
(3x² + 5x + 2) - (x² + 2x + 1)
= 2x² + 3x + 1

MULTIPLICATION:
(x + 2)(x + 3)
= x² + 3x + 2x + 6
= x² + 5x + 6

IMPORTANT IDENTITIES:

1. (a + b)² = a² + 2ab + b²
   (x + 3)² = x² + 6x + 9

2. (a - b)² = a² - 2ab + b²
   (x - 5)² = x² - 10x + 25

3. (a + b)(a - b) = a² - b²
   (x + 4)(x - 4) = x² - 16

4. (x + a)(x + b) = x² + (a+b)x + ab

5. (a + b)³ = a³ + 3a²b + 3ab² + b³

6. (a - b)³ = a³ - 3a²b + 3ab² - b³

FACTORIZATION:

1. COMMON FACTOR:
   2x² + 4x = 2x(x + 2)

2. GROUPING:
   xy + xz + y + z = x(y+z) + (y+z) = (y+z)(x+1)

3. IDENTITIES:
   x² - 9 = x² - 3² = (x+3)(x-3)

4. QUADRATIC:
   x² + 5x + 6
   Find two numbers that multiply to 6 and add to 5
   = 2 and 3
   = (x + 2)(x + 3)

ZEROS OF POLYNOMIAL:
Value of variable that makes polynomial = 0

Example: x² - 9 = 0
x² = 9
x = ±3

So zeros are 3 and -3.

REMAINDER THEOREM:
If polynomial p(x) is divided by (x - a),
remainder = p(a)

Example: p(x) = x² + 3x + 5
Divide by (x - 2):
Remainder = p(2) = 4 + 6 + 5 = 15

FACTOR THEOREM:
(x - a) is factor of p(x) if p(a) = 0

VALUE AT POINT:
If p(x) = x² + 3x - 4
p(2) = 4 + 6 - 4 = 6
p(-1) = 1 - 3 - 4 = -6''',
        'quiz_questions': [
            {'q': 'Degree of 3x² + 5x + 1?', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'correct': 'B'},
            {'q': '(x + 3)(x - 3) = ?', 'a': 'x² - 9', 'b': 'x² + 9', 'c': 'x² + 6x', 'd': 'x² - 6x', 'correct': 'A'},
            {'q': '(a + b)² = ?', 'a': 'a² + b²', 'b': 'a² - b²', 'c': 'a² + 2ab + b²', 'd': 'a² - 2ab + b²', 'correct': 'C'},
            {'q': 'p(x) = x² - 4. Find p(3).', 'a': '5', 'b': '7', 'c': '9', 'd': '13', 'correct': 'A'},
            {'q': 'Factor x² + 5x + 6 = ?', 'a': '(x+1)(x+6)', 'b': '(x+2)(x+3)', 'c': '(x+5)(x+1)', 'd': '(x+6)(x-1)', 'correct': 'B'},
            {'q': 'Zero of x - 5 = 0?', 'a': '0', 'b': '5', 'c': '-5', 'd': '1', 'correct': 'B'},
        ]
    },
    {
        'grade': 9, 'subject': 'Science', 'title': 'Matter in Our Surroundings',
        'description': 'States of matter, changes, and physical properties',
        'content': '''MATTER IN OUR SURROUNDINGS

MATTER:
Anything that has mass and occupies space.

Examples: Air, water, stone, table, food

CHARACTERISTICS:
1. Has MASS
2. Occupies SPACE (volume)
3. Made of small particles
4. Particles attract each other
5. Particles in continuous motion

STATES OF MATTER:

1. SOLID
- Definite shape and size
- Cannot be compressed
- Particles tightly packed
- Strong force of attraction
- Vibrate but don't move
- Examples: Ice, stone, wood

2. LIQUID
- No definite shape (takes container's shape)
- Definite volume
- Can flow
- Particles slightly apart
- Examples: Water, oil, milk

3. GAS
- No definite shape or volume
- Easily compressed
- Particles very far apart
- Move randomly in all directions
- Examples: Air, oxygen, hydrogen

PROPERTIES COMPARISON:
| Property | Solid | Liquid | Gas |
|----------|-------|--------|-----|
| Shape | Definite | Container | None |
| Volume | Definite | Definite | Container |
| Particle distance | Very close | Close | Far |
| Compression | No | Slight | Yes |
| Diffusion | Slow | Medium | Fast |

CHANGES OF STATE:

1. MELTING: Solid → Liquid
   - Adding heat
   - Ice → Water
   - Melting point of ice: 0°C

2. FREEZING: Liquid → Solid
   - Removing heat
   - Water → Ice

3. EVAPORATION: Liquid → Gas
   - Adding heat (slow)
   - At surface, any temperature

4. BOILING: Liquid → Gas
   - Adding heat (fast)
   - Throughout liquid
   - Boiling point of water: 100°C

5. CONDENSATION: Gas → Liquid
   - Removing heat
   - Vapor → Water drops

6. SUBLIMATION: Solid → Gas (directly)
   - Examples: Camphor, naphthalene, dry ice (CO2)

7. DEPOSITION: Gas → Solid (directly)

LATENT HEAT:
Heat absorbed/released during state change WITHOUT temperature change.

FACTORS AFFECTING EVAPORATION:
1. Temperature: Higher = faster
2. Surface area: More = faster
3. Humidity: Less = faster
4. Wind speed: More = faster

WHY DOES EVAPORATION CAUSE COOLING?
Particles need energy to evaporate.
They take heat from surroundings.
Surroundings get cooler.

That's why:
- Sweat cools us
- Earthen pots keep water cool
- We feel cool after rain

PLASMA:
4th state of matter
- Ionized gas
- Found in stars, lightning
- TV screens use plasma

BOSE-EINSTEIN CONDENSATE:
5th state (at very low temperatures)
- Discovered by Indian scientist S.N. Bose

PHYSICAL vs CHEMICAL CHANGES:

Physical:
- No new substance
- Reversible
- Examples: Melting ice, breaking glass, dissolving salt

Chemical:
- New substance formed
- Irreversible
- Examples: Burning, rusting, cooking

INTERCONVERSION OF STATES:
Change in:
- Temperature
- Pressure

Solid ↔ Liquid ↔ Gas

Higher temp → moves towards gas
Higher pressure → moves towards solid

DENSITY:
Mass per unit volume
Density = Mass / Volume
Unit: kg/m³ or g/cm³

- Solids: Highest density
- Liquids: Medium
- Gases: Lowest (except special cases)''',
        'quiz_questions': [
            {'q': 'States of matter?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'B'},
            {'q': 'Particles tightly packed in?', 'a': 'Gas', 'b': 'Liquid', 'c': 'Solid', 'd': 'All same', 'correct': 'C'},
            {'q': 'Solid to gas directly is?', 'a': 'Melting', 'b': 'Boiling', 'c': 'Sublimation', 'd': 'Condensation', 'correct': 'C'},
            {'q': 'Boiling point of water?', 'a': '50°C', 'b': '75°C', 'c': '100°C', 'd': '150°C', 'correct': 'C'},
            {'q': 'Melting point of ice?', 'a': '-10°C', 'b': '0°C', 'c': '10°C', 'd': '25°C', 'correct': 'B'},
            {'q': 'Plasma is found in?', 'a': 'Ice', 'b': 'Stars', 'c': 'Water', 'd': 'Rocks', 'correct': 'B'},
            {'q': 'Sweat cools us because of?', 'a': 'Wind', 'b': 'Evaporation', 'c': 'Sunlight', 'd': 'Sound', 'correct': 'B'},
        ]
    },
    {
        'grade': 9, 'subject': 'Social Studies', 'title': 'The French Revolution',
        'description': 'Causes, events and impact of the French Revolution',
        'content': '''THE FRENCH REVOLUTION (1789-1799)

A turning point in world history that ended monarchy in France.

CAUSES:

1. POLITICAL:
- Absolute monarchy of Louis XVI
- King had unlimited power
- No rights for common people
- Corrupt administration

2. SOCIAL:
Three Estates (classes):

FIRST ESTATE: Clergy (Priests)
- 1% of population
- Owned 10% of land
- No taxes
- Rich and powerful

SECOND ESTATE: Nobility
- 2% of population
- Owned 25% of land
- No taxes
- Many privileges

THIRD ESTATE: Common people
- 97% of population
- Peasants, workers, middle class
- Paid all taxes
- No rights
- Many were poor and hungry

3. ECONOMIC:
- Long wars drained treasury
- Help to American Revolution costly
- High taxes only on poor
- Bread shortage and high prices
- France was bankrupt

4. INTELLECTUAL:
PHILOSOPHERS inspired people:
- Voltaire: Freedom of speech
- Rousseau: Social contract
- Montesquieu: Separation of powers
- Spread ideas of liberty, equality

5. AMERICAN REVOLUTION (1776):
- Showed people could revolt
- Inspired French

MAJOR EVENTS:

5 MAY 1789: Estates General meeting called
- Third Estate demanded more votes
- Refused, broke away

20 JUNE 1789: Tennis Court Oath
- Third Estate formed National Assembly
- Vowed to write Constitution

14 JULY 1789: Storming of Bastille
- People attacked Bastille prison
- Marks beginning of Revolution
- Now French National Day

26 AUGUST 1789: Declaration of Rights of Man
- Liberty, Equality, Fraternity
- Basic rights for all

OCTOBER 1789: Women's March on Versailles
- Demanded bread and rights

1791: Constitution of France
- France became Constitutional Monarchy

1792: Republic Declared
- Louis XVI arrested

1793: Reign of Terror
- Led by Robespierre
- Thousands killed by guillotine
- Louis XVI and Marie Antoinette executed

1794: Robespierre executed
- End of Terror

1799: Napoleon Bonaparte rises to power

KEY FIGURES:

LOUIS XVI: King of France, executed
MARIE ANTOINETTE: Queen, executed ("Let them eat cake")
ROBESPIERRE: Leader of Reign of Terror
NAPOLEON BONAPARTE: Military leader, became Emperor
LAFAYETTE: Helped American Revolution too

IDEALS OF REVOLUTION:
- LIBERTY (Freedom)
- EQUALITY (Equal rights)
- FRATERNITY (Brotherhood)

These became motto of France and inspiration worldwide.

IMPACT:

In France:
- End of monarchy
- Feudalism abolished
- New legal system
- Democratic ideas

Worldwide:
- Inspired other revolutions
- Spread democracy
- Influenced Indian freedom movement
- Decline of absolute monarchies
- Rise of nationalism

The Tricolour Flag:
- Blue, White, Red
- Adopted during Revolution
- Symbol of revolutionary ideals

THE GUILLOTINE:
- Execution device
- Invented by Joseph Guillotin
- Used to execute thousands

SIGNIFICANCE FOR INDIA:
- Inspired Indian freedom fighters
- Concepts of Liberty, Equality, Fraternity included in Indian Constitution''',
        'quiz_questions': [
            {'q': 'When did French Revolution start?', 'a': '1776', 'b': '1789', 'c': '1799', 'd': '1815', 'correct': 'B'},
            {'q': 'Bastille was stormed on?', 'a': '4 July', 'b': '14 July', 'c': '26 August', 'd': '5 May', 'correct': 'B'},
            {'q': 'Motto of French Revolution?', 'a': 'Peace, Love, Unity', 'b': 'Liberty, Equality, Fraternity', 'c': 'Power, Money, Fame', 'd': 'King, Queen, Country', 'correct': 'B'},
            {'q': 'Last King of France?', 'a': 'Louis XIV', 'b': 'Louis XV', 'c': 'Louis XVI', 'd': 'Napoleon', 'correct': 'C'},
            {'q': 'Reign of Terror was led by?', 'a': 'Napoleon', 'b': 'Robespierre', 'c': 'Louis', 'd': 'Marie', 'correct': 'B'},
            {'q': 'Third Estate consisted of?', 'a': 'Clergy', 'b': 'Nobles', 'c': 'Common people', 'd': 'Royals', 'correct': 'C'},
        ]
    },
    {
        'grade': 9, 'subject': 'English', 'title': 'Sentence Structure',
        'description': 'Types of sentences and their structure',
        'content': '''SENTENCE STRUCTURE

A SENTENCE is a group of words that expresses a complete thought.

TYPES OF SENTENCES:

By PURPOSE:

1. DECLARATIVE (Statement)
- Tells something
- Ends with .
- Example: I love books.

2. INTERROGATIVE (Question)
- Asks something
- Ends with ?
- Example: Do you like cricket?

3. IMPERATIVE (Command/Request)
- Gives order or request
- Ends with . or !
- Example: Close the door. Please help me.

4. EXCLAMATORY (Strong feeling)
- Shows emotion
- Ends with !
- Example: What a beautiful day!

By STRUCTURE:

1. SIMPLE SENTENCE
- One independent clause
- Has one subject and one verb
- Example: She sings.

2. COMPOUND SENTENCE
- Two independent clauses joined by coordinator
- Coordinators: and, but, or, so, yet
- Example: She sings AND he dances.

3. COMPLEX SENTENCE
- One independent + one dependent clause
- Subordinators: because, since, although, if, when
- Example: She sings BECAUSE she is happy.

4. COMPOUND-COMPLEX
- Two or more independent + at least one dependent
- Example: She sings AND he dances WHEN they are happy.

PARTS OF A SENTENCE:

1. SUBJECT: Who/what the sentence is about
   - The dog barks. (dog = subject)
   - Children play. (children = subject)

2. PREDICATE: What the subject does/is
   - The dog BARKS.
   - Children PLAY in the garden.

3. OBJECT: Receives the action
   - I read a BOOK. (book = object)
   - She wrote a LETTER.

CLAUSES:

INDEPENDENT CLAUSE (Main):
- Has subject and verb
- Makes complete sense
- Can stand alone
- Example: "I love mangoes."

DEPENDENT CLAUSE (Subordinate):
- Has subject and verb
- Doesn't make complete sense alone
- Starts with subordinator
- Example: "Because they are sweet"

Together: "I love mangoes because they are sweet."

PHRASES:

A group of words without subject-verb pair.

Types:
- Noun phrase: a beautiful flower
- Verb phrase: was running fast
- Adjective phrase: full of joy
- Adverb phrase: in the morning
- Prepositional phrase: under the tree

CORRECT vs INCORRECT:

Incorrect: "Me and my friend went."
Correct: "My friend and I went."

Incorrect: "She don't like it."
Correct: "She doesn't like it."

Incorrect: "I have went there."
Correct: "I have gone there." OR "I went there."

Incorrect: "Between you and I"
Correct: "Between you and me"

PUNCTUATION:

. Period: End of statement
? Question mark: End of question
! Exclamation: Strong emotion
, Comma: Pause, lists
; Semicolon: Joins related ideas
: Colon: Introduces list/explanation
' Apostrophe: Contractions, possession
" " Quotation marks: Direct speech

CAPITALIZATION:
- First letter of sentence
- Proper nouns (names)
- Days, months
- "I" (always capital)
- Titles

Examples:
- My friend Ram lives in Delhi.
- I went to school on Monday.''',
        'quiz_questions': [
            {'q': 'Sentence ending with ? is?', 'a': 'Declarative', 'b': 'Interrogative', 'c': 'Imperative', 'd': 'Exclamatory', 'correct': 'B'},
            {'q': '"I love cake" is which type?', 'a': 'Simple', 'b': 'Compound', 'c': 'Complex', 'd': 'Run-on', 'correct': 'A'},
            {'q': 'Coordinator joins ___ clauses', 'a': 'Independent', 'b': 'Dependent', 'c': 'Both', 'd': 'None', 'correct': 'A'},
            {'q': 'Correct sentence:', 'a': 'Me went home', 'b': 'I went home', 'c': 'I going home', 'd': 'Home went I', 'correct': 'B'},
            {'q': 'In "Children play", what is subject?', 'a': 'Children', 'b': 'Play', 'c': 'Both', 'd': 'None', 'correct': 'A'},
            {'q': 'Imperative sentence?', 'a': 'I am happy', 'b': 'Are you sure?', 'c': 'Close the door', 'd': 'How beautiful!', 'correct': 'C'},
        ]
    },

    # ==================== GRADE 10 ====================
    {
        'grade': 10, 'subject': 'Mathematics', 'title': 'Trigonometry',
        'description': 'Sin, Cos, Tan ratios and trigonometric identities',
        'content': '''TRIGONOMETRY

Trigonometry deals with relationships between sides and angles of right triangles.

RIGHT TRIANGLE:
A triangle with one 90° angle.

In a right triangle with angle θ (theta):
- HYPOTENUSE: Longest side (opposite to 90°)
- OPPOSITE: Side opposite to θ
- ADJACENT: Side next to θ

SIX TRIGONOMETRIC RATIOS:

1. SIN θ = Opposite / Hypotenuse
2. COS θ = Adjacent / Hypotenuse
3. TAN θ = Opposite / Adjacent
4. COSEC θ = 1/sin θ = Hypotenuse/Opposite
5. SEC θ = 1/cos θ = Hypotenuse/Adjacent
6. COT θ = 1/tan θ = Adjacent/Opposite

Memory aid: SOH-CAH-TOA
- Sin = Opposite/Hypotenuse
- Cos = Adjacent/Hypotenuse
- Tan = Opposite/Adjacent

STANDARD VALUES:

| Angle | 0° | 30° | 45° | 60° | 90° |
|-------|-----|------|------|------|------|
| Sin | 0 | 1/2 | 1/√2 | √3/2 | 1 |
| Cos | 1 | √3/2 | 1/√2 | 1/2 | 0 |
| Tan | 0 | 1/√3 | 1 | √3 | undefined |

TRIGONOMETRIC IDENTITIES:

1. sin²θ + cos²θ = 1
2. 1 + tan²θ = sec²θ
3. 1 + cot²θ = cosec²θ

RELATIONSHIPS:
- tan θ = sin θ / cos θ
- cot θ = cos θ / sin θ
- sec θ = 1/cos θ
- cosec θ = 1/sin θ

COMPLEMENTARY ANGLES:
sin(90° - θ) = cos θ
cos(90° - θ) = sin θ
tan(90° - θ) = cot θ

EXAMPLES:

If sin θ = 3/5, find cos θ and tan θ.
Using sin²θ + cos²θ = 1:
(3/5)² + cos²θ = 1
9/25 + cos²θ = 1
cos²θ = 1 - 9/25 = 16/25
cos θ = 4/5

tan θ = sin θ/cos θ = (3/5)/(4/5) = 3/4

APPLICATIONS:

1. Height of building (using angle of elevation)
2. Width of river
3. Distance of ships from shore
4. Astronomy and navigation
5. Architecture

ANGLE OF ELEVATION:
Angle from horizontal looking UP.
Used for tall objects.

ANGLE OF DEPRESSION:
Angle from horizontal looking DOWN.

EXAMPLE PROBLEM:
A 10m ladder leans against a wall at 60° angle to ground.
Find height reached.

Sin 60° = height / 10
height = 10 × sin 60°
height = 10 × √3/2
height = 5√3 m
height ≈ 8.66 m

PYTHAGORAS THEOREM:
In right triangle: a² + b² = c²
(c is hypotenuse)

This relates to trigonometry:
If sin θ = 3/5 (Opposite=3, Hypotenuse=5)
Then Adjacent = √(5²-3²) = √16 = 4

So cos θ = 4/5 (Adjacent/Hypotenuse)''',
        'quiz_questions': [
            {'q': 'sin 30° = ?', 'a': '0', 'b': '1/2', 'c': '√3/2', 'd': '1', 'correct': 'B'},
            {'q': 'cos 60° = ?', 'a': '0', 'b': '1/2', 'c': '√3/2', 'd': '1', 'correct': 'B'},
            {'q': 'tan 45° = ?', 'a': '0', 'b': '1/2', 'c': '1', 'd': '√3', 'correct': 'C'},
            {'q': 'sin²θ + cos²θ = ?', 'a': '0', 'b': '1', 'c': '2', 'd': 'tan θ', 'correct': 'B'},
            {'q': 'sin 90° = ?', 'a': '0', 'b': '1/2', 'c': '√3/2', 'd': '1', 'correct': 'D'},
            {'q': 'If sin θ = 3/5, cos θ = ?', 'a': '3/4', 'b': '4/5', 'c': '5/4', 'd': '5/3', 'correct': 'B'},
            {'q': 'sec θ = ?', 'a': '1/sin θ', 'b': '1/cos θ', 'c': '1/tan θ', 'd': 'cos θ', 'correct': 'B'},
        ]
    },
    {
        'grade': 10, 'subject': 'Science', 'title': 'Chemical Reactions and Equations',
        'description': 'Types of chemical reactions and balancing equations',
        'content': '''CHEMICAL REACTIONS AND EQUATIONS

CHEMICAL REACTION:
A process where one or more substances change into different substances.

Signs of Chemical Reaction:
1. Change in color
2. Change in temperature
3. Evolution of gas
4. Formation of precipitate
5. Change in smell

REACTANTS → PRODUCTS

Reactants: Substances that combine
Products: New substances formed

CHEMICAL EQUATION:
Symbolic representation of reaction.

Example: H₂ + O₂ → H₂O (unbalanced)
Balanced: 2H₂ + O₂ → 2H₂O

BALANCING EQUATIONS:
Number of atoms must be EQUAL on both sides.

Steps to Balance:
1. Write skeletal equation
2. Count atoms on each side
3. Multiply with coefficients
4. Check again

Example:
Fe + O₂ → Fe₂O₃
Balance:
4Fe + 3O₂ → 2Fe₂O₃

TYPES OF CHEMICAL REACTIONS:

1. COMBINATION REACTION:
Two or more substances combine to form one.

A + B → AB

Examples:
- 2H₂ + O₂ → 2H₂O (water formation)
- CaO + H₂O → Ca(OH)₂ (slaked lime)
- 2Mg + O₂ → 2MgO (magnesium oxide)

2. DECOMPOSITION REACTION:
One substance breaks into two or more.

AB → A + B

Examples:
- 2H₂O → 2H₂ + O₂ (electrolysis)
- CaCO₃ → CaO + CO₂ (limestone heated)
- 2AgCl → 2Ag + Cl₂ (light)

3. DISPLACEMENT REACTION:
More reactive element replaces less reactive one.

A + BC → AC + B

Examples:
- Zn + CuSO₄ → ZnSO₄ + Cu
- Fe + CuSO₄ → FeSO₄ + Cu

Reactivity Series: K > Na > Ca > Mg > Al > Zn > Fe > Cu > Hg > Ag > Au

4. DOUBLE DISPLACEMENT:
Two compounds exchange ions.

AB + CD → AD + CB

Examples:
- AgNO₃ + NaCl → AgCl + NaNO₃ (precipitation)
- BaCl₂ + Na₂SO₄ → BaSO₄ + 2NaCl

5. OXIDATION & REDUCTION (Redox):

OXIDATION:
- Addition of oxygen
- Removal of hydrogen
- Loss of electrons

REDUCTION:
- Removal of oxygen
- Addition of hydrogen
- Gain of electrons

Memory: OIL RIG
Oxidation Is Loss (of electrons)
Reduction Is Gain (of electrons)

Example: 2Cu + O₂ → 2CuO
Cu is oxidized (gains oxygen)

CORROSION:
Slow eating away of metals.

Examples:
- Iron rusts (Fe₂O₃)
- Silver tarnishes (black)
- Copper turns green

Prevention:
- Painting
- Greasing/oiling
- Galvanization (zinc coating)
- Electroplating

RANCIDITY:
Oxidation of fats/oils in food.
- Bad smell and taste
- Prevented by:
  - Antioxidants
  - Air-tight containers
  - Refrigeration
  - Adding nitrogen

EXOTHERMIC REACTION:
Releases heat.
Examples: Burning, neutralization, respiration

ENDOTHERMIC REACTION:
Absorbs heat.
Examples: Photosynthesis, melting ice

LAW OF CONSERVATION OF MASS:
"Mass can neither be created nor destroyed."
That's why we balance equations.

COMMON CHEMICAL FORMULAS:
- Water: H₂O
- Carbon dioxide: CO₂
- Common salt: NaCl
- Sugar: C₁₂H₂₂O₁₁
- Methane: CH₄
- Ammonia: NH₃
- Sulphuric acid: H₂SO₄
- Calcium carbonate: CaCO₃ (chalk, marble)''',
        'quiz_questions': [
            {'q': 'Balanced: 2H₂ + O₂ → ?', 'a': 'H₂O', 'b': '2H₂O', 'c': '3H₂O', 'd': '4H₂O', 'correct': 'B'},
            {'q': 'A + B → AB is which type?', 'a': 'Decomposition', 'b': 'Combination', 'c': 'Displacement', 'd': 'Redox', 'correct': 'B'},
            {'q': 'Rusting of iron is?', 'a': 'Physical', 'b': 'Chemical', 'c': 'Both', 'd': 'None', 'correct': 'B'},
            {'q': 'Oxidation means?', 'a': 'Loss of oxygen', 'b': 'Loss of electrons', 'c': 'Gain of electrons', 'd': 'No change', 'correct': 'B'},
            {'q': 'Formula of water?', 'a': 'CO₂', 'b': 'H₂O', 'c': 'O₂', 'd': 'H₂', 'correct': 'B'},
            {'q': 'Photosynthesis is?', 'a': 'Exothermic', 'b': 'Endothermic', 'c': 'Neither', 'd': 'Both', 'correct': 'B'},
            {'q': 'AgNO₃ + NaCl → ? + NaNO₃', 'a': 'AgN', 'b': 'AgCl', 'c': 'NaCl', 'd': 'Ag', 'correct': 'B'},
        ]
    },
    {
        'grade': 10, 'subject': 'Science', 'title': 'Life Processes',
        'description': 'How living organisms perform essential functions',
        'content': '''LIFE PROCESSES

Processes that maintain life in organisms.

7 LIFE PROCESSES:
1. Nutrition
2. Respiration
3. Transportation
4. Excretion
5. Control and Coordination
6. Reproduction
7. Growth

1. NUTRITION:
Process of obtaining food.

TYPES:

A) AUTOTROPHIC: Make own food
- Plants (photosynthesis)
- Some bacteria

PHOTOSYNTHESIS:
6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂

Site: Chloroplast (contains chlorophyll)
- Chlorophyll captures sunlight
- Stomata: tiny pores for gas exchange
- Sugar stored as starch

B) HETEROTROPHIC: Depend on others
- Animals, humans, fungi

Types of Heterotrophs:
- Herbivores (eat plants): cow, deer
- Carnivores (eat meat): lion, tiger
- Omnivores (both): humans, bears

HUMAN DIGESTIVE SYSTEM:
Mouth → Esophagus → Stomach → Small Intestine → Large Intestine → Rectum

Organs:
- Mouth: Chewing, saliva starts digestion
- Stomach: HCl, pepsin
- Small intestine: Main digestion (bile from liver, pancreatic juice)
- Large intestine: Water absorption
- Liver: Bile production
- Pancreas: Enzymes

2. RESPIRATION:
Breaking down food to release energy.

EQUATION:
C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy (ATP)

TYPES:

A) AEROBIC (with oxygen):
- More energy released
- In humans, plants
- CO₂ and water as byproducts

B) ANAEROBIC (without oxygen):
- Less energy
- In yeast (alcohol fermentation)
- In muscles during heavy exercise (lactic acid)

Human Respiratory System:
Nose → Pharynx → Larynx → Trachea → Bronchi → Lungs → Alveoli

Breathing Rate:
- Adult: 15-18 per minute
- Children: 20-30 per minute

Plants:
- Day: Photosynthesis + Respiration
- Night: Only Respiration
- Through stomata (leaves) and lenticels (stems)

3. TRANSPORTATION:

IN HUMANS:
Circulatory System
- Heart: Pumps blood
- Blood vessels: Arteries, veins, capillaries
- Blood: Transport medium

Heart:
- 4 chambers: 2 atria, 2 ventricles
- Right side: receives impure blood (CO₂-rich)
- Left side: pumps pure blood (O₂-rich)

Blood:
- RBC (Red Blood Cells): carry O₂ (hemoglobin)
- WBC (White Blood Cells): fight infection
- Platelets: blood clotting
- Plasma: liquid part

Heart rate: 72 beats per minute (average)

IN PLANTS:
- XYLEM: transports water and minerals (root to leaves)
- PHLOEM: transports food (leaves to all parts)

TRANSPIRATION:
Loss of water from leaves
- Helps in pulling water up
- Cools the plant

4. EXCRETION:
Removing waste from body.

IN HUMANS:
Kidneys filter blood → Urine

Urinary system:
- 2 Kidneys (filter blood)
- Ureters
- Bladder (stores urine)
- Urethra (passes urine out)

Each kidney has nephrons (filtering units).

DIALYSIS:
Artificial kidney for patients with kidney failure.

IN PLANTS:
- Through stomata (O₂, water vapor)
- Through bark
- Through leaves falling

5. CONTROL AND COORDINATION:

IN HUMANS:
Two systems:

A) NERVOUS SYSTEM:
- Brain (control center)
- Spinal cord
- Nerves
- Fast response

Reflex Action: Quick automatic response
(touching hot object → pulling hand)

B) ENDOCRINE SYSTEM (Hormones):
- Slow but long-lasting
- Glands release hormones

Important Glands:
- Pituitary: Master gland
- Thyroid: Metabolism
- Pancreas: Insulin (blood sugar)
- Adrenal: Adrenaline (emergencies)

IN PLANTS:
Hormones called PHYTOHORMONES:
- Auxin: growth, bending toward light
- Gibberellin: growth
- Cytokinin: cell division
- Abscisic acid: stress response

Movements:
- Phototropism: toward light
- Geotropism: roots grow down, shoots up
- Hydrotropism: toward water
- Thigmotropism: response to touch (creepers)

6. REPRODUCTION:
Creating new offspring.

Asexual: One parent (binary fission, budding)
Sexual: Two parents

7. GROWTH:
Increase in size and complexity over time.

THE HEART (Detailed):

Four chambers:
- Right Atrium (RA): receives blood from body
- Right Ventricle (RV): pumps to lungs
- Left Atrium (LA): receives blood from lungs
- Left Ventricle (LV): pumps to body

Blood Flow:
Body → RA → RV → Lungs → LA → LV → Body

Why double circulation?
- O₂ rich and poor blood stay separate
- More efficient
- Important for warm-blooded animals''',
        'quiz_questions': [
            {'q': 'Process of breathing?', 'a': 'Respiration', 'b': 'Digestion', 'c': 'Excretion', 'd': 'Circulation', 'correct': 'A'},
            {'q': 'Site of photosynthesis?', 'a': 'Root', 'b': 'Stem', 'c': 'Chloroplast', 'd': 'Flower', 'correct': 'C'},
            {'q': 'Heart has how many chambers?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'C'},
            {'q': 'RBC carry?', 'a': 'CO₂', 'b': 'O₂', 'c': 'Food', 'd': 'Water', 'correct': 'B'},
            {'q': 'Xylem transports?', 'a': 'Food', 'b': 'Water', 'c': 'Air', 'd': 'Both', 'correct': 'B'},
            {'q': 'Insulin is produced by?', 'a': 'Liver', 'b': 'Kidney', 'c': 'Pancreas', 'd': 'Heart', 'correct': 'C'},
            {'q': 'Plants making own food is?', 'a': 'Heterotrophic', 'b': 'Autotrophic', 'c': 'Parasitic', 'd': 'Saprophytic', 'correct': 'B'},
        ]
    },
    {
        'grade': 10, 'subject': 'Social Studies', 'title': 'Nationalism in India',
        'description': 'Rise of nationalism and freedom movement in India',
        'content': '''NATIONALISM IN INDIA

Nationalism: Strong feeling of pride in one's country.

NATIONALISM IN INDIA:
Movement against British rule (1857-1947)

EARLY PHASE (1857-1905):

1857 - First War of Independence
- Soldiers' revolt against British
- Failed but inspired future movements

1885 - Indian National Congress (INC) founded
- A.O. Hume played key role
- First president: W.C. Bonnerjee
- Initially moderate

MODERATE LEADERS:
- Dadabhai Naoroji
- Gopal Krishna Gokhale
- Surendranath Banerjee
- Used petitions, requests

EXTREMIST LEADERS:
- Bal Gangadhar Tilak ("Swaraj is my birthright")
- Lala Lajpat Rai
- Bipin Chandra Pal
- (Lal-Bal-Pal trio)

1905: PARTITION OF BENGAL
- Lord Curzon divided Bengal
- Caused widespread protests
- Swadeshi Movement started

SWADESHI MOVEMENT:
- Boycott British goods
- Promote Indian products
- Burned British clothes

1911: Partition revoked

GANDHIAN ERA (1915-1947):

1915: GANDHI returned from South Africa
1917: CHAMPARAN movement (indigo farmers)
1918: AHMEDABAD movement (mill workers)
1919: KHEDA movement (peasants)

1919: ROWLATT ACT
- British law allowing arrest without trial
- Gandhi started Satyagraha

1919: JALLIANWALA BAGH MASSACRE
- General Dyer's troops fired
- 379 killed (official), 1000s actually
- 13 April 1919, Baisakhi day
- Shocked the world

1920-22: NON-COOPERATION MOVEMENT
Methods:
- Boycott schools, courts
- Surrender titles
- Don't pay taxes
- Don't buy British goods

Why ended: 1922 Chauri Chaura (violence)

1928: SIMON COMMISSION
- Came to review reforms
- No Indians in commission
- Slogan: "Simon Go Back"
- Lala Lajpat Rai injured, died

1929: PURNA SWARAJ
- Complete Independence declared
- 26 January celebrated as Independence Day
- Later became Republic Day

1930-31: CIVIL DISOBEDIENCE / SALT MARCH
- 12 March to 6 April 1930
- 240 mile march
- Gandhi made salt at Dandi
- Broke salt law
- Millions joined

1942: QUIT INDIA MOVEMENT
Slogan: "Do or Die"
- Demand: British leave India
- Mass protests
- All Congress leaders arrested

1942: AZAD HIND FAUJ (INA)
- Led by Subhash Chandra Bose
- "Give me blood, I'll give you freedom"
- Joined Japanese to fight British

1946: ROYAL INDIAN NAVY MUTINY

1947: INDEPENDENCE + PARTITION
- 15 August 1947: India free
- 14 August: Pakistan formed
- Massive violence and migrations

GREAT LEADERS:

MAHATMA GANDHI (1869-1948):
- Mohan Das Karam Chand Gandhi
- "Bapu" / "Father of Nation"
- Non-violence, Satyagraha
- Worked for Harijan welfare
- Khadi promotion
- Killed: 30 January 1948 by Nathuram Godse

JAWAHARLAL NEHRU (1889-1964):
- First Prime Minister
- Discovery of India (book)
- Friend of children

SARDAR PATEL (1875-1950):
- Iron Man of India
- United 565 princely states
- First Home Minister
- Bismarck of India

BHAGAT SINGH (1907-1931):
- Revolutionary
- "Inquilab Zindabad"
- Hanged at 23

SUBHASH CHANDRA BOSE (1897-1945):
- Netaji
- Indian National Army
- Mysterious death

DR. AMBEDKAR (1891-1956):
- Constitution architect
- Dalit rights champion

OTHER FIGURES:
- Rabindranath Tagore: National anthem author, Nobel laureate
- Sarojini Naidu: Poet, first woman governor
- C. Rajagopalachari (Rajaji): First Indian Governor-General
- Maulana Azad: Freedom fighter, first Education Minister

CONTRIBUTIONS:

WOMEN IN FREEDOM:
- Sarojini Naidu
- Kasturba Gandhi
- Vijayalakshmi Pandit
- Aruna Asaf Ali
- Sucheta Kripalani
- Captain Lakshmi Sehgal (INA)

PEASANT MOVEMENTS:
- Champaran (1917)
- Kheda (1918)
- Bardoli (1928)

LABOR MOVEMENTS:
- Workers strikes
- Trade unions

SYMBOLS:
- Flag (Tricolour)
- Bharat Mata image
- "Vande Mataram"
- Songs of patriotism

IMPACT:
- Got freedom 15 August 1947
- Democratic India
- Inspired other colonized nations
- Constitution gave equal rights
- Gandhian methods used worldwide''',
        'quiz_questions': [
            {'q': 'When was INC founded?', 'a': '1875', 'b': '1885', 'c': '1895', 'd': '1905', 'correct': 'B'},
            {'q': 'Jallianwala Bagh massacre year?', 'a': '1909', 'b': '1919', 'c': '1929', 'd': '1939', 'correct': 'B'},
            {'q': 'Quit India Movement slogan?', 'a': 'Inquilab', 'b': 'Do or Die', 'c': 'Swaraj', 'd': 'Vande', 'correct': 'B'},
            {'q': 'Salt March was led by?', 'a': 'Nehru', 'b': 'Patel', 'c': 'Gandhi', 'd': 'Bose', 'correct': 'C'},
            {'q': 'INA was formed by?', 'a': 'Gandhi', 'b': 'Nehru', 'c': 'Bose', 'd': 'Patel', 'correct': 'C'},
            {'q': '"Swaraj is my birthright" was said by?', 'a': 'Gandhi', 'b': 'Tilak', 'c': 'Nehru', 'd': 'Bose', 'correct': 'B'},
            {'q': '"Inquilab Zindabad" associated with?', 'a': 'Gandhi', 'b': 'Bhagat Singh', 'c': 'Patel', 'd': 'Tagore', 'correct': 'B'},
        ]
    },
    {
        'grade': 10, 'subject': 'English', 'title': 'Letter Writing and Communication',
        'description': 'Formal and informal letter writing skills',
        'content': '''LETTER WRITING

A letter is a written message from one person to another.

TYPES OF LETTERS:

1. FORMAL LETTERS
- For official purposes
- Professional tone
- Examples: Applications, complaints, business

2. INFORMAL LETTERS
- For personal communication
- Friendly tone
- Examples: To family, friends

FORMAL LETTER FORMAT:

Sender's Address
City - PIN
Date

The Recipient's Designation
Organization Name
Address
City - PIN

Subject: Brief topic

Salutation:
Sir/Madam,
Dear Sir/Madam,

Body:
- Paragraph 1: Purpose
- Paragraph 2: Details
- Paragraph 3: Closing

Yours faithfully/sincerely,
Signature
NAME (BLOCK LETTERS)

EXAMPLE - APPLICATION TO PRINCIPAL:

15 ABC Colony
Delhi - 110001
15 May 2024

The Principal
XYZ Public School
New Delhi - 110002

Subject: Application for Leave

Sir,

I am writing to inform you that I will not be able to attend school from 16 May to 18 May due to my sister's wedding. I will return to school on 19 May.

I request you to kindly grant me leave for these three days. I will make up for the missed lessons.

Thank you.

Yours obediently,
[Signature]
RAVI KUMAR
Class X-A

INFORMAL LETTER FORMAT:

Sender's Address
Date

Dear [Name],

Body:
- Opening (Hi, how are you?)
- Main message
- Closing

With love,
Your name

EXAMPLE - LETTER TO FRIEND:

15 ABC Colony
Delhi - 110001
15 May 2024

Dear Ravi,

How are you? I hope you and your family are doing well. I am writing to invite you to my birthday party next Saturday at 6 PM.

We will have games, food, and music. All our friends from school are coming. I would love it if you could come too.

Please let me know if you can make it.

Looking forward to seeing you!

With love,
Mohan

OTHER WRITING TYPES:

NOTICE WRITING:
- For announcements
- Box format
- Heading: NOTICE in center
- Issued by, Date

[INSIDE A BOX]

XYZ SCHOOL
NOTICE
15 May 2024

ANNUAL SPORTS DAY

This is to inform all students that Annual Sports Day will be held on 25 May 2024. All students are requested to participate enthusiastically.

For registration, contact: Sports Captain

[Signature]
Principal

EMAIL FORMAT:

To: recipient@email.com
Cc: (optional)
Subject: Brief topic

Dear [Name],

Body text

Regards,
Your Name

PARAGRAPH WRITING:

A paragraph is a group of sentences about ONE main idea.

Structure:
1. TOPIC SENTENCE: Main idea
2. SUPPORTING SENTENCES: Details, examples
3. CONCLUDING SENTENCE: Wrap up

Example Paragraph on "My Favorite Subject":
"Mathematics is my favorite subject. I enjoy solving problems and finding patterns in numbers. Algebra is particularly fascinating because it teaches me logical thinking. I also like how math connects to real life through measurements and calculations. Overall, mathematics challenges me and brings me joy."

ESSAY WRITING:

Structure:
1. INTRODUCTION
- Hook (interesting opening)
- Main idea/thesis

2. BODY (2-3 paragraphs)
- Point + explanation + example
- Connecting words

3. CONCLUSION
- Summary
- Final thought

COMMUNICATION TIPS:

1. CLARITY: Be clear and simple
2. CONCISENESS: No unnecessary words
3. COURTESY: Polite words
4. CORRECTNESS: Grammar and facts right
5. COMPLETENESS: All necessary info

COMMON PHRASES:

Beginning:
- "I am writing to inform..."
- "This is in reference to..."
- "I would like to..."

Ending (Formal):
- "Yours faithfully" (Unknown recipient)
- "Yours sincerely" (Known recipient)
- "Yours respectfully" (Superior)

Ending (Informal):
- "With love"
- "Best wishes"
- "Yours lovingly"

SALUTATIONS:

Formal:
- "Sir/Madam"
- "Dear Sir"
- "Dear Mr. Sharma"

Informal:
- "Dear [name]"
- "My dear [name]"
- "Hi [name]"

MISTAKES TO AVOID:

1. Wrong format
2. Spelling/grammar errors
3. Long sentences
4. Repetition
5. Missing date/address
6. Wrong salutation
7. Forgetting to sign''',
        'quiz_questions': [
            {'q': 'Formal letter to unknown person ends with?', 'a': 'With love', 'b': 'Yours faithfully', 'c': 'Best wishes', 'd': 'Cheers', 'correct': 'B'},
            {'q': 'Where is date written in formal letter?', 'a': 'After address', 'b': 'Bottom', 'c': 'Middle', 'd': 'Not needed', 'correct': 'A'},
            {'q': 'Subject in formal letter is?', 'a': 'Optional', 'b': 'Always required', 'c': 'In body', 'd': 'After signature', 'correct': 'B'},
            {'q': 'Informal letter starts with?', 'a': 'Sir/Madam', 'b': 'Dear [name]', 'c': 'To whom it may concern', 'd': 'Respected', 'correct': 'B'},
            {'q': 'A paragraph should focus on?', 'a': 'Many ideas', 'b': 'One main idea', 'c': 'No idea', 'd': 'Random topics', 'correct': 'B'},
            {'q': 'Yours sincerely is used when?', 'a': 'Unknown recipient', 'b': 'Known recipient', 'c': 'Always', 'd': 'Never', 'correct': 'B'},
        ]
    },
]


def load_all_content():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found.")
            return

        os.makedirs('./data/resources', exist_ok=True)

        existing_resources = {r.title for r in Resource.query.all()}
        existing_quizzes = {q.title for q in Quiz.query.all()}

        resources_added = 0
        quizzes_added = 0

        for topic in NCERT_TOPICS:
            # Add resource if not exists
            if topic['title'] not in existing_resources:
                filename = f"ncert_g{topic['grade']}_{topic['subject'].replace(' ', '_')}_{topic['title'].replace(' ', '_').replace('/', '_')[:40]}.txt"
                file_path = f"data/resources/{filename}"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(topic['content'])

                file_size = os.path.getsize(file_path)

                resource = Resource(
                    title=topic['title'],
                    description=topic['description'],
                    subject=topic['subject'],
                    grade_level=topic['grade'],
                    content_type='txt',
                    file_path=file_path,
                    file_size=file_size,
                    created_by=teacher.id,
                    is_published=True
                )
                db.session.add(resource)
                resources_added += 1
                print(f"[RES] Grade {topic['grade']} {topic['subject']}: {topic['title']}")

            # Add matching quiz if not exists
            quiz_title = topic['title'] + ' - Quiz'
            if quiz_title not in existing_quizzes:
                quiz = Quiz(
                    title=quiz_title,
                    description=f"Test your knowledge on: {topic['title']}",
                    subject=topic['subject'],
                    grade_level=topic['grade'],
                    created_by=teacher.id,
                    total_questions=len(topic['quiz_questions']),
                    passing_score=60.0,
                    is_published=True
                )
                db.session.add(quiz)
                db.session.flush()

                for idx, q in enumerate(topic['quiz_questions']):
                    question = QuizQuestion(
                        quiz_id=quiz.id,
                        question_text=q['q'],
                        question_type='mcq',
                        option_a=q['a'],
                        option_b=q['b'],
                        option_c=q['c'],
                        option_d=q['d'],
                        correct_option=q['correct'],
                        question_order=idx,
                        marks=1.0
                    )
                    db.session.add(question)

                quizzes_added += 1
                print(f"[QUIZ] Grade {topic['grade']} {topic['subject']}: {quiz_title}")

        db.session.commit()

        print(f"\n========================================")
        print(f"[COMPLETE] Loaded NCERT content:")
        print(f"  Resources added: {resources_added}")
        print(f"  Quizzes added:   {quizzes_added}")
        print(f"  Total resources: {Resource.query.count()}")
        print(f"  Total quizzes:   {Quiz.query.count()}")
        print(f"========================================")


if __name__ == '__main__':
    try:
        load_all_content()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
