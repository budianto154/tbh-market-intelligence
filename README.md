# 🛡️ TBH Market Intelligence

Market Intelligence tool for **Taskbar Heroes Steam Market**.

This project collects Steam Market data, stores historical snapshots into SQLite, and provides market analysis such as demand trends, price history, and profit opportunities.

> 🚧 Project Status: Under Development

---

# Features

Current implemented features:

- ✅ Steam Market Scraper (Playwright)
- ✅ HTML Parser (BeautifulSoup4)
- ✅ DTO Pattern
- ✅ Repository Pattern
- ✅ SQLite Database
- ✅ SQLAlchemy ORM
- ✅ Item Repository
- ✅ Market Snapshot Repository
- ✅ Market Service
- 🚧 Historical Snapshot
- 🚧 Dashboard
- 🚧 Market Intelligence

---

# Tech Stack

|   Technology   |   Description   |
|----------------|-----------------|
| Python         | Main Programming Language |
| Playwright     | Steam Market Scraper |
| BeautifulSoup4 | HTML Parsing |
| SQLAlchemy     | ORM |
| SQLite         | Local Database |
| Git            | Version Control |

---

# Roadmap

## Episode 1 - Project Foundation ✅

- [x] Setup Python
- [x] Virtual Environment
- [x] SQLite
- [x] SQLAlchemy
- [x] Repository Pattern
- [x] Logger
- [x] Playwright
- [x] Steam Market berhasil dibuka

---

## Episode 2 - Data Collection 🚧

### Scraper

- [x] Analisis Network Request
- [x] Ambil HTML Steam Market
- [x] Robust Selector Strategy

### Parser

- [x] Parse HTML
- [x] DTO (ItemDTO)
- [x] Ambil daftar item Steam Market

### Database

- [x] ItemRepository
- [x] MarketSnapshotRepository
- [x] MarketService
- [x] save_item()

### Workflow

- [x] Scraper → Parser
- [ ] Parser → ItemRepository
- [ ] ItemRepository → SnapshotRepository
- [ ] sync_market() selesai

---

## Episode 3 - Historical Market Data

- [ ] Snapshot Market
- [ ] Snapshot Scheduler
- [ ] Price History
- [ ] Volume History
- [ ] Historical Query

---

## Episode 4 - Market Intelligence

- [ ] Top Demand
- [ ] Price Trend
- [ ] Profit Analysis
- [ ] Arbitrage Opportunity
- [ ] Rarity Analysis

---

## Episode 5 - Dashboard

- [ ] Dashboard Backend
- [ ] REST API
- [ ] Charts
- [ ] Search Item
- [ ] Filter Category
- [ ] Historical Graph

---

## Episode 6 - Automation

- [ ] Scheduled Scraping
- [ ] Daily Snapshot
- [ ] Error Recovery
- [ ] Logging Improvement
- [ ] Export CSV

---

## Episode 7 - AI Market Analyst

- [ ] Demand Prediction
- [ ] Price Prediction
- [ ] Recommendation Engine
- [ ] AI Market Summary

---

# Running Project

Clone repository

```bash
git clone https://github.com/budianto154/tbh-market-intelligence.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create database

```bash
python app.py
```

Run project

```bash
python -m tests.test_market_service
```

---
