#this file is used to insert data into the database

from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

# create a Session
Session = sessionmaker(bind = engine)
session = Session()


#####################################################
#information for courses table
course_id = [320, 321, 322, 323, 324, 325]

courses_name = ['Computer Network', 'Machine Learning', 'Object-Oriented Design', 
           'Web Development', 'Discreet Structure', 'Operating System']

course_descriptions = [
    'Explore the fundamentals of networking, including protocols, data transmission, and network architecture.',
    'Dive into the world of artificial intelligence and data analysis, learning how to build predictive models and algorithms.',
    'Design: Learn the principles of designing software using object-oriented programming concepts, promoting code reusability and modularity.',
    'Master the art of creating dynamic and interactive websites, covering HTML, CSS, JavaScript, and server-side technologies.',
    'Study mathematical structures that underlie computer science, including logic, set theory, and graph theory.',
    'Gain an understanding of the core components and functions of operating systems, essential for managing computer resources and processes.'
]

#####################################################
#information for students table
student_id = [100000, 100001, 100002, 100003, 100004, 100005]

first_name = ['John', 'Jane', 'Jack', 'Jill', 'James', 'Judy']

last_name = ['Doe', 'Doe', 'Smith', 'Smith', 'Johnson', 'Johnson']

#####################################################

#information for schools table
school_id = [20000, 20001, 20002, 20003, 20004, 20005]

school_name = ['University of California, Berkeley', 'University of California, Los Angeles','University of California, San Diego',
                'University of California, Santa Barbara', 'University of California, Irvine', 'University of California, Davis']
school_address = ['Berkeley, CA', 'Los Angeles, CA', 'San Diego, CA', 'Santa Barbara, CA', 'Irvine, CA', 'Davis, CA']


#####################################################

#creates all courses in session
for i in range(len(course_id)):
    new_course = Course(course_id[i], courses_name[i], course_descriptions[i])
    session.add(new_course)

#####################################################

#creates all students in session
for i in range(len(student_id)):
    new_student = Student(student_id[i], first_name[i], last_name[i])
    session.add(new_student)

#####################################################

#creates all schools in session

for i in range(len(school_id)):
    new_school = School(school_id[i], school_name[i], school_address[i])
    session.add(new_school)

#####################################################

#commits the changes to the database
session.commit()

