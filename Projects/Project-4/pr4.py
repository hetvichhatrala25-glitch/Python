dataset=[]

print("Welcome to the Data Analyser and Transformer Program\n")

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary(Built-in Function)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Filter Data by Threshold(Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics(Return Multiple Values)")
    print("7. Exit Program")
    
    choice = int(input("\n Please enter your choice:"))
    
    if choice == 1:
        print("\nInput Data")
        data= input("Enter data for a 1D array(separated by spaces):")
        dataset=[int(i) for i in data.split()]
        print("Data has been stored successfully !")
        
        