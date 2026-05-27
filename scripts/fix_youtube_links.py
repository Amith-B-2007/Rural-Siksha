"""
Fix YouTube links - Use SEARCH URLs that always work
Instead of specific video IDs that can break, use search queries
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from urllib.parse import quote
from app import create_app
from extensions import db
from backend.models import Resource


def get_search_url(title, subject, grade):
    """Generate a YouTube search URL that always returns relevant results"""
    # Build a smart search query
    if subject in ['Hindi', 'Kannada']:
        query = f"learn {subject} for class {grade} students {title}"
    else:
        query = f"NCERT class {grade} {subject} {title} explanation"

    # URL encode the search query
    encoded = quote(query)
    return f"https://www.youtube.com/results?search_query={encoded}"


def get_channel(subject):
    """Get a recommended channel based on subject"""
    channels = {
        'Mathematics': 'Magnet Brains',
        'Science': 'Magnet Brains',
        'English': 'Magnet Brains',
        'Social Studies': 'Magnet Brains',
        'Hindi': 'Magnet Brains Hindi',
        'Kannada': 'Kannada Learning Tutor',
    }
    return channels.get(subject, 'Educational Channels')


def fix_all():
    app = create_app('development')
    with app.app_context():
        resources = Resource.query.all()
        print(f"Updating YouTube links for {len(resources)} resources...")
        print("=" * 60)

        updated = 0
        for r in resources:
            new_url = get_search_url(r.title, r.subject, r.grade_level)
            new_channel = get_channel(r.subject)

            r.youtube_url = new_url
            r.youtube_channel = new_channel
            updated += 1

            if updated % 10 == 0:
                print(f"  Updated {updated}/{len(resources)}...")

        db.session.commit()
        print("=" * 60)
        print(f"[DONE] Updated {updated} resources with reliable YouTube search URLs")
        print(f"\nSample URL: {resources[0].youtube_url[:100]}...")


if __name__ == '__main__':
    try:
        fix_all()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
