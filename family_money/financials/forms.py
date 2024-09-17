from django import forms
from django.db.models import Q
from .models import Bill, SavingsGoal, Budget, Expense, Income, Category

# Bill Form
# Handles creating and updating bill information
class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'amount', 'due_date']
        widgets = {
            # Text input for the bill name with Bootstrap styling
            'name': forms.TextInput(attrs={'class': 'form-control short-input'}),
            # Number input for the bill amount with Bootstrap styling
            'amount': forms.NumberInput(attrs={'class': 'form-control short-input'}),
            # Date input for the due date using HTML5 date picker
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control short-input'}),
        }

# Savings Goal Form
# Handles creating and updating savings goals
class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']
        widgets = {
            # Text input for the goal name with Bootstrap styling
            'name': forms.TextInput(attrs={'class': 'form-control short-input'}),
            # Number input for the target and current amount with Bootstrap styling
            'target_amount': forms.NumberInput(attrs={'class': 'form-control short-input'}),
            'current_amount': forms.NumberInput(attrs={'class': 'form-control short-input'}),
            # Date input for the deadline using HTML5 date picker
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control short-input'}),
        }

# Budget Form
# Handles creating and updating budget information
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'amount', 'start_date', 'end_date']
        widgets = {
            # Text input for the budget name with Bootstrap styling
            'name': forms.TextInput(attrs={'class': 'form-control short-input'}),
            # Number input for the budget amount with Bootstrap styling
            'amount': forms.NumberInput(attrs={'class': 'form-control short-input'}),
            # Date input for the start and end date using HTML5 date picker
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control short-input'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control short-input'}),
        }

# Expense Form
# Handles creating and updating expenses with the option to add new categories
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date']
        widgets = {
            # Specify HTML5 'date' input type for the date field
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control short-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Expense form initialized")  # Debugging line
        # Prepopulate the 'category' field with categories from the database
        self.fields['category'].queryset = Category.objects.all()
        # Apply Bootstrap styling to the 'category' field
        self.fields['category'].widget.attrs.update({'class': 'form-control short-input'})

        
# Income Form
# Handles creating and updating income records
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date']
        widgets = {
            # Text input for the income source with Bootstrap styling
            'source': forms.TextInput(attrs={'class': 'form-control short-input'}),
            # Number input for the income amount with Bootstrap styling
            'amount': forms.NumberInput(attrs={'class': 'form-control short-input'}),
            # Date input for the income date using HTML5 date picker
            'date': forms.DateInput(attrs={'class': 'form-control short-input', 'type': 'date'}),
        }

# Category Form
# Handles creating and updating categories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            # Text input for the category name with Bootstrap styling
            'name': forms.TextInput(attrs={'class': 'form-control short-input'})
        }