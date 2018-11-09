from configParser import parser
from siteData import *

parser.parse("./config.yml")
print(DATAOBJECT)
print(GLOBALS)
print(NUODIR)
print(DATAFILESOBJECT)