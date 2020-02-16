#!/usr/bin/env python
#
# usage:
#       testyoke pytest 
#       testyoke rspec
#
# automatically add appropriate parameter, grab file
#
import sys
from os import environ, path, getcwd
import argparse
import subprocess
from testyoke import Client, get_config
from testyoke.cvs import Git
from testyoke.client import ClientException
from testyoke.view import view
from . import main

if __name__ == '__main__':
    main()
