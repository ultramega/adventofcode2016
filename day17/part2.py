from hashlib import md5

inp = 'yjjvjgan'
openChars = 'bcdef'

def getValidDirections(x, y, path):
    hash = md5(bytes(inp + ''.join(path), 'utf-8')).hexdigest()
    dirs = []
    if y > 0 and hash[0] in openChars:
        dirs.append((x, y - 1, path + tuple('U')))
    if y < 3 and hash[1] in openChars:
        dirs.append((x, y + 1, path + tuple('D')))
    if x > 0 and hash[2] in openChars:
        dirs.append((x - 1, y, path + tuple('L')))
    if x < 3 and hash[3] in openChars:
        dirs.append((x + 1, y, path + tuple('R')))
    return dirs

valid = set()
stack = [(0, 0, ())]
while stack:
    state = stack.pop()
    if state[0] == state[1] == 3:
        valid.add(''.join(state[2]))
        continue
    stack += getValidDirections(*state)

print(max([len(x) for x in valid]))
input()
