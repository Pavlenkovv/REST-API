from django.core.management.base import BaseCommand, CommandError
from mainapp.models import NewsPost


class Command(BaseCommand):
    help = 'Reset all upvotes'

    def handle(self, *args, **options):
        NewsPost.objects.all().update(amount_of_upvotes=0)
    print('well done')