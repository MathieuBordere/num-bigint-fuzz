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
        #sys.stderr.write('command: ' + command + '\n')
        if command == 'stop':
            break
        elif command == 'add':
            a = sys.stdin.readline().strip()
            b = sys.stdin.readline().strip()
            #sys.stderr.write('add read 2 \n')
            a = int.from_bytes(base64.b64decode(a))
            b = int.from_bytes(base64.b64decode(b))
            result = a + b
            n_bytes = math.ceil(result.bit_length() / 8)
            if n_bytes == 0:
                n_bytes = 1 
            result = int.to_bytes(result, n_bytes, 'big')
            result = base64.b64encode(result)
            sys.stdout.buffer.write(result)
            sys.stdout.buffer.write(b'\n')
            sys.stdout.flush()
        elif command == 'mult':
            a = sys.stdin.readline().strip()
            b = sys.stdin.readline().strip()
            #sys.stderr.write('mult read 2 \n')
            a = int.from_bytes(base64.b64decode(a))
            b = int.from_bytes(base64.b64decode(b))
            result = a * b
            #sys.stderr.write(str(a) + ' ' + str(b) + ' ' + str(result) + '\n');
            n_bytes = math.ceil(result.bit_length() / 8)
            if n_bytes == 0:
                n_bytes = 1 
            result = int.to_bytes(result, n_bytes, 'big')
            #sys.stderr.write('bytes' + str(result) + '\n');
            result = base64.b64encode(result)
            sys.stdout.buffer.write(result)
            sys.stdout.buffer.write(b'\n')
            sys.stdout.flush()
        else:
            break

if __name__ == "__main__":
    main()
