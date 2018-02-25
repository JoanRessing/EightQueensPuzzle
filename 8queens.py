
# coding: utf-8

# Realize that in any solution a column must contain precisely one queen and therefore you can represent a solution as an list of eight integers between 1-8. Also realize that all queens must be on a different row as well, therefore any solution must be a permutation of [1,2,3,4,5,6,7,8].

# In[ ]:


candidate = [1,2,3,4,5,6,7,8]


# Write a function to check whether a candidate solution is valid. To do this only the diagonals have to be checked. Check to see if the function works as intended.

# In[118]:


def check_candidate(candidates):
    for i1, c1 in enumerate(candidates):
        for i2, c2 in enumerate(candidates):
            if i1 < i2:
                if i1+c1 == i2+c2 or i2-i1 == c2-c1:
                    return False
    return True

print(check_candidate([1,2,3,4,5,6,7,8]))
print(check_candidate([4,6,8,2,7,1,3,5]))


# Test your luck to find a solution.

# In[123]:


from random import shuffle

def random_search(candidate):
    while not check_candidate(candidate):
        shuffle(candidate)

candidate = [1,2,3,4,5,6,7,8]
random_search(candidate)

print(candidate)


# Note that the everything also works for larger boards. Let's try the 12 queens problem.

# In[124]:


candidate = [1,2,3,4,5,6,7,8,9,10,11,12]
random_search(candidate)

print(candidate)

