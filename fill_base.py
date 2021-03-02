from data import db_session
from data.users import User


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def fill_base():
    temp_users = [("Scott", "Ridley", "21", "captain", "research engineer", "module_1", "scott_chief@mars.org"),
                  ("Mett", "Lonely", "37", "colonist", "human", "module_2", "lonelymett@mars.org"),
                  ("Daiv", "Lonely", "34", "colonist", "psychiatrist", "module_2", "MrDLon@mars.org"),
                  ("Honor", "Pettersen", "18", "colonist", "student", "module_9", "AnnaAndreevnaZactite@please.org")]
    for user in temp_users:
        try:
            add_user(*user)
        except Exception as e:
            print(e, e.__class__.__name__)


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")

    fill_base()
    print('-----')

