"""Skills 5: SQLAlchemy & AJAX

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Template(db.Model):
    """Data model for a Template."""

    __tablename__ = 'templates'

    template_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    templatename = db.Column(db.String(25), nullable=False)
    createdby = db.Column(db.String(25), nullable=False)
    createdon = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printing."""

        return f'<Template template_id={self.template_id} templatename={self.templatename}>'


class Animal(db.Model):
    """Data model for an animal."""

    __tablename__ = 'animals'

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)

    template_id = db.Column(db.Integer,
                         db.ForeignKey('templates.template_id'),
                         nullable=False)
    Template = db.relationship('Template', backref='animals')

    def __repr__(self):
        """Provide helpful representation when printing."""

        # Sometimes, to avoid messy concatenation, it's ok to have your string
        # go past the 80-charcter line limit
        return f'<Animal animal_id={self.animal_id} name={self.name}> animal_species={self.animal_species}'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
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
