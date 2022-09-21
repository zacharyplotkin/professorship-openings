from bs4 import BeautifulSoup
import csv
import re
import requests
import time


def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("./output/rawJobsData.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen, lineterminator='\n')
            csv_writer.writerow(list_input)
    except Exception as e:
        print(e)


def scrape(source_url, soup):
    jobdata = soup.find_all("div", class_="sub-grid column-1 edge-span-2-mobile")

    for job_data in jobdata:

        if job_data.find("h1") is not None:
            # find the university name
            university_name = job_data.find("h3").text.strip()
            # find the job title
            position_name = job_data.find("h1").text.strip()
            # find the job description
            job_description = job_data.find("div", {"id": "job-description"}).text.strip()
            # find the job details
            advert_details = job_data.find("div", class_="j-advert-details__container").text.strip()
            write_to_csv([university_name, position_name, job_description, advert_details])
        else:
            continue


def browse_and_scrape(seed_url, job_page=0):
    url_path = re.compile(r"(https://.*\.uk)")
    source_url = url_path.search(seed_url).group(0)

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


if __name__ == "__main__":
    joblist = open('./jobs/jobsParsed.txt')
    jobpage = joblist.readlines()
    seed_url = "https://www.jobs.ac.uk/{}"
    print("Web scraping has begun")
    result = browse_and_scrape(seed_url)
    if result is not True:
        print("Web scraping is now complete!")
