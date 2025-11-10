#!/usr/bin/env python3
import yaml
from pprint import pprint

with open('pp.yml', 'r') as f:
    data = yaml.safe_load(f)

pprint(data)