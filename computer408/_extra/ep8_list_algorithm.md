# 单链表408常考操作

## 1 数据结构定义

```C
// 单链表节点定义
typedef struct LNode {
    int data;                // 数据域
    struct LNode *next;      // 指针域
} LNode, *LinkList;
```

## 2 基础操作函数

### 2.1 初始化链表（带头结点）

```C
// 初始化带头结点的空链表
bool InitList(LinkList *L) {
    *L = (LNode*)malloc(sizeof(LNode));
    if (*L == NULL) return false;
    (*L)->next = NULL;
    return true;
}
```

### 2.2 尾插法创建链表

```C
// 尾插法创建链表（带头结点）
LinkList CreateList_Tail(int arr[], int n) {
    LinkList L = (LNode*)malloc(sizeof(LNode));
    L->next = NULL;
    LNode *r = L; // r指向尾结点
    
    for (int i = 0; i < n; i++) {
        LNode *s = (LNode*)malloc(sizeof(LNode));
        s->data = arr[i];
        s->next = NULL;
        r->next = s;
        r = s;
    }
    return L;
}
```

### 2.3 头插法创建链表

```C
// 头插法创建链表（带头结点）
LinkList CreateList_Head(int arr[], int n) {
    LinkList L = (LNode*)malloc(sizeof(LNode));
    L->next = NULL;
    
    for (int i = 0; i < n; i++) {
        LNode *s = (LNode*)malloc(sizeof(LNode));
        s->data = arr[i];
        s->next = L->next;
        L->next = s;
    }
    return L;
}
```

### 2.4 打印链表

```C
// 打印链表
void PrintList(LinkList L) {
    LNode *p = L->next;
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}
```

## 3 常考算法

### 3.1 原地逆置

```C
/**
 * 链表原地逆置 - 时间复杂度O(n)，空间复杂度O(1)
 * 方法：头插法重建链表
 */
void ReverseList(LinkList L) {
    LNode *p = L->next;    // p指向第一个数据结点
    L->next = NULL;        // 将头结点的next置空
    
    while (p != NULL) {
        LNode *q = p->next; // q保存p的后继
        p->next = L->next;  // p插入到头结点之后
        L->next = p;
        p = q;              // p指向下一个待处理结点
    }
}

/**
 * 链表原地逆置 - 三指针法
 */
void ReverseList_ThreePointers(LinkList L) {
    if (L->next == NULL || L->next->next == NULL) 
        return;
    
    LNode *pre = NULL;
    LNode *cur = L->next;
    LNode *next = NULL;
    
    while (cur != NULL) {
        next = cur->next;   // 保存后继
        cur->next = pre;    // 反转指针
        pre = cur;          // 移动pre
        cur = next;         // 移动cur
    }
    L->next = pre;          // 更新头结点的next
}
```

### 3.2 快慢指针

#### 3.2.1 判断链表是否有环

```C
/**
 * 判断链表是否有环 - Floyd判圈算法
 * 返回：true表示有环，false表示无环
 */
bool HasCycle(LinkList L) {
    if (L->next == NULL) return false;
    
    LNode *slow = L->next;
    LNode *fast = L->next;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return true;
    }
    return false;
}
```

#### 3.2.2 寻找环的入口点

```C
/**
 * 寻找环的入口点
 * 返回：环的入口结点，无环返回NULL
 */
LNode* FindCycleEntry(LinkList L) {
    if (L->next == NULL) return NULL;
    
    LNode *slow = L->next;
    LNode *fast = L->next;
    
    // 第一步：判断是否有环，并找到相遇点
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) break;
    }
    
    // 无环情况
    if (fast == NULL || fast->next == NULL) 
        return NULL;
    
    // 第二步：寻找环入口
    slow = L->next; // slow从头开始
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}
```

#### 3.2.3 寻找链表中点

```C
/**
 * 寻找链表中点
 * 对于偶数个结点，返回中间两个结点的第一个
 */
LNode* FindMiddle(LinkList L) {
    if (L->next == NULL) return NULL;
    
    LNode *slow = L->next;
    LNode *fast = L->next;
    
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

#### 3.2.4 寻找倒数第 k 个结点

```C
/**
 * 寻找倒数第k个结点
 * 返回：倒数第k个结点的指针，不存在返回NULL
 */
LNode* FindKthFromEnd(LinkList L, int k) {
    if (k <= 0) return NULL;
    
    LNode *fast = L->next;
    LNode *slow = L->next;
    
    // fast先走k步
    for (int i = 0; i < k; i++) {
        if (fast == NULL) return NULL; // k大于链表长度
        fast = fast->next;
    }
    
    // slow和fast同时移动
    while (fast != NULL) {
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}
```

### 3.3 查找第 k 个元素

```C
/**
 * 查找第k个元素（k从1开始计数）
 * 返回：第k个元素的值，-1表示不存在
 */
int GetElem(LinkList L, int k) {
    if (k <= 0) return -1;
    
    LNode *p = L->next;
    int i = 1;
    
    while (p != NULL && i < k) {
        p = p->next;
        i++;
    }
    
    if (p == NULL) return -1; // 第k个元素不存在
    return p->data;
}
```

### 3.4 删除最小值结点

```C
/**
 * 删除链表中最小值的结点（仅删除第一个最小值）
 * 返回：true表示删除成功，false表示链表为空
 */
bool DeleteMin(LinkList L) {
    if (L->next == NULL) return false;
    
    LNode *pre = L;           // pre指向最小值结点的前驱
    LNode *min_pre = L;       // min_pre指向当前最小值结点的前驱
    LNode *p = L->next;
    
    while (p->next != NULL) {
        if (p->next->data < min_pre->next->data)
            min_pre = pre;

        pre = p;
        p = p->next;
    }
    
    // 删除最小值结点
    LNode *min_node = min_pre->next;
    min_pre->next = min_node->next;
    free(min_node);
    return true;
}
```

### 3.5 有序链表合并

```C
/**
 * 合并两个有序链表（非递归）
 * 返回：合并后的链表头指针
 */
LinkList MergeSortedLists(LinkList L1, LinkList L2) {
    LinkList L = (LNode*)malloc(sizeof(LNode));
    LNode *p1 = L1->next;
    LNode *p2 = L2->next;
    LNode *r = L;
    
    while (p1 != NULL && p2 != NULL) {
        if (p1->data <= p2->data) {
            r->next = p1;
            p1 = p1->next;
        } else {
            r->next = p2;
            p2 = p2->next;
        }
        r = r->next;
    }
    
    // 处理剩余结点
    r->next = (p1 != NULL) ? p1 : p2;
    
    // 释放原头结点
    free(L1);
    free(L2);
    
    return L;
}
```

### 3.6 链表划分

```C
/**
 * 链表划分：将链表按值x划分，小于x的在前，大于等于x的在后
 * 保持原有相对顺序
 */
void PartitionList(LinkList L, int x) {
    LinkList small = (LNode*)malloc(sizeof(LNode)); // 小于x的链表
    LinkList large = (LNode*)malloc(sizeof(LNode)); // 大于等于x的链表
    
    LNode *small_tail = small;
    LNode *large_tail = large;
    LNode *p = L->next;
    
    while (p != NULL) {
        LNode *next = p->next;
        if (p->data < x) {
            small_tail->next = p;
            small_tail = p;
        } else {
            large_tail->next = p;
            large_tail = p;
        }
        p = next;
    }
    
    // 连接两个链表
    small_tail->next = large->next;
    large_tail->next = NULL;
    
    // 更新原链表
    L->next = small->next;
    
    // 释放临时头结点
    free(small);
    free(large);
}
```

### 3.7 有序链表去重

```C
/**
 * 删除有序链表中的重复元素，只保留一个
 */
void RemoveDuplicates_Sorted(LinkList L) {
    LNode *p = L->next;
    
    while (p != NULL && p->next != NULL) {
        if (p->data == p->next->data) {
            LNode *q = p->next;
            p->next = q->next;
            free(q);
        } else {
            p = p->next;
        }
    }
}

/**
 * 删除所有重复元素（有序链表），重复的全部删除
 */
void RemoveAllDuplicates_Sorted(LinkList L) {
    LNode dummy;
    dummy.next = L->next;
    LNode *prev = &dummy;
    LNode *curr = L->next;
    
    while (curr != NULL) {
        if (curr->next != NULL && curr->data == curr->next->data) {
            // 跳过所有重复元素
            int val = curr->data;
            while (curr != NULL && curr->data == val) {
                LNode *temp = curr;
                curr = curr->next;
                free(temp);
            }
            prev->next = curr;
        } else {
            prev = curr;
            curr = curr->next;
        }
    }
    L->next = dummy.next;
}
```

## 4 测试示例

```C
// 测试函数
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // 创建链表
    LinkList L = CreateList_Tail(arr, n);
    printf("原链表: ");
    PrintList(L);
    
    // 测试逆置
    ReverseList(L);
    printf("逆置后: ");
    PrintList(L);
    
    // 测试查找倒数第2个元素
    LNode *kth = FindKthFromEnd(L, 2);
    if (kth != NULL) {
        printf("倒数第2个元素: %d\n", kth->data);
    }
    
    // 测试中点
    LNode *mid = FindMiddle(L);
    if (mid != NULL) {
        printf("中点元素: %d\n", mid->data);
    }
    
    return 0;
}
```

## 5 关键知识点总结

### 时间复杂度对比

| 操作 | 时间复杂度 | 空间复杂度 |
|------|------------|------------|
| 原地逆置 | O(n) | O(1) |
| 快慢指针判环 | O(n) | O(1) |
| 查找第k个元素 | O(k) | O(1) |
| 查找倒数第k个 | O(n) | O(1) |
| 删除最小值 | O(n) | O(1) |
| 有序链表合并 | O(m+n) | O(1) |

### 408考试重点

1. **原地逆置**：必须掌握头插法和三指针法
2. **快慢指针**：判环、找中点、找倒数第k个
3. **删除操作**：删除最小值、删除重复元素
4. **合并操作**：有序链表合并
5. **划分操作**：按条件划分链表

### 注意事项

- 始终注意**边界条件**（空链表、单结点）
- **带头结点** vs **不带头结点**的实现差异
- **内存管理**：及时释放不用的结点
- **指针操作顺序**：避免断链
