import time

def time_track(func):
    def wrapper(*args, **kwarg):
        start_time = time.time()
        print("Start Execution........")
        func(*args, **kwarg)
        print("Stop the Execution......")
        stop_time = time.time()
        print(f"Total time spent on execution is {stop_time - start_time: .4f}")
    return wrapper

@time_track
def long_process():
    for _ in range(10**4):
        pass


long_process()

 
