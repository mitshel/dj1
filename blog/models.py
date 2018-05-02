from django.db import models

# Create your models here.

class DashaPost(models.Model):
	title = models.CharField(max_length=150, default='Новое сообщение')
	body = models.TextField()
	timestamp = models.DateTimeField()

	class Meta:
		ordering = ('title',)
