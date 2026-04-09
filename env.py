import random

class HealthEnv:

    def __init__(self):
        self.state_data = {}
        self.done = False
        self.prev_heart_rate = None
        self.prev_temperature = None

    def reset(self):
        self.state_data = {
            "heart_rate": random.randint(70, 90),
            "temperature": round(random.uniform(36.5, 37.5), 1)
        }
        self.prev_heart_rate = self.state_data["heart_rate"]
        self.prev_temperature = self.state_data["temperature"]
        self.done = False
        return self.state_data

    def state(self):
        return self.state_data

    def step(self, action):
        hr = self.state_data["heart_rate"]
        temp = self.state_data["temperature"]

        # Simulate realistic change
        hr += random.randint(-3, 8)
        temp += round(random.uniform(-0.1, 0.4), 1)

        # Clamp values
        hr = max(50, min(180, hr))
        temp = max(35.0, min(42.0, temp))

        # Trend detection
        hr_trend = hr - self.prev_heart_rate
        temp_trend = temp - self.prev_temperature

        self.prev_heart_rate = hr
        self.prev_temperature = temp

        self.state_data = {
            "heart_rate": hr,
            "temperature": temp,
            "hr_trend": hr_trend,
            "temp_trend": temp_trend
        }

        reward = 0.0

        # Emergency condition
        if hr > 120 or temp > 39:
            if action == 2:
                reward = 1.0
            elif action == 1:
                reward = 0.5
            else:
                reward = 0.0

        # Warning condition
        elif hr > 100 or temp > 38 or hr_trend > 5:
            if action == 1:
                reward = 0.8
            elif action == 2:
                reward = 0.4
            else:
                reward = 0.2

        # Normal condition
        else:
            if action == 0:
                reward = 1.0
            else:
                reward = 0.3

        # Done condition
        if hr > 140 or temp > 41:
            self.done = True

        return self.state_data, float(reward), self.done, {}
