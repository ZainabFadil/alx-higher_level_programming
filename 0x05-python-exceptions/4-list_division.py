#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    iteration = max(len(my_list_1), len(my_list_2))
    minim = min(len(my_list_1), len(my_list_2))
    final_list = []
    for i in range(iteration):
        try:
            try:
                x = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
                final_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                final_list.append(0)
        except IndexError:
            print("out of range")
            for i in range(iteration - minim):
                final_list.append(0)
        finally:
            return final_list
