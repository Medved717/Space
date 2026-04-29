import csv

data = [
    {'Country': 'Russia', 'Population (millions)': '146', 'GDP (billion USD)': '1700'},
    {'Country': 'USA', 'Population (millions)': '331', 'GDP (billion USD)': '25350'},
    {'Country': 'China', 'Population (millions)': '1412', 'GDP (billion USD)': '17700'},
    {'Country': 'India', 'Population (millions)': '1380', 'GDP (billion USD)': '3170'},
    {'Country': 'Germany', 'Population (millions)': '83', 'GDP (billion USD)': '4260'},
    {'Country': 'UK', 'Population (millions)': '67', 'GDP (billion USD)': '3070'},
    {'Country': 'France', 'Population (millions)': '68', 'GDP (billion USD)': '3050'},
    {'Country': 'Japan', 'Population (millions)': '126', 'GDP (billion USD)': '4910'},
    {'Country': 'South Korea', 'Population (millions)': '52', 'GDP (billion USD)': '1720'},
    {'Country': 'Brazil', 'Population (millions)': '213', 'GDP (billion USD)': '1610'},
    {'Country': 'Mexico', 'Population (millions)': '128', 'GDP (billion USD)': '1270'},
    {'Country': 'Indonesia', 'Population (millions)': '273', 'GDP (billion USD)': '1180'},
    {'Country': 'Pakistan', 'Population (millions)': '225', 'GDP (billion USD)': '265'},
    {'Country': 'Nigeria', 'Population (millions)': '211', 'GDP (billion USD)': '477'},
    {'Country': 'Bangladesh', 'Population (millions)': '165', 'GDP (billion USD)': '324'},
    {'Country': 'Italy', 'Population (millions)': '60', 'GDP (billion USD)': '2010'},
    {'Country': 'Canada', 'Population (millions)': '38', 'GDP (billion USD)': '2140'},
    {'Country': 'Saudi Arabia', 'Population (millions)': '35', 'GDP (billion USD)': '834'},
    {'Country': 'Australia', 'Population (millions)': '26', 'GDP (billion USD)': '1540'},
    {'Country': 'Spain', 'Population (millions)': '47', 'GDP (billion USD)': '1430'},
    {'Country': 'Argentina', 'Population (millions)': '45', 'GDP (billion USD)': '630'},
    {'Country': 'Poland', 'Population (millions)': '38', 'GDP (billion USD)': '622'},
    {'Country': 'Egypt', 'Population (millions)': '104', 'GDP (billion USD)': '404'},
    {'Country': 'Malaysia', 'Population (millions)': '33', 'GDP (billion USD)': '373'},
    {'Country': 'Netherlands', 'Population (millions)': '18', 'GDP (billion USD)': '992'},
    {'Country': 'Vietnam', 'Population (millions)': '98', 'GDP (billion USD)': '341'},
    {'Country': 'Iran', 'Population (millions)': '84', 'GDP (billion USD)': '240'},
    {'Country': 'Turkey', 'Population (millions)': '85', 'GDP (billion USD)': '745'},
    {'Country': 'Thailand', 'Population (millions)': '70', 'GDP (billion USD)': '544'},
    {'Country': 'UAE', 'Population (millions)': '10', 'GDP (billion USD)': '415'},
    {'Country': 'Switzerland', 'Population (millions)': '9', 'GDP (billion USD)': '801'},
    {'Country': 'Singapore', 'Population (millions)': '6', 'GDP (billion USD)': '397'},
    {'Country': 'Philippines', 'Population (millions)': '111', 'GDP (billion USD)': '367'},
    {'Country': 'Belgium', 'Population (millions)': '12', 'GDP (billion USD)': '586'},
    {'Country': 'Sweden', 'Population (millions)': '11', 'GDP (billion USD)': '551'},
    {'Country': 'Austria', 'Population (millions)': '9', 'GDP (billion USD)': '461'},
    {'Country': 'Norway', 'Population (millions)': '6', 'GDP (billion USD)': '482'},
    {'Country': 'Israel', 'Population (millions)': '10', 'GDP (billion USD)': '447'},
    {'Country': 'Ireland', 'Population (millions)': '5', 'GDP (billion USD)': '505'},
    {'Country': 'Denmark', 'Population (millions)': '6', 'GDP (billion USD)': '356'},
    {'Country': 'South Africa', 'Population (millions)': '60', 'GDP (billion USD)': '411'},
    {'Country': 'Colombia', 'Population (millions)': '51', 'GDP (billion USD)': '320'},
    {'Country': 'Chile', 'Population (millions)': '19', 'GDP (billion USD)': '300'},
    {'Country': 'Romania', 'Population (millions)': '19', 'GDP (billion USD)': '284'},
    {'Country': 'Czech Republic', 'Population (millions)': '11', 'GDP (billion USD)': '252'},
    {'Country': 'Peru', 'Population (millions)': '33', 'GDP (billion USD)': '230'},
    {'Country': 'Greece', 'Population (millions)': '11', 'GDP (billion USD)': '210'},
    {'Country': 'Portugal', 'Population (millions)': '11', 'GDP (billion USD)': '248'},
    {'Country': 'Qatar', 'Population (millions)': '3', 'GDP (billion USD)': '180'},
    {'Country': 'Kuwait', 'Population (millions)': '5', 'GDP (billion USD)': '135'}
]

with open('csv_files/county_dict.csv', 'w', newline='') as file:
    fieldnames = ['Country', 'Population (millions)', 'GDP (billion USD)']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for row in data:
        writer.writerow(row)
