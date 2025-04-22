#!/usr/bin/env python
#
# Data Management Case Study: Currency Exchange Application
# This application combines working with URLs, exceptions, files and directories, dictionaries, standard modules, OOP, Pandas etc.

import os
import time
import urllib.request
import sys
import datetime
import json
import pandas as pd
import ssl
from inscriptis import get_text
import matplotlib.pyplot as plt

class CurrencyExchange():
    def __init__(self, exurl):
        self.exurl = exurl
        self.dir = os.path.join(os.path.expanduser("~"), "exchange_data")
        os.makedirs(self.dir, exist_ok=True)
        self.exfile = os.path.join(self.dir, "exchange_data_auto.txt")
        self.c = {}

    def update(self):
        self.retrieve()
        self.parse()

    def retrieve(self):
        caching = os.path.isfile(self.exfile) and (time.time() - int(os.stat(self.exfile).st_mtime) <= 24 * 60 * 60)

        if not caching:
            print(f"Auto-updating file {self.exfile} from {self.exurl}...")
            try:
                ctx = ssl.create_default_context()
                ctx.set_ciphers("HIGH:!DH")
                fweb = urllib.request.urlopen(self.exurl, context=ctx)
            except Exception as e:
                print(f"Cannot load data! ({e})", file=sys.stderr)
                exit(-1)
            else:
                data_html = fweb.read().decode()
                data_text = get_text(data_html)
                with open(self.exfile, "w") as f:
                    f.write(data_text)
        else:
            print(f"Re-using cache file {self.exfile}")

    def parse(self):
        with open(self.exfile) as f:
            lines = [l.strip() for l in f.readlines()]

        ctr = 100
        for l in lines:
            if l.startswith("Land"):
                ctr = 0

            if ctr >= 2 and ctr < 100:
                fields = l.split()
                if 8 <= len(fields) <= 10:
                    if len(fields) > 8:
                        landname = " ".join(fields[:len(fields) - 7])
                        fields = [landname] + fields[len(fields) - 7:]
                    cur = fields[2]
                    mul = int(fields[3])
                    if fields[4] == "-":
                        continue
                    buy = float(fields[4])
                    sell = float(fields[5])
                    print(f"{cur} {buy:6.3f} {sell:6.3f} {mul:3d}")
                    self.c[cur] = buy / mul, sell / mul
                else:
                    ctr = 100

            ctr += 1
        print("")

    def calculate(self):
        rates = {}
        for currency, v in self.c.items():
            r = 100 * (v[1] / v[0] - 1) / 2
            rates[currency] = r

        currencies = list(self.c.keys())
        currencies.sort(key=lambda x: rates[x])
        for currency in currencies:
            print(f"{currency}: {rates[currency]:5.2f}%")
        print("")

        midrates = {}
        for currency, v in self.c.items():
            r = sum(v) / len(v)
            midrates[currency] = r

        currencies.sort(key=lambda x: midrates[x])
        for currency in currencies:
            print(f"- midrate: {currency} = {midrates[currency]:.3f}")
        print("")

    def snapshot(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        snapfile = self.exfile + "." + date
        print(f"Snapshotting to file {snapfile}")
        with open(snapfile, "w") as f:
            json.dump(self.c, f)
        print("")

    def analyse(self):
        snapshotfiles = os.listdir(self.dir)
        snapshotfiles = [sf for sf in snapshotfiles if sf.startswith(os.path.basename(self.exfile) + ".")]
        snapshotfiles.sort()
        print("List of snapshots to load", snapshotfiles)
        print("")

        df_buy = pd.DataFrame({"Currency": []})
        for snapshotfile in snapshotfiles:
            date = snapshotfile.split(".")[-1]
            with open(os.path.join(self.dir, snapshotfile)) as f:
                c = json.load(f)
            for rowpos, (k, v) in enumerate(c.items()):
                buy = v[1]
                df_buy.loc[rowpos, "Currency"] = k
                df_buy.loc[rowpos, date] = buy
        print(df_buy)

        print("Averages:")
        print(df_buy.mean(numeric_only=True).to_string())

        eur_chf = df_buy[df_buy["Currency"] == "EUR"].set_index("Currency").T
        eur_chf.plot(title="EUR/CHF Rate Development")
        plt.show()

        asian_currencies = ["JPY", "CNY"]
        df_asian = df_buy[df_buy["Currency"].isin(asian_currencies)].set_index("Currency").T
        df_asian.plot(title="Far-East Asian Currencies Volatility")
        plt.show()

if __name__ == "__main__":
    url = "https://zkb-finance.mdgms.com/home/currencies/exchangerates/index.html"
    ce = CurrencyExchange(url)
    ce.update()
    ce.calculate()
    ce.snapshot()
    ce.analyse()

