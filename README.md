# pip install testcase

This demonstrates an undesired difference behavior on Windows when installing
scripts in editable mode vs. a standard install.

```
$ pip install .
$ testcase
It works.
$ python c:\Python35-32\Scripts\testcase.exe
It works.

$ pip install -e .
$ testcase
It works.
$ python c:\Python35-32\Scripts\testcase.exe
  File "c:\Python35-32\Scripts\testcase.exe", line 1
SyntaxError: Non-UTF-8 code starting with '\x90' in file c:\Python35-32\Scripts\testcase.exe on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

When installed in editable mode, three files are created in the scripts folder:

```
testcase.exe
testcase.exe.manifest
testcase-script.pyw
```

When installed normally, only `testcase.exe` is created.
