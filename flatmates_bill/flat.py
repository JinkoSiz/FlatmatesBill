class Bill:
    """
    Obj that contains data about the bill (total amount, period)
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate, person who lives in the flat and pays bills
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bills, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bills.amount * weight


