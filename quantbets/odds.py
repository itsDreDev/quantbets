from decimal import Decimal, InvalidOperation
from .probability import calculate_ev_percentage

class Odds:
    def __init__(self, odds, odds_type='decimal'):
        """
        Initialize the Odds object with odds and their type. Converts odds to Decimal for precision.

        :param odds: The odds value, can be a numeric value for decimal and American odds, or a tuple for fractional odds.
        :param odds_type: The type of the odds ('decimal', 'fractional', 'american').
        """
        if odds_type.lower() not in ['decimal', 'fractional', 'american']:
            raise ValueError("Unsupported odds type. Use 'decimal', 'fractional', or 'american'.")

        try:
            # Convert input odds to Decimal for precision, handling tuples for fractional odds
            if isinstance(odds, str) or isinstance(odds, (int, float)):
                odds = Decimal(odds)
                if odds == Decimal('0'):
                    raise ValueError("Odds must be a positive value.")
            elif isinstance(odds, tuple):
                odds = (Decimal(odds[0]), Decimal(odds[1]))
                if odds[0] <= Decimal('0') or odds[1] <= Decimal('0'):
                    raise ValueError("Fractional odds must be positive values.")
            else:
                raise ValueError("Odds must be a numeric value or a tuple of numeric values for fractional odds.")
        except (InvalidOperation, TypeError):
            raise ValueError("Invalid odds format or type.")

        self.odds = odds
        self.odds_type = odds_type.lower()
        self.decimal_odds = self.to_decimal()  # Convert odds to decimal format for internal calculations
        
        if self.decimal_odds <= Decimal('1'):
            if self.odds_type == 'american':
                if self.odds == 0:
                    raise ValueError("American odds cannot be zero.")
            else:
                raise ValueError("Odds must be greater than 1.")

    def to_decimal(self):
        """
        Converts odds to decimal format based on the original odds type.

        :return: Odds in decimal format as a Decimal object.
        """
        if self.odds_type == 'decimal':
            return self.odds
        elif self.odds_type == 'fractional':
            numerator, denominator = self.odds
            return numerator / denominator + Decimal('1')
        elif self.odds_type == 'american':
            if self.odds > 0:
                return self.odds / Decimal('100') + Decimal('1')
            else:
                return Decimal('-100') / self.odds + Decimal('1')
        else:
            raise ValueError("Unsupported odds type. Use 'decimal', 'fractional', or 'american'.")

    def to_fractional(self):
        """
        Converts the internal decimal odds back to fractional format.

        :return: Odds in fractional format as a tuple of Decimals.
        """
        if self.odds_type == 'fractional':
            return self.odds
        fractional = (self.decimal_odds - Decimal('1')).as_integer_ratio()
        return (Decimal(fractional[0]), Decimal(fractional[1]))

    def to_american(self):
        """
        Converts the internal decimal odds to American format.

        :return: Odds in American format as a Decimal.
        """
        if self.odds_type == 'american':
            return self.odds
        if self.decimal_odds >= Decimal('2'):
            return (self.decimal_odds - Decimal('1')) * Decimal('100')
        else:
            return Decimal('-100') / (self.decimal_odds - Decimal('1'))

    def odds_to_probability(self):
        """
        Calculates the implied probability from the internal decimal odds.

        :return: Implied probability as a Decimal.
        """
        return Decimal('1') / self.decimal_odds

    def calculate_ev(self, estimated_probability):
        """
        Calculates the expected value (EV) of a bet based on the internal decimal odds and an estimated probability.

        :param estimated_probability: Your estimated probability of the outcome, as a numeric value or string that can be converted to Decimal.
        :return: The expected value of the bet as a Decimal.
        """
        return calculate_ev_percentage(self.decimal_odds, estimated_probability)

    def __str__(self):
        """
        Provides a string representation of the Odds object, displaying the odds in all formats and the implied probability.

        :return: String representation of the object.
        """
        try:
            f1, f2 = self.to_fractional()
            fractional_str = f"{f1}/{f2}"
            american_odds = self.to_american()
            american_str = f"+{american_odds}" if american_odds >= 0 else str(american_odds)

            return (f"Decimal: {self.decimal_odds}, Fractional: {fractional_str}, "
                    f"American: {american_str}, Probability: {self.odds_to_probability()}")
        except Exception as e:
            return f"Error converting odds formats: {e}"