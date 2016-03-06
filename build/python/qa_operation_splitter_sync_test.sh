#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/python:$PATH
export LD_LIBRARY_PATH=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/build/swig:$PYTHONPATH
/usr/bin/python2 /home/zbd/Workspaces/workspace_gr_orig/gr-SYNC/python/qa_operation_splitter_sync.py 
