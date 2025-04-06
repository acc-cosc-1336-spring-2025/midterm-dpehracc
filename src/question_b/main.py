#add import

from src.question_b.question_b import get_assessment_value, get_tax_assessed

def main():
    print("Property Tax Assessment")

    continuation = "y"
    while continuation.lower() == "y":
        value = float(input("Enter the actual value of the property: $"))

        assessment = get_assessment_value(value)
        tax = get_tax_assessed(assessment)

        print(f"Assessment value: ${assessment:,.2f}")
        print(f"Property tax:     ${tax:,.2f}")

        continuation = input("Would you like to calculate another? (y/n): ")

if __name__ == "__main__":
    main()