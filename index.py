class ComplexCalculator:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexCalculator(real_sum, imaginary_sum)

    def subtract(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexCalculator(real_diff, imaginary_diff)

    def multiply(self, other):
        real_product = self.real * other.real - self.imaginary * other.imaginary
        imaginary_product = self.real * other.imaginary + self.imaginary * other.real
        return ComplexCalculator(real_product, imaginary_product)

    def divide(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_quotient = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_quotient = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexCalculator(real_quotient, imaginary_quotient)

def main():
    # Create complex numbers
    num1 = ComplexCalculator(2, 3)
    num2 = ComplexCalculator(4, 5)

    # Perform operations
    sum_result = num1.add(num2)
    diff_result = num1.subtract(num2)
    product_result = num1.multiply(num2)
    quotient_result = num1.divide(num2)

    # Print results
    print("Sum:", sum_result.real, "+", sum_result.imaginary, "i")
    print("Difference:", diff_result.real, "+", diff_result.imaginary, "i")
    print("Product:", product_result.real, "+", product_result.imaginary, "i")
    print("Quotient:", quotient_result.real, "+", quotient_result.imaginary, "i")

if __name__ == "__main__":
    main()