def daycal(date):
    year,month,day = map(int, date.split('.'))
    return year*12*28+month*28+day
def solution(today, terms, privacies):
    ans = []
    today = daycal(today)
    for i in range(len(privacies)):
        date,type = privacies[i].split()
        for term in terms:
            if type == term.split()[0]:
                if daycal(date)+int(term.split()[1])*28 <= today:
                    ans.append(i+1)
    return ans
