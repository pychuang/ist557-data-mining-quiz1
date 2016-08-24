#! /usr/bin/env python

import sys

def load_data():
    m1 = []
    m2 = []

    state = 'M1'
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line:
                state = 'M2'
                continue

            row = [int(n) for n in line.split()]
            if state == 'M1':
                m1.append(row)
            else:
                m2.append(row)

    return m1, m2

def mult(m1, m2):
    n = len(m1)
    k = len(m1[0])
    m = len(m2[0])

    result = []
    for i in xrange(n):
        row = []
        for j in xrange(m):
            cell = 0
            for l in xrange(k):
                cell += m1[i][l] * m2[l][j]
            row.append(cell)
        result.append(row)
    return result

def output(m):
    for row in m:
        print ' '.join([str(n) for n in row])

def main():
    m1, m2 = load_data()
    #output(m1)
    #output(m2)
    result = mult(m1, m2)
    output(result)

if __name__ == '__main__':
    main()
