data = {}
raw = None
current_dir = None
previous_dirs = []

with open('day7/input.txt') as f:
    for l in f:
        l = l.strip()
        l = l.split(' ')
        if l[0] == '$':
            if l[1] == 'cd':
                if l[2] == '/':
                    current_dir = data
                    previous_dirs = []
                elif l[2] == '..':
                    current_dir = previous_dirs.pop()
                else:
                    new_dir = {}
                    current_dir[l[2]] = new_dir
                    previous_dirs.append(current_dir)
                    current_dir = new_dir
        else:
            if l[0] != 'dir':
                current_dir[l[1]] = int(l[0])

dir_sizes = []

def dir_size(dir_struct):
    global dir_sizes
    total_size = 0
    for e in dir_struct:
        if type(dir_struct[e]) == dict:
            total_size += dir_size(dir_struct[e])
        else:
            total_size += dir_struct[e]
    dir_sizes.append(total_size)
    return total_size

dir_size(data)

ans = 0
for d in dir_sizes:
    if d <= 100000:
        ans += d

print(ans)
