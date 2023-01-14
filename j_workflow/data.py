from urllib.request import urlretrieve
import os
import pandas as pd
FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
# saves us downloading every time
def get_fremont_data(filename = "fremont.csv",
                     url = FREMONT_URL, force_download = False):
    """Download and cache the fremont data
    
    Parameters
    __________
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : boolean
        override the detection of the file to re - download
        
    Returns a modified pandas df
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, filename)
    data  = pd.read_csv(filename, index_col = "Date", parse_dates = True)
    data.columns = ['Total', 'West', 'East'] # rename columns
    return data
