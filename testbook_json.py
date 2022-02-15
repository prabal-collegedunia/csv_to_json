import csv
import json
import sys
maxInt = sys.maxsize



def build_json(csv_file_path, json_file_path):

    json_data ={}

    # Open a csv reader called dict_reader
    with open(csv_file_path, encoding = 'utf-8') as csvf:
        csvReader = csv.DictReader(csvf,delimiter='|',quoting=csv.QUOTE_NONE)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            json_data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(json_data, indent=4))

## driver code


while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

csv_file_path = r'SSC_Steno_Previous_Paper_20__Held_on__24_Dec_2020_Shift_2.csv'
json_file_path = r'SSC_Steno.json'
 
# Call the make_json function
build_json(csv_file_path, json_file_path)
