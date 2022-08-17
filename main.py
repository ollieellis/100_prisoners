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

def main():
    n = 4
    all_combos = gen_all_box_combinations(n)
    # for i in range(n-1):
    #     all_combos = add_all_to_each_array(all_combos, n)

    print(all_combos)
    print(np.shape(all_combos))
    

if __name__ == "__main__":
    main()
