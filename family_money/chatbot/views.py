from django.http import JsonResponse
import requests
import json
import logging

logger = logging.getLogger(__name__)


def get_chatbot_response_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data
            query = data.get('query')  # Extract the 'query' field

            response = requests.post(
                url="https://yahoo-finance160.p.rapidapi.com/finbot",
                headers={
                    "x-rapidapi-key": "your_api_key_here",
                    "x-rapidapi-host": "yahoo-finance160.p.rapidapi.com",
                    "Content-Type": "application/json"
                },
                json={"query": query}
            )

            logger.debug(f"Chatbot API Response: {response.status_code} {response.text}")

            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data)
            else:
                return JsonResponse({'error': 'Failed to get chatbot response'}, status=response.status_code)
        except Exception as e:
            logger.error(f"Error processing chatbot response: {str(e)}")
            return JsonResponse({'error': 'Failed to process request'}, status=500)