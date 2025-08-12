# Backend 
This repo contains a set of software tools to ease the development of HDL projects.
**Tools:**
- HDLtool
## HDLtool
HDLtool is a terminal tool to build ASIC/FPGA projects. It interfaces other tools to compile and simulate the project files. HDLtool relies on yaml files to point to the diferent sources of the project.
**Current supported tools:**
- ghdl
## Usage example
Compile the project described in project.yaml, elaborate and simulate with the default top.
```
hdltool -d <project_path>/project.yaml -a -e -s
```
Compile the project described in project.yaml, elaborate and simulate other_top unit
```
hdltool -d <project_path>/project.yaml -a -e -s other_top
```
Compile the project described in project.yaml, elaborate and simulate with the default top.
_It is also possible to pass extra options to the tool in use if the flags are used individually_
## Project Descriptor
HDLtool relies on yaml files to point to the sources of the project.
```
top : <top_unit_name>
src:
    pkg: <list of packages>
    rtl: <list of design files>
sim:
    test_1 : { tb : "<tb_file>", sim_flags: "<extra_simulation_flags>"}
    test_2: { tb : "<tb_file>", sim_flags: "<extra_simulation_flags>"}
    test_3 : { tb : "<tb_file>", sim_flags: "<extra_simulation_flags>"}
    ...
deps: <list of paths to other project descriptors>
```
## Dependencies
- Python3.12
- argparse
- Pyaml
- ghdl 5.0 or newer

## ToDo
- Integrate Vivado Simulator
- It would be nice to separate sim function from cocotb simulation
- Backend flow with at least one tool?
- Veification flow
