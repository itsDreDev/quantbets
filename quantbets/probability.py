from decimal import Decimal, InvalidOperation

def calculate_ev_percentage(odds, probability):
    """
    Calculate the expected value (EV) as a percentage of return on investment (ROI) in decimal format.

    :param odds: Decimal odds of the bet.
    :param probability: The bettor's estimated probability of winning (as a decimal).
    :return: The expected value of the bet as a percentage in decimal format.
    """
    try:
        odds = Decimal(odds)
        probability = Decimal(probability)
    except InvalidOperation:
        raise ValueError("Odds and probability must be convertible to Decimal.")

    if not (Decimal('0') <= probability <= Decimal('1')):
        raise ValueError("Probability must be between 0 and 1.")

    if odds <= Decimal('1'):
        raise ValueError("Odds must be greater than 1.")

    # EV calculation as ROI percentage
    ev_percentage = (probability * (odds - Decimal('1'))) - (Decimal('1') - probability)
    
    return ev_percentage