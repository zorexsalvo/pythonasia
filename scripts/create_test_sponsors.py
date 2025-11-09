#!/usr/bin/env python
"""
Standalone script to create test sponsors in the database.

Usage:
    python -m scripts.create_test_sponsors
    python -m scripts.create_test_sponsors --clear  # Clear existing sponsors first
"""

import argparse
from datetime import date

from app.sponsors.models import Sponsor


def create_test_sponsors(clear=False):
    """Create test sponsors in the database."""
    if clear:
        count = Sponsor.objects.count()
        Sponsor.objects.all().delete()
        print(f"⚠️  Deleted {count} existing sponsor(s)")

    # Organizers
    organizer_data = [
        {
            "name": "Python Philippines",
            "logo_url": "https://placehold.co/400x200?text=Python+Philippines",
            "website_url": "https://www.python.ph",
            "info": "Python Philippines is the premier community for Python developers in the Philippines.",
            "sponsorship_date": date(2024, 1, 1),
            "sponsor_type": Sponsor.SponsorType.ORGANIZER,
            "contact_name": "Community Team",
            "contact_email": "contact@python.ph",
        },
    ]

    # Institutional Sponsors
    institutional_data = [
        {
            "name": "University of the Philippines",
            "logo_url": "https://placehold.co/400x200?text=UP",
            "website_url": "https://www.up.edu.ph",
            "info": "The premier state university of the Philippines.",
            "sponsorship_date": date(2024, 2, 1),
            "sponsor_type": Sponsor.SponsorType.INSTITUTIONAL,
            "contact_name": "University Relations",
            "contact_email": "relations@up.edu.ph",
        },
        {
            "name": "Ateneo de Manila University",
            "logo_url": "https://placehold.co/400x200?text=Ateneo",
            "website_url": "https://www.ateneo.edu",
            "info": "A leading private university in the Philippines.",
            "sponsorship_date": date(2024, 2, 1),
            "sponsor_type": Sponsor.SponsorType.INSTITUTIONAL,
            "contact_name": "Events Office",
            "contact_email": "events@ateneo.edu",
        },
    ]

    # Keystone Sponsors
    keystone_data = [
        {
            "name": "TechCorp Solutions",
            "logo_url": "https://placehold.co/400x200?text=TechCorp",
            "website_url": "https://www.techcorp.example.com",
            "info": "Leading technology solutions provider in Southeast Asia.",
            "sponsorship_date": date(2024, 3, 1),
            "sponsor_type": Sponsor.SponsorType.KEYSTONE,
            "contact_name": "John Smith",
            "contact_email": "john.smith@techcorp.example.com",
        },
        {
            "name": "DataFlow Analytics",
            "logo_url": "https://placehold.co/400x200?text=DataFlow",
            "website_url": "https://www.dataflow.example.com",
            "info": "Advanced analytics and data science consulting firm.",
            "sponsorship_date": date(2024, 3, 1),
            "sponsor_type": Sponsor.SponsorType.KEYSTONE,
            "contact_name": "Maria Garcia",
            "contact_email": "maria.garcia@dataflow.example.com",
        },
    ]

    # Platinum Sponsors
    platinum_data = [
        {
            "name": "CloudTech Industries",
            "logo_url": "https://placehold.co/400x200?text=CloudTech",
            "website_url": "https://www.cloudtech.example.com",
            "info": "Cloud infrastructure and DevOps solutions provider.",
            "sponsorship_date": date(2024, 4, 1),
            "sponsor_type": Sponsor.SponsorType.PLATINUM,
            "contact_name": "Robert Lee",
            "contact_email": "robert.lee@cloudtech.example.com",
        },
        {
            "name": "CodeWorks Studio",
            "logo_url": "https://placehold.co/400x200?text=CodeWorks",
            "website_url": "https://www.codeworks.example.com",
            "info": "Software development and consulting company specializing in Python.",
            "sponsorship_date": date(2024, 4, 1),
            "sponsor_type": Sponsor.SponsorType.PLATINUM,
            "contact_name": "Sarah Chen",
            "contact_email": "sarah.chen@codeworks.example.com",
        },
        {
            "name": "AI Innovations Inc",
            "logo_url": "https://placehold.co/400x200?text=AI+Innovations",
            "website_url": "https://www.aiinnovations.example.com",
            "info": "Artificial intelligence and machine learning solutions provider.",
            "sponsorship_date": date(2024, 4, 1),
            "sponsor_type": Sponsor.SponsorType.PLATINUM,
            "contact_name": "David Kim",
            "contact_email": "david.kim@aiinnovations.example.com",
        },
    ]

    # Gold Sponsors
    gold_data = [
        {
            "name": "DevTools Pro",
            "logo_url": "https://placehold.co/400x200?text=DevTools",
            "website_url": "https://www.devtools.example.com",
            "info": "Developer tools and productivity solutions.",
            "sponsorship_date": date(2024, 5, 1),
            "sponsor_type": Sponsor.SponsorType.GOLD,
            "contact_name": "Emily Wong",
            "contact_email": "emily.wong@devtools.example.com",
        },
        {
            "name": "WebScale Systems",
            "logo_url": "https://placehold.co/400x200?text=WebScale",
            "website_url": "https://www.webscale.example.com",
            "info": "Scalable web application development and hosting services.",
            "sponsorship_date": date(2024, 5, 1),
            "sponsor_type": Sponsor.SponsorType.GOLD,
            "contact_name": "James Rodriguez",
            "contact_email": "james.rodriguez@webscale.example.com",
        },
        {
            "name": "SecureNet Solutions",
            "logo_url": "https://placehold.co/400x200?text=SecureNet",
            "website_url": "https://www.securenet.example.com",
            "info": "Cybersecurity and network solutions provider.",
            "sponsorship_date": date(2024, 5, 1),
            "sponsor_type": Sponsor.SponsorType.GOLD,
            "contact_name": "Lisa Tan",
            "contact_email": "lisa.tan@securenet.example.com",
        },
        {
            "name": "StartupHub",
            "logo_url": "https://placehold.co/400x200?text=StartupHub",
            "website_url": "https://www.startuphub.example.com",
            "info": "Incubator and accelerator for tech startups.",
            "sponsorship_date": date(2024, 5, 1),
            "sponsor_type": Sponsor.SponsorType.GOLD,
            "contact_name": "Michael Santos",
            "contact_email": "michael.santos@startuphub.example.com",
        },
    ]

    # Silver Sponsors
    silver_data = [
        {
            "name": "CodeMentor Academy",
            "logo_url": "https://placehold.co/400x200?text=CodeMentor",
            "website_url": "https://www.codementor.example.com",
            "info": "Online coding education platform.",
            "sponsorship_date": date(2024, 6, 1),
            "sponsor_type": Sponsor.SponsorType.SILVER,
            "contact_name": "Anna Cruz",
            "contact_email": "anna.cruz@codementor.example.com",
        },
        {
            "name": "TechJobs PH",
            "logo_url": "https://placehold.co/400x200?text=TechJobs",
            "website_url": "https://www.techjobs.example.com",
            "info": "Job board for tech professionals in the Philippines.",
            "sponsorship_date": date(2024, 6, 1),
            "sponsor_type": Sponsor.SponsorType.SILVER,
            "contact_name": "Carlos Rivera",
            "contact_email": "carlos.rivera@techjobs.example.com",
        },
        {
            "name": "DigitalCraft Studio",
            "logo_url": "https://placehold.co/400x200?text=DigitalCraft",
            "website_url": "https://www.digitalcraft.example.com",
            "info": "Digital design and development studio.",
            "sponsorship_date": date(2024, 6, 1),
            "sponsor_type": Sponsor.SponsorType.SILVER,
            "contact_name": "Patricia Lim",
            "contact_email": "patricia.lim@digitalcraft.example.com",
        },
    ]

    # Community Partners
    community_partner_data = [
        {
            "name": "PyData Manila",
            "logo_url": "https://placehold.co/400x200?text=PyData",
            "website_url": "https://www.pydata.example.com",
            "info": "Community for data science enthusiasts using Python.",
            "sponsorship_date": date(2024, 7, 1),
            "sponsor_type": Sponsor.SponsorType.COMMUNITY_PARTNER,
            "contact_name": "Community Organizer",
            "contact_email": "organizer@pydata.example.com",
        },
        {
            "name": "Django Philippines",
            "logo_url": "https://placehold.co/400x200?text=Django+PH",
            "website_url": "https://www.djangoph.example.com",
            "info": "Local Django community in the Philippines.",
            "sponsorship_date": date(2024, 7, 1),
            "sponsor_type": Sponsor.SponsorType.COMMUNITY_PARTNER,
            "contact_name": "Community Lead",
            "contact_email": "lead@djangoph.example.com",
        },
        {
            "name": "Women Who Code Manila",
            "logo_url": "https://placehold.co/400x200?text=WWCode",
            "website_url": "https://www.womenwhocode.example.com",
            "info": "Community empowering women in technology.",
            "sponsorship_date": date(2024, 7, 1),
            "sponsor_type": Sponsor.SponsorType.COMMUNITY_PARTNER,
            "contact_name": "Chapter Lead",
            "contact_email": "lead@womenwhocode.example.com",
        },
        {
            "name": "DevOps PH",
            "logo_url": "https://placehold.co/400x200?text=DevOps+PH",
            "website_url": "https://www.devopsph.example.com",
            "info": "DevOps community in the Philippines.",
            "sponsorship_date": date(2024, 7, 1),
            "sponsor_type": Sponsor.SponsorType.COMMUNITY_PARTNER,
            "contact_name": "Organizer",
            "contact_email": "organizer@devopsph.example.com",
        },
    ]

    # Wellness Partners
    wellness_partner_data = [
        {
            "name": "HealthFit Gym",
            "logo_url": "https://placehold.co/400x200?text=HealthFit",
            "website_url": "https://www.healthfit.example.com",
            "info": "Premium fitness and wellness center.",
            "sponsorship_date": date(2024, 8, 1),
            "sponsor_type": Sponsor.SponsorType.WELLNESS_PARTNER,
            "contact_name": "Events Coordinator",
            "contact_email": "events@healthfit.example.com",
        },
        {
            "name": "Mindful Moments",
            "logo_url": "https://placehold.co/400x200?text=Mindful",
            "website_url": "https://www.mindful.example.com",
            "info": "Meditation and mindfulness services.",
            "sponsorship_date": date(2024, 8, 1),
            "sponsor_type": Sponsor.SponsorType.WELLNESS_PARTNER,
            "contact_name": "Wellness Director",
            "contact_email": "wellness@mindful.example.com",
        },
    ]

    # Group all sponsors by type for reporting
    all_sponsors_by_type = {
        "Organizers": organizer_data,
        "Institutional": institutional_data,
        "Keystone": keystone_data,
        "Platinum": platinum_data,
        "Gold": gold_data,
        "Silver": silver_data,
        "Community Partners": community_partner_data,
        "Wellness Partners": wellness_partner_data,
    }

    # Create sponsors
    total_new = 0
    total_existing = 0

    for sponsor_type_name, sponsors_data in all_sponsors_by_type.items():
        created_list = []
        for data in sponsors_data:
            sponsor, created = Sponsor.objects.get_or_create(
                name=data["name"],
                defaults=data,
            )
            created_list.append((sponsor, created))

        new_count = sum(1 for _, created in created_list if created)
        existing_count = len(created_list) - new_count
        total_new += new_count
        total_existing += existing_count

        print(f"\n✓ {sponsor_type_name}:")
        print(f"  Created: {new_count}, Already existed: {existing_count}")

    print(f"\n✓ Total: {total_new} new sponsors created, {total_existing} already existed")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Create test sponsors in the database")
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all existing sponsors before creating new ones",
    )

    args = parser.parse_args()
    create_test_sponsors(clear=args.clear)


if __name__ == "__main__":
    main()
