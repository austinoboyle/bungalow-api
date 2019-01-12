---
title: API Reference - Bungalow

toc_footers:
  - <a href='https://github.com/lord/slate'>Documentation Powered by Slate</a>

search: true
---

# Introduction

Welcome to my API Docs!.  This API documentation page was created with [Slate](https://github.com/lord/slate). 

# Rentals

## Fields

These are all of the fields associated with a Rental object.

| name                       | description                                 | type   |
| -------------------------- | ------------------------------------------- | ------ |
| id                         | unique identified                           | int    |
| area_unit                  | Unit used to measure home_size              | string |
| bathrooms                  | Number of bathrooms                         | float  |
| bedroms                    | number of bedrooms                          | int    |
| home_size                  | Floor area (measured in area_unit)          | int    |
| home_type                  | Type of home (Apartment, SingleFamily, etc) | string |
| last_sold_date             | Last time the house was sold                | date   |
| last_sold_price            | price of the house last time it was sold    | int    |
| link                       | link to the place's listing                 | string |
| price                      | price of the listing                        | int    |
| property_size              | size of the entire property                 | int    |
| rent_price                 | monthly rent price of the listing           | int    |
| rentzestimate_amount       | zillow rental estimate amount               | int    |
| rentzestimate_last_updated | last time zillow updated the estimate       | date   |
| tax_value                  | Assessed value of the home                  | int    |
| tax_year                   | year of assessed value                      | int    |
| year_build                 | the year the home was built                 | int    |
| zestimate_amount           | Zillow's estimated home value               | int    |
| zestimate_last_updated     | last time resimated value was updated       | date   |
| zillow_id                  | unique identified on zillow                 | string |
| address                    | street address of the home                  | string |
| city                       | city the home is located                    | string |
| state                      | 2-letter state code                         | string |
| zipcode                    | zipcode of the listing address              | string |

### Home Type Codes

These are the possible values for the home_type field.

| Code | Home Type             |
| ---- | --------------------- |
| APAR | Apartment             |
| COND | Condominium           |
| DUPL | Duplex                |
| MF24 | MultiFamily2To4       |
| MISC | Miscallaneous         |
| SING | SingleFamily          |
| VARL | VacantResidentialLand |
| UNKN | Unknown               |


## Get All Rentals

This endpoint retrieves all rental properties.

> Example Request: `/api/rentals/?city=West+Hills&ordering=-price`

> Example response:

```json
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1346,
            "area_unit": "SqFt",
            "bathrooms": 2.0,
            "bedrooms": 4,
            "home_size": 1372,
            "home_type": "SING",
            "last_sold_date": null,
            "last_sold_price": null,
            "link": "https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/",
            "price": 739000,
            "property_size": 10611,
            "rent_price": null,
            "rentzestimate_amount": 2850,
            "rentzestimate_last_updated": "2018-08-07",
            "tax_value": 215083,
            "tax_year": 2017,
            "year_built": 1956,
            "zestimate_amount": 709630,
            "zestimate_last_updated": "2018-08-07",
            "zillow_id": "19866015",
            "address": "7417 Quimby Ave",
            "city": "West Hills",
            "state": "CA",
            "zipcode": "91307"
        },
        {
            "id": 1347,
            "area_unit": "SqFt",
            "bathrooms": 2.5,
            "bedrooms": 4,
            "home_size": 1490,
            "home_type": "SING",
            "last_sold_date": "2017-12-18",
            "last_sold_price": 720000,
            "link": "https://www.zillow.com/homedetails/7001-Vicky-Ave-West-Hills-CA-91307/19868265_zpid/",
            "price": 720000,
            "property_size": 7557,
            "rent_price": null,
            "rentzestimate_amount": 3000,
            "rentzestimate_last_updated": "2018-08-07",
            "tax_value": 535000,
            "tax_year": 2017,
            "year_built": 1958,
            "zestimate_amount": 703598,
            "zestimate_last_updated": "2018-08-07",
            "zillow_id": "19868265",
            "address": "7001 Vicky Ave",
            "city": "West Hills",
            "state": "CA",
            "zipcode": "91307"
        },
        ...
    ]
}
```

### HTTP Request

`GET {BASEURL}/api/rentals`

### Filtering & Sorting

The rentals can be filtered by any/all of the following fields using standard
querystring syntax:

`api/rentals/?field1=value1&field2=value2`

- bathrooms
- bedrooms
- home_type
- zillow_id
- city
- state
- zipcode

They can also be sorted in increasing/decreasing order by 1 of these
fields.  For descending order, use a '-' sign in front of the field name.

`api/rentals/?field1=value1&ordering=field2`

- price
- home_size
- rent_price
- rentzestimate_amount
- zestimate_amount



## Get a Specific Rental

> Example Request: `/api/rentals/1349`
> Example response:

```json
{
    "id": 1349,
    "area_unit": "SqFt",
    "bathrooms": 3.0,
    "bedrooms": 4,
    "home_size": 1800,
    "home_type": "SING",
    "last_sold_date": "2017-10-11",
    "last_sold_price": 1200000,
    "link": "https://www.zillow.com/homedetails/7143-Pomelo-Dr-West-Hills-CA-91307/19871789_zpid/",
    "price": 1200000,
    "property_size": 12196,
    "rent_price": null,
    "rentzestimate_amount": 3200,
    "rentzestimate_last_updated": "2018-08-07",
    "tax_value": 451808,
    "tax_year": 2017,
    "year_built": 1964,
    "zestimate_amount": 782165,
    "zestimate_last_updated": "2018-08-07",
    "zillow_id": "19871789",
    "address": "7143 Pomelo Dr",
    "city": "West Hills",
    "state": "CA",
    "zipcode": "91307"
}
```

Each rental record has an integer id associated with it.  You can query for
individual properties this way.

### HTTP Request

`GET {BASEURL}/api/rentals/RENTALID`

## Create a Rental

> Example Request: POST `/api/rentals/`

```json
{
    "bathrooms": 2.0,
    "bedrooms": 4,
    "home_size": 5000,
    "home_type": "APAR",
    "last_sold_price": 1000000,
    "price": 1200000,
    "property_size": 10000,
    "tax_year": 2017,
    "year_built": 1980,
    "address": "111 Bungalow Ct.",
    "city": "San Francisco",
    "state": "CA",
    "zipcode": "10101"
}
```

> Example response:

```json
{
    "id": 1794,
    "area_unit": "SqFt",
    "bathrooms": 2.0,
    "bedrooms": 4,
    "home_size": 5000,
    "home_type": "APAR",
    "last_sold_date": null,
    "last_sold_price": 1000000,
    "link": null,
    "price": 1200000,
    "property_size": 10000,
    "rent_price": null,
    "rentzestimate_amount": null,
    "rentzestimate_last_updated": null,
    "tax_value": null,
    "tax_year": 2017,
    "year_built": 1980,
    "zestimate_amount": null,
    "zestimate_last_updated": null,
    "zillow_id": null,
    "address": "111 Bungalow Ct.",
    "city": "San Francisco",
    "state": "CA",
    "zipcode": "10101"
}
```

Create a new rental.

### HTTP Request

`POST {BASEURL}/api/rentals`

## Update a Rental

> Example Request: PUT `/api/rentals/1349`

```json
{
    "price": 5555555
}
```

> Example response:

```json
{
    "id": 1349,
    "area_unit": "SqFt",
    "bathrooms": 3.0,
    "bedrooms": 4,
    "home_size": 1800,
    "home_type": "SING",
    "last_sold_date": "2017-10-11",
    "last_sold_price": 1200000,
    "link": "https://www.zillow.com/homedetails/7143-Pomelo-Dr-West-Hills-CA-91307/19871789_zpid/",
    "price": 5555555,
    "property_size": 12196,
    "rent_price": null,
    "rentzestimate_amount": 3200,
    "rentzestimate_last_updated": "2018-08-07",
    "tax_value": 451808,
    "tax_year": 2017,
    "year_built": 1964,
    "zestimate_amount": 782165,
    "zestimate_last_updated": "2018-08-07",
    "zillow_id": "19871789",
    "address": "7143 Pomelo Dr",
    "city": "West Hills",
    "state": "CA",
    "zipcode": "91307"
}
```

Update an existing rental.

### HTTP Request

`PUT {BASEURL}/api/rentals/RENTAL_ID`

## Delete a Rental

> Example Request: DELETE `/api/rentals/1349`

Delete a rental by id.

### HTTP Request

`DELETE {BASEURL}/api/rentals/RENTAL_ID`