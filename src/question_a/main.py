#add import
from src.question_a.question_a import get_fahrenheit

def main():
    print("Celsius   Fahrenheit")
    for c in range(0, 21):
        f = get_fahrenheit(c)
        print(f"{c:<8}   {f:.1f}")

if __name__ == "__main__":
    main()