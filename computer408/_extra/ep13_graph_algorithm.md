# 图 Graph — 408常考操作（邻接矩阵 + 邻接表）

> 📌 **命题趋势说明**：  
>
> - **2021–2025年算法大题全部采用邻接矩阵**（结构规整、便于手写）；  
> - **邻接表主要用于选择题或概念理解**；  
> - **所有图默认为无权图**，顶点编号通常为 `0 ~ n-1`；  
> - 本笔记优先保证**邻接矩阵实现的完整性**，邻接表作为补充。

---

## 1 数据结构定义

### 1.1 邻接矩阵（✅ 主流考法）

```c
#define MAXV 100

typedef struct {
    int arcs[MAXV][MAXV];  // 邻接矩阵，0/1 表示无边/有边
    int vexnum;            // 顶点数 n
} MGraph;
```

### 1.2 邻接表（辅助理解）

```c
typedef struct ArcNode {
    int adjvex;
    struct ArcNode *nextarc;
} ArcNode;

typedef struct VNode {
    ArcNode *firstarc;
} VNode, AdjList[MAXV];

typedef struct {
    AdjList vertices;
    int vexnum;
} ALGraph;
```

---

## 2 基础遍历操作

### 2.1 深度优先搜索（DFS）

**邻接矩阵实现（✅ 必掌握）**

```c
bool visited[MAXV];

void DFS_M(MGraph G, int v) {
    visited[v] = true;
    for (int w = 0; w < G.vexnum; w++)
        if (G.arcs[v][w] == 1 && !visited[w])
            DFS_M(G, w);
}

void DFSTraverse_M(MGraph G) {
    for (int i = 0; i < G.vexnum; i++) visited[i] = false;
    for (int i = 0; i < G.vexnum; i++)
        if (!visited[i]) DFS_M(G, i);
}
```

**邻接表实现（了解即可）**

```c
void DFS_L(ALGraph G, int v) {
    visited[v] = true;
    ArcNode *p = G.vertices[v].firstarc;
    while (p != NULL) {
        int w = p->adjvex;
        if (!visited[w]) DFS_L(G, w);
        p = p->nextarc;
    }
}
```

> ⏱️ 时间复杂度：  
>
> - 邻接矩阵：O(n²)  
> - 邻接表：O(n + e)

---

### 2.2 广度优先搜索（BFS）

**邻接矩阵实现（✅ 必掌握）**

```c
void BFSTraverse_M(MGraph G) {
    bool visited[MAXV] = {false};
    int Q[MAXV], front = 0, rear = 0;

    for (int i = 0; i < G.vexnum; i++) {
        if (!visited[i]) {
            visited[i] = true;
            Q[rear++] = i;
            while (front != rear) {
                int u = Q[front++];
                for (int v = 0; v < G.vexnum; v++) {
                    if (G.arcs[u][v] == 1 && !visited[v]) {
                        visited[v] = true;
                        Q[rear++] = v;
                    }
                }
            }
        }
    }
}
```

**邻接表实现（了解）**

```c
void BFSTraverse_L(ALGraph G) {
    bool visited[MAXV] = {false};
    int Q[MAXV], front = 0, rear = 0;
    for (int i = 0; i < G.vexnum; i++) {
        if (!visited[i]) {
            visited[i] = true;
            Q[rear++] = i;
            while (front != rear) {
                int u = Q[front++];
                ArcNode *p = G.vertices[u].firstarc;
                while (p) {
                    int v = p->adjvex;
                    if (!visited[v]) {
                        visited[v] = true;
                        Q[rear++] = v;
                    }
                    p = p->nextarc;
                }
            }
        }
    }
}
```

---

## 3 常考算法（按存储结构倾向分类）

### 3.1 判断无向图是否连通  
>
> ✅ **两种结构均可，但近年用邻接矩阵**

