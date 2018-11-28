from django.db import models

app_name = 'main'

class Category (models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField('date of creation')
    def __str__(self):
        return self.name

class Achievements(models.Model):
    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField('date of creation')
    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField('date of birth')
    email = models.EmailField()
    number = models.CharField(max_length=20)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    year_at_school = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    achievements = models.ForeignKey(Achievements, on_delete=models.CASCADE, related_name='achievements')
    date_created = models.DateTimeField('date of creation')
    def __str__(self):
        return ("%s %s") % (self.name, self.surname)