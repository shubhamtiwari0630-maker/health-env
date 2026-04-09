# AI Health Monitoring OpenEnv

## Overview
This project is a real-world OpenEnv environment where an AI agent learns to monitor health data and take decisions.

## State Space
- heart_rate (0–200)
- temperature (30–45°C)

## Action Space
0 → Do Nothing  
1 → Warning  
2 → Emergency  

## Reward
- Correct action → High reward  
- Wrong action → Low reward  

## Tasks
- Easy → High BPM detection  
- Medium → Trend detection  
- Hard → Multi-sensor decision  

## Run
python inference.py

## Docker
docker build -t health-env .
docker run health-env
