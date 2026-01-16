# 📚 Course Search API

A Django REST Framework project that allows users to **create, list, and search courses** using natural language queries.  
The search is powered by **SpaCy** for NLP preprocessing and **PostgreSQL** for robust data storage.

---

## 🚀 Features
- **Create Courses** via API (with name, description, tags, etc.)
- **Automatic Tokenization**: Course names are preprocessed into searchable tokens using SpaCy.
- **Cached Queries**: Tokens are stored in a `CachedQuery` table for faster lookups.
- **Search Courses**: Query courses by keywords, tags, or cached tokens.
- **List Courses**: Retrieve all courses in the database.

---

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **NLP**: SpaCy (`en_core_web_sm` model)
- **Language**: Python 3.10+

---
