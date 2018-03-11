
from pyecharts import Gauge
import psutil
import json

percent = percent_memory = psutil.virtual_memory().percent
gauge = Gauge("内存占用率")
gauge.add("", "内存占用率", percent)
res = json.dumps(gauge._option)

