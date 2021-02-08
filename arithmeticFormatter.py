def arithmetic_arranger(problems):
    dim_arr = []
    # adding restrictions
    for num in problems:
        try:
            eval(num)
        except:
            error = 'Error: Numbers must only contain digits.'
            return error
    # closed restriction
    for indata in problems:
        lst = []
        lst = indata.split()
        # adding restrictions
        if len(problems) > 5:
            error = 'Error: Too many problems.'
            return error
        elif len(lst[0]) > 4:
            error = 'Error: Numbers cannot be more than four digits.'
            return error
        elif len(lst[2]) > 4:
            error = 'Error: Numbers cannot be more than four digits.'
            return error
        if lst[1] == '+' or lst[1] == '-':
            pass
        else:
            error = "Error: Operator must be '+' or '-'."
            return error
        # closed restrictions
        rowAe = lst[0]
        rowBe = lst[1] + ' ' + lst[2]
        maxi = max(len(rowAe), len(rowBe))
        rowCe = max(len(rowAe), len(rowBe)) * '-'
        rowDe = eval(indata)
        minilst = [rowAe, rowBe, rowCe, rowDe]
        dim_arr.append(minilst)
    # finding length for right-aligned
    #this is my resultant array [['32', '+ 698', '-----', 730], ['3801', '- 2', '----', 3799], ['45', '+ 43', '----', 88], ['123', '+ 49', '----', 172]]
    rowA = str()
    rowB = str()
    rowC = str()
    rowD = str()
    pos = 4
    space = '    '
    for elements in dim_arr:
        maxA = max(len(elements[0]),len(elements[1]))-len(elements[0])
        maxB = max(len(elements[0]), len(elements[1])) - len(elements[1])
        maxD = max(len(elements[2]), len(str(elements[3]))) - len(str(elements[3]))
        rowA = rowA + maxA*' ' + str(elements[0])+ space
        rowB = rowB + maxB*' ' + str(elements[1]).rjust(maxB) + space
        rowC = rowC + str(elements[2]).rjust(4) + space
        rowD = rowD + maxD*' ' + str(elements[3]) + space
    arr = [str(rowA), str(rowB), str(rowC), str(rowD)]
    final = '0123'
    for count in arr:
        print(count)
    return space
'''
    print(rowA,rowB,rowC,rowD)
    print(dim_arr)
'''
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855","3801 - 2", "455 + 43", "123 + 49"]))
