# Rutronik Elektronische Bauelemente GmbH Disclaimer: The evaluation board
# including the software is for testing purposes only and,
# because it has limited functions and limited resilience, is not suitable
# for permanent use under real conditions. If the evaluation board is
# nevertheless used under real conditions, this is done at one’s responsibility;
# any liability of Rutronik is insofar excluded

def complex_from_i_q_array(i, q):
    retval = []
    for index in range(len(i)):
        retval.append(i[index] + q[index] * 1j)
    return retval