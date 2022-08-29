'''
Question: Given a list L of video names and their watch rates, write a function that will return 
the videos with the top 10 watch rates. Video names may appear more than once.

Example:
L = [(‘abc’, 10), (‘def’, 15), (‘ghi’, 10), (‘abc’, 12), …, (‘xyz’, 100)]

The function should return [‘xyz’, ‘abc’, …, ‘def’, ‘ghi’]
*/


Note that the original list is also sorted if .sort method of list is called.
If you do not want the original list to be sorted then you may want to call sorted function and pass in list as a parameter as below:
'''

def ranked_games(L):
    sorted_list = sorted(L, key = lambda x:x[1], reverse=True) #sort by value
    print("Sorted by Value Descending",[i for i, _ in sorted_list[:10]]) # [:10] for slicing 10 sorted values

# calling the function
my_list = [('abc',10),('def',15),('ghi',10),('abc', 12),('xyz',100)]
ranked_games(my_list)
print('Original List: ', my_list)
