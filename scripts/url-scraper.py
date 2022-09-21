from bs4 import BeautifulSoup
import csv
import re
import requests
import time


def write_to_csv(list_input, csv_file):
    # The scraped info will be written to a CSV here.
    try:
        with open(csv_file, "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen, lineterminator='\n')
            csv_writer.writerow(list_input)
    except Exception as e:
        print(e)


def scrape(source_url, soup):
    cards = soup.find_all("div", class_="j-doorway__text")

    for card in cards:
        url = card.find("a", href=True)
        write_to_csv([url], "./jobs/jobsRaw.txt")


def browse_and_scrape(seed_url, job_page=0):
    url_path = re.compile(r"(https://.*\.uk)")
    source_url = url_path.search(seed_url).group(0)

    # I don't know what this actually does, but it's in the original code I
    # wrote a while ago. I'm not sure why I put it in or if/why it's needed,
    # but I'm leaving it in for now cuz it works.

    formatted_url = seed_url.format(str(jobpage[job_page].replace("\n", "")))

    try:
        html_text = requests.get(formatted_url).text
        soup = BeautifulSoup(html_text, "html.parser")

        print(url_path.search(seed_url))
        scrape(source_url, soup)

        time.sleep(1)
        job_page += 1

        print(str(job_page) + "/" + str(len(jobpage)))
        print(f"Now Scraping - {formatted_url}")
        print(jobpage[job_page])

        browse_and_scrape(seed_url, job_page)

    except Exception as e:
        return e


def parse_urls():
    with open("./jobs/jobsRaw.txt", "r") as fopen:
        csv_reader = csv.reader(fopen)
        for line in csv_reader:
            write_to_csv([line[0].split('"')[1]], "./jobs/jobsParsed.txt")


if __name__ == "__main__":
    paginationList = open('./input/paginationList.txt')
    jobpage = paginationList.readlines()
    seed_url = "https://www.jobs.ac.uk/categories/{}"
    print("Web scraping has begun")
    result = browse_and_scrape(seed_url)
    if result is not True:
        parse_urls()
