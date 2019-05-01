// Template code taken form GeeksForGeeks

// C++ implementation to print the last k nodes 
// of linked list in reverse order 
#include <bits/stdc++.h> 
using namespace std; 
  
// Structure of a node 
struct Node { 
    int data; 
    Node* next; 
}; 
  
// Function to get a new node 
Node* getNode(int data) 
{ 
    // allocate space 
    Node* newNode = new Node; 
  
    // put in data 
    newNode->data = data; 
    newNode->next = NULL; 
    return newNode; 
} 
  
// Function to print the last k nodes 
// of linked list in reverse order 
void printLastKRev(Node* head, int& count, int k) 
{ 
    // if list is empty 
    if (!head) 
        return; 
  
    // Recursive call with the next node 
    // of the list 
    printLastKRev(head->next, count, k); 
  
    // Count variable to keep track of 
    // the last k nodes 
    count++; 
  
    // Print data 
    if (count <= k) 
        cout << head->data << " "; 
} 
  
// Driver code 
int main() 
{ 
    /* sdfjbsjkh 
    
    */

    // as
    Node* head = getNode(1); 
    head->next = getNode(2); 
    head->next->next = getNode(3); 
    head->next->next->next = getNode(4); 
    head->next->next->next->next = getNode(5); 
  
    int k = 4, count = 0; 
    cout << "HI THIS IS THE THEME #!"
  
    // print the last k nodes 
    printLastKRev(head, count, k); 
  
    return 0; 
} 