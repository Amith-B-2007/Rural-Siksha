#!/usr/bin/env python
"""
Setup script to initialize the database and optionally load sample data
"""

import os
import sys
from app import create_app
from extensions import db
from backend.models import User, Resource

def init_db():
    """Initialize database"""
    app = create_app('development')
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("[OK] Database initialized")

def load_sample_data():
    """Load sample data for testing"""
    app = create_app('development')
    with app.app_context():
        # Check if sample data already exists
        if User.query.filter_by(email='student@example.com').first():
            print("Sample data already exists, skipping...")
            return

        print("Loading sample data...")

        # Create sample student
        student = User(
            email='student@example.com',
            full_name='Sample Student',
            role='student',
            grade_level=5
        )
        student.set_password('password123')

        # Create sample teacher
        teacher = User(
            email='teacher@example.com',
            full_name='Sample Teacher',
            role='teacher',
            subject='Mathematics'
        )
        teacher.set_password('password123')

        db.session.add(student)
        db.session.add(teacher)
        db.session.commit()

        print("[OK] Sample users created:")
        print("  Student: student@example.com / password123")
        print("  Teacher: teacher@example.com / password123")

if __name__ == '__main__':
    try:
        init_db()

        if '--sample-data' in sys.argv:
            load_sample_data()

        print("\n[OK] Setup complete!")
        print("\nTo run the app:")
        print("  python app.py")
        print("\nThen open http://localhost:5000 in your browser")

    except Exception as e:
        print(f"[ERROR] Setup failed: {e}")
        sys.exit(1)
