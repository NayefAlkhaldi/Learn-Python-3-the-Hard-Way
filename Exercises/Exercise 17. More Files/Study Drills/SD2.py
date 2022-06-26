# Making the script shorter without semicolons (;)
import sys, os

script, from_file, to_file = sys.argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long\nDoes the output file exist? {os.path.exists(to_file)}\nAlright, all done.")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close(), in_file.close()