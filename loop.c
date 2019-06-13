#include <stdio.h>
#include <string.h>
#include <math.h>
int main() {
    int i,c,b;
    char a[11][100]={"even","odd","one","two","three","four","five","six","seven","eight","nine"};
    scanf("%d%d",&c,&b);
    for(i=c;i<=b;i++)
    {
        if((i>9) && (i%2==0))  printf("%s\n",a[0]);
                else if((i>9) && (i%2!=0)) printf("%s\n",a[1]);
        else    printf("%s\n",a[i+1]);
    }
    return 0;
}

