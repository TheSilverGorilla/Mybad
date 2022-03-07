x = [1,2,1,2,-1,-2,-1,-2]
y = [2,1,-2,-1,2,1,-2,-1]
d = {}
final_list = []
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
#arr is a sample to see if the code works.
def get_knight_pos(start_pos, arr):
    for i in range(8):
        X = start_pos[0] + x[i]
        Y = start_pos[1] + y[i]
        if X>=0 and Y>=0:
           try:
               d.update({arr[X][Y]: [X,Y]})
           except:
               pass
final_list.append(arr[0][0])
get_knight_pos([0,0], arr)

def n():
    max_knight= sorted(d.keys())[-1]
    max_coords = d.get(max_knight)
    final_list.append(max_knight)
    d.clear()
    get_knight_pos(max_coords, arr)
    max_knight= sorted(d.keys())[-1]
    max_coords = d.get(max_knight)
    final_list.append(max_knight)
    d.clear()
    get_knight_pos(max_coords, arr)
    if max_knight == final_list[len(final_list)-1]:
        max_knight = sorted(d.keys())[-2]
    else:
        pass
n()
while len(final_list)<11:
    max_knight= sorted(d.keys())[-1]
    if max_knight == final_list[len(final_list)-2]:
        max_knight = sorted(d.keys())[-2]
    else:
        pass
    max_coords = d.get(max_knight)
    final_list.append(max_knight)
    d.clear()
    get_knight_pos(max_coords, arr)

print(final_list)
