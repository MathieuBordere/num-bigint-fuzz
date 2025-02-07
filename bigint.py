import base64
import sys

def main():
    # 1 operation type and 2 inputs
    assert(len(sys.argv) == 4)
    op = sys.argv[1]
    assert(op == 'add' or op == 'mult')
    lb = base64.b64decode((sys.argv[2]))
    rb = base64.b64decode((sys.argv[3]))
    print("{} {}".format(lb, rb))
    l = int.from_bytes(lb)
    r = int.from_bytes(rb)
    print("{} {}".format(l, r))
    match op:
        case 'add':
            res = l + r
        case 'mult':
            res = l * r
    print(int(res))
    sys.stdout.buffer.write(base64.b64encode(res.to_bytes()))

if __name__ == "__main__":
    main()
