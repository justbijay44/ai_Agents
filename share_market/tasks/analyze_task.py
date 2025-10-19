from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description= """
        Analyze the recent performance of the stock: {stock}. Use the live stock information tool to retrieve
        current price, percentage change, trading volume, and other market data. Provide a summary of how the stock
        is performing today and highlight any key observations from the data.
        """,
    expected_output= """
        A clear, bullet-point summary \n
        - Current Price \n
        - Daily Price Changes and percentage \n
        - Volume and Volatile \n
        - immediate trend or observation
        """,
    agent=analyst_agent
)