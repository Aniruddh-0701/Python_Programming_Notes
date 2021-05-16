# Modules and Packages
Modules are files that contain functions, variables or classes that can be used without redefining them. They're generally written in Python.

Packages are directory or folders which conatin a number of modules or packages in them.

Few built-in Modules are:
1. \_\_builtins\_\_
0. \_\_file\_\_
2. math
3. cmath
2. sys
4. os
5. itertools
6. string

The basics of working with module are discussed using a file *prime_generator.py*

Code:  
>from time import &#42; <br>
from itertools import &#42;  <br>
from math import &#42; <br>
<br>
def prime_gen(n): <br> 
&nbsp;&nbsp;&nbsp;&nbsp; num = 2<br>
&nbsp;&nbsp;&nbsp;&nbsp; while num <= n: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; k = 2 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while k * k <= num: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if num % k == 0: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; k += 1 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; yield num <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; num += 1 <br>
<br>
prime = 2 <br>
prime\_square = 4 <br>
\_\_primeval\_\_ = 3<br>
<br>
if \_\_name\_\_ == '\_\_main\_\_': <br>
&nbsp;&nbsp;&nbsp;&nbsp; t = time()<br>
&nbsp;&nbsp;&nbsp;&nbsp; for i in prime_gen(10 ** 2):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print(i)<br>
&nbsp;&nbsp;&nbsp;&nbsp; print(time()-t)

Contents:
1. prime_gen - function or generator 
2. prime - varaiable (constant when imported)
3. prime_square - variable (constant when imported)
4. \_\_primeval\_\_ - private value

## import statement:
The *import* keyword is used to import a module or package.

Syntax: `import module_name`


```python
import prime_generator

for i in prime_generator.prime_gen(20):
    print(i, end=' ')
```

    2 3 5 7 11 13 17 19 

## from statement:
The *from* keyword is used to import a specific set of functions or classes from a module.

Syntax: `from module_name import function_name`


```python
from prime_generator import prime_gen

for i in prime_gen(20):
    print(i, end=' ')
```

    2 3 5 7 11 13 17 19 

## Importing all the objects from the module:
To import all the functions or objects, use * .

Syntax: `from module_name import *`


```python
from prime_generator import *

for i in prime_gen(20):
    print(i, end=' ')
```

    2 3 5 7 11 13 17 19 

## **as** Keyword:
*as* Keyword is used to have a custom name for imported module or function.

Syntax:  
`import moule_name as custom_name`  
`from module_name import function_name as custom_name`


```python
import prime_generator as pg

for i in pg.prime_gen(20):
    print(i, end=' ')
```

    2 3 5 7 11 13 17 19 


```python
from prime_generator import prime_gen as pgf

for i in pgf(20):
    print(i, end=' ')
```

    2 3 5 7 11 13 17 19 

## \_\_name\_\_:
It returns the name of the module without the extension. If called for main executing program (main module), it returns '\_\_main\_\_'

Syntax: `module_name.__name__`


```python
import prime_generator as pg

print(pg.__name__)
print(__name__)
```

    prime_generator
    __main__
    

## dir method:

Returns the list of attributes (that are relevant) of an object or a module. By default, it gives the details of main module.

Syntax: `dir([object])`


