from django.core.management.base import BaseCommand

import os
os.path.dirname(os.path.dirname(__file__))


class Command(BaseCommand):
    help = 'Transfers the contents of a mongo db to a sqlite db'

    def handle(self, *args, **options):
        os.system('python mongo_to_sqlite.py')
