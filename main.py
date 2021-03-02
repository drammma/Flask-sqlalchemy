from data import db_session
from data.job import Jobs

import datetime


def add_job(team_leader, job_, work_size, collaborators, start_date, is_finished):
    jobs = Jobs()
    jobs.team_leader = team_leader
    jobs.job = job_
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished

    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


def fill_base():
    temp_job = [(1, "deployment of residential modules 1 and 2", 15, "2, 3", datetime.datetime.now(), False),]
    for job in temp_job:
        try:
            add_job(*job)
        except Exception as e:
            print(e, e.__class__.__name__)


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")

    fill_base()
    print('-----')
