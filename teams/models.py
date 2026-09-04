from django.db import models

# Create your models here.
class Team(models.Model):
	team_number = models.CharField(max_length=10)
	team_name = models.CharField(max_length=100)
	program = models.CharField(max_length=20)
	school = models.CharField(max_length=150, blank=True)

	def __str__(self):
		return f"{self.team_number} - {self.team_name}"

