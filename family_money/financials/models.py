from django.db import models
from django import forms
    
class Bill(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.amount}'

class SavingsGoal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deadline = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.user.username}'
    
class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.user.username} - {self.amount}'
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.category} - {self.amount}'
    
    

class ExpenseForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label="Add New Category",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new category'}),
    )

    class Meta:
        model = Expense
        fields = ['category', 'new_category', 'amount', 'date']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prepopulate the category dropdown
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        new_category = cleaned_data.get("new_category")

        # If 'new_category' is filled, create a new Category instance
        if new_category:
            category, created = Category.objects.get_or_create(name=new_category)
            cleaned_data['category'] = category

        return cleaned_data
    
    
class Income(models.Model):
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.source} - {self.amount} - {self.user.username}'