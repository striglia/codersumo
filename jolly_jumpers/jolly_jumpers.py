import sys

def successive_differences(vals):
    """Given a series of values, return the set of absolute differences between
    each successive pair."""
    pairs = zip(vals, vals[1:])
    return set(abs(int(a)-int(b)) for a, b in pairs)

def jolly_jumpers():
    lines = sys.stdin.readlines()
    for line in lines:
        vals = line.strip().split()
        if successive_differences(vals) == set(range(1, len(vals))):
            print ':)'
        else:
            print ':('

if __name__ == '__main__':
    main()
