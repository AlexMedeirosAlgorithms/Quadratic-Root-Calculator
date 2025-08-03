import grpc
import quadratic_calc_pb2
import quadratic_calc_pb2_grpc

""" Method to run the client. The client will prompt for user inter of 3 values. The values will be passed to the server to run the computation, then print the response."""

## Method to handle client requests
def run(num1, num2, num3): 
    with grpc.insecure_channel('localhost:50051') as channel: ## establish communication channel
        stub = quadratic_calc_pb2_grpc.quadratic_CalculatorStub(channel) ## create a stub for the client to make requests to the server
        response = stub.Compute(quadratic_calc_pb2.ComputeRequest(num1=num1, num2=num2, num3=num3)) ## send the values to the server and store response
    print(f"Solutions for x = {response.result}") ## print the result of the computation


## Method to check if an input is a number
def check_isnum(string):
    try:
        float(string) ## attempt to convert value to float, if possible input is a number and return true
        return True
    except ValueError: ## if this fails, input is not a number and contains non-numeric characters, return false
        return False

## Main method
def main(): 

    ## Get user input 
    print("For a quadratic equation you wish to solve that is in the form of ax^2 + bx + c = 0, enter values 'a','b','c' in the format of integer or float ")
    a = input("Please input first number 'a' and press enter: ") ## variable to store first value
    b = input("Please input second number 'b' and press enter: ") ## variable to store second value
    c = input("Please input third number 'c' and press enter: ") ## variable to store third value

    ## check if the input is a number 
    if check_isnum(a) is False or check_isnum(b) is False or check_isnum(c) is False: ## when false, promp the user for new input
        print("Not a valid input, please enter valid Real numbers")
        main()
    else:
        run(float(a),float(b),float(c)) ## when true, run the request


if __name__ == '__main__':
   main() ## run the main