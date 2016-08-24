#! /usr/bin/env python

def process(data):
    counts = {}
    for c in data:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts

def output(counts):
    kvpairs = [(k, v) for k, v in counts.iteritems()]
    sorted_kvpairs = sorted(kvpairs, key=lambda x: x[1], reverse=True)
    for pair in sorted_kvpairs:
        print pair[0], pair[1]

def main():
    with open('hubctog') as f:
        data = f.read()

    counts = process(data)
    output(counts)

if __name__ == '__main__':
    main()
