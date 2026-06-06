from agents.business_impact_agent import BusinessImpactAgent

agent = BusinessImpactAgent(
    "data/business_impact.csv"
)

print(agent.assess())