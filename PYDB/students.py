import peewee
from peewee import *

db = MySQLDatabase('python_db',host="localhost", port=3306, user='root')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default = 0)
    
    class Meta:
        database = db
        

students=[
    {'username': 'Srini', 'points':23423},
    {'username': 'Ram', 'points':2344344},
    {'username': 'test', 'points':4234},
    {'username': 'sfsdft', 'points':6656}   
]

def add_students():
    for student in students:
        try:
            Student.create(
            username=student['username'],
            points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
    
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print('Top student: {0.username} '.format(top_student()))