import goody


def read_voter_preferences(file : open):
    pass


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    pass


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    pass


def remaining_candidates(vd : {str:int}) -> {str}:
    pass


def run_election(vp_file : open) -> {str}:
    pass

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
