from django.contrib import admin

from .models import Author,Blog,Entry, City, Branch, Employee
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(City)
admin.site.register(Branch)
admin.site.register(Employee)
