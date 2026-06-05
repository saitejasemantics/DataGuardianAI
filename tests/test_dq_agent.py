# tests/test_dq_agent.py

from agents.dq_agent import DataQualityAgent

agent = DataQualityAgent(
    "data/data_quality_metrics.csv"
)

results = agent.investigate()

print(results)