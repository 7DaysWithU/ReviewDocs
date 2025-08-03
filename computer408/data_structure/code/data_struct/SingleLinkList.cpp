#include <iostream>

using namespace std;

typedef int ElemType;
struct LinkNode
{
    ElemType data;
    LinkNode *next;
};

void init(LinkNode *&L)
{
    L = (LinkNode *)malloc(sizeof(LinkNode));
    L->data = 0;
    L->next = NULL;
}

void ergodic(LinkNode *L)
{
    LinkNode *temp = L->next;
    int length = 0;

    while (temp != NULL)
    {
        printf("LinkList[%d]=%d\n", length, temp->data);
        temp = temp->next;
        length += 1;
    }
}

void head_insert(LinkNode *L, ElemType element)
{
    LinkNode *new_node = (LinkNode *)malloc(sizeof(LinkNode));
    new_node->data = element;
    new_node->next = L->next;
    L->next = new_node;
}

void tail_insert(LinkNode *L, ElemType element)
{
    LinkNode *tail = L;
    LinkNode *new_node = (LinkNode *)malloc(sizeof(LinkNode));

    while (tail->next != NULL)
        tail = tail->next;

    new_node->data = element;
    new_node->next = NULL;
    tail->next = new_node;
    tail = new_node;
}

bool pop(LinkNode *L, int target_idx)
{
    if (target_idx < 0)
        return false;

    LinkNode *temp = L->next;
    int now_idx = 0;

    while (temp != NULL and now_idx < target_idx - 1)
    {
        temp = temp->next;
        now_idx += 1;
    }

    if (temp->next == NULL)
        return false;
    LinkNode *target_node = temp->next;
    temp->next = target_node->next;
    free(target_node);

    return true;
}

ElemType iloc(LinkNode *L, int target_idx)
{
    if (target_idx < 0)
        return -1;

    LinkNode *temp = L->next;
    int now_idx = 0;

    while (temp != NULL)
    {
        if (now_idx == target_idx)
            return temp->data;
        temp = temp->next;
        now_idx += 1;
    }

    return -1;
}

LinkNode *loc(LinkNode *L, ElemType target_element)
{
    LinkNode *result;
    init(result);
    LinkNode *temp = L->next;
    int now_idx = 0;

    while (temp != NULL)
    {
        if (temp->data == target_element)
            tail_insert(result, now_idx);
        temp = temp->next;
        now_idx += 1;
    }

    return result;
}

int main()
{
    std::cout << "Hello Cpp!\n";

    // 建立单链表
    LinkNode *header;
    init(header);

    // 头插法
    printf("after head insert:\n");
    int data[5] = {0, 1, 2, 3, 4};
    for (int idx = 0; idx < 5; idx += 1)
        head_insert(header, data[idx]);
    ergodic(header);
    printf("\n");

    // 尾插法
    printf("after tail insert:\n");
    for (int idx = 0; idx < 5; idx += 1)
        tail_insert(header, data[idx]);
    ergodic(header);
    printf("\n");

    // 按下标查找元素
    printf("iloc:\n");
    int target_idx = 5;
    ElemType result_1 = iloc(header, target_idx);
    printf("LinkList[%d]=%d\n\n", target_idx, result_1);

    // 按值查找元素
    printf("loc:\n");
    int target_element = 4;
    LinkNode *result_2 = loc(header, target_element);
    ergodic(result_2);
    printf("\n");

    // 尾插法
    printf("after pop:\n");
    int target_pop_idx = 4;
    pop(header, target_pop_idx);
    ergodic(header);
    printf("\n");
}
