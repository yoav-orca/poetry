import os
import yaml

with open("a.yaml") as f:
    yaml.load(f)

x = 1
if x == x:
    print("X")

with open("b.yaml") as f:
    yaml.load(f)

