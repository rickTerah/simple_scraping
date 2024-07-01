import csv


def save_to_csv(data, filename):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
