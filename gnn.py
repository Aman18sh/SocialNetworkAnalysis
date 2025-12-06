import random
import math
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch.nn import GRU

# Example Facebook text data (shortened for runtime) 

facebook_text = [
 ' Excited about the upcoming weekend getaway!        ',
 ' Rainy days call for cozy blankets and hot cocoa.   ',
 ' Missing summer vibes and beach days.               ',
 " Exploring the city's hidden gems.                  ",
 ' Reflecting on the past and looking ahead.          ',
 ' Attending a virtual conference on AI.              ',
 ' Exploring the world of virtual reality.            ',
 ' Celebrating a milestone at work! 🎉               ',
 ' Learning a new language for personal growth.       ',
 ' New painting in progress! 🎨                       ',
 ' Coding a new project with enthusiasm.              ',
 ' Quality time with family this weekend.             ',
 ' Trying out a new dessert recipe.                   ',
 " Celebrating a friend's birthday tonight! 🎂       ",
 ' Exploring local art galleries this weekend.        ',
 ' Reflecting on the beauty of nature.                ',
 ' Starting a new fitness challenge tomorrow! 💪     ',
 ' Heartbroken after hearing the news about a natural disaster. ',
 ' Laughter is the best medicine—enjoying a comedy show. ',
 ' Enjoying a quiet evening with a book and some tea.      ',
 ' Experiencing awe at the breathtaking sunset.            ',
 " Finding acceptance in the midst of life's challenges.   ",
 ' A bitter experience turned into a valuable lesson.      ',
 ' Excitement building up for the upcoming vacation!       ',
 ' A moment of shame for not standing up against injustice. ',
 ' Heartfelt sadness after bidding farewell to a dear friend. ',
 ' Laughter is the key to joy—attending a stand-up comedy show. ',
 ' Enjoying every moment of this trip—pure enjoyment!      ',
 ' Awe-struck by the beauty of the night sky.               ',
 " Embracing acceptance of life's ups and downs.           ",
 ' Bitter experience at the customer service department.   ',
 ' Excitement building up for a surprise birthday party.   ',
 ' A moment of shame for not speaking up against injustice.',
 ' Calmness prevails as I practice mindfulness.            ',
 ' Kindness witnessed today restores my faith in humanity.  ',
 ' Embracing the beauty of nature, a moment of contentment. ',
 ' Hopeful for a brighter tomorrow, despite challenges.  ',
 ' A moment of tenderness, connecting with loved ones.    ',
 ' Feeling a sense of fulfillment after reaching a milestone.',
 ' The euphoria of a live music concert under the stars.  ',
 ' Gratitude for the support received during tough times. ',
 ' Compassion towards those in need during the holidays.  ',
 ' Enthusiasm for a creative project in the making.       ',
 ' Elation after achieving a personal goal.               ',
 ' Contentment in the simplicity of a home-cooked meal. ',
 ' Hopeful about the prospects of a new business venture.',
 ' Tenderness in a heartfelt message to a loved one.    ',
 ' Feeling a sense of fulfillment after helping others. ',
 ' The euphoria of a successful product launch.         ',
 ' Gratitude for the small joys that each day brings.   ',
 ' Compassion in volunteering for a local charity.       ',
 ' Enthusiasm for a DIY home improvement project.       ',
 ' Elation after a surprise reunion with a childhood friend.',
 ' Loneliness creeps in as the night grows colder.    ',
 ' Frustration mounts as obstacles block my path.     ',
 ' Intimidation by the unknown future ahead.          ',
 ' Regret over missed opportunities haunts my thoughts.',
 ' Grief weighs heavy, tears a constant companion.    ',
 ' Resentment festers, poisoning relationships.       ',
 ' Anxiety grips my chest, a relentless grip on my thoughts.',
 " Envy poisons my thoughts, coveting others' success.",
 ' Sinking in despair, each day darker than the last. ',
 ' Jealousy poisons my thoughts, resentment brewing within.',
 ' Boredom lingers, a stagnant pool of indifference.  ',
 ' The complex puzzle of life leaves me in a state of perpetual confusion, seeking answers in the chaos. ',
 " Revisiting old photographs, caught in the embrace of nostalgia's bittersweet symphony. ",
 ' Facing challenges head-on, a determination that fuels the fire within to achieve the impossible. ',
 ' Floating through the day with an air of indifference, detached from the mundane happenings around. ',
 ' Melancholy whispers in the breeze, a silent conversation with the echoes of forgotten dreams. ',
 ' Embracing the flaws, finding acceptance in imperfection, a journey towards self-love. ',
 ' Exploring new horizons with the spark of curiosity, an adventurer in the vast landscape of knowledge. ',
 ' Immersed in a state of emotional numbness, a shield against the storm of daily struggles. ',
 ' Torn between opposing emotions, an ambivalence that colors my decisions with shades of uncertainty. ',
 ' Basking in the serenity of a quiet forest, where the whispers of nature bring peace to the soul. ',
 ' Navigating through the labyrinth of thoughts, confusion a constant companion in the maze of ideas. ',
 ' A journey into the past, flipping through the pages of an old diary, nostalgia taking the lead. ',
 ' Determination as the driving force, propelling me forward on the path to extraordinary achievements. ',
 ' Drifting through the day with an air of nonchalance, indifferent to the trivialities of life. ',
 ' Melancholy as a companion, painting the canvas of life with the brushstrokes of wistful yearning. ',
 " Embracing the beauty in imperfections, finding acceptance in the mosaic of life's unpredictable art. ",
 ' Fueled by curiosity, venturing into uncharted realms, a fearless explorer of the mysteries of the world. ',
 ' Basking in the golden glow of contentment, a serene river flowing through the landscape of the heart. ',
 ' A heart overflowing with gratitude, a garden where appreciation blooms in the soil of kindness and connection. ',
 ' Playfully dancing in the rain of laughter, a whimsical spirit twirling in the puddles of joy and lightheartedness. ',
 ' Navigating the sea of hope, sailing towards the sunrise of possibilities, confident in the ship of positive anticipation. ',
 ' In the embrace of the autumn breeze, leaves of ambivalence dancing in a waltz between choices and uncertainties. ',
 ' A compassionate rain, tears of empathy falling gently, nurturing the seeds of kindness in the garden of human connections. ',
 ' A playful escapade in the carnival of life, carousel laughter and cotton candy dreams swirling in the joyous atmosphere. ',
 ' With empathy as a lantern, wandering through the dark alleys of sorrow, illuminating the path with compassion and care. ',
 ' Confident strides in the dance of life, a ballroom where self-assuredness leads, twirling through challenges with grace. ',
 ' Whispering tales of inspiration to the stars, a storyteller crafting constellations from the threads of imagination. ',
 ' A playful escapade in the carnival of life, carousel laughter and cotton candy dreams swirling in the joyous atmosphere. ',
 ' With empathy as a lantern, wandering through the dark alleys of sorrow, illuminating the path with compassion and care. ',
 ' Confident strides in the dance of life, a ballroom where self-assuredness leads, twirling through challenges with grace. ',
 ' Whispering tales of inspiration to the stars, a storyteller crafting constellations from the threads of imagination. ',
 ' A playful escapade in the carnival of life, carousel laughter and cotton candy dreams swirling in the joyous atmosphere. ',
 ' Bitterness festering like a venomous vine, entwining the soul in a web of resentment, poisoning the garden of peace. ',
 ' Eyes wide open in the night, fearful shadows dancing on the walls, the mind a prisoner of imagined horrors. ',
 " Jealousy, a green-eyed monster, lurking in the shadows, casting a dark cloud over the sunshine of others' success. ",
 ' Envious eyes fixated on the gilded prize, a heartache fueled by the painful desire for possessions that seem forever out of reach. ',
 " Loneliness, a silent companion in the night, the only echo in the chamber of solitude, a heart's solitary nocturne. ",
 ' Overwhelmed by the cacophony of expectations, a drowning soul in the tempest of pressure, struggling to stay afloat. ',
 ' Frustrated attempts to mend a broken connection, the threads of understanding slipping through the fingers like grains of sand. ',
 ' Despair like a heavy fog, enveloping every thought, blurring the path ahead, a journey in the labyrinth of utter hopelessness. ',
 ' Yearning for the warmth of a vanished sun, a heartache painted in the hues of a sunset that never graced the horizon. ',
 ' Overwhelmed by the maze of expectations, a minotaur of pressure lurking in the labyrinth, waiting to devour the spirit of resilience. ',
 ' Frustrated attempts to untangle the knot of confusion, the threads of understanding slipping further into the labyrinth of miscommunication. ',
 " Loneliness, a silent companion in the night, the only echo in the chamber of solitude, a heart's solitary nocturne. ",
 'Nostalgia hits while flipping through an old photo album.     ',
 'Overwhelmed by the support received during a personal challenge.',
 'Curiosity sparked by exploring a mysterious ancient ruin.      ',
 'Motivated to achieve fitness goals after an invigorating workout.  ',
 'Amused by the antics of playful kittens during playtime.           ',
 'Excitement builds while preparing for a surprise celebration.     ',
 'Captivated by the serenity of a tranquil garden in full bloom.     ',
 'Nostalgic memories flood in while revisiting childhood favorites. ',
 'Contentment in the midst of a family gathering filled with laughter. ',
 'A sense of accomplishment after completing a challenging workout.',
 'Pride in achieving a personal milestone in career progression.   ',
 'Curiosity piqued by the mysteries of an ancient archaeological site.',
 "Giggles and joy echo in the air during a children's playdate.      ",
 'Spellbound by the elegance of a ballroom dance under crystal chandeliers. ',
 "Embracing the thrill of speed on a rollercoaster's exhilarating twists. ",
 'Radiant joy akin to blooming flowers on a sun-kissed spring morning. ',
 'Whispers of inspiration from the rustling leaves in a serene forest. ',
 'Heartfelt gratitude for the laughter shared during a family reunion. ',
 "Awe-inspired by the grandeur of an ancient cathedral's intricate architecture. ",
 'Joyful laughter resonates through a lively summer carnival.         ',
 "Dazzled by the elegance of a masquerade ball's dazzling costumes. ",
 "Riding the adrenaline rush on a rollercoaster's wild twists.      ",
 'Radiant joy akin to blossoming flowers on a sunlit spring morning. ',
 'Whispers of inspiration from the rustling leaves in a serene forest. ',
 'Heartfelt gratitude for the laughter shared during a family reunion. ',
 "Awe-struck by the grandeur of an ancient cathedral's intricate architecture. ",
 'Inspired by the resilience of a lone tree standing tall in a storm. ',
 'Spark of inspiration ignites like a shooting star in the night sky. ',
 'Awash with serenity as the sun sets over a tranquil lakeside retreat. ',
 'Tears fall like raindrops, mourning the end of a cherished friendship. ',
 'Aching heart, the symphony of pain plays in the silence of solitude. ',
 'Torn apart by grief, the echoes of loss reverberate through the soul. ',
 'Painful echoes of a love once cherished, now lost in the abyss of time. ',
 'Bitterness like a poison, seeping into every crevice of the wounded heart. ',
 'Darkness descends, engulfing the soul in the shadows of despair.  ',
 'In the labyrinth of grief, the walls echo with the footsteps of lost joy. ',
 'In the ruins of hope, echoes of shattered dreams whisper tales of loss. ',
 'In the wasteland of lost trust, the echoes of broken promises reverberate. ',
 'In the labyrinth of despair, the echoes of a broken heart reverberate endlessly. ',
 'Tears, the currency of grief, spent in the marketplace of lost love and longing. ',
 'In the tapestry of despair, threads of hope unravel, leaving a portrait of sorrow. ',
 'In the symphony of grief, each tear is a note, composing a melancholic melody. ',
 'Wandering through the cemetery of lost dreams, tombstones marking untold sorrows. ',
 'In the gallery of broken promises, each shattered vow framed, a painful exhibition. ',
 'In the garden of contentment, each bloom whispers tales of inner peace and joy. ',
 'Basking in the glow of accomplishment, each milestone a stepping stone to happiness. ',
 'Draped in the warmth of kindness, a quilt of compassion stitched with love. ',
 'In the symphony of excitement, each note is a burst of energy, igniting the soul with fervor. ',
 'Floating on clouds of gratitude, each raindrop a blessing, a shower of thankfulness. ',
 'A symphony of laughter, each note a key to unlocking the door of boundless happiness. ',
 'Exploring the wonders of Ferrari World, the roar of engines creating a symphony of speed. ',
 'Journeying through the serenity of Santorini, where each sunset paints the sky with hues of tranquility. ',
 'At the summit of Machu Picchu, a breathtaking panorama that whispers the secrets of ancient civilizations. ',
 'Sailing the azure waters of the Maldives, each wave a whisper of serenity in paradise. ',
 'At the summit of Mount Fuji, a breathtaking sunrise that paints the sky with hues of accomplishment. ',
 "In the tranquility of Kyoto's bamboo forest, whispers of ancient Zen wisdom echo through the groves. ",
 "In the crowd of a Taylor Swift concert, the lyrics of 'Love Story' create an enchanting fairy tale. ",
 "Immersed in the pulsating beats of a Bruno Mars concert, where 'Uptown Funk' becomes a city of joy. ",
 'In the mosh pit of a Metallica concert, the thunderous chords create a symphony of headbanging ecstasy. ',
 "Immersed in the soulful melodies of Adele, tears flow freely, moved by the emotion of 'Hello'. ",
 "Dancing to Shakira's rhythmic beats, hips swaying to the hypnotic charm of 'Hips Don't Lie'. ",
 "In the crowd of an Ariana Grande concert, the high notes of 'Into You' create a euphoric symphony. ",
 "Streaming the latest web series, the viewer is engrossed in the characters' journey, feeling a sense of connection and empathy. ",
 'At the Oscars, the actor graciously accepts an award, radiating joy and gratitude for the recognition of their outstanding performance. ',
 'Binge-watching a thrilling crime series, the suspense keeps the viewer on the edge of their seat, creating a rush of adrenaline. ',
 'In the cricket championship, a nail-biting finish leaves fans on the edge of their seats, experiencing a rollercoaster of emotions. ',
 'Cheering for the underdog in the basketball finals, the crowd erupts in applause as the team defies odds to claim the championship title. ',
 'In the cycling world championship, the climber conquers challenging terrains, symbolizing determination and achievement against all odds. ',
 'Facing a defeat in the championship, the boxer reflects on the challenges, vowing to return stronger and more determined in the next bout. ',
 'In the golf tournament, a missed crucial putt results in defeat, causing the golfer to reflect on the pressure of high-stakes competition. ',
 "The weightlifter's failed attempt at a personal record results in frustration, highlighting the challenging nature of pushing physical limits. ",
 'Amidst the bustling city, a quiet café becomes a sanctuary for reflection, where a cup of coffee brings solace to the wandering mind. ',
 'Connecting with the melody of a live orchestra, the music enthusiast experiences a symphony that resonates deep within the soul. ',
 'In the realm of literature, a captivating novel transports the reader to distant lands, weaving a tapestry of imagination and escape. ',
 'As the first snowflake descends, the winter enthusiast eagerly prepares for a season of frosty delights, anticipating the magic of snow-covered landscapes. ',
 'At the astronomy observatory, the stargazer marvels at the vastness of the cosmos, contemplating the mysteries hidden within the celestial expanse. ',
 "As the waves crash against the shore, the surfer embraces the thrill of riding the ocean's energy, capturing the essence of freedom in each wave. ",
 'Spent an hour choosing the perfect filter for a selfie. The struggle for that Instagram aesthetic is real. #SelfieQueen #TeenVibes ',
 "Got dressed for the day, then remembered it's Saturday. Oops. #WeekendVibes #TeenStruggles ",
 "Staring at the clock in class, waiting for the bell to ring like it's the most exciting event of the day. #ClassCountdown #TeenLife ",
 'Spent the day binge-watching a new series. Productivity level: Zero. #LazyDay #TVSeriesMarathon ',
 'Spent hours creating the perfect playlist for every mood. Music is my therapy. #PlaylistMaker #TeenMusicLover ',
 'Attended a concert and danced the night away. Music is the heartbeat of life. #ConcertVibes #DanceAllNight ',
 'Spent the afternoon at a museum, pretending to be cultured. Art enthusiast in the making. #MuseumDay #TeenArtLover ',
 "Exploring the world of digital art. It's never too late to discover new passions. #DigitalArtistry #LateBloomer ",
 'Attended a classical music concert, feeling the timeless melodies resonate. Music transcends generations. #ClassicalMusic #TimelessMelodies ',
 'Embarked on a road trip to revisit cherished places from the past. Nostalgia, the ultimate travel companion. #RoadTrip #NostalgiaTour ',
 "Taking a stroll in the garden, appreciating the beauty of blooming flowers. Nature's wonders never cease. #GardenWalk #FloralBeauty ",
 'Embarking on a journey of writing a memoir, documenting a lifetime of experiences. Every story matters. #MemoirWriting #SeniorStories ',
 'Joined a nature photography club, capturing the beauty of the great outdoors. Every click is a connection to nature. #NaturePhotography #SeniorPhotographer ',
 'Attended a vintage car show, reminiscing about the classics that once ruled the roads. Nostalgia in every rev. #VintageCars #ClassicRides ',
 'Visited an art gallery, appreciating the brushstrokes that tell tales of creativity. Art, an eternal companion. #ArtGallery #SeniorArtLover ',
 'Participated in a local theater production, proving that the stage belongs to every age. #TheaterProduction #SeniorActor ',
 "Joined a seniors' cycling club, feeling the wind in my hair and the freedom of the open road. #CyclingClub #SeniorCyclist ",
 'Organized a community painting event, turning blank canvases into a masterpiece of shared creativity. #PaintingEvent #SeniorArtist ',
 'Attended a local jazz festival, tapping toes to the tunes that have stood the test of time. Music, a lifelong love affair. #JazzFestival #SeniorMusicLover ',
 "Joined the school debate team. Words are my weapons, and I'm ready for battle! ",
 'Convinced the teacher to have class outdoors. Learning equations with a side of fresh air! ',
 'Bonding with friends over the latest K-pop sensation. Fangirling at its finest! ',
 'Joined the drama club to unleash my inner actor. Lights, camera, action! ',
 'Attempting to break the school record for the longest handstand. Wish me luck! ',
 'Spent hours on a TikTok dance, only to realize I have two left feet. Dance fail: Unleashed! ',
 'Trying to set a new trend by juggling textbooks between classes. Academic juggling: A unique skill! ',
 'Danced in the rain to celebrate the end of exams. Rain dance: Unexpectedly refreshing! ',
 'Creating a secret handshake with friends. Friendship level: Expert! ',
 'Accidentally sent a love letter to the wrong person. Love note fail: Maximum embarrassment! ',
 'Organizing a movie marathon with friends. Popcorn and cinematic adventures await! ',
 'Building a time capsule to capture memories for the future. Time-traveling emotions! ',
 'Had a bad day at school. Everything seems to be going wrong. ',
 'Received a not-so-great grade on a major project. Academic frustration setting in. ',
 'Experiencing cyberbullying. Hateful messages online are disheartening. ',
 'Dealing with unfounded rumors circulating about personal life. Rumors can be hurtful. ',
 'Facing rejection from a dream college. Disheartened but determined to explore other paths. ',
 "Feeling a sense of despair after a major project failure. Hard work didn't pay off this time. ",
 'Missing out on a long-anticipated event due to unexpected circumstances. A day filled with sadness. ',
 'Sharing favorite book recommendations with classmates. Building a mini book club. ',
 'Exploring a new part-time job opportunity for gaining work experience. Career development in progress. ',
 'Participating in a science fair to showcase a unique experiment. Sharing knowledge with peers. ',
 'Collaborating on a group project to promote teamwork and shared responsibilities. Group effort in action. ',
 'Attending a school talent show to support classmates. Applauding the diverse talents on display! ',
 'Receiving a heartfelt letter from a pen pal in another country. Connecting across the globe! ',
 'Collaborating on a science project that received recognition at a regional fair. Science triumphs and smiles! ',
 'Participating in a multicultural festival, celebrating diversity with music, dance, and delicious food! '
]

