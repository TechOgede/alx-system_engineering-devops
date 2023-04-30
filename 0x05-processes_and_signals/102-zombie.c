#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

/**
* infinite_while - eternal sleep
*
* Description: calls sleep on an infinite loop
* Return: an int
*/

int infinite_while(void);

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}


/**
* main - Entry point
*
* Return: 0 if successful, anything else otherwise
*/

int main(void)
{
	int i;
	pid_t zombie;

	for (i = 1; i <= 5; i++)
	{
		zombie = fork();

		if (zombie > 0)
			printf("Zombie process created, PID: %d\n", zombie);
		else if (zombie == 0)
			exit(0);
		else
			return (3);
	}

	infinite_while();

	return (0);
}
