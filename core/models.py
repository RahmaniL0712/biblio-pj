from django.db import models
from django.core.validators import MinValueValidator
from .constants import *

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Book(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=70)
    published_year = models.IntegerField(validators=[
        MinValueValidator(0, 'Publishing year under 0 is not allowed.')
    ])
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    
    def __str__(self):
        return f'{self.title}'
    
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=10)
    category = models.CharField(choices=COPY_CATEGORIES)
    status = models.CharField(choices=COPY_STATUS)
    class Meta:
        verbose_name = 'Book copy'
        verbose_name_plural = 'Book copies'
    
    def __str__(self):
        return f'{self.book} - {self.book.author}'
    
    
class Patron(models.Model):
    n_id = models.CharField()
    name = models.CharField()
    surname = models.CharField()
    address = models.CharField()
    phone_number = models.CharField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Loan(models.Model):
    loan_code = models.CharField(max_length=10)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.loan_code
    
    