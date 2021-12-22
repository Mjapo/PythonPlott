import matplotlib.pyplot as plt
notas_matematica = [5, 6, 5, 8, 9, 9.5, 6.5, 8]
x= list(range(0,11))
y = notas_matematica
plt.plot(x, y)
plt.show()

import pandas as pd
import numpy as np
import matplotlib as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()    
ts.plot()