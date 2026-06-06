from agents.executive_agent import ExecutiveAgent

root_causes = [
    {"root_cause": "Schema Drift"},
    {"root_cause": "Data Quality Degradation"}
]

impacts = [
    {"dashboard": "Revenue Dashboard"},
    {"dashboard": "Customer Dashboard"}
]

recommendations = [
    "Implement schema validation",
    "Add DQ monitoring"
]

agent = ExecutiveAgent()

summary = agent.summarize(
    root_causes,
    impacts,
    recommendations
)

print(summary)