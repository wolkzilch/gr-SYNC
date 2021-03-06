# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_SYNC_swig', [dirname(__file__)])
        except ImportError:
            import _SYNC_swig
            return _SYNC_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_SYNC_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _SYNC_swig = swig_import_helper()
    del swig_import_helper
else:
    import _SYNC_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
  """high_res_timer_now() -> gr::high_res_timer_type"""
  return _SYNC_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
  """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
  return _SYNC_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
  """high_res_timer_tps() -> gr::high_res_timer_type"""
  return _SYNC_swig.high_res_timer_tps()

def high_res_timer_epoch():
  """high_res_timer_epoch() -> gr::high_res_timer_type"""
  return _SYNC_swig.high_res_timer_epoch()
class operation_splitter_sync(object):
    """<+description of block+>"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make():
        """
        make() -> operation_splitter_sync_sptr

        Return a shared_ptr to a new instance of SYNC::operation_splitter_sync.

        To avoid accidental use of raw pointers, SYNC::operation_splitter_sync's constructor is in a private implementation class. SYNC::operation_splitter_sync::make is the public interface for creating new instances.

        Params: (NONE)
        """
        return _SYNC_swig.operation_splitter_sync_make()

    make = staticmethod(make)
    __swig_destroy__ = _SYNC_swig.delete_operation_splitter_sync
    __del__ = lambda self : None;
operation_splitter_sync_swigregister = _SYNC_swig.operation_splitter_sync_swigregister
operation_splitter_sync_swigregister(operation_splitter_sync)

def operation_splitter_sync_make():
  """
    operation_splitter_sync_make() -> operation_splitter_sync_sptr

    Return a shared_ptr to a new instance of SYNC::operation_splitter_sync.

    To avoid accidental use of raw pointers, SYNC::operation_splitter_sync's constructor is in a private implementation class. SYNC::operation_splitter_sync::make is the public interface for creating new instances.

    Params: (NONE)
    """
  return _SYNC_swig.operation_splitter_sync_make()

class operation_splitter_sync_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::SYNC::operation_splitter_sync)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(boost::shared_ptr<(gr::SYNC::operation_splitter_sync)> self) -> operation_splitter_sync_sptr
        __init__(boost::shared_ptr<(gr::SYNC::operation_splitter_sync)> self, operation_splitter_sync p) -> operation_splitter_sync_sptr
        """
        this = _SYNC_swig.new_operation_splitter_sync_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(operation_splitter_sync_sptr self) -> operation_splitter_sync"""
        return _SYNC_swig.operation_splitter_sync_sptr___deref__(self)

    __swig_destroy__ = _SYNC_swig.delete_operation_splitter_sync_sptr
    __del__ = lambda self : None;
    def make(self):
        """
        make(operation_splitter_sync_sptr self) -> operation_splitter_sync_sptr

        Return a shared_ptr to a new instance of SYNC::operation_splitter_sync.

        To avoid accidental use of raw pointers, SYNC::operation_splitter_sync's constructor is in a private implementation class. SYNC::operation_splitter_sync::make is the public interface for creating new instances.

        Params: (NONE)
        """
        return _SYNC_swig.operation_splitter_sync_sptr_make(self)

    def history(self):
        """history(operation_splitter_sync_sptr self) -> unsigned int"""
        return _SYNC_swig.operation_splitter_sync_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(operation_splitter_sync_sptr self, int which, int delay)
        declare_sample_delay(operation_splitter_sync_sptr self, unsigned int delay)
        """
        return _SYNC_swig.operation_splitter_sync_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(operation_splitter_sync_sptr self, int which) -> unsigned int"""
        return _SYNC_swig.operation_splitter_sync_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(operation_splitter_sync_sptr self) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(operation_splitter_sync_sptr self) -> double"""
        return _SYNC_swig.operation_splitter_sync_sptr_relative_rate(self)

    def start(self):
        """start(operation_splitter_sync_sptr self) -> bool"""
        return _SYNC_swig.operation_splitter_sync_sptr_start(self)

    def stop(self):
        """stop(operation_splitter_sync_sptr self) -> bool"""
        return _SYNC_swig.operation_splitter_sync_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(operation_splitter_sync_sptr self, unsigned int which_input) -> uint64_t"""
        return _SYNC_swig.operation_splitter_sync_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(operation_splitter_sync_sptr self, unsigned int which_output) -> uint64_t"""
        return _SYNC_swig.operation_splitter_sync_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(operation_splitter_sync_sptr self) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(operation_splitter_sync_sptr self, int m)"""
        return _SYNC_swig.operation_splitter_sync_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(operation_splitter_sync_sptr self)"""
        return _SYNC_swig.operation_splitter_sync_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(operation_splitter_sync_sptr self) -> bool"""
        return _SYNC_swig.operation_splitter_sync_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, *args, **kwargs):
        """set_min_noutput_items(operation_splitter_sync_sptr self, int m)"""
        return _SYNC_swig.operation_splitter_sync_sptr_set_min_noutput_items(self, *args, **kwargs)

    def min_noutput_items(self):
        """min_noutput_items(operation_splitter_sync_sptr self) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_min_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(operation_splitter_sync_sptr self, int i) -> long"""
        return _SYNC_swig.operation_splitter_sync_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(operation_splitter_sync_sptr self, long max_output_buffer)
        set_max_output_buffer(operation_splitter_sync_sptr self, int port, long max_output_buffer)
        """
        return _SYNC_swig.operation_splitter_sync_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(operation_splitter_sync_sptr self, int i) -> long"""
        return _SYNC_swig.operation_splitter_sync_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(operation_splitter_sync_sptr self, long min_output_buffer)
        set_min_output_buffer(operation_splitter_sync_sptr self, int port, long min_output_buffer)
        """
        return _SYNC_swig.operation_splitter_sync_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(operation_splitter_sync_sptr self, int which) -> float
        pc_input_buffers_full(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(operation_splitter_sync_sptr self, int which) -> float
        pc_input_buffers_full_avg(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(operation_splitter_sync_sptr self, int which) -> float
        pc_input_buffers_full_var(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(operation_splitter_sync_sptr self, int which) -> float
        pc_output_buffers_full(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(operation_splitter_sync_sptr self, int which) -> float
        pc_output_buffers_full_avg(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(operation_splitter_sync_sptr self, int which) -> float
        pc_output_buffers_full_var(operation_splitter_sync_sptr self) -> pmt_vector_float
        """
        return _SYNC_swig.operation_splitter_sync_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self):
        """pc_throughput_avg(operation_splitter_sync_sptr self) -> float"""
        return _SYNC_swig.operation_splitter_sync_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(operation_splitter_sync_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _SYNC_swig.operation_splitter_sync_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(operation_splitter_sync_sptr self)"""
        return _SYNC_swig.operation_splitter_sync_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(operation_splitter_sync_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _SYNC_swig.operation_splitter_sync_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(operation_splitter_sync_sptr self) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(operation_splitter_sync_sptr self) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(operation_splitter_sync_sptr self, int priority) -> int"""
        return _SYNC_swig.operation_splitter_sync_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(operation_splitter_sync_sptr self) -> std::string"""
        return _SYNC_swig.operation_splitter_sync_sptr_name(self)

    def symbol_name(self):
        """symbol_name(operation_splitter_sync_sptr self) -> std::string"""
        return _SYNC_swig.operation_splitter_sync_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(operation_splitter_sync_sptr self) -> io_signature_sptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(operation_splitter_sync_sptr self) -> io_signature_sptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(operation_splitter_sync_sptr self) -> long"""
        return _SYNC_swig.operation_splitter_sync_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(operation_splitter_sync_sptr self) -> basic_block_sptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(operation_splitter_sync_sptr self, int ninputs, int noutputs) -> bool"""
        return _SYNC_swig.operation_splitter_sync_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(operation_splitter_sync_sptr self) -> std::string"""
        return _SYNC_swig.operation_splitter_sync_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(operation_splitter_sync_sptr self, std::string name)"""
        return _SYNC_swig.operation_splitter_sync_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(operation_splitter_sync_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _SYNC_swig.operation_splitter_sync_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(operation_splitter_sync_sptr self) -> swig_int_ptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(operation_splitter_sync_sptr self) -> swig_int_ptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(operation_splitter_sync_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _SYNC_swig.operation_splitter_sync_sptr_message_subscribers(self, *args, **kwargs)

operation_splitter_sync_sptr_swigregister = _SYNC_swig.operation_splitter_sync_sptr_swigregister
operation_splitter_sync_sptr_swigregister(operation_splitter_sync_sptr)

operation_splitter_sync_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
operation_splitter_sync = operation_splitter_sync.make;



