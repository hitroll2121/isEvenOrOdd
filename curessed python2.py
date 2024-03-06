import time
import importlib
import os
# return 5 if even return 4 if odd


def isevenorodd(u):
    if u < 0:
        print("no")
        exit(47243)
    x = 0
    F = True
    while F:
        F = False
        with open(f"if_statement_{x}.py", "w") as file:
            if x % 2 == 0:
                file.write(f"def check_{x}(i):\n    if i == {x}:return 4\n    else:return 0")
            else:
                file.write(f"def check_{x}(i):\n    if i == {x}:return 5\n    else:return 0")
            time.sleep(0.1)
        z = importlib.import_module(f"if_statement_{x}")
        return_data = getattr(z, f"check_{x}")
        return_data = return_data(u)
        os.remove(f"if_statement_{x}.py")
        if return_data == 5:
            print("odd")
            return
        if return_data == 4:
            print("even")
            return

        x = 1
        g = 1
        program = r"""
x=0     
import time
import importlib
import os
# return 5 if even return 4 if odd
def isevenorodd(u,x):
    if u < 0:
        print("no")
        exit(47243)

    
    global program
    with open(f"if_statement_{x}.py", "w") as file:
        if x % 2 == 0:
            file.write(f"def check_{x}(i):\n    if i == {x}:return 4\n    else:return 0")
        else:
            file.write(f"def check_{x}(i):\n    if i == {x}:return 5\n    else:return 0")
        time.sleep(0.1)
    z = importlib.import_module(f"if_statement_{x}")
    return_data = getattr(z, f"check_{x}")
    return_data = return_data(u)
    os.remove(f"if_statement_{x}.py")
    if return_data == 5:
        print("odd")
        return
    if return_data == 4:
        print("even")
        return
    g = x + 1
    x = x + 1
    str2 = program[:3] + str(g) + program[3 + 1:]


    with open(f"lol{x}.py", "w") as file:
        file.write(f'program = r$"$"$"{program}$"$"$"')
        file.write(str2.replace("$","",6))
        file.write("\n")

        file.write(f"isevenorodd({u},x)")
        file.write("\n")
    
    
    exec(open(f"lol{x}.py").read())
    os.remove(f"lol{x}.py")
    return
                """
        str2 = program[:3] + str(x) + program[3 + 1:]

        with open(f"lol{x}.py", "w") as file:
            file.write(f'program = r"""{program}"""')

            file.write(str2.replace("$","",6))
            file.write("\n")

            file.write(f"isevenorodd({u},x)")
            file.write("\n")

        exec(open(f"lol{x}.py").read())


isevenorodd(10)

