# this function handles the data downloading part of the all the stocks
# we will be downloading the complete data from the NSE itself
# this class consists all such functions for this purpose

# class to handle the download stock related data
class DownloadStockData:
    def __init__(self, downloadStatus : bool, downloadPath : str):
        self.downloadStatus = downloadStatus
        self.downloadPath = downloadPath

    def DownloadStockDataGivenCompany(companyName : str, dowloadPath : str):
        print("Downloading the stock given the company name comes here")