N = 100
p = 0.10
G = nx.erdos_renyi_graph(N, p, seed=42)

# Sentiment analysis fallback 
def _fallback_sentiment(text: str) -> float:
    pos = {'love','great','excellent','enjoy','joy','grateful','hope','content','enthusiasm','euphoria','gratitude','kindness','laugh','excited'}
    neg = {'awful','terrible','bitter','grief','sad','resentment','anxiety','envy','jealousy','despair','loneliness','frustration','fear','regret','heartbroken'}
    t = text.lower()
    score = sum(w in t for w in pos) - sum(w in t for w in neg)
    return max(-1.0, min(1.0, score/4.0))

try:
    from textblob import TextBlob
    def sentiment_score(text: str) -> float:
        return float(TextBlob(text).sentiment.polarity)
except Exception:
    def sentiment_score(text: str) -> float:
        return _fallback_sentiment(text)

# Assign posts and sentiment
random.seed(7)
k_posts = 3
for n in G.nodes():
    posts = random.sample(facebook_text, k=min(k_posts, len(facebook_text)))
    G.nodes[n]['posts'] = posts
    s = sum(sentiment_score(t) for t in posts)/len(posts)
    G.nodes[n]['sentiment'] = max(-1.0, min(1.0, s))

# Trust / Influence 
deg = nx.degree_centrality(G)
pr = nx.pagerank(G, alpha=0.85)
def minmax(d):
    vals = list(d.values())
    lo, hi = min(vals), max(vals)
    return {k: 0.0 if hi==lo else (v-lo)/(hi-lo) for k,v in d.items()}

