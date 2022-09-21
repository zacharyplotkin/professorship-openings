import csv


def write_to_csv(list_input, csv_file):
    # The information will be written to a CSV here.
    try:
        with open(csv_file, "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen, lineterminator='\n')
            csv_writer.writerow(list_input)
    except Exception as e:
        print(e)


# To change the number of pages, change the second value in the range function. To change the URL, just
# adjust "humanities/" to whatever you want.
for i in range(1, 12):
    write_to_csv(["humanities/" + str(i)], "./input/paginationList.txt")