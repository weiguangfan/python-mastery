import os
import sys

# 指定想要的工作目录
target_directory = 'F:\\github_projects\\python-mastery\\Work'

# 更改当前工作目录
os.chdir(target_directory)

# 启动Python Console
sys.argv.append('python')
sys.argv.append('-i')
sys.executable = sys.argv.pop(0)
os.execlp(sys.executable, *sys.argv)
