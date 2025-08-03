import grpc ## module to handle client-server communication
from concurrent import futures ## module for managing thread pool
import quadratic_calc_pb2 ## module generated using grpc
import quadratic_calc_pb2_grpc ## module generated using grpc for server side services
from quadratic_calc_python import quadratic_solver # custom python module to solve quadratic equations

""" Server side definition of the quadratic solver. This program will recieve information from the client, process it though the compute function, 
then return the results to the client"""

## Class to implement GRPC methods
class quadratic_CalculatorServicer(quadratic_calc_pb2_grpc.quadratic_CalculatorServicer):
    def Compute(self, request, context):## compute method is called when a request is made from the client
        result = quadratic_solver(request.num1,request.num2,request.num3) ## call the compute function of the three values and return the results
        return quadratic_calc_pb2.ComputeResponse(result=result)

## function to start the server
def serve(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) ## create server instance
    quadratic_calc_pb2_grpc.add_quadratic_CalculatorServicer_to_server(quadratic_CalculatorServicer(), server) ## add the service to the server
    server.add_insecure_port('[::]:50051') ## bind to network port
    server.start() ## start the server
    server.wait_for_termination() ## run the server until exit condition

if __name__ == '__main__':
    serve()