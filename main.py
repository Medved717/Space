import csv

rows = [
    ['Country', 'Population (millions)', 'GDP (billion USD)'],
    ['Russia', '146', '1700'],
    ['USA', '331', '25350'],
    ['China', '1412', '17700'],
    ['India', '1380', '3170'],
    ['Germany', '83', '4260'],
    ['UK', '67', '3070'],
    ['France', '68', '3050'],
    ['Japan', '126', '4910'],
    ['South Korea', '52', '1720'],
    ['Brazil', '213', '1610'],
    ['Mexico', '128', '1270'],
    ['Indonesia', '273', '1180'],
    ['Pakistan', '225', '265'],
    ['Nigeria', '211', '477'],
    ['Bangladesh', '165', '324'],
    ['Italy', '60', '2010'],
    ['Canada', '38', '2140'],
    ['Saudi Arabia', '35', '834'],
    ['Australia', '26', '1540'],
    ['Spain', '47', '1430'],
    ['Argentina', '45', '630'],
    ['Poland', '38', '622'],
    ['Egypt', '104', '404'],
    ['Malaysia', '33', '373'],
    ['Netherlands', '18', '992'],
    ['Vietnam', '98', '341'],
    ['Iran', '84', '240'],
    ['Turkey', '85', '745'],
    ['Thailand', '70', '544'],
    ['UAE', '10', '415'],
    ['Switzerland', '9', '801'],
    ['Singapore', '6', '397'],
    ['Philippines', '111', '367'],
    ['Belgium', '12', '586'],
    ['Sweden', '11', '551'],
    ['Austria', '9', '461'],
    ['Norway', '6', '482'],
    ['Israel', '10', '447'],
    ['Ireland', '5', '505'],
    ['Denmark', '6', '356'],
    ['South Africa', '60', '411'],
    ['Colombia', '51', '320'],
    ['Chile', '19', '300'],
    ['Romania', '19', '284'],
    ['Czech Republic', '11', '252'],
    ['Peru', '33', '230'],
    ['Greece', '11', '210'],
    ['Portugal', '11', '248'],
    ['Qatar', '3', '180'],
    ['Kuwait', '5', '135']
]

with open('countrys.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(rows)

with open('countrys.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




