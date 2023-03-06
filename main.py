from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/sqlachemy.db")
db_sess = db_session.create_session()


@app.route('/')
def index():
    s = []
    for job in db_sess.query(Jobs).all():
        teams = [job.job, job.team_leader, job.work_size, job.collaborators, job.is_finished]
        s.append(teams)
    for i in s:
        for user in db_sess.query(User).filter(User.id == int(i[1])):
            i[1] = (user.surname, user.name)
        if i[-1]:
            i[-1] = "Is finished"
        else:
            i[-1] = "Is not finished"
    return render_template("index.html", ex=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)