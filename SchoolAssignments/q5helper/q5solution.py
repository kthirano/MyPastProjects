def compare(a,b):
    if a=='' and b=='':
        return '='
    elif a == '':
        return '<'
    elif b == '':
        return '>'
    elif a[0] > b[0]:
        return '>'
    elif a[0] < b[0]:
        return '<'
    else:
        new_a = a[1:]
        new_b = b[1:]
        return compare(new_a, new_b)
        
        
def is_sorted(l):
    if len(l) < 2:
        return True
    else:
        if l[0] > l[1]:
            return False
        else:
            return is_sorted(l[1:])


def merge (l1,l2):
    if len(l1) == 0 and len(l2) == 0:
        return []
    elif len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        masterlist = []
        if l1[0]==l2[0]:
            masterlist += [l1[0], l2[0]]
            masterlist += merge(l1[1:], l2[1:])
        elif l1[0] > l2[0]:
            masterlist += [l2[0]]
            masterlist += merge(l1, l2[1:])
        else:
            masterlist += [l1[0]]
            masterlist += merge(l1[1:], l2)
        return masterlist


def sort(l):
    if len(l) < 2:
        return l  
    else:
        midindex = int(len(l)/2)
        return merge(sort(l[0:midindex]), sort(l[midindex:]))
        



def nested_sum(l):
    total = 0
    if len(l) == 0:
        return 0
    elif type(l[0]) == int:
        total += l[0]
    else:
        total += nested_sum(l[0])
    total += nested_sum(l[1:])
    return total
        
        

if __name__=="__main__":
    import random,driver
    
    print('\nTesting compare')
    
    print(compare('',''))
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
   
    
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting merge')
    print(merge([],[]))
    print(merge([],[1,2,3]))
    print(merge([1,2,3],[]))
    print(merge([1,2,3,4],[5,6,7,8]))
    print(merge([5,6,7,8],[1,2,3,4]))
    print(merge([1,3,5,7],[2,4,6,8]))
    print(merge([2,4,6,8],[1,3,5,7]))
    print(merge([1,2,5,7,10],[1,2,6,10,12]))


    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = list(range(20))  # List of values 0-19
    for i in range(10):  # Sort 10 times
        random.shuffle(l)
        print(sort(l),sep='-->')
    
    
    print('\nTesting nested_sum')
    print(nested_sum([1,2,3,4,5,6,7,8,9,10]))
    print(nested_sum([[1,2,3,4,5],[6,7,8,9,10]]))
    print(nested_sum([[1,[2,3],4,5],[[6,7,8],9,10]]))
    print(nested_sum([[1,[2,3],[[4]],5],[[6,[7,[8]]],[9,10]]]))


    import driver
    print()
    driver.driver()
