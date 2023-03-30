## Install dependencies
```
>pip install -r requirements.txt
```

## Usage
```
>python3 cli.py -h
usage: Sports Results [-h] [--sport SPORT]

Displays a list of sport results on the command line

optional arguments:
  -h, --help     show this help message and exit
  --sport SPORT  limit events to a particular sport
```

## Run Unit Test
```
>python3 test_cli_unittests.py
```

## Tasks:
- Create python script that displays the sports results in reverse chronological order in the CLI.
    - [x] Completed
- Add an argument to the script to display only certain types or events (e.g. f1Results)
    - [x] Completed
- Add an argument to set the locale (e.g. en)
    - [ ] Not Complete. Note: results from the endpoint given do not include any `locale` info.  The REST endpoint itself doesn't seem to support a `locale` query string param.
- How can you confirm the code works?
    - [x] Completed. We can test this code in a number of ways via unit tests and integration tests.  Unit tests could mock out the REST api call so that the entire script could be tested or we could test specific functions that we care about that avoid the REST call altogether.  The latter was provided for this solution.  Integration tests could verify that the REST api call itself was working correctly and that any error scenarios are correctly handled.
- Bonus: Implement the rest call asynchronously
    - [x] Completed