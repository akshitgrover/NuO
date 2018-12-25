#! /usr/bin/env python

import os
import shutil

from NuO.configParser import parser
import NuO.nuoParser as nps
import NuO.siteData as sd

def main():
    if(os.path.exists("build")):
        shutil.rmtree("build")
    os.mkdir("build")
    print("Starting to parse...", end = "\n\n")
    parser.parse("./config.yml")
    sd.siteData()
    nps.parse()
