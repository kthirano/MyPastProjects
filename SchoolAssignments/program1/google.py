import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    pass


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    pass


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    pass


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    pass


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    pass





# Script

if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
