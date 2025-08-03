import math

""" A method to solve for the roots of quadratic equation given the polynomial coefficients """

def quadratic_solver(a,b,c):
    """ Logic to handle solving quadric equation problems
    
    inputs - (int) recieves the polynomial coefficients and stores them in varaibles 'a','b','c'
    outputs - (int) returns the positive and negative products in a tuple converted to a string for universal processing when dealing with imaginary roots
    """
    
    # store discriminant for comparison
    alpha = b*b-(4*a*c)
    root_alpha = math.sqrt(abs(alpha))

    ## check if root are real
    if alpha > 0: # roots are real and distinct
        # (print("real,unequal roots"))
        x_pos  = (-b + root_alpha) / (2*a)
        x_neg = (-b - root_alpha) / (2*a)
    
        output = (x_pos,x_neg)

    elif alpha == 0: # roots are real and equal
        # print("real, equal roots")
        x_pos  = (-b + root_alpha) / (2*a)
        x_neg = (-b - root_alpha) / (2*a)
    
        output = (x_pos,x_neg)

    else: # roots are complex
        # print("complex roots")
        x_pos = str(f"{-b / (2*a)}") + '+' + str(f"{root_alpha / (2*a)}") +'i'
        x_neg = str(f"{-b / (2*a)}") + '-' + str(f"{root_alpha / (2*a)}") +'i'
        output = (x_pos,x_neg)

    return str(output)
