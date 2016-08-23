from django.db import models

class Answers(models.Model):
	phone_num = models.BigIntegerField()
	answer1 = models.TextField()
	answer2 = models.TextField()
	answer3 = models.TextField()
	answer4 = models.TextField()
	answer5 = models.TextField()
	answer6 = models.TextField()
	answer7 = models.TextField()
	answer8 = models.TextField()
	answer9 = models.TextField()
	answer10 = models.TextField()
