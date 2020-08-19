
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Data model for an animal."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Date(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    usertype = db.Column(db.String(), nullable=False)

    # user_id = db.Column(db.Integer,
    #                      db.ForeignKey('templates.user_id'),
    #                      nullable=False)
    # Template = db.relationship('Template', backref='users')

    def __repr__(self):
        """Provide helpful representation when printing."""

        return f'<User user_id={self.user_id} email={self.email}> username={self.username} usertype={self.usertype}'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///users'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
