# QuantBets

QuantBets is a Python package designed for **quantitative analysis in sports betting**. It provides tools for calculating betting odds, expected value, bankroll management strategies like the Kelly Criterion, and more. Aimed at assisting bettors in making informed decisions, QuantBets leverages statistical models and historical data analysis.

## Features

- **Odds Calculation**: Convert odds between different formats (decimal, fractional, American).
- **Expected Value Calculation**: Determine the expected value of bets based on odds and probability.
- **Bankroll Management**: Apply the Kelly Criterion to calculate optimal bet sizes.
- **Data Analysis**: Tools for analyzing historical betting data.

## Installation

Ensure you have Python 3.6 or later installed. It's recommended to use a virtual environment.

```bash
pip install quantbets
```

### Usage

Here's a quick start guide on using QuantBets:
Calculating Optimal Bet Size with the Kelly Criterion

python

from quantbets.bankroll_management import kelly_criterion

### Example parameters

bankroll = 1000 # Your total betting bankroll
probability = 0.55 # Your estimated probability of winning
odds = 2.5 # The decimal odds offered on the bet
fraction = 1.0 # Fraction of the Kelly criterion to bet

bet_size = kelly_criterion(bankroll, probability, odds, fraction)
print(f"Recommended bet size: ${bet_size}")

This example demonstrates how to calculate the optimal bet size using the Kelly Criterion based on your bankroll, the probability of winning, and the odds.

### Contributing

Contributions to QuantBets are welcome!

    Bug Reports & Feature Requests: Please use the issue tracker to report any bugs or file feature requests.
    Developing: PRs are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Support

Need help? Feel free to open an issue on our GitHub repository. Whether you're encountering a bug, need help with using QuantBets, or want to share ideas for improvement, we'd love to hear from you!
License

QuantBets is licensed under the MIT License. See the LICENSE file for more details.
