
def gradient_descent(grad_f, x0, learning_rate, n_steps):
    """
    Performs gradient descent to find the minimum of a function.
    """
    x = x0
    history = [x]

    for _ in range(n_steps):
        # Calculate the gradient at the current position
        gradient = grad_f(x)

        # Update x by moving against the gradient
        x = x - (learning_rate * gradient)

        # Record the new position
        history.append(x)

    return x, history
