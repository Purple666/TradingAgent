import os
from os.path import join


class Constant:
    SRC_DIR = os.path.dirname(__file__)
    DATA_DIR = join(SRC_DIR, "../data")
    EUR_USD_H1 = join(DATA_DIR, "eur_usd", "EURUSD_h1.csv")
