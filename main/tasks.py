from core.celery import app
# from celery import
from main.models import LinearGraph, Sponsor, Student, MainDatas
import datetime


@app.task
def create_data_graph():
    yestarday = datetime.datetime.today() - datetime.timedelta(days=1)
    number_sp = Sponsor.objects.filter(created_at__date=yestarday.date()).count() #11-may, ID 1
    number_st = Student.objects.filter(created_at__date=yestarday.date()).count()
    LinearGraph.objects.create(day=yestarday, numbers_student=number_st, numbers_sponsor=number_sp)


@app.task
def money_management(sponsor_id, student_id, money):
    sponsor = Sponsor.objects.get(id=sponsor_id)
    student = Student.objects.get(id=student_id)

    sponsor.used += money
    sponsor.save()

    student.send += money
    student.save()

    main_data = MainDatas.objects.get(id=1)
    main_data.money_sent += money
    main_data.save()


@app.task
def money_given(money):
    main_data = MainDatas.objects.get(id=1) # True/False
    main_data.money_amount += money
    main_data.save()



@app.task
def money_is_needed(money):
    main_data = MainDatas.objects.get(id=1)
    main_data.money_asked += money
    main_data.save()