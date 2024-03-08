# tests/test_bankroll_management.py
import pytest
from decimal import Decimal
from quantbets.bankroll_management import kelly_criterion

def test_kelly_criterion_probability_basic():
    result = kelly_criterion(bankroll='1000', win_input='0.5', odds='2.0', multiplier='1.0', input_type='probability')
    assert result == Decimal('0'), "No bet expected for break-even odds and probability"

def test_kelly_criterion_probability_positive_ev():
    result = kelly_criterion('1000', '0.6', '2.0', '1.0', 'probability')
    assert result > Decimal('0'), "Positive bet size expected for positive EV"

def test_kelly_criterion_true_odds_basic():
    result = kelly_criterion('1000', '2.0', '2.0', '1.0', 'true_odds')
    assert result == Decimal('0'), "No bet expected for break-even true odds and given odds"

def test_kelly_criterion_true_odds_positive_ev():
    result = kelly_criterion('1000', '1.5', '2.5', '1.0', 'true_odds')
    assert result > Decimal('0'), "Positive bet size expected for positive EV"

def test_kelly_criterion_invalid_input_type():
    with pytest.raises(ValueError):
        kelly_criterion('1000', '0.55', '2.5', '1.0', 'invalid_type')

def test_kelly_criterion_invalid_bankroll():
    with pytest.raises(ValueError):
        kelly_criterion('invalid', '0.55', '2.5', '1.0', 'probability')

def test_kelly_criterion_invalid_win_input():
    with pytest.raises(ValueError):
        kelly_criterion('1000', 'invalid', '2.5', '1.0', 'probability')

def test_kelly_criterion_invalid_odds():
    with pytest.raises(ValueError):
        kelly_criterion('1000', '0.55', 'invalid', '1.0', 'probability')

def test_kelly_criterion_invalid_multiplier():
    with pytest.raises(ValueError):
        kelly_criterion('1000', '0.55', '2.5', 'invalid', 'probability')

def test_kelly_criterion_multiplier_effect():
    full_bet = kelly_criterion('1000', '0.6', '2.0', '1.0', 'probability')
    half_bet = kelly_criterion('1000', '0.6', '2.0', '0.5', 'probability')
    assert half_bet == full_bet / 2, "Half multiplier should result in half the bet size"

def test_kelly_criterion_negative_bankroll():
    with pytest.raises(ValueError, match="Bankroll must be a positive value"):
        kelly_criterion('-1000', '0.55', '2.5', '1.0', 'probability')

def test_kelly_criterion_zero_bankroll():
    with pytest.raises(ValueError, match="Bankroll must be a positive value"):
        kelly_criterion('0', '0.55', '2.5', '1.0', 'probability')

def test_kelly_criterion_negative_win_input_probability():
    with pytest.raises(ValueError, match="Probability must be between 0 and 1."):
        kelly_criterion('1000', '-0.1', '2.5', '1.0', 'probability')

def test_kelly_criterion_negative_win_input_true_odds():
    with pytest.raises(ValueError, match="True odds must be greater than 1."):
        kelly_criterion('1000', '-1.5', '2.5', '1.0', 'true_odds')

def test_kelly_criterion_negative_multiplier():
    with pytest.raises(ValueError, match="Multiplier must be between 0 and 1, exclusive of 0 and inclusive of 1."):
        kelly_criterion('1000', '0.55', '2.5', '-0.5', 'probability')

def test_kelly_criterion_multiplier_greater_than_one():
    with pytest.raises(ValueError, match="Multiplier must be between 0 and 1, exclusive of 0 and inclusive of 1."):
        kelly_criterion('1000', '0.55', '2.5', '1.1', 'probability')

def test_kelly_criterion_extremely_high_multiplier():
    # Assuming you adjust your function to allow multipliers strictly between 0 and 1, this test would be redundant
    # This is more of a conceptual test assuming the function could accept it
    with pytest.raises(ValueError, match="Multiplier must be between 0 and 1, exclusive of 0 and inclusive of 1."):
        kelly_criterion('1000', '0.55', '2.5', '100', 'probability')

def test_kelly_criterion_probability_of_one():
    result = kelly_criterion('1000', '1', '2.5', '1.0', 'probability')
    assert result == Decimal('1000') * ((Decimal('2.5') - Decimal('1')) / (Decimal('2.5') - Decimal('1'))), "Bet size should be maximal for a certainty"

def test_kelly_criterion_true_odds_of_one():
    with pytest.raises(ValueError, match="True odds must be greater than 1."):
        kelly_criterion('1000', '1', '2.5', '1.0', 'true_odds')

def test_kelly_criterion_extremely_high_odds():
    # Testing with extremely high odds to ensure function handles large numbers well
    result = kelly_criterion('1000', '0.99', '1000', '1.0', 'probability')
    assert result < Decimal('1000'), "Bet size should be less than bankroll even with very high odds and high probability"
