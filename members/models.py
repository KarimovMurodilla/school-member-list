from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Pupil(models.Model):
    year = models.CharField("O'quv yili", max_length=10)
    school_class = models.CharField("Sinflar", max_length=10)
    fullname = models.CharField("F.I.SH", max_length=100)
    date_of_birth = models.DateField("Tug'ilgan yili", max_length=10)
    gender_choices = (('Erkak', 'Erkak'), ('Ayol', 'Ayol'))
    gender = models.CharField("Jinsi", choices=gender_choices, max_length=10)
    start_date = models.DateField("Boshlanish vaqti")

    def __str__(self):
        return self.school_class

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"


class Teacher(models.Model):
    job_title = models.CharField("Kasbi", max_length=50)
    graphic = models.CharField("Ishlash grafigi", max_length=25)
    start_date = models.DateField("Boshlanish vaqti")
    fullname = models.CharField("F.I.SH", max_length=100)
    date_of_birth = models.DateField("Tug'ilgan yili")
    gender_choices = (('Erkak', 'Erkak'), ('Ayol', 'Ayol'))
    gender = models.CharField("Jinsi", choices=gender_choices, max_length=10)
    inn = models.CharField("INN", max_length=50)
    pinfl = models.CharField("JSHIR", max_length=20)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


# ---Lessons---

class ClassNumber(models.Model):
    class_number = models.PositiveIntegerField(
        "Sinf", default=1, 
        validators=[
            MinValueValidator(1, "0 sinf mavjud emas. Iltimos bohcha bolalarini qo'shmang ;)"), 
            MaxValueValidator(11, message="O'zbekistonda 11 dan katta sinf yo'qku =)")
        ]
    )

    def __str__(self):
        return str(self.class_number)

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"


class Subject(models.Model):
    title = models.CharField("Nomi", max_length=50)
    description = models.CharField("Qisqa ma'lumot", max_length=150)
    image = models.ImageField("Rasm", upload_to='images/')
    classes = models.ManyToManyField(ClassNumber)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField("Nomi", max_length=50)
    description = models.CharField("Qisqa ma'lumot", max_length=150)
    url = models.URLField("Dars uchun link", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"   



# ---Feedbacks---
class Feedback(models.Model):
    name = models.CharField("Ism", max_length=50)
    email = models.EmailField("Email")
    subject = models.CharField("Mavzu", max_length=150)
    message = models.TextField("Habar", max_length=4000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Habar"
        verbose_name_plural = "Habarlar"