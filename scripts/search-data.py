import csv

with open('./output/rawJobsData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('./output/possibleJobs.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', lineterminator='\n')
        for line in csv_reader:
            # add search terms and keywords here
            if ('interdisciplinary' or 'environmental humanities' or 'comparative literature') in line[2].lower():
                csv_writer.writerow(line)

with open('./output/possibleJobs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('./output/idealJobs.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', lineterminator='\n')
        for line in csv_reader:
            # add ideal search keywords here
            if ('full time' or 'tenure track') in line[2].lower():
                csv_writer.writerow(line)
