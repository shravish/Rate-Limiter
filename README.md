# Rate-Limiter
The goal is to make a system that says “yes” or “no” when a user tries to make a request. But they’re only allowed to make N requests every T seconds.

So for example:
If we allow 3 requests every 10 seconds, and a user makes 3 quick requests—those are allowed.
If they try a 4th one right away, it’s blocked.
But after 10 seconds have passed since the first request, they can make another.

The core idea is to track the timestamps of requests for each user. You store those in a list, and each time they try to make a new request, you:

1.Remove old timestamps outside the time window.

2.Check how many recent ones are left.

3.If it’s fewer than the limit, allow and add the new timestamp.

4.Otherwise, reject it.

## Step one: 
We need a class called RateLimiter. Inside it, we’ll track requests per user. So first, in the __init__ method, we’ll set up the limit (like 3 requests per 10 seconds) and a dictionary to store timestamps per user.

## Step Two: Processing a request.

Now, we need to define the method is_allowed(user_id) that will:

Remove outdated timestamps: For each user, we look at their request timestamps and remove those that are outside the time window (older than T seconds).

Check the remaining requests: If there are fewer than max_requests within the window, we allow the new request, add the timestamp, and return True.

Reject the request: If there are already max_requests in the window, we deny the request and return False.

### What we’ve done:
1.timestamps stores the timestamps of when the user made their requests.

2.time.time() gives us the current time in seconds.

3.popleft() removes old requests from the front of the deque that are outside the time window.


