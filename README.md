# ATSD_PZs

'''1.	Given a recursive function (= a definition of a recursive algorithm). !!!Done!!!

2.	Write a recursive algorithm int Prod( int a, int b) that calculates and returns a×b; !!!Done!!!

3.	Write a recursive algorithm  int Sum() that calculates and returns the sum of integer items of a linked list. !!!Done!!!

4.	Write a recursive algorithm  void printList() that prints integer items of a linked list. !!!Done!!!

5.	Write a recursive algorithm  void printListReverse() that prints integer items of a linked list in reverse order. !!!Done!!!

6.	Write an algorithm void BST_print_asc() that prints node values of a BST in ascending  order. !!!Done!!!

7.	Write an algorithm void BST_print_desc() that prints BST values in descending order. !!!Done!!!

8.	Write an algorithm int BST_sum() that returns the total sum of integer items in a binary search tree. !!!Done!!!

9.	Write an algorithm bool isEqual(BST *T2) that compares two binary search trees T1 and T2. It returns true if T1 == T2 (values and shape). !!!Done!!!

10.	Write an algorithm bool sameData(BST *T2) that compares two binary search trees T1 and T2. It returns true if T1 and T2 have the same data items (their  shapes may be different).
 !!!Done!!!
11.	Write an algorithm  function void BST_List(linkedList *L)  that copies data from a binary search tree T into a linked list L which is sorted in ascending order. !!!Done!!!

12.	Write an algorithm void makeEmpty() for the class BST. !!!Done!!!

13.	Write an algorithm int size() for the class BST that returns the number of data items (= nodes) in a BST. !!!Done!!!

14.	Write an algorithm for the method bool isBalanced() of the class BBST that returns true if a calling object is balanced and false otherwise. !!!Done!!!

15.	Given time-efficiency function of some algorithm A:   Done              
TA (n)  =  5, if n < 3; 4* TA (n - 3) + 2 , if n >= 3;
Find its asymptotic notation using Master Theorem.

Answer:
5 * 4 ^ (n / 3) - (2/3) * (1 - 4 ^ (n / 3))