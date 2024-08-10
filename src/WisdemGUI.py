import os
from utilities.utilities import run_powershell_command


class WisdemGUI:

    def __init__(self):
        pass

    def run(self):
        run_powershell_command("wisdem")
