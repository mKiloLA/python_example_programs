"""
Python program to find the largest element and its location.
"""

def largest_element(a):
    """ Return the largest element of a sequence a.
    """
    try:
        maxval = a[0]
        loc = 0
        for i, f in enumerate(a):
            if a[i] > maxval:
                maxval = a[i]
                loc = i
        return maxval, loc
    except ValueError:
        print('ValueError Nerd')
        return -1
    except TypeError:
        print('TypeError nerd')
        return -2
    except Exception as e:
        print(f'A more different error nerd: {e}')
        return -3


if __name__ == "__main__":

    a = [1,'a', 2]
    print("Largest element is {:}".format(largest_element(a)))
