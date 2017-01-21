__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import subprocess
from time import time

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------

SEP = "*"*100
OK = "OK"
WRONG = "WRONG"
ERR = "ERR"
TIME = "OUT-OF-TIME"

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def check_script(orig_script_name, name_base):
    inp_file_name = name_base + "_inp.txt"
    out_file_name = name_base + "_out.txt"

    print("\n"*5)
    print("Running tests for " + orig_script_name)
    print()

    status_count = {
        OK: 0,
        WRONG: 0,
        ERR: 0,
        TIME: 0
    }

    inp_file = None
    out_file = None
    try:
        inp_file = open(inp_file_name, 'r')
        out_file = open(out_file_name, 'r')

        inp_lines = inp_file.readlines()
        out_lines = out_file.readlines()
        if len(inp_lines) != len(out_lines):
            raise Exception("Number of inputs != number of outputs")
        total = len(inp_lines)

        for i in range(total):
            print(SEP)
            print("* Test case " + str(i + 1))
            print(SEP)
            inp_line = inp_lines[i].strip()
            out_line = out_lines[i].strip()
            time_limit = int(out_line.split(':')[0])
            out_line = out_line[out_line.find(":") + 1:]

            print("Input         : '" + inp_line + "'")
            print("Desired output: '" + out_line + "'")

            print("Executing ...")

            before = time()
            p = subprocess.Popen(['python3', orig_script_name] + inp_line.split(' '),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = p.communicate()
            after = time()
            exec_time = after - before

            print("Execution time: " + str(round(after - before, 5)) + " sec")

            out = out.decode("utf-8").strip()
            err = err.decode("utf-8")

            print()
            if err != "":
                print("ERROR")
                print("Your program raised the following error: " + err)
                status_count[ERR] += 1
            elif out != out_line:
                print("WRONG")
                print("Your program gave a wrong output: '" + out + "'")
                status_count[WRONG] += 1
            elif exec_time > time_limit:
                print("OUT-OF-TIME")
                print("Your program exceeded the time limit of " + str(time_limit) + " seconds")
                status_count[TIME] += 1
            else:
                print("OK")
                status_count[OK] += 1
            print()
    except:
        print("There was error running the check. Please notify Fero")
        return None
    finally:
        if inp_file is not None:
            inp_file.close()
        if out_file is not None:
            out_file.close()

    print(SEP)
    print()
    if status_count[OK] == total:
        print("Results: all OK")
    else:
        print("Results: ")
        statuses = [OK, WRONG, TIME, ERR]
        for status in statuses:
            print("  " + status.ljust(12) + ": " + str(status_count[status]))
    print()

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main(argv):
    orig_script_name = argv[0]
    name_base = orig_script_name.lower()
    name_base = name_base.replace(".py", "")
    check_script(orig_script_name, name_base)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
