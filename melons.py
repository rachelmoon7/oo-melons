"""Classes for melon orders."""
class AbstractMelonOrder:

    def __init__(self, species, qty, shipped, order_type,tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5

        if self.species = "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3
            
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, shipped, "domestic", 0.08):
        super().__init__(species, qty, shipped, order_type)
    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
   
    def __init__(self, species, qty, shipped, "international", country_code, 0.17):
        super().__init__(species, qty, shipped, order_type)
        self.country_code = country_code

    def get_country_code(self, country_code):
        """Return the country code."""

        return self.country_code
