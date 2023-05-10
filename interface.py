import main

import tkinter as tk
from tkinter import ttk

taxaAtualizacao = 1000     #taxa de atualizacao de dados

#atualiza dados
def atualizaDados():
    #dados CPU
    cpuUsing.config(text=(main.getCpuUsedPercent(), "%"), font=fonte_dados)
    cpuFreq.config(text=(main.getCpuFreq(), "GHz"), font=fonte_dados)

    #dados RAM
    ramUsingPercent.config(text=(main.getRamUsedPercent(), "%"))
    ramUsing.config(text=(main.getRamUsed(), "Gb"), font=fonte_dados)
    ramFree.config(text=(main.getRamFree(), "Gb"), font=fonte_dados)

    #dados GPU
    gpuUsing.config(text=(main.getGpuUsedPercent(), "%"), font=fonte_dados)
    gpuTemp.config(text=(main.getGpuTemp(), "°C"), font=fonte_dados)
    gpuMemoryUsingPercent.config(text=(main.getGpuMemoryPercent(), "%"), font=fonte_dados)
    gpuMemoryUsing.config(text=(main.getGpuMemoryUsed(), "Gb"), font=fonte_dados)
    gpuMemoryFree.config(text=(main.getGpuMemoryFree(), "Gb"), font=fonte_dados)

    root.after(taxaAtualizacao, atualizaDados)

# criar a janela
root = tk.Tk()

# definir a geometria da janela
root.geometry("480x800")
root.title('ProgMonitor')
root.columnconfigure(0, weight=1) #weight=0 faz com que o root nao aumente junto com a janela, já =1 sim

# ESTILIZACAO------------------------------------------------------------------
fonte_grande = ("TkDefaultFont", 30)
fonte_dados = ("TkDefaultFont", 22)
# ESTILIZACAO------------------------------------------------------------------

# FRAME CPU--------------------------------------------------------------------
# criar um frame para CPU
square1_frame = tk.Frame(root, bg="orange", pady=10)
square1_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

# criar a label para a CPU
cpu_label = ttk.Label(square1_frame, text="CPU", font=fonte_grande)
cpu_label.pack()

# criar um frame interno no segundo frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(square1_frame, bg="blue")
labels_frame.pack()

# adicionar a primeira label ao frame interno
lbCpuName = ttk.Label(labels_frame, text=main.getCpuName(), font=("TkDefaultFont", 18))
lbCpuName.grid(row=1, column=0, columnspan=2, sticky=tk.W)

lbCpuFreq = ttk.Label(labels_frame, text="Frequencia de CPU: ", font=fonte_dados)
lbCpuFreq.grid(row=2, column=0, sticky=tk.W)
cpuFreq = ttk.Label(labels_frame, text=(main.getCpuFreq(), "GHz"), font=fonte_dados)
cpuFreq.grid(row=2, column=1)

lbCpuUsing = ttk.Label(labels_frame, text="Uso de CPU: " , font=fonte_dados)
lbCpuUsing.grid(row=3, column=0, sticky=tk.W)
cpuUsing = ttk.Label(labels_frame, text=(main.getCpuUsedPercent(), "%"), font=fonte_dados)
cpuUsing.grid(row=3, column=1)

lbCpuCount = ttk.Label(labels_frame, text="Nucleos logicos: ", font=fonte_dados)
lbCpuCount.grid(row=4, column=0, sticky=tk.W)
cpuCount = ttk.Label(labels_frame, text=(main.getCpuCount()), font=fonte_dados)
cpuCount.grid(row=4, column=1)
# FRAME CPU--------------------------------------------------------------------

# FRAME RAM--------------------------------------------------------------------
# criar um frame para RAM
square2_frame = tk.Frame(root, bg="purple", pady=10)
square2_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

# adicionar a label RAM ao segundo frame
ram_label = ttk.Label(square2_frame, text="RAM", font=fonte_grande)
ram_label.pack()

# criar um frame interno no segundo frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(square2_frame, bg="green")
labels_frame.pack()

# adicionar a primeira label ao frame interno
lbRamUsingPercent = ttk.Label(labels_frame, text="Uso de RAM: ", font=fonte_dados)
lbRamUsingPercent.grid(row=0, column=0, sticky=tk.W)
ramUsingPercent = ttk.Label(labels_frame, text=(main.getRamUsedPercent(), "%"), font=fonte_dados)
ramUsingPercent.grid(row=0, column=1)

lbRamUsing = ttk.Label(labels_frame, text="RAM em uso: ", font=fonte_dados)
lbRamUsing.grid(row=1, column=0, sticky=tk.W)
ramUsing = ttk.Label(labels_frame, text=(main.getRamUsed(), "Gb"), font=fonte_dados)
ramUsing.grid(row=1, column=1)

lbRamFree = ttk.Label(labels_frame, text="RAM Livre: ", font=fonte_dados)
lbRamFree.grid(row=2, column=0, sticky=tk.W)
ramFree = ttk.Label(labels_frame, text=(main.getRamFree(), "Gb"), font=fonte_dados)
ramFree.grid(row=2, column=1)

lbRamTotal = ttk.Label(labels_frame, text="Ram Total: ", font=fonte_dados)
lbRamTotal.grid(row=3, column=0, sticky=tk.W)
ramTotal = ttk.Label(labels_frame, text=(main.getRamTotal(), "Gb"), font=fonte_dados)
ramTotal.grid(row=3, column=1)
# FRAME RAM--------------------------------------------------------------------

# FRAME GPU--------------------------------------------------------------------
# criar um frame para o GPU
rectangle_frame = tk.Frame(root, bg="pink", pady=10)
rectangle_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

# criar a label para a GPU
gpu_label = ttk.Label(rectangle_frame, text="GPU", font=fonte_grande)
gpu_label.pack()

# criar um frame interno no terceiro frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(rectangle_frame, bg="red")
labels_frame.pack()

# adicionar a primeira label ao frame interno
lbGpuName = ttk.Label(labels_frame, text=main.getGpuName(), font=fonte_dados)
lbGpuName.grid(row=0, column=0, columnspan=2)

lbGpuTemp = ttk.Label(labels_frame, text="Temperatura GPU: ", font=fonte_dados)
lbGpuTemp.grid(row=1, column=0, sticky=tk.W)
gpuTemp = ttk.Label(labels_frame, text=(main.getGpuTemp(), "%"), font=fonte_dados)
gpuTemp.grid(row=1, column=1)

lbGpuUsing = ttk.Label(labels_frame, text="Uso de GPU: ", font=fonte_dados)
lbGpuUsing.grid(row=2, column=0, sticky=tk.W)
gpuUsing = ttk.Label(labels_frame, text=(main.getGpuUsedPercent(), "%"), font=fonte_dados)
gpuUsing.grid(row=2, column=1)

lbGpuMemoryUsingPercent = ttk.Label(labels_frame, text="Uso de memoria GPU: ", font=fonte_dados)
lbGpuMemoryUsingPercent.grid(row=3, column=0, sticky=tk.W)
gpuMemoryUsingPercent = ttk.Label(labels_frame, text=(main.getGpuMemoryPercent(), "%"), font=fonte_dados)
gpuMemoryUsingPercent.grid(row=3, column=1)

lbGpuMemoryUsing = ttk.Label(labels_frame, text="Memoria GPU em uso: ", font=fonte_dados)
lbGpuMemoryUsing.grid(row=4, column=0, sticky=tk.W)
gpuMemoryUsing = ttk.Label(labels_frame, text=(main.getGpuMemoryUsed(), "Gb"), font=fonte_dados)
gpuMemoryUsing.grid(row=4, column=1)

lbGpuMemoryFree = ttk.Label(labels_frame, text="Memoria GPU em Livre: ", font=fonte_dados)
lbGpuMemoryFree.grid(row=5, column=0, sticky=tk.W)
gpuMemoryFree = ttk.Label(labels_frame, text=(main.getGpuMemoryFree(), "Gb"), font=fonte_dados)
gpuMemoryFree.grid(row=5, column=1)
# FRAME GPU--------------------------------------------------------------------

# iniciar o loop de eventos do tkinter
root.after(taxaAtualizacao, atualizaDados)
root.mainloop()