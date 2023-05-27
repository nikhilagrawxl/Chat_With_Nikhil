# Chat_With_Nikhil

This chatbot basically uses OpenAI Api to handle the user queries.

The provided cDjango application that includes views for handling different requests related to a financial management chatbot. Here's a brief explanation:
1. The analyze_transactions() function is used to perform analysis on the provided transactions data. In this example, it calculates the total expenses and total income.
2. The chat() and about() views render the respective HTML templates (index.html and about.html) when the corresponding routes are accessed.
3.The chatAPI() view is responsible for handling the API endpoint for processing user queries. It expects a POST request with a "prompt" parameter, and it uses OpenAI's Completion API to generate a response based on the prompt.
4. The handle_query() function is called from the chatAPI() view and handles different types of queries. It analyzes the transactions data and generates an appropriate response based on the query type.

I have used OpenAI Playground to try the prompts and also fine tune the prompts. Some of them queries are:
User Query: How much money did I spend on groceries last month?
Chatbot Response: According to your transaction history, you spent a total of $200 on groceries last month.

User Query: Can you recommend a budgeting app to track my expenses?
Chatbot Response: Sure! I recommend using "Expense Tracker" app. It's user-friendly, allows you to categorize your expenses, set budget goals, and provides detailed spending reports.

User Query: How can I save more money on my utility bills?
Chatbot Response: Here are a few tips to save money on your utility bills: 1) Reduce energy consumption by turning off lights and appliances when not in use, 2) Use energy-efficient appliances, 3) Set your thermostat to an optimal temperature, 4) Seal air leaks around windows and doors, etc.

User Query: What is the average amount I spend on dining out per month?
Chatbot Response: Based on your transaction history, the average amount you spend on dining out per month is approximately $150.

User Query: How can I improve my savings?
Chatbot Response: To improve your savings, consider these strategies: 1) Create a monthly budget and track your expenses, 2) Set specific savings goals, 3) Automate your savings by setting up recurring transfers to a savings account, 4) Look for opportunities to reduce discretionary spending, etc.

User Query: Can you analyze my spending patterns?

Chatbot Response: Sure! I can analyze your spending patterns and provide you with insights to help you better understand your financial habits. Would you like to proceed?

User Query: What are my total expenses for the current year?
Chatbot Response: Based on your transaction history, your total expenses for the current year amount to $2,100.

User Query: How much did I earn from my side gig last month?
Chatbot Response: According to your transaction history, you earned a total of $500 from your side gig last month.

User Query: Can you recommend some investment options for long-term growth?
Chatbot Response: Sure! For long-term growth, you may consider investing in a diversified portfolio of stocks, index funds, or mutual funds. It's advisable to consult with a financial advisor to determine the best investment strategy based on your risk tolerance and financial goals.

User Query: What are my top spending categories?
Chatbot Response: Analyzing your transaction history, your top spending categories are "groceries," "bills," and "entertainment." These categories account for the majority of your expenses.

User Query: How can I reduce my monthly expenses?
Chatbot Response: To reduce your monthly expenses, consider these tips: 1) Review your subscriptions and cancel any that you don't use, 2) Compare prices before making purchases, 3) Cook meals at home instead of eating out, 4) Use public transportation or carpool to save on transportation costs, etc.

User Query: What is my current savings rate?
Chatbot Response: Based on your transaction history, your current savings rate is 25% of your monthly income.

To run this project just change the OpenAI API and in the terminal run "python manage.py"


