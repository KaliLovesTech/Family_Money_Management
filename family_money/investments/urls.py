from django.urls import path
from .views import get_stock_info_view, get_company_financials_view, get_stock_history_view, get_market_news_view

app_name = 'investments'

urlpatterns = [
    path('get_stock_info/', get_stock_info_view, name='get_stock_info'),
    path('get_company_financials/', get_company_financials_view, name='get_company_financials'),
    path('get_stock_history/', get_stock_history_view, name='get_stock_history'),
    path('get_market_news/', get_market_news_view, name='get_market_news'),
]