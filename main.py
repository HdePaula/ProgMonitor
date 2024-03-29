# no cmd: pip install psutil, pip install GPUtil, pip install py-cpuinfo, pip install wmi

import GPUtil
import cpuinfo

from psutil import virtual_memory, cpu_freq, cpu_count, cpu_percent

def Mhz_to_Ghz(value):
    return f'{value/1000: .2f}'

def bytes_to_gigas(value):
    return f'{value/1024/1024/1024: .1f}'

def mega_to_giga(value):
    return f'{value/1024: .1f}'

def memGpuPercent(total, using):
    return f'{(using*100)/total: .1f}'

def dec_to_percent(value):
    return f'{value*100: .1f}'

#-----DADOS CPU------
def getCpuName():
    cpu = cpuinfo.get_cpu_info()
    return cpu['brand_raw']

def getCpuFreq():
    return float(Mhz_to_Ghz(cpu_freq().current))

def getCpuCount():
    return cpu_count()

def getCpuUsedPercent():
    return cpu_percent()
#-----DADOS CPU------

#-----DADOS GPU------
def getGpuName():
    gpu = GPUtil.getGPUs()[0]
    return gpu.name

def getGpuTemp():
    gpu = GPUtil.getGPUs()[0]
    return gpu.temperature

def getGpuMemoryTotal():
    gpu = GPUtil.getGPUs()[0]
    return float(mega_to_giga(gpu.memoryTotal))

def getGpuMemoryUsed():
    gpu = GPUtil.getGPUs()[0]
    return float(mega_to_giga(gpu.memoryUsed))

def getGpuMemoryFree():
    gpuTotal = GPUtil.getGPUs()[0]
    gpuUsing = GPUtil.getGPUs()[0]
    gpuFree = float(mega_to_giga(gpuTotal.memoryTotal)) - float(mega_to_giga(gpuUsing.memoryUsed))
    return round(gpuFree, 1)

def getGpuMemoryPercent():
    gpu = GPUtil.getGPUs()[0]
    return float(memGpuPercent(gpu.memoryTotal, gpu.memoryUsed))

def getGpuUsedPercent():
    gpu = GPUtil.getGPUs()[0]
    return float(dec_to_percent(gpu.load))
#-----DADOS GPU------

#-----DADOS RAM------
def getRamTotal():
    return float(bytes_to_gigas(virtual_memory().total))

def getRamUsed():
    return float(bytes_to_gigas(virtual_memory().used))

def getRamUsedPercent():
    return virtual_memory().percent

def getRamFree():
    x = (virtual_memory().total-virtual_memory().used)
    return float(f'{bytes_to_gigas(x)}')
#-----DADOS RAM------