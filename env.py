import random

class HealthEnv:

    def __init__(self):
        self.state_data = {}
        self.done = False

    def reset(self):
        self.state_data = {
            "heart_rate": random.randint(70, 90),
            "temperature": round(random.uniform(36.5, 37.5), 1)
        }
        self.done = False
        return self.state_data

    def state(self):
        return self.state_data

    def step(self, action):
        hr = self.state_data["heart_rate"]
        temp = self.state_data["temperature"]

        # Simulate changes
        hr += random.randint(-5, 10)
        temp += round(random.uniform(-0.2, 0.5), 1)

        self.state_data = {
            "heart_rate": hr,
            "temperature": temp
        }

        reward = 0.0

        if hr > 120 or temp > 39:
            reward = 1.0 if action == 2 else 0.0
        elif hr > 100 or temp > 38:
            reward = 0.7 if action == 1 else 0.2
        else:
            reward = 1.0 if action == 0 else 0.3

        if hr > 130 or temp > 40:
            self.done = True

        return self.state_data, reward, self.done, {}
