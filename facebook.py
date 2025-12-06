import random
import math
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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

# Graph 
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


# Figures With Simulation 

def simulate_with_snapshots_and_trajectories(G, states, steps=15):
    pos = nx.spring_layout(G, seed=42)
    snapshots = {}
    counts = {"S": [], "I1": [], "I2": [], "R": []}

    snapshot_times = [0, steps//4, steps//2, 3*steps//4, steps]

    s = states.copy()
    for t in range(steps+1):
        # record counts
        for st in counts:
            counts[st].append(sum(1 for x in s.values() if x==st))
        # record snapshot
        if t in snapshot_times:
            snapshots[t] = s.copy()
        # step forward
        if t < steps:
            s = step(s)

    # Figure -Snapshots 

    fig, axes = plt.subplots(1, len(snapshot_times), figsize=(30, 8))
    color_map = {'S': 'gray', 'I1': 'green', 'I2': 'red', 'R': 'blue'}
    labels = ['(a)', '(b)', '(c)', '(d)', '(e)']

    for i, t in enumerate(snapshot_times):
        node_colors = [color_map[snapshots[t][n]] for n in G.nodes()]
        nx.draw(
            G, pos, node_color=node_colors, ax=axes[i],
            node_size=150, with_labels=True,font_color="white",font_size=9
        )

        axes[i].set_title(f"t = {t}", fontsize=25)
        axes[i].text(
            0.5, -0.1, labels[i],
            transform=axes[i].transAxes,
            ha='center', va='top',
            fontsize=25, fontweight="bold"
        )

    # Adding Legend Manually 

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

    plt.subplots_adjust(bottom=0.2)
    plt.savefig("fb_snapshots.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Figure - Trajectories 
    plt.figure(figsize=(7, 5))
    t = range(len(counts['S']))
    plt.plot(t, counts["S"], label="S (Susceptible)", color="gray", marker="o")
    plt.plot(t, counts["I1"], label="I1 (Positive)", color="green", marker="o")
    plt.plot(t, counts["I2"], label="I2 (Negative)", color="red", marker="o")
    plt.plot(t, counts["R"], label="R (Recovered)", color="blue", marker="o")
    plt.xlabel("Time step",fontsize=15)
    plt.ylabel("Number of nodes",fontsize=15)
    # plt.title("Diffusion Trajectories",fontsize=16)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("fb_dynamics.png", dpi=300, bbox_inches="tight")
    plt.show()

    return counts

#  Run 
counts = simulate_with_snapshots_and_trajectories(G, states, steps=15)


trust_scores = {n: G.nodes[n]['trust'] for n in G.nodes()}

def plot_trust_distribution(trust_scores):
    trust_values = list(trust_scores.values())

    # Figure - Histogram + KDE 
    plt.figure(figsize=(7,5))
    plt.hist(trust_values, bins=10, color="skyblue", edgecolor="black", alpha=0.7)
    plt.axvline(sum(trust_values)/len(trust_values), color="red", linestyle="--", label="Mean trust")
    plt.xlabel("Trust Score", fontsize=15)
    plt.ylabel("Number of Users", fontsize=15)  
    # plt.title("Distribution of Trust Scores", fontsize=16)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("trust_histogram.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Figure - Boxplot 
    plt.figure(figsize=(5,5))
    plt.boxplot(trust_values, vert=True, patch_artist=True,
                boxprops=dict(facecolor="lightgreen", color="black"))
    plt.ylabel("Trust Score")
    plt.title("Boxplot of Trust Scores")
    plt.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig("trust_boxplot.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Figure - Network colored by trust 
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(5,4))
    nodes = nx.draw_networkx_nodes(
        G, pos,
        node_color=trust_values,
        cmap=plt.cm.viridis,
        node_size=200
    )
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    # plt.colorbar(nodes, label="Trust Score")
    cbar = plt.colorbar(nodes)
    cbar.set_label("Trust Score", fontsize=12)   
    cbar.ax.tick_params(labelsize=12)            # Tick label 

    plt.xlabel("Trust Score", fontsize=15)
    plt.ylabel("Number of Users", fontsize=15) 
    # plt.title("Network Colored by Trust")
    plt.legend(fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.axis("off")
    plt.savefig("network_trust_colormap.png", dpi=300, bbox_inches="tight")
    plt.show()

# Run trust plots 
plot_trust_distribution(trust_scores)


# DEGREE DISTRIBUTION (LOG–LOG)

import matplotlib.pyplot as plt
import numpy as np

# Get degrees of all nodes
degrees = np.array([d for _, d in G.degree()])

# Count occurrences of each degree
unique_degrees, counts = np.unique(degrees, return_counts=True)

# Plot
plt.figure(figsize=(8,6))

# Use a colormap based on degree value
scatter = plt.scatter(
    unique_degrees,
    counts,
    c=unique_degrees,             # color by degree
    cmap="viridis",               # beautiful colormap
    s=80,                         # bigger dots
    edgecolor="black",            # outline for clarity
    linewidth=0.7
)

plt.xscale('log')
plt.yscale('log')

plt.xlabel("Degree", fontsize=16)
plt.ylabel("Degree Distribution", fontsize=16)
# plt.title("Degree Distribution (Log–Log Scale)", fontsize=18)

# Colorbar (acts like legend)
cbar = plt.colorbar(scatter)
cbar.set_label("Node Degree", fontsize=14)
cbar.ax.tick_params(labelsize=12)

plt.grid(True, which="both", linestyle="--", linewidth=0.4)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.tight_layout()
plt.show()


