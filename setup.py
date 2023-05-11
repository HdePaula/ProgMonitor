# buildando o programa com cx_freeze
# pip install cx_freeze

from cx_Freeze import setup, Executable

# Configurações do executável
executables = [
    Executable(
        "interface.py",  # Nome do arquivo principal do seu programa
        base=None,  # Deixe como None para criar um executável sem interface
        targetName="interface.exe"  # Nome do arquivo executável gerado
    )
]

# Opções do build
build_options = {
    "includes": ["tkinter", "psutil", "GPUtil", "cpuinfo"], # Bibliotecas adicionais que você está usando
    "include_files": ["main.py"]  # Arquivos adicionais que o programa precisa
}

# Configurações do setup
setup(
    name="ProgMonitor",
    version="1.0",
    description="Dados de hardware",
    options={"build_exe": build_options},
    executables=executables
)