class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        queue = []
        visited = [0] * n

        in_deg = [0] * n
        for lc in leftChild:
            if lc != -1:
                in_deg[lc] += 1
        for rc in rightChild:
            if rc != -1:
                in_deg[rc] += 1

        head = -1
        for i in range(n):
            if in_deg[i] == 0:
                head = i
                break
        
        if head == -1:
            return False

        queue.append(head)
        visited[head] = 1
        while len(queue) > 0:
            curr = queue.pop(0)

            lc = leftChild[curr]
            rc = rightChild[curr]

            if lc != -1:
                if visited[lc] != 1:
                    queue.append(lc)
                    visited[lc] = 1
                else:
                    return False
            if rc != -1:
                if visited[rc] != 1:
                    queue.append(rc)
                    visited[rc] = 1
                else:
                    return False
        
        if sum(visited) != n:
            return False

        return True