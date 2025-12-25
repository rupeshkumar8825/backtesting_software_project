# this function handles the data downloading part of the all the stocks
# we will be downloading the complete data from the NSE itself
# this class consists all such functions for this purpose

import pandas as pandas
import yfinance as yfinance
import logging
logger = logging.getLogger(__name__)

# class to handle the download stock related data
class DownloadStockData:

    """
    Constructor for this DownloadStockData class for this purpose
    """
    def __init__(self):
        self.download_status = False
        self.download_path = ""




    """
    Given the companyName, downloadPath this function downloads the 
    complete stock data from the NSE website.
    We are going to download the data from the yfinance.
    """
    def download_stock_data_given_company_name(companyName : str, dowloadPath : str):
        print("Downloading the stock given the company name comes here")

    



    '''
    Given the file path of all the equity symobl we will filter out the array 
    of all the supported stock symbols on the NSE website
    '''
    def get_all_equity_symbols(self, equitySymbolFile : str) -> pandas.DataFrame:
        try :
            read_data : pandas.DataFrame = pandas.read_csv(equitySymbolFile)
            read_data = read_data["SYMBOL"]
            logger.info("The list of all the equity symbols read are as follows:")
            logger.info(read_data)
            logger.info("Total number of stocks are ")
            logger.debug(len(read_data))
        except Exception as exception:
            # we need to log the exception completely
            logger.exception(exception)
            return []
        # say everything went fine
        return read_data
        
        



    