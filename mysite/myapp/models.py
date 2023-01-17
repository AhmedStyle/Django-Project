from django.db import models

# Home page
class HomePage(models.Model):
    title = models.CharField(max_length=255)
    profession_description = models.TextField(max_length=3000)
    profession_image = models.ImageField(upload_to='profession_images/')

    def __str__(self):
        return self.title
    

# Demand page
class Demand(models.Model):
    profession = models.CharField(max_length=255)
    year = models.IntegerField()
    salary = models.FloatField()
    vacancies = models.IntegerField()


# Geography page 
class Geography(models.Model):
    city = models.CharField(max_length=255)
    salary = models.FloatField()
    vacancies_percentage = models.FloatField()


# Skills page
class Skills(models.Model):
    profession = models.CharField(max_length=255)
    year = models.IntegerField()
    key_skills = models.TextField()


# Latest jobs
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    region = models.CharField(max_length=255)
    date = models.DateField()
