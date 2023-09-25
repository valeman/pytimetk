
# *** Import everything to make timetk a standalone package ***

from .core.summarize_by_time import *
from .core.timeseries_signature import *
from .core.holiday_signature import *
from .core.make_future_timeseries import *
from .core.make_timeseries_sequence import *
from .core.lags import *
from .core.pad import *
from .core.rolling import *

from .datasets.get_datasets import *

from .utils.datetime_helpers import *
from .utils.pandas_helpers import *
from .utils.memory_helpers import *

# *** Needed for quartodoc build important functions ***
from .core.summarize_by_time import (
    summarize_by_time
)
from .core.timeseries_signature import (
    get_timeseries_signature, augment_timeseries_signature
)
from .core.holiday_signature import (
    augment_holiday_signature
)
from .core.make_future_timeseries import (
    make_future_timeseries, future_frame
)
from .core.make_timeseries_sequence import (
    make_weekday_sequence, make_weekend_sequence
)
from .core.lags import (
    augment_lags
)
from .core.pad import (
    pad_by_time
)
from .core.rolling import (
    augment_rolling
)
from .datasets.get_datasets import (
    load_dataset, get_available_datasets
)
from .utils.datetime_helpers import (
    floor_date, week_of_month, get_pandas_frequency, is_holiday
)
from .utils.memory_helpers import (
    reduce_memory_usage
)


__version__ = '0.0.0.9000'
__author__ = 'Matt Dancho (Business Science)'
