#! /usr/bin/env python

import os
import shutil

from configParser import parser
import nuoParser as nps
import siteData as sd

if __name__ == "__main__":
    if(os.path.exists("build")):
        shutil.rmtree("build")
    os.mkdir("build")
    print("Starting to parse...", end = "\n\n")
    parser.parse("./config.yml")
    sd.siteData()
    nps.parse()
