"""
Standalone script to create test speakers in the database.

Usage:
    python -m scripts.create_test_speakers
    python -m scripts.create_test_speakers --clear  # Clear existing speakers first
"""

import argparse

from app.speakers.models import Speaker


def create_test_speakers(clear=False):
    """Create test speakers in the database."""
    if clear:
        count = Speaker.objects.count()
        Speaker.objects.all().delete()
        print(f"⚠️  Deleted {count} existing speaker(s)")

    # Featured/Keynote Speakers
    featured_speakers_data = [
        {
            "first_name": "JC",
            "last_name": "Peralta",
            "title": "Data Scientist & Climate Scientist",
            "introduction": (
                "JC Peralta is a data scientist, Geospatial Machine Learning "
                "Consultant, and Climate Scientist. He earned his Master's in "
                "Atmospheric Science from Ateneo de Manila University in 2019 and "
                "has worked on projects in climate science, disaster management, "
                "renewable energy, and climate action."
            ),
            "email": "jc.peralta@example.com",
            "is_featured": True,
            "photo_url": "https://placehold.co/400x400?text=JC+Peralta",
        },
        {
            "first_name": "Michael",
            "last_name": "Kennedy",
            "title": "Python Software Foundation Fellow",
            "introduction": (
                "Michael Kennedy is a Python Software Foundation Fellow, "
                "entrepreneur, and host of the Talk Python To Me and Python Bytes "
                "podcasts. He founded Talk Python Training, offering 250+ hours "
                "of online courses for developers and data scientists. He is based "
                "in Portland, OR."
            ),
            "email": "michael.kennedy@example.com",
            "is_featured": True,
            "photo_url": "https://placehold.co/400x400?text=Michael+Kennedy",
        },
        {
            "first_name": "Matt",
            "last_name": "Harrison",
            "title": "Stanford CS Expert & Author",
            "introduction": (
                "Matt Harrison is a Stanford-educated CS expert and bestselling "
                "author of Effective XGBoost and Effective Pandas. With 20+ years "
                "of Python experience, he has taught professionals at companies "
                "like Netflix and NASA and impacted thousands through live and "
                "online courses."
            ),
            "email": "matt.harrison@example.com",
            "is_featured": True,
            "photo_url": "https://placehold.co/400x400?text=Matt+Harrison",
        },
        {
            "first_name": "Reina",
            "middle_name": "Reyes",
            "last_name": "Reyes",
            "title": "Associate Professor, UP Diliman",
            "introduction": (
                'Reinabelle "Reina" Reyes, Ph.D., is an Associate Professor at '
                "UP Diliman's National Institute of Physics, where she leads the "
                "Data and Computation Research Group. She consults for Z-Lift "
                "Solutions and WeSolve Foundation and received the 2023 NAST "
                "Outstanding Young Scientist Award."
            ),
            "email": "reina.reyes@example.com",
            "is_featured": True,
            "photo_url": "https://placehold.co/400x400?text=Reina+Reyes",
        },
    ]

    # Regular Speakers
    regular_speakers_data = [
        {
            "first_name": "Athena",
            "middle_name": "Aliafe",
            "last_name": "Abe",
            "title": "Senior Software Engineer",
            "introduction": (
                "Athena Aliafe Abe is a senior software engineer with expertise "
                "in Python web development and data engineering. She has contributed "
                "to various open-source projects and is passionate about teaching "
                "programming to beginners."
            ),
            "email": "athena.abe@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Athena+Abe",
        },
        {
            "first_name": "Swastik",
            "last_name": "Anupam",
            "title": "ML Engineer",
            "introduction": (
                "Swastik Anupam is a machine learning engineer specializing in "
                "deep learning and computer vision. He has worked on projects "
                "involving image recognition and natural language processing."
            ),
            "email": "swastik.anupam@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Swastik+Anupam",
        },
        {
            "first_name": "Neil",
            "last_name": "Riego",
            "title": "DevOps Engineer",
            "introduction": (
                "Neil Riego is a DevOps engineer with extensive experience in "
                "containerization, CI/CD pipelines, and cloud infrastructure. "
                "He helps teams build scalable and reliable systems."
            ),
            "email": "neil.riego@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Neil+Riego",
        },
        {
            "first_name": "Ian",
            "last_name": "Panganiban",
            "title": "Backend Developer",
            "introduction": (
                "Ian Panganiban is a backend developer specializing in Django "
                "and RESTful API design. He has experience building high-performance "
                "web applications and APIs."
            ),
            "email": "ian.panganiban@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Ian+Panganiban",
        },
        {
            "first_name": "Fidel",
            "middle_name": "Ivan",
            "last_name": "Racines",
            "title": "Data Engineer",
            "introduction": (
                "Fidel Ivan Racines is a data engineer with expertise in building "
                "data pipelines and ETL processes. He works with big data "
                "technologies and helps organizations make data-driven decisions."
            ),
            "email": "fidel.racines@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Fidel+Racines",
        },
        {
            "first_name": "Albert",
            "last_name": "Yumol",
            "title": "Full Stack Developer",
            "introduction": (
                "Albert Yumol is a full stack developer with expertise in both "
                "frontend and backend technologies. He enjoys building end-to-end "
                "solutions and mentoring junior developers."
            ),
            "email": "albert.yumol@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Albert+Yumol",
        },
        {
            "first_name": "Yoshi",
            "last_name": "Yamaguchi",
            "title": "Python Consultant",
            "introduction": (
                "Yoshi Yamaguchi is a Python consultant with over 15 years of "
                "experience in software development. He specializes in code "
                "optimization and best practices."
            ),
            "email": "yoshi.yamaguchi@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Yoshi+Yamaguchi",
        },
        {
            "first_name": "Maria",
            "last_name": "Santos",
            "title": "AI Researcher",
            "introduction": (
                "Maria Santos is an AI researcher focusing on natural language "
                "processing and machine learning. She has published papers on "
                "sentiment analysis and text classification."
            ),
            "email": "maria.santos@example.com",
            "is_featured": False,
            "photo_url": "https://placehold.co/400x400?text=Maria+Santos",
        },
    ]

    # Create featured speakers
    created_featured = []
    for data in featured_speakers_data:
        speaker, created = Speaker.objects.get_or_create(
            email=data["email"],
            defaults=data,
        )
        created_featured.append((speaker, created))

    # Create regular speakers
    created_regular = []
    for data in regular_speakers_data:
        speaker, created = Speaker.objects.get_or_create(
            email=data["email"],
            defaults=data,
        )
        created_regular.append((speaker, created))

    # Report results
    featured_new = sum(1 for _, created in created_featured if created)
    featured_existing = len(created_featured) - featured_new
    regular_new = sum(1 for _, created in created_regular if created)
    regular_existing = len(created_regular) - regular_new

    print("\n✓ Featured Speakers:")
    print(f"  Created: {featured_new}, Already existed: {featured_existing}")

    print("\n✓ Regular Speakers:")
    print(f"  Created: {regular_new}, Already existed: {regular_existing}")

    total_new = featured_new + regular_new
    total_existing = featured_existing + regular_existing

    print(f"\n✓ Total: {total_new} new speakers created, {total_existing} already existed")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Create test speakers in the database")
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all existing speakers before creating new ones",
    )

    args = parser.parse_args()
    create_test_speakers(clear=args.clear)


if __name__ == "__main__":
    main()
