#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp->next != NULL)
	{
		if (tmp->next == list)
		{
			return (1);
		}
		tmp = tmp->next;
	}
	return (0);
}
