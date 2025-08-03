#include <iostream>

using namespace std;

typedef int ElemType;
struct SqList
{
    ElemType *data;
    int max_size = 0;
    int length = 0;
};

void init(SqList &L, int max_size)
{
    L.data = (ElemType *)malloc(sizeof(ElemType) * max_size);
    L.max_size = max_size;
    L.length = 0;
}

void expand(SqList &L, int length)
{
    ElemType *data_temp = L.data;

    L.data = (ElemType *)malloc(sizeof(ElemType) * (L.max_size + length));
    for (int idx = 0; idx < L.length; idx += 1)
        L.data[idx] = data_temp[idx];

    L.max_size += length;
    free(data_temp);
}

bool insert(SqList &L, int target_idx, ElemType element)
{
    if (L.length != 0 and (target_idx < 0 or target_idx > L.length))
    {
        printf("Target index out of range.\n");
        return false;
    }
    if (L.length == L.max_size)
    {
        printf("SqList has already full\n");
        return false;
    }

    for (int idx = L.length; idx > target_idx; idx -= 1)
        L.data[idx] = L.data[idx - 1];
    L.data[target_idx] = element;
    L.length += 1;

    return true;
}

bool pop(SqList &L, int target_idx, ElemType &element)
{
    if (L.length != 0 and (target_idx < 0 or target_idx > L.length))
    {
        printf("Target index out of range.\n");
        return false;
    }

    element = L.data[target_idx];
    for (int idx = target_idx; idx < L.length; idx += 1)
        L.data[idx] = L.data[idx + 1];
    L.length -= 1;

    return true;
}

SqList iloc(SqList &L, ElemType target_element)
{
    SqList indices;
    init(indices, 0);

    int result_num = 0;
    for (int idx = 0; idx < L.length; idx += 1)
    {
        if (L.data[idx] == target_element)
        {
            expand(indices, 1);
            insert(indices, result_num, idx);
            result_num += 1;
        }
    }

    return indices;
}

int main()
{
    std::cout << "Hello CPP!\n";

    SqList my_SqList;
    init(my_SqList, 5);

    // 插入元素并输出
    printf("max_size = %d\n", my_SqList.max_size);
    for (int idx = 0; idx < my_SqList.max_size; idx += 1)
        insert(my_SqList, idx, idx);
    printf("after insert:\n");
    for (int idx = 0; idx < my_SqList.length; idx += 1)
        printf("data[%d] = %d\n", idx, my_SqList.data[idx]);

    // 查找元素并输出
    SqList indices = iloc(my_SqList, 5);
    for (int idx = 0; idx < indices.length; idx += 1)
        printf("indices[%d] = %d\n", idx, indices.data[idx]);

    // 扩展顺序表
    expand(my_SqList, 5);
    printf("after expand:\n");
    printf("max_size = %d\n", my_SqList.max_size);

    // 对扩展部分插入并输出
    for (int idx = my_SqList.length; idx < my_SqList.max_size; idx += 1)
        insert(my_SqList, idx, idx);
    printf("after insert:\n");
    for (int idx = 0; idx < my_SqList.length; idx += 1)
        printf("data[%d] = %d\n", idx, my_SqList.data[idx]);
    
    // 删除元素并输出
    int removed_element = -1;
    pop(my_SqList, 5, removed_element);
    printf("removed_element = %d\n", removed_element);
    printf("after pop:\n");
    for (int idx = 0; idx < my_SqList.length; idx += 1)
        printf("data[%d] = %d\n", idx, my_SqList.data[idx]);

    return 0;
}
