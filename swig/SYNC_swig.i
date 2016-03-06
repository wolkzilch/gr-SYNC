/* -*- c++ -*- */

#define SYNC_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "SYNC_swig_doc.i"

%{
#include "SYNC/operation_splitter_sync.h"
%}


%include "SYNC/operation_splitter_sync.h"
GR_SWIG_BLOCK_MAGIC2(SYNC, operation_splitter_sync);