deg_n = minmax(deg)
pr_n  = minmax(pr)

alpha, beta = 0.6, 0.4
for n in G.nodes():
    trust = alpha*deg_n[n] + beta*pr_n[n]
    G.nodes[n]['trust'] = float(trust)

# Initial states
nodes_by_sent = sorted(G.nodes(), key=lambda u: G.nodes[u]['sentiment'])
initial_I2 = nodes_by_sent[:5]
initial_I1 = nodes_by_sent[-6:]
states = {n: 'S' for n in G.nodes()}
for n in initial_I1: states[n] = 'I1'
for n in initial_I2: states[n] = 'I2'

# Diffusion parameters
base_beta_pos = 0.30
base_beta_neg = 0.40
gamma = 0.20

def combine_prob(p_accum, p_new):
    p_new = max(0.0, min(1.0, p_new))
    return 1 - (1 - p_accum) * (1 - p_new)

def step(states):
    new_states = states.copy()
    for u in G.nodes():
        if states[u] == 'S':
            pos_p = 0.0
            neg_p = 0.0
            for v in G.neighbors(u):
                sv = G.nodes[v]['sentiment']
                tv = G.nodes[v]['trust']
                if states[v] == 'I1':
                    p = base_beta_pos * tv * max(0.0, sv)
                    pos_p = combine_prob(pos_p, p)
                elif states[v] == 'I2':
                    p = base_beta_neg * tv * max(0.0, -sv)
                    neg_p = combine_prob(neg_p, p)
            r = random.random()
            if r < pos_p:
                new_states[u] = 'I1'
            elif r < pos_p + neg_p:
                new_states[u] = 'I2'
        elif states[u] in ('I1','I2'):
            if random.random() < gamma:
                new_states[u] = 'R'
    return new_states

