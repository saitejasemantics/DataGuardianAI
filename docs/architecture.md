┌───────────────────────────────────────────────────────────┐
│                 Microsoft Fabric IQ Layer                │
│     Semantic Context • Business Knowledge • Metadata     │
└───────────────────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────────────────┐
│                   Agent Orchestrator                     │
│         Investigation Workflow & Reasoning Engine        │
└───────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Pipeline    │    │ Data Quality│    │ Schema      │
│ Agent       │    │ Agent       │    │ Agent       │
└─────────────┘    └─────────────┘    └─────────────┘

        └───────────────┬───────────────┘
                        ▼

              ┌─────────────────┐
              │ Root Cause Agent│
              │ Reasoning Layer │
              └─────────────────┘
                        │
                        ▼

              ┌─────────────────┐
              │ Business Impact │
              │ Agent           │
              └─────────────────┘
                        │
                        ▼

              ┌─────────────────┐
              │ Recommendation  │
              │ Agent           │
              └─────────────────┘
                        │
                        ▼

              ┌─────────────────┐
              │ Executive Agent │
              └─────────────────┘
                        │
                        ▼

┌───────────────────────────────────────────────────────────┐
│                Incident Intelligence Hub                 │
├───────────────────────────────────────────────────────────┤
│ Root Cause Analysis                                      │
│ Confidence Score                                         │
│ Business Impact Assessment                               │
│ AI Recommendations                                       │
│ Executive Summary                                        │
└───────────────────────────────────────────────────────────┘