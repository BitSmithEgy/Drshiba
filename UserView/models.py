from django.db import models
from django.conf import settings

class Course(models.Model):
    image = models.ImageField(upload_to='courses')
    title = models.CharField(max_length=100, default='')
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    description = models.TextField()

    def __str__(self):
        return f"{self.author.username} ({self.title})"

class Video(models.Model):
    image = models.ImageField(upload_to='videos', default=' ')
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=2000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    q = models.TextField()
    q_option1 = models.CharField(max_length=100)
    q_option2 = models.CharField(max_length=100)
    q_option3 = models.CharField(max_length=100)
    q_option4 = models.CharField(max_length=100)
    correct_answer_q = models.CharField(max_length=100)
    
    def __str__(self):
        return self.q

class Quiz(models.Model):
    questions = models.ManyToManyField(Question, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)
    completed_courses = models.ManyToManyField(Course, blank=True)
