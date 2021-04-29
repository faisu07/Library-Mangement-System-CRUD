from django.db import models


from datetime import datetime
class Book(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	author = models.CharField(max_length = 30)
	email = models.EmailField(blank = True)
	describe = models.TextField()
	NumberOfCopies = models.IntegerField()
	Release = models.DateField('date released', default=datetime.now)
	Price = models.FloatField()	
	Discount = models.BooleanField(default=False)
	def __str__(self):
		return self.name
