"""Models for job app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )
    email = db.Column(db.String(50),
                      unique=True,
                      nullable=False,
                      )
    password = db.Column(db.String(25),
                         nullable=False,
                         )
    first_name = db.Column(db.String(50),
                           nullable=False
                           )
    last_name = db.Column(db.String(50),
                          nullable=False
                          )
    birthday = db.Column(db.Date, nullable=False)
    date_user_joined = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(17))
    login_occurrences = db.Column(db.Integer)
    phone_number = db.Column(db.String(12))

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Job(db.Model):
    """A job."""

    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True)
    job_title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    location = db.Column(db.String(75))
    seniority_level = db.Column(db.String(50))
    employment_type = db.Column(db.String(25))
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    url = db.Column(db.TinyText)

# Todo add Doc class
# class Document(db.Model):
