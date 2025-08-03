from compare import compare_code_files,get_ast_similarity
import os
from agent import run_agent
if __name__ == "__main__":
    if not os.path.exists('results.txt'):
        with open('results.txt', 'w') as f:
            f.write('SSIM Scores:\n')
    test_cases = [
        ("/test_cases/original.py", "/test_cases/identical.py"),
        ("/test_cases/original.py", "/test_cases/whitespace_changed.py"),
        ("/test_cases/original.py", "/test_cases/variable_renamed.py"),
        ("/test_cases/original.py", "/test_cases/structure_changed.py"),
    ]

    with open('result_md.md', 'a') as f:
        f.write('Comparing code snippets...\n')
        for file1, file2 in test_cases:
            # Remove leading slash and build correct paths
            path = os.getcwd()
            code1 = os.path.join(path, file1.lstrip('/'))
            code2 = os.path.join(path, file2.lstrip('/'))
            print(f"Looking for: {code1}, {code2}")
            
            # Check if files exist before processing
            if not os.path.exists(code1):
                f.write(f"Error: {code1} not found\n")
                continue
            if not os.path.exists(code2):
                f.write(f"Error: {code2} not found\n")
                continue
            
            # Uncomment the next line to use SSIM comparison
            # score,source1,source2 = compare_code_files(code1, code2)
            # Use AST similarity comparison
            score = get_ast_similarity(code1, code2)
            source1 = open(code1, 'r', encoding='utf-8').read()
            source2 = open(code2, 'r', encoding='utf-8').read()
            if score is None:
                f.write(f"Error comparing {file1} and {file2}\n")
                continue
            if score < 1:
                with open(os.path.join(path,"knowledge_base/prompt.txt"),'r', encoding='utf-8') as prompt_file:
                    prompt = prompt_file.read().strip()
                    result= run_agent(f"{prompt}\n\n{source1}\n\n{source2}\n\n Similarity score: {score}")
                    f.write("------\n")
                    f.write(str(result) if result is not None else "")
            f.write(f"SSIM between {file1} and {file2}: {score}\n")