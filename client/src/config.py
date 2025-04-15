import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Alpha Vantage API Configuration
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "your_default_api_key")
    ALPHA_VANTAGE_BASE_URL = os.getenv("ALPHA_VANTAGE_BASE_URL", "https://www.alphavantage.co/query")

    # Stock Symbols to Monitor
    STOCK_SYMBOLS = os.getenv("STOCK_SYMBOLS", "AAPL,GOOGL,MSFT,AMZN,TSLA").split(",")

    # Server Configuration
    SERVER_URL = os.getenv("SERVER_URL", "http://localhost:8000/api/v1/stocks")

    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Retry Configuration
    RETRY_COUNT = int(os.getenv("RETRY_COUNT", 3))
    RETRY_DELAY = int(os.getenv("RETRY_DELAY", 5))

    # Poll Interval (in seconds)
    POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 60))

    @staticmethod
    def validate():
        if not Config.ALPHA_VANTAGE_API_KEY:
            raise ValueError("ALPHA_VANTAGE_API_KEY is not set in the environment variables.")
        if not Config.STOCK_SYMBOLS:
            raise ValueError("STOCK_SYMBOLS is not set in the environment variables.")
        if not Config.SERVER_URL:
            raise ValueError("SERVER_URL is not set in the environment variables.")
        if Config.RETRY_COUNT < 0:
            raise ValueError("RETRY_COUNT must be a non-negative integer.")
        if Config.RETRY_DELAY < 0:
            raise ValueError("RETRY_DELAY must be a non-negative integer.")
        if Config.POLL_INTERVAL <= 0:
            raise ValueError("POLL_INTERVAL must be a positive integer.")

