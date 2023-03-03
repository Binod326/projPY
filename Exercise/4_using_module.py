#excersice using modules
'''import sys
from pathlib import Path
import math
content = dir(math)
print(content)
print(dir(Path))
'''

from Mod_Multiplication_Table import multiplicationTable as MT
content = dir(MT)
print(MT(51,20))
