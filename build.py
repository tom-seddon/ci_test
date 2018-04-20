import sys,argparse

def main():
    suffix=sys.argv[1]

    fname='output-%s.txt'%suffix
    print 'output name: %s'%fname

    with open(fname,'wt') as f: f.write("hello. %s\n"%suffix)

if __name__=="__main__":
    main()