```python
import prime_generator

print(dir(prime_generator))
print()
print(dir(prime_generator.prime_gen))
print()
print(dir())
```

    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__primeval__', '__spec__', 'accumulate', 'acos', 'acosh', 'altzone', 'asctime', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'chain', 'comb', 'combinations', 'combinations_with_replacement', 'compress', 'copysign', 'cos', 'cosh', 'count', 'ctime', 'cycle', 'daylight', 'degrees', 'dist', 'dropwhile', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'filterfalse', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'get_clock_info', 'gmtime', 'groupby', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'islice', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'localtime', 'log', 'log10', 'log1p', 'log2', 'mktime', 'modf', 'monotonic', 'monotonic_ns', 'nan', 'perf_counter', 'perf_counter_ns', 'perm', 'permutations', 'pi', 'pow', 'prime', 'prime_gen', 'prime_square', 'process_time', 'process_time_ns', 'prod', 'product', 'radians', 'remainder', 'repeat', 'sin', 'sinh', 'sleep', 'sqrt', 'starmap', 'strftime', 'strptime', 'struct_time', 'takewhile', 'tan', 'tanh', 'tau', 'tee', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'trunc', 'tzname', 'zip_longest']
    
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    
    ['In', 'Out', '_', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i2', '_i3', '_i4', '_ih', '_ii', '_iii', '_oh', 'exit', 'get_ipython', 'prime_generator', 'quit']
    

## namespace:

A container that has a list of names (objects) defined in a module. It is the place where python searches for objects defined and used in a function.

## Global, Local and Built-in Namespaces

### Global:
Namespace containing values defined throughout a file or module (globally)

### Local:
Namespace containing values defined in a part of a file or module (Locally)

### Builtin:
Namespace containing values common for all python file.

## Order of Search:
1. Local
2. Global
3. Builtin

## Packages:
Directory or folder containing a number of modules and subpackages.

It contains '\_\_init\_\_.py' file which defines the modules that can be imported from the package.

### Importing a module from package:  
`import package_name.module_name`  
`import package_name.module_name as custom_name`

### Import a specific object from a module:
`from package_name.module_name import object_name`

## Builtins:

\_\_builtins\_\_ module contains the list of methods and variables that are standard definitions in Python.


```python
builtin = dir(__builtins__)
for i in builtin:
    print(i)
```

    ArithmeticError
    AssertionError
    AttributeError
    BaseException
    BlockingIOError
    BrokenPipeError
    BufferError
    BytesWarning
    ChildProcessError
    ConnectionAbortedError
    ConnectionError
    ConnectionRefusedError
    ConnectionResetError
    DeprecationWarning
    EOFError
    Ellipsis
    EnvironmentError
    Exception
    False
    FileExistsError
    FileNotFoundError
    FloatingPointError
    FutureWarning
    GeneratorExit
    IOError
    ImportError
    ImportWarning
    IndentationError
    IndexError
    InterruptedError
    IsADirectoryError
    KeyError
    KeyboardInterrupt
    LookupError
    MemoryError
    ModuleNotFoundError
    NameError
    None
    NotADirectoryError
    NotImplemented
    NotImplementedError
    OSError
    OverflowError
    PendingDeprecationWarning
    PermissionError
    ProcessLookupError
    RecursionError
    ReferenceError
    ResourceWarning
    RuntimeError
    RuntimeWarning
    StopAsyncIteration
    StopIteration
    SyntaxError
    SyntaxWarning
    SystemError
    SystemExit
    TabError
    TimeoutError
    True
    TypeError
    UnboundLocalError
    UnicodeDecodeError
    UnicodeEncodeError
    UnicodeError
    UnicodeTranslateError
    UnicodeWarning
    UserWarning
    ValueError
    Warning
    WindowsError
    ZeroDivisionError
    __IPYTHON__
    __build_class__
    __debug__
    __doc__
    __import__
    __loader__
    __name__
    __package__
    __spec__
    abs
    all
    any
    ascii
    bin
    bool
    breakpoint
    bytearray
    bytes
    callable
    chr
    classmethod
    compile
    complex
    copyright
    credits
    delattr
    dict
    dir
    display
    divmod
    enumerate
    eval
    exec
    filter
    float
    format
    frozenset
    get_ipython
    getattr
    globals
    hasattr
    hash
    help
    hex
    id
    input
    int
    isinstance
    issubclass
    iter
    len
    license
    list
    locals
    map
    max
    memoryview
    min
    next
    object
    oct
    open
    ord
    pow
    print
    property
    range
    repr
    reversed
    round
    set
    setattr
    slice
    sorted
    staticmethod
    str
    sum
    super
    tuple
    type
    vars
    zip
    

## \_\_file\_\_ module:

It contains the list of builtin variables and functions that can be used in the current file.

### contents:
\_\_add\_\_  
\_\_class\_\_  
\_\_contains\_\_  
\_\_delattr\_\_  
\_\_dir\_\_  
\_\_doc\_\_  
\_\_eq\_\_  
\_\_format\_\_  
\_\_ge\_\_  
\_\_getattribute\_\_  
\_\_getitem\_\_  
\_\_getnewargs\_\_  
\_\_gt\_\_  
\_\_hash\_\_  
\_\_init\_\_  
\_\_init_subclass\_\_  
\_\_iter\_\_  
\_\_le\_\_  
\_\_len\_\_  
\_\_lt\_\_  
\_\_mod\_\_  
\_\_mul\_\_  
\_\_ne\_\_  
\_\_new\_\_  
\_\_reduce\_\_  
\_\_reduce_ex\_\_  
\_\_repr\_\_  
\_\_rmod\_\_  
\_\_rmul\_\_  
\_\_setattr\_\_  
\_\_sizeof\_\_  
\_\_str\_\_  
\_\_subclasshook\_\_  
capitalize  
casefold  
center  
count  
encode  
endswith  
expandtabs  
find  
format  
format_map  
index  
isalnum  
isalpha  
isascii  
isdecimal  
isdigit  
isidentifier  
islower  
isnumeric  
isprintable  
isspace  
istitle  
isupper  
join  
ljust  
lower  
lstrip  
maketrans  
partition  
replace  
rfind  
rindex  
rjust  
rpartition  
rsplit  
rstrip  
split  
splitlines  
startswith  
strip  
swapcase  
title  
translate  
upper  
zfill  

## Private in modules:

Objects can be restricted to usage when running as a main module. They cannot be imported when importing the complete module using ' &#42; '.

They start and end with double underscores, \_\_


```python
import prime_generator as pg

print(pg.__primeval__)
```

    3
    


```python
from prime_generator import *

print(__primeval__)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-42698b27057d> in <module>
          1 from prime_generator import *
          2 
    ----> 3 print(__primeval__)
    

    NameError: name '__primeval__' is not defined


## globals(), locals() and reload()

globals - returns the list of objects that can be accessed globally from that point.

locals - returns the list of objects that can be accessed locally from that point.

reload - reloads the given module. (imported from impotlib module)

Syntax: `reload(module_name)`

## math:
This module contains list of all mathematical functions.


```python
import math

print(*dir(math), sep='\n')
```

    __doc__
    __loader__
    __name__
    __package__
    __spec__
    acos
    acosh
    asin
    asinh
    atan
    atan2
    atanh
    ceil
    comb
    copysign
    cos
    cosh
    degrees
    dist
    e
    erf
    erfc
    exp
    expm1
    fabs
    factorial
    floor
    fmod
    frexp
    fsum
    gamma
    gcd
    hypot
    inf
    isclose
    isfinite
    isinf
    isnan
    isqrt
    ldexp
    lgamma
    log
    log10
    log1p
    log2
    modf
    nan
    perm
    pi
    pow
    prod
    radians
    remainder
    sin
    sinh
    sqrt
    tan
    tanh
    tau
    trunc
    


```python
import math

print(math.pi/2)
print(math.asin(1))
# 1.570796... = pi/2
```

    1.5707963267948966
    1.5707963267948966
    


```python
# 21.33 ceil - 22
# 21.33 floor - 21
# 21, 21.33, 22
print(math.ceil(21.33))
print(math.floor(21.33))
```

    22
    21
    


```python
math.pow(2, 3) # 2 ** 3
```




    8.0



$\mathit{^5P_2}$  
$\mathit{^5C_2}$


```python
math.perm(5, 2) # 5P2
```




    20




```python
math.comb(5, 2) # 5C2
```




    10



## cmath:
Like math, used to work with complex numbers.


```python
import cmath

print(*dir(cmath), sep='\n')
```

    __doc__
    __loader__
    __name__
    __package__
    __spec__
    acos
    acosh
    asin
    asinh
    atan
    atanh
    cos
    cosh
    e
    exp
    inf
    infj
    isclose
    isfinite
    isinf
    isnan
    log
    log10
    nan
    nanj
    phase
    pi
    polar
    rect
    sin
    sinh
    sqrt
    tan
    tanh
    tau
    

## sys:

Work with program execution and system.


```python
import sys

print(*dir(sys), sep='\n')
```

    __breakpointhook__
    __displayhook__
    __doc__
    __excepthook__
    __interactivehook__
    __loader__
    __name__
    __package__
    __spec__
    __stderr__
    __stdin__
    __stdout__
    __unraisablehook__
    _base_executable
    _clear_type_cache
    _current_frames
    _debugmallocstats
    _enablelegacywindowsfsencoding
    _framework
    _getframe
    _git
    _home
    _xoptions
    addaudithook
    api_version
    argv
    audit
    base_exec_prefix
    base_prefix
    breakpointhook
    builtin_module_names
    byteorder
    call_tracing
    callstats
    copyright
    displayhook
    dllhandle
    dont_write_bytecode
    exc_info
    excepthook
    exec_prefix
    executable
    exit
    flags
    float_info
    float_repr_style
    get_asyncgen_hooks
    get_coroutine_origin_tracking_depth
    getallocatedblocks
    getcheckinterval
    getdefaultencoding
    getfilesystemencodeerrors
    getfilesystemencoding
    getprofile
    getrecursionlimit
    getrefcount
    getsizeof
    getswitchinterval
    gettrace
    getwindowsversion
    hash_info
    hexversion
    implementation
    int_info
    intern
    is_finalizing
    maxsize
    maxunicode
    meta_path
    modules
    path
    path_hooks
    path_importer_cache
    platform
    prefix
    ps1
    ps2
    ps3
    pycache_prefix
    set_asyncgen_hooks
    set_coroutine_origin_tracking_depth
    setcheckinterval
    setprofile
    setrecursionlimit
    setswitchinterval
    settrace
    stderr
    stdin
    stdout
    thread_info
    unraisablehook
    version
    version_info
    warnoptions
    winver
    

## os:
works with operating system


```python
import os
print(*dir(os), sep='\n')
```

    DirEntry
    F_OK
    MutableMapping
    O_APPEND
    O_BINARY
    O_CREAT
    O_EXCL
    O_NOINHERIT
    O_RANDOM
    O_RDONLY
    O_RDWR
    O_SEQUENTIAL
    O_SHORT_LIVED
    O_TEMPORARY
    O_TEXT
    O_TRUNC
    O_WRONLY
    P_DETACH
    P_NOWAIT
    P_NOWAITO
    P_OVERLAY
    P_WAIT
    PathLike
    R_OK
    SEEK_CUR
    SEEK_END
    SEEK_SET
    TMP_MAX
    W_OK
    X_OK
    _AddedDllDirectory
    _Environ
    __all__
    __builtins__
    __cached__
    __doc__
    __file__
    __loader__
    __name__
    __package__
    __spec__
    _check_methods
    _execvpe
    _exists
    _exit
    _fspath
    _get_exports_list
    _putenv
    _unsetenv
    _wrap_close
    abc
    abort
    access
    add_dll_directory
    altsep
    chdir
    chmod
    close
    closerange
    cpu_count
    curdir
    defpath
    device_encoding
    devnull
    dup
    dup2
    environ
    error
    execl
    execle
    execlp
    execlpe
    execv
    execve
    execvp
    execvpe
    extsep
    fdopen
    fsdecode
    fsencode
    fspath
    fstat
    fsync
    ftruncate
    get_exec_path
    get_handle_inheritable
    get_inheritable
    get_terminal_size
    getcwd
    getcwdb
    getenv
    getlogin
    getpid
    getppid
    isatty
    kill
    linesep
    link
    listdir
    lseek
    lstat
    makedirs
    mkdir
    name
    open
    pardir
    path
    pathsep
    pipe
    popen
    putenv
    read
    readlink
    remove
    removedirs
    rename
    renames
    replace
    rmdir
    scandir
    sep
    set_handle_inheritable
    set_inheritable
    spawnl
    spawnle
    spawnv
    spawnve
    st
    startfile
    stat
    stat_result
    statvfs_result
    strerror
    supports_bytes_environ
    supports_dir_fd
    supports_effective_ids
    supports_fd
    supports_follow_symlinks
    symlink
    sys
    system
    terminal_size
    times
    times_result
    truncate
    umask
    uname_result
    unlink
    urandom
    utime
    waitpid
    walk
    write
    

## itertools:

A module containing iterators for efficient looping


```python
import itertools

print(*dir(itertools), sep='\n')
```

    __doc__
    __loader__
    __name__
    __package__
    __spec__
    _grouper
    _tee
    _tee_dataobject
    accumulate
    chain
    combinations
    combinations_with_replacement
    compress
    count
    cycle
    dropwhile
    filterfalse
    groupby
    islice
    permutations
    product
    repeat
    starmap
    takewhile
    tee
    zip_longest
    


```python

```
