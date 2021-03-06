#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for y in range(0, list_length):
        try:
            result = my_list_1[y] / my_list_2[y]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except:
            result = 0
        finally:
            list.append(result)
    return list