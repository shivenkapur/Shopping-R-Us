from PricingRule.PricingRule import PricingRule


class BulkDiscountDeal(PricingRule):

    def __init__(self, product, quantity_to_purchase, changed_price):
        """
        constructor for BulkDiscountDeal that inherits from PricingRule

        @param product: Product for which Deal is being created
        @type Product

        @param quantity_to_purchase: Quantity of Products to purchase for the Deal to be used
        @type Integer

        @param changed_price: New price to be applied for bulk buys
        @type Float

        """
        self.product = product
        self.quantity_to_purchase = quantity_to_purchase
        self.changed_price = changed_price

    def total_cost(self, quantity_of_products_purchased):
        """
        Calculates total cost of products based on pricing rule of bulk deal and number of products purchased

        @param quantity_of_products_purchased: Quantity of Products purchased
        @type Integer

        """
        if quantity_of_products_purchased >= self.quantity_to_purchase:
            return self.changed_price * quantity_of_products_purchased
        else:
            return self.product.price * quantity_of_products_purchased
