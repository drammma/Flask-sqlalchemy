import sqlalchemy
from data import db_session
from data.users import User
from data.news import News


def add_user(name, about, email):
    user = User()
    user.name = name
    user.about = about
    user.email = email
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def fill_base():
    temp_users = [("Пользователь 1", "биография пользователя 1", "email@email.ru"),
                  ("Админ", "биография админа", "admin@email.ru"),
                  ("Гость", "-", "guest@email.ru")]
    for user in temp_users:
        try:
            add_user(*user)
        except Exception as e:
            print(e, e.__class__.__name__)

    temp_news = [(1, "Публичная запись", "ТестТест", False),
                 (2, "Запись от админа", "Что-нибудь", False)]
    for news in temp_news:
        try:
            add_news(*news)
        except Exception as e:
            print(e, e.__class__.__name__)


def add_news(user_id, title, content, is_private):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    news = News(title=title, content=content, is_private=is_private)
    user.news.append(news)
    db_sess.commit()


def print_users():
    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        print(user)


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")

    print_users()
    fill_base()
    print('-----')
    print_users()
