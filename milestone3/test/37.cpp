#include<std.cpp>
// Iterative C++ program to reverse 
// a linked list 
class Node 
{ 
    int data; 
    class Node* next; 
}; 

class Node ::  void Node (int data){ 
    this->data = data; 
} 

  
class LinkedList 
{ 
   class Node *head; 
  
}; 

class LinkedList :: void reverse() 
    { 
        // Initialize current, previous and 
        // next pointers 
        class Node *current = this->head; 
        class Node *prev , *next ; 
  
  
        while (current) 
        { 
            // Store next 
            next = current->next; 
  
            // Reverse current node's pointer 
            current->next = prev; 
  
            // Move pointers one position ahead. 
            prev = current; 
            current = next; 
        } 
        this->head = prev; 
    } 
class LinkedList ::  void print() 
    { 
        class Node *temp = this->head; 
        while (temp) 
        { 
            temp = temp->next; 
        } 
    } 
class LinkedList :: void push(int data) 
    { 
        class Node *temp = new (class Node); 
        temp->next = this->head; 
        this->head = temp; 
    } 

/* Driver program to test above function*/
int main() 
{ 
    /* Start with the empty list */
    class LinkedList ll; 
    ll.push(20); 
    ll.push(4); 
    ll.push(15); 
    ll.push(85); 
  
   
    ll.print(); 
  
    ll.reverse(); 
  
    ll.print(); 
    return 0; 
} 