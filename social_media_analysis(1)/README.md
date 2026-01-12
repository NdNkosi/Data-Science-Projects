# Kenya June 2025 Protests: Visibility, Emotional Rhythms, and Platform Dynamics

## 📌 Project Overview
This project analyses the online discourse surrounding the **June 2025 Kenyan protests** using a comprehensive Twitter (X) dataset. The analysis focuses on:

1. **Influential actors** driving visibility in the dataset  
2. **Temporal dynamics** of protest conversation and emotional rhythms

Visualisations, outputs, and full Python scripts are included to support the analyses.

---

## 📊 Dataset
- **Source:** Kenya June 2025 Protests Twitter (X) dataset  
- **Content:** Tweets related to protest mobilisation, political commentary, and public reaction  
- **Key Variables Used:**  
  - Tweet text  
  - Timestamp  
  - Retweets, mentions, and replies  
  - Author metadata (followers, engagement metrics)  
  - Sentiment scores

---

## 🛠️ Tools & Libraries
- **Python**  
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
- `networkx` for network visualisation and centrality calculations  
- `scikit-learn` for basic clustering and analytics  
- `nltk` and text processing utilities  

All scripts and outputs are included in the repository.

---

## 🔹Influential Actors & Visibility

### Method
- **Definition of Influence:** Influence was measured using **in-degree centrality** in the mention network, combined with **retweet count** as a proxy for engagement. This metric reflects both the direct attention an actor receives and the amplification of their messages.  
- **Network Visualisation:** A mention network was created using `networkx`, highlighting the **top 10 influential actors** based on the combined metric. Node size corresponds to influence, and edge weight reflects mentions or retweets.

### Key Insights
- Visibility is heavily concentrated among a small set of actors, often urban-based or politically connected.  
- Platform affordances such as retweets and mentions amplify certain voices while silencing others, particularly rural or less digitally connected participants.  
- Structural constraints, such as network centrality and follower count, determine which narratives gain traction.  
- Limitations: Twitter/X data cannot capture offline mobilisation or sentiment in languages less used on the platform.

---

## 🔹Temporal Dynamics & Emotional Rhythms

### Method
- Tweets were aggregated **daily** to observe **volume spikes**, **moving average of sentiment**, and **topic drift** over time.  
- Two key visualisations were produced:  
  1. **Volume of tweets and moving average sentiment over time**  
  2. **Topic distribution over time**, showing shifts in dominant narratives

### Key Insights
- Peaks in activity often coincide with major protest events, political announcements, or viral hashtags.  
- Sentiment analysis reveals alternating cycles of outrage, solidarity, and mobilisation energy.  
- Topic drift shows how the conversation evolves: initial mobilisation → critique of leadership → calls for justice → reflection on repression.  
- Insights suggest **mobilisation under constrained digital infrastructures** is uneven: spikes are amplified by highly connected actors and certain hashtags, while offline participants and vernacular voices remain underrepresented.  

---

## 📈 Visualisations
- `figures/network_top10_actors.png` — Mention network highlighting top influencers  
- `figures/sentiment_over_time.png` — Sentiment moving average across the dataset  
- `figures/topic_drift.png` — Topic evolution across the protest timeline  

---

## 🧠 Critical Reflections
- Digital methods surface **who gets heard and what frames dominate**, but cannot fully capture nuance, offline activity, or marginalized voices.  
- Network-based influence metrics highlight structural inequalities in online visibility.  
- Temporal sentiment and topic analyses reveal the **emotional rhythm** of protests and how online discourse shapes collective understanding.  

---

