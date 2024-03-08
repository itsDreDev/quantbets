# tests/test_probability.py
import pytest
from decimal import Decimal
from quantbets.probability import calculate_ev_percentage

def test_calculate_ev_percentage():
    assert calculate_ev_percentage(2.0, 0.5) == Decimal('0.0'), "EV should be 0 for break-even odds and probability"
    assert calculate_ev_percentage(2.5, 0.5) > Decimal('0.0'), "Positive EV expected for these odds and probability"
    with pytest.raises(ValueError):
        calculate_ev_percentage(-1, 0.5)
    with pytest.raises(ValueError):
        calculate_ev_percentage(2.5, -0.5)
    with pytest.raises(ValueError):
        calculate_ev_percentage(2.5, 1.5) 

def test_calculate_ev_percentage_negative_ev():
    """Test that a negative EV is correctly calculated when the probability of winning is low relative to the odds."""
    assert calculate_ev_percentage(2.5, 0.2) < Decimal('0.0'), "Negative EV expected for these odds and low probability"

def test_calculate_ev_percentage_high_probability():
    """Test that a higher positive EV is returned for high probabilities of winning."""
    assert calculate_ev_percentage(1.8, 0.7) > Decimal('0.0'), "Positive EV expected for high probability and lower odds"

def test_calculate_ev_percentage_probability_zero():
    # Expecting the maximum possible negative EV, essentially losing the bet
    assert calculate_ev_percentage(2.0, 0) == Decimal('-1'), "EV should be -1 for a probability of 0"

def test_calculate_ev_percentage_probability_one():
    # Expecting EV based on the odds, as the win is assumed
    # This test assumes the bettor always wins, so the payout is (odds - 1)
    assert calculate_ev_percentage(10, 1) == Decimal('9'), "EV should reflect the odds for a probability of 1"

def test_calculate_ev_percentage_invalid_odds():
    """Test handling of invalid odds values."""
    with pytest.raises(ValueError):
        calculate_ev_percentage(0, 0.5)
    with pytest.raises(ValueError):
        calculate_ev_percentage('invalid', 0.5)

def test_calculate_ev_percentage_invalid_probability():
    """Test handling of invalid probability values."""
    with pytest.raises(ValueError):
        calculate_ev_percentage(2.5, 'invalid')
    with pytest.raises(ValueError):
        calculate_ev_percentage(2.5, 2)  # Probability greater than 1
    with pytest.raises(ValueError):
        calculate_ev_percentage(2.5, -0.1)  # Negative probability

def test_calculate_ev_percentage_boundary_conditions():
    """Test boundary conditions for probability close to 0 and 1."""
    assert calculate_ev_percentage(3.0, Decimal('0.01')) < Decimal('0.0'), "Very low probability should result in negative EV"
    assert calculate_ev_percentage(3.0, Decimal('0.99')) > Decimal('0.0'), "Very high probability should result in positive EV"


def test_valid_inputs():
    odds = Decimal('2')
    probability = Decimal('0.55')
    expected_ev_percentage = Decimal('0.1')
    assert calculate_ev_percentage(odds, probability) == expected_ev_percentage

def test_invalid_odds_type():
    with pytest.raises(ValueError):
        calculate_ev_percentage("not a number", Decimal('0.4'))

def test_invalid_probability_type():
    with pytest.raises(ValueError):
        calculate_ev_percentage(Decimal('2.5'), "not a number")

def test_probability_out_of_range_low():
    with pytest.raises(ValueError):
        calculate_ev_percentage(Decimal('2.5'), Decimal('-0.1'))

def test_probability_out_of_range_high():
    with pytest.raises(ValueError):
        calculate_ev_percentage(Decimal('2.5'), Decimal('1.1'))

def test_odds_less_than_one():
    with pytest.raises(ValueError):
        calculate_ev_percentage(Decimal('0.5'), Decimal('0.4'))

def test_zero_probability():
    odds = Decimal('2.5')
    probability = Decimal('0')
    expected_ev_percentage = Decimal('-1')
    assert calculate_ev_percentage(odds, probability) == expected_ev_percentage

def test_one_probability():
    odds = Decimal('2.5')
    probability = Decimal('1')
    expected_ev_percentage = Decimal('1.5')
    assert calculate_ev_percentage(odds, probability) == expected_ev_percentage