
import pandas as pd
from importlib.resources import open_text
from importlib.resources import contents

    
def load_dataset(
    name: str = "m4_daily", 
    verbose: bool = False, 
    **kwargs
) -> pd.DataFrame:
    '''
    Load one of 11 Time Series Datasets.
    
    The `load_dataset` function is used to load various time series datasets by name, with options to print the available datasets and pass additional arguments to `pandas.read_csv`. The available datasets are:
    
    - `m4_hourly`: The M4 hourly dataset
    - `m4_daily`: The M4 daily dataset
    - `m4_weekly`: The M4 weekly dataset
    - `m4_monthly`: The M4 monthly dataset
    - `m4_quarterly`: The M4 quarterly dataset
    - `m4_yearly`: The M4 yearly dataset
    - `bike_sharing_daily`: The bike sharing daily dataset
    - `bike_sales_sample`: The bike sales sample dataset
    - `taylor_30_min`: The Taylor 30 minute dataset
    - `walmart_sales_weekly`: The Walmart sales weekly dataset
    - `wikipedia_traffic_daily`: The Wikipedia traffic daily dataset
    
    The datasets can be loaded with `timetk.load_dataset(name)`, where `name` is the name of the dataset that you want to load. The default value is set to "m4_daily", which is the M4 daily dataset. However, you can choose from a list of available datasets mentioned above.
    
    Parameters
    ----------
    name : str, optional
        The `name` parameter is used to specify the name of the dataset that you want to load. The default value is set to "m4_daily", which is the M4 daily dataset. However, you can choose from a list of available datasets mentioned in the function's docstring.
    verbose : bool, optional
        The `verbose` parameter is a boolean flag that determines whether or not to print the names of the available datasets. If `verbose` is set to `True`, the function will print the names of the available datasets. If `verbose` is set to `False`, the function will not print anything.
    **kwargs
        The `**kwargs` parameter is used to pass additional arguments to `pandas.read_csv`.
    
    Returns
    -------
    pd.DataFrame
        The `load_dataset` function returns the requested dataset as a pandas DataFrame.
        
        
    Examples
    --------
    ```{python}
    import timetk as tk
    import pandas as pd
    ```
    
    ```{python}
    # Bike Sales Sample Dataset
    df = tk.load_dataset('bike_sales_sample', parse_dates = ['order_date'])
    
    df
    ```
    
    ```{python}
    # Taylor 30-Minute Dataset
    df = tk.load_dataset('taylor_30_min', parse_dates = ['date'])
    
    df
    ```
    
    
    '''
    
    # Return the list of available datasets
    dataset_list = get_available_datasets()
    
    if verbose:
        print("Available Datasets:")
        print(dataset_list)
        
    if name not in dataset_list:
        raise ValueError(f"Dataset {name} not found. Please choose from the following: \n{dataset_list}")
    
    # Load the dataset
    with open_text("timetk.datasets", f"{name}.csv") as f:
        df = pd.read_csv(f, **kwargs)
        
    return df

    
def get_available_datasets():
    '''Get a list of 11 datasets that can be loaded with `timetk.load_dataset`.
    
    The `get_available_datasets` function returns a sorted list of available dataset names from the `timetk.datasets` module. The available datasets are:
    
    
    
    Returns
    -------
    list
        The function `get_available_datasets` returns a sorted list of available dataset names from the `timetk.datasets` module.
    
    Examples
    --------
    ```{python}
    import timetk as tk
    
    tk.get_available_datasets()
    ```
    
    '''
    
    file_names   = list(contents("timetk.datasets"))
    dataset_list = [item for item in file_names if item.endswith(".csv")]
    dataset_list = [name.rstrip('.csv') for name in dataset_list]
    dataset_list = sorted(dataset_list)
    
    return dataset_list