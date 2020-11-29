#!/usr/bin/python
from gui import *
import kernel as Kernel
from file import *
from gui2 import *


h2 = threading.Thread(target=Kernel.Kernel)
h2.start()
