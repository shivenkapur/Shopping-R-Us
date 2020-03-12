class Products:

    def __init__(self):
        """
        constructor for Products

        @variable products: a list of Product objects created
        @type: list
        """
        self.products = []

    def add_product(self, product):
        """ adds a Product to the list of Products """
        self.products.append(product)

    def get_products(self):
        """ gets all the Products added """
        return self.products

    def get_product_with_sku(self, sku):
        """
        gets Product for a particular SKU

        @return product: a Product object
        @type: Product
        """
        for product in self.products:
            if product.sku == sku:
                return product

        return None
