from fastapi import FastAPI

from src.raw import get_job_titles


app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Welcome to this fantastic app!'}


@app.get('/titles')
def read_job_titles():
    url = 'https://www.brightermonday.co.ke/jobs'
    job_titles = get_job_titles(url)
    return {'job_titles': job_titles}
