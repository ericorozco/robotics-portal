from django.db import models
from teams.models import Team
# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	grade_level = models.IntegerField()
	team = models.ForeignKey(
		Team,
		on_delete=models.CASCADE,
		related_name="students"
	)
	
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
