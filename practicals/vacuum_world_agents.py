# Vacuum Cleaner World

# Environment
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# -----------------------------
# Simple Reflex Agent
# -----------------------------
def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

def run_simple_reflex():
    print("Simple Reflex Agent\n")
    location = "A"

    for i in range(4):
        status = environment[location]
        action = simple_reflex_agent(location, status)

        print(f"Location: {location} | Status: {status} -> Action: {action}")

        if action == "Suck":
            environment[location] = "Clean"

        elif action == "Right":
            location = "B"

        elif action == "Left":
            location = "A"

    print("\nFinal Environment:", environment)


# -----------------------------
# Model Based Agent
# -----------------------------
def model_based_agent(location, status, model):
    model[location] = status

    if model['A'] == "Clean" and model['B'] == "Clean":
        return "NoOp"
    elif status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

def run_model_based():
    print("\nModel Based Agent\n")

    model = {'A': None, 'B': None}
    location = "A"

    for i in range(6):
        status = environment[location]
        action = model_based_agent(location, status, model)

        print(f"Location: {location} | Status: {status} -> Action: {action}")

        if action == "Suck":
            environment[location] = "Clean"

        elif action == "Right":
            location = "B"

        elif action == "Left":
            location = "A"

        elif action == "NoOp":
            break

    print("\nFinal Environment:", environment)


# Run both agents
run_simple_reflex()
run_model_based()