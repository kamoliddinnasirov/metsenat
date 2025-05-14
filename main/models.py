from django.db import models
from main.abstract import  BaseModel



class University(BaseModel):
    name = models.CharField("Universitet nomi", max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Universitet'
        verbose_name_plural = '1.Universitetlar'




PERSON = [
    (0, 'Yuridik'),
    (1, 'Jismoniy'),
]

CONDITIONS = [
    (1, 'Yangi'),
    (2, 'Tasdiqlangan'),
    (3, 'Moderatsiyada'),
    (4, 'Bekor qilingan'),
]


class Sponsor(BaseModel):
    is_phisical_person = models.BooleanField(verbose_name='Shaxs turi', choices=PERSON)
    full_name = models.CharField('F.I.Sh', max_length=255)
    phone = models.CharField(max_length=13, verbose_name='Telefon raqam')
    name_company = models.CharField('Firma nomi', max_length=255, blank=True, null=True)
    condition = models.IntegerField('Holat', choices=CONDITIONS, default=1)
    budget = models.PositiveIntegerField()
    used = models.PositiveIntegerField(default=0)
    is_counted = models.BooleanField(default=False)

    #10 000 - 7000 = 3000

    @property
    def remaining_budget(self):
        return self.budget - self.used

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = 'Homiy'
        verbose_name_plural = '2.Homiylar'



#Students type
TYPE = [
    (1, 'Bakalavr'),
    (2, 'Magistratura'),
    (3, 'Aspirantura')
]


class Student(BaseModel):
    full_name = models.CharField('F.I.Sh', max_length=255)
    phone = models.CharField('Telefon raqam', max_length=13)
    university = models.ForeignKey(University, verbose_name='Institut', on_delete=models.RESTRICT)
    student_type = models.IntegerField('Talim turi', choices=TYPE)
    request = models.PositiveIntegerField('Soralgan pul miqdor')
    send = models.PositiveIntegerField('Tolangan pul miqdori', default=0)

    @property
    def remaining_budget(self):
        return self.request - self.send

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = '3.Talabalar'



class StudentBudget(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, verbose_name='Talaba')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.RESTRICT, verbose_name='Homiy')
    money = models.PositiveIntegerField(verbose_name='Pull miqdori')


    def __str__(self):
        return f"{self.student} {self.sponsor}"


    class Meta:
        verbose_name = 'Talaba va Homiy'
        verbose_name_plural = '4.Talabalar va Homiylar'


class LinearGraph(BaseModel):
    numbers_sponsor = models.PositiveIntegerField(default=0)
    numbers_student = models.PositiveIntegerField(default=0)
    day = models.DateTimeField()


    def __str__(self):
        return  self.day

    class Meta:
        verbose_name = 'Kunlik statistika'
        verbose_name_plural = '5.Kunlik statistikalar'



class MainDatas(models.Model):
    money_asked = models.PositiveIntegerField(default=0)
    money_sent = models.PositiveIntegerField(default=0)
    money_amount = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"To'landi: {self.money_sent}, So'raldi: {self.money_asked}, To'lanishi kerak: {self.money_amount}"



    class Meta:
        verbose_name = "Asosiy ma'lumot"
        verbose_name = "6.Asosiy ma'lumotlar"