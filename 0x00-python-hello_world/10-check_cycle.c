#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{

	while (list->next != NULL)
	{
		if (list < list->next)
		{
			return (1);
		}

		list = list->next;
	}
	return (0);
}
