from collections import defaultdict


def err(f : callable, p : float) -> callable:
    def return_this(x) -> (float, float):
        if ((1.0-p)*f(x) < (1.0+p)*f(x)):
            return ((1.0-p)*f(x),(1.0+p)*f(x))
        else:
            return ((1.0+p)*f(x),(1.0-p)*f(x))
    return return_this


def rank(db : {str:{(str,int)}}) -> [str]:
    return sorted(db, key = (lambda z: len(db[z])), reverse = True)


def who(db : {str:{(str,int)}}, job: str, min_skill : int) -> [(str,int)]:
    if (not type(min_skill) == int):
        raise AssertionError
    if (min_skill > 5 or min_skill < 0):
        raise AssertionError
    passed = []
    for z in db:
        for c,v in db[z]:
            if (job == c and min_skill <= v):
                passed.append((z, v))
    passed.sort()
    passed.sort(key=lambda x:-x[1])
    return passed

    
def by_job (db : {str:{(str,int)}}) -> {str:{(str,int)}}:
    job_dict = dict()
    for z in db:
        for c,v in db[z]:
            if c not in job_dict:
                job_dict[c] = [(z,v)]
            else:
                job_dict[c].append((z,v))
    return job_dict

def scramble(l : [str], ordering : str) -> [str]:
    wordnumbers = []
    for word in l:
        wrdnum = []
        for letter in word:
            for num in range(len(ordering)):
                if letter == ordering[num]:
                    wrdnum.append(num)
        wordnumbers.append(wrdnum)
    wordnumbers.sort(key = lambda x: x)
    final = []
    for word in wordnumbers:
        wrdnum = ""
        for letter in word:
            for num in range(len(ordering)):
                if int(letter) == num:
                    wrdnum += ordering[num]
        final.append(wrdnum)
    return final
        


def longest_match(top : str, bottom : str) -> (int,int):
    def max_same(top_start : int) -> int:
        matches = 0
        for x in range(len(bottom)):
            if (top_start + x >= len(top)):
                return matches
            elif (top[top_start + x] == bottom[x]):
                matches += 1
            else:
                return matches
        return matches
            
    max_matches = (0,0)
    for x in range(len(top)):
        matches = max_same(x)
        if matches > max_matches[1]:
            max_matches = (x, matches)
    return max_matches



if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bsc.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    print('Testing err')
    f = err(lambda x : x, .01)
    print(f(-1),f(0),f(1))
    f = err(lambda x : x**2 - 2.5, .1)
    print(f(0),f(2),f(4))
 
 
    print('\nTesting rank')
    db = {'Adam':    {},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(rank(db))
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(rank(db))
 
 
    print('\nTesting who')
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(who(db,'Cleaning',4))
    print(who(db,'Gardening',0))
    print(who(db,'Tutoring',3))
    print(who(db,'Gambling',0))
    
    
    print('\nTesting by_jobs')
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(by_job(db))
    db = {'Adam':    {},
          'Betty':   {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Charles': {('Laundry', 2)},
          'Diane':   {('Gardening', 2), ('Tutoring', 1)}}
    print(by_job(db))
    
    
    print('\nTesting scramble')
    print(scramble(['abc', 'bac', 'abb'], 'abc'))
    print(scramble(['abc', 'bac', 'abb'], 'cba'))
    print(scramble(['amobea', 'ambian', 'amount', 'amgen'], 'abcdefghijklmnopqrstuvwxyz'))
    print(scramble(['amobea', 'ambian', 'amount', 'amgen'], 'zyxwvutsrqponmlkjihgfedcba'))
 

    print('\nTesting longest_match')
    print(longest_match('accgt','a'))
    print(longest_match('accgt','ccg'))
    print(longest_match('accgt','at'))
    print(longest_match('accgt','ccgt'))
    print(longest_match('accgt','x'))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           

