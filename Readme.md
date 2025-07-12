# 🎬 F1 Movie Trailer Sentiment Analysis with Python

This project analyzes YouTube comments on the official **F1 Movie Trailer** using Natural Language Processing (NLP) in Python. The goal was to understand how the audience reacted — positively, negatively, or neutrally — and identify trending themes in the conversation.

> 🔍 A real-world use case of sentiment analysis on user-generated content (UGC).

---

## 📌 Project Summary

- 📥 Collected 300+ top comments from YouTube using `youtube-comment-downloader`
- 🧹 Cleaned and preprocessed text using regular expressions
- 💬 Performed sentiment analysis with `TextBlob`
- 📊 Visualized results using pie charts and word clouds
- 🧠 Interpreted viewer sentiment and top keywords

---

## 🛠️ How I Built This Project (Step-by-Step)

1. **Selected the Source:**
   - Chose the official F1 movie trailer on YouTube as the data source.
   - link used: `https://www.youtube.com/watch?v=69ffwl-8pCU`

2. **Extracted Comments:**
   - Used the Python package `youtube-comment-downloader` to fetch the **top public comments** from the video.
   - Iterated through each comment and stored them in a list.

3. **Created a DataFrame:**
   - Used `pandas` to structure the raw comments into a DataFrame.
   - Cleaned the comments (removed URLs, special characters, converted to lowercase).

4. **Analyzed Sentiment:**
   - Applied `TextBlob` sentiment analysis to classify each comment as **Positive**, **Negative**, or **Neutral**.
   - Added the sentiment result as a new column.

5. **Generated CSV File:**
   - Exported the final DataFrame into a file named `f1_movie_comments.csv`.
   - This file contains all raw, cleaned, and labeled comment data.

6. **Created Visual Insights:**
   - Used `matplotlib` to generate a **sentiment pie chart**.
   - Created a **word cloud** using the `WordCloud` library to visualize common words.

---

## 📈 Key Findings

### 🟢 Sentiment Distribution
Over **90%** of viewers expressed **neutral or positive** sentiment:
- **Neutral**: 52.2%
- **Positive**: 38.2%
- **Negative**: 9.7%

This shows that the F1 movie trailer was received favorably by the audience, with limited negative reactions.

### ☁️ Word Cloud Insights
Top recurring words include:
- 🎥 `movie`, `trailer`, `watch`, `scene`, `look`
- 🏎️ `f1`, `driver`, `race`, `racing`, `hamilton`, `alonso`
- 👤 `brad`, `pitt`, `love`, `real`, `great`, `hope`, `amazing`

This indicates a strong association with F1 culture, well-known drivers, and high expectations for realism and performance.

---


