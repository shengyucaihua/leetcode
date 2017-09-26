# for a binary tree, left<=root<=right

# case 1 if L<=root.val<=right， keep the root node and perform recursion.
# case 2 if L>root.val trim all the left node.
# case 3 if root.val>R, trim all the right node.



def trimBST(root,L,R):
    # edge case
    if not root:
        return None

    if root.val>R:
        return trimBST(root.left,L,R)

    if root.val<L:
        return trimBST(root.right,L,R)

    trimBST(root.left,L,R)
    trimBST(root.right,L,R)
    return root





