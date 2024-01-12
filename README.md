# PythonEssentials

------
INDEX
------
- utility of '\__slots__'
  - [YouTube Link](https://www.youtube.com/watch?v=1UBr94hg0FE)
  
- utility of '\__all__'

- dataclass `level-2`

- unittest `level-2`

- method overloading `level-1`
  - [mutipledispatch](https://pypi.org/project/multipledispatch/)
 
- TyoeGuard `level-1`

- decorators `level-2`
  - function based
  - class based
  - parameter based
  - concept as a pattern in API development
  - most common use-cases/examples in python web api development
    
- `C` in Python `level-1`
  - ctypes
  - cython
  - cffi
  - [perfomance comparision](https://github.com/mattip/c_from_python)
 
## To Explore
- doctest `level-0`
- metaclass `level-0`
- @atexit
- pickling
- Daemon Threading & backgroud processes `level-0`
    <details>
    <summary>use case</summary>
      
    <br>
      
    **1.** I want to send an email once the api have done it's working & the api must return/close. So the email sending operation must not block the api & must run in backround . It may run either as a daemon thread OR a seperate process .
  
    **2.** In an api call , if the content/result exists it is returned else a backgroud processing to produce the content is started & api exists .
       In successive api calls , if the status of backgroud process is `Done` then content is fetched from cache/db based on process-id else api exists .
  </details>

- numba `level-0`
- code caching
    - [read on real python](https://realpython.com/lru-cache-python/)
- [functools-higherorder functions](https://docs.python.org/3/library/functools.html#module-functools)
- tempfile


**
LEVELS :

`level-0` : just read about it & know something like this exists

`level-1` : tried out , or have a workspace designated on it where you have tried once or twice

`level-2` : have implemented in live projects & can decide when to apply it .

`level-3` : can implement/use without searching over net (syntax is frogiven)

`level-4` : proficient and used uncountable times.

`level-5` : can teach
