#include <stdio.h>

int main()
{
	FILE *file;
	FILE *reverse;
	char filename[1024];
	char namu[1024]="TEST";
	scanf("%s",filename);
	file=fopen(filename,"r");
	reverse=fopen(namu,"w");
	if (file == NULL || reverse == NULL)
	{
		printf("NMSL\n");
		return 1;
	}
	fseek(file,0,"SEEK_END");
	int length = ftell(file);
	



	return 0;
}