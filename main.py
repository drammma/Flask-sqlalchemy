from flask import Flask, render_template, redirect

from data import db_session
from data.job import Jobs
from data.users import User
from data.LoginForm import LoginForm

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('login.html',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('login.html',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            email=form.email.data,

        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return render_template('success.html')
    return render_template('login.html', form=form)

def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
