class RequestLogger:
    def __init__(self, time_limit):
        # Store last printed timestamp for each message
        self.time_limit = time_limit
        self.message_timestamps = {}

    def message_request_decision(self, timestamp, request):
        # If message not seen before → allow
        if request not in self.message_timestamps:
            self.message_timestamps[request] = timestamp
            return True

        # Check time difference
        last_time = self.message_timestamps[request]

        if timestamp - last_time >= self.time_limit:
            # Update timestamp and allow
            self.message_timestamps[request] = timestamp
            return True
        else:
            # Reject (too soon)
            return False
