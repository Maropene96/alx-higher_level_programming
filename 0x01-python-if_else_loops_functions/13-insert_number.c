#include "lists.h"

/**
 * insert_node - Inserts a new node
 * @head:head of the linked list.
 * @number: The number 
 * Return: the address of the new node
 *or NULL if it fals
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node; 
	listint_t *new;
	listint_t head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
