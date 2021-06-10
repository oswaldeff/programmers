import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    
    # 3
    det = True
    while det:
        prev = new_id
        new_id = new_id.replace('..', '.')
        if prev == new_id:
            det = False
    
    # 4
    det = True
    while det:
        front = new_id[:1]
        if front == '.':
            new_id = new_id[1:]
        end = new_id[-1:]
        if end == '.':
            new_id = new_id[:-1]
        if front != '.' and end != '.':
            det = False
    
    # 5
    if len(new_id) == 0:
        new_id += 'a'
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    
    # 7
    det = True
    while det:
        if len(new_id) <= 2:
            new_id += new_id[-1:]
        if len(new_id) > 2:
            det = False
    
    answer = new_id
    return answer
