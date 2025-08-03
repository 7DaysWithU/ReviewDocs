from collections import deque


def is_valid_stack_sequence(n: int, output: list[int]) -> bool:
    """
    判断栈输出序列是否合法

    :param n: 输入元素数量
    :param output: 输出序列
    :return: 是否合法

    注意
    ------
    - 入栈顺序为 1, 2, ..., n, 入栈操作中可以夹杂出栈操作
    """

    stack = []
    current = 1  # 从1开始入栈

    for number in output:
        # 如果栈顶元素与当前输出序列的元素不匹配，则继续入栈
        # 还有元素可以入栈且栈非空或栈顶与序列不符
        while current <= n and (not stack or stack[-1] != number):
            stack.append(current)
            current += 1

        # 栈顶匹配当前输出序列
        if stack and stack[-1] == number:
            stack.pop()
        # 无法匹配输出序列
        else:
            return False

    return True


def is_valid_queue_sequence(n: int, output: list[int]) -> bool:
    """
    判断队列输出序列是否合法

    :param n: 输入元素数量
    :param output: 输出序列
    :return: 是否合法

    注意
    ------
    - 入队顺序为 1, 2, ..., n, 入队操作中可以夹杂出队操作
    """

    queue = deque()
    current = 1  # 从1开始入队

    for number in output:
        # 如果队列的前端元素与当前输出序列的元素不匹配，则继续入队
        # 还有元素可以入队且队非空或队头与序列不符
        while current <= n and (not queue or queue[0] != number):
            queue.append(current)
            current += 1

        # 队头匹配当前输出序列
        if queue and queue[0] == number:
            queue.popleft()
        # 无法匹配序列
        else:
            return False

    return True


if __name__ == '__main__':
    output_sequence = [1, 2, 3, 4, 5]
    print(output_sequence)

    print(is_valid_stack_sequence(len(output_sequence), output_sequence))
    print(is_valid_queue_sequence(len(output_sequence), output_sequence))