# Code Testing ===============================

print(G)
print(len(G.nodes))
print(len(G.edges))
# print(G.nodes)
# print(G.edges)
# print(list(G.nodes))
# print(list(G.edges))
print(G.nodes[3])
# print(G.nodes['sentiment'])
# G.nodes['Trust']

l = []
for i in range(5):
    l.append(G.nodes[i])

print(l)
print(states)


#==================================================================================================================================================


# Function for Visualizing True Diffusion vs Predicted Diffusion 

import torch
import torch.nn.functional as F
from torch.nn import GRU
from torch_geometric.nn import GCNConv
from torch_geometric.utils import from_networkx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

# Define Diffusion + Visualization 

def visualize_diffusion_snapshots(G, true_states_over_time, pred_states_over_time, steps=35):

    # Visualize the true vs predicted diffusion at selected timesteps.

    pos = nx.spring_layout(G, seed=42)
    snapshot_times = [0, steps//4, steps//2, 3*steps//4, steps]
    color_map = {'S': 'gray', 'I1': 'green', 'I2': 'red', 'R': 'blue'}
    labels = ['(a)', '(b)', '(c)', '(d)', '(e)']

    fig, axes = plt.subplots(2, len(snapshot_times), figsize=(22, 8))

    # Row 1: True diffusion
    for i, t in enumerate(snapshot_times):
        node_colors = [color_map[true_states_over_time[t][n]] for n in G.nodes()]
        nx.draw(G, pos, node_color=node_colors, node_size=80, with_labels=False, ax=axes[0, i])
        axes[0, i].set_title(f"t={t}", fontsize=18)
        axes[0, i].text(
            0.5, -0.1, labels[i],
            transform=axes[0, i].transAxes, ha='center', va='top',
            fontsize=20, fontweight='bold'
        )

    # Row 2: Predicted diffusion
    for i, t in enumerate(snapshot_times):
        node_colors = [color_map[pred_states_over_time[t][n]] for n in G.nodes()]
        nx.draw(G, pos, node_color=node_colors, node_size=80, with_labels=False, ax=axes[1, i])
        axes[1, i].set_title(f"t={t}", fontsize=18)
        axes[1, i].text(
            0.5, -0.1, labels[i],
            transform=axes[1, i].transAxes, ha='center', va='top',
            fontsize=20, fontweight='bold'
        )

    # Legend 
    legend_handles = [
        mpatches.Patch(color='gray', label='S (Susceptible)'),
        mpatches.Patch(color='green', label='I1 (Positive)'),
        mpatches.Patch(color='red', label='I2 (Negative)'),
        mpatches.Patch(color='blue', label='R (Recovered)')
    ]
    fig.legend(handles=legend_handles, loc='lower center', ncol=4, fontsize=20, frameon=False)
    # fig.suptitle("True vs Predicted Diffusion Snapshots", fontsize=22, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()


# ===========================================================================================================================================================


# Build Temporal Graphs (35 steps)
steps = 35
graphs_over_time = []
true_states_over_time = []  # to store for visualization

for t in range(steps + 1):
    # Save true states for visualization
    true_states_over_time.append(states.copy())

    # Update node features
    for n in G.nodes():
        G.nodes[n]['x'] = [G.nodes[n]['sentiment'], G.nodes[n]['trust']]

    g_t = from_networkx(G)   # Convert to PyTorch Geometric Graph
    g_t.x = torch.tensor([G.nodes[n]['x'] for n in G.nodes()], dtype=torch.float)
    graphs_over_time.append(g_t)

    # Step forward (except after final)
    if t < steps:
        states = step(states)

# Code Testing
print(G.nodes[0])
print(g_t)
print(g_t.x[0])


# GNN - Graph Neural Network ===============================================================================


# Prepare Training / Testing
state_map = {'S': 0, 'I1': 1, 'I2': 2, 'R': 3}
data = graphs_over_time[-1]
data.y = torch.tensor([state_map[true_states_over_time[-1][n]] for n in G.nodes()], dtype=torch.long) # label which is our main state

train_graphs = graphs_over_time[:25]
test_graphs = graphs_over_time[25:35]

print(data.x)


# # Define EvolveGCN Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class EvolveGCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, device):
        super(EvolveGCN, self).__init__()
        self.hidden_channels = hidden_channels
        self.device = device
        self.conv = GCNConv(in_channels, hidden_channels)
        self.rnn = GRU(hidden_channels, hidden_channels)
        self.fc = torch.nn.Linear(hidden_channels, out_channels)

    def forward(self, graph_sequence):
        h = torch.zeros(1, graph_sequence[0].num_nodes, self.hidden_channels).to(self.device) # defining hidden states for GRU (RNN)
        for data in graph_sequence:
            x, edge_index = data.x.to(self.device), data.edge_index.to(self.device)
            x = F.relu(self.conv(x, edge_index))   #(100,2)X(2,948) => (100,948)X(948,64) => (100,64) It'sJust Assumption thats not true->what actuall happens is (100,2)X(2,64)->(100,64)-MessageParsing(sharing information between nodes)->(100,64)->Relu()->(100,64)
            x = F.dropout(x, p=0.3, training=self.training)
            h, _ = self.rnn(x.unsqueeze(0), h)
        out = self.fc(h.squeeze(0))
        return F.log_softmax(out, dim=1)

# Train Model
model = EvolveGCN(in_channels=2, hidden_channels=64, out_channels=4, device=device).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(250):
    model.train() # training starts 
    optimizer.zero_grad()
    out = model(train_graphs)
    loss = F.nll_loss(out, data.y.to(device))
    loss.backward() 
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1:03d} | Loss: {loss.item():.4f}")


