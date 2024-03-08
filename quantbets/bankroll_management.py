from decimal import Decimal, InvalidOperation

def kelly_criterion(bankroll, win_input, odds, multiplier=1.0, input_type='probability'):
    """
    Calculate the optimal bet size using the Kelly Criterion, with an optional multiplier to adjust the bet size.
    This function allows using either the estimated probability of winning or the true odds (in decimal) as input.

    :param bankroll: Total available bankroll for betting.
    :param win_input: The bettor's estimated probability of winning or the true odds, based on the input_type.
    :param odds: Decimal odds of the bet.
    :param multiplier: A multiplier to adjust the fraction of the bankroll to bet according to Kelly's suggestion.
                       A value of 1.0 uses the full Kelly bet; less than 1.0 uses a more conservative approach.
    :param input_type: 'probability' if win_input is the probability of winning, 'true_odds' if win_input is true odds.
    :return: The recommended bet size.
    """
    
    try:        
        bankroll = Decimal(bankroll)
        win_input = Decimal(win_input)
        odds = Decimal(odds)
        multiplier = Decimal(multiplier)
    except InvalidOperation:
        raise ValueError("Bankroll, win_input, odds, and multiplier must be convertible to Decimal.")
    
    if bankroll <= Decimal('0'):
        raise ValueError("Bankroll must be a positive value.")

    if input_type == 'probability':
        probability = win_input
        if not (Decimal('0') <= probability <= Decimal('1')):
            raise ValueError("Probability must be between 0 and 1, inclusive.")

    elif input_type == 'true_odds':
        true_odds = win_input
        if true_odds <= Decimal('1'):
            raise ValueError("True odds must be greater than 1.")
        probability = Decimal('1') / true_odds

    else:
        raise ValueError("input_type must be either 'probability' or 'true_odds'.")

    if odds <= Decimal('1'):
        raise ValueError("Odds must be greater than 1.")

    if not (Decimal('0') < multiplier <= Decimal('1')):
        raise ValueError("Multiplier must be between 0 and 1, exclusive of 0 and inclusive of 1.")

    b = odds - Decimal('1')  # Converts decimal odds to multiplier
    q = Decimal('1') - probability

    # Calculate the fraction of the bankroll to bet according to Kelly's formula
    kelly_fraction = (b * probability - q) / b

    # Apply the multiplier
    adjusted_bet = kelly_fraction * multiplier

    # Calculate the recommended bet size based on the bankroll and adjusted Kelly fraction
    recommended_bet = bankroll * adjusted_bet

    return recommended_bet
