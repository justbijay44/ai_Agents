from dotenv import load_dotenv
from crew import stock_crew

load_dotenv('../.env')

def run(stock: str):
    result = stock_crew.kickoff(inputs={'stock': stock})
    print(result)

if __name__ == "__main__":
    run("Apple")
