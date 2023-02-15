from django.db import models

# Create your models here.
class question(models.Model):
    question_text=models.CharField((""), max_length=200)
    pub_date=models.DateField(("date published"), auto_now=False, auto_now_add=False)
class choice(models.Model):
    questions=models.ForeignKey(question, verbose_name=(""), on_delete=models.CASCADE)
    choice_text=models.CharField((""), max_length=100)
    votes=models.IntegerField(default=0)
