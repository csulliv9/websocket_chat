#!/usr/bin/python

from __future__ import division
from subprocess import PIPE, Popen
import psutil

def get_cpu_temperature():
    process = Popen(['vcgencmd','measure_temp'],stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")]);

print psutil.cpu_percent(interval=1);
print psutil.virtual_memory().percent;
print psutil.disk_usage('/').percent;
print get_cpu_temperature();
