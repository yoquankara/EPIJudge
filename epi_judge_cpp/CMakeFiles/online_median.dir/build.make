# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.10.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.10.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# Include any dependencies generated for this target.
include CMakeFiles/online_median.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/online_median.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/online_median.dir/flags.make

CMakeFiles/online_median.dir/online_median.cc.o: CMakeFiles/online_median.dir/flags.make
CMakeFiles/online_median.dir/online_median.cc.o: online_median.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/online_median.dir/online_median.cc.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/online_median.dir/online_median.cc.o -c "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/online_median.cc"

CMakeFiles/online_median.dir/online_median.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/online_median.dir/online_median.cc.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/online_median.cc" > CMakeFiles/online_median.dir/online_median.cc.i

CMakeFiles/online_median.dir/online_median.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/online_median.dir/online_median.cc.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/online_median.cc" -o CMakeFiles/online_median.dir/online_median.cc.s

CMakeFiles/online_median.dir/online_median.cc.o.requires:

.PHONY : CMakeFiles/online_median.dir/online_median.cc.o.requires

CMakeFiles/online_median.dir/online_median.cc.o.provides: CMakeFiles/online_median.dir/online_median.cc.o.requires
	$(MAKE) -f CMakeFiles/online_median.dir/build.make CMakeFiles/online_median.dir/online_median.cc.o.provides.build
.PHONY : CMakeFiles/online_median.dir/online_median.cc.o.provides

CMakeFiles/online_median.dir/online_median.cc.o.provides.build: CMakeFiles/online_median.dir/online_median.cc.o


# Object files for target online_median
online_median_OBJECTS = \
"CMakeFiles/online_median.dir/online_median.cc.o"

# External object files for target online_median
online_median_EXTERNAL_OBJECTS =

online_median: CMakeFiles/online_median.dir/online_median.cc.o
online_median: CMakeFiles/online_median.dir/build.make
online_median: CMakeFiles/online_median.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable online_median"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/online_median.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/online_median.dir/build: online_median

.PHONY : CMakeFiles/online_median.dir/build

CMakeFiles/online_median.dir/requires: CMakeFiles/online_median.dir/online_median.cc.o.requires

.PHONY : CMakeFiles/online_median.dir/requires

CMakeFiles/online_median.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/online_median.dir/cmake_clean.cmake
.PHONY : CMakeFiles/online_median.dir/clean

CMakeFiles/online_median.dir/depend:
	cd "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles/online_median.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/online_median.dir/depend
