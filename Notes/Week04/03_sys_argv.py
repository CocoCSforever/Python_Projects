import sys
#stands for the operating system
#terminal is the interface of system
#system execuate the python process
#access the argument vector(a list of agrs)
#if python3 03_sys_argv.py, the name of the script "03_sys_argv.py" is the first argument
#the memory will not last any longer than the life span of the script execuation
#if we use REPL:
# >>>import sys
# >>>print(sys.argv)
# ['']



def main():
    #if we declare sys.argv[1]="Hello", and try to print it, IndexError: Out of index
    #but if we add one user arg, and print it again, we cannot reassign the value if we already declare it as "Hello"
    print(sys.argv)
    #sys.argv[1]==the first argu after the name of the script


main()