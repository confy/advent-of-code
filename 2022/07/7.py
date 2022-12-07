with open('./2022/07/input.txt') as f:
    text = f.read()

files = {}
folders = set()
parents = []

for line in text.split('\n'):
    if line.startswith('$'):
        if line.startswith('$ cd'):
            new_dir = line[5:]
            if new_dir == '..' and len(parents) > 0:
                parents.pop(-1)
            elif new_dir == '/':
                parents = []
            else:
                parents.extend(new_dir.split('/'))
    else:
        size, name = line.split(' ')
        if size == 'dir':
            continue
        size = int(size)
        files['/'.join(parents+[name])] = size
    folders.add('/'.join(parents))


part_1 = 0
fsizes = {}

for folder in folders:
    fsize = sum(value for file, value in files.items()
                if file.startswith(folder))
    if fsize <= 100000:
        part_1 += fsize
    fsizes[folder] = fsize
    
print(part_1)
print(min((v for v in fsizes.values()if 70000000-fsizes['']+v >= 30000000)))
