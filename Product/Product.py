class Product:
    def __init__(self, sku, name, price):
        """
        constructor for Product

        @param sku: SKU name for Product
        @type String

        @param name: Name of Product
        @type String

        @param price: Price of Product
        @type Float
        """
        self.sku = sku
        self.name = name
        self.price = price
