# tests/test_odds.py
import pytest
from decimal import Decimal
from quantbets.odds import Odds

def test_decimal_to_fractional_conversion():
    odds = Odds(2.5)  # Example for a constructor that takes decimal odds by default
    assert odds.to_fractional() == (3, 2), "Decimal odds of 2.5 should convert to fractional odds of 3/2"

def test_fractional_to_decimal_conversion():
    odds = Odds((3, 2), odds_type='fractional')
    assert odds.to_decimal() == Decimal('2.5'), "Fractional odds of 3/2 should convert to decimal odds of 2.5"

def test_american_to_decimal_conversion_positive():
    odds = Odds(150, odds_type='american')
    assert odds.to_decimal() == Decimal('2.5'), "American odds of +150 should convert to decimal odds of 2.5"

def test_american_to_decimal_conversion_negative():
    odds = Odds(-200, odds_type='american')
    assert odds.to_decimal() == Decimal('1.5'), "American odds of -200 should convert to decimal odds of 1.5"

def test_probability_calculation():
    odds = Odds(2.0)
    assert odds.odds_to_probability() == Decimal('0.5'), "Decimal odds of 2.0 should result in a probability of 0.5"

def test_ev_calculation():
    odds = Odds(2.5)
    # Assuming your Odds class has an integrated method to use the standalone calculate_ev_percentage function
    ev_percentage = odds.calculate_ev(0.55)  # Example probability
    assert ev_percentage > Decimal('0.0'), "Expected a positive EV percentage for these odds and probability"

def test_error_handling_invalid_odds():
    with pytest.raises(ValueError):
        Odds('invalid', odds_type='decimal')

def test_error_handling_invalid_odds_type():
    with pytest.raises(ValueError):
        Odds(2.5, odds_type='unsupported_type')


def test_odds_conversion_accuracy():
    """
    Test the accuracy of converting between odds formats.
    """
    # Using an example where decimal odds are 3.0 (2/1 fractional, +200 American)
    odds = Odds(3.0)
    assert odds.to_fractional() == (2, 1), "Decimal odds of 3.0 should convert to fractional odds of 2/1"
    assert odds.to_american() == 200, "Decimal odds of 3.0 should convert to American odds of +200"

def test_invalid_fractional_odds_conversion():
    """
    Test error handling for invalid fractional odds input.
    """
    with pytest.raises(ValueError):
        Odds((0, 2), odds_type='fractional')

def test_negative_decimal_odds():
    """
    Ensure negative decimal odds raise an error.
    """
    with pytest.raises(ValueError):
        Odds(-2.5)

def test_zero_or_negative_fractional_odds():
    """
    Test that zero or negative values in fractional odds raise an error.
    """
    with pytest.raises(ValueError):
        Odds((0, 1), odds_type='fractional')
    with pytest.raises(ValueError):
        Odds((-1, 2), odds_type='fractional')

def test_invalid_american_odds_conversion():
    """
    Test error handling for invalid American odds input.
    """
    # American odds of 0 should raise an error since it doesn't represent a betting scenario
    with pytest.raises(ValueError):
        Odds(0, odds_type='american')

def test_calculate_ev_with_invalid_probability():
    """
    Test calculate EV with probability outside [0,1] range.
    """
    odds = Odds(2.5)
    with pytest.raises(ValueError):
        odds.calculate_ev(-0.1)  # Invalid probability
    with pytest.raises(ValueError):
        odds.calculate_ev(1.1)  # Invalid probability

def test_odds_representation():
    """
    Test the string representation of odds for easy debugging.
    """
    odds = Odds(2.5)
    representation = str(odds)  # Assuming you implement a __str__ method in your Odds class
    assert "Decimal: 2.5" in representation
    assert "Fractional: (3, 2)" in representation or "Fractional: 3/2" in representation
    assert "American: +150" in representation