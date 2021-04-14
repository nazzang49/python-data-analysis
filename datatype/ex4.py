# sequential data

import numpy as np
import pandas as pd

# 1월 1일 ~ 1월 15일
date_range = pd.date_range(start='2020-01-01', periods=15)
print(date_range)

random_list = np.random.rand(15)
df = pd.DataFrame(random_list.tolist(), columns=['random_value'], index=date_range)
print(df)



