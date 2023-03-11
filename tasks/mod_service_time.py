def computeCheckoutTime(customers: list, queues: int) -> int:
    '''
    Function calculates minimum service time of customers among ques.
    
    Takes two arguments
    customers: list of positive integers, values are servive times at counter.
    n: a positive integer, the number of checkout counters.

    Returns: integer
    The total time required to service customers at all counters.
    '''
    #lets say we have a shop with a number of empty ques
    counters = [0 for _ in range(queues)]
    
    # 1s: first customer goes to first counter in shop
    for customer in customers:
        counters[0] += customer
        
        # 2s: find counter with smallest que, sort, descending as default
        counters.sort()
        
        # 3s: after sort smallest is at index 0
        # 4s: iterate through customers, add to index 0
        
    # 5s: after all customes are added to ques, choose longest
    return max(counters)
    
if __name__ == "__main__":
    customers = [1,2,3,4,5]
    queues = 2
    print(computeCheckoutTime(customers, queues))