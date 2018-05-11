from django.shortcuts import render
import requests
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap
import pandas
import bs4 as bs
import urllib.request
import datetime
import time
from coin import timec

def index(request):
    return render(request,'index.html')

def coinDetail(request):
    lala = (int(time.time())-60*10)
    url = 'http://coincap.io/front'
    data = requests.get(url)
    data = data.json()

    return render(request,'temp/coindetail.html',{"data":data,"lala":lala})

def graph(request, coin_id):
    price = []
    time = []

    url1 = 'http://coincap.io/page/'+str(coin_id)
    datadet = requests.get(url1)
    detail = datadet.json()
    url = 'http://coincap.io/history/365day/'+str(coin_id)

    data = requests.get(url)
    j = data.json()
    l = (len(j['market_cap']))
    for i in range(0, l):
        time.append(pandas.to_datetime(j['market_cap'][i][0], unit='ms'))
        price.append(j['market_cap'][i][1])

    p = figure(plot_width=1200, plot_height=400, title="Crypto Graph", x_axis_label='Time', y_axis_label='Value')
    p.line(time, price, legend=str(coin_id), line_width=2)

    script, div = components(p, CDN)
    return render(request, "graph.html", {"bokeh_script": script, "bokeh_div": div, "detail":detail})


def moneyEXC(request):
    x = timec.time()
    y = x.date()
    url = urllib.request.urlopen("https://www.xe.com/currencytables/?from=USD&date="+str(y))
    soup = bs.BeautifulSoup(url, 'lxml')
    data = []
    table = soup.find('table', {"class": "tablesorter"})
    tbody = table.find('tbody')
    tr = tbody.find_all('tr')
    for i in tr:
        td = i.find_all('td')
        row = {"code": td[0].text, "name": td[1].text, "price": td[2].text, "unit": td[3].text}
        data.append(row)
    return render(request,'temp/moneyEXC.html',{"data":data})

def excGraph(request):
    unit =[]
    code = []
    x = timec.time()
    y = x.date()
    url = urllib.request.urlopen("https://www.xe.com/currencytables/?from=USD&date="+str(y))
    soup = bs.BeautifulSoup(url, 'lxml')
    data = []
    table = soup.find('table', {"class": "tablesorter"})
    tbody = table.find('tbody')
    tr = tbody.find_all('tr')
    for i in tr:
        td = i.find_all('td')
        if (td[0].text in ("PKR", "USD", "INR", "EUR", "CNY", "GBP","SAR")):
            code.append(td[0].text)
            unit.append(td[3].text)
        else:
            continue
    source = ColumnDataSource(data=dict(code=code, unit=unit))
    p = figure(x_range=code, plot_height=350, toolbar_location=None, title="Currency Status w.r.t US Dollar")
    p.vbar(x='code', top='unit', width=0.9, source=source,legend='code',
           line_color='white', fill_color=factor_cmap('code', palette=Spectral6, factors=code))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 1.5
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    script, div = components(p, CDN)
    return render(request, 'temp/excGraph.html',{"bokeh_script": script, "bokeh_div": div})
