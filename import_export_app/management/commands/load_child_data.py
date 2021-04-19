from csv import DictReader
from django.core.management import BaseCommand
from import_export_app.models import Document

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from Document.csv"

    def handle(self, *args, **options):
        if Document.objects.exists():
            print('child data already loaded...exiting')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Loading Document data')
        for row in DictReader(open('media/file.csv')):
            document = Document(title=row['Title'], text=row['Text'],
                                date=row['Date'],
                                target=row['Target'],date_expired=row['date_expired'])
            document.save()
