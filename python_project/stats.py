# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

# Compute the average value of an array
import numpy as np

def avg(y):
    retval = 0
    count = 0
    for i in range(len(y)):
        if (np.isnan(y[i]) == False):
            retval = retval + y[i]
            count = count + 1
    return retval / count