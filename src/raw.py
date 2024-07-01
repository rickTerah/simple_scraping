import requests
from bs4 import BeautifulSoup

from src.save import save_to_csv


def get_job_titles(url):
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')

    job_titles_elements = soup.find_all(
        'a', {'class': 'text-loading-animate text-loading-animate-link'})

    job_titles = []

    for element in job_titles_elements:
        job_titles.append(element.text.strip())

    with open('job_titles.csv', 'w') as file:
        for title in job_titles:
            file.write(f'{title}\n')

    csv_data = [[title, "Nairobi, Kenya", "The Unique Company", "USD 4,500"]
                for title in job_titles]

    csv_data.insert(0, ['Title', 'Location', 'Company', 'Salary'])

    save_to_csv(csv_data, 'job_titles.csv')

    return job_titles
