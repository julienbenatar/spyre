# from spyre import spyre
# import spyre
try:
	from . import server
except:
	import server
server.include_df_index = True

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import pi
import time

class TestApp2(server.App):
	title = "Test App 2"
	inputs = [{	"input_type":'slider',
				"label": 'frequency', 
				"variable_name": 'freq', 
				"value" : 2,
				"min" : 1, 
				"max" : 10,
				"action_id" : "refresh",
			}]
	controls = [{	"control_type" : "button",
					"control_id" : "refresh",
					"label" : "refresh",
				}]
	outputs = [{	"output_type" : "plot",
					"output_id" : "plot1",
					"control_id" : "refresh",
				},
				{	"output_type" : "table",
					"output_id" : "table1",
					"control_id" : "refresh",
				}]

	def getData(self,params):
		f = float(params['freq'])
		x = np.arange(0,6*pi,pi/50)
		y1 = np.cos(f*x)
		y2 = np.sin(f*x)
		df = pd.DataFrame({"cos":y1,"sin":y2},index=x)
		df.index.name = "t"
		return df

if __name__ == '__main__':
	app = TestApp2()
	app.launch(port=9095)
