def solution(skill, skill_trees):
    skill_list = list(skill)
    
    skill_graph = {}
    for idx, sk in enumerate(skill_list):
        if sk == skill_list[-1]:
            skill_graph[sk] = []
        else:
            skill_graph[sk] = skill_list[idx+1:]
    
    answer = 0
    for skill_tree in skill_trees:
        skills = list(skill_tree)
        skill_book = []
        for sk in skills:
            if sk in skill_list:
                skill_book.append(sk)
        
        possible = True
        for idx, sk in enumerate(skill_book):
            if sk != skill_book[-1]:
                if idx == 0 and sk != skill_list[0]:
                    possible = False
                    break
                if skill_book[idx+1] not in skill_graph[sk]:
                    possible = False
                    break
        if possible == True:
            answer += 1
    
    return answer