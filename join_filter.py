from sqlalchemy import create_engine, select
from models import School, Student, Course, students_courses

def query_students_by_course(course_name):
    engine = create_engine('sqlite:///curricular.db', echo=True)
    with engine.connect() as connection:
        try:
            query = select([Student]).select_from(Student.join(students_courses).join(Course)).where(Course.course_name == course_name)
            result = connection.execute(query)
            students = result.fetchall()
            return students
        except Exception as e:
            print(f"Error: {e}")
            return []

def insert_data(session, course_data, student_data, school_data):
    try:
        for id, name, description in course_data:
            new_course = Course(course_id=id, course_name=name, course_description=description)
            session.add(new_course)

        for id, first_name, last_name in student_data:
            new_student = Student(student_id=id, first_name=first_name, last_name=last_name)
            session.add(new_student)

        for id, name, address in school_data:
            new_school = School(school_id=id, school_name=name, school_address=address)
            session.add(new_school)

        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
