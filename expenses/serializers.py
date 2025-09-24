from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for the Expense model."""

    class Meta:
        model = Expense
        fields = ["id", "name", "amount", "description", "date", "category"]