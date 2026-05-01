with open('triangular_100_higher_ensembles.txt', 'r') as f1, open('triangular_100.txt', 'w') as f2:
    for i in range(101021):
        line = f1.readline()
        if not line:  # stop if file ends early
            break
        f2.write(line)
        
## if the raw data contains higher number of ensembles, this script allows us to extract the dada associated with specified ensemble
