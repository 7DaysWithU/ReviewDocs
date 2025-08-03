def infix_to_postfix(expression: str) -> str:
    """
    中缀表达式转换为后缀表达式

    :param expression: 中缀表达式
    :return: 后缀表达式
    """

    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    # 遍历每个字符
    print(f"{'Char':<10}{'Stack':<25}{'Postfix':<50}")
    for char in expression:
        # 如果是操作数，直接添加到输出
        if char.isalnum():
            output.append(char)
            print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")
        # 左括号直接入栈
        elif char == '(':
            stack.append(char)
            print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")
        # 右括号，弹出栈中元素直到遇到左括号
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
                print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")
            # 弹出左括号
            stack.pop()
            print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")
        # 操作符
        else:
            while stack and stack[-1] != '(' and priority.get(char, 0) <= priority.get(stack[-1], 0):
                output.append(stack.pop())
                print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")
            stack.append(char)
            print(f"{char:<10}{''.join(stack):<25}{''.join(output):<50}")

    # 弹出栈中的剩余操作符
    while stack:
        output.append(stack.pop())
        print(f"{'':<10}{''.join(stack):<25}{''.join(output):<50}")

    return ''.join(output)


def cal_postfix(expression: str) -> float:
    """
    计算后缀表达式

    :param expression: 后缀表达式
    :return: 计算结果
    """

    stack = []

    print(f"{'Char':<10}{'Stack':<25}")
    for char in expression:
        if char.isdigit():
            stack.append(char)
            print(f"{char:<10}{', '.join([str(e) for e in stack]):<25}")
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(eval(f'{num1}{char}{num2}'))
            print(f"{char:<10}{', '.join([str(e) for e in stack]):<25}")

    return stack.pop()


if __name__ == '__main__':
    # my_expression = 'A+B*(C-D)-E/F'
    my_expression = '1+2*(3-4)-5/5'

    postfix = infix_to_postfix(my_expression)
    result = cal_postfix(postfix)
    print(f'  in fix: {my_expression}')
    print(f'post fix: {postfix}')
    print(f'  result: {result}')

"""
Char      Stack                    Postfix                                           
1                                  1                                                 
+         +                        1                                                 
2         +                        12                                                
*         +*                       12                                                
(         +*(                      12                                                
3         +*(                      123                                               
-         +*(-                     123                                               
4         +*(-                     1234                                              
)         +*(                      1234-                                             
)         +*                       1234-                                             
-         +                        1234-*                                            
-                                  1234-*+                                           
-         -                        1234-*+                                           
5         -                        1234-*+5                                          
/         -/                       1234-*+5                                          
5         -/                       1234-*+55                                         
          -                        1234-*+55/                                        
                                   1234-*+55/-                                       
Char      Stack                    
1         1                        
2         1, 2                     
3         1, 2, 3                  
4         1, 2, 3, 4               
-         1, 2, -1                 
*         1, -2                    
+         -1                       
5         -1, 5                    
5         -1, 5, 5                 
/         -1, 1.0                  
-         -2.0                     
  in fix: 1+2*(3-4)-5/5
post fix: 1234-*+55/-
  result: -2.0
"""
