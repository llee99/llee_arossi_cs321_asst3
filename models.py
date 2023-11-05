from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db_create import Base

students_courses = Table(
    'students_courses', 
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.student_id')),
    Column('course_id', Integer, ForeignKey('courses.course_id'))
)

class School(Base):
    __tablename__ = 'schools'

    school_id = Column(Integer, primary_key=True, autoincrement=True)
    school_name = Column(String(50), unique=True)
    school_address = Column(String(50))

    def __repr__(self):
        return f'<School {self.school_name}>'

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    courses = relationship("Course", secondary=students_courses, backref="students")

    def __repr__(self):
        return f'<Student {self.first_name}>'

class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(50))
    course_description = Column(String(200))

    students = relationship("Student", secondary=students_courses, backref="courses")

    def __repr__(self):
        return f'<Course {self.course_name}>'

Student.courses = relationship("Course", secondary=students_courses, back_populates="students")
Course.students = relationship("Student", secondary=students_courses, back_populates="courses")
