import sys
import re
line = sys.stdin.readline()
while line != '':
        for token in line.split(' '):
                if token.strip() == '\n':
                        sys.stdout.write(token)
                if token.strip() == '':
                        continue
                if token[-1] in '!?':
                        sys.stdout.write(token + '\n')
                elif token[-1] == '.':
                        if token in ['etc.','i.e.','e.g.',';','41.','Prof.','Dr.',':','b.','A.','J.','3.','4.','298.','s.','81-93.','III.','IV.','vs.','(d.']:
                                sys.stdout.write(token + ' ')
                        else:
                                sys.stdout.write(token + '\n')
                else:
                        sys.stdout.write(token + ' ')
        line = sys.stdin.readline()
