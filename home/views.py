from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"

transactions = [
    {"date": "2021-01-01", "amount": 1000, "category": "income", "description": "salary"},
    {"date": "2021-01-02", "amount": -50, "category": "groceries", "description": "milk and eggs"},
    {"date": "2021-01-03", "amount": -100, "category": "entertainment", "description": "movie tickets"},
    {"date": "2021-01-04", "amount": -20, "category": "transportation", "description": "bus fare"},
    {"date": "2021-01-05", "amount": -200, "category": "bills", "description": "electricity bill"},
    {"date": "2021-01-06", "amount": -30, "category": "groceries", "description": "bread and cheese"},
    {"date": "2021-01-07", "amount": -150, "category": "clothing", "description": "new shoes"},
    {"date": "2021-01-08", "amount": -40, "category": "healthcare", "description": "prescription drugs"},
    {"date": "2021-01-09", "amount": -80, "category": "education", "description": "online course"},
    {"date": "2021-01-10", "amount": -60, "category": "entertainment", "description": "pizza delivery"},
    {"date": "2021-01-11", "amount": -25, "category": "transportation", "description": "taxi ride"},
    {"date": "2021-01-12", "amount": -300, "category": "bills", "description": "internet bill"},
    {"date": "2021-01-13", "amount": -50, "category": "groceries", "description": "fruits and vegetables"}
]

def analyze_transactions(transactions):
    # Implement your transaction analysis logic here
    # For simplicity, this example calculates total expenses and income
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['amount'] < 0)
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['amount'] > 0)
    return total_expenses, total_income


# Create your views here.
def chat(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST["prompt"]
        # response={"this":"that"}
        response = openai.Completion.create(
        engine="davinci",
        prompt=request,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
        print(response)
        return response.choices[0].text.strip()
    return HttpResponse("Bad Request")

def handle_query(request):
    if "spending patterns" in request:
        # Analyze transactions to extract spending patterns
        # In this example, calculate total expenses
        total_expenses, _ = analyze_transactions(transactions)
        response = f"Your total expenses are ${total_expenses:.2f}."
    
    elif "income sources" in request:
        # Analyze transactions to extract income sources
        # In this example, calculate total income
        _, total_income = analyze_transactions(transactions)
        response = f"Your total income is ${total_income:.2f}."

    elif "savings goals" in request:
        # Implement logic to provide savings goals advice based on transactions
        response = "Here's a suggestion for setting savings goals..."

    elif "financial advice" in request:
        # Implement logic to provide personalized financial advice based on transactions
        response = "Here's some financial advice for you..."

    else:
        # Handle other types of queries or provide a default response
        response = "I'm sorry, I couldn't understand your query."

    return response
