#include "lists.h"

/**
 * reverse_listint - reverses a singly linked linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prv_node = NULL;
	listint_t *now_node = *head;
	listint_t *nxt_node = NULL;

	while (now_node)
	{
		nxt_node = now_node->nxt_node;
		now_node->nxt_node = prv_node;
		prv_node = now_node;
		now_node = nxt_node;
	}

	*head = prv_node;
}

/**
 * is_palindrome - definess if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl_pnt = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->nxt_node == NULL)
		return (1);

	while (1)
	{
		fast = fast->nxt_node->nxt_node;
		if (!fast)
		{
			dup = sl_pnt->nxt_node;
			break;
		}
		if (!fast->nxt_node)
		{
			dup = sl_pnt->nxt_node->nxt_node;
			break;
		}
		sl_pnt = sl_pnt->nxt_node;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->nxt_node;
			temp = temp->nxt_node;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
