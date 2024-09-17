from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Bill, SavingsGoal, Budget, Expense, Income, Category
from .forms import BillForm, SavingsGoalForm, BudgetForm, ExpenseForm, IncomeForm, CategoryForm


# Bills
class BillListView(ListView):
    model = Bill
    template_name = 'financials/bill_list.html'
    context_object_name = 'bills'

    def get_queryset(self):
        # Return all bills
        return Bill.objects.all()


class BillCreateView(CreateView):
    model = Bill
    form_class = BillForm
    template_name = 'financials/bill_form.html'
    success_url = reverse_lazy('financials:bill_list')


class BillUpdateView(UpdateView):
    model = Bill
    form_class = BillForm
    template_name = 'financials/bill_form.html'
    success_url = reverse_lazy('financials:bill_list')


class BillDeleteView(DeleteView):
    model = Bill
    template_name = 'financials/bill_confirm_delete.html'
    success_url = reverse_lazy('financials:bill_list')


# Savings Goals
class SavingsGoalListView(ListView):
    model = SavingsGoal
    template_name = 'financials/savingsgoal_list.html'

    def get_queryset(self):
        return SavingsGoal.objects.all()


class SavingsGoalCreateView(CreateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'financials/savingsgoal_form.html'
    success_url = reverse_lazy('financials:savings_goal_list')


class SavingsGoalUpdateView(UpdateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'financials/savingsgoal_form.html'
    success_url = reverse_lazy('financials:savings_goal_list')


# Budgets
class BudgetListView(ListView):
    model = Budget
    template_name = 'financials/budget_list.html'

    def get_queryset(self):
        return Budget.objects.all()


class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'financials/budget_form.html'
    success_url = reverse_lazy('financials:budget_list')


class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'financials/budget_form.html'
    success_url = reverse_lazy('financials:budget_list')


# Expenses
class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'financials/expense_form.html'
    success_url = reverse_lazy('financials:expense_list')


class ExpenseListView(ListView):
    model = Expense
    template_name = 'financials/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        # Return all expenses, adjust if you want specific filtering
        return Expense.objects.all()


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'financials/expense_confirm_delete.html'
    success_url = reverse_lazy('financials:expense_list')

# Expense Update View
class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'financials/expense_form.html'
    success_url = reverse_lazy('financials:expense_list')

    def get_queryset(self):
        # Return the queryset for the Expense model
        return Expense.objects.all()


# Income

# IncomeListView
class IncomeListView(ListView):
    model = Income
    template_name = 'financials/income_list.html'
    context_object_name = 'incomes'

    def get_context_data(self, **kwargs):
        # Get the existing context
        context = super().get_context_data(**kwargs)
        # Calculate the total income
        total_income = Income.objects.aggregate(total=models.Sum('amount'))['total'] or 0
        # Add the total income to the context
        context['total_income'] = total_income
        return context


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'financials/income_form.html'
    success_url = reverse_lazy('financials:income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'financials/income_form.html'
    success_url = reverse_lazy('financials:income_list')


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'financials/income_confirm_delete.html'
    success_url = reverse_lazy('financials:income_list')


# Categories
class CategoryListView(ListView):
    model = Category
    template_name = 'financials/category_list.html'

    def get_queryset(self):
        # Return all categories
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'financials/category_form.html'
    success_url = reverse_lazy('financials:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'financials/category_form.html'
    success_url = reverse_lazy('financials:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'financials/category_confirm_delete.html'
    success_url = reverse_lazy('financials:category_list')