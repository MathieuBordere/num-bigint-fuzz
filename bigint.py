import base64
import math
import sys

def main():
    assert(len(sys.argv) == 1)
    # The program waits for input from the user, the first line is the command, followed
    # by the arguments. The program will then execute the command and write the result to stdout.
    # The possible commands are: 'add', 'mult' and 'stop'. When the command 'stop' is given, the program
    # terminates. The program will only accept commands that are in the list of possible commands.
    # 'add' and 'mult' will take two arguments, which are two base64 encoded integers. The program will
    # decode the integers, perform the operation and encode the result. The result will be written to stdout.
    while True:
        command = sys.stdin.readline().strip()
        if command == 'stop':
            break
        elif command == 'add':
            a = sys.stdin.readline().strip()
            b = sys.stdin.readline().strip()
            a = int.from_bytes(base64.b64decode(a))
            b = int.from_bytes(base64.b64decode(b))
            result = a + b
            result = int.to_bytes(result, math.ceil(result.bit_length() / 8), 'big')
            result = base64.b64encode(result)
            sys.stdout.buffer.write(result)
            sys.stdout.buffer.write(b'\n')
            sys.stdout.flush()
        elif command == 'mult':
            a = sys.stdin.readline().strip()
            b = sys.stdin.readline().strip()
            a = int.from_bytes(base64.b64decode(a))
            b = int.from_bytes(base64.b64decode(b))
            result = a * b
            result = int.to_bytes(result, math.ceil(result.bit_length() / 8), 'big')
            result = base64.b64encode(result)
            sys.stdout.buffer.write(result)
            sys.stdout.buffer.write(b'\n')
            sys.stdout.flush()
        else:
            break

if __name__ == "__main__":
    main()
