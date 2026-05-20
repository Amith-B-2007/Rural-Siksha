"""
Load sample NCERT-aligned quizzes for testing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from extensions import db
from backend.models import User, Quiz, QuizQuestion

SAMPLE_QUIZZES = [
    {
        'title': 'Basic Arithmetic Quiz',
        'description': 'Test your basic math skills',
        'subject': 'Mathematics',
        'grade_level': 5,
        'passing_score': 60.0,
        'time_limit_minutes': 15,
        'questions': [
            {
                'question_text': 'What is 25 + 17?',
                'question_type': 'mcq',
                'option_a': '40', 'option_b': '42', 'option_c': '44', 'option_d': '46',
                'correct_option': 'B',
                'explanation': '25 + 17 = 42'
            },
            {
                'question_text': 'What is 8 x 7?',
                'question_type': 'mcq',
                'option_a': '54', 'option_b': '55', 'option_c': '56', 'option_d': '57',
                'correct_option': 'C',
                'explanation': '8 x 7 = 56'
            },
            {
                'question_text': 'What is 144 / 12?',
                'question_type': 'mcq',
                'option_a': '10', 'option_b': '11', 'option_c': '12', 'option_d': '13',
                'correct_option': 'C',
                'explanation': '144 / 12 = 12'
            },
            {
                'question_text': 'What is 100 - 37?',
                'question_type': 'mcq',
                'option_a': '63', 'option_b': '67', 'option_c': '73', 'option_d': '77',
                'correct_option': 'A',
                'explanation': '100 - 37 = 63'
            },
            {
                'question_text': 'Write the number 245 in words.',
                'question_type': 'short_answer',
                'expected_answer': 'two hundred forty-five',
                'explanation': '245 is "two hundred forty-five"'
            }
        ]
    },
    {
        'title': 'Science: Plants and Animals',
        'description': 'Test your knowledge about living things',
        'subject': 'Science',
        'grade_level': 5,
        'passing_score': 60.0,
        'questions': [
            {
                'question_text': 'Which part of the plant makes food?',
                'question_type': 'mcq',
                'option_a': 'Root', 'option_b': 'Stem', 'option_c': 'Leaf', 'option_d': 'Flower',
                'correct_option': 'C',
                'explanation': 'Leaves contain chlorophyll and perform photosynthesis to make food.'
            },
            {
                'question_text': 'Which animal is a mammal?',
                'question_type': 'mcq',
                'option_a': 'Fish', 'option_b': 'Bird', 'option_c': 'Snake', 'option_d': 'Dog',
                'correct_option': 'D',
                'explanation': 'Dogs are mammals - they give birth to young and feed them milk.'
            },
            {
                'question_text': 'Plants need ___ to make food.',
                'question_type': 'mcq',
                'option_a': 'Sunlight', 'option_b': 'Moonlight', 'option_c': 'Darkness', 'option_d': 'Cold',
                'correct_option': 'A',
                'explanation': 'Plants need sunlight for photosynthesis.'
            },
            {
                'question_text': 'Name three parts of a plant.',
                'question_type': 'short_answer',
                'expected_answer': 'root stem leaf',
                'explanation': 'A plant has roots, stem, leaves, flowers, and fruits.'
            }
        ]
    },
    {
        'title': 'English: Basic Grammar',
        'description': 'Test your grammar skills',
        'subject': 'English',
        'grade_level': 5,
        'passing_score': 60.0,
        'questions': [
            {
                'question_text': 'Which word is a noun?',
                'question_type': 'mcq',
                'option_a': 'Run', 'option_b': 'Book', 'option_c': 'Quickly', 'option_d': 'Beautiful',
                'correct_option': 'B',
                'explanation': '"Book" is a noun - it names a thing.'
            },
            {
                'question_text': 'Choose the correct plural of "child":',
                'question_type': 'mcq',
                'option_a': 'Childs', 'option_b': 'Childes', 'option_c': 'Children', 'option_d': 'Childrens',
                'correct_option': 'C',
                'explanation': 'The plural of "child" is "children" (irregular plural).'
            },
            {
                'question_text': 'Which is an adjective?',
                'question_type': 'mcq',
                'option_a': 'Happy', 'option_b': 'Eat', 'option_c': 'School', 'option_d': 'Tree',
                'correct_option': 'A',
                'explanation': '"Happy" describes a feeling - it is an adjective.'
            }
        ]
    },
    {
        'title': 'Social Studies: India Basics',
        'description': 'Learn about India',
        'subject': 'Social Studies',
        'grade_level': 5,
        'passing_score': 60.0,
        'questions': [
            {
                'question_text': 'What is the capital of India?',
                'question_type': 'mcq',
                'option_a': 'Mumbai', 'option_b': 'New Delhi', 'option_c': 'Kolkata', 'option_d': 'Chennai',
                'correct_option': 'B',
                'explanation': 'New Delhi is the capital of India.'
            },
            {
                'question_text': 'India\'s national flag has how many colors?',
                'question_type': 'mcq',
                'option_a': '2', 'option_b': '3', 'option_c': '4', 'option_d': '5',
                'correct_option': 'B',
                'explanation': 'The Indian flag has 3 colors: saffron, white, and green.'
            },
            {
                'question_text': 'Who is known as the Father of the Nation in India?',
                'question_type': 'mcq',
                'option_a': 'Nehru', 'option_b': 'Patel', 'option_c': 'Gandhi', 'option_d': 'Bose',
                'correct_option': 'C',
                'explanation': 'Mahatma Gandhi is known as the Father of the Nation.'
            }
        ]
    }
]


def load_quizzes():
    app = create_app('development')
    with app.app_context():
        # Get the sample teacher
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Sample teacher not found. Run setup.py --sample-data first.")
            return

        # Check existing quizzes
        existing_titles = {q.title for q in Quiz.query.all()}

        added = 0
        for quiz_data in SAMPLE_QUIZZES:
            if quiz_data['title'] in existing_titles:
                continue

            quiz = Quiz(
                title=quiz_data['title'],
                description=quiz_data['description'],
                subject=quiz_data['subject'],
                grade_level=quiz_data['grade_level'],
                created_by=teacher.id,
                total_questions=len(quiz_data['questions']),
                passing_score=quiz_data['passing_score'],
                time_limit_minutes=quiz_data.get('time_limit_minutes'),
                is_published=True
            )
            db.session.add(quiz)
            db.session.flush()

            for idx, q in enumerate(quiz_data['questions']):
                question = QuizQuestion(
                    quiz_id=quiz.id,
                    question_text=q['question_text'],
                    question_type=q['question_type'],
                    option_a=q.get('option_a'),
                    option_b=q.get('option_b'),
                    option_c=q.get('option_c'),
                    option_d=q.get('option_d'),
                    correct_option=q.get('correct_option'),
                    expected_answer=q.get('expected_answer'),
                    explanation=q.get('explanation'),
                    question_order=idx,
                    marks=1.0
                )
                db.session.add(question)

            added += 1
            print(f"[OK] Added quiz: {quiz_data['title']}")

        db.session.commit()
        print(f"\n[OK] Added {added} new sample quizzes")


if __name__ == '__main__':
    try:
        load_quizzes()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
