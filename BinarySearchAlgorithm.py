def BinarySearchAlgorithm(List, Left, Right, Objective):
    while (Left <= Right):
        Center = int(Left +(Right - Left) / 2)
        if (objective == List[Center]):
            return ("The number is {}".format(List[Center]))
        if (List[Center] > Objective):
                Right = Center - 1
        else:
            left = centre + 1 
    return ("Unable to find the selected number")

List = [4, 12, 25, 39, 40, 47]
Objective = 25
Length = len(Llista)

Result = BinarySearchAlgorithm(List, 0, Length - 1, Objective)


print(Result)
