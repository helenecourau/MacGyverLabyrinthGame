from cx_Freeze import setup, Executable

setup(
    name = macgyver,
    version = 0.1,
    description = "macgyver maze game",
    executables = [Executable(macgyver.py)],
)