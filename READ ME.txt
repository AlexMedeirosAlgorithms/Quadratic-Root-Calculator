CSC6304 Project 01 Documentation
Alexander Medeiros 11/04/2024

This document serves as the instructions for how to build and use the quadratic calculator using grpc and python.


Quadratic formula implementation:

This program uses the quadratic formula to calculate the solutions of a polynomal equation. This computational method is defined in the file "quadratic_calc_python.py"

The method takes 3 seperate real number values as input, and returns a string in the format: result = ('root 1', 'root 2')


Client and server implementation

Steps:

1.) Navigate to the parent directory where the project is stored " cd ~/project01_AMedeiros"

2.) The quadratic_calc.proto file is run to construct the grpc code, which is produced using the console command (this is already done for you)
	"python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. quadratic_calc.proto"

- Then, the server and client are run.

3.) In seperate terminals run the commands in the following order:

	"python quadratic_calc_server.py"

4.) in a new terminal, run:

	"python quadratic_calc_client.py"

In the client terminal, instructions will be printed on how to use the calculator. 

Enter the values as you are prompted and press enter to submit the value. 

When each of the values are submitted, the server will compute the result and return it to the client and print to display for the user. Then the client will close.