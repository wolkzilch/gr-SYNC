# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-SYNC.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-SYNC.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-SYNC.dir/flags.make

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o: lib/CMakeFiles/gnuradio-SYNC.dir/flags.make
lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o: ../lib/operation_splitter_sync_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o"
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o -c /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/lib/operation_splitter_sync_impl.cc

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.i"
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/lib/operation_splitter_sync_impl.cc > CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.i

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.s"
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/lib/operation_splitter_sync_impl.cc -o CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.s

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.requires

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.provides: lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-SYNC.dir/build.make lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.provides

lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o

# Object files for target gnuradio-SYNC
gnuradio__SYNC_OBJECTS = \
"CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o"

# External object files for target gnuradio-SYNC
gnuradio__SYNC_EXTERNAL_OBJECTS =

lib/libgnuradio-SYNC.so: lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o
lib/libgnuradio-SYNC.so: lib/CMakeFiles/gnuradio-SYNC.dir/build.make
lib/libgnuradio-SYNC.so: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/libgnuradio-SYNC.so: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/libgnuradio-SYNC.so: /home/zbd/Targets/target_gr_orig/lib/libgnuradio-runtime.so
lib/libgnuradio-SYNC.so: /home/zbd/Targets/target_gr_orig/lib/libgnuradio-pmt.so
lib/libgnuradio-SYNC.so: lib/CMakeFiles/gnuradio-SYNC.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libgnuradio-SYNC.so"
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-SYNC.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-SYNC.dir/build: lib/libgnuradio-SYNC.so
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/build

lib/CMakeFiles/gnuradio-SYNC.dir/requires: lib/CMakeFiles/gnuradio-SYNC.dir/operation_splitter_sync_impl.cc.o.requires
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/requires

lib/CMakeFiles/gnuradio-SYNC.dir/clean:
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-SYNC.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/clean

lib/CMakeFiles/gnuradio-SYNC.dir/depend:
	cd /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/lib /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib/CMakeFiles/gnuradio-SYNC.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/gnuradio-SYNC.dir/depend

