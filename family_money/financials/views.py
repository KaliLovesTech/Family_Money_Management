from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import logging

logger = logging.getLogger(__name__)

@login_required
def get_stock_info_view(request):
    symbol = request.GET.get('symbol', 'AAPL')  # Default to AAPL if no symbol provided
    url = "https://yahoo-finance160.p.rapidapi.com/info"
    payload = {"symbol": symbol}
    headers = {
        "x-rapidapi-key": "847ba95febmshc5c3ba75afc88a2p1ec10bjsnf5eb2eaa4310",
        "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        logger.error(f"Failed to fetch stock info for {symbol}: {response.status_code}")
        return JsonResponse({'error': 'Failed to fetch stock info'}, status=response.status_code)

@login_required
def get_company_financials_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    url = "https://yahoo-finance160.p.rapidapi.com/financials"
    payload = {"symbol": symbol}
    headers = {
        "x-rapidapi-key": "847ba95febmshc5c3ba75afc88a2p1ec10bjsnf5eb2eaa4310",
        "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        logger.error(f"Failed to fetch financials for {symbol}: {response.status_code}")
        return JsonResponse({'error': 'Failed to fetch financials'}, status=response.status_code)

@login_required
def get_stock_history_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    url = "https://yahoo-finance160.p.rapidapi.com/history"
    payload = {"symbol": symbol}
    headers = {
        "x-rapidapi-key": "847ba95febmshc5c3ba75afc88a2p1ec10bjsnf5eb2eaa4310",
        "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        logger.error(f"Failed to fetch history for {symbol}: {response.status_code}")
        return JsonResponse({'error': 'Failed to fetch stock history'}, status=response.status_code)

@login_required
def get_market_news_view(request):
    symbol = request.GET.get('symbol', 'AAPL')
    url = "https://yahoo-finance160.p.rapidapi.com/stocknews"
    payload = {"symbol": symbol}
    headers = {
        "x-rapidapi-key": "847ba95febmshc5c3ba75afc88a2p1ec10bjsnf5eb2eaa4310",
        "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        logger.error(f"Failed to fetch market news for {symbol}: {response.status_code}")
        return JsonResponse({'error': 'Failed to fetch market news'}, status=response.status_code)
    

