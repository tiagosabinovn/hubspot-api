# Install Dependencies

%run GeneralDependencies
%run functions/gsheets
%sh pip install pygsheets
%run functions/google_api
%run functions/redshift

import pandas as pd
import pyspark.sql.functions as F
from pyspark.sql import Window
from pyspark.sql.types import ArrayType, BooleanType, DateType, DecimalType, DoubleType, IntegerType, StringType, TimestampType

