def nestedListContains(NL, target):
    if isinstance(NL, int):
        if NL == target:
            return True
     else:

        for i in range(len(NL)):
            if nestedListContains(NL[i], target) == True:
                return True
    return False
