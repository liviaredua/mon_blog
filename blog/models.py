
from django.db import models

class Profile(models.Model):
    first_name = models.CharField('Nome',max_length=30)
    last_name = models.CharField('Sobrenome',max_length=30)
    birth = models.IntegerField('Data de Nascimento')
    linkedin = models.CharField('Likedin',max_length=50)
    gitHub = models.CharField('GitHub',max_length=50)


class About(models.Model):
    salutation = models.CharField('salutation',max_length=30)
    textSalutation = models.CharField('Text Salutation',max_length=100)
    aboutMe = models.TextField('About Me')


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
        return  f'Work_{self.id}'


class WorkExperienceComplements(models.Model):
    idWork = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    complemtText = models.TextField('Complement')

    def __str__(self):
        return  str(self.complemtText)[0:15]


class LatestWorks(models.Model):
    workTilte = models.CharField('Work Tilte ',max_length=30)
    description = models.TextField('Description')
    isRedirect: models.BooleanField(default=False)

    def __str__(self):
        return  str(self.workTilte)

class Details(models.Model):
    idWK = models.ForeignKey(LatestWorks, on_delete=models.CASCADE)
    title = models.CharField('Tile',max_length=50)
    subtitle = models.CharField('Subtile',max_length=30, blank=True)
    year = models.DateField(auto_now=True)
    description = models.TextField('Description')
    
    def __str__(self):
        return  str(self.title)


class Tools(models.Model):
    tool = models.CharField('Tool', max_length=50)
    title = models.CharField('Tile',max_length=50, blank=True)
    description = models.TextField('Description')

    def __str__(self):
        return  str(self.tool)

class ToolsTopics(models.Model):
    idToll = models.ForeignKey(Tools, on_delete=models.CASCADE)
    title = models.CharField('Tile',max_length=50)
    year = models.DateField(auto_now=True)
    description = models.CharField('Description', max_length=120)

    def __str__(self):
        return  str(self.title)


class Articles(models.Model):
    articleTilte = models.CharField('Article Tilte',max_length=30)
    description = models.TextField('Description')
    isRedirect: models.BooleanField(default=False)

    def __str__(self):
        return  str(self.articleTilte)

class DetailsArticles(models.Model):
    idArt = models.ForeignKey(Articles, on_delete=models.CASCADE)
    title = models.CharField('Tile',max_length=50)
    subtitle = models.CharField('Subtile',max_length=30, blank=True)
    year = models.DateField(auto_now=True)
    description = models.TextField('Description')
    
    def __str__(self):
        return  str(self.title)