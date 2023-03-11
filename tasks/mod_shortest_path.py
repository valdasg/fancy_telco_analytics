def shortest_route(ls: list) -> list:
    '''
    Function calculates shortest route cancelling out adjacent oposite directions.
    
    Takes one argument
    ls: list with each item as 1 of the 4 cardinal paths, all in uppercase

    Returns: list
    The optimized set of instructions.
    '''
    def oposite_to(direction: str) -> str:
        '''
        Function oposite direction to a given one.
    
        Takes one argument
        direction: string with the direction name

        Returns: string
        Oposite to the direction.
        '''
        
        oposites = {
            'SOUTH': 'NORTH',
            'NORTH': 'SOUTH',
            'WEST': 'EAST',
            'EAST': 'WEST'
        }
        return oposites[direction]
    
    # create a counter of appearances of oposite directions
    occurancies = sum(ls[i] == oposite_to(ls[i+1]) for i in range (len(ls)-1))
    
    # set number of iterations needed to run through list
    iterations = len(ls)-(len(ls)-occurancies)
    
    # set base case
    if occurancies == 0:
        return ls
    
    # set recursive case
    for i in range (iterations):
        #if adjacent directions are oposite, remove both
        if ls[i] == oposite_to(ls[i+1]):
            del ls[i:i+2]
            
    # use recursion to iterate through list
    return shortest_route(ls)

if __name__ == "__main__":
    
    path = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST", 'NORTH','SOUTH']
    
    print(shortest_route(ls=path))