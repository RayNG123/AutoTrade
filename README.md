# AutoTrade: Stock Trading Automation with Alpaca API

## Overview

This project aims to automate stock trading using machine learning models for predictive analytics and Alpaca API for executing trades. The system employs machine learning models trained to understand and predict stock price movements. These models can be either for regression or classification tasks. They are capable of dynamically retraining based on new data and can be fine-tuned for various trading strategies. It incorporates a variety of trading indicators and strategies to make buy/sell decisions. The project consists of various modules including data downloading, price prediction, and trading strategy implementation.

**Note: This project is intended for educational purposes and should not be used as financial advice.**

## Prerequisites

- Python 3.x
- Alpaca trading account
- pandas
- numpy

## Installation

First, clone the repository:

\`\`\`bash
git clone https://github.com/yourusername/yourrepository.git
\`\`\`

Navigate to the project directory:

\`\`\`bash
cd yourrepository
\`\`\`

Install the required Python packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Modules

1. `data_downloader`: Responsible for downloading stock data.
2. `price_prediction`: Uses machine learning models to predict stock prices.
3. `trading_strategy`: Determines trading decisions based on price predictions and other indicators.
4. `models`: contains a set of machine learning models to predict stock prices

## How to Set up Hyperparamters

The main file is `execution.py`. You can run it via the command line and pass various arguments to customize your trading strategy. Below are some of the options:

- `--start_date`: Start date for historical data
- `--days`: Number of days for which data is needed
- `--stock`: The stock ticker symbol (e.g., 'AAPL')
- `--need_log`: Log transformation flag
- ... (add more based on your argparse setup)

Example usage:

\`\`\`bash
python execution.py --start_date=2022-01-01 --days=350 --stock=AAPL
\`\`\`

## GitHub Actions Workflow

### Automated Trading Schedule

This project uses GitHub Actions to automate the trading script. The workflow is scheduled to run at 3:30 PM ET (8:30 PM UTC) from Monday to Friday. After customizing your trading strategy and hyperparamters in execution.py, Github Actions automates the trading process based on predetermined schedule on each trading day.

### Workflow Configuration

The `.github/workflows` directory contains the YAML configuration file for the workflow.

**Important:**  Please register your own Alpaca API ID and Secret key for API trading services

## Trading Functions

- `GetPosition(trading_client)`: Retrieves the current position in the given stock.
- `PlaceOrderBUY(trading_client, ticker, quantity)`: Places a buy order.
- `PlaceOrderSELL(trading_client, ticker, quantity)`: Places a sell order.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
