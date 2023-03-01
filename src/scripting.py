import argparse

def input_parse():
    #initialie the parser
    parser = argparse.ArgumentParser()
    # add argument
    parser.add_argument("--name", type=str, default="Kevin")
    parser.add_argument("--age", type=int, required = True)
    # parse the arguments from command line
    args = parser.parse_args()
    #return the parsed arguments
    return args

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old!")

def main():
    #run input parse to get name and age
    args = input_parse()
    #pass name and age to hello()
    hello(args.name, args.age)

#only if this module is run from the commandline, the code should be run. It should if its run in another script
if __name__=="__main__":
    main()