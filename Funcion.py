def funcion(A, B):
    S = []
    if (type(A) == int and type(B) == int):
        x = A
        y = B
        if (A >= B):
            S1 = (x - y)
            S2 = (x + y)
            S3 = (x * y)
            S = S1, S2, S3
        else:
            S = -1
    else:
        S = -1
    return S


W = funcion(4, 4)
