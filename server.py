
from flask import Flask, jsonify, render_template
from model import connect_to_db, Template


app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/template/<int:template_id>')
def get_template(template_id):
    """Return a template from the database as JSON."""

    template = Template.query.get(template_id)

    if template:
        return jsonify({'status': 'success',
                        'template_id': template.template_id,
                        'templatename': template.templatename,
                        'createdby': template.createdby,
                        'createdon': template.createdon})
    else:
        return jsonify({'status': 'error',
                        'message': 'No template found with that ID'})


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)