"""
Load comprehensive NCERT-aligned quizzes for grades 1-10
All 4 core subjects: Mathematics, Science, English, Social Studies
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Quiz, QuizQuestion

# NCERT-aligned curriculum quizzes
NCERT_QUIZZES = [
    # ========== GRADE 1 ==========
    {
        'title': 'Numbers 1-20',
        'description': 'Counting numbers from 1 to 20',
        'subject': 'Mathematics', 'grade_level': 1,
        'questions': [
            {'q': 'What comes after 7?', 'a': '6', 'b': '8', 'c': '9', 'd': '10', 'correct': 'B'},
            {'q': 'How many fingers do you have on one hand?', 'a': '3', 'b': '4', 'c': '5', 'd': '6', 'correct': 'C'},
            {'q': 'What is 2 + 3?', 'a': '4', 'b': '5', 'c': '6', 'd': '7', 'correct': 'B'},
            {'q': 'Which number is bigger: 8 or 5?', 'a': '8', 'b': '5', 'c': 'Same', 'd': 'None', 'correct': 'A'},
            {'q': 'What comes before 10?', 'a': '11', 'b': '9', 'c': '8', 'd': '12', 'correct': 'B'},
        ]
    },
    {
        'title': 'Animals Around Us',
        'description': 'Learn about animals in our environment',
        'subject': 'Science', 'grade_level': 1,
        'questions': [
            {'q': 'Which animal gives us milk?', 'a': 'Dog', 'b': 'Cow', 'c': 'Cat', 'd': 'Bird', 'correct': 'B'},
            {'q': 'Which animal can fly?', 'a': 'Fish', 'b': 'Cow', 'c': 'Bird', 'd': 'Dog', 'correct': 'C'},
            {'q': 'Where does a fish live?', 'a': 'Tree', 'b': 'Water', 'c': 'Cave', 'd': 'Nest', 'correct': 'B'},
            {'q': 'How many legs does a dog have?', 'a': '2', 'b': '3', 'c': '4', 'd': '6', 'correct': 'C'},
        ]
    },
    {
        'title': 'The Alphabet',
        'description': 'Learn English alphabet',
        'subject': 'English', 'grade_level': 1,
        'questions': [
            {'q': 'How many letters in English alphabet?', 'a': '24', 'b': '25', 'c': '26', 'd': '27', 'correct': 'C'},
            {'q': 'Which letter comes after B?', 'a': 'A', 'b': 'C', 'c': 'D', 'd': 'E', 'correct': 'B'},
            {'q': 'A is for ___', 'a': 'Apple', 'b': 'Ball', 'c': 'Cat', 'd': 'Dog', 'correct': 'A'},
            {'q': 'Which is a vowel?', 'a': 'B', 'b': 'C', 'c': 'D', 'd': 'A', 'correct': 'D'},
        ]
    },
    {
        'title': 'My Family',
        'description': 'About family members',
        'subject': 'Social Studies', 'grade_level': 1,
        'questions': [
            {'q': 'Who is your mother\'s mother?', 'a': 'Aunt', 'b': 'Grandmother', 'c': 'Sister', 'd': 'Cousin', 'correct': 'B'},
            {'q': 'A family that has parents and children is called?', 'a': 'Big', 'b': 'Nuclear', 'c': 'Joint', 'd': 'Small', 'correct': 'B'},
            {'q': 'Your father\'s brother is your?', 'a': 'Uncle', 'b': 'Cousin', 'c': 'Grandfather', 'd': 'Brother', 'correct': 'A'},
        ]
    },

    # ========== GRADE 2 ==========
    {
        'title': 'Addition and Subtraction',
        'description': 'Basic addition and subtraction',
        'subject': 'Mathematics', 'grade_level': 2,
        'questions': [
            {'q': 'What is 15 + 7?', 'a': '21', 'b': '22', 'c': '23', 'd': '24', 'correct': 'B'},
            {'q': 'What is 20 - 8?', 'a': '11', 'b': '12', 'c': '13', 'd': '14', 'correct': 'B'},
            {'q': 'What is 9 + 6?', 'a': '14', 'b': '15', 'c': '16', 'd': '17', 'correct': 'B'},
            {'q': 'What is 30 - 15?', 'a': '12', 'b': '15', 'c': '18', 'd': '20', 'correct': 'B'},
            {'q': '10 + 10 = ?', 'a': '15', 'b': '20', 'c': '25', 'd': '30', 'correct': 'B'},
        ]
    },
    {
        'title': 'Plants Around Us',
        'description': 'Parts and uses of plants',
        'subject': 'Science', 'grade_level': 2,
        'questions': [
            {'q': 'Which part of plant absorbs water?', 'a': 'Leaf', 'b': 'Stem', 'c': 'Root', 'd': 'Flower', 'correct': 'C'},
            {'q': 'Plants need ___ to grow', 'a': 'Sunlight', 'b': 'Darkness', 'c': 'Cold', 'd': 'Smoke', 'correct': 'A'},
            {'q': 'Which is NOT a plant?', 'a': 'Tree', 'b': 'Grass', 'c': 'Stone', 'd': 'Flower', 'correct': 'C'},
            {'q': 'Where do trees get their food?', 'a': 'Soil only', 'b': 'Leaves make food', 'c': 'From animals', 'd': 'From people', 'correct': 'B'},
        ]
    },
    {
        'title': 'Simple Words',
        'description': 'Reading simple English words',
        'subject': 'English', 'grade_level': 2,
        'questions': [
            {'q': 'C-A-T spells?', 'a': 'Cat', 'b': 'Bat', 'c': 'Rat', 'd': 'Mat', 'correct': 'A'},
            {'q': 'What is the opposite of "big"?', 'a': 'Large', 'b': 'Huge', 'c': 'Small', 'd': 'Tall', 'correct': 'C'},
            {'q': 'Which is a color?', 'a': 'Run', 'b': 'Blue', 'c': 'Big', 'd': 'Sit', 'correct': 'B'},
        ]
    },

    # ========== GRADE 3 ==========
    {
        'title': 'Multiplication Tables',
        'description': 'Times tables 2-5',
        'subject': 'Mathematics', 'grade_level': 3,
        'questions': [
            {'q': '6 x 4 = ?', 'a': '20', 'b': '22', 'c': '24', 'd': '26', 'correct': 'C'},
            {'q': '5 x 7 = ?', 'a': '30', 'b': '35', 'c': '40', 'd': '45', 'correct': 'B'},
            {'q': '3 x 9 = ?', 'a': '24', 'b': '27', 'c': '30', 'd': '33', 'correct': 'B'},
            {'q': '8 x 3 = ?', 'a': '21', 'b': '24', 'c': '27', 'd': '30', 'correct': 'B'},
            {'q': '4 x 6 = ?', 'a': '20', 'b': '22', 'c': '24', 'd': '26', 'correct': 'C'},
        ]
    },
    {
        'title': 'Living and Non-Living',
        'description': 'Difference between living and non-living things',
        'subject': 'Science', 'grade_level': 3,
        'questions': [
            {'q': 'Which is a living thing?', 'a': 'Stone', 'b': 'Chair', 'c': 'Tree', 'd': 'Book', 'correct': 'C'},
            {'q': 'Living things need ___', 'a': 'Food', 'b': 'Water', 'c': 'Air', 'd': 'All of these', 'correct': 'D'},
            {'q': 'Which is non-living?', 'a': 'Bird', 'b': 'Pencil', 'c': 'Fish', 'd': 'Plant', 'correct': 'B'},
            {'q': 'Do plants need water?', 'a': 'Yes', 'b': 'No', 'c': 'Sometimes', 'd': 'Never', 'correct': 'A'},
        ]
    },
    {
        'title': 'Nouns and Verbs',
        'description': 'Basic grammar parts of speech',
        'subject': 'English', 'grade_level': 3,
        'questions': [
            {'q': 'Which is a noun?', 'a': 'Run', 'b': 'Book', 'c': 'Quickly', 'd': 'Beautiful', 'correct': 'B'},
            {'q': 'Which is a verb?', 'a': 'Apple', 'b': 'Happy', 'c': 'Jump', 'd': 'Red', 'correct': 'C'},
            {'q': 'Plural of "book" is?', 'a': 'Bookes', 'b': 'Books', 'c': 'Bookies', 'd': 'Bookz', 'correct': 'B'},
            {'q': 'I ___ to school every day.', 'a': 'go', 'b': 'going', 'c': 'gone', 'd': 'goes', 'correct': 'A'},
        ]
    },
    {
        'title': 'Our Country India',
        'description': 'Basic facts about India',
        'subject': 'Social Studies', 'grade_level': 3,
        'questions': [
            {'q': 'What is the capital of India?', 'a': 'Mumbai', 'b': 'New Delhi', 'c': 'Kolkata', 'd': 'Chennai', 'correct': 'B'},
            {'q': 'How many colors in Indian flag?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'B'},
            {'q': 'National animal of India?', 'a': 'Lion', 'b': 'Elephant', 'c': 'Tiger', 'd': 'Peacock', 'correct': 'C'},
            {'q': 'National bird of India?', 'a': 'Parrot', 'b': 'Peacock', 'c': 'Sparrow', 'd': 'Eagle', 'correct': 'B'},
        ]
    },

    # ========== GRADE 4 ==========
    {
        'title': 'Division and Fractions',
        'description': 'Basic division and fractions',
        'subject': 'Mathematics', 'grade_level': 4,
        'questions': [
            {'q': '36 / 4 = ?', 'a': '8', 'b': '9', 'c': '10', 'd': '12', 'correct': 'B'},
            {'q': '1/2 of 20 = ?', 'a': '5', 'b': '10', 'c': '15', 'd': '20', 'correct': 'B'},
            {'q': 'How many quarters in 1 whole?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'C'},
            {'q': '100 / 10 = ?', 'a': '5', 'b': '10', 'c': '15', 'd': '20', 'correct': 'B'},
            {'q': '1/4 + 1/4 = ?', 'a': '1/8', 'b': '1/2', 'c': '2/4', 'd': 'Both B and C', 'correct': 'D'},
        ]
    },
    {
        'title': 'Food and Nutrition',
        'description': 'Healthy eating and food groups',
        'subject': 'Science', 'grade_level': 4,
        'questions': [
            {'q': 'Which gives us energy?', 'a': 'Carbohydrates', 'b': 'Water', 'c': 'Salt', 'd': 'Sand', 'correct': 'A'},
            {'q': 'Vitamin C is found in?', 'a': 'Rice', 'b': 'Oranges', 'c': 'Bread', 'd': 'Salt', 'correct': 'B'},
            {'q': 'Milk gives us?', 'a': 'Calcium', 'b': 'Sugar', 'c': 'Oil', 'd': 'Iron', 'correct': 'A'},
            {'q': 'We should eat fruits and vegetables daily.', 'a': 'True', 'b': 'False', 'c': 'Sometimes', 'd': 'Never', 'correct': 'A'},
        ]
    },
    {
        'title': 'Reading Comprehension',
        'description': 'Understanding stories',
        'subject': 'English', 'grade_level': 4,
        'questions': [
            {'q': 'A story is also called?', 'a': 'Tale', 'b': 'Math', 'c': 'Quiz', 'd': 'Game', 'correct': 'A'},
            {'q': 'Who wrote stories about boys with magical powers?', 'a': 'Shakespeare', 'b': 'J.K. Rowling', 'c': 'Tagore', 'd': 'Premchand', 'correct': 'B'},
            {'q': 'Tense for "I am walking"?', 'a': 'Past', 'b': 'Present continuous', 'c': 'Future', 'd': 'Past perfect', 'correct': 'B'},
        ]
    },
    {
        'title': 'States of India',
        'description': 'Indian states and capitals',
        'subject': 'Social Studies', 'grade_level': 4,
        'questions': [
            {'q': 'Capital of Maharashtra?', 'a': 'Pune', 'b': 'Mumbai', 'c': 'Nagpur', 'd': 'Nashik', 'correct': 'B'},
            {'q': 'Capital of Karnataka?', 'a': 'Mysore', 'b': 'Bangalore', 'c': 'Mangalore', 'd': 'Hubli', 'correct': 'B'},
            {'q': 'How many states in India?', 'a': '26', 'b': '27', 'c': '28', 'd': '29', 'correct': 'C'},
            {'q': 'Which river is called "Ganga Maa"?', 'a': 'Yamuna', 'b': 'Ganges', 'c': 'Krishna', 'd': 'Godavari', 'correct': 'B'},
        ]
    },

    # ========== GRADE 5 ==========
    {
        'title': 'Decimals and Percentages',
        'description': 'Working with decimals',
        'subject': 'Mathematics', 'grade_level': 5,
        'questions': [
            {'q': '0.5 = ?', 'a': '1/2', 'b': '1/4', 'c': '1/3', 'd': '1/5', 'correct': 'A'},
            {'q': '50% of 200 = ?', 'a': '50', 'b': '100', 'c': '150', 'd': '200', 'correct': 'B'},
            {'q': '0.25 = ?', 'a': '25%', 'b': '50%', 'c': '75%', 'd': '100%', 'correct': 'A'},
            {'q': '1.5 + 2.5 = ?', 'a': '3', 'b': '3.5', 'c': '4', 'd': '4.5', 'correct': 'C'},
            {'q': '10% of 50 = ?', 'a': '3', 'b': '5', 'c': '8', 'd': '10', 'correct': 'B'},
        ]
    },
    {
        'title': 'Human Body Systems',
        'description': 'Organs and body functions',
        'subject': 'Science', 'grade_level': 5,
        'questions': [
            {'q': 'Which organ pumps blood?', 'a': 'Lungs', 'b': 'Heart', 'c': 'Brain', 'd': 'Kidney', 'correct': 'B'},
            {'q': 'We breathe through?', 'a': 'Stomach', 'b': 'Heart', 'c': 'Lungs', 'd': 'Liver', 'correct': 'C'},
            {'q': 'How many bones in adult human?', 'a': '156', 'b': '206', 'c': '256', 'd': '306', 'correct': 'B'},
            {'q': 'Which sense organ detects smell?', 'a': 'Eye', 'b': 'Ear', 'c': 'Nose', 'd': 'Tongue', 'correct': 'C'},
            {'q': 'Brain is part of which system?', 'a': 'Digestive', 'b': 'Nervous', 'c': 'Respiratory', 'd': 'Circulatory', 'correct': 'B'},
        ]
    },
    {
        'title': 'Sentences and Punctuation',
        'description': 'Building correct sentences',
        'subject': 'English', 'grade_level': 5,
        'questions': [
            {'q': 'A question ends with?', 'a': '.', 'b': '?', 'c': '!', 'd': ',', 'correct': 'B'},
            {'q': 'A complete sentence must have?', 'a': 'Subject only', 'b': 'Verb only', 'c': 'Subject and verb', 'd': 'Just nouns', 'correct': 'C'},
            {'q': 'Which is a proper noun?', 'a': 'city', 'b': 'Delhi', 'c': 'cat', 'd': 'book', 'correct': 'B'},
            {'q': 'Find the verb: "She sings beautifully."', 'a': 'She', 'b': 'sings', 'c': 'beautifully', 'd': 'None', 'correct': 'B'},
        ]
    },
    {
        'title': 'Indian Freedom Struggle',
        'description': 'History of independence',
        'subject': 'Social Studies', 'grade_level': 5,
        'questions': [
            {'q': 'When did India get independence?', 'a': '1945', 'b': '1947', 'c': '1949', 'd': '1950', 'correct': 'B'},
            {'q': 'Father of the Nation?', 'a': 'Nehru', 'b': 'Gandhi', 'c': 'Patel', 'd': 'Bose', 'correct': 'B'},
            {'q': 'First Prime Minister of India?', 'a': 'Nehru', 'b': 'Gandhi', 'c': 'Shastri', 'd': 'Indira', 'correct': 'A'},
            {'q': 'Independence Day is on?', 'a': 'Aug 15', 'b': 'Jan 26', 'c': 'Oct 2', 'd': 'Nov 14', 'correct': 'A'},
        ]
    },

    # ========== GRADE 6 ==========
    {
        'title': 'Integers and Number System',
        'description': 'Positive and negative numbers',
        'subject': 'Mathematics', 'grade_level': 6,
        'questions': [
            {'q': '(-5) + (-3) = ?', 'a': '-8', 'b': '-2', 'c': '2', 'd': '8', 'correct': 'A'},
            {'q': '7 + (-4) = ?', 'a': '3', 'b': '-3', 'c': '11', 'd': '-11', 'correct': 'A'},
            {'q': 'LCM of 4 and 6 = ?', 'a': '8', 'b': '10', 'c': '12', 'd': '24', 'correct': 'C'},
            {'q': 'HCF of 12 and 18?', 'a': '4', 'b': '6', 'c': '8', 'd': '12', 'correct': 'B'},
            {'q': 'Is 0 positive or negative?', 'a': 'Positive', 'b': 'Negative', 'c': 'Neither', 'd': 'Both', 'correct': 'C'},
        ]
    },
    {
        'title': 'Components of Food',
        'description': 'Nutrients and food chemistry',
        'subject': 'Science', 'grade_level': 6,
        'questions': [
            {'q': 'Which provides protein?', 'a': 'Rice', 'b': 'Eggs', 'c': 'Sugar', 'd': 'Oil', 'correct': 'B'},
            {'q': 'Deficiency of Vitamin D causes?', 'a': 'Night blindness', 'b': 'Rickets', 'c': 'Scurvy', 'd': 'Anemia', 'correct': 'B'},
            {'q': 'Carbohydrates give us?', 'a': 'Growth', 'b': 'Energy', 'c': 'Repair', 'd': 'Protection', 'correct': 'B'},
            {'q': 'Source of iodine?', 'a': 'Salt', 'b': 'Sugar', 'c': 'Oil', 'd': 'Water', 'correct': 'A'},
        ]
    },
    {
        'title': 'Earth and Solar System',
        'description': 'Our planet and beyond',
        'subject': 'Social Studies', 'grade_level': 6,
        'questions': [
            {'q': 'How many planets in solar system?', 'a': '7', 'b': '8', 'c': '9', 'd': '10', 'correct': 'B'},
            {'q': 'Closest planet to sun?', 'a': 'Venus', 'b': 'Earth', 'c': 'Mercury', 'd': 'Mars', 'correct': 'C'},
            {'q': 'Earth\'s only natural satellite?', 'a': 'Sun', 'b': 'Moon', 'c': 'Mars', 'd': 'Star', 'correct': 'B'},
            {'q': 'How long does Earth take to revolve around Sun?', 'a': '24 hours', 'b': '30 days', 'c': '365 days', 'd': '1000 days', 'correct': 'C'},
        ]
    },

    # ========== GRADE 7 ==========
    {
        'title': 'Algebraic Expressions',
        'description': 'Introduction to algebra',
        'subject': 'Mathematics', 'grade_level': 7,
        'questions': [
            {'q': 'If x = 3, then 2x + 5 = ?', 'a': '8', 'b': '11', 'c': '13', 'd': '15', 'correct': 'B'},
            {'q': 'Simplify: 3a + 2a = ?', 'a': '5a', 'b': '6a', 'c': '5', 'd': '6', 'correct': 'A'},
            {'q': 'If y = 5, then y² = ?', 'a': '10', 'b': '15', 'c': '20', 'd': '25', 'correct': 'D'},
            {'q': '(2x)(3x) = ?', 'a': '5x', 'b': '6x', 'c': '5x²', 'd': '6x²', 'correct': 'D'},
            {'q': 'If 2x + 4 = 10, x = ?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'B'},
        ]
    },
    {
        'title': 'Acids, Bases and Salts',
        'description': 'Chemistry basics',
        'subject': 'Science', 'grade_level': 7,
        'questions': [
            {'q': 'Lemon juice is?', 'a': 'Acid', 'b': 'Base', 'c': 'Salt', 'd': 'Neutral', 'correct': 'A'},
            {'q': 'pH of pure water?', 'a': '5', 'b': '6', 'c': '7', 'd': '8', 'correct': 'C'},
            {'q': 'Sodium bicarbonate is?', 'a': 'Strong acid', 'b': 'Weak base', 'c': 'Strong base', 'd': 'Salt', 'correct': 'B'},
            {'q': 'Acid + Base = ?', 'a': 'Water only', 'b': 'Salt only', 'c': 'Salt + Water', 'd': 'Gas', 'correct': 'C'},
        ]
    },
    {
        'title': 'Tenses in English',
        'description': 'Past, present, future',
        'subject': 'English', 'grade_level': 7,
        'questions': [
            {'q': '"I have eaten" is which tense?', 'a': 'Past simple', 'b': 'Present perfect', 'c': 'Future', 'd': 'Past continuous', 'correct': 'B'},
            {'q': 'Past tense of "go"?', 'a': 'Goed', 'b': 'Went', 'c': 'Gone', 'd': 'Going', 'correct': 'B'},
            {'q': '"She will sing" is?', 'a': 'Past', 'b': 'Present', 'c': 'Future', 'd': 'Perfect', 'correct': 'C'},
            {'q': 'Active to passive: "He writes a letter."', 'a': 'A letter writes him', 'b': 'A letter is written by him', 'c': 'He wrote a letter', 'd': 'Letter was written', 'correct': 'B'},
        ]
    },

    # ========== GRADE 8 ==========
    {
        'title': 'Rational Numbers',
        'description': 'Working with fractions',
        'subject': 'Mathematics', 'grade_level': 8,
        'questions': [
            {'q': 'Which is a rational number?', 'a': '√2', 'b': 'π', 'c': '3/4', 'd': 'e', 'correct': 'C'},
            {'q': '2/3 + 1/3 = ?', 'a': '1', 'b': '3/3', 'c': '2/6', 'd': 'Both A and B', 'correct': 'D'},
            {'q': 'Reciprocal of 5/7?', 'a': '7/5', 'b': '5/7', 'c': '-5/7', 'd': '0', 'correct': 'A'},
            {'q': '(-1/2) × (4) = ?', 'a': '2', 'b': '-2', 'c': '1/2', 'd': '-1/8', 'correct': 'B'},
            {'q': 'Decimal of 1/4?', 'a': '0.20', 'b': '0.25', 'c': '0.30', 'd': '0.40', 'correct': 'B'},
        ]
    },
    {
        'title': 'Force and Pressure',
        'description': 'Physics: forces in nature',
        'subject': 'Science', 'grade_level': 8,
        'questions': [
            {'q': 'SI unit of force?', 'a': 'Joule', 'b': 'Newton', 'c': 'Pascal', 'd': 'Watt', 'correct': 'B'},
            {'q': 'Pressure = ?', 'a': 'Force × Area', 'b': 'Force / Area', 'c': 'Area / Force', 'd': 'Mass × Force', 'correct': 'B'},
            {'q': 'Force that opposes motion?', 'a': 'Gravity', 'b': 'Friction', 'c': 'Magnetic', 'd': 'Electric', 'correct': 'B'},
            {'q': 'Atmospheric pressure at sea level?', 'a': '1 atm', 'b': '2 atm', 'c': '5 atm', 'd': '10 atm', 'correct': 'A'},
        ]
    },
    {
        'title': 'Indian Constitution',
        'description': 'Civics and government',
        'subject': 'Social Studies', 'grade_level': 8,
        'questions': [
            {'q': 'India adopted Constitution on?', 'a': 'Aug 15, 1947', 'b': 'Jan 26, 1950', 'c': 'Oct 2, 1948', 'd': 'Nov 26, 1949', 'correct': 'D'},
            {'q': 'Who drafted Indian Constitution?', 'a': 'Nehru', 'b': 'Patel', 'c': 'Ambedkar', 'd': 'Bose', 'correct': 'C'},
            {'q': 'India is a ___', 'a': 'Monarchy', 'b': 'Democracy', 'c': 'Dictatorship', 'd': 'Theocracy', 'correct': 'B'},
            {'q': 'How many Fundamental Rights?', 'a': '5', 'b': '6', 'c': '7', 'd': '8', 'correct': 'B'},
        ]
    },

    # ========== GRADE 9 ==========
    {
        'title': 'Polynomials and Equations',
        'description': 'Algebra advanced',
        'subject': 'Mathematics', 'grade_level': 9,
        'questions': [
            {'q': 'Degree of x³ + 2x² + 1?', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'correct': 'C'},
            {'q': 'If p(x) = x² - 4, p(2) = ?', 'a': '0', 'b': '2', 'c': '4', 'd': '8', 'correct': 'A'},
            {'q': '(x+1)(x-1) = ?', 'a': 'x² + 1', 'b': 'x² - 1', 'c': 'x² + x', 'd': 'x² - x', 'correct': 'B'},
            {'q': 'Solve: 2x - 6 = 0', 'a': 'x = 2', 'b': 'x = 3', 'c': 'x = 4', 'd': 'x = 6', 'correct': 'B'},
            {'q': '(a + b)² = ?', 'a': 'a² + b²', 'b': 'a² - b²', 'c': 'a² + 2ab + b²', 'd': 'a² - 2ab + b²', 'correct': 'C'},
        ]
    },
    {
        'title': 'Matter in Our Surroundings',
        'description': 'States and properties of matter',
        'subject': 'Science', 'grade_level': 9,
        'questions': [
            {'q': 'States of matter?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'correct': 'B'},
            {'q': 'Plasma is found in?', 'a': 'Ice', 'b': 'Stars', 'c': 'Water', 'd': 'Rocks', 'correct': 'B'},
            {'q': 'Process of solid to gas?', 'a': 'Melting', 'b': 'Boiling', 'c': 'Sublimation', 'd': 'Freezing', 'correct': 'C'},
            {'q': 'Particles in solid?', 'a': 'Far apart', 'b': 'Close together', 'c': 'Moving fast', 'd': 'No arrangement', 'correct': 'B'},
            {'q': 'Evaporation is a ___', 'a': 'Slow process', 'b': 'Fast process', 'c': 'Sudden process', 'd': 'No change', 'correct': 'A'},
        ]
    },
    {
        'title': 'Literature Basics',
        'description': 'Understanding literary forms',
        'subject': 'English', 'grade_level': 9,
        'questions': [
            {'q': 'Author of "Romeo and Juliet"?', 'a': 'Dickens', 'b': 'Shakespeare', 'c': 'Wordsworth', 'd': 'Keats', 'correct': 'B'},
            {'q': 'A poem with 14 lines is?', 'a': 'Haiku', 'b': 'Sonnet', 'c': 'Ode', 'd': 'Ballad', 'correct': 'B'},
            {'q': 'Comparison using "like" or "as"?', 'a': 'Metaphor', 'b': 'Simile', 'c': 'Irony', 'd': 'Hyperbole', 'correct': 'B'},
            {'q': 'Author who wrote "Wings of Fire"?', 'a': 'Kalam', 'b': 'Tagore', 'c': 'Sen', 'd': 'Chetan', 'correct': 'A'},
        ]
    },

    # ========== GRADE 10 ==========
    {
        'title': 'Trigonometry Basics',
        'description': 'Sin, Cos, Tan fundamentals',
        'subject': 'Mathematics', 'grade_level': 10,
        'questions': [
            {'q': 'sin(0°) = ?', 'a': '0', 'b': '1', 'c': '1/2', 'd': '√2/2', 'correct': 'A'},
            {'q': 'cos(90°) = ?', 'a': '0', 'b': '1', 'c': '-1', 'd': '0.5', 'correct': 'A'},
            {'q': 'tan(45°) = ?', 'a': '0', 'b': '1', 'c': '√3', 'd': '1/√3', 'correct': 'B'},
            {'q': 'sin²θ + cos²θ = ?', 'a': '0', 'b': '1', 'c': '2', 'd': 'tan θ', 'correct': 'B'},
            {'q': 'sin(30°) = ?', 'a': '0', 'b': '1/2', 'c': '√3/2', 'd': '1', 'correct': 'B'},
        ]
    },
    {
        'title': 'Chemical Reactions',
        'description': 'Types of chemical changes',
        'subject': 'Science', 'grade_level': 10,
        'questions': [
            {'q': 'Rusting of iron is?', 'a': 'Physical change', 'b': 'Chemical change', 'c': 'No change', 'd': 'Reversible', 'correct': 'B'},
            {'q': 'Photosynthesis is what type?', 'a': 'Combination', 'b': 'Decomposition', 'c': 'Displacement', 'd': 'Double displacement', 'correct': 'B'},
            {'q': 'Balanced equation has equal?', 'a': 'Atoms', 'b': 'Volume', 'c': 'Weight only', 'd': 'Color', 'correct': 'A'},
            {'q': 'Symbol of Sodium?', 'a': 'So', 'b': 'Na', 'c': 'Sd', 'd': 'S', 'correct': 'B'},
            {'q': 'Chemical formula for water?', 'a': 'CO2', 'b': 'H2O', 'c': 'O2', 'd': 'H2', 'correct': 'B'},
        ]
    },
    {
        'title': 'Life Processes (Biology)',
        'description': 'Living organism functions',
        'subject': 'Science', 'grade_level': 10,
        'questions': [
            {'q': 'Process of breathing?', 'a': 'Respiration', 'b': 'Digestion', 'c': 'Excretion', 'd': 'Circulation', 'correct': 'A'},
            {'q': 'Site of photosynthesis?', 'a': 'Root', 'b': 'Stem', 'c': 'Chloroplast', 'd': 'Flower', 'correct': 'C'},
            {'q': 'Largest organ in human body?', 'a': 'Heart', 'b': 'Liver', 'c': 'Skin', 'd': 'Brain', 'correct': 'C'},
            {'q': 'Blood is pumped by?', 'a': 'Lungs', 'b': 'Heart', 'c': 'Kidney', 'd': 'Liver', 'correct': 'B'},
        ]
    },
    {
        'title': 'Resource and Development',
        'description': 'Geography and economics',
        'subject': 'Social Studies', 'grade_level': 10,
        'questions': [
            {'q': 'Type of renewable resource?', 'a': 'Coal', 'b': 'Petroleum', 'c': 'Solar', 'd': 'Natural gas', 'correct': 'C'},
            {'q': 'Black soil is good for?', 'a': 'Rice', 'b': 'Cotton', 'c': 'Wheat', 'd': 'Tea', 'correct': 'B'},
            {'q': 'India\'s major source of energy?', 'a': 'Wind', 'b': 'Coal', 'c': 'Solar', 'd': 'Nuclear', 'correct': 'B'},
            {'q': 'GDP stands for?', 'a': 'Gross Daily Product', 'b': 'Gross Domestic Product', 'c': 'General Domestic Price', 'd': 'Gross Demand Price', 'correct': 'B'},
        ]
    },
]


def load_content():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found. Run setup.py --sample-data first.")
            return

        existing_titles = {q.title for q in Quiz.query.all()}
        added = 0
        skipped = 0

        for quiz_data in NCERT_QUIZZES:
            if quiz_data['title'] in existing_titles:
                skipped += 1
                continue

            quiz = Quiz(
                title=quiz_data['title'],
                description=quiz_data['description'],
                subject=quiz_data['subject'],
                grade_level=quiz_data['grade_level'],
                created_by=teacher.id,
                total_questions=len(quiz_data['questions']),
                passing_score=60.0,
                is_published=True
            )
            db.session.add(quiz)
            db.session.flush()

            for idx, q in enumerate(quiz_data['questions']):
                question = QuizQuestion(
                    quiz_id=quiz.id,
                    question_text=q['q'],
                    question_type='mcq',
                    option_a=q.get('a'),
                    option_b=q.get('b'),
                    option_c=q.get('c'),
                    option_d=q.get('d'),
                    correct_option=q['correct'],
                    explanation=q.get('explanation', ''),
                    question_order=idx,
                    marks=1.0
                )
                db.session.add(question)

            added += 1
            print(f"[OK] Added: Grade {quiz_data['grade_level']} - {quiz_data['title']}")

        db.session.commit()
        print(f"\n[DONE] Added {added} new quizzes (skipped {skipped} existing)")
        print(f"Total NCERT quizzes in system: {Quiz.query.count()}")


if __name__ == '__main__':
    try:
        load_content()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
