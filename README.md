# Jobs.ac.uk scraper

Web scraper for job listings. Specifically, it scrapes the job listings from [jobs.ac.uk](https://www.jobs.ac.uk/), 
but with pretty minimal adjustments it can be used to scrape just about any job listing site.

## Usage

So, you want to scrape some job listings? Great! Here's how to do it.

First, you need to install the packages required to run the scraper. You can do this by running the following command:

    poetry install

After that, you can configure the scraper by altering the variables in the `scripts/pagination-generator.py` file. Replace
the `humanities/` part of the URL with the URL of the subject you want to scrape. Then, replace the ending range with 
whatever number you want to scrape up to. For example, if you want to scrape all the job listings for the subject `humanities`
up to page 100, you would replace `humanities/` with your subject (in this case we wouldn't change it), then you would adjust
`range(1, 12)` to `range(1, 100)`.

You can also alter the search terms by going into the `scripts/search-data.py` file and altering the search criteria on lines
9 and 18.

Once you've done that, you can run the scripts by running the following commands:

This generates the pagination URLs

    poetry run python scripts/pagination-generator.py 

This scrapes the job listing URLs from the pagination URLs

    poetry run python scripts/url-scraper.py

This scrapes the actual job listings

    poetry run python scripts/jobs-scraper.py

This searches all the job listings for specific search terms 

    poetry run python scripts/search-data.py 

Please note that the scripts must be run in the order they are listed above. If you run them in a different order, they will
not work.

## Output

The output of the scraper is a CSV file containing all the job listings. The CSV file is saved in the `output/` directory,
titled `rawJobsData.csv`. The CSV file contains the following columns: 

- `university_name`: The name of the university the job is at
- `job_title`: The title of the job
- `job_description`: The full description of the job 
- `advert_details`: The details of the job advert

The output of the search script are CSV files containing all the job listings that match the search criteria. The CSV file
is saved in the `output/` directory, titled `possibleJobs.csv` and `idealJobs.csv`. The CSV file contains the same content
as the `rawJobsData.csv` file, but only contains the job listings that match the search criteria.

Todo: Clean up the resulting raw data and make it more usable. Most importantly:
- add salary data
- add location data
- add job type data
- add link to job listing