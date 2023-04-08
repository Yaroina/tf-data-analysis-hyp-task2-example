import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    alpha = 0.03  # уровень значимости
    statistic, pvalue = ks_2samp(x, y)
    return pvalue < alpha