# Test Model on Future (Unseen) Graphs
model.eval()
with torch.no_grad():
    out_test = model(test_graphs)
    pred = out_test.argmax(dim=1).cpu()

print(pred)


true = data.y.cpu()
accuracy = (pred == true).sum().item() / len(true)
print(f"\nTest Accuracy (Final step prediction): {accuracy:.2f}")


for i, n in enumerate(G.nodes()):
    print(i,n)



# # ==========================================================================================================================

# Visualization — True vs Predicted

# Build predicted state maps for selected timesteps (for fair comparison)
# Here we reuse final prediction for illustration purposes
pred_state_map = {0: 'S', 1: 'I1', 2: 'I2', 3: 'R'}
pred_states_over_time = []
for t in range(steps + 1):
    pred_states_over_time.append({n: pred_state_map[int(pred[i])] for i, n in enumerate(G.nodes())})

# Visualize true vs predicted
visualize_diffusion_snapshots(G, true_states_over_time, pred_states_over_time, steps=steps)


# # Visualization — Final Predicted Snapshot

# Create color mapping
color_map = {
    'S': 'gray',     # Susceptible
    'I1': 'green',   # Positive influence
    'I2': 'red',     # Negative influence
    'R': 'blue'      # Recovered
}

# Build true and predicted state maps for the final step
true_final = true_states_over_time[-1]
pred_final = {n: pred_state_map[int(pred[i])] for i, n in enumerate(G.nodes())}