```c
bool isConnected_M(MGraph G) {
    for (int i = 0; i < G.vexnum; i++) visited[i] = false;
    DFS_M(G, 0);
    for (int i = 0; i < G.vexnum; i++)
        if (!visited[i]) return false;
    return true;
}
```

---

### 3.2 判断有向图是否有环（拓扑排序）  
>
> ✅ **408连续考查（2022），仅需掌握邻接矩阵实现**

```c
bool TopologicalSort(MGraph G) {
    int indegree[MAXV] = {0};
    for (int i = 0; i < G.vexnum; i++)
        for (int j = 0; j < G.vexnum; j++)
            if (G.arcs[j][i] == 1) indegree[i]++;

    int Q[MAXV], front = 0, rear = 0;
    for (int i = 0; i < G.vexnum; i++)
        if (indegree[i] == 0) Q[rear++] = i;

    int count = 0;
    while (front != rear) {
        int u = Q[front++];
        count++;
        for (int v = 0; v < G.vexnum; v++) {
            if (G.arcs[u][v] == 1) {
                if (--indegree[v] == 0)
                    Q[rear++] = v;
            }
        }
    }
    return count == G.vexnum;
}
```

> ❌ 不要求邻接表实现（真题未出现）

---

### 3.3 输出 s 到 t 的所有简单路径  
>
> ✅ **2023年真题，邻接矩阵实现**

```c
int path[MAXV], top = -1;

void findAllPaths(MGraph G, int s, int t, bool visited[]) {
    path[++top] = s;
    visited[s] = true;
    if (s == t) {
        // 可在此打印路径
    } else {
        for (int v = 0; v < G.vexnum; v++) {
            if (G.arcs[s][v] == 1 && !visited[v])
                findAllPaths(G, v, t, visited);
        }
    }
    visited[s] = false; // 回溯
    top--;
}
```

> ❌ 邻接表虽可行，但近年未考，不优先掌握

---

### 3.4 判断无向图是否为树  
>
> ✅ **2024年真题，邻接矩阵**

```c
bool isTree(MGraph G) {
    if (!isConnected_M(G)) return false;
    int edges = 0;
    for (int i = 0; i < G.vexnum; i++)
        for (int j = i + 1; j < G.vexnum; j++)
            if (G.arcs[i][j] == 1) edges++;
    return edges == G.vexnum - 1;
}
```

---

### 3.5 求无权图中 s 到 t 的最短路径长度  
>
> ✅ **2025年真题，BFS + 邻接矩阵**

```c
int shortestPath(MGraph G, int s, int t) {
    if (s == t) return 0;
    bool visited[MAXV] = {false};
    int dist[MAXV];
    int Q[MAXV], front = 0, rear = 0;

    visited[s] = true; dist[s] = 0; Q[rear++] = s;
    while (front != rear) {
        int u = Q[front++];
        for (int v = 0; v < G.vexnum; v++) {
            if (G.arcs[u][v] == 1 && !visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                if (v == t) return dist[v];
                Q[rear++] = v;
            }
        }
    }
    return -1; // 不可达
}
```

---

### 3.6 判断无向图是否为二分图（预测考点）  
>
> ⚠️ **尚未考过，但逻辑清晰，适合邻接矩阵**

```c
int color[MAXV]; // 0:未染色, 1/2:颜色

bool dfsColor(MGraph G, int u, int c) {
    color[u] = c;
    for (int v = 0; v < G.vexnum; v++) {
        if (G.arcs[u][v] == 1) {
            if (color[v] == c) return false;
            if (color[v] == 0 && !dfsColor(G, v, 3 - c))
                return false;
        }
    }
    return true;
}

bool isBipartite(MGraph G) {
    for (int i = 0; i < G.vexnum; i++) color[i] = 0;
    for (int i = 0; i < G.vexnum; i++) {
        if (color[i] == 0 && !dfsColor(G, i, 1))
            return false;
    }
    return true;
}
```
