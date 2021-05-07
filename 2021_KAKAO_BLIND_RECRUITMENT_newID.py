import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    print("1: ", new_id)
    
    # 2
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    print("2: ", new_id)
    
    # 3
    det = True
    while det:
        prev = new_id
        new_id = new_id.replace('..', '.')
        if prev == new_id:
            det = False
    print("3: ", new_id)
    
    # 4
    new_id = list(new_id)
    print(new_id[0])
    print(new_id[-1])
    if new_id[0] == '.':
        print('1Pass', new_id)
        del new_id[0]
    if new_id[-1] == '.':
        print('2Pass', new_id)
        #del new_id[-1]
    #new_id = new_id.join
    print("4: ", new_id)
    
    # 5
    
    answer = ''
    return answer