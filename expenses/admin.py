from django.contrib import admin

from .models import Expense
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'description', 'date', 'category')
    search_fields = ('name', 'description', 'category__name')
    list_filter = ('date', 'category')
    search_fields = ('name', 'description', 'category__name')   