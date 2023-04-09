import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    from scipy.stats import ks_2samp 
    p = ks_2samp(x, y)[1]
    return p < alpha
