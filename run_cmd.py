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
