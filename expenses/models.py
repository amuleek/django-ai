from django.db import models


class Category(models.Model):
    """Simple category model for expenses."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    Category_Choices = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Healthcare', 'Healthcare'),
        ('Other', 'Other'),
    ]
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=Category_Choices, default='Other')
    class Meta:
        ordering = ["-date"]    

    def __str__(self):
        return f"{self.description}: {self.amount} on {self.date}"