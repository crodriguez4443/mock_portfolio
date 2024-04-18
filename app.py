from flask import render_template, url_for, request, redirect
from datetime import datetime
from  models import db, app, Projects

@app.route('/')
def index():
    projects = Projects.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects' )
def projects(id):
    projects = Projects.query.get_or_404(id)
    #tells app to go to template folder and grab index.html
    return render_template('detail.html', projects=projects) 

@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        #tells appp to go to template folder and grab index.html
        date_str = request.form['date']
        date_obj = datetime.strptime(date_str, '%Y-%m').date()

        new_project = Projects(
            title=request.form['title'],
            skills_list=request.form['skills_list'], 
            description=request.form['description'], 
            project_url=request.form['github'],
            date=date_obj
            )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

@app.route('/about')
def about():
    projects = Projects.query.all()
    return render_template('about.html', projects=projects)

@app.route('/projects/<int:id>')
def project(id):
    project = Projects.query.get_or_404(id)
    return render_template('detail.html', project=project)

@app.route('/projects/<int:id>/edit', methods = ['get', 'post'] )
def edit(id):
    project = Projects.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.skills_list = request.form['skills_list']
        project.project_url = request.form['github']
        date_str = request.form['date']
        #so you have to convert date to datetime
        project.date = datetime.strptime(date_str, '%Y-%m').date()
        try:
            db.session.commit()
        except Exception as e:
            print("Failed to commit:", e)
            db.session.rollback()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project)

@app.route('/delete/<int:id>')
def delete(id):
    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')


