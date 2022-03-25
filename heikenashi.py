from click import format_filename
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

def read_csv(filename):
    if os.name == 'nt':
        return pd.read_csv('c:/trade/Data/bars1/' + filename)
    else:
        return pd.read_csv('/Users/ljp2/trade/Data/bars1/' + filename)

class HA:
    def __init__(self) -> None:
        self.bars = []

    def add(self, bar):
        t = bar.time
        o = bar.open
        h = bar.high
        l = bar.low
        c = bar.close

        if len(self.bars) == 0:
            thisbar = (t,o,h,l,c) 
        else:
            pt,po,ph,pl,pc = self.bars[-1]
            ht = t
            ho = (po + pc) / 2
            hc = (o + h + l + c) / 4
            hh = max(h, ho, hc)
            hl = min(l, ho, hc)
            thisbar = (ht, ho, hh, hl, hc) 
        self.bars.append(thisbar)
        return thisbar


haf = read_csv('20220324.csv')
ha = HA()
for i, row in haf.iterrows():
    ha.add(row)

haf = pd.DataFrame(ha.bars, columns='time open high low close'.split())


fig = go.Figure(data=[go.Candlestick(x=haf['time'],
                open=haf['open'],
                high=haf['high'],
                low=haf['low'],
                close=haf['close'])])

# fig.show()
fig.write_html('ha.html', auto_open=True)