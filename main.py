# no cmd: pip install psutill, pip install GPUtil, pip install py-cpuinfo, pip install wmi

import GPUtil
import cpuinfo

from psutil import virtual_memory, cpu_freq, cpu_count, cpu_percent
from time import sleep

def Mhz_to_Ghz(value):
    return f'{value/1000: .2f} Hz'

def bytes_to_gigas(value):
    return f'{value/1024/1024/1024: .1f}'

def mega_to_giga(value):
    return f'{value/1024: .1f} Gb'

def memGpuPercent(total, using):
    return f'{(using*100)/total: .1f} %'

def dec_to_percent(value):
    return f'{value*100: .1f} %'

#-----DADOS CPU------
def getCpuName():
    cpu = cpuinfo.get_cpu_info()
    return cpu['brand_raw']

def getCpuFreq():
    return Mhz_to_Ghz(cpu_freq().current)

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
    return mega_to_giga(gpu.memoryTotal)

def getGpuMemoryUsed():
    gpu = GPUtil.getGPUs()[0]
    return mega_to_giga(gpu.memoryUsed)

def getGpuMemoryPercent():
    gpu = GPUtil.getGPUs()[0]
    return memGpuPercent(gpu.memoryTotal, gpu.memoryUsed)

def getGpuUsedPercent():
    gpu = GPUtil.getGPUs()[0]
    return dec_to_percent(gpu.load)
#-----DADOS GPU------

#-----DADOS RAM------
def getRamTotal():
    return bytes_to_gigas(virtual_memory().total)

def getRamUsed():
    return bytes_to_gigas(virtual_memory().used)

def getRamUsedPercent():
    return virtual_memory().percent

def getRamFree():
    x = (virtual_memory().total-virtual_memory().used)
    return f'{bytes_to_gigas(x)}'
#-----DADOS RAM------

cont = 0

while cont < 10:
#    gpu = GPUtil.getGPUs()[0] #atribui os dados da gpu
#    cpu = cpuinfo.get_cpu_info()

#    print('Total de memora ram: ', bytes_to_gigas(virtual_memory().total))
#    print('Uso de memoria ram: ', bytes_to_gigas(virtual_memory().used))
#    print('Uso de memoria ram: ', virtual_memory().percent, '% \n')

#    print(cpu['brand_raw'])
    #print(cpu['hz_actual_friendly']) # key de frequencia usando cpuinfo
    #print(cpu['hz_advertised_friendly'])
#    print('Frequancia base do cpu: ', Mhz_to_Ghz(cpu_freq().current))
#    print('Quantidade de nucleos do cpu: ', cpu_count())
#    print('Uso do cpu: ', cpu_percent(), '% \n') #para melhor precisao chamar em 0.1 s ou menor

#    print(gpu.name)
#    print('Temperatura da gpu: ', gpu.temperature, '°C') #Alt + 0176
#    print('Memoria de gpu total: ', mega_to_giga(gpu.memoryTotal))
#    print('Uso de memoria gpu: ', mega_to_giga(gpu.memoryUsed))
#    print('Percentual da memoria gpu em uso: ', memGpuPercent(gpu.memoryTotal, gpu.memoryUsed))
#    print('Percentual de uso gpu', dec_to_percent(gpu.load))

#    print()
#    sleep(1)

    cont = cont + 1