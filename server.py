
from flask import Flask, jsonify, render_template
from model import connect_to_db, Checklist


app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/checklist/<int:checklist_id>')
def get_checklist(checklist_id):
    """Return a checklist from the database as JSON."""

    checklist = Checklist.query.get(checklist_id)

    if checklist:
        return jsonify({'status': 'success',
                        'checklist_id': checklist.checklist_id,
                        'templatename': checklist.templatename,
                        'timframe': checklist.timeframe,
                        'whofor': checklist.whofor})
    else:
        return jsonify({'status': 'error',
                        'message': 'No checklist found with that ID'})


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)