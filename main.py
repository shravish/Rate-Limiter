import time
from collections import defaultdict, deque
class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.user_requests = defaultdict(deque)  
        # stores timestamps per user

    def is_allowed(self, user_id):
        current_time = time.time()  
        # current timestamp in seconds

        # Remove timestamps that are outside the window (older than 'window' seconds)
        timestamps = self.user_requests[user_id]
        while timestamps and timestamps[0] < current_time - self.window:
            timestamps.popleft()

        # Check if the number of recent requests is within the limit
        if len(timestamps) < self.max_requests:
            # Allow the request: Add the current timestamp
            timestamps.append(current_time)
            return True
        else:
            # Deny the request (too many requests within the time window)
            return False
rate_limiter = RateLimiter(3, 10)  
# 3 requests every 10 seconds
print(rate_limiter.is_allowed('user1'))  
# True (1st request)
print(rate_limiter.is_allowed('user1'))  
# True (2nd request)
print(rate_limiter.is_allowed('user1'))  
# True (3rd request)
print(rate_limiter.is_allowed('user1'))  
# False (too many requests)

