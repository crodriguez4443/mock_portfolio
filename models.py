from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String(255) )
    skills_list = db.Column('Skills List', db.String(255))
    description = db.Column('Description', db.String(255))
    project_url = db.Column('Project URL', db.String(255))
    tags = db.Column('Tags', db.String(255))
    challenges_faced = db.Column('Challenges_faced', db.Text)
    achievements = db.Column('Achievements',db.String(255))
    date = db.Column(db.Date)


    def __repr__(self):
        return f'''<Projects: (Title: {self.title}
                Skills_List: {self.skills_list}
                Description: {self.description}
                Project URL: {self.project_url}
                Tags: {self.tags}
                Challenges_faced: {self.challenges_faced}
                Achievements: {self.achievements}
                date_added: {self.date_added}
                )
                '''




