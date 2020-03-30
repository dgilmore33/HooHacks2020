import csv

with open("us_cities_states_counties.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        raw_data = row[0].split('|')
        try:
            print('%s is a city in %s' %(raw_data[0], raw_data[2]))
        except IndexError, msg:
            print("%s\nwe couldnt find it at %s" %(msg, raw_data[0]))
        #print('%s' %(row[0]))
        #print(f'{row["City"]} is a city in {row["State full"]}')

