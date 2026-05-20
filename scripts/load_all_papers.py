"""
Comprehensive Question Papers Loader
Adds previous year question papers for ALL grades 1-10
Multiple subjects per grade
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, QuestionPaper

ALL_PAPERS = [
    # ==================== GRADE 1 ====================
    {
        'grade': 1, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 60, 'total_marks': 30,
        'title': 'Grade 1 Mathematics Annual 2023',
        'description': 'Annual exam for Class 1 Mathematics',
        'content': '''GRADE 1 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 1 hour
Maximum Marks: 30

Section A - Count and Write (10 marks)

1. Count and write the number:
   (a) 🍎🍎🍎 = ____
   (b) ⭐⭐⭐⭐⭐ = ____
   (c) 🐱🐱🐱🐱🐱🐱🐱 = ____
   (d) ⚽⚽⚽⚽ = ____
   (e) 🌸🌸🌸🌸🌸🌸 = ____

2. Write the missing numbers:
   (a) 1, 2, ___, 4, 5
   (b) 6, 7, 8, ___, 10
   (c) ___, 12, 13, 14
   (d) 15, ___, 17, 18
   (e) 20, ___, 22, 23

Section B - Simple Addition (10 marks)

3. Add:
   (a) 2 + 1 = ___
   (b) 3 + 2 = ___
   (c) 5 + 4 = ___
   (d) 6 + 3 = ___
   (e) 7 + 2 = ___

4. Add the pictures:
   (a) 🍎🍎 + 🍎🍎🍎 = ___
   (b) 🌟 + 🌟🌟🌟🌟 = ___
   (c) 🐱🐱🐱 + 🐱🐱 = ___
   (d) ⚽⚽⚽⚽ + ⚽ = ___
   (e) 🌸🌸🌸🌸🌸🌸 + 🌸🌸 = ___

Section C - Subtraction (5 marks)

5. Subtract:
   (a) 5 - 2 = ___
   (b) 7 - 3 = ___
   (c) 9 - 4 = ___
   (d) 10 - 5 = ___
   (e) 8 - 6 = ___

Section D - Compare Numbers (5 marks)

6. Circle the bigger number:
   (a) 5 or 7
   (b) 9 or 3
   (c) 8 or 4
   (d) 6 or 10
   (e) 2 or 5

WELL DONE!'''
    },
    {
        'grade': 1, 'subject': 'English', 'year': 2023,
        'exam_type': 'annual', 'duration': 60, 'total_marks': 30,
        'title': 'Grade 1 English Annual 2023',
        'description': 'Annual examination for Class 1 English',
        'content': '''GRADE 1 ENGLISH - ANNUAL EXAM
Year: 2023
Time: 1 hour
Maximum Marks: 30

Section A - Alphabet (10 marks)

1. Write the missing letters:
   A, B, ___, D, ___, F, G
   H, I, ___, K, L, ___, N
   O, ___, Q, R, ___, T, U
   V, W, ___, Y, Z

2. Match capital with small letters: (5 marks)
   A      d
   B      a
   C      e
   D      c
   E      b

Section B - Words and Pictures (10 marks)

3. Fill in the blanks (use the words: cat, sun, dog, ball, tree):
   (a) The ___ is yellow.
   (b) A ___ has 4 legs.
   (c) I play with my ___.
   (d) The ___ is tall.
   (e) The ___ says meow.

4. Circle the correct word:
   (a) (Apple / Banana) is red.
   (b) Cats say (Bark / Meow).
   (c) Fish live in (Water / Air).
   (d) Sun rises in the (East / West).
   (e) (One / Five) plus four is five.

Section C - Reading (5 marks)

5. Read and answer:
   "Ram has a dog. The dog is brown. Ram plays with the dog."

   (a) Who has a dog? _______
   (b) What color is the dog? _______

6. Write True or False:
   (a) Birds can fly. (___)
   (b) Fish can walk. (___)
   (c) Sun is hot. (___)

Section D - Writing (5 marks)

7. Write any 5 nouns you see in your classroom:
   1. _____________
   2. _____________
   3. _____________
   4. _____________
   5. _____________

WELL DONE!'''
    },

    # ==================== GRADE 2 ====================
    {
        'grade': 2, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 50,
        'title': 'Grade 2 Mathematics Annual 2023',
        'description': 'Class 2 annual math examination',
        'content': '''GRADE 2 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 1.5 hours
Maximum Marks: 50

Section A - MCQ (1 mark each) - 10 marks

1. What comes after 25?
   (a) 24    (b) 26    (c) 27    (d) 23

2. 5 + 7 = ?
   (a) 11    (b) 12    (c) 13    (d) 14

3. 20 - 8 = ?
   (a) 10    (b) 11    (c) 12    (d) 13

4. Which is bigger: 45 or 54?
   (a) 45    (b) 54    (c) Same    (d) None

5. ₹10 + ₹20 = ?
   (a) ₹10    (b) ₹20    (c) ₹30    (d) ₹40

6. 1 hour = ___ minutes
   (a) 30    (b) 45    (c) 60    (d) 90

7. Which is the heaviest?
   (a) Pencil    (b) Book    (c) Stone    (d) Paper

8. 10 + 10 + 10 = ?
   (a) 20    (b) 30    (c) 40    (d) 10

9. How many days in a week?
   (a) 5    (b) 6    (c) 7    (d) 8

10. Half of 10 = ?
    (a) 2    (b) 4    (c) 5    (d) 7

Section B - Fill in blanks (20 marks)

11. Add:
    (a) 15 + 23 = ___
    (b) 34 + 27 = ___
    (c) 48 + 19 = ___
    (d) 56 + 35 = ___
    (e) 18 + 47 = ___

12. Subtract:
    (a) 45 - 23 = ___
    (b) 60 - 28 = ___
    (c) 73 - 45 = ___
    (d) 88 - 56 = ___
    (e) 90 - 67 = ___

13. Write in words:
    (a) 25 = _______________
    (b) 47 = _______________
    (c) 100 = _______________

14. Multiply:
    (a) 2 × 3 = ___
    (b) 4 × 5 = ___
    (c) 6 × 2 = ___

15. Match the time:
    Morning      6:00 PM
    Afternoon    9:00 PM
    Evening      8:00 AM
    Night        2:00 PM

Section C - Word Problems (15 marks)

16. (3 marks) Anu has 25 candies. Her friend gives her 15 more.
    How many does she have now?

17. (3 marks) There are 40 birds on a tree. 12 birds flew away.
    How many birds are left?

18. (3 marks) A pencil costs ₹10. Find cost of 5 pencils.

19. (3 marks) Ravi has ₹100. He buys a book for ₹65.
    How much money is left?

20. (3 marks) Draw a clock showing 3 o'clock.

Section D - Shapes and Patterns (5 marks)

21. Name these shapes:
    🔵 ____  ⬛ ____  🔺 ____  ⬜ ____  ⚪ ____

ALL THE BEST!'''
    },
    {
        'grade': 2, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 60, 'total_marks': 40,
        'title': 'Grade 2 Science Annual 2023',
        'description': 'Class 2 annual science examination',
        'content': '''GRADE 2 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 1 hour
Maximum Marks: 40

Section A - MCQ (1 mark each) - 10 marks

1. Plants give us:
   (a) Light    (b) Oxygen    (c) Sound    (d) Music

2. Which is a fruit?
   (a) Potato    (b) Carrot    (c) Apple    (d) Onion

3. Cow eats:
   (a) Meat    (b) Grass    (c) Fish    (d) Stone

4. Birds can:
   (a) Swim    (b) Fly    (c) Crawl    (d) Run only

5. We use ___ to see:
   (a) Ears    (b) Eyes    (c) Nose    (d) Tongue

6. Water is:
   (a) Solid    (b) Liquid    (c) Gas    (d) Stone

7. Which is hot?
   (a) Ice    (b) Sun    (c) Snow    (d) Water

8. Sun rises in the:
   (a) North    (b) South    (c) East    (d) West

9. Trees grow from:
   (a) Stones    (b) Seeds    (c) Water    (d) Air

10. Honey comes from:
    (a) Cow    (b) Bees    (c) Tree    (d) Sun

Section B - Match (10 marks)

11. Match the animals with their food:
    Lion        Grass
    Cow         Meat
    Cat         Fish
    Rabbit      Milk
    Bee         Carrot

12. Match the body parts:
    Eyes        Smell
    Ears        See
    Nose        Hear
    Tongue      Touch
    Skin        Taste

Section C - Fill in blanks (10 marks)

13. _____ is the source of light during the day.
14. _____ shines at night.
15. We breathe through our _____.
16. Plants need _____, water, and air.
17. There are _____ seasons in India.
18. _____ is a baby of a cow.
19. The opposite of hot is _____.
20. We need food to get _____.
21. Honey is made by _____.
22. _____ are needed to fly a kite.

Section D - Short Answer (10 marks)

23. (2 marks) Name any 3 animals.
24. (2 marks) Name any 3 fruits.
25. (2 marks) Name any 3 vegetables.
26. (2 marks) Why do we need water?
27. (2 marks) What do plants need to grow?

ALL THE BEST!'''
    },
    {
        'grade': 2, 'subject': 'English', 'year': 2023,
        'exam_type': 'annual', 'duration': 60, 'total_marks': 40,
        'title': 'Grade 2 English Annual 2023',
        'description': 'Class 2 annual English examination',
        'content': '''GRADE 2 ENGLISH - ANNUAL EXAM
Year: 2023
Time: 1 hour
Maximum Marks: 40

Section A - Reading (10 marks)

Read the passage:
"Lily is a girl. She has a red hat. She has a yellow bag. Lily likes to go to school. She has a friend named Mona. They play together in the park. They are happy."

Answer:
1. What is the girl's name? ____
2. What color is her hat? ____
3. What color is her bag? ____
4. Who is her friend? ____
5. Where do they play? ____

Section B - Grammar (10 marks)

6. Fill with a, an, or the:
   (a) ___ apple
   (b) ___ elephant
   (c) ___ cat
   (d) ___ sun
   (e) ___ orange

7. Plural of:
   (a) book = ___
   (b) baby = ___
   (c) toy = ___
   (d) child = ___
   (e) man = ___

Section C - Vocabulary (10 marks)

8. Write opposite (antonyms):
   (a) hot - ___
   (b) big - ___
   (c) day - ___
   (d) good - ___
   (e) up - ___

9. Make sentences using these words:
   (a) Tree
   _______________
   (b) Happy
   _______________
   (c) School
   _______________
   (d) Friend
   _______________
   (e) Garden
   _______________

Section D - Writing (10 marks)

10. (5 marks) Write any 5 sentences about your family.

11. (5 marks) Write your daily routine in 5 sentences.

ALL THE BEST!'''
    },

    # ==================== GRADE 3 ====================
    {
        'grade': 3, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 60,
        'title': 'Grade 3 Mathematics Annual 2023',
        'description': 'Class 3 annual mathematics examination',
        'content': '''GRADE 3 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 1.5 hours
Maximum Marks: 60

Section A - MCQ (1 mark each) - 10 marks

1. 245 + 134 = ?
   (a) 369    (b) 379    (c) 389    (d) 399

2. 7 × 8 = ?
   (a) 49    (b) 54    (c) 56    (d) 63

3. 36 ÷ 6 = ?
   (a) 4    (b) 5    (c) 6    (d) 7

4. 1 km = ___ m
   (a) 100    (b) 500    (c) 1000    (d) 10000

5. Half of 50 = ?
   (a) 20    (b) 25    (c) 30    (d) 35

6. How many corners in a square?
   (a) 2    (b) 3    (c) 4    (d) 5

7. 9 × 9 = ?
   (a) 72    (b) 81    (c) 90    (d) 99

8. What is 1/2?
   (a) Half    (b) Quarter    (c) Whole    (d) Third

9. Greatest 3-digit number:
   (a) 100    (b) 500    (c) 999    (d) 1000

10. 1 hour = ___ minutes
    (a) 30    (b) 45    (c) 60    (d) 90

Section B - Fill in blanks (15 marks)

11. (3 marks) Add:
    (a) 234 + 567 = ___
    (b) 845 + 137 = ___
    (c) 478 + 286 = ___

12. (3 marks) Subtract:
    (a) 678 - 234 = ___
    (b) 900 - 345 = ___
    (c) 1000 - 478 = ___

13. (3 marks) Multiply:
    (a) 12 × 5 = ___
    (b) 25 × 4 = ___
    (c) 35 × 3 = ___

14. (3 marks) Divide:
    (a) 48 ÷ 6 = ___
    (b) 81 ÷ 9 = ___
    (c) 100 ÷ 10 = ___

15. (3 marks) Fractions:
    (a) 1/2 + 1/2 = ___
    (b) 1/4 + 2/4 = ___
    (c) 3/4 - 1/4 = ___

Section C - Word Problems (20 marks)

16. (4 marks) A book has 250 pages. Ravi read 80 pages.
    How many pages are left?

17. (4 marks) There are 6 boxes of pencils. Each box has 12 pencils.
    How many pencils are there in total?

18. (4 marks) Mom bought 4 dozen bananas. (1 dozen = 12)
    How many bananas?

19. (4 marks) Three friends shared ₹150 equally.
    How much did each get?

20. (4 marks) A train ticket costs ₹85. How much for 7 tickets?

Section D - Geometry & Measurement (15 marks)

21. (3 marks) Find the perimeter:
    Rectangle: length 8 cm, width 5 cm = ___ cm

22. (3 marks) Name these shapes:
    (a) 3 sides = ___
    (b) 4 equal sides = ___
    (c) Round shape = ___

23. (3 marks) Time conversions:
    (a) 2 hours = ___ minutes
    (b) 120 seconds = ___ minutes
    (c) 1 day = ___ hours

24. (3 marks) Measurement:
    (a) 3 kg = ___ g
    (b) 2 L = ___ mL
    (c) 5 m = ___ cm

25. (3 marks) Find:
    (a) ₹100 - ₹65 = ___
    (b) ₹250 + ₹175 = ___
    (c) 5 × ₹25 = ___

ALL THE BEST!'''
    },
    {
        'grade': 3, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 60, 'total_marks': 50,
        'title': 'Grade 3 Science Annual 2023',
        'description': 'Class 3 annual science examination',
        'content': '''GRADE 3 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 1 hour
Maximum Marks: 50

Section A - MCQ (1 mark each) - 10 marks

1. Living things need:
   (a) Food only    (b) Water only    (c) Air only    (d) All of these

2. Stone is:
   (a) Living    (b) Non-living    (c) Growing    (d) Eating

3. Sun gives us:
   (a) Heat and light    (b) Air    (c) Water    (d) Food

4. Plants make food in:
   (a) Roots    (b) Stem    (c) Leaves    (d) Flowers

5. We drink water that is:
   (a) Dirty    (b) Clean    (c) Salty    (d) Muddy

6. Number of states of matter:
   (a) 1    (b) 2    (c) 3    (d) 4

7. Ice is:
   (a) Solid    (b) Liquid    (c) Gas    (d) Plasma

8. Air contains:
   (a) Water    (b) Oxygen    (c) Stone    (d) Food

9. Lion is a:
   (a) Herbivore    (b) Carnivore    (c) Omnivore    (d) None

10. Tigers live in:
    (a) Houses    (b) Forests    (c) Oceans    (d) Schools

Section B - Fill in blanks (10 marks)

11. ___ is the source of light during the day.
12. ___ shines at night.
13. Plants need ___, water, and air.
14. Animals which eat plants are ___.
15. Animals which eat meat are ___.
16. ___ cycle includes evaporation and rain.
17. The ___ is the largest organ of our body.
18. ___ is needed for breathing.
19. We get vitamins from ___.
20. A ___ has roots, stem, and leaves.

Section C - Short Answer (15 marks)

21. (3 marks) What are 3 differences between living and non-living things?

22. (3 marks) Name 3 herbivores, 3 carnivores, and 3 omnivores.

23. (3 marks) Why do we need to keep our environment clean?

24. (3 marks) Name the parts of a plant.

25. (3 marks) What are the 3 states of water?

Section D - Long Answer (15 marks)

26. (5 marks) Draw and label parts of a plant.

27. (5 marks) Write 5 ways to save water.

28. (5 marks) Explain the water cycle in your own words.

ALL THE BEST!'''
    },

    # ==================== GRADE 4 ====================
    {
        'grade': 4, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 70,
        'title': 'Grade 4 Mathematics Annual 2023',
        'description': 'Class 4 annual mathematics exam',
        'content': '''GRADE 4 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 1.5 hours
Maximum Marks: 70

Section A - MCQ (1 mark each) - 10 marks

1. 5678 + 2345 = ?
   (a) 7923    (b) 8023    (c) 8123    (d) 8223

2. 1/4 of 80 = ?
   (a) 15    (b) 20    (c) 25    (d) 40

3. 144 ÷ 12 = ?
   (a) 10    (b) 11    (c) 12    (d) 13

4. Largest 4-digit number:
   (a) 1000    (b) 9999    (c) 9990    (d) 10000

5. 1/2 = ?
   (a) 0.2    (b) 0.5    (c) 0.25    (d) 0.75

6. Perimeter of square (side=6):
   (a) 12    (b) 24    (c) 36    (d) 48

7. Area of rectangle 5×4:
   (a) 9    (b) 18    (c) 20    (d) 25

8. 30% as fraction:
   (a) 3/10    (b) 3/100    (c) 1/3    (d) 30/1000

9. 3 hours 30 min = ___ min
   (a) 180    (b) 210    (c) 240    (d) 270

10. (-3) + 5 = ?
    (a) 8    (b) 2    (c) -2    (d) -8

Section B - Short Answer (3 marks each) - 30 marks

11. Add: 4567 + 2895 + 1234

12. Subtract: 8000 - 3456

13. Multiply: 245 × 8

14. Divide: 432 ÷ 9

15. Convert to decimal: 3/4

16. Add fractions: 1/4 + 1/3

17. Convert: 5 km = ___ m

18. Find LCM of 4 and 6

19. Find HCF of 12 and 18

20. Round 4567 to nearest 100

Section C - Word Problems (20 marks)

21. (5 marks) A factory makes 350 cars in a day.
    (a) How many in a week?
    (b) How many in 30 days?

22. (5 marks) A field is 80m long and 50m wide.
    (a) Find perimeter.
    (b) Find area.
    (c) Cost of fencing at ₹15/m

23. (5 marks) Ravi saved ₹500 every month.
    (a) How much in 1 year?
    (b) If he spent ₹2000, how much left after 1 year?

24. (5 marks) A bus travels 240 km in 4 hours.
    (a) Find speed.
    (b) Find time for 360 km at same speed.

Section D - Geometry (10 marks)

25. (5 marks) Draw a rectangle 6 cm × 4 cm.
    Find its perimeter and area.

26. (5 marks) Name and define:
    (a) Right angle
    (b) Acute angle
    (c) Obtuse angle

ALL THE BEST!'''
    },
    {
        'grade': 4, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 60,
        'title': 'Grade 4 Science Annual 2023',
        'description': 'Class 4 annual science examination',
        'content': '''GRADE 4 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 1.5 hours
Maximum Marks: 60

Section A - MCQ (1 mark each) - 10 marks

1. Carbohydrates give us:
   (a) Growth    (b) Energy    (c) Beauty    (d) Sleep

2. Vitamin C is found in:
   (a) Rice    (b) Oranges    (c) Oil    (d) Bread

3. Lack of iron causes:
   (a) Scurvy    (b) Anemia    (c) Rickets    (d) Goitre

4. Plants need ___ for photosynthesis:
   (a) Moonlight    (b) Sunlight    (c) Darkness    (d) Wind

5. Earth rotates in:
   (a) 12 hrs    (b) 24 hrs    (c) 365 days    (d) 1 month

6. Source of calcium:
   (a) Milk    (b) Oil    (c) Sugar    (d) Salt

7. Which is renewable?
   (a) Coal    (b) Petrol    (c) Solar    (d) Gas

8. Largest organ in human body:
   (a) Heart    (b) Liver    (c) Skin    (d) Brain

9. Bee gives us:
   (a) Milk    (b) Wool    (c) Honey    (d) Silk

10. Salt is obtained from:
    (a) Mountains    (b) Sea water    (c) Rain water    (d) Wells

Section B - Fill in blanks (10 marks)

11. ___ is the largest planet in our solar system.
12. ___ is the closest planet to the Sun.
13. Plants give out ___ in the day.
14. We get vitamins from ___.
15. ___ helps us digest food.
16. Earth revolves around ___.
17. ___ keeps us standing on ground.
18. The ___ is our nearest star.
19. ___ are needed for strong bones.
20. ___ rotation causes day and night.

Section C - Short Answer (3 marks each) - 20 marks (Choose 6-7)

21. What are the main food groups?

22. Name 5 nutrients and their sources.

23. What is the importance of water?

24. Why should we eat fruits and vegetables?

25. Name the parts of a plant.

26. What causes day and night?

27. What is air pollution?

Section D - Long Answer (5 marks each) - 20 marks

28. Draw the human body and label 5 parts.

29. Explain the importance of plants in our life.

30. Write 5 ways to stay healthy.

31. Describe the solar system briefly.

ALL THE BEST!'''
    },

    # ==================== GRADE 6 ====================
    {
        'grade': 6, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 120, 'total_marks': 80,
        'title': 'Grade 6 Mathematics Annual 2023',
        'description': 'Class 6 annual mathematics examination',
        'content': '''GRADE 6 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 2 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 15 marks

1. (-5) + (-3) = ?
   (a) 8    (b) -8    (c) 2    (d) -2

2. LCM of 4, 6 = ?
   (a) 12    (b) 24    (c) 10    (d) 8

3. Smallest prime number:
   (a) 0    (b) 1    (c) 2    (d) 3

4. 3/4 + 1/4 = ?
   (a) 1    (b) 4/4    (c) Both A&B    (d) 3/8

5. 5² = ?
   (a) 10    (b) 25    (c) 32    (d) 50

6. Area of square (side=7):
   (a) 14    (b) 28    (c) 49    (d) 56

7. 50% of 200:
   (a) 50    (b) 75    (c) 100    (d) 150

8. Acute angle is:
   (a) >90°    (b) =90°    (c) <90°    (d) =180°

9. Integers include:
   (a) Positive only    (b) Negative only    (c) Both & zero    (d) Fractions

10. HCF of 12, 18 = ?
    (a) 4    (b) 6    (c) 8    (d) 12

11. Cube of 4:
    (a) 16    (b) 32    (c) 64    (d) 128

12. Decimal of 1/5:
    (a) 0.2    (b) 0.5    (c) 1.5    (d) 5

13. Roman numeral L = ?
    (a) 1    (b) 10    (c) 50    (d) 100

14. Perimeter of triangle 3,4,5:
    (a) 7    (b) 10    (c) 12    (d) 15

15. Sum of angles in triangle:
    (a) 90°    (b) 120°    (c) 180°    (d) 360°

Section B - Short Answer (3 marks each) - 24 marks

16. Find: (-12) + 8 - (-5)

17. LCM of 8, 12, 16

18. HCF of 24, 36

19. Add: 2/3 + 3/5

20. Solve: x + 7 = 20

21. Cost of 8 pens at ₹15 each

22. 20% of 250

23. Area of triangle base=8, height=6

Section C - Long Answer (5 marks each) - 25 marks

24. A man earns ₹15000 monthly. He spends ₹12000.
    (a) Monthly savings?
    (b) Yearly savings?

25. Find: HCF and LCM of 24, 36

26. Solve: 2x - 5 = 11. Verify your answer.

27. Distance from school to home is 3 km. If Ravi walks both ways,
    how much does he walk in a week?

28. The angles of triangle are 60°, 80°, ?
    Find third angle.

Section D - Application (16 marks)

29. (8 marks) Geometry construction:
    (a) Draw a circle with radius 4 cm
    (b) Find its diameter
    (c) Find its circumference (use π=22/7)
    (d) Find its area

30. (8 marks) Data Handling:
    Marks in 5 subjects: 80, 75, 85, 90, 70
    Find:
    (a) Mean
    (b) Median
    (c) Mode
    (d) Range

ALL THE BEST!'''
    },
    {
        'grade': 6, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 120, 'total_marks': 80,
        'title': 'Grade 6 Science Annual 2023',
        'description': 'Class 6 annual science examination',
        'content': '''GRADE 6 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 2 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 15 marks

1. Carbohydrates give us:
   (a) Growth    (b) Energy    (c) Beauty    (d) Sleep

2. Source of Vitamin C:
   (a) Rice    (b) Oranges    (c) Oil    (d) Bread

3. Lack of iodine causes:
   (a) Anemia    (b) Goitre    (c) Scurvy    (d) Rickets

4. Largest planet:
   (a) Earth    (b) Mars    (c) Jupiter    (d) Saturn

5. Heart has:
   (a) 1 chamber    (b) 2 chambers    (c) 3 chambers    (d) 4 chambers

6. Photosynthesis happens in:
   (a) Root    (b) Stem    (c) Leaf    (d) Flower

7. We breathe out:
   (a) Oxygen    (b) Carbon dioxide    (c) Nitrogen    (d) Hydrogen

8. Plasma is the:
   (a) 1st state    (b) 2nd state    (c) 3rd state    (d) 4th state of matter

9. Stomata are found in:
   (a) Root    (b) Stem    (c) Leaves    (d) Fruits

10. Light travels in:
    (a) Curves    (b) Circles    (c) Straight lines    (d) Spirals

11. Compass needle points:
    (a) East    (b) West    (c) North    (d) South

12. Insulator is:
    (a) Copper    (b) Iron    (c) Wood    (d) Aluminum

13. Friction between:
    (a) Air    (b) Water    (c) Surfaces in contact    (d) Light

14. Pressure unit:
    (a) Newton    (b) Pascal    (c) Joule    (d) Watt

15. Magnet attracts:
    (a) Plastic    (b) Wood    (c) Iron    (d) Paper

Section B - Short Answer (3 marks each) - 24 marks

16. Name 5 nutrients and their sources.

17. Difference between aerobic and anaerobic respiration.

18. Define: Light, Sound, Heat.

19. What is balanced diet?

20. Draw a plant cell and label parts.

21. Name parts of digestive system.

22. What is photosynthesis equation?

23. Name 5 environmental problems.

Section C - Long Answer (5 marks each) - 30 marks

24. Explain different types of motion with examples.

25. Describe water cycle with diagram.

26. Explain the importance of forests.

27. What are the 8 planets in solar system?

28. Difference between solid, liquid, and gas.

29. Describe the human digestive system.

Section D - Application (11 marks)

30. (5 marks) Why are renewable resources important?
    Give 3 examples.

31. (6 marks) Look at the table:
    Tomato: Red color, Sour taste, Round shape

    (a) What sense organ detects taste?
    (b) Why does tomato look red?
    (c) Name another sour food.
    (d) Is tomato a fruit or vegetable? Why?

ALL THE BEST!'''
    },

    # ==================== GRADE 9 ====================
    {
        'grade': 9, 'subject': 'Mathematics', 'year': 2023,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 9 Mathematics Annual 2023',
        'description': 'Class 9 annual mathematics exam',
        'content': '''GRADE 9 MATHEMATICS - ANNUAL EXAM
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 20 marks

1. √2 is:
   (a) Rational    (b) Irrational    (c) Integer    (d) Natural

2. Degree of polynomial 3x² + 5x + 1:
   (a) 0    (b) 1    (c) 2    (d) 3

3. Coordinates of origin:
   (a) (1,0)    (b) (0,1)    (c) (0,0)    (d) (1,1)

4. y = 2x + 3, slope = ?
   (a) 1    (b) 2    (c) 3    (d) 5

5. (a+b)² = ?
   (a) a²+b²    (b) a²-b²    (c) a²+2ab+b²    (d) a²-2ab+b²

6. p(x) = x² - 4, p(2) = ?
   (a) 0    (b) 2    (c) 4    (d) 8

7. Distance from (0,0) to (3,4):
   (a) 4    (b) 5    (c) 6    (d) 7

8. Area of triangle with sides 3,4,5:
   (a) 6    (b) 7    (c) 12    (d) 15

9. Volume of sphere = ?
   (a) πr²    (b) (4/3)πr³    (c) (1/3)πr²h    (d) πr²h

10. Mean of 5,8,10,12,15:
    (a) 8    (b) 9    (c) 10    (d) 11

11. Probability range:
    (a) 0 to 1    (b) 1 to 10    (c) 0 to 10    (d) Any value

12. Sum of angles of polygon:
    (a) 180°    (b) 360°    (c) (n-2)×180°    (d) n×180°

13. Heron's formula uses:
    (a) base & height    (b) sides    (c) angles    (d) None

14. Median is:
    (a) Average    (b) Middle value    (c) Most frequent    (d) Highest

15. Mode is:
    (a) Average    (b) Middle    (c) Most frequent    (d) Lowest

16. SI unit of area:
    (a) m    (b) m²    (c) m³    (d) cm

17. 1 hectare = ?
    (a) 100 m²    (b) 10,000 m²    (c) 1,00,000 m²    (d) 1 km²

18. Number of irrational numbers between 2 rationals:
    (a) 1    (b) 2    (c) Infinite    (d) None

19. Angle in semicircle:
    (a) 30°    (b) 45°    (c) 60°    (d) 90°

20. Cyclic quadrilateral opposite angles sum:
    (a) 90°    (b) 180°    (c) 270°    (d) 360°

Section B - Very Short Answer (2 marks each) - 12 marks

21. Express 0.625 as fraction.

22. Find p(2) if p(x) = x³ - 2x + 5.

23. Plot points (3, 4) and (-2, 1) on graph.

24. Volume of cylinder with r=7, h=10.

25. Find mean of 12, 14, 16, 18, 20.

26. Find probability of getting 6 on die.

Section C - Short Answer (3 marks each) - 18 marks

27. Find: HCF of 96, 404.

28. Factorize: x² - 16

29. Solve: 3x + y = 7, x + y = 3

30. Find area of triangle with sides 13, 14, 15 using Heron's formula.

31. Probability of getting King from deck of 52 cards.

32. Distance and midpoint between (1,2) and (5,8).

Section D - Long Answer (5 marks each) - 30 marks

33. Prove √2 is irrational.

34. Factorize: x³ - 8

35. Find surface area and volume of:
    (a) Cube with side 5 cm
    (b) Sphere with radius 7 cm

36. Mean of 6 numbers is 8. If a new number is added, mean becomes 9.
    Find the new number.

37. Prove: If two chords are equal, they are equidistant from center.

38. Construct triangle ABC where AB = 6cm, BC = 4cm, AC = 5cm.
    Find its area using Heron's formula.

ALL THE BEST!'''
    },
    {
        'grade': 9, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 9 Science Annual 2023',
        'description': 'Class 9 annual science examination',
        'content': '''GRADE 9 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 20 marks

1. Number of states of matter:
   (a) 2    (b) 3    (c) 4    (d) 5

2. Boiling point of water:
   (a) 50°C    (b) 75°C    (c) 100°C    (d) 150°C

3. SI unit of mass:
   (a) g    (b) kg    (c) lb    (d) ton

4. SI unit of force:
   (a) Pascal    (b) Newton    (c) Joule    (d) Watt

5. Density formula:
   (a) M×V    (b) M/V    (c) V/M    (d) M+V

6. Plant cell has:
   (a) No nucleus    (b) Cell wall    (c) No vacuole    (d) Plasma membrane only

7. Smallest unit of life:
   (a) Tissue    (b) Cell    (c) Organ    (d) Atom

8. SI unit of work:
   (a) Newton    (b) Pascal    (c) Joule    (d) Watt

9. Cell discovered by:
   (a) Newton    (b) Robert Hooke    (c) Einstein    (d) Edison

10. Acceleration unit:
    (a) m/s    (b) m/s²    (c) m²/s    (d) s/m

11. Tissue is:
    (a) Single cell    (b) Group of similar cells    (c) Organ    (d) System

12. Mitochondria is:
    (a) Power house    (b) Brain    (c) Food maker    (d) Garbage

13. Nucleus controls:
    (a) Movement    (b) All cell activities    (c) Reproduction only    (d) Nothing

14. Photosynthesis happens in:
    (a) Mitochondria    (b) Chloroplast    (c) Nucleus    (d) Vacuole

15. Newton's 1st law:
    (a) F=ma    (b) Inertia    (c) Action-Reaction    (d) Gravity

16. Diversity in living organisms:
    (a) Biodiversity    (b) Geography    (c) Cells    (d) Tissues

17. Conservation of mass:
    (a) Mass can be created    (b) Mass can be destroyed    (c) Mass cannot be created/destroyed    (d) None

18. SI unit of pressure:
    (a) Newton    (b) Pascal    (c) Joule    (d) Watt

19. Sound travels fastest in:
    (a) Air    (b) Water    (c) Solid    (d) Vacuum

20. Universal donor blood group:
    (a) A    (b) B    (c) AB    (d) O

Section B - Very Short Answer (2 marks each) - 12 marks

21. Define matter and state.

22. Define cell. Who discovered it?

23. State Newton's 2nd law.

24. Difference between mass and weight.

25. Name 3 types of plant tissues.

26. What is biological classification?

Section C - Short Answer (3 marks each) - 18 marks

27. Define states of matter with examples.

28. Difference between plant cell and animal cell.

29. State Newton's three laws of motion.

30. Define and explain: Work and Energy.

31. Different types of animal tissues.

32. Importance of biodiversity.

Section D - Long Answer (5 marks each) - 30 marks

33. Describe characteristics of solid, liquid, and gas.

34. Draw a labeled diagram of plant cell.

35. Explain Newton's laws with real-life examples.

36. Describe the structure and function of:
    (a) Mitochondria
    (b) Ribosomes
    (c) Endoplasmic Reticulum

37. Calculate force when 5 kg object accelerates at 2 m/s².
    Also calculate work done if moved 10 m.

38. Discuss conservation of natural resources. Why important?
    Suggest ways.

ALL THE BEST!'''
    },

    # ==================== GRADE 7 SCIENCE ====================
    {
        'grade': 7, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 150, 'total_marks': 80,
        'title': 'Grade 7 Science Annual 2023',
        'description': 'Class 7 annual science examination',
        'content': '''GRADE 7 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 2.5 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 15 marks

1. Lemon is:
   (a) Acid    (b) Base    (c) Salt    (d) Neutral

2. pH of pure water:
   (a) 0    (b) 7    (c) 10    (d) 14

3. Wind is moving:
   (a) Water    (b) Air    (c) Sand    (d) Stone

4. Plants prepare food using:
   (a) Light    (b) Sound    (c) Magnet    (d) Cold

5. Animals which eat plants:
   (a) Carnivores    (b) Herbivores    (c) Omnivores    (d) Saprophytes

6. Forest fires destroy:
   (a) Plants    (b) Animals    (c) Both    (d) Neither

7. Cotton plant gives us:
   (a) Wool    (b) Silk    (c) Cotton fabric    (d) Leather

8. Heat travels in solid by:
   (a) Conduction    (b) Convection    (c) Radiation    (d) None

9. Sweating cools us because:
   (a) Water absorbs heat    (b) Air is cold    (c) Sun is hidden    (d) None

10. Sun light contains:
    (a) 1 color    (b) 3 colors    (c) 5 colors    (d) 7 colors

11. Acid + Base = ?
    (a) Water    (b) Salt    (c) Both    (d) Gas

12. Photosynthesis byproduct:
    (a) Carbon dioxide    (b) Oxygen    (c) Water    (d) Nitrogen

13. Spider belongs to:
    (a) Insects    (b) Arachnids    (c) Reptiles    (d) Mammals

14. Lightning is:
    (a) Sound    (b) Heat    (c) Light    (d) All

15. Soil layer with humus:
    (a) Top soil    (b) Sub soil    (c) Bed rock    (d) Sand

Section B - Short Answer (3 marks each) - 30 marks

16. Difference between acid and base. Give 2 examples each.

17. What is balanced diet? List 5 essential nutrients.

18. Explain photosynthesis with chemical equation.

19. Difference between herbivores, carnivores, and omnivores.

20. What is forest? Why is it important?

21. Explain types of fibers: natural and synthetic.

22. Differences between solid, liquid, and gas.

23. What is heat? How does it transfer?

24. Reflection and refraction of light.

25. What are renewable and non-renewable resources?

Section C - Long Answer (5 marks each) - 20 marks

26. Describe water cycle with diagram.

27. Explain the importance of soil and types of soil.

28. Describe respiration in plants and animals.

29. Write about pollution: types, causes, and prevention.

Section D - Application (15 marks)

30. (5 marks) An experiment shows acid changes blue litmus to red.
    Tell which substances acids, bases, neutrals:
    Vinegar, Soap, Salt water, Lemon juice, Sodium hydroxide

31. (5 marks) Plants need:
    Water, Sunlight, Carbon dioxide, Chlorophyll
    Explain what happens if any is missing.

32. (5 marks) Suggest 5 ways to prevent water pollution
    and explain importance of water conservation.

ALL THE BEST!'''
    },

    # ==================== GRADE 8 SCIENCE ====================
    {
        'grade': 8, 'subject': 'Science', 'year': 2023,
        'exam_type': 'annual', 'duration': 180, 'total_marks': 80,
        'title': 'Grade 8 Science Annual 2023',
        'description': 'Class 8 annual science exam',
        'content': '''GRADE 8 SCIENCE - ANNUAL EXAM
Year: 2023
Time: 3 hours
Maximum Marks: 80

Section A - MCQ (1 mark each) - 20 marks

1. SI unit of force:
   (a) Pascal    (b) Newton    (c) Joule    (d) Watt

2. Pressure = ?
   (a) Force × Area    (b) Force / Area    (c) Mass × Force    (d) None

3. Friction opposes:
   (a) Force    (b) Motion    (c) Weight    (d) Mass

4. Sound travels in:
   (a) Vacuum    (b) Air    (c) Solid    (d) All except vacuum

5. Pitch of sound depends on:
   (a) Amplitude    (b) Frequency    (c) Volume    (d) Distance

6. Hertz unit of:
   (a) Sound    (b) Frequency    (c) Distance    (d) Volume

7. Coal is:
   (a) Renewable    (b) Non-renewable    (c) Both    (d) Plant

8. Reproduction in flowering plants:
   (a) Asexual    (b) Sexual    (c) Both    (d) None

9. Pollination is by:
   (a) Wind    (b) Insects    (c) Water    (d) All

10. Pollination + fertilization = ?
    (a) Pollen    (b) Seed    (c) Fruit    (d) Flower

11. Stem cuttings of plants:
    (a) Stem reproduction    (b) Leaf reproduction    (c) Root    (d) Pollen

12. Glass is good:
    (a) Conductor    (b) Insulator    (c) Magnet    (d) Acid

13. Synthetic fibre:
    (a) Cotton    (b) Wool    (c) Nylon    (d) Silk

14. Material gets attracted to magnet:
    (a) Magnetic material    (b) Non-magnetic    (c) Insulator    (d) Conductor

15. Saturated solution:
    (a) Cannot dissolve more    (b) Always full    (c) Pure water    (d) Solid

16. Speed of light:
    (a) 300 km/s    (b) 3,00,000 km/s    (c) 3,000 km/s    (d) 30,000 km/s

17. Pendulum movement is:
    (a) Linear    (b) Periodic    (c) Random    (d) None

18. Tornado is:
    (a) Wave    (b) Wind storm    (c) Rain    (d) Earthquake

19. Fossil fuel:
    (a) Wood    (b) Coal    (c) Solar    (d) Wind

20. Pollution from car exhaust:
    (a) Water    (b) Soil    (c) Air    (d) Sound

Section B - Short Answer (3 marks each) - 24 marks

21. State Pascal's law of pressure.

22. Explain echo with example.

23. Renewable vs non-renewable resources with examples.

24. Asexual reproduction methods.

25. Difference: pollination vs fertilization.

26. What is friction? Types.

27. Properties of metals.

28. Air pollution causes and effects.

Section C - Long Answer (5 marks each) - 20 marks

29. Newton's three laws of motion with examples.

30. Difference: sound and light waves.

31. Reproduction in plants: sexual vs asexual.

32. Why we should conserve fossil fuels?
    Suggest 5 ways.

Section D - Application (16 marks)

33. (8 marks) Calculate pressure if force is 50N and area 2 m².
    What if same force on 0.5 m²?
    Why nail is pointed?

34. (8 marks) An echo is heard 2 seconds after sound made.
    If sound speed is 340 m/s, find distance to wall.
    Why we use echolocation? Give example.

ALL THE BEST!'''
    },

    # ==================== GRADE 5 ENGLISH ====================
    {
        'grade': 5, 'subject': 'English', 'year': 2023,
        'exam_type': 'annual', 'duration': 90, 'total_marks': 60,
        'title': 'Grade 5 English Annual 2023',
        'description': 'Class 5 annual English examination',
        'content': '''GRADE 5 ENGLISH - ANNUAL EXAM
Year: 2023
Time: 1.5 hours
Maximum Marks: 60

Section A - Reading (15 marks)

Read the passage:
"The Indian peacock is the national bird of India. It has beautiful feathers in blue, green, and gold. The male peacock spreads its feathers during the rainy season. This is called the 'peacock dance'. Peacocks live in forests and parks. They eat seeds, insects, and small reptiles. The peacock is also a symbol of beauty and grace."

Answer:
1. What is the national bird of India? (2 marks)

2. Describe the peacock's feathers. (2 marks)

3. When does the peacock spread its feathers? (2 marks)

4. What is this called? (1 mark)

5. Where do peacocks live? (2 marks)

6. What do peacocks eat? (3 marks)

7. What does the peacock symbolize? (3 marks)

Section B - Grammar (20 marks)

8. (5 marks) Fill in the correct verb form:
   (a) She _____ (go) to school every day.
   (b) They _____ (play) cricket yesterday.
   (c) We _____ (eat) dinner now.
   (d) I _____ (read) a book.
   (e) He _____ (write) a letter tomorrow.

9. (5 marks) Change the tense:
   (a) Past of "see" = ____
   (b) Past of "go" = ____
   (c) Past of "eat" = ____
   (d) Past of "do" = ____
   (e) Past of "come" = ____

10. (5 marks) Articles (a, an, the):
    (a) ___ apple is red.
    (b) Sun rises in ___ east.
    (c) She is ___ honest girl.
    (d) ___ orange is sweet.
    (e) I saw ___ elephant.

11. (5 marks) Pronouns - Replace nouns:
    (a) Ravi went to school. (He / She)
    (b) Sita is my friend. (He / She)
    (c) The dog is sleeping. (It / He)
    (d) Books are useful. (They / It)
    (e) Mom is cooking. (She / He)

Section C - Vocabulary (10 marks)

12. (5 marks) Antonyms:
    (a) tall ↔ ____
    (b) day ↔ ____
    (c) happy ↔ ____
    (d) come ↔ ____
    (e) hot ↔ ____

13. (5 marks) Synonyms:
    (a) big = ____
    (b) small = ____
    (c) fast = ____
    (d) happy = ____
    (e) start = ____

Section D - Writing (15 marks)

14. (5 marks) Write a paragraph about "My Favorite Game."

15. (5 marks) Write a letter to your friend about your summer vacation.

16. (5 marks) Story: Complete the story in 5-6 sentences:
    "One day a thirsty crow was flying. He saw a pot of water, but..."

ALL THE BEST!'''
    },
]


def load_all_papers():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found.")
            return

        os.makedirs('./data/question_papers', exist_ok=True)

        existing_papers = {p.title for p in QuestionPaper.query.all()}
        added = 0
        skipped = 0

        for paper_data in ALL_PAPERS:
            if paper_data['title'] in existing_papers:
                skipped += 1
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
            added += 1
            print(f"[ADDED] Grade {paper_data['grade']} {paper_data['subject']} {paper_data['year']}")

        db.session.commit()

        print(f"\n========================================")
        print(f"[COMPLETE]")
        print(f"  Papers added: {added}")
        print(f"  Papers skipped (already existed): {skipped}")
        print(f"  TOTAL papers in system: {QuestionPaper.query.count()}")

        # Show distribution
        print("\nPapers by Grade:")
        for grade in range(1, 11):
            papers = QuestionPaper.query.filter_by(grade_level=grade).all()
            if papers:
                subjects = list(set(p.subject for p in papers))
                print(f"  Grade {grade}: {len(papers)} papers - {subjects}")

        print(f"========================================")


if __name__ == '__main__':
    try:
        load_all_papers()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
