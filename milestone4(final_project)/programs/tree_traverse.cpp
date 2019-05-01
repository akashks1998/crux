// C program for different tree traversals   
/* A binary tree node has data, pointer to left child 
and a pointer to right child */
class Node 
{ 
    int data; 
    class Node* left, *right; 
}; 


class Node :: int init(int data){
    this->data = data;
    this->left = 0;
    this->right = 0;
    return 0;
}
  
/* Given a binary tree, print its nodes according to the 
"bottom-up" postorder traversal. */
int printPostorder(class Node* node) 
{ 
    if (node == 0){
        return 0; 
    } 
        
  
    // first recur on left subtree 
    printPostorder(node->left); 
  
    // then recur on right subtree 
    printPostorder(node->right); 
  
    // now deal with the node 
    print_int(node->data);

    return 0;
} 
  
/* Given a binary tree, print its nodes in inorder*/
int printInorder(class Node* node) 
{ 
    if (node == 0){
        return 0; 
    } 
       
  
    /* first recur on left child */
    printInorder(node->left); 
  
    /* then print the data of node */
    print_int(node->data);
  
    /* now recur on right child */
    printInorder(node->right); 
    return 0;
} 
  
/* Given a binary tree, print its nodes in preorder*/
int printPreorder(class Node* node) 
{ 
    if (node == 0){
        return 0; 
    } 
    /* first print data of node */
    print_int(node->data);
  
    /* then recur on left sutree */
    printPreorder(node->left);  
  
    /* now recur on right subtree */
    printPreorder(node->right); 

    return 0;
}  
  
/* Driver program to test above functions*/
int main() 
{ 
    class Node *root = new (class Node);
    root->init(1); 

    class Node * l  = new (class Node); 
    root->left = l; 
    root->left->init(2);
    class Node * r  = new (class Node); 
    r->init(3);
    root->right = r;

    l = new (class Node); l->init(4);
    root->left->left     = l; 

    r = new (class Node); r->init(5);
    root->left->right = r;  

    print_char(10);
    printPreorder(root); 
  
    print_char(10);
    printInorder(root);  
  
    print_char(10);
    printPostorder(root); 
  
    return 0; 
} 