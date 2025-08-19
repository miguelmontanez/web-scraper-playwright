from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ParseResult:
    shop_name: str
    product_name: str
    discount: Optional[str] = None
    price: Optional[str] = None
    url: Optional[str] = None
    sku: Optional[List[str]] = None

    def __str__(self):
        return (
            f"Shop: {self.shop_name}\n"
            f"Product: {self.product_name}\n"
            f"Discount: {self.discount or '—'}\n"
            f"Price: {self.price or '—'}\n"
            f"URL: {self.url or '—'}\n"
            f"SKU(s): {', '.join(self.sku) if self.sku else '—'}\n"
        )