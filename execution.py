#!pip install finta
#!pip install yfinance
#!pip install ta

from data_downloader import data_downloader
from price_prediction import predict
import argparse
from datetime import datetime, timedelta, date, time

###########################################Set hyperparameters###################################################

# Create the parser
parser = argparse.ArgumentParser(description="argument parser for preprocessing and downloading data")

#timing intervals
parser.add_argument("--start_date", type=str, default = None, help="start date of all data")
parser.add_argument("--days", type=int, default = 500, help="number of days needed")
parser.add_argument("--room_na", type=int, default = 200, help="room of na days")
parser.add_argument("--interval", type=str, default = "1d", choices=["1d","1wk","1mo"], help="choose an interval")
parser.add_argument("--end_date", type=str, default = str(date.today()) , help="end date of all data")

#stock needed
parser.add_argument("--stock", action="store_true", default = 'AAPL' , help = "stock to consider download")

#log indicaters
parser.add_argument("--need_log", action="store_false", help="check if log transformation needed")

#finta indicaters without params
parser.add_argument("--need_ta", action="store_false", help="check if ta indicaters needed")
parser.add_argument("--choices_ta", default = "['RSI','STOCH']", help="choices of ta indicaters")

#trend indicaters
parser.add_argument("--need_macd", action="store_false", help="check if macd indicaters needed")
parser.add_argument("--columns_macd", default = "['Close']" , help="target column of macd")
parser.add_argument("--short_span", type = int, default = 12 , help="short span of macd")
parser.add_argument("--long_span", type = int, default = 26 , help="long span of macd")
parser.add_argument("--signal_span", type = int, default = 9 , help="signal span of macd")

#ema indicaters
parser.add_argument("--need_ema", action="store_false", help="check if ema indicaters needed")
parser.add_argument("--days_ema", default = "[5,15,25,50]" , help="days of ema installed")
parser.add_argument("--columns_ema", default = "['Close']" , help="target column of ema")

#prev day
parser.add_argument("--need_prev", action="store_false", help="check if previous day indicaters needed")
parser.add_argument("--columns_prev", default = "['Close']" , help="target column of previous day")
parser.add_argument("--days_prev", type = int, default = "20" , help= "number of previous days needed")

#shift target
parser.add_argument("--shift_target", action="store_false", help="check if shifting target for backtesting is needed")
#task definition
parser.add_argument("--regression", action = 'store_false', help="to do regression or classification task")
parser.add_argument("--training_size", type = int, default = 300, help = "number of days to used for traning the model" )
parser.add_argument("--training_interval", type = int,  default = 1, help = 'interval to train a new model for each testing day')

#data preprocessing
parser.add_argument("--return_normalization", action = 'store_true', help="to do return rate normalization or not")
parser.add_argument("--min_max_normalization", action = 'store_true', help="to do min max normalization or not" )
parser.add_argument("--standard_normalization", action = 'store_false', help = "to do standard normalization or not"  )

#sequential
parser.add_argument("--sequential", action = 'store_true', help="using sequential model or  not")
parser.add_argument("--window_size", type = int, default = 20, help="using sequential model or  not")
parser.add_argument("--model", default = 'Conv', help="model to use for training")
parser.add_argument("--model_param", default = {}, help = 'model hyperparamters')

def main(args):
  data = data_downloader(args)
  prediction = predict(args,data)

if __name__ == '__main__':
  args = parser.parse_args([])
  main(args)
