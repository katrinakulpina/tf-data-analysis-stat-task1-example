import pandas as pd
import numpy as np


chat_id = 324047628 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    from scipy.stats import expon
    return (x.mean() - expon.mean(loc=-11))/10
