class Checkout:

    def __init__(self, pricing_rules):
        """
            constructor for Checkout

            @param pricing_rules: pricing rules for all items
            @type: PricingRules
        """
        self.skus = []
        self.pricing_rules = pricing_rules

    def scan(self, item_sku):
        """
            Scanning items at checkout

            @param item_sku: SKU of item added to checkout
            @type: String
        """
        self.skus.append(item_sku)

    def total(self):
        """
            Getting total cost of Checkout products. Free Products are not added to the cost

            @variable sku_quantity: gets the number of products added for each SKU
            @type dictionary

            @variable free_products: gets the free products the customer get based on the pricing rules
            @type dictionary

            @return total price
        """
        total = 0
        skus_quantity = self.get_skus_quantity()
        free_products = self.free_products()

        for sku in skus_quantity:
            quantity = max(skus_quantity[sku] -
                           free_products.get(sku, 0), 0)
            price = self.price_for_sku(sku, quantity)
            total += price
        return total

    def get_skus_quantity(self):
        """
            Gets the number of products added for each SKU

            @variable sku_quantity: gets the number of products added for each SKU
            @type dictionary

            @return SKU Quantity
        """
        sku_quantity = {}
        for sku in self.skus:
            sku_quantity[sku] = sku_quantity.get(sku, 0) + 1

        return sku_quantity

    def price_for_sku(self, sku, sku_quanity):
        """
            Gets the total cost of the given SKU based on the quantity and pricing rules

            @param sku: SKU name
            @type: String

            @param sku_quanity: Number of products in the checkout cart for this sku
            @type: Integer

            @variable pricing_rule: gets the pricing rule for each SKU
            @type PricingRule

            @return total cost for sku
        """
        pricing_rule = self.pricing_rules.get_pricing_rule_by_sku(sku)
        return pricing_rule.total_cost(sku_quanity)

    def free_products(self):
        """
            Gets the number of free products provided to the customer based on the pricing rules

            @variable free_products: a dictionary containing the quantity of free products for each SKU
            @type dictionary

            @return free products dictionary
        """

        free_products = {}
        for sku in self.skus:
            pricing_rule = self.pricing_rules.get_pricing_rule_by_sku(sku)
            pricing_rule_free_products = pricing_rule.get_free_products()

            if pricing_rule_free_products:
                for product in pricing_rule_free_products:
                    free_products[product['Product'].sku] = free_products.get(
                        product['Product'].sku, 0) + product['Quantity']

        return free_products
