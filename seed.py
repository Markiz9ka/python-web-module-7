from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models.models import Base, Student, Group, Teacher, Subject, Grade
import datetime

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 6)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(30)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 20)):
            grade = Grade(student=student, subject=subject, grade=random.uniform(2.0, 5.0), date=fake.date_between(start_date='-1y', end_date='today'))
            session.add(grade)
session.commit()
