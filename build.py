import sys,argparse

def main():
    fname=sys.argv[1]
    
    print 'output name: %s'%fname

    with open(fname,'wt') as f: f.write("hello. %s\n"%suffix)

if __name__=="__main__":
    main()
