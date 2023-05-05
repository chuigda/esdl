from esdl_parser import parser

if __name__ == '__main__':
    # read all from 'rbuf.esdl' file
    with open('rbuf.esdl', 'r') as f:
        rbuf = f.read()
        # parse
        r = parser.parse(rbuf)
        # print result
        print(r)
