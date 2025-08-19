import asyncio
import logging
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from parsers.nike import parse_nike

logging.basicConfig(
        level=logging.INFO,
        filename='scraper.log',
        filemode='w',  # 'w' - overwrite, 'a' - add
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

async def schedule():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            locale="ru-RU",
            viewport={"width": 1280, "height": 800},
            extra_http_headers = {
                "Accept-language":"ru-RU,ru;q=0.9",
                "Referer":"https://www.google.com/",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Upgrade-Insecure-Requests":"1",
                "DNT":"1",
                "Connection":"keep-alive"
            }
        )
        stealth = Stealth()
        await stealth.apply_stealth_async(context)

        try:
            results = await parse_nike(context)
            logging.info(f"Nike scraping finished, found {len(results)} products: \n")
            for result in results:
                logging.info(result)
        except Exception as e:
            logging.error(f"Error during Nike scraping: {e}")
        finally:
            logging.info("Scraping finished")
            await context.close()
            await browser.close()

    

async def main():
    try:
        logging.info("Scraping started")
        await schedule()
        logging.info("All scrapers finished")
    except Exception as e:
        logging.error(f"Error: {e}")

    return



if __name__ == "__main__":
    asyncio.run(main())