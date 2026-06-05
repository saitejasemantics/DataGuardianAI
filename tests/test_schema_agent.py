from agents.schema_agent import SchemaAgent

agent = SchemaAgent(
    "data/schema_changes.csv"
)

results = agent.investigate()

print(results)