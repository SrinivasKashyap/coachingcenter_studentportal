import django
import datetime
from django.contrib.auth.models import User
from student.models import Student,Result,Session,CustomUser
from teacher.models import Subject,Teacher,Class,Course

def run():
    # Create super user
    CustomUser.objects.create_superuser('srinivaskashyap', 'projectsk391@gmail.com', 'srinirox')

    print("Superuser created...")

    # Create subjects
    math1=Subject.objects.create(name='Math',code='001')
    math2=Subject.objects.create(name='Math', code='002')
    physics1=Subject.objects.create(name='Physics',code='001')
    physics2=Subject.objects.create(name='Physics',code='002')
    chemistry1=Subject.objects.create(name='Chemistry',code='001')
    chemistry2=Subject.objects.create(name='Chemistry',code='002')
    biology1=Subject.objects.create(name='Biology',code='001')
    biology2=Subject.objects.create(name='Biology',code='002')
    math3=Subject.objects.create(name='Adv Math',code='001')
    physics3=Subject.objects.create(name='Adv Physics',code='001')
    chemistry3=Subject.objects.create(name='Adv Chemistry',code='001')
    biology3=Subject.objects.create(name='Adv Biology',code='001')


    print("Subjects created...")

    # Create CustomUser and assign as teacher

    teacher1 = CustomUser.objects.create_user(username='teacher1',
                                     email='teacher1@portal.com',
                                     password='testing1',
                                    first_name="Teacher",
                                    last_name="Name1",is_teacher=True)

    teacher1 = Teacher.objects.create(user=teacher1 , subject = math1)

    teacher2 = CustomUser.objects.create_user(username='teacher2',
                                     email='teacher2@portal.com',
                                     password='testing2',
                                    first_name="Teacher",
                                    last_name="Name2",is_teacher=True)

    teacher2 = Teacher.objects.create(user=teacher2 , subject = physics1)

    teacher3 = CustomUser.objects.create_user(username='teacher3',
                                     email='teacher3@portal.com',
                                     password='testing3',
                                    first_name="Teacher",
                                    last_name="Name3",is_teacher=True)

    teacher3 = Teacher.objects.create(user=teacher3 , subject=chemistry1)

    teacher4 = CustomUser.objects.create_user(username='teacher4',
                                     email='teacher4@portal.com',
                                     password='testing4',
                                    first_name="Teacher",
                                    last_name="Name4",is_teacher=True)

    teacher4 = Teacher.objects.create(user=teacher4 , subject=biology1)

    print("Created teacher users and assigned as teachers")

    # Create a class

    class1 = Class.objects.create(name='Foundation JEE A', teacher=teacher1, year=1)
    class2 = Class.objects.create(name='Final JEE A', teacher=teacher2, year=8)
    class3 = Class.objects.create(name='Advance JEE A', teacher=teacher3, year=9)
    class4 = Class.objects.create(name='Foundation NEET A', teacher=teacher4, year=10)


    print("Created classes")


#Creating Courses (the subjects to be taught in each class and taught by which teacher)
    Course.objects.create(className=class1, subject=math1, teacher = teacher1)
    Course.objects.create(className=class1, subject=physics1, teacher = teacher2)
    Course.objects.create(className=class1, subject=chemistry1, teacher=teacher3)
    Course.objects.create(className=class2, subject=math2, teacher=teacher1)
    Course.objects.create(className=class2, subject=physics2, teacher = teacher2)
    Course.objects.create(className=class2, subject=chemistry2, teacher = teacher3)
    Course.objects.create(className=class3, subject=math3, teacher=teacher1)
    Course.objects.create(className=class3, subject=physics3, teacher=teacher2)
    Course.objects.create(className=class3, subject=chemistry3, teacher=teacher3)
    Course.objects.create(className=class4, subject=physics1, teacher=teacher2)
    Course.objects.create(className=class4, subject=chemistry1, teacher=teacher3)
    Course.objects.create(className=class4, subject=biology1, teacher=teacher4)

    print("Created course....")
#Creating Student Users
    student1 = CustomUser.objects.create_user(username='student1',
                                     email='student1@portal.com',
                                     password='stesting1',
                                    first_name="Student",
                                    last_name="Name1",is_student=True)

    student2 = CustomUser.objects.create_user(username='student2',
                                     email='student2@portal.com',
                                     password='stesting2',
                                    first_name="Student",
                                    last_name="Name2",is_student=True)

    student3 = CustomUser.objects.create_user(username='student3',
                                     email='student3@portal.com',
                                     password='stesting3',
                                    first_name="Student",
                                    last_name="Name3",is_student=True)

    student4 = CustomUser.objects.create_user(username='student4',
                                     email='student4@portal.com',
                                     password='stesting4',
                                    first_name="Student",
                                    last_name="Name4",is_student=True)

    student5 = CustomUser.objects.create_user(username='student5',
                                     email='student5@portal.com',
                                     password='stesting5',
                                    first_name="Student",
                                    last_name="Name5",is_student=True)

    student6 = CustomUser.objects.create_user(username='student6',
                                     email='student6@portal.com',
                                     password='stesting6',
                                    first_name="Student",
                                    last_name="Name6",is_student=True)

    student7 = CustomUser.objects.create_user(username='student7',
                                     email='student7@portal.com',
                                     password='stesting7',
                                    first_name="Student",
                                    last_name="Name7",is_student=True)

    student8 = CustomUser.objects.create_user(username='student8',
                                     email='student8@portal.com',
                                     password='stesting8',
                                    first_name="Student",
                                    last_name="Name8",is_student=True)

    print("Student users created...")
#Creating Student objects
    d=datetime.date(1998,10,1)
    Student.objects.create(user=student1, adm_no=1, rollno=1, class_studying=class1, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='male')
    Student.objects.create(user=student2, adm_no=2, rollno=2, class_studying=class1, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='female')
    Student.objects.create(user=student3, adm_no=3, rollno=1, class_studying=class2, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='male')
    Student.objects.create(user=student4, adm_no=4, rollno=2, class_studying=class2, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='male')
    Student.objects.create(user=student5, adm_no=5, rollno=1, class_studying=class3, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='female')
    Student.objects.create(user=student6, adm_no=6, rollno=2, class_studying=class3, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='female')
    Student.objects.create(user=student7, adm_no=7, rollno=1, class_studying=class4, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='female')
    Student.objects.create(user=student8, adm_no=8, rollno=2, class_studying=class4, father_name='Father', mother_name='Mother', date_join=d, dob= d, parent_phn='123456',gender='female')


    print("Sample students created...")
