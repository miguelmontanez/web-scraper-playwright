# 🛍️ Nike Product Scraper (Playwright + Python)

This is a minimalist demonstration project that scrapes product information from a Nike catalog page using **Playwright** and Python. The script emulates user actions (like hovering over color options) and extracts key data such as the product name, price range, description, and SKU identifiers.

---

## 🚀 Project Goal

This project was created as part of a Junior Developer portfolio. It showcases the following skills:

- Headless browser automation with Playwright
- Asynchronous programming in Python
- Scraping dynamic, JavaScript-driven websites
- DOM traversal and data extraction
- Clean data structuring with `@dataclass`

---

## 🔍 What the Script Does

- Opens a Nike category page
- Locates product cards
- Hovers over available color variations (up to 5 options)
- Extracts:
  - Product name
  - Price or price range
  - Promotion label (if available)
  - Product URL
  - List of SKUs (variant identifiers)

### 📦 Example Output
Shop: Nike <br>
Product: Nike Free Run 5.0 <br>
Discount: New Markdown <br>
Price: $65.97 – $87.97 <br>
URL: `https://www.nike.com/...` <br>
SKU(s): CZ1884-001, CZ1884-103 <br>

## 🧰 Technologies Used

- Python 3.10+
- [Playwright (Python)](https://playwright.dev/python/)
- [playwright-stealth](https://github.com/AtuboDad/playwright-stealth)
- Async/Await
- Python `dataclasses`



## ⚙️ Installation & Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```
2. Run the scraper:
    `python main.py`
    The script will run once and print the results to the console.

⚠️ Disclaimer
    This project is for educational and demonstration purposes only. 
    All trademarks and content belong to Nike.