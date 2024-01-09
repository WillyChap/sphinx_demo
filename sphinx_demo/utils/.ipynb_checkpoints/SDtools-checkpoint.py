import yaml
import os
import glob
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import copy
import re
from datetime import datetime

def func1(arg1,arg2):
    """
    This function takes two arguements setting the first to the second
    
    Parameters:
    
        arg1 (str): arguement 1 
        arg2 (str): arguement 2
    
    Returns:
    
        arg1 (str): arguement 1 
        arg2 (str): arguement 2 = arguement 1
    """
    
    arg1 = arg2
    
    return arg1,arg2

def flip_lat_if_necessary(data):
    """
    Check the orientation of the latitude dimension in an xarray dataset and flip it if necessary.

    Parameters:
        data (xr.Dataset): Input xarray dataset.

    Returns:
        data_flipped (xr.Dataset): Flipped xarray dataset, if necessary.
    """
    # Get the latitude values
    lat_values = data.coords["lat"].values
    
    # Check if latitude is oriented from South to North
    if lat_values[0] < lat_values[-1]:
        # Latitude is oriented from South to North, no need to flip
        return data
    else:
        # Latitude is oriented from North to South, flip it
        data_flipped = data.reindex(lat=lat_values[::-1])
        return data_flipped

def check_lat_lon_coords(data):
    """
    Check if either "latitude/longitude" or "lat/lon" are in the coordinates of the xarray dataset.

    Parameters:
        data (xr.Dataset): Input xarray dataset.

    Returns:
        has_lat_lon_coords (bool): True if either "latitude/longitude" or "lat/lon" are in the coordinates, False otherwise.
    """
    has_lat_lon_coords = False

    # Check for "latitude/longitude" or "lat/lon" in the coordinates
    if "latitude" in data.coords and "longitude" in data.coords:
        has_lat_lon_coords = True
    elif "lat" in data.coords and "lon" in data.coords:
        has_lat_lon_coords = True

    return has_lat_lon_coords
