class PricingRule:
    def __init__(self, product):
        """
        constructor for PricingRule which is inherited by Deals

        @param product: Product for which Deal is being created
        @type Product

        """
        self.product = product

    def total_cost(self, sku_quantity):
        """
        Calculates total cost of products based on default pricing rule 

        @param quantity_of_products_purchased: Quantity of Products purchased
        @type Integer

        """
        return sku_quantity * self.product.price

    def get_free_products(self):
        """ Returns the free products the customer gets """
        return None
