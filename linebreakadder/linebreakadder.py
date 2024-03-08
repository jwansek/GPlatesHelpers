import sys
import re

try:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
except IndexError:
    print("You need to specify the path to the .rot file as the first parameter and the output file path as the second parameter e.g. python linebreakadder.exe Rotation.rot output.rot")
    exit(-1)

with open(input_path, "r") as f:
    input_ = f.read()

lines = re.sub(r"\n{2,}", "\n", input_)

thelastnumber = None
output = ""
for i, line in enumerate(lines.split("\n"), 0):
    if line.split(" ")[0] != thelastnumber and output != "":
        output += "\n"

    output += line + "\n"

    thelastnumber = line.split(" ")[0]

with open(output_path, "w") as fo:
    fo.write(output[:-2])