# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/leh/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/leh/catkin_ws/build

# Include any dependencies generated for this target.
include mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/depend.make

# Include the progress variables for this target.
include mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/progress.make

# Include the compile flags for this target's objects.
include mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/flags.make

mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o: mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/flags.make
mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o: /home/leh/catkin_ws/src/mservo_manipulator_control-main/ethercat_test/src/ecat_dc.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/leh/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o"
	cd /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o   -c /home/leh/catkin_ws/src/mservo_manipulator_control-main/ethercat_test/src/ecat_dc.c

mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.i"
	cd /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/leh/catkin_ws/src/mservo_manipulator_control-main/ethercat_test/src/ecat_dc.c > CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.i

mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.s"
	cd /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/leh/catkin_ws/src/mservo_manipulator_control-main/ethercat_test/src/ecat_dc.c -o CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.s

# Object files for target ECAT_DC
ECAT_DC_OBJECTS = \
"CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o"

# External object files for target ECAT_DC
ECAT_DC_EXTERNAL_OBJECTS =

/home/leh/catkin_ws/devel/lib/libECAT_DC.so: mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/src/ecat_dc.c.o
/home/leh/catkin_ws/devel/lib/libECAT_DC.so: mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/build.make
/home/leh/catkin_ws/devel/lib/libECAT_DC.so: mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/leh/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library /home/leh/catkin_ws/devel/lib/libECAT_DC.so"
	cd /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ECAT_DC.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/build: /home/leh/catkin_ws/devel/lib/libECAT_DC.so

.PHONY : mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/build

mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/clean:
	cd /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test && $(CMAKE_COMMAND) -P CMakeFiles/ECAT_DC.dir/cmake_clean.cmake
.PHONY : mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/clean

mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/depend:
	cd /home/leh/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leh/catkin_ws/src /home/leh/catkin_ws/src/mservo_manipulator_control-main/ethercat_test /home/leh/catkin_ws/build /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test /home/leh/catkin_ws/build/mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mservo_manipulator_control-main/ethercat_test/CMakeFiles/ECAT_DC.dir/depend
