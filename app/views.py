"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, send_from_directory, flash
from .forms import PropertyForm
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

@app.route('/files')
def files():
    plist = get_uploaded_images()
    return render_template('files.html', plist = plist)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    myform = PropertyForm()

    if request.method == 'POST':
        if myform.validate_on_submit():
            title = myform.title.data
            description = myform.description.data
            rooms = myform.rooms.data
            baths = myform.baths.data
            price = myform.price.data
            type = myform.type.data
            location = myform.location.data
            photo = myform.photo.data

            filename = secure_filename(photo.filename)

            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('home'))

    return render_template('createProperty.html', form=myform)

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def get_uploaded_images():
    rootdir = os.getcwd()

    print(rootdir + app.config['UPLOAD_FOLDER'])

    plist = []
    
    # for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            # print(os.path.join(subdir, file))
            # print(file)
            plist.append(file)

    return plist