import main

import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image

#taxa de atualizacao de dados
taxaAtualizacao = 700

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

# Função para desenhar uma linha no canvas
def draw_line(canvas, x1, y1, x2, y2, color):
    canvas.create_line(x1, y1, x2, y2, fill=color)

# criar a janela
root = tk.Tk()

# ESTILIZACAO------------------------------------------------------------------
fonte_grande = ("TkDefaultFont", 30, "bold")
fonte_dados = ("TkDefaultFont", 22, "bold")
fonte_peca = ("TkDefaultFont", 18, "bold")

color_padrao_letra = "cyan"
color_padrao_bg = "black"

label_pad = (0,5,0,0)
# ESTILIZACAO------------------------------------------------------------------

# definir a geometria da janela
root.geometry("480x800")
root.title('ProgMonitor')
root.configure(background=color_padrao_bg)
root.columnconfigure(0, weight=1) #weight=0 faz com que o root nao aumente junto com a janela, já =1 sim
root.iconbitmap("image/icone.ico")

# FRAME CPU--------------------------------------------------------------------
# criar um frame para CPU
square1_frame = tk.Frame(root, bg=color_padrao_bg, pady=5)
square1_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
square1_frame.columnconfigure(0, weight= 1) #wight=1 faz com que tudo que estra dentro se alinhe junto com o square frame

# criar a label para a CPU
cpu_label = ttk.Label(square1_frame, text="CPU", font=fonte_grande, background=color_padrao_bg, foreground=color_padrao_letra)
cpu_label.grid(row=0, column=0, columnspan=2)

# criar um frame interno no segundo frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(square1_frame, bg=color_padrao_bg)
labels_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
labels_frame.columnconfigure(0, weight=1)

