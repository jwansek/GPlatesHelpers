import sys
import re

try:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
except IndexError:
    print("You need to specify the path to the .rot file as the first parameter and the output file path as the second parameter e.g. python linebreaker.py Rotation.rot output.rot")
    exit(-1)

with open(input_path, "r") as f:
    input_ = f.read()

output = re.sub(r"\n{2,}", "\n", input_)

with open(output_path, "w") as f:
    f.write(output)
