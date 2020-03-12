from Product.Products import Products
from utils.helper import add_products
from utils.helper import add_pricing_rules
from PricingRule.PricingRules import PricingRules
from Checkout.Checkout import Checkout

products = Products()
pricing_rules = PricingRules()

add_products(products)
add_pricing_rules(products, pricing_rules)

co = Checkout(pricing_rules)

SKUsScanned = str(input("SKUs Scanned: "))
skus = SKUsScanned.split(',')

for sku in skus:
    sku = sku.strip()
    co.scan(sku)

print("Total expected: $", co.total())
