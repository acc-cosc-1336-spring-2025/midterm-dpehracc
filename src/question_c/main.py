#add import
from src.question_c.question_c import use_local_variable

def main():
    num = 100
    print("Initial value of num =", num)
    use_local_variable(num)
    print("Value after calling use_local_variable, num =", num)

main()