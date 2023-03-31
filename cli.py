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
import pandas as pd
import asyncio

URL = 'https://restest.free.beeceptor.com/results'

parser = argparse.ArgumentParser(
                    prog='Sports Results',
                    description='Displays a list of sport results on the command line')
parser.add_argument("--sport", help='limit events to a particular sport')

def get_publication_date_obj(event):
    date_str = event['publicationDate']
    date_obj = datetime.strptime(date_str, '%b %d, %Y %I:%M:%S %p')
    return date_obj

def filter_and_sort(json_data: dict, sport_filter: str):
    json_data = json_data.copy()
    # filter out results based on sport
    if sport_filter != None:
        if sport_filter in json_data:
            json_data = {sport_filter: json_data[sport_filter]}
        else:
            raise ValueError(sport_filter + " not found. please check spelling. Examples:(f1Results, nbaResults, Tennis)") 

    # sort events in reverse chronological order
    for sport in json_data:
        sorted_events = sorted(json_data[sport], key=get_publication_date_obj, reverse=True)
        json_data[sport] = sorted_events
    
    return json_data

async def make_request(url):
    return requests.post(url)

async def main():
    args = parser.parse_args()

    # make request to http service
    try:
        rsp = await make_request(url=URL)
    except Exception as e:
        print("unable to connect to service.", e)
        return
    
    # parse json response and display results
    if rsp.status_code == 200:
        try:
            data = json.loads(rsp.content)
        except Exception as e:
            print("unable to convert response to json.", e)
        results = filter_and_sort(data, sport_filter=args.sport)
        for sport in results:
            df = pd.DataFrame.from_dict(results[sport], orient='columns')
            print(sport)
            print(df.to_string())
            print("\n")
    else:
        print("invalid http status code received.", rsp.status_code, rsp.text)
    
if __name__ == "__main__":
    asyncio.run(main())