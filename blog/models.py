from pyexpat import model
from django.db import models

class Profile(models.Model):
    first_name = models.CharField('Nome',max_length=30)
    last_name = models.CharField('Sobrenome',max_length=30)
    birth = models.IntegerField('Data de Nascimento')
    linkedin = models.CharField('Likedin',max_length=50)
    gitHub = models.CharField('GitHub',max_length=50)


class CoreSkills(models.Model):
    skill = models.CharField('Skill',max_length=30)
    level = models.CharField('Level',max_length=30)

    def __str__(self):
        return  f'{str(self.skill)}_{str(self.level)}'

class OtherSkills(models.Model):
    skill = models.CharField('Skill',max_length=30)
    level = models.CharField('Level',max_length=30)
    def __str__(self):
        return  f'{str(self.skill)}_{str(self.level)}'

class WorkExperience(models.Model):
    timeRange = models.CharField('Time',max_length=30)
    officename = models.CharField('Office Name',max_length=30)
    department = models.CharField('Department',max_length=30)
    description = models.TextField('Description')

    def __str__(self):
        return  str(self.description)[0:15]


class WorkExperienceComplements(models.Model):
    idWork = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    complemtText = models.TextField('Complement')

    def __str__(self):
        return  str(self.complemtText)[0:15]


class LatestWorks(models.Model):
    workTilte = models.CharField('Work Tilte ',max_length=30)
    description = models.TextField('Description')
    isRedirect: models.BooleanField(default=False)
    linkRedirect = models.CharField('Work Tilte ',max_length=100, default='#')

    def __str__(self):
        return  str(self.workTilte)

    




