INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SYNC SYNC)

FIND_PATH(
    SYNC_INCLUDE_DIRS
    NAMES SYNC/api.h
    HINTS $ENV{SYNC_DIR}/include
        ${PC_SYNC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SYNC_LIBRARIES
    NAMES gnuradio-SYNC
    HINTS $ENV{SYNC_DIR}/lib
        ${PC_SYNC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SYNC DEFAULT_MSG SYNC_LIBRARIES SYNC_INCLUDE_DIRS)
MARK_AS_ADVANCED(SYNC_LIBRARIES SYNC_INCLUDE_DIRS)

