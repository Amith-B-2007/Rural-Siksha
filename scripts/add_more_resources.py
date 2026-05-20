"""
Add many more comprehensive NCERT resources covering additional topics
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import User, Resource

# YouTube channel mappings (reuse from before)
def get_youtube(title, subject):
    """Get YouTube link for topic"""
    title_lower = title.lower()
    keyword_map = {
        'algebra': ('https://www.youtube.com/watch?v=NybHckSEQBI', 'Khan Academy'),
        'percentage': ('https://www.youtube.com/watch?v=JeVSmq1Nrpw', 'Math Antics'),
        'ratio': ('https://www.youtube.com/watch?v=mvOkMYCABGc', 'Math Antics'),
        'profit': ('https://www.youtube.com/watch?v=JeVSmq1Nrpw', 'Magnet Brains'),
        'interest': ('https://www.youtube.com/watch?v=NCYNXkbTTUw', 'Magnet Brains'),
        'roman': ('https://www.youtube.com/watch?v=qrqj7g0DwHs', 'Magnet Brains'),
        'area': ('https://www.youtube.com/watch?v=AAY1bsazcgM', 'Math Antics'),
        'volume': ('https://www.youtube.com/watch?v=AAY1bsazcgM', 'Math Antics'),
        'perimeter': ('https://www.youtube.com/watch?v=AAY1bsazcgM', 'Math Antics'),
        'light': ('https://www.youtube.com/watch?v=hsXLwsr-aTw', 'Magnet Brains'),
        'sound': ('https://www.youtube.com/watch?v=qV4lR9EWGlY', 'Magnet Brains'),
        'heat': ('https://www.youtube.com/watch?v=ROalU379l3U', 'Magnet Brains'),
        'electricity': ('https://www.youtube.com/watch?v=ru032Mfsfig', 'Magnet Brains'),
        'magnet': ('https://www.youtube.com/watch?v=tFzqAEZnDt8', 'Magnet Brains'),
        'cell': ('https://www.youtube.com/watch?v=URUJD5NEXC8', 'Magnet Brains'),
        'tissue': ('https://www.youtube.com/watch?v=URUJD5NEXC8', 'Magnet Brains'),
        'circulation': ('https://www.youtube.com/watch?v=lXBCpkYrPdU', 'Magnet Brains'),
        'breathing': ('https://www.youtube.com/watch?v=lXBCpkYrPdU', 'Magnet Brains'),
        'digestion': ('https://www.youtube.com/watch?v=MepFD0fS3Cw', 'Magnet Brains'),
        'air': ('https://www.youtube.com/watch?v=K-8t8KMUm6E', 'Magnet Brains'),
        'soil': ('https://www.youtube.com/watch?v=im4HVXMGI68', 'Magnet Brains'),
        'rocks': ('https://www.youtube.com/watch?v=im4HVXMGI68', 'Magnet Brains'),
        'pollution': ('https://www.youtube.com/watch?v=eS2FDBSCqRk', 'Magnet Brains'),
        'forest': ('https://www.youtube.com/watch?v=p3St51F4kE8', 'Magnet Brains'),
        'sentence': ('https://www.youtube.com/watch?v=BIAS0bWZP9I', 'Magnet Brains'),
        'paragraph': ('https://www.youtube.com/watch?v=BELlZKpi1Zs', 'Magnet Brains'),
        'essay': ('https://www.youtube.com/watch?v=A-iLkbdvK_Q', 'Magnet Brains'),
        'preposition': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
        'conjunction': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
        'adverb': ('https://www.youtube.com/watch?v=zUk0FxszZ3M', 'Magnet Brains'),
        'poetry': ('https://www.youtube.com/watch?v=BELlZKpi1Zs', 'Magnet Brains'),
        'civics': ('https://www.youtube.com/watch?v=zXxxqxhWvyM', 'Magnet Brains'),
        'history': ('https://www.youtube.com/watch?v=ZP4ggcG6GgU', 'Magnet Brains'),
        'geography': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Magnet Brains'),
        'maps': ('https://www.youtube.com/watch?v=libKVRa01L8', 'Magnet Brains'),
        'climate': ('https://www.youtube.com/watch?v=eS2FDBSCqRk', 'Magnet Brains'),
        'agriculture': ('https://www.youtube.com/watch?v=p3St51F4kE8', 'Magnet Brains'),
    }
    for kw, (url, ch) in keyword_map.items():
        if kw in title_lower:
            return url, ch
    return 'https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains'


# MANY more NCERT-aligned resources
MORE_RESOURCES = [
    # Grade 1 - More
    {'g': 1, 's': 'Mathematics', 't': 'Money - Coins and Notes',
     'd': 'Learn about Indian coins and currency notes',
     'c': '''MONEY - COINS AND NOTES

What is Money?
Money is what we use to buy things. In India, we use Rupees (Rs.).

Indian Coins:
- 1 Rupee coin
- 2 Rupee coin
- 5 Rupee coin
- 10 Rupee coin

Indian Currency Notes:
- 10 Rupee note
- 20 Rupee note
- 50 Rupee note
- 100 Rupee note
- 200 Rupee note
- 500 Rupee note
- 2000 Rupee note

Counting Money:
- 5 + 5 = 10 rupees
- 10 + 10 = 20 rupees
- 20 + 30 = 50 rupees
- 50 + 50 = 100 rupees

Simple Word Problems:

Problem 1:
Mom has Rs. 50. She gives Rs. 20 to Ravi. How much money is left with Mom?
Answer: 50 - 20 = Rs. 30

Problem 2:
A pencil costs Rs. 5. How much for 4 pencils?
Answer: 5 + 5 + 5 + 5 = Rs. 20

Problem 3:
A toffee is Rs. 2. How many toffees can you buy with Rs. 10?
Answer: 10 / 2 = 5 toffees

Important Points:
- Always count money carefully
- Save money in a piggy bank
- Don't waste money on unnecessary things
- Help parents in shopping'''},

    {'g': 1, 's': 'Social Studies', 't': 'Our Helpers',
     'd': 'Community helpers and their work',
     'c': '''OUR HELPERS

People in our society who help us are called HELPERS or COMMUNITY HELPERS.

Important Community Helpers:

1. DOCTOR
- Treats sick people
- Works in hospitals and clinics
- Wears white coat
- Has a stethoscope

2. TEACHER
- Teaches us in school
- Helps us learn new things
- Tells us stories

3. POLICE
- Catches thieves
- Keeps us safe
- Wears uniform
- Controls traffic

4. POSTMAN
- Delivers letters and parcels
- Wears blue uniform
- Carries a bag

5. FIREMAN
- Stops fire
- Saves people from fire
- Uses water hoses

6. FARMER
- Grows food
- Works in farms
- Gives us rice, wheat, vegetables

7. SHOPKEEPER
- Sells things in shops
- Helps us buy what we need

8. CARPENTER
- Makes furniture from wood
- Uses tools like saw, hammer

9. COBBLER
- Makes and repairs shoes

10. TAILOR
- Makes clothes
- Uses sewing machine

11. BARBER
- Cuts hair
- Works in salon

12. DRIVER
- Drives buses, cars, taxis
- Takes us to places

13. SWEEPER
- Keeps our streets clean
- Very important work

14. ELECTRICIAN
- Fixes electricity problems
- Repairs lights and fans

15. PLUMBER
- Fixes water pipes
- Repairs taps

We should:
- Respect all helpers
- Be polite to them
- Thank them for their work
- Never look down on any job'''},

    # Grade 2 - More
    {'g': 2, 's': 'Science', 't': 'Our Senses',
     'd': 'Five senses and sense organs',
     'c': '''OUR SENSES

We have 5 senses that help us know the world around us.

The Five Senses:

1. SIGHT (Seeing)
   Organ: Eyes
   We use eyes to see colors, shapes, and people.
   Examples: Reading books, watching TV

2. HEARING (Listening)
   Organ: Ears
   We use ears to hear sounds.
   Examples: Music, talking, birds singing

3. SMELL
   Organ: Nose
   We use nose to smell things.
   Examples: Flowers, food, perfume

4. TASTE
   Organ: Tongue
   We use tongue to taste food.
   Four basic tastes:
   - Sweet (sugar, mango)
   - Sour (lemon, tamarind)
   - Bitter (neem, karela)
   - Salty (salt, chips)

5. TOUCH
   Organ: Skin
   We use skin to feel things.
   We can feel:
   - Hot or Cold
   - Soft or Hard
   - Smooth or Rough
   - Wet or Dry

Taking Care of Sense Organs:

For Eyes:
- Don't read in dim light
- Don't watch TV too close
- Eat carrots and green vegetables
- Wash eyes daily

For Ears:
- Don't put anything in ears
- Don't listen to loud sounds
- Keep ears clean and dry

For Nose:
- Don't put fingers in nose
- Cover when sneezing
- Keep clean

For Tongue:
- Clean tongue every day
- Don't eat too hot food
- Brush teeth twice a day

For Skin:
- Take bath daily
- Apply moisturizer in winter
- Use sunscreen
- Wear clean clothes

Activities:

Activity 1: Blindfold Test
Close your eyes and try to identify objects by touch and smell.

Activity 2: Taste Test
Try different foods - identify if sweet, sour, salty, or bitter.

Activity 3: Sound Test
Close eyes and identify different sounds.

Special People:
- Blind people cannot see but their other senses are stronger
- Helen Keller could not see or hear but became a famous writer'''},

    # Grade 3 - More
    {'g': 3, 's': 'Science', 't': 'Air and Water',
     'd': 'Properties and importance of air and water',
     'c': '''AIR AND WATER

AIR

What is Air?
Air is the mixture of gases around us. We cannot see air, but we can feel it.

Properties of Air:
- Has no color
- Has no smell
- Has no taste
- Takes space
- Has weight
- Can be compressed
- Moves from one place to another

Composition of Air:
- 78 percent Nitrogen
- 21 percent Oxygen
- 1 percent Other gases (Carbon dioxide, Water vapor, etc.)

Uses of Air:

1. BREATHING
All living things need air to breathe. We use oxygen.

2. BURNING
Air is needed for fire. Without air, fire goes out.

3. WIND ENERGY
Moving air (wind) is used to run windmills for electricity.

4. PLANTS NEED AIR
Plants use carbon dioxide from air to make food.

5. TRANSPORT
Aeroplanes fly through air.

6. SOUND
Sound travels through air.

7. DRYING
Wet clothes dry in air.

Air Pollution:
- Smoke from factories
- Vehicle exhaust
- Burning of fuels
- Dust

We should:
- Plant more trees
- Use cycles instead of cars
- Don't burn garbage
- Use clean fuels

WATER

What is Water?
Water is the most important liquid for life.

Properties of Water:
- Has no color
- Has no taste
- Has no smell
- Takes shape of container
- Can be solid, liquid, or gas
- Necessary for life

Three Forms of Water:

1. SOLID (Ice)
Below 0 degrees Celsius
Examples: Ice cubes, snow, glaciers

2. LIQUID (Water)
Between 0 and 100 degrees Celsius
Examples: River water, ocean, rain

3. GAS (Water Vapor)
Above 100 degrees Celsius
Invisible gas in air

Sources of Water:

Natural Sources:
- Rivers
- Lakes
- Ponds
- Springs
- Oceans (salty)
- Underground water
- Rain

Made by People:
- Wells
- Hand pumps
- Tube wells
- Dams

Uses of Water:

At Home:
- Drinking
- Cooking
- Bathing
- Washing clothes
- Cleaning house

In Industry:
- Making products
- Cooling machines

In Agriculture:
- Growing crops
- Watering plants

Save Water Tips:
1. Don't leave taps running
2. Fix leaking taps
3. Use bucket for bath (not shower)
4. Reuse vegetable wash water for plants
5. Don't waste water while brushing
6. Collect rainwater

Water Pollution:
- Throwing garbage in rivers
- Factory waste in water
- Sewage water
- Pesticides from farms

Causes of Pollution:
- Diseases
- Death of fish
- Bad smell
- Cannot drink water

Save Water - Save Life!'''},

    # Grade 4 - More
    {'g': 4, 's': 'Mathematics', 't': 'Roman Numerals',
     'd': 'Reading and writing Roman numerals',
     'c': '''ROMAN NUMERALS

What are Roman Numerals?
Roman numerals are a number system used by ancient Romans. They use letters to represent numbers.

Basic Roman Numerals:
- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Numbers 1 to 20:
1 = I
2 = II
3 = III
4 = IV
5 = V
6 = VI
7 = VII
8 = VIII
9 = IX
10 = X
11 = XI
12 = XII
13 = XIII
14 = XIV
15 = XV
16 = XVI
17 = XVII
18 = XVIII
19 = XIX
20 = XX

Bigger Numbers:
30 = XXX
40 = XL
50 = L
60 = LX
70 = LXX
80 = LXXX
90 = XC
100 = C

Rules for Reading Roman Numerals:

Rule 1: When a smaller numeral comes after a larger one, ADD them.
Example: VI = 5 + 1 = 6
Example: XII = 10 + 2 = 12

Rule 2: When a smaller numeral comes before a larger one, SUBTRACT it.
Example: IV = 5 - 1 = 4
Example: IX = 10 - 1 = 9
Example: XL = 50 - 10 = 40

Rule 3: A numeral cannot be repeated more than 3 times.
- III is fine (3)
- IIII is NOT correct (we write IV instead)

Rule 4: V, L, D are NEVER repeated.
- VV is NOT correct (we use X)
- LL is NOT correct (we use C)

Rule 5: Subtract only specific numerals:
- I from V and X only
- X from L and C only
- C from D and M only

Examples to Try:
1. Write 17 in Roman numerals
   17 = 10 + 5 + 2 = X + V + II = XVII

2. Write 49 in Roman numerals
   49 = (50 - 10) + (10 - 1) = XL + IX = XLIX

3. What is XXIV?
   = 10 + 10 + (5 - 1) = 24

4. What is LXXXVIII?
   = 50 + 30 + 8 = 88

Where Roman Numerals are Used:
- Clock faces
- Chapter numbers in books
- Year of movies (sometimes)
- Names of kings (Henry VIII)
- Outline structures
- Watches

Practice:
Write these in Roman numerals:
1. 7 = ?
2. 14 = ?
3. 25 = ?
4. 39 = ?
5. 99 = ?

Answers:
1. VII
2. XIV
3. XXV
4. XXXIX
5. XCIX'''},

    # Grade 5 - More
    {'g': 5, 's': 'Mathematics', 't': 'Profit and Loss',
     'd': 'Calculating profit, loss and percentage',
     'c': '''PROFIT AND LOSS

What is Profit and Loss?
When we buy and sell things, we either make MONEY (profit) or LOSE MONEY (loss).

Key Terms:

COST PRICE (CP):
The price at which an item is bought.

SELLING PRICE (SP):
The price at which an item is sold.

PROFIT:
When SP is more than CP, we make PROFIT.
Profit = SP - CP

LOSS:
When SP is less than CP, we have LOSS.
Loss = CP - SP

Examples:

Example 1: PROFIT
A shopkeeper buys a book for Rs. 50 and sells it for Rs. 75.
- CP = Rs. 50
- SP = Rs. 75
- Profit = SP - CP = 75 - 50 = Rs. 25

Example 2: LOSS
A man buys a watch for Rs. 500 and sells it for Rs. 400.
- CP = Rs. 500
- SP = Rs. 400
- Loss = CP - SP = 500 - 400 = Rs. 100

PROFIT PERCENTAGE:
Profit percent = (Profit / CP) x 100

LOSS PERCENTAGE:
Loss percent = (Loss / CP) x 100

Example 3:
A shopkeeper buys a pen for Rs. 20 and sells for Rs. 25. Find profit percent.
- Profit = 25 - 20 = Rs. 5
- Profit percent = (5 / 20) x 100 = 25 percent

Example 4:
A man buys a toy for Rs. 200 and sells for Rs. 150. Find loss percent.
- Loss = 200 - 150 = Rs. 50
- Loss percent = (50 / 200) x 100 = 25 percent

Finding SP from CP and Profit Percent:
SP = CP + (Profit percent of CP)
or SP = CP x (100 + Profit percent) / 100

Example 5:
CP = Rs. 80, Profit percent = 25 percent. Find SP.
- Profit = 25 percent of 80 = (25/100) x 80 = Rs. 20
- SP = 80 + 20 = Rs. 100

Finding SP from CP and Loss Percent:
SP = CP - (Loss percent of CP)
or SP = CP x (100 - Loss percent) / 100

Example 6:
CP = Rs. 500, Loss percent = 10 percent. Find SP.
- Loss = 10 percent of 500 = (10/100) x 500 = Rs. 50
- SP = 500 - 50 = Rs. 450

Word Problems:

Problem 1:
A fruit seller bought 100 apples for Rs. 500. He sold all for Rs. 700. Find profit and profit percent.

Solution:
- CP = Rs. 500
- SP = Rs. 700
- Profit = 700 - 500 = Rs. 200
- Profit percent = (200/500) x 100 = 40 percent

Problem 2:
A trader bought a TV for Rs. 8000. He sold it for Rs. 7200. Find loss and loss percent.

Solution:
- CP = Rs. 8000
- SP = Rs. 7200
- Loss = 8000 - 7200 = Rs. 800
- Loss percent = (800/8000) x 100 = 10 percent

Important Tips:
- Profit and Loss percentages are always calculated on CP, not SP
- If SP > CP, there is profit
- If SP < CP, there is loss
- If SP = CP, no profit no loss

Discount:
Sometimes shops give DISCOUNT on items.
Discount = Marked Price - Selling Price

Example:
MRP of shirt = Rs. 1000
Discount = 20 percent
Discount amount = 20 percent of 1000 = Rs. 200
SP = 1000 - 200 = Rs. 800

Practice Problems:
1. CP = Rs. 100, SP = Rs. 120. Find profit.
2. CP = Rs. 250, SP = Rs. 200. Find loss percent.
3. Shop offers 25 percent discount on Rs. 400 item. What is new price?
4. A person bought 10 mangoes for Rs. 100 and sold each for Rs. 12. Profit?

Answers:
1. Profit = Rs. 20
2. Loss percent = 20 percent
3. New price = Rs. 300
4. Total SP = 120, Total CP = 100, Profit = Rs. 20'''},

    # Grade 6 - More
    {'g': 6, 's': 'Mathematics', 't': 'Ratio and Proportion',
     'd': 'Understanding ratios and proportions',
     'c': '''RATIO AND PROPORTION

What is a Ratio?
A ratio compares two quantities of the same kind.

Symbol: : (colon)
Example: 2 : 3 (read as "2 is to 3" or "2 ratio 3")

Examples in Daily Life:
- Boys to girls in class
- Salt to sugar in tea
- Time spent studying vs playing

Writing Ratios:
The ratio of a to b is written as a : b or a/b

Example:
If there are 3 boys and 5 girls:
- Ratio of boys to girls = 3 : 5
- Ratio of girls to boys = 5 : 3

EQUIVALENT RATIOS:
Just like equivalent fractions, ratios can be equivalent.

To get equivalent ratios:
- Multiply both terms by same number
- Or divide both terms by same number

Examples:
1 : 2 = 2 : 4 = 3 : 6 = 4 : 8 = 5 : 10
(Multiply both by 2, 3, 4, 5)

10 : 20 = 5 : 10 = 1 : 2
(Divide both by 2 and 10)

SIMPLEST FORM OF RATIO:
Divide both terms by their HCF.

Example: Simplify 12 : 18
HCF of 12 and 18 = 6
12 / 6 = 2
18 / 6 = 3
So 12 : 18 = 2 : 3 (simplest form)

COMPARING RATIOS:
Convert to same denominator (like fractions) to compare.

Example: Compare 2 : 3 and 3 : 4
- 2/3 = 8/12
- 3/4 = 9/12
- Since 9/12 > 8/12, 3 : 4 > 2 : 3

PROPORTION:
A proportion is when two ratios are EQUAL.

Symbol: : :
Example: 2 : 3 : : 4 : 6
(Read as "2 is to 3 as 4 is to 6")

This is true because 2/3 = 4/6

In a Proportion a : b : : c : d:
- a and d are EXTREMES
- b and c are MEANS

Important Rule:
Product of extremes = Product of means
a x d = b x c

Example:
In 2 : 3 : : 4 : 6
- Extremes: 2 and 6, Product = 2 x 6 = 12
- Means: 3 and 4, Product = 3 x 4 = 12
- Both products are equal!

Finding Missing Term:

Example 1:
If 5 : 8 : : x : 32, find x.
Using the rule: 5 x 32 = 8 x x
160 = 8x
x = 160 / 8 = 20

Example 2:
4 : 7 : : 12 : y, find y.
4 x y = 7 x 12
4y = 84
y = 21

UNITARY METHOD:
To find value of many from one or vice versa.

Example 1:
5 pens cost Rs. 100. Find cost of 3 pens.

Solution:
Cost of 5 pens = Rs. 100
Cost of 1 pen = 100 / 5 = Rs. 20
Cost of 3 pens = 20 x 3 = Rs. 60

Example 2:
A car travels 60 km in 1 hour. How far in 3.5 hours?

Solution:
In 1 hour = 60 km
In 3.5 hours = 60 x 3.5 = 210 km

DIRECT PROPORTION:
When two quantities increase together (or decrease together).

Examples:
- More money, more items
- More speed, more distance covered

INVERSE PROPORTION:
When one quantity increases, the other decreases.

Examples:
- More workers, less time
- More speed, less time

DIVIDING IN A RATIO:
Sometimes we divide something in a given ratio.

Example:
Divide Rs. 100 between A and B in the ratio 3 : 2

Solution:
Total parts = 3 + 2 = 5
A gets = (3/5) of 100 = Rs. 60
B gets = (2/5) of 100 = Rs. 40
Total = 60 + 40 = Rs. 100 (check!)

Real-Life Applications:
- Cooking recipes (ingredients in ratio)
- Mixing paints
- Scale of maps
- Photographs (aspect ratio)
- Speed = Distance / Time

Practice Problems:
1. Simplify the ratio 24 : 36
2. Are 4 : 5 and 8 : 10 in proportion?
3. Find x: 6 : 9 : : x : 27
4. Divide Rs. 200 between two friends in ratio 2 : 3

Answers:
1. 2 : 3 (divide by HCF 12)
2. Yes (4 x 10 = 40, 5 x 8 = 40)
3. x = 18 (6 x 27 / 9)
4. Rs. 80 and Rs. 120'''},

    # Grade 7 - More
    {'g': 7, 's': 'Science', 't': 'Heat and Temperature',
     'd': 'Understanding heat, temperature, and thermometer',
     'c': '''HEAT AND TEMPERATURE

What is Heat?
Heat is a form of energy that flows from a HOT object to a COLD object.

Examples:
- Sun heats Earth
- Stove heats food
- Iron heats clothes
- Body heat

Difference between Heat and Temperature:

HEAT:
- Total energy in an object
- Measured in Joules (J) or Calories
- Tells "amount" of energy

TEMPERATURE:
- How hot or cold something is
- Measured in degrees Celsius or Fahrenheit
- Tells "intensity" of heat

THERMOMETER:
An instrument to measure temperature.

Types of Thermometers:

1. CLINICAL THERMOMETER
- Used to measure body temperature
- Range: 35 to 42 degrees Celsius
- Normal body temperature: 37 degrees Celsius or 98.6 F
- Has a kink (bend) to keep reading

2. LABORATORY THERMOMETER
- Used in science labs
- Range: -10 to 110 degrees Celsius
- No kink

3. DIGITAL THERMOMETER
- Shows temperature on display
- Quick and accurate

4. INFRARED THERMOMETER
- No need to touch
- Used during COVID

Scales of Temperature:

1. CELSIUS Scale
- Most commonly used
- Water freezes at 0 degree Celsius
- Water boils at 100 degree Celsius

2. FAHRENHEIT Scale
- Used in some countries (USA)
- Water freezes at 32 F
- Water boils at 212 F

3. KELVIN Scale
- Used in science
- Absolute zero = -273.15 C = 0 K

How to Use a Thermometer:

1. Wash thermometer
2. Shake to bring mercury below 35 C
3. Place under tongue (or armpit)
4. Wait for 1-2 minutes
5. Read the temperature
6. Note down

Transfer of Heat:

Heat travels in 3 ways:

1. CONDUCTION
- Heat flows through SOLIDS
- Particles vibrate and pass heat
- Example: Spoon in hot tea gets hot
- Metals are good conductors
- Wood, plastic are bad conductors (insulators)

2. CONVECTION
- Heat flows through LIQUIDS and GASES
- Particles move and carry heat
- Example: Boiling water, breeze
- Sea breeze, land breeze

3. RADIATION
- Heat flows WITHOUT any medium
- Even through vacuum
- Example: Heat from Sun
- Heat from fire

Conductors and Insulators:

GOOD CONDUCTORS of heat:
- Iron, copper, aluminum
- All metals
- Water (slow)
- Used in: cooking utensils, soldering

POOR CONDUCTORS (Insulators):
- Wood
- Plastic
- Rubber
- Glass
- Air
- Used in: handles of utensils, winter clothes

Daily Uses:

Pressure cooker handles - wood/plastic
Water heaters - copper inside
Winter clothes - wool (traps air)
Hot water bottles - rubber
House walls - mud, brick

Effects of Heat:

1. Change of State
Solid melts to liquid
Liquid evaporates to gas

2. Expansion
Most things expand when heated
- Iron tracks have gaps
- Bridges have rollers

3. Chemical Changes
- Cooking
- Burning
- Reactions

Why we wear cotton in summer:
- Cotton is light
- Allows heat to escape
- Light colors reflect sun's heat

Why we wear wool in winter:
- Wool traps air
- Air is bad conductor
- Keeps body heat in

Land and Sea Breeze:

DAY (Sea Breeze):
- Land heats up faster than sea
- Hot air rises from land
- Cool air comes from sea to land

NIGHT (Land Breeze):
- Land cools faster than sea
- Sea is warmer
- Air moves from land to sea

Practice Questions:
1. What is normal body temperature?
2. Why metal pots have wooden handles?
3. What is the unit of temperature?
4. Name three types of heat transfer.
5. Why winter clothes are usually woolen?'''},

    # Grade 8 - More
    {'g': 8, 's': 'Mathematics', 't': 'Compound Interest',
     'd': 'Simple and Compound Interest calculations',
     'c': '''COMPOUND INTEREST

INTEREST is the extra money paid for using someone\'s money.

Two Types of Interest:

1. SIMPLE INTEREST (SI)
Interest calculated only on the original amount.

Formula:
SI = (P x R x T) / 100

Where:
P = Principal (original amount)
R = Rate of interest (per year, in percent)
T = Time (in years)

Total Amount = Principal + Simple Interest

Example 1:
Find SI on Rs. 1000 at 10 percent per year for 2 years.

Solution:
P = 1000, R = 10, T = 2
SI = (1000 x 10 x 2) / 100
SI = 20000 / 100
SI = Rs. 200

Total Amount = 1000 + 200 = Rs. 1200

Example 2:
Find SI on Rs. 5000 at 8 percent per year for 3 years.

Solution:
SI = (5000 x 8 x 3) / 100 = Rs. 1200

2. COMPOUND INTEREST (CI)
Interest calculated on the AMOUNT (Principal + Interest).
Interest gets added to principal each year.

Formula:
A = P (1 + R/100)^n

Where:
A = Final Amount
P = Principal
R = Rate of interest (per year)
n = Number of years

CI = A - P

Example 3:
Find CI on Rs. 1000 at 10 percent per year for 2 years.

Solution:
P = 1000, R = 10, n = 2

A = 1000 x (1 + 10/100)^2
A = 1000 x (1.1)^2
A = 1000 x 1.21
A = Rs. 1210

CI = A - P = 1210 - 1000 = Rs. 210

Notice: CI (Rs. 210) is more than SI (Rs. 200)!

Year-by-Year Calculation:

Year 1:
Principal = Rs. 1000
Interest at 10 percent = Rs. 100
Amount after Year 1 = Rs. 1100

Year 2:
New Principal = Rs. 1100
Interest at 10 percent = Rs. 110
Amount after Year 2 = Rs. 1210

Total Interest = Rs. 210

Comparison: SI vs CI

For Rs. 1000 at 10 percent for 2 years:
- SI = Rs. 200, Total = Rs. 1200
- CI = Rs. 210, Total = Rs. 1210
- Difference = Rs. 10

For longer time periods, CI is much more!

Example 4:
Find CI on Rs. 8000 at 5 percent for 2 years.

Solution:
A = 8000 x (1 + 5/100)^2
A = 8000 x (1.05)^2
A = 8000 x 1.1025
A = Rs. 8820

CI = 8820 - 8000 = Rs. 820

Compound Interest Compounded:

Compounded ANNUALLY = once per year
Compounded HALF-YEARLY = twice a year (every 6 months)
Compounded QUARTERLY = 4 times a year

When compounded half-yearly:
- Rate becomes R/2
- Time becomes 2T

A = P (1 + R/200)^2T

When compounded quarterly:
- Rate becomes R/4
- Time becomes 4T

A = P (1 + R/400)^4T

Example 5:
Find CI on Rs. 10000 at 8 percent for 1 year, compounded half-yearly.

Solution:
A = 10000 x (1 + 8/200)^2
A = 10000 x (1.04)^2
A = 10000 x 1.0816
A = Rs. 10816

CI = 10816 - 10000 = Rs. 816

Real Life Applications:

Banks:
- Savings account uses compound interest
- More money grows over time

Loans:
- Banks charge compound interest on loans
- Repay more than borrowed

Investments:
- Stocks, mutual funds, FDs grow with compound interest
- Albert Einstein called CI "the most powerful force in the universe"

Population Growth:
- Population also grows with compound formula
- A = P(1 + R/100)^n

Depreciation:
- Things lose value over time
- A = P(1 - R/100)^n (note: minus sign)

Example 6: (Depreciation)
A car costs Rs. 5,00,000. It depreciates at 10 percent per year. Find value after 2 years.

Solution:
A = 500000 x (1 - 10/100)^2
A = 500000 x (0.9)^2
A = 500000 x 0.81
A = Rs. 4,05,000

Practice Problems:
1. Find SI on Rs. 2000 at 5 percent for 3 years.
2. Find CI on Rs. 5000 at 4 percent for 2 years.
3. Compare SI and CI on Rs. 10000 at 10 percent for 2 years.

Answers:
1. SI = (2000 x 5 x 3) / 100 = Rs. 300
2. A = 5000 x (1.04)^2 = Rs. 5408
   CI = Rs. 408
3. SI = Rs. 2000, CI = Rs. 2100, Difference = Rs. 100'''},

    # Grade 9 - More
    {'g': 9, 's': 'Science', 't': 'Atoms and Molecules',
     'd': 'Basic structure of atoms and molecules',
     'c': '''ATOMS AND MOLECULES

What is Matter?
Anything that has mass and occupies space.

What is an Atom?
The smallest particle of an element that cannot be further divided.

Discovery: John Dalton (1808) proposed atomic theory.

Dalton\'s Atomic Theory:
1. All matter is made of tiny particles called ATOMS.
2. Atoms cannot be created or destroyed.
3. Atoms of same element are identical.
4. Atoms of different elements have different properties.
5. Atoms combine in fixed ratios to form compounds.

Structure of Atom:

Three Sub-atomic Particles:

1. PROTON
- Located in nucleus
- Positive charge (+1)
- Mass = 1 unit
- Discovered by Goldstein (1886)

2. NEUTRON
- Located in nucleus
- No charge (neutral)
- Mass = 1 unit
- Discovered by James Chadwick (1932)

3. ELECTRON
- Revolves around nucleus
- Negative charge (-1)
- Mass = 1/1836 of proton (very small)
- Discovered by J.J. Thomson (1897)

NUCLEUS:
- Center of atom
- Contains protons and neutrons
- Most of atom\'s mass here
- Discovered by Ernest Rutherford

ATOMIC NUMBER (Z):
Number of protons in the nucleus.
Different elements have different atomic numbers.

Examples:
- Hydrogen: Z = 1
- Helium: Z = 2
- Carbon: Z = 6
- Oxygen: Z = 8
- Sodium: Z = 11

MASS NUMBER (A):
Total of protons and neutrons in nucleus.
A = Number of protons + Number of neutrons

Example: Carbon
- Atomic Number (Z) = 6
- Mass Number (A) = 12
- Neutrons = 12 - 6 = 6

ELEMENTS:
A pure substance made of only one type of atom.
118 elements known so far.

Common Elements and their Symbols:
- Hydrogen: H
- Oxygen: O
- Carbon: C
- Nitrogen: N
- Sodium: Na (from Natrium)
- Potassium: K (from Kalium)
- Iron: Fe (from Ferrum)
- Copper: Cu (from Cuprum)
- Silver: Ag (from Argentum)
- Gold: Au (from Aurum)
- Mercury: Hg (from Hydrargyrum)
- Lead: Pb (from Plumbum)

MOLECULES:
When two or more atoms combine, they form a molecule.

Types of Molecules:

1. ATOMS OF SAME ELEMENT
- O2 (Oxygen molecule - 2 oxygen atoms)
- H2 (Hydrogen molecule - 2 hydrogen atoms)
- N2 (Nitrogen molecule)
- Cl2 (Chlorine molecule)

2. ATOMS OF DIFFERENT ELEMENTS (Compounds)
- H2O (Water - 2 hydrogen + 1 oxygen)
- CO2 (Carbon dioxide - 1 carbon + 2 oxygen)
- CH4 (Methane - 1 carbon + 4 hydrogen)
- NH3 (Ammonia - 1 nitrogen + 3 hydrogen)

ATOMIC MASS:
Mass of an atom expressed in atomic mass units (amu).

Examples:
- Hydrogen: 1 amu
- Helium: 4 amu
- Carbon: 12 amu
- Oxygen: 16 amu
- Sodium: 23 amu

MOLECULAR MASS:
Sum of atomic masses of all atoms in a molecule.

Example: Water (H2O)
- H: 1 amu (and there are 2)
- O: 16 amu (1 of them)
- H2O mass = (1 x 2) + 16 = 18 amu

Example: Carbon dioxide (CO2)
- C: 12 amu (1)
- O: 16 amu (2)
- CO2 mass = 12 + (16 x 2) = 44 amu

CHEMICAL FORMULAS:
A short way to write molecules using symbols.

Examples:
- Water = H2O
- Sodium chloride = NaCl
- Sulfuric acid = H2SO4
- Carbon dioxide = CO2
- Glucose = C6H12O6

VALENCY:
The combining power of an element.
- Hydrogen: 1
- Oxygen: 2
- Sodium: 1
- Calcium: 2
- Aluminum: 3
- Carbon: 4

How to Write Formulas:

Step 1: Write symbols of elements
Step 2: Write valencies on top
Step 3: Cross-multiply

Example: Aluminum oxide
Al = 3, O = 2
Al2O3

ION:
A charged particle (atom that lost or gained electrons).

CATION (Positive ion):
- Atom loses electrons
- Examples: Na+, K+, Ca2+

ANION (Negative ion):
- Atom gains electrons
- Examples: Cl-, O2-, OH-

LAW OF CONSERVATION OF MASS:
Mass can neither be created nor destroyed in a chemical reaction.

Important Points:
- Number of atoms is constant
- Equations must be BALANCED

Practice Questions:
1. What is the smallest unit of matter?
2. Name the three sub-atomic particles.
3. What is atomic number of Carbon?
4. Write the formula of water.
5. What is the difference between atom and molecule?'''},

    # Grade 10 - More
    {'g': 10, 's': 'Science', 't': 'Light - Reflection and Refraction',
     'd': 'Properties of light, mirrors and lenses',
     'c': '''LIGHT - REFLECTION AND REFRACTION

What is Light?
Light is a form of energy that helps us see things. It travels in STRAIGHT LINES.

Speed of Light:
- In vacuum/air: 3 x 10^8 m/s (3,00,000 km/sec)
- Fastest thing in universe!

Properties of Light:
- Travels in straight lines (rectilinear propagation)
- Can pass through transparent materials
- Reflects off shiny surfaces
- Refracts when entering different mediums
- Has 7 colors (VIBGYOR)
- Can be polarized

REFLECTION OF LIGHT:

Definition: Bouncing back of light from a surface.

Laws of Reflection:
1. Angle of incidence = Angle of reflection
2. Incident ray, reflected ray, and normal lie in same plane

Terms:
- INCIDENT RAY: Light ray falling on surface
- REFLECTED RAY: Light ray bouncing back
- NORMAL: Imaginary line perpendicular to surface
- ANGLE OF INCIDENCE: Angle between incident ray and normal
- ANGLE OF REFLECTION: Angle between reflected ray and normal

TYPES OF MIRRORS:

1. PLANE MIRROR (Flat)
- Forms VIRTUAL image
- Image is ERECT (upright)
- Image SAME SIZE as object
- Image at SAME DISTANCE behind mirror
- LATERALLY INVERTED (left-right reversed)

Uses:
- Looking in bathroom
- Vehicles
- Periscope

2. CONCAVE MIRROR (Curved inward)
- Reflecting surface is inside of sphere
- Forms both REAL and VIRTUAL images
- Image size depends on object position

POSITIONS and IMAGES:
- Object at infinity: Image is highly diminished, at focus
- Object beyond C: Image diminished, between C and F, real, inverted
- Object at C: Same size, at C, real, inverted
- Object between C and F: Image larger, beyond C, real, inverted
- Object at F: Image at infinity
- Object between F and pole: Image larger, behind mirror, virtual, erect

Uses:
- Make-up mirrors (close-up)
- Shaving mirrors
- Headlights of vehicles
- Reflectors in torch
- Solar furnaces
- Telescopes

3. CONVEX MIRROR (Curved outward)
- Reflecting surface is outside of sphere
- Always forms VIRTUAL image
- Image is DIMINISHED
- Image is ERECT
- Wider field of view

Uses:
- Side mirrors of vehicles
- Security mirrors in shops
- Road bends/blind spots

MIRROR FORMULA:

1/v + 1/u = 1/f

Where:
v = image distance
u = object distance
f = focal length

MAGNIFICATION (m):
m = h\' / h = -v / u

Where:
h\' = height of image
h = height of object

If m is positive: virtual, erect image
If m is negative: real, inverted image
If |m| > 1: image is magnified
If |m| < 1: image is diminished

REFRACTION OF LIGHT:

Definition: Bending of light when it passes from one medium to another.

Why does it bend?
Light travels at different speeds in different mediums.
- Air (fastest)
- Water (slower)
- Glass (slowest among these)

Laws of Refraction:
1. Incident ray, refracted ray, and normal lie in same plane.
2. SNELL\'S LAW: sin(i) / sin(r) = constant = n (refractive index)

Where:
i = angle of incidence
r = angle of refraction
n = refractive index

REFRACTIVE INDEX:
- Light bends towards normal: denser medium
- Light bends away from normal: rarer medium

Common Refractive Indices:
- Vacuum: 1.00
- Air: 1.0003 (approx 1)
- Water: 1.33
- Glass: 1.5
- Diamond: 2.42

Examples of Refraction:
- Pencil appears bent in water
- Star twinkling
- Mirage in desert
- Pool appears shallower
- Sun visible before actual sunrise

LENSES:

1. CONVEX LENS (Convergent)
- Thicker in middle, thinner at edges
- Converges light rays
- Can form real and virtual images

Uses:
- Magnifying glass
- Camera
- Telescope
- Microscope
- Reading glasses for hypermetropia (far-sightedness)

2. CONCAVE LENS (Divergent)
- Thinner in middle, thicker at edges
- Diverges light rays
- Always forms virtual, erect, diminished image

Uses:
- Eyeglasses for myopia (near-sightedness)
- Peepholes in doors

LENS FORMULA:
1/v - 1/u = 1/f

POWER OF LENS:
P = 1/f (when f is in meters)
Unit: DIOPTER (D)
- Convex lens: positive power
- Concave lens: negative power

HUMAN EYE:

Parts:
- Cornea: Front clear part
- Iris: Colored part with hole (pupil)
- Pupil: Adjustable hole
- Lens: Behind pupil, focuses light
- Retina: At back, has light-sensitive cells
- Optic nerve: Carries signals to brain

How We See:
1. Light enters through cornea
2. Pupil controls light amount
3. Lens focuses on retina
4. Retina converts to electrical signals
5. Optic nerve sends to brain
6. Brain interprets the image

Defects of Vision:

1. MYOPIA (Near-sightedness)
- Can see near but not far
- Eye lens too thick
- Image forms before retina
- Corrected with CONCAVE lens

2. HYPERMETROPIA (Far-sightedness)
- Can see far but not near
- Eye lens too thin
- Image forms after retina
- Corrected with CONVEX lens

3. PRESBYOPIA
- Old age vision
- Cannot see near things
- Bifocal lenses used

4. CATARACT
- Lens becomes cloudy
- Surgery needed

5. ASTIGMATISM
- Blurred vision
- Cylindrical lens

WHITE LIGHT (Sunlight):
Consists of 7 colors - VIBGYOR
- Violet
- Indigo
- Blue
- Green
- Yellow
- Orange
- Red

When white light passes through prism, it disperses into 7 colors.
Newton showed this in 1665.

RAINBOW:
- Sunlight passes through water droplets
- Acts like prisms
- Splits into 7 colors

Scattering of Light:
- Why sky is blue (blue scatters most)
- Why sunsets are red (red scatters least)
- Why warning signals are red

Practice Questions:
1. State the laws of reflection.
2. What is the speed of light?
3. Where is the image formed in a concave mirror?
4. What is the lens used for myopia?
5. Why is the sky blue?'''},
]


def sanitize(text):
    """Sanitize text for PDF"""
    replacements = {
        '×': 'x', '÷': '/', '−': '-', '°': ' deg',
        '²': '2', '³': '3', '√': 'sqrt', 'π': 'pi',
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


class SimplePDF(FPDF):
    def __init__(self, title='', subject='', grade=0):
        super().__init__()
        self.doc_title = sanitize(title)[:80]
        self.doc_subject = sanitize(subject)
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
        content = sanitize(content)
        for raw in content.split('\n'):
            line = raw.rstrip()
            if not line.strip():
                self.ln(2)
                continue

            stripped = line.strip()
            is_heading = stripped.isupper() and len(stripped) <= 70 and '=' not in stripped and '/' not in stripped
            is_sub = stripped.endswith(':') and len(stripped) <= 40 and not stripped.startswith('-') and not any(c.isdigit() for c in stripped[:2])

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


def add_more():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("Teacher not found")
            return

        os.makedirs('./data/resources', exist_ok=True)
        existing = {r.title for r in Resource.query.all()}

        added = 0
        for r in MORE_RESOURCES:
            if r['t'] in existing:
                print(f"[SKIP] {r['t']} already exists")
                continue

            filename = f"ncert_g{r['g']}_{r['s'].replace(' ', '_')}_{r['t'].replace(' ', '_').replace('/', '_')[:40]}"
            txt_path = f"data/resources/{filename}.txt"
            pdf_path = f"data/resources/{filename}.pdf"

            # Save text
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(r['c'])

            # Generate PDF
            try:
                pdf = SimplePDF(title=r['t'], subject=r['s'], grade=r['g'])
                pdf.add_page()
                pdf.render(r['c'])
                pdf.output(pdf_path)
            except Exception as e:
                print(f"[ERROR PDF] {r['t']}: {e}")
                continue

            file_size = os.path.getsize(pdf_path)
            yt_url, yt_ch = get_youtube(r['t'], r['s'])

            resource = Resource(
                title=r['t'],
                description=r['d'],
                subject=r['s'],
                grade_level=r['g'],
                content_type='pdf',
                file_path=pdf_path,
                file_size=file_size,
                youtube_url=yt_url,
                youtube_channel=yt_ch,
                created_by=teacher.id,
                is_published=True
            )
            db.session.add(resource)
            added += 1
            print(f"[ADDED] Grade {r['g']} - {r['t']} ({yt_ch})")

        db.session.commit()
        print(f"\n{'='*60}")
        print(f"Added {added} new resources")
        print(f"Total resources: {Resource.query.count()}")
        print(f"{'='*60}")


if __name__ == '__main__':
    try:
        add_more()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
