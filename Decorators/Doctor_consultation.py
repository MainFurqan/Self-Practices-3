import time

def logs(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' at {time.ctime()}.")
        return func(*args, **kwargs)
    return wrapper

def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time spent on execution: {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@logs
@track_time
def doctor_consul(patient_name):
    print(f"Doctor consulting the {patient_name}.......")
    print(f"Doctor given the prescription to {patient_name}.")

# Call the function
doctor_consul("Hamza")
