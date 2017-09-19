#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

	int number;

	number = strtol(argv[1], NULL, 10);

	printf("Factors of %d are: ", number);

	for(int i = 1; i <= number; ++i) {

		if (number % i == 0) {
			printf("%d ", i);
		}
	}

	printf("\n");

	return 0;

}
