#balance or unbalanced
#any open bracket push into stack until same symbol matches
#initallyy empty
def check(s):
    stack=[]
    openings=['[','(','{']
    brackets={
        '(':')',
        '[':']',
        '{':'}'
    }
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack:
                top=stack.pop()
                if brackets[top]!=i:
                    return "No"
            else:
                return "No"
    if stack:
        return "No"
    else:
        return "Yes"
s='{[()]}'
print(check(s))

