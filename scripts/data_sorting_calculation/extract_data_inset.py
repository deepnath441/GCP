## 'square_100.txt' --> data after ensemble average
## extract small section for the plotting the inset of Figures 4, 5 and 6

with open('square_100.txt', 'r') as f1, open('square_100_small.txt', 'w') as f2:
    
    lines = f1.readlines()
    
    # write header (first line)
    f2.write(lines[0])
    
    # process remaining lines
    for line in lines[1:]:
        cols = line.split()
        
        if not cols:
            continue
        
        theta = float(cols[0])
        
        #if 0.27 <= theta <= 0.37: #triangular
        if 0.31 <= theta <= 0.38: #hexagonal
            f2.write(line)
