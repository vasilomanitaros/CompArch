#include <stdio.h>
#include <stdlib.h>

void fibonacci(int n) {
	int a=0, b=1, next;
	for (int i=0; i<n; i++) {
		if (i<=1) {
			next=i;
		} else {
			next=a+b;
			a=b;
			b=next;
		}
		printf("%d ",next);
	}
	printf("\n");
}

int main(int argc, char *argv[]) {
	if (argc!= 2) {
		printf("Usage: %s <number_of_terms>\n",argv[0]);
		return 1;
}
int n = atoi(argv[1]);
if (n<0) {
printf("Please enter a non-negative integer\n");
return 1;
}

printf("Fibonacci Sequence:\n");
fibonacci(n);
return 0;
}