import logging
import playwright
from models.parseResult import ParseResult
import re

async def parse_nike(context):
    page = await context.new_page()

    await page.goto("https://www.nike.com/w/2083cz3yaep")
    await page.screenshot(path="prewiev.png", full_page=True)
    
    await page.wait_for_selector("div.product-card__body")

    cards = await page.query_selector_all("div.product-card__body")

    results = []


    for card in cards[:5]:
        prices = []
        skus = []
        
        figure = await card.query_selector("figure")
        info = await figure.query_selector("div.product-card__info")

        await card.hover()
        try:
            await card.wait_for_selector("div.product-card__colorways-thumbs", timeout=1000)
            options = await card.query_selector_all("div.product-card__colorways-thumbs > a.colorway")

            for option in options[:4]:
                await option.evaluate("""
                        el => {
                            el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
                        }
                    """)
                price_el = await info.query_selector("div.product-price.is--current-price")

                url_overlay = await figure.query_selector("a.product-card__link-overlay")
                url_sku = await url_overlay.get_attribute("href")
                sku = url_sku.rsplit("/", 1)[-1]
                skus.append(sku)


                price = await price_el.inner_text() if price_el else "—"
                match = re.search(r'\d+(?:\.\d+)?', price)
                if match:
                    number = float(match.group())
                    number = int(number) if number.is_integer() else number
                    prices.append(number)

        except playwright.async_api.TimeoutError:
            logging.info("No additional color options available")

        
        title_el = await info.query_selector("div.product-card__title")
        title = await title_el.inner_text() if title_el else "—"

        promo_el = await info.query_selector("div.promo__message > p")
        promo = await promo_el.inner_html() if promo_el else "—"

        link_el = await card.query_selector("a.product-card__link-overlay")
        link = await link_el.get_attribute("href")

        final_price = ""
        if prices:
            min_price = min(prices)
            max_price = max(prices)
            if min_price == max_price:
                final_price = f"${min_price}"
            else:
                final_price = f"${min_price} – ${max_price}"
        
        results.append(
            ParseResult(
                shop_name="Nike",
                product_name=title,
                discount=promo.strip(),
                price=final_price,
                url=link,
                sku=skus
                ))

    await page.close()
    return results