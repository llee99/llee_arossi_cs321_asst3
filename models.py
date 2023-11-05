from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from db_create import Base

#many students to many courses,
#courses could have many students
#students could have many courses
students_courses = Table(
    'students_courses', 
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

#School table
class School(Base):
    __tablename__ = 'schools'

    school_id = Column(Integer, primary_key=True)
    school_name = Column(String(50), unique=True)
    school_address = Column(String(50))
    #enrolled_students = relationship("Student", secondary=association_table, backref="schools")

    def __init__(self,school_id, school_name, school_address):

        self.school_id = school_id
        self.school_name = school_name
        self.school_address = school_address
        
    def __repr__(self):
        return '<School %r>' % (self.School_name)

#Student table
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    courses = relationship("Course", secondary=students_courses, backref="students")


    def __init__(self, id, first_name, last_name, default_courses=None):
        self.student_id = id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = default_courses or []  # Assign default courses if provided, else an empty list

    def __repr__(self):
        return '<Student %r>' % (self.first_name)
        
#Course table
class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(50))
    course_description = Column(String(50))
    students = relationship("Student", secondary=students_courses, backref="courses")

    def __init__(self, id, name, description):
        self.course_id = id
        self.course_name = name
        self.course_description = description

    def __repr__(self):
        return '<Course %r>' % (self.course_name)
    
#Sets the relationship between the tables
Student.courses = relationship("Course", secondary=students_courses, back_populates="students")
Course.students = relationship("Student", secondary=students_courses, back_populates="courses")

