#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    output = dir(hidden_4)
    for i in output:
        if i[:2] != "__":
            print(i)
