from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Pet, Vaccine
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        if Vaccine.objects.exists() or Pet.objects.exists():
            print('Pet data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating vaccine data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vaccine(name=vaccine_name)
            vac.save()
        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./pet_data.csv')):
            pet = Pet()
            pet.name = row['Pet']
            pet.submitter = row['Submitter']
            pet.species = row['Species']
            pet.breed = row['Breed']
            pet.description = row['Pet Description']
            pet.sex = row['Sex']
            pet.age = row['Age']
            raw_submission_date = row['submission date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            pet.submission_date = submission_date
            pet.save()
            raw_vaccination_names = row['vaccinations']
            vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            for vac_name in vaccination_names:
                vac = Vaccine.objects.get(name=vac_name)
                pet.vaccinations.add(vac)
            pet.save()
