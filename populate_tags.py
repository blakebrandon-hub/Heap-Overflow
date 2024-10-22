import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heap_overload.settings')
django.setup()

from heap.models import Tag

tags = [
    {'name': 'Javascript'},
    {'name': 'HTML'},
    {'name': 'CSS'},
    {'name': 'AWS'},
    {'name': 'SQL'},
    {'name': 'Git'},
    {'name': 'Stripe'},
    {'name': 'Automation'},
    {'name': 'Web Scraping'},
]

for tag in tags:
    Tag.objects.create(**tag)

print("Tag(s) added successfully!")