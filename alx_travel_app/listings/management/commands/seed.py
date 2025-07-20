from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING('Listings already exist. Skipping seeding.'))
            return

        sample_titles = [
            "Cozy Beachfront Villa",
            "Modern Apartment in City Center",
            "Charming Cabin in the Woods",
            "Luxurious Downtown Loft",
            "Rustic Mountain Retreat"
        ]

        for title in sample_titles:
            listing = Listing.objects.create(
                title=title,
                description=f"This is a beautiful place: {title}",
                price_per_night=random.randint(50, 300),
                max_guests=random.randint(2, 10),
                location=random.choice(["Nairobi", "Mombasa", "Naivasha", "Diani", "Kisumu"])
            )
            self.stdout.write(self.style.SUCCESS(f'Added listing: {listing.title}'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
