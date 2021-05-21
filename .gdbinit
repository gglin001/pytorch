# python
# import sys
# sys.path.insert(0, '/usr/share/gcc-8/python')
# from libstdcxx.v6.printers import register_libstdcxx_printers
# register_libstdcxx_printers (None)
# end
# define sbove in ~/.gdbinit

set print element 0
set print array on
set print pretty on
set print object on
set print vtbl on
set print symbol on

skip -gfi /usr/include/c++/8/*
skip -gfi /usr/include/c++/7/*
skip -gfi /usr/include/c++/7.5.0/*
skip -gfi stdlib/*.c
