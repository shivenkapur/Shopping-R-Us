class PricingRules:

    def __init__(self):
        """
        constructor for PricingRules

        @variable pricing_rules: a list of PricingRule objects to be added to Checkout
        @type: list
        """
        self.pricing_rules = []

    def add_pricing_rule(self, pricing_rule):
        """ adds a pricing rule to the list of pricing rules """
        self.pricing_rules.append(pricing_rule)

    def get_pricing_rules(self):
        """ gets all the pricing rules added """
        return self.pricing_rules

    def get_pricing_rule_by_sku(self, sku):
        """
        gets pricing rule for a particular SKU. Restriction: Only one pricing rule per SKU for now

        @return pricing_rule: a PricingRule object
        @type: PricingRule
        """
        for pricing_rule in self.pricing_rules:
            if pricing_rule.product.sku == sku:
                return pricing_rule
