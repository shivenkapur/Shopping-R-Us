from PricingRule.PricingRule import PricingRule


class FreeProductDeal(PricingRule):
    def __init__(self, product, free_products):
        """
        constructor for FreeProductDeal that inherits from PricingRule

        @param product: Product for which Deal is being created
        @type Product

        @param free_products: Free Products to be added if certain conditions are met
        @type Product

        """
        self.product = product
        self.free_products = free_products

    def total_cost(self, quantity_of_products_purchased):
        """
        Calculates total cost of products based on pricing rule of free product deal and number of products purchased

        @param quantity_of_products_purchased: Quantity of Products purchased
        @type Integer

        """
        return quantity_of_products_purchased * self.product.price

    def get_free_products(self):
        """ Returns the free products the customer gets """
        return self.free_products
