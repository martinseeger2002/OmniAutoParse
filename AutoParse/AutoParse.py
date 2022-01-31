first_token = input('enter the "Property ID" number of first token in series \n')
last_token = input('enter the "Property ID" number of last token in series \n')


def omni_scraper():
    import json
    import requests
    import time

    url = "https://api.omnilite.org/v1/property/"
    prop_number = int(first_token)


    def create_output_txt():
        f = open('data.txt', 'w+')
        f.write('serial,data' + '\n')
        f.close()

    def add_to_output_txt():
        f = open('data.txt', 'a+')
        f.write(serial_number + ',' + d1 + d2 + d3 + '\n')
        f.close()

    def get_JSON_data(url):
        r = requests.get(url)
        global  d1, d2, d3, name, serial_number
        data = json.loads(r.text)    
        name = data['name']
        d3 = data['data']
        d1 = data['category']
        d2 = data['subcategory']
        serial_number = name[-5:]

    create_output_txt()

    while prop_number<=int(last_token):

        get_JSON_data(url + str(prop_number))
        print(d1,d2,d3)
    
        add_to_output_txt()

        prop_number=prop_number+1
        time.sleep(5)


def panda_sort():
    # importing pandas package
    import pandas as pd
  
    # assign dataset
    csvData = pd.read_csv("data.txt")
                                         
    # displaying unsorted data frame
    print("\nBefore sorting:")
    print(csvData)
  
    # sort data frame
    csvData.sort_values(["serial"], 
                        ascending=[True], 
                        inplace=True)
  
    # displaying sorted data frame
    print("\nAfter sorting:")
    print(csvData)
    csvData.to_csv('data.txt')

def convert_to_data_only():
    import pandas as pd

    def get_data():
    
        global base64_data
        # Then loading csv file
        df = pd.read_csv('data.txt')

        # converting ;data' column into list
        a = list(df['data'])

        # converting list into string and then joining it with space
        base64_data = ' '.join(str(e) for e in a)
    
    get_data()
    print(base64_data)

    f = open('data.txt', 'w+')
    f.write(base64_data)
    f.close()

omni_scraper()
panda_sort()
convert_to_data_only()
