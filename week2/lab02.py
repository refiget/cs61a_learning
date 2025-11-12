# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python (base)
#     language: python
#     name: base
# ---

# %% [markdown]
# **Problem Solving**
# 1. We have a function that can verify whether k in a digit in n.
# 2. Split the integer into the rightmost digit and the rest, then check the rest whether has the rightmost digit
# 3. Introduce i to count the number of unique digits
#
# **P.S.** mod 10 operation can get the rightmost digit and  integer division by 10 to get the rest.

# %%
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n > 0:
        right_most = n % 10
        n //= 10
        rest = n
        if has_digit(rest, right_most) == False:
            i += 1

    return i
            



# %% [markdown]
# **How to get the indicated digits of a integer**
# 1. We divide the integer by 10 and get its remainder.
# 2. Times it by 10
# 3. Introduce an additonal variable k to represent the k-th digit from rightmost
#    

# %%
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False



# %%
import doctest
doctest.testmod(verbose = True)


# %% [markdown]
# #### Q7: Repeating
# - Definition: A positive integer n is a repeating sequence of positive integer m if n is written by repeating the digits of m one or more times. For example, 616161 is a repeating sequence of 61, but 61616 is not.
#
# - Implement repeating which takes positive integers t and n. It returns whether n is a repeating sequence of some t-digit integer.

# %% [markdown]
# **Problem Solving**
# 1. Input (t,n) and output True/False, return whether t digits repeat to form positive integer n.
# 2. If t equal to n, the return is always True. Notice that the digits of n must be the multiple of t, or return False. For t digits, we just need to consider the rightmost t digits as a integral then check the rest.
# 3. Introduce variable end to store the rightmost t digits.
#

# %%
def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10,t)
    rest = n // pow(10,t)
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest //= pow(10,t)
    return True


# %%
import doctest
doctest.testmod(verbose = True)

# %%
