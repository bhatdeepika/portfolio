import csv
import email
from lib2to3.pgen2.token import NEWLINE
import sys
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# to handle 500 error
@app.errorhandler(500)
def exception_handler(e):
    return render_template('500.html'), 500

@app.route('/<string:page_name>')
def render_static(page_name):
    return render_template(page_name)


@app.route('/')
def hello_world():
    return render_template('index.html')


# def write_to_csv(data):
#     with open('database.csv', 'a', newline='') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',',
#                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])

def write_data_csv(data):
    with open('C:\\Users\\bhatr\\OneDrive\\Desktop\\LearnPython\\app\\portfolio\\database.csv', newline='', mode='a', encoding='utf-8') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# def write_to_csv(data):
#     with open('database.csv', 'a', newline='') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',',
#                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow(['email', 'subject', 'message'])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_data_csv(data)
            # with open('C:\\Users\\bhatr\\OneDrive\\Desktop\\LearnPython\\app\\webserver\\database.txt', mode='a', encoding='utf-8') as file:
            #     for key, value in data.items():
            #         file.write('%s:%s\n' % (key, value))
            # with open('C:\\Users\\bhatr\\OneDrive\\Desktop\\LearnPython\\app\\webserver\\database.csv', mode='a', newline='', encoding='utf-8') as database:
            #     writer = csv.DictWriter(database, fieldnames=field_names)
            #     writer.writeheader()
            #     writer.writerows(data)
            return redirect('/thankyou.html')
        except:
            return 'Data not present in Database'
    else:
        return 'Something went wrong , please try again later !'


# @app.route('/')
# def my_home():
#     return render_template('index.html')


# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')


# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')


# @app.route('/services.html')
# def my_services():
#     return render_template('services.html')


# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def my_components():
#     return render_template('components.html')


# @app.route('/project.html')
# def my_project():
#     return render_template('project.html')


# @app.route('/<string:page_name>')
# def my_project(page_name):
#     return render_template(page_name)

# @app.route('/favicon.ico')
# def favicon():
#     return 'Explore through the range of ART WORK'


# @app.route('/artwork')
# def artwork():
#     return 'Explore through the range of ART WORK'
