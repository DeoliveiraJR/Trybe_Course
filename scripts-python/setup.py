from cx_Freeze import setup, Executable

setup(
    name="script",
    version="0.1",
    description="Meu programa incrível",
    executables=[Executable("script-final.py")]
)
