# fake-news-detection
# 📰 Fake News Detection using NLP and Machine Learning

This project is a machine learning-based system to detect fake news using Natural Language Processing (NLP) techniques. It classifies news articles as **REAL** or **FAKE** using a trained Passive Aggressive Classifier.

---

## 🚀 Features

- Fake and real news classification using NLP
- TF-IDF Vectorization for text preprocessing
- Passive Aggressive and SVM classifiers
- Streamlit web app for interactive predictions
- Easy deployment-ready model

---

## 📁 Dataset

- `Fake.csv` from [Kaggle Fake News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- A synthetic "real news" dataset is generated to balance the data (can be replaced with `True.csv` for production use)

---

## 🧠 Model

- **TF-IDF** for converting text to features
- **Passive Aggressive Classifier** for training
- Accuracy over 90% on test data

---

| File                 | Description                           |
| -------------------- | ------------------------------------- |
| `Fake.csv`           | Fake news data                        |
| `fake_news_train.py` | Python script to train and save model |
| `fake_news_app.py`   | Streamlit app for prediction          |
| `requirements.txt`   | Python dependencies                   |
| `pac_model.pkl`      | Trained model file                    |
| `tfidf.pkl`          | TF-IDF vectorizer                     |

