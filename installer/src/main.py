# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/LGRAM_auto_processer/installer/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import

# flow
from method.flow import FlowProcess


# ----------------------------------------------------------------------------------
# **********************************************************************************

def main():
    main_flow = FlowProcess()
    main_flow.parallel_process()

# **********************************************************************************

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------
