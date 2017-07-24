from django.core.management.base import BaseCommand

import os
os.path.dirname(os.path.dirname(__file__))


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        os.system('python test3.py')
