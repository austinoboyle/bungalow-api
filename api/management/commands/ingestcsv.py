from django.core.management.base import BaseCommand, CommandError
from api.models import Rental, HOME_TYPES
import pandas as pd
from datetime import datetime

homeTypeMapping = dict(map(reversed, HOME_TYPES))


def toShortCode(field, value):
    """
    Convert a value of type 'field' to it's shortened version in the database

    Currently only used for home_type, could be extended for anything.
    """
    if field == 'home_type':
        return homeTypeMapping[value]
    return value


def priceToInt(price):
    """
    Convert price strings to integers

    Example:
        - $12.5K -> 12000
        - $0.37M -> 370000
    """
    if not price:
        return None
    unit = price[-1]
    base = float(price.replace('$', '')[:-1])
    if unit.lower() == 'k':
        return int(base * 1000)
    elif unit.lower() == 'm':
        return int(base * 1000000)


def formatDate(date):
    """
    Convert dates from MM/DD/YYYY to YYYY-MM-DD
    """
    if not date:
        return None
    return datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')


class Command(BaseCommand):
    help = 'Ingest a csv file into the Rentals model'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+')

    def handle(self, *args, **options):
        date_fields = ['last_sold_date',
                       'rentzestimate_last_updated', 'zestimate_last_updated']

        for name in options['filename']:  # Will handle multiple files
            try:
                df = pd.read_csv(name, header=0)
                # Convert empty values to None
                df = df.where((pd.notnull(df)), None)
                df['price'] = df['price'].map(priceToInt)
                df['home_type'] = df['home_type'].map(
                    lambda x: toShortCode('home_type', x))
                for field in date_fields:
                    df[field] = df[field].map(formatDate)
                rentals = [Rental(**rec) for rec in df.to_dict('records')]
                Rental.objects.bulk_create(rentals)
                self.stdout.write(self.style.SUCCESS(
                    'Successfully ingested {}'.format(name)))
            except Exception as e:
                self.stderr.write('Failed to ingest {}'.format(name))
                self.stderr.write(str(e))

        self.stdout.write("Done")
