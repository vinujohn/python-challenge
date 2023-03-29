'''
Assignment:
Use the following API to retrieve sports results and sort into a table of results that are displayed
in the CLI. Each sport result contains several data and always includes the publication time.
Method: POST
Content-Type: application/json
Url: https://restest.free.beeceptor.com/results
Tasks:
- Create python script that displays the sports results in reverse chronological order in the
CLI.
- Add an argument to the script to display only certain types or events (e.g. f1Results)
- Add an argument to set the locale (e.g. en)
- How can you confirm the code works?
- Bonus: Implement the rest call asynchronously
'''
import argparse
import requests
import json
from datetime import datetime

URL = 'https://restest.free.beeceptor.com/results'

parser = argparse.ArgumentParser(
                    prog='Sports Results',
                    description='Displays a list of sport results on the command line')
parser.add_argument("--sport", help='limit events to a particular sport')

def sort_by_date_desc(event):
    date_str = event['publicationDate']
    date_obj = datetime.strptime(date_str, '%b %d, %Y %I:%M:%S %p')
    return date_obj

def display_results(data, sport_filter):
    # filter out results based on sport
    if sport_filter != None:
        if sport_filter in data:
            data = {sport_filter: data[sport_filter]}
        else:
            raise ValueError(sport_filter + " not found. please check spelling. Examples:(f1Results, nbaResults, Tennis)") 

    # sort events in reverse chronological order
    for sport in data:
        sorted_events = sorted(data[sport], key=sort_by_date_desc, reverse=True)
        data[sport] = sorted_events
    
    # print results to console
    print(json.dumps(data, indent=4))
    return

def main():
    args = parser.parse_args()

    # make request to http service
    try:
        rsp = requests.post(URL)
    except Exception as e:
        print("unable to connect to service.", e)
        return
    
    # parse json response and display results
    if rsp.status_code == 200:
        try:
            data = json.loads(rsp.content)
        except Exception as e:
            print("unable to convert response to json.", e)
        display_results(data, sport_filter=args.sport)
    else:
        print("invalid http status code received.", rsp.status_code, rsp.text)
    
if __name__ == "__main__":
    main()