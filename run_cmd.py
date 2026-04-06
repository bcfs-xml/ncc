import subprocess
# subprocess.run(r"C:\Users\bcfsant\www\ncc-test\genetic_nesting_optimized.exe")

subprocess.run([
	"nesting.exe",
	"input_shapes.json",
	"-o",
	"genetic_nesting_optimized_result.json",
	"--time",
	"500",
], check=True)

  File "C:\Users\bcfsant\www\ncc-test\run_cmd.py", line 4, in <module>
    subprocess.run([
  File "C:\Program Files\Python310\lib\subprocess.py", line 501, in run
    with Popen(*popenargs, **kwargs) as process:
  File "C:\Program Files\Python310\lib\subprocess.py", line 966, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\Python310\lib\subprocess.py", line 1435, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
OSError: [WinError 1392] The file or directory is corrupted and unreadable
