def solution(info, query):
    applicants_graph = {}
    for idx, i in enumerate(info):
        applicants_graph[idx] = {}
        applicants_graph[idx]["language"] = i.split(" ")[0]
        applicants_graph[idx]["position"] = i.split(" ")[1]
        applicants_graph[idx]["career"] = i.split(" ")[2]
        applicants_graph[idx]["soulfood"] = i.split(" ")[3]
        applicants_graph[idx]["score"] = i.split(" ")[4]
        
    answer = []
    for q in query:
        applicants = [x for x in range(len(info))]
        passers = []
        data = (q.replace(" and ", " ")).split(" ")
        while applicants:
            applicant = applicants.pop(0)
            if data[0] != '-' and applicants_graph[applicant]["language"] != data[0]:
                continue
            if data[1] != '-' and applicants_graph[applicant]["position"] != data[1]:
                continue
            if data[2] != '-' and applicants_graph[applicant]["career"] != data[2]:
                continue
            if data[3] != '-' and applicants_graph[applicant]["soulfood"] != data[3]:
                continue
            if int(applicants_graph[applicant]["score"]) < int(data[4]):
                continue
            else:
                passers.append(applicant)
        answer.append(len(passers))
    return answer