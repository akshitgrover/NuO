#! /usr/bin/python

from configParser import parser
import nuoParser as nps
import siteData as sd

if __name__ == "__main__":
    print("Starting to parse...", end = "\n\n")
    parser.parse("./config.yml")
    sd.siteData()
    nps.parse()