from PricingRule.PricingRule import PricingRule


class ForthePriceofDeal(PricingRule):
    def __init__(self, product, quantity_to_purchase, quantity_charged):
        """
        constructor for ForthePriceofDeal that inherits from PricingRule

        @param product: Product for which Deal is being created
        @type Product

        @param quantity_to_purchase: Quantity of Products to purchase for the Deal to be used
        @type Integer

        @param quantity_charged: Quantity of products to be charged for
        @type Integer

        """
        self.product = product
        self.quantity_to_purchase = quantity_to_purchase
        self.quantity_charged = quantity_charged

    def total_cost(self, quantity_of_products_purchased):
        """
        Calculates total cost of products based on pricing rule of deal and number of products purchased

        @param quantity_of_products_purchased: Quantity of Products purchased
        @type Integer
        """
        products_eligible_for_deal = int(
            quantity_of_products_purchased/self.quantity_to_purchase) * self.quantity_charged
        remaining_products = quantity_of_products_purchased % self.quantity_to_purchase
        return (products_eligible_for_deal + remaining_products) * self.product.price