# adicionar a primeira label ao frame interno
lbCpuName = ttk.Label(labels_frame, text=main.getCpuName(), font=fonte_peca, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbCpuName.grid(row=1, column=0, columnspan=2, sticky=tk.W)

lbCpuFreq = ttk.Label(labels_frame, text="Frequencia de CPU: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbCpuFreq.grid(row=2, column=0, sticky=tk.W)
cpuFreq = ttk.Label(labels_frame, text=(main.getCpuFreq(), "GHz"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
cpuFreq.grid(row=2, column=1, sticky=tk.E)

lbCpuUsing = ttk.Label(labels_frame, text="Uso de CPU: " , font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbCpuUsing.grid(row=3, column=0, sticky=tk.W)
cpuUsing = ttk.Label(labels_frame, text=(main.getCpuUsedPercent(), "%"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
cpuUsing.grid(row=3, column=1, sticky=tk.E)

lbCpuCount = ttk.Label(labels_frame, text="Nucleos logicos: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbCpuCount.grid(row=4, column=0, sticky=tk.W)
cpuCount = ttk.Label(labels_frame, text=(main.getCpuCount()), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
cpuCount.grid(row=4, column=1, sticky=tk.E)

# Cria o canvas dentro do frame (Linha de divisao de frame)
canvas = tk.Canvas(square1_frame, bg=color_padrao_letra, height=2)
canvas.grid(row=2, column=0, sticky="nsew")
# FRAME CPU--------------------------------------------------------------------

# FRAME RAM--------------------------------------------------------------------
# criar um frame para RAM
square2_frame = tk.Frame(root, bg=color_padrao_bg, pady=5)
square2_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
square2_frame.columnconfigure(0, weight=1)

# adicionar a label RAM ao segundo frame
ram_label = ttk.Label(square2_frame, text="RAM", font=fonte_grande, background=color_padrao_bg, foreground=color_padrao_letra)
ram_label.grid(row=0, column=0, columnspan=2)

# criar um frame interno no segundo frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(square2_frame, bg=color_padrao_bg)
labels_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
labels_frame.columnconfigure(0, weight=1)

# adicionar a primeira label ao frame interno
lbRamUsingPercent = ttk.Label(labels_frame, text="Uso de RAM: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbRamUsingPercent.grid(row=0, column=0, sticky=tk.W)
ramUsingPercent = ttk.Label(labels_frame, text=(main.getRamUsedPercent(), "%"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
ramUsingPercent.grid(row=0, column=1, sticky=tk.E)

lbRamUsing = ttk.Label(labels_frame, text="RAM em uso: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbRamUsing.grid(row=1, column=0, sticky=tk.W)
ramUsing = ttk.Label(labels_frame, text=(main.getRamUsed(), "Gb"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
ramUsing.grid(row=1, column=1, sticky=tk.E)

lbRamFree = ttk.Label(labels_frame, text="RAM Livre: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbRamFree.grid(row=2, column=0, sticky=tk.W)
ramFree = ttk.Label(labels_frame, text=(main.getRamFree(), "Gb"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
ramFree.grid(row=2, column=1, sticky=tk.E)

lbRamTotal = ttk.Label(labels_frame, text="Ram Total: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbRamTotal.grid(row=3, column=0, sticky=tk.W)
ramTotal = ttk.Label(labels_frame, text=(main.getRamTotal(), "Gb"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
ramTotal.grid(row=3, column=1, sticky=tk.E)

# Cria o canvas dentro do frame (Linha de divisao de frame)
canvas = tk.Canvas(square2_frame, bg=color_padrao_letra, height=2)
canvas.grid(row=2, column=0, sticky="nsew")
# FRAME RAM--------------------------------------------------------------------

# FRAME GPU--------------------------------------------------------------------
# criar um frame para o GPU
rectangle_frame = tk.Frame(root, bg=color_padrao_bg, pady=5)
rectangle_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
rectangle_frame.columnconfigure(0, weight=1)

# criar a label para a GPU
gpu_label = ttk.Label(rectangle_frame, text="GPU", font=fonte_grande, background=color_padrao_bg, foreground=color_padrao_letra)
gpu_label.grid(row=0, column=0, columnspan=2)

# criar um frame interno no terceiro frame para adicionar as labels na mesma linha
labels_frame = tk.Frame(rectangle_frame, bg=color_padrao_bg)
labels_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
labels_frame.columnconfigure(0, weight=1)

# adicionar a primeira label ao frame interno
lbGpuName = ttk.Label(labels_frame, text=main.getGpuName(), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuName.grid(row=0, column=0, columnspan=2)

lbGpuTemp = ttk.Label(labels_frame, text="Temperatura GPU: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuTemp.grid(row=1, column=0, sticky=tk.W)
gpuTemp = ttk.Label(labels_frame, text=(main.getGpuTemp(), "%"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
gpuTemp.grid(row=1, column=1, sticky=tk.E)

lbGpuUsing = ttk.Label(labels_frame, text="Uso de GPU: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuUsing.grid(row=2, column=0, sticky=tk.W)
gpuUsing = ttk.Label(labels_frame, text=(main.getGpuUsedPercent(), "%"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
gpuUsing.grid(row=2, column=1, sticky=tk.E)

lbGpuMemoryUsingPercent = ttk.Label(labels_frame, text="Uso de memoria GPU: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuMemoryUsingPercent.grid(row=3, column=0, sticky=tk.W)
gpuMemoryUsingPercent = ttk.Label(labels_frame, text=(main.getGpuMemoryPercent(), "%"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
gpuMemoryUsingPercent.grid(row=3, column=1, sticky=tk.E)

lbGpuMemoryUsing = ttk.Label(labels_frame, text="Memoria GPU em uso: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuMemoryUsing.grid(row=4, column=0, sticky=tk.W)
gpuMemoryUsing = ttk.Label(labels_frame, text=(main.getGpuMemoryUsed(), "Gb"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
gpuMemoryUsing.grid(row=4, column=1, sticky=tk.E)

lbGpuMemoryFree = ttk.Label(labels_frame, text="Memoria GPU em Livre: ", font=fonte_dados, padding=label_pad, background=color_padrao_bg, foreground=color_padrao_letra)
lbGpuMemoryFree.grid(row=5, column=0, sticky=tk.W)
gpuMemoryFree = ttk.Label(labels_frame, text=(main.getGpuMemoryFree(), "Gb"), font=fonte_dados, background=color_padrao_bg, foreground=color_padrao_letra)
gpuMemoryFree.grid(row=5, column=1, sticky=tk.E)

# Cria o canvas dentro do frame (Linha de divisao de frame)
canvas = tk.Canvas(rectangle_frame, bg=color_padrao_letra, height=2)
canvas.grid(row=2, column=0, sticky="nsew")
# FRAME GPU--------------------------------------------------------------------

# iniciar o loop de eventos do tkinter
root.after(taxaAtualizacao, atualizaDados)
root.mainloop()