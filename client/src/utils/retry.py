import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry_with_exponential_backoff(max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 60.0):
    """
    Decorator to retry a function with exponential backoff.

    Args:
        max_retries (int): Maximum number of retries.
        base_delay (float): Base delay in seconds for the first retry.
        max_delay (float): Maximum delay in seconds between retries.

    Returns:
        Callable: Decorated function that will be retried on failure.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Retrying {func.__name__} due to error: {e}")
                    time.sleep(min(base_delay * (2 ** retries), max_delay))
                    retries += 1
            raise Exception(f"Function {func.__name__} failed after {max_retries} retries.")
        return wrapper
    return decorator

# Example usage
if __name__ == "__main__":
    @retry_with_exponential_backoff(max_retries=3, base_delay=2, max_delay=10)
    def fetch_data():
        """
        Simulates a function that may fail intermittently.
        """
        print("Attempting to fetch data...")
        # Simulate a failure
        raise Exception("Simulated network error")

    try:
        fetch_data()
    except Exception as e:
        print(f"Final failure: {e}")