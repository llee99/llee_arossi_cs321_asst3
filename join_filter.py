from sqlalchemy import create_engine, select
from models import School, Student, Course, students_courses

# Define the database engine
engine = create_engine('sqlite:///curricular.db', echo=True)

# Create a connection to the engine
with engine.connect() as connection:
    # Define the SQL query
    query = select([Student]).select_from(
        Student.join(students_courses).join(Course)
    ).where(Course.course_name == 'Machine Learning')

    # Execute the query and fetch the results
    result = connection.execute(query)

    # Print the results
    for row in result:
        print(row)
