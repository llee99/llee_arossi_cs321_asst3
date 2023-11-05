from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *
from join_filter import query_students_by_course, insert_data

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Information for courses, students, and schools table
course_data = [(320, 'Computer Network', 'Explore the fundamentals of networking, including protocols, data transmission, and network architecture.'),
               (321, 'Machine Learning', 'Dive into the world of artificial intelligence and data analysis, learning how to build predictive models and algorithms.'),
               # Add more course data as needed
              ]

student_data = [(100000, 'John', 'Doe'),
                (100001, 'Jane', 'Doe'),
                # Add more student data as needed
               ]

school_data = [(20000, 'University of California, Berkeley', 'Berkeley, CA'),
               (20001, 'University of California, Los Angeles', 'Los Angeles, CA'),
               # Add more school data as needed
              ]

# Insert data into the database
insert_data(session, course_data, student_data, school_data)

# Query students for a specific course
course_name = 'Machine Learning'
students = query_students_by_course(course_name)
print(f"Students enrolled in '{course_name}':")
for student in students:
    print(student)
