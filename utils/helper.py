from Product.Product import Product
from Product.Products import Products

from PricingRule.Deals.BulkDiscountDeal import BulkDiscountDeal
from PricingRule.Deals.FreeProductDeal import FreeProductDeal
from PricingRule.Deals.ForthePriceofDeal import ForthePriceofDeal

from PricingRule.PricingRule import PricingRule


def add_products(products):

    super_ipad = Product('ipd', 'Super iPad', 549.99)

    vga_adapter = Product('vga', 'VGA adapter', 30.00)

    macBook_pro = Product('mbp', 'MacBook Pro', 1399.99)

    apple_tv = Product('atv', 'Apple TV', 109.50)

    products.add_product(super_ipad)
    products.add_product(vga_adapter)
    products.add_product(macBook_pro)
    products.add_product(apple_tv)


def add_pricing_rules(products, pricing_rules):
    super_ipad = products.get_product_with_sku('ipd')
    super_ipad_bulk_discount_deal = BulkDiscountDeal(super_ipad, 5, 499.99)

    macBook_pro = products.get_product_with_sku('mbp')
    vga_adapter = products.get_product_with_sku('vga')
    macBook_pro_free_product_deal = FreeProductDeal(
        macBook_pro, [{'Product': vga_adapter, 'Quantity': 1}])

    apple_tv = products.get_product_with_sku('atv')
    apple_tv_for_the_price_of_deal = ForthePriceofDeal(apple_tv, 3, 2)

    vga = products.get_product_with_sku('vga')
    vga_pricing_rule = PricingRule(vga)

    pricing_rules.add_pricing_rule(super_ipad_bulk_discount_deal)
    pricing_rules.add_pricing_rule(macBook_pro_free_product_deal)
    pricing_rules.add_pricing_rule(apple_tv_for_the_price_of_deal)
    pricing_rules.add_pricing_rule(vga_pricing_rule)
