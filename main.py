import numpy as np

def gen_all_box_combinations(n: int) -> np.array:
    # starting_arrays = np.reshape(np.arange(n), (n,1))
    all_combos = np.reshape(np.arange(n), (n,1))
    for i in range(n-1):
        all_combos = add_all_to_each_array(all_combos, n)
    return all_combos

def append_to_each_array(twoD_array, item_to_append):
    appended_arrays = np.array([])
    for i, array in enumerate(twoD_array): 
        concatinated_array = np.append(array, item_to_append)
        if(i == 0): #get rid of this, initilise the size of array above and then just append 
            appended_arrays = np.array([concatinated_array])
        else:
            appended_arrays = np.append(appended_arrays, [concatinated_array], axis=0)
    return appended_arrays

def add_all_to_each_array(twoD_array, max_value):
    new_arrays = np.array([])
    for i in range(max_value):
        if(i == 0):
            new_arrays = append_to_each_array(twoD_array, i)
        else: 
            new_arrays = np.append(new_arrays, append_to_each_array(twoD_array, i), axis=0)
    return new_arrays

def next_number_solution(prisoner_num, box_array):
    prevously_visited = set()
    stop_searching = False
    box_2_check = prisoner_num
    num_opened = 0
    while(not stop_searching):
        num_opened += 1
        stop_searching, box_found = check_stop_searching(num_opened, prisoner_num, prevously_visited, box_array, box_2_check)
        prevously_visited.add(box_2_check)
        box_2_check = box_array[box_2_check]
        print(box_2_check)
    print(box_found)

def check_stop_searching(num_opened, prisoner_num, boxes_visited, box_array, current_position):
    if num_opened >= np.floor(np.shape(box_array)[0]/2):
        return True, False
    if box_array[current_position] == prisoner_num:
        return True, True
    if current_position in boxes_visited: #this is just to stop early as we will just cycle
        return True, False
    return False, False




def main():
    n = 4
    all_combos = gen_all_box_combinations(n)
    # for i in range(n-1):
    #     all_combos = add_all_to_each_array(all_combos, n)

    print(all_combos)
    print(np.shape(all_combos))
    
    test_case = np.array([7, 1, 3, 6, 5, 2, 0, 4])
    
    for i in range(6):
        print("i: = ", i, "     ", test_case)
        next_number_solution(i, test_case)
    
    
    

if __name__ == "__main__":
    main()
    
  
