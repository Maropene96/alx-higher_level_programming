#include "lists.h"

/**
 * check_cycle - checks singly linked list
 * @list: shecked linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *first_n = list;
	listint_t *last_n = list;

	if (!list)
		return (0);

	while (first_n && last_n && last_n->next)
	{
		first_n = first_n->next;
		last_n = last_n->next->next;
		if (first_n == last_n)
			return (1);
	}

	return (0);
}
