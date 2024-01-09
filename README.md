# WARN-scrape
Companies that are expecting to undergo mass layoffs must file a WARN notice in their respective states two months before layoffs begin. This application scrapes most states' warn lists and is set up to send out emails on a cron schedule detailing the companies who filed WARN notices by state.

This program is written in Python3.

## Running the Program

### Set Up Dotenv
Notify code developers for steps on how to create your `.env` file

### How to Run Database
`py db/setup.py`

### How to Run Email Service
`py main.py`

## Dependencies
- `pip install python-dotenv`
- `pip install psycopg2`
- `pip install requests`
- `pip install pandas`
