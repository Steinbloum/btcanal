import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
matplotlib inline

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
cf.go_offline()

arr_1 = np.random.randn(50, 4)
df1 = pd.DataFrame(arr_1, columns=["A", "B", "C", "D"])
df1.iplot()
