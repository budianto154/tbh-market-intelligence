# TBH Market Intelligence

Market Intelligence Tool untuk menganalisis Steam Community Market pada game **TBH: Task Bar Hero**.

## ✨ Features

- Steam Community Market Scraper
- SQLite Database
- Historical Price Tracking
- Demand & Supply Analysis
- Farming Recommendation (Planned)
- Dashboard (Planned)
- Telegram Notification (Planned)

---

# 🛠 Tech Stack

- Python 3.13+
- SQLAlchemy
- SQLite
- Playwright
- Loguru
- Pandas
- Streamlit

---

# 📁 Project Structure

```
tbh-market-intelligence/
│
├── analysis/
├── core/
├── dashboard/
├── data/
├── database/
├── logs/
├── scheduler/
├── scraper/
├── tests/
├── venv/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd tbh-market-intelligence
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright Browser

**Penting!**

Playwright membutuhkan browser khusus. Jalankan:

```bash
python -m playwright install
```

Jika langkah ini dilewati, akan muncul error seperti:

```
Executable doesn't exist...
```

---

## 5. Run Application

```bash
python app.py
```

---

# 🧪 Running Tests

Repository

```bash
python -m tests.test_repository
```

DTO

```bash
python -m tests.test_dto
```

Logger

```bash
python -m tests.test_logger
```

Steam Scraper

```bash
python -m tests.test_scraper
```

---

# 📂 Database

SQLite database akan otomatis dibuat pada:

```
data/market.db
```

---

# 🗺 Roadmap

## ✅ Episode 1 - Foundation

- [x] Project Setup
- [x] SQLite
- [x] SQLAlchemy
- [x] Repository Pattern
- [x] DTO
- [x] Logger
- [ ] Steam Scraper

## 🔜 Episode 2

- Full Steam Market Scraper
- Market Parser
- Save to Database

## 🔜 Episode 3

- Demand Score
- Supply Score
- Price History
- Top Material Ranking

## 🔜 Episode 4

- Streamlit Dashboard
- Search Item
- Price Graph
- Market Trend

## 🔜 Episode 5

- Telegram Bot
- Auto Notification
- Daily Market Report

---

# 👨‍💻 Author

Mochamad Budianto