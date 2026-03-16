import sys
from analyzer import analyze_code

def run_cli():
    
    if len(sys.argv) < 3:
        print("사용법:")
        print("python main.py review <파일>")
        return

    command = sys.argv[1]
    filename = sys.argv[2]

    analyze_code(command, filename)