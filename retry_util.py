import time


def call_with_retry(
    operation,
    max_attempts=3,
    base_delay=1
):
    for attempt in range(max_attempts):
        try:
            return operation()

        except Exception:
            if attempt == max_attempts - 1:
                raise

            delay = base_delay * (2 ** attempt)

            time.sleep(delay)