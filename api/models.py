from django.db import models

STATES = [('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
          ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]


AREA_UNITS = [('SqFt', 'SqFt')]


HOME_TYPES = [('APAR', 'Apartment'), ('COND', 'Condominium'),
              ('DUPL', 'Duplex'), ('MISC', 'Miscellaneous'),
              ('MF24', 'MultiFamily2To4'), ('SING', 'SingleFamily'),
              ('VARL', 'VacantResidentialLand'), ('UNKN', 'Unknown')]


class Rental(models.Model):
    area_unit = models.CharField(
        max_length=4, choices=AREA_UNITS, default='SqFt')
    bathrooms = models.FloatField(null=True)
    bedrooms = models.IntegerField(null=True)
    home_size = models.IntegerField(null=True)
    home_type = models.CharField(
        max_length=4, choices=HOME_TYPES, default='UNKN')
    last_sold_date = models.DateField(null=True)
    last_sold_price = models.IntegerField(null=True)
    link = models.CharField(max_length=150, null=True, unique=True)
    price = models.IntegerField(null=True)
    property_size = models.IntegerField(null=True)
    rent_price = models.IntegerField(null=True)
    rentzestimate_amount = models.IntegerField(null=True)
    rentzestimate_last_updated = models.DateField(null=True)
    tax_value = models.IntegerField(null=True)
    tax_year = models.IntegerField(null=True)
    year_built = models.IntegerField(null=True)
    zestimate_amount = models.IntegerField(null=True)
    zestimate_last_updated = models.DateField(null=True)
    zillow_id = models.CharField(max_length=20, null=True, unique=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, choices=STATES, null=True)
    zipcode = models.CharField(max_length=5, null=True)