# Plot side-by-side comparison
plt.figure(figsize=(10, 5))

# True Final State 
plt.subplot(1, 2, 1)
node_colors_true = [color_map[true_final[n]] for n in G.nodes()]
nx.draw(G, pos=nx.spring_layout(G, seed=42), node_color=node_colors_true, with_labels=False, node_size=80)
plt.title("True Final State ($t=35$)")

# Predicted Final State
plt.subplot(1, 2, 2)
node_colors_pred = [color_map[pred_final[n]] for n in G.nodes()]
nx.draw(G, pos=nx.spring_layout(G, seed=42), node_color=node_colors_pred, with_labels=False, node_size=80)
plt.title("Predicted Final State ($t=35$)")

# Add legend
from matplotlib.patches import Patch

# Legend
legend_handles = [
        mpatches.Patch(color='gray', label='S (Susceptible)'),
        mpatches.Patch(color='green', label='I1 (Positive)'),
        mpatches.Patch(color='red', label='I2 (Negative)'),
        mpatches.Patch(color='blue', label='R (Recovered)')
    ]
plt.legend(handles=legend_handles, loc='lower center', ncol=5, fontsize=20, frameon=False)
    # fig.suptitle("True vs Predicted Diffusion Snapshots", fontsize=22, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# legend_elements = [
#     Patch(facecolor='gray', label='S (Susceptible)'),
#     Patch(facecolor='green', label='I1 (Positive)'),
#     Patch(facecolor='red', label='I2 (Negative)'),
#     Patch(facecolor='blue', label='R (Recovered)')
# ]
# plt.legend(handles=legend_elements, loc='lower center', ncol=4)
# plt.tight_layout()

# Save the figure
# plt.savefig("predicted_final_snapshot.png", dpi=300, bbox_inches='tight')
# plt.show()
