def f(x):
    return x**3 - x - 2  # Example function

def f_prime(x):
    return 3*x**2 - 1  # Derivative of the function

def newton_raphson(x0, tol=1e-6, max_iter=100):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        fpxn = f_prime(xn)
        if fpxn == 0:
            print("Zero derivative. No solution found.")
            return None
        xn_next = xn - fxn / fpxn
        if abs(xn_next - xn) < tol:
            print(f"Found solution after {n+1} iterations.")
            return xn_next
        xn = xn_next
    print("Exceeded maximum iterations. No solution found.")
    return None

# Example usage
initial_guess = 1.5
root = newton_raphson(initial_guess)
print("Root:", root)
