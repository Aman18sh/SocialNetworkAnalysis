import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import random
from textblob import TextBlob  # For sentiment analysis


# Creating a synthetic graph
random.seed(42)  # reproducibility
G = nx.erdos_renyi_graph(50, 0.12)  # 50 users with 12% connection probability

# Assign initial states to all nodes as Susceptible (S)
states = {node: 'S' for node in G.nodes()}

# Select initial infected nodes (positive and negative)
initial_I1 = random.sample(list(G.nodes()), 5)  # 5 positive influencers
initial_I2 = random.sample(list(set(G.nodes()) - set(initial_I1)), 3)  # 3 negative influencers

for node in initial_I1:
    states[node] = 'I1'
for node in initial_I2:
    states[node] = 'I2'


# Assign synthetic text + trust
user_text = {}
trust_scores = {}

sample_texts = [
    "I love this product. It’s amazing!", 
    "This service is awful and disappointing.", 
    "Pretty good experience overall.", 
    "Terrible support from the team!", 
    "The platform is excellent!"
]

for node in G.nodes():
    text = random.choice(sample_texts)
    user_text[node] = text
    sentiment = TextBlob(text).sentiment.polarity
    trust = round(random.uniform(0.4, 1.0), 2)
    trust_scores[node] = trust


# Assigning Parameters
base_beta_pos = 0.3
base_beta_neg = 0.4
gamma = 0.2  # Recovery probability


# Simulation step function
def step(states):
    new_states = states.copy()
    for node in G.nodes():
        if states[node] == 'S':
            neighbors = list(G.neighbors(node))
            for neighbor in neighbors:
                if states[neighbor] in ['I1', 'I2']:
                    sentiment = TextBlob(user_text[neighbor]).sentiment.polarity
                    trust = trust_scores[neighbor]
                    
                    if states[neighbor] == 'I1':
                        beta = base_beta_pos * trust * max(0, sentiment)
                        if random.random() < beta:
                            new_states[node] = 'I1'
                            break
                    elif states[neighbor] == 'I2':
                        beta = base_beta_neg * trust * abs(min(0, sentiment))
                        if random.random() < beta:
                            new_states[node] = 'I2'
                            break

        elif states[node] in ['I1', 'I2']:
            if random.random() < gamma:
                new_states[node] = 'R'
    return new_states


# Simulation with trajectories + snapshots
def simulate_with_trajectories(G, states, steps=15):
    pos = nx.spring_layout(G, seed=42)  # fixed layout for consistency
    snapshots = {}
    counts = {"S": [], "I1": [], "I2": [], "R": []}

    # adaptive snapshot selection
    snapshot_times = [0, steps//4, steps//2, 3*steps//4, steps]

    for t in range(steps+1):
        # record counts
        for state in ["S", "I1", "I2", "R"]:
            counts[state].append(sum(1 for s in states.values() if s == state))
        
        # record snapshots
        if t in snapshot_times:
            snapshots[t] = states.copy()
        
        # next step
        if t < steps:
            states = step(states)


    # Plotting snapshots 
    fig, axes = plt.subplots(1, len(snapshot_times), figsize=(20, 4))
    color_map = {'S': 'gray', 'I1': 'green', 'I2': 'red', 'R': 'blue'}

    labels = ['(a)', '(b)', '(c)', '(d)', '(e)']  # subfigure labels

    for i, t in enumerate(snapshot_times):
        node_colors = [color_map[snapshots[t][n]] for n in G.nodes()]
        nx.draw(G, pos, node_color=node_colors, ax=axes[i], node_size=80, with_labels=False)
        
        # add label BELOW manually (absolute axes coords)
        axes[i].text(
            0.5, -0.1, labels[i], 
            transform=axes[i].transAxes, 
            ha='center', va='top',
            fontsize=25, fontweight="bold"
        )
        
        # add timestep on top
        axes[i].set_title(f"t = {t}", fontsize=25)

    # Add legend manually 
    legend_handles = [
        mpatches.Patch(color='gray', label='S (Susceptible)'),
        mpatches.Patch(color='green', label='I1 (Positive)'),
        mpatches.Patch(color='red', label='I2 (Negative)'),
        mpatches.Patch(color='blue', label='R (Recovered)')
    ]
    fig.legend(
        handles=legend_handles,
        loc='lower center',  # put legend below plots
        ncol=4,
        fontsize=20,
        frameon=False
    )    

    plt.subplots_adjust(bottom=0.2)  # <-- give extra margin at bottom
    plt.savefig("synthetic_snapshots.png", dpi=300, bbox_inches="tight")
    plt.show()

    
    # Plotting trajectories 
    plt.figure(figsize=(7,5))
    plt.plot(counts["S"], label="Susceptible (S)", color="gray", marker="o")
    plt.plot(counts["I1"], label="Positive Infected (I1)", color="green", marker="o")
    plt.plot(counts["I2"], label="Negative Infected (I2)", color="red", marker="o")
    plt.plot(counts["R"], label="Recovered (R)", color="blue", marker="o")
    plt.xlabel("Time step",fontsize=15)
    plt.ylabel("Number of nodes",fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    # plt.title("Competitive Diffusion Dynamics")
    plt.legend(fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("synthetic_dynamics.png", dpi=300)
    plt.show()

# Run simulation
simulate_with_trajectories(G, states, steps=15)
