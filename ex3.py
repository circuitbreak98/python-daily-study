def run_timing():
    s = 0
    cnt = 0
    while True:
        run = input("Enter 10 km run time: ")
        if not run:
            print(f"Average of {s/cnt}, over {cnt} runs")
            break
        else:
            s += float(run)
            cnt +=1 

run_timing()
