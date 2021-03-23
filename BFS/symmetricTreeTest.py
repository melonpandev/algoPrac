import symmetricTree
def tree_depth(n):
    curr=n
    depth = -1
    while curr > 0:
        depth += 1
        curr -= 2**depth
    return depth

def list_to_tree(l):
    init = None
    depth=tree_depth(len(l))
    for i in range(depth):

    return init


def test_mirrorTree():
    mirrorTree=list_to_tree([1,2,2,3,4,4,3])
    assert Solution().isSymmetric(mirrorTree) == True, "Should be True"

def test_nonMirrorTree():
    mirrorTree=list_to_tree([1,2,2,null,3,null,3])
    assert Solution().isSymmetric(mirrorTree) == False, "Should be False"

if __name__ == "__main__":
    test_mirrorTree()
    test_nonMirrorTree()
    print("Everything passed")