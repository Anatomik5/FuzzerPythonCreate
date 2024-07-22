import coverage
import fuzzer
import os
import time
def print_coverage_report(cov):
    os.system('cls' if os.name == 'nt' else 'clear')
    cov.report()
    time.sleep(2)
#start of test function
def process_array(arr):
    result = []
    if not arr:
        return result 
    if len(arr) % 2 == 0:
        print("Array length is even.")
    else:
        print("Array length is odd.")
    if len(result)>20:
        print(1)
    if len(result)>10:
        print(1)
    if len(result)>100:
        print(1)
    for i, num in enumerate(arr):
        if num % 2 == 0:
            if num % 4 == 0:
                result.append(num // 2)
            else:
                result.append(num * 2)
        else:
            if num < 0:
                result.append(abs(num))
            elif num < 10:
                result.append(num + 10)
            else:
                result.append(num - 10)
        if i % 3 == 0:
            result.append(num * 3)
        elif i % 3 == 1:
            result.append(num + 5)
        elif i % 3 == 2:
            result.append(num - 7)
    sum_result = sum(result)
    if sum_result > 100:
        1+1
    if sum_result > 50:
        1+1
    if sum_result > 0:
        1+1
    if any(x < 0 for x in result):
        print("Warning: Negative values found in the result.")
    return result
#end of test function

def main():    
    arr = fuzz.mutator.mutate() 
    process_array(arr)
if __name__ == "__main__":
    fuzz = fuzzer.MyFuzzer(10, "int_arr")
    cov = coverage.Coverage()
    cov.start()
    try:
        while True:
            main()
            cov.stop()
            cov.save()
            print_coverage_report(cov)
            cov.start()
    except KeyboardInterrupt:
        cov.stop()
        cov.save()
        print_coverage_report(cov)
