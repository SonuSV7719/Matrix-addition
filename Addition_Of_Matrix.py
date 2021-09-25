def matAddition(mat1, mat2, r, c):
    '''
    mat = matrix
    r= Number of rows
    c= Number of columns
    '''
    addition = []
    for i in range(r):
        subList = []
        for j in range(c):
            sum = mat1[i][j]+mat2[i][j]
            subList.append(sum)
        addition.append(subList)
    return addition   


def cMatrix(mat, r, c):
    for i in range(r):
            row = []
            for j in range(c):
                element = int(input("Enter elements of matrix: "))
                row.append(element)
            mat.append(row)

mat1 = []
mat2 = []
decision = 0
loop = True

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))



while loop:
    if r== c:
        choice = input("-------------------------------------Steps---------------------------------\n**** Enter 1 to start *****\nStep 1)Create 1st matrix\nStep 2)Create 2nd matrix\nStep 3)Addition of both the matrix\n")
    
        if choice == "1":
            cMatrix(mat1, r, c)
            print("You entered in step 2 create another matrix")
            choice = "2"

        if choice == "2":
            cMatrix(mat2, r, c)
            print("You entered in step 3 addition of matrix given below: \n")
            choice = "3"

        if choice == "3":
            matrix = matAddition(mat1, mat2, r, c)
            for i in range(r):
                for j in range(c):
                    print(matrix[i][j],end="\t")
                print("\n")
            loop = False
            # choice = input("1)Enter 1 for create 1st matrix\n2)Enter 2 for create 2nd matrix\n3)Enter 3 for addition of both the matrix\n")
    
    else:
        print("Addition not possible as rows and columns are not equal")
        loop = False
