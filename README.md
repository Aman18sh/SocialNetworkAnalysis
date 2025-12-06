**Sentiment-Aware Competitive Graph Diffusion Model**

This repository contains the core implementation of our research work on modeling how sentiment and trust influence the propagation of positive and negative information in online social networks.
The model extends classical diffusion frameworks and integrates Graph Neural Networks (EvolveGCN) for temporal prediction.

-- facebook.py       # Real-world diffusion experiments on Facebook network
-- synthetic.py      # Synthetic graph generation + diffusion simulations
-- toy.py            # Minimal example to understand the diffusion process
-- gnn.py            # GNN/EvolveGCN implementation for temporal modeling
-- requirements.txt  # Python dependencies
-- README.md         # Project documentation


**Sentiment-Aware Competitive Graph Diffusion Model for Negative Information Control in Online Social Networks**

**Overview**

Understanding how sentiment, trust, and user credibility influence the spread of information is critical for modeling realistic diffusion in online social networks.
This project introduces a sentiment- and trust-aware competitive diffusion model, extending the classical SIR framework to analyze the interaction between positive and negative contagions.


**Our model integrates:**

- Sentiment polarity (from textual data)
- Trust score (via centrality features such as degree & PageRank)
- Graph Convolutional Networks (EvolveGCN) to learn temporal diffusion patterns

**Key Contributions**

- A novel diffusion model capturing the effect of sentiment and trust on information propagation.
- A competitive diffusion setup modeling positive vs negative cascades.
- A temporal graph learning pipeline using EvolveGCN to predict future diffusion states.
- Synthetic and real-world experiments (e.g., Facebook datasets) showing strong prediction accuracy (>70%).
- Insights showing that high-trust nodes stabilize sentiment, while negative contagions exploit low-trust clusters.

**How the Model Works**

Sentiment Extraction:
- Text posts -> sentiment polarity score.

Trust Score Computation:
- Degree + PageRank centrality -> normalized trust.

Competitive SIR Diffusion:
- Positive and negative cascades compete for influence.

Temporal Evolution Learning:
- Graph snapshots -> EvolveGCN -> next-step prediction.


**Results (Summary)**

- Trust-rich nodes accelerate positive diffusion and stabilize sentiment.
- Negative contagions spread faster in low-trust communities.
- EvolveGCN achieves >70% accuracy in predicting future diffusion states.