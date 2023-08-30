#include "lists.h"

/**
 * check_cycle - checks to see if a singly linked list has a cirle
 * @list: linked list
 * Return: return 0 if there is no circle and 1 if there is a circle
 */
int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *prev;
	
	prev = list;
	p2 = list;

	if (!list)
		return (0);

	while (prev && p2 && p2->next)
	{
		p2 = p2->next;
		prev = prev->next->next;
		if (p2 == prev)
			return (1);
	}


	return (0);
}
