#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer of list
 * Return: 0  if there is no circle and 1 if the is a circle
 */
int check_cycle(listint_t *list)
{
	listint_t *p2 = list;
	listint_t *prev = list;

	if (!list)
		return (0);

	while (p2 && fast && prev->next)
	{
		p2= p2->next;
		prev = prev->next->next;
		if (p2 == prev)
			return (1);
	}

	return (0);
}
