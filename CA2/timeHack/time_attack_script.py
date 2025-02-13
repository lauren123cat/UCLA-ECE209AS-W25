# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        

    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.

        all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~ "
        max_attempts = 3  
        attempt = 0

        while attempt < max_attempts:
            curr_correct = "" 
            while True:
                timing_results = {}  
                
                for char in all_chars:
                    curr_pass = curr_correct + char
                    times = []

                    for _ in range(50):  
                        T1 = time.time()
                        result = check_password(curr_pass)
                        T2 = time.time()
                        times.append(T2 - T1)

                    # calculate median
                    times.sort()
                    median_time = times[len(times) // 2] 
                    timing_results[char] = median_time

                    if result == "Correct":
                        return curr_pass

                # get char using median
                best_char = max(timing_results, key=timing_results.get)
                curr_correct += best_char
                print(f"char: {best_char}")

                # prevents pw from becoming TOO long
                if len(curr_correct) > 12:
                    break 

            attempt += 1  
        
        return ""


soln = solution()
pwd = soln.getPassword()
print(pwd)

# Write Up
# Please explain your solution

"""
I'm exploiting time information to obtain the correct password.

I know that if a guessed char is correct, it returns false immediately so 
    Longer time -> good
    Shorter time -> bad

1) Try possible chars
2) Filter noise by using the median time -> gets best char

I made it so there's 3 attempts to get the right password so it doesn't run infinitely
"""