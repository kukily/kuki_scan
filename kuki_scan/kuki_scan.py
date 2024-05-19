import os

def user_input_to_fofa_query(user_input):
    # 假设这里是将用户输入转化为FOFA语句的逻辑
    # 示例：简单地返回用户输入内容
    # 实际情况中，你需要根据具体的转换规则来实现
    fofa_query = f'{user_input}'
    return fofa_query

def execute_bug_scan_script():
    script_path = "/root/scan/bug_scan.sh"
    command = f"sh {script_path}"
    os.system(command)

if __name__ == "__main__":
    user_input = input("请输入语句：")
    fofa_query = user_input_to_fofa_query(user_input)
    print(f"转换后的FOFA语句：{fofa_query}")
    
    # 这里可以将fofa_query存储到一个文件或环境变量中，供bug_scan.sh脚本使用
    # 示例：写入到一个文件中
    with open("/root/keyword.txt", "w") as file:
        file.write(fofa_query)
    
    # 执行bug_scan.sh脚本
    execute_bug_scan_script()
