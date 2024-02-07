import datetime

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def question(self):
        return self.question_text
    
    def send_date(self):
        return self.pub_date.strftime("%B %d, %Y")
    
    def num_responses(self):
        return self.responses.count()



class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    response_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.response_text
    
    def send_date(self):
        return self.pub_date.strftime("%B %d, %Y")

    

