def generate_next(pattern: str) -> list[int]:
    """
    生成 next列表

    :param pattern: 模式串
    :return: next列表
    """

    # 第一个字符前边肯定没有匹配的, 直接内置0
    pattern_next = [0]
    max_prefix_len: int = 0

    # 下标0已经被内置了, 直接从1开始
    idx = 1
    while idx < len(pattern):
        if pattern[max_prefix_len] == pattern[idx]:
            max_prefix_len += 1
            pattern_next.append(max_prefix_len)
            idx += 1
        else:
            if max_prefix_len == 0:
                pattern_next.append(0)
                idx += 1
            else:
                max_prefix_len = pattern_next[max_prefix_len - 1]

    return pattern_next


def kmp(target: str, pattern: str) -> int:
    """
    KMP匹配

    :param target: 目标串
    :param pattern: 模式串
    :return: 匹配下标
    """

    pattern_next = generate_next(pattern)
    print(pattern_next)

    target_idx, pattern_idx = 0, 0
    while target_idx < len(target):
        print(target_idx, target[target_idx])
        print(pattern_idx, pattern[pattern_idx])
        print()

        if target[target_idx] == pattern[pattern_idx]:
            target_idx += 1
            pattern_idx += 1
        elif pattern_idx > 0:
            pattern_idx = pattern_next[pattern_idx - 1]
        else:
            target_idx += 1

        if pattern_idx == len(pattern):
            print(target_idx - pattern_idx)


if __name__ == '__main__':
    my_target = 'aaaaaaaaaaaaaaab'
    my_pattern = 'aab'
    kmp(my_target, my_pattern)
