from __future__ import unicode_literals
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg
from fbprophet import Prophet
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt


def test_matplotlib():
    prophet = Prophet()

    years = [2014, 2015, 2016, 2017]
    scores = [240, 240, 257, 272]

    # scores = [
    #     ("2014", 240),
    #     ("2015", 240),
    #     ("2016", 257),
    #     ("2017", 272)
    # ]
    # labels = ['year', 'score']
    # df = pd.DataFrame.from_records(scores, columns=labels)

    df = pd.DataFrame({'y': years, 'ds': scores})

    prophet.add_seasonality(name="yearly", period=1, fourier_order=3, prior_scale=0.1)

    prophet.fit(df)

    future = prophet.make_future_dataframe(periods=10)
    future['cap'] = 4000
    future['floot'] = 1500
    forecast = prophet.predict(future)

    return forecast

    matplotlib.pyplot.close(f)

    canvas = FigureCanvasAgg(f)
    return canvas
