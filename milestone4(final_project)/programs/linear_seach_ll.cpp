// Iterative C program to search an element in linked list 
  
/* Link list node */
class Node { 
    int key; 
    class Node* next; 
}; 
  
/* Given a reference (pointer to pointer) to the head 
  of a list and an int, push a new node on the front 
  of the list. */
int push(class Node** head_ref, int new_key) 
{ 
    /* allocate node */
    class Node* new_node =  new(class Node); 
  
    /* put in the key  */
    new_node->key  = new_key; 
  
    /* link the old list off the new node */
    new_node->next = (*head_ref); 
  
    /* move the head to point to the new node */
    (*head_ref)    = new_node; 
    return 0;
} 
  
/* Checks whether the value x is present in linked list */
int search(class Node* head, int x) 
{ 
    class Node* current = head;  // Initialize current 
    while (current != 0) { 
        if (current->key == x){
            return 1; 
        } 
            
        current = current->next; 
    } 
    return 0; 
} 

int print_ll(class Node* head){
    class Node* current = head;  // Initialize current 
    while (current != 0) { 
        print_int(current->key);            
        current = current->next; 
    } 
    return 0; 
}
  
/* Driver program to test count function*/
int main() 
{ 
    /* Start with the empty list */
    class Node* head = 0; 
    int x = 21; 
  
    /* Use push() to conclass below list 
     14->21->11->30->10  */
    // class Node* new_node =  new(class Node); 
    // new_node->key  = 10; 
    // print_int(new_node->key);

    push(&head, 10); 
    push(&head, 30); 
    push(&head, 11); 
    push(&head, 21); 
    push(&head, 14); 
    
    print_ll(head);
    int res = search(head, 30);
    print_char('s');
    if(res == 1){
        print_int(1);
    }else{
        print_int(0);
    }  
    return 0; 
} 