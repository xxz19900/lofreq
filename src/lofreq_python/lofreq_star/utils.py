#!/usr/bin/env python
"""Generic utils for LoFreq
"""


__author__ = "Andreas Wilm"
__email__ = "wilma@gis.a-star.edu.sg"
__copyright__ = "2013 Genome Institute of Singapore"
__license__ = "Free for non-commercial use"



#--- standard library imports
#
from math import log10
import sys

MAX_INT = 2147483647
# instead of sys.maxint

#--- third-party imports
#
# /


#--- project specific imports
#
# nothing should go here by definition




#def mean_and_stdv(x):
#    """
#    Calculate mean and standard deviation of data x[]:
#    mean = {\sum_i x_i \over n}
#    std = sqrt(\sum_i (x_i - mean)^2 \over n-1)
# 
#    Based on
#    http://www.physics.rutgers.edu/~masud/computing/WPark_recipes_in_python.html
#    """
# 
#    num = len(x)
#    assert num != 0
#    if num == 1:
#        return (x[0], 0.0)
#        
#    mean = sum(x)/float(num)
#    std = sum([(a-mean)**2 for a in x])
#    std = sqrt(std / float(num-1))
# 
#    return mean, std



def prob_to_phredqual(prob):
    """
    Turns an error probability into a phred value
    
    >>> prob_to_phredqual(0.01)
    20
    
    """

    assert prob >= 0.0, (
        "Probability can't be smaller than 0 but got %f" % prob)
    try:
        return int(round(-10.0 * log10(prob)))
    except ValueError:
        # prob is zero
        #return sys.maxint
        return MAX_INT

def phredqual_to_prob(phredqual):
    """
    Turns a phred quality into an error probability

    >>> '%.2f' % phredqual_to_prob(20)
    '0.01'

    """

    assert isinstance(phredqual, int)
    #assert phredqual >= 0, ("Phred-quality must be >= 0, but is %s" % phredqual)
    # also works for phredqual=0
    return 10**(-phredqual/10.0)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()        
            
