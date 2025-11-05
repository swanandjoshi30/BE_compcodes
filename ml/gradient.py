def f(x):
    return (x + 3)**2

def df(x):
    return 2 * (x + 3)

# Step 2: Initialize parameters
x = 2                # starting point
learning_rate = 0.1  # step size
epochs = 30          # number of iterations

# Lists to store values for plotting
x_values = [x]
f_x_values = [f(x)]

# Step 3: Gradient Descent loop
for i in range(epochs):
    grad = df(x)                    # compute gradient
    x = x - learning_rate * grad    # update x
    x_values.append(x)
    f_x_values.append(f(x))
    print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")

print("\nLocal minima occurs at x =", round(x, 4))
print("Minimum value of function =", round(f(x), 4))

# Step 4: Plotting the results (Simplified)
plt.figure(figsize=(8, 5))
plt.scatter(x_values, f_x_values, color='b', label='Gradient Descent Steps')
plt.title('Gradient Descent Path (Simplified)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
