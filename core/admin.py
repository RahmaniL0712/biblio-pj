from django.contrib import admin

from .models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)  
    @admin.display(description='Full Name', ordering='name')
    def full_name(self, obj):
        return f'{obj.name} {obj.surname}'
    search_fields = ('name', 'surname')
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'title', 'author', 'publisher', 'published_year', 'genre',)
    list_filter = ('author', 'publisher', 'genre')
    search_fields = ('title', 'ISBN', 'publisher', 'author__name', 'author__surname')
    
@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'barcode', 'category', 'status')
    list_filter = ('category', 'status',)
    search_fields = ('book__title', 'barcode')
    list_editable = ('status', )
    @admin.action(description="Mark selected copies as Loaned")
    def make_loaned(modeladmin, request, queryset):
        queryset.update(status = 'loaned')
    @admin.action(description="Mark selected copies as In Stock")
    def make_instock(modeladmin, request, queryset):
        queryset.update(status = 'in_stock')
    actions = (make_loaned, make_instock)

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'phone_number', 'email')
    # list_filter = ('address',)
    @admin.display(description='Full name', ordering='name')
    def full_name(self, obj):
        return f'{obj.name} {obj.surname}'
    search_fields = ('name', 'surname', 'address', 'phone_number', 'email')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_code', 'patron', 'book_copy', 'loan_date', 'due_date', 'return_date')
    list_filter = ('due_date','patron')
    search_fields = ('loan_code', 'patron__name', 'patron__surname', 'book_copy__book__title')
    search_help_text = 'Search by loan code, patron name, or book title'
    

    
    #make it so loaned copies don't appear in the dropdown list
    
