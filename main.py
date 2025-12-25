# this is a sample main.py file
# this is going to be the entry point of the application 
from download.download import DownloadStockData
import logging.config
from logging_config import *
from pathlib import Path


def main():
    logger = logging.getLogger(__name__)
    logger.info("Application Started")

    download_stock_data : DownloadStockData = DownloadStockData()
    equity_symbol_file_path = Path(__file__).parent/'data/equity_symbols.csv'

    all_equity_list = download_stock_data.get_all_equity_symbols(equity_symbol_file_path)
    logger.info("The returned list of all equity for the first five are as follows")
    logger.info(all_equity_list.head(5))
    logger.info("Application Finished")



if __name__ == '__main__':
    setup_logging();
    main()
