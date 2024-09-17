from django.urls import path
from .views import (
    BillListView, BillCreateView, BillDeleteView, BillUpdateView,
    SavingsGoalListView, SavingsGoalCreateView, SavingsGoalUpdateView,
    BudgetListView, BudgetCreateView, BudgetUpdateView,
    ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView,
    IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView, CategoryListView, CategoryCreateView,
    CategoryDeleteView, CategoryUpdateView,
)

app_name = 'financials'

urlpatterns = [
    # Bills
    path('bills/', BillListView.as_view(), name='bill_list'),
    path('bills/new/', BillCreateView.as_view(), name='bill_create'),
    path('bills/<int:pk>/edit/', BillUpdateView.as_view(), name='bill_edit'),  # Edit URL
    path('bills/<int:pk>/delete/', BillDeleteView.as_view(), name='bill_delete'),  # Delete URL

    # Savings Goals
    path('savings-goals/', SavingsGoalListView.as_view(), name='savings_goal_list'),
    path('savings-goals/new/', SavingsGoalCreateView.as_view(), name='savings_goal_create'),
    path('savings-goals/<int:pk>/edit/', SavingsGoalUpdateView.as_view(), name='savings_goal_update'),

    # Budgets
    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budgets/new/', BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget_update'),

    # Expenses
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
    path('expenses/new/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expenses/<int:pk>/edit/', ExpenseUpdateView.as_view(), name='expense_edit'),
    path('expenses/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),

    # Income
    path('income/', IncomeListView.as_view(), name='income_list'),
    path('income/new/', IncomeCreateView.as_view(), name='income_create'),
    path('income/<int:pk>/edit/', IncomeUpdateView.as_view(), name='income_edit'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income_delete'),
    
    # Categories
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]