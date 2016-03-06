#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib:$PATH
export LD_LIBRARY_PATH=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-SYNC 
