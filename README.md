# AutoTrade: Stock Trading Automation with ML and API Trading

## Overview

This project aims to fully automate stock trading by integrating machine learning models with the Alpaca API for trade execution. Designed to function as a comprehensive trading system, it is built on a modular architecture that includes distinct components for data downloading, stock price prediction, and trading strategy implementation.

### Machine Learning Models
The system employs specialized machine learning models for predictive analytics. These models, which can be configured for either regression or classification tasks, are designed to understand and forecast stock price movements. Additionally, they can dynamically retrain based on new data and are highly customizable to align with various trading strategies.

### Alpaca API Integration
The Alpaca API is integral to the project, serving as the execution engine for trades. It enables the system to place market orders, manage portfolios, and acquire real-time or historical market data across a variety of stock tickers.

### Trading Indicators and Strategies
The project leverages a plethora of trading indicators such as RSI, MACD, and EMA to assist the machine learning models in making more precise buy/sell decisions. These indicators are configurable, providing flexibility to adapt to different trading strategies.

### GitHub Actions for Automation
Thanks to GitHub Actions, the entire trading workflow—from data acquisition and price prediction to order execution—is automated. The system is set to operate from Monday to Friday at 3:30 PM ET, ensuring a consistent trading schedule.

By synergizing these elements, the project delivers a robust, adaptable, and fully automated stock trading system.

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
cd your repository
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



## API Trading Functions

- `GetPosition(trading_client)`: Retrieves the current position in the given stock.
- `PlaceOrderBUY(trading_client, ticker, quantity)`: Places a buy order.
- `PlaceOrderSELL(trading_client, ticker, quantity)`: Places a sell order.

**Important:**  Please register your own Alpaca API ID and Secret key for API trading services

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
