from django.db import models

# Create your models here.
# models.py (the database tables)

class Author(models.Model):
	AuthorID = models.CharField(max_length=50, primary_key=True)
	Name = models.CharField(max_length=50)
	Age = models.CharField(max_length=50)
	Country = models.CharField(max_length=50)
	class Meta:
		db_table = "Author"

class Book(models.Model):
	ISBN = models.CharField(max_length=50, primary_key=True)
	Title = models.CharField(max_length=50)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length=50)
	PublishDate = models.CharField(max_length=50)
	Price = models.CharField(max_length=50)
	class Meta:
		db_table = "Book"