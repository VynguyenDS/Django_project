from django.db import models
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Multi_Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length= 200)
    frequently = models.TextField()
    def __str__(self):
        self.id_post = str(self.id_post)
        return self.id_post
class Newsfeed(models.Model):
    id = models.AutoField(primary_key=True)
    id_post = models.CharField(max_length= 100)
    content = models.TextField()
    post_ower = models.TextField()
    def __str__(self):
        self.id = str(self.id)
        return self.id


