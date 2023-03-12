# python3

def parallel_processing(n, m, data):
    output = []

    threads = list(range(n))
    timee = [0] * n
    i=0
    pabeigts_process = False
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    while not pabeigts_process:
        if i>=m:
            pabeigts_process = True
        else:
            time = data[i]
            if threads:
                tr = threads.pop(0)
                sakums = timee[tr]
                if output:
                    sakums = max(sakums, output[-1][1])
                output.append((tr, sakums))
                timee[tr] = sakums + time

                if i < n-1 and i < m-1:
                    threads.append(tr)
            else:
            for j in range(n):
                if timee[j] <= timee[threads[0]]:
                    output.append((j, timee[j]))
                    timee[j] += time
                    threads[0] = j
                    break
        i += 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    if not (1<=n<10**5):
        print("error")
        return
    if not (1<=m<=10**5):
        print("error")
        return
    for time in data:
        if time<0 or time>10**9:
            print("error")
            return []



    #n = 0
    #m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)

    for output in result:
        print(output[0], output[1])


    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
