import sys

for line in sys.stdin:
        line = line.strip()
        words = line.split()
        try:
            time = words[3].lstrip('[')
            #time = time.replace(':',' ',1)
            print(time,'\t',1)
        except IndexError:
            continue
            
            
