/**
 * Sorting numbers using insertion sort
 */
#include <stdio.h>

int main(){
	int i,j,key=0;
	int num[6] = {9,4,2,5,1,8};
	for(i=0;i<6;i++){
		key = num[i];
		j = i-1;
		while(j>=0 && key<num[j]){
			num[j+1] = num[j];
			j--;
		}
		num[j+1] = key;
		printf("%d\n",num[i]);
	}
	return 0;
}
