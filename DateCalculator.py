class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.month = month
        self.day = day

        # Adjust for January and February
        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year = year - 1
        else:
            self.year = year

        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_day(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        # Zeller’s formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        # Mapping of Zeller’s output to days
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


# Example usage
date = DateCalculator(1589, 9, 15)
print(f"September 15, 1589 was a {date.calculate_day()}")
