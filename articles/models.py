from django.db import models
from django.contrib import admin

class Article(models.Model):
	title=models.CharField(max_length=200)
	text=models.TextField()
	time_pub=models.DateField(auto_now_add=True)


	def __unicode__(self):
		return self.title
