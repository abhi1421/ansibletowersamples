graph TD
    %% Define Styles
    classDef git fill:#F05032,stroke:#fff,color:#fff,font-weight:bold
    classDef ingress fill:#f9f9f9,stroke:#333,stroke-dasharray: 5 5
    classDef cluster fill:#00417a,stroke:#fff,color:#fff
    classDef storage fill:#333,stroke:#fff,color:#fff
    
    %% Elements
    Start((Push Code to Git)):::git --> Webhook[Webhook Sent]
    
    subgraph "External/Ingress"
    Webhook --> LB[Load Balancer]:::ingress
    end
    
    subgraph "Automation Gateway Tier"
    LB --> PGW1[PGW Node 1]:::cluster
    LB --> PGW2[PGW Node 2]:::cluster
    PGW1 -.-> Redis1[(Redis)]
    PGW2 -.-> Redis2[(Redis)]
    end
    
    subgraph "Event & Logic Tier"
    PGW1 --> EDA[EDA Node]:::cluster
    PGW2 --> EDA
    EDA -.-> Redis3[(Redis)]
    EDA -->|Trigger Job| CTRL[Controller Cluster]:::cluster
    end
    
    subgraph "Controller & Content Tier"
    CTRL --> CTRL1[Controller 1]
    CTRL --> CTRL2[Controller 2]
    CTRL1 -.-> Redis4[(Redis)]
    CTRL2 -.-> Redis5[(Redis)]
    HUB[Private Hub]:::cluster -->|EE Images/Collections| CTRL
    HUB -.-> Redis6[(Redis)]
    end
    
    subgraph "Execution Tier (The Mesh)"
    CTRL1 --> Mesh{Automation Mesh}
    CTRL2 --> Mesh
    Mesh --> EXEC1[Execution Node 1]:::cluster
    Mesh --> EXEC2[Execution Node 2]:::cluster
    end
    
    subgraph "Database Tier"
    PGW1 & PGW2 & EDA & CTRL1 & CTRL2 & HUB --> DB[(Central PostgreSQL)]:::storage
    end

    EXEC1 & EXEC2 --> End((Job Complete))