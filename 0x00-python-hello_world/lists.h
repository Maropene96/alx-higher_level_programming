#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * next: points to the next node
 * @n: int
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
int check_cycle(lisint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif