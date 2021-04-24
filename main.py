from flask import Flask, render_template

from data import db_session
from data.job import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    res = []
    for job in jobs:
        res.append({
            'job': job.job,
            'team_leader': f'{db_sess.query(User).filter(User.id == job.team_leader).first().name} {db_sess.query(User).filter(User.id == job.team_leader).first().surname}',
            'collaborators': job.collaborators,
            'work_size': job.work_size,
            'is_finished': 'is finished' if job.is_finished else 'is not finished',
        })
    return render_template("index.html", jobs=res)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
