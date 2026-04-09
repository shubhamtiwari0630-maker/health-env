import os
from env import HealthEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

def choose_action(state):
    hr = state["heart_rate"]
    temp = state["temperature"]

    if hr > 120 or temp > 39:
        return 2
    elif hr > 100 or temp > 38:
        return 1
    else:
        return 0

def run_episode():
    env = HealthEnv()

    print("[START]")

    state = env.reset()
    done = False
    step_count = 0
    total_reward = 0.0

    print(f"[STEP] step={step_count} state={state} action=None reward=0.0 done={done}")

    while not done and step_count < 20:
        action = choose_action(state)

        next_state, reward, done, _ = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} state={next_state} action={action} reward={float(reward)} done={done}")

        state = next_state

    print(f"[END] total_steps={step_count} total_reward={round(total_reward,2)}")

if __name__ == "__main__":
    run_episode()
