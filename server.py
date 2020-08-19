
from flask import Flask, jsonify, render_template
from model import connect_to_db, User


app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    """Return a user from the database as JSON."""

    user = User.query.get(user_id)

    if user:
        return jsonify({'status': 'success',
                        'user_id': user.user_id,
                        'email': user.email,
                        'username': user.username,
                        'usertype': user.usertype})
    else:
        return jsonify({'status': 'error',
                        'message': 'No user found with that ID'})


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)