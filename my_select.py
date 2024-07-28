from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from models.models import Student, Group, Teacher, Subject, Grade

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def select_1():
    session = Session()
    result = session.query(Student, func.avg(Grade.grade).label('average')).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    session.close()
    return result

def select_2(subject_id):
    session = Session()
    result = session.query(Student, func.avg(Grade.grade).label('average')).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    session.close()
    return result

def select_3(subject_id):
    session = Session()
    result = session.query(Group, func.avg(Grade.grade).label('average')).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    session.close()
    return result

def select_4():
    session = Session()
    result = session.query(func.avg(Grade.grade)).scalar()
    session.close()
    return result

def select_5(teacher_id):
    session = Session()
    result = session.query(Subject).filter(Subject.teacher_id == teacher_id).all()
    session.close()
    return result

def select_6(group_id):
    session = Session()
    result = session.query(Student).filter(Student.group_id == group_id).all()
    session.close()
    return result

def select_7(group_id, subject_id):
    session = Session()
    result = session.query(Student, Grade).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    session.close()
    return result

def select_8(teacher_id):
    session = Session()
    result = session.query(func.avg(Grade.grade)).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    session.close()
    return result

def select_9(student_id):
    session = Session()
    result = session.query(Subject).join(Grade).filter(Grade.student_id == student_id).all()
    session.close()
    return result

def select_10(student_id, teacher_id):
    session = Session()
    result = session.query(Subject).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()
    session.close()
    return result
