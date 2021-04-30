int check_cycle(listint_t *list)
{
	listint_t *nextx = list, *nextxnext = list;
	while (nextx && nextxnext  && nextxnext->next)
	{
		nextx = nextx->next;
		nextxnext  = nextxnext->next->next;
		if (nextx == nextxnext)
		{
			return (1);
		}
	}
	return (0);
}