import os
import shutil

import matplotlib.pyplot as plt
import numpy as np
from scipy import interp
import pandas as pd
import seaborn as sns


df = pd.read_json('uwo_sample_tls.json')

print(list(df))