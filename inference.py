import os
from env import HealthEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

env = HealthEnv()

print("[START]")

state = env.reset()
done = False
step_count = 0
total_reward = 0

print(f"[STEP] step={step_count} state={state} action=None reward=0 done={done}")

while not done and step_count < 20:

    hr = state["heart_rate"]
    temp = state["temperature"]

    if hr > 120 or temp > 39:
        action = 2
    elif hr > 100 or temp > 38:
        action = 1
    else:
        action = 0

    next_state, reward, done, _ = env.step(action)

    step_count += 1
    total_reward += reward

    print(f"[STEP] step={step_count} state={next_state} action={action} reward={reward} done={done}")

    state = next_state

print(f"[END] total_steps={step_count} total_reward={total_reward}")
