#include<stdio.h>
#include<malloc.h>
#include<string.h>
#include<stdlib.h>
#define maxlength 90000000


merge(long int arr[],long int s,long int m,long int e){
	long int i,j,k;
	long int n1=m-s+1,n2=e-m;
	long int L[n1],R[n2];
	for(i=0;i<n1;i++){
		L[i]=arr[s+i];
	}	
	for(j=0;j<n2;j++){
		R[j]=arr[m+1+j];
	}	
	i=j=0;
	k=s;
	while(i<n1 && j<n2){
		if(L[i]<=R[j]){
			arr[k]=L[i];
			i++;
		}	
		else{
			arr[k]=R[j];
			j++;		
		}
		k++;
	}
	while(i<n1){
		arr[k]=L[i];
		k++;
		i++;
	}
	while(j<n2){
		arr[k]=R[j];
		k++;
		j++;
	}
}


mergesort(long int arr[],long int s,long int e){
	if(s<e)
	{	
		long int m=s+(e-s)/2;	
		mergesort(arr,s,m);
		mergesort(arr,m+1,e);
		merge(arr,s,m,e);
	}
}

int main()
{
	int i,j;
	FILE *fp =fopen("file.txt","r");
	long int rows,count=0,uni,rows1,count1=0,uni1;
	long int **array,**array1;
	unsigned char  *ptr,*ptr1;
	long int *clust_d;
	long int *cl1_p;
	long int *cl2_p;
	printf("\nfile1 read started");
        if(fp!=NULL){
		unsigned char  line1[maxlength],line2[maxlength];
		if(fgets(line1,sizeof(line1),fp)!=NULL)
			rows=atoi(line1);
		if(fgets(line1,sizeof(line1),fp)!=NULL)
			uni=atoi(line1);
		array = (long int **)malloc(rows * sizeof(long int *));	
		clust_d = (long int*) malloc(rows * sizeof(long int));
               // long int clust_d[rows];
		for(i=0;i<rows;i++){
		count=0;
			fgets(line1,sizeof line1,fp);
			strcpy(line2,line1);
			ptr=strtok(line1," ");	
			while(ptr!=NULL){
				ptr=strtok(NULL," ");
				count++;	
			}
			array[i]=(long int *)malloc(count*sizeof (long int));
			ptr=strtok(line2," ");
			j=0;
			while(ptr!=NULL){
				array[i][j]=atoi(ptr);				
				ptr=strtok(NULL," ");
				j++;
			}
                        clust_d[i]=count;
			mergesort(array[i],0,count-1);
			long int k;
			//printf("\n");			
						
			count=0;
			
		}	
	}
	printf("\nfile2 read started");
	FILE *fp2 =fopen("file2.txt","r");
	long int *clust_d1;
        if(fp2!=NULL){
		unsigned char  line1[maxlength],line2[maxlength];
		if(fgets(line1,sizeof(line1),fp2)!=NULL)
			rows1=atoi(line1);
		if(fgets(line1,sizeof(line1),fp2)!=NULL)
			uni1=atoi(line1);
		array1 = (long int **)malloc(rows1 * sizeof(long int *));	
		clust_d1 = (long int*) malloc(rows1 * sizeof(long int));
               // long int clust_d[rows];
		for(i=0;i<rows1;i++){
		count1=0;
			fgets(line1,sizeof line1,fp2);
			strcpy(line2,line1);
			ptr1=strtok(line1," ");	
			while(ptr1!=NULL){
				ptr1=strtok(NULL," ");
				count1++;	
			}
			array1[i]=(long int *)malloc(count1*sizeof (long int));
			ptr1=strtok(line2," ");
			j=0;
			while(ptr1!=NULL){
				array1[i][j]=atoi(ptr1);				
				ptr1=strtok(NULL," ");
				j++;
			}
                        clust_d1[i]=count1;
			mergesort(array1[i],0,count1-1);
			long int k;
			//printf("\n");			
						
			count1=0;
			
		}	
	}
	long int found,inner_cnt=0,p=0;
	long int *unique = (long int*) malloc((uni+1) * sizeof(long int));
	

	//finding unique points
	printf("\nfinding unique elements");
	
	for(i=0;i<rows;i++)
		{
		 for(j=0;j<clust_d[i];j++)
			{
				found=0;
				for(inner_cnt=0;inner_cnt<p;inner_cnt++)
				{

					if(unique[inner_cnt] == array[i][j])
					{
					printf("\nelements found %lu",array[i][j]);

					  found=1;
					 break;
					}


				}
					if(found == 0)
					{
					//	printf("\nelements not found %lu",array[i][j]);

					  unique[p]=array[i][j];
					  p++;
					  
					}
				       found=0;

			}
				//printf("%d ",array[i][j]);
		}
		printf("\nunique elements found1 %lu ",p);
		printf("\nstarting binary search1");
		printf("\nrow details1 %lu %lu ",rows,rows1);
	
	//finding unique pairs
	cl1_p = (long int *) malloc((rows+1) * sizeof(long int));
	cl2_p = (long int *) malloc((rows1+1) * sizeof(long int));
	printf("\nrow details2 %lu %lu ",rows,rows1);
	
	printf("\nstarting binary search2");
	long int pair1,pair2,ii;
	long int ele1,ele2,sum,clu1,clu2,l_max1=0,l_max2=0;
	long double  a=0,b=0,c=0,d=0;
	int yy=0;
	for(ii=0;ii<uni;ii++)
			{
				if(yy==500)
				{
			printf("\n processing pair %lu ",ii);
				yy=0;
				}
				yy++;
			 for(j=ii+1;j<uni;j++)
			   {
				clu1=0,clu2=0;
				pair1=unique[ii];
				pair2=unique[j];
				//printf("\n pair %lu \t %lu",pair1,pair2);
				for(i=0;i<rows;i++)
				{
				//printf("\nbinary search for cluster %lu",i);
 
				ele1=0,ele2=0;
				  //ele1 = binarySearch(a,l,u,m);	
				 long int mid1,l1,u1,m1;
				l1=0;
				u1=clust_d[i];
				m1=pair1;
				while(l1<=u1){
					mid1=(l1+u1)/2;
					if(m1==array[i][mid1]){	
								//printf("found ele %d", +array[i][mid1]); 							
								ele1=1;
								break;
							     }
					else if(m1<array[i][mid1]){
							     u1=mid1-1;
							      }
					 else
							l1=mid1+1;
				            }

				//for second ele

				 long int mid2,l2,u2,m2;
				l2=0;
				u2=clust_d[i];
				//printf("val of clissss %d\n\n ",clust_d[i]); 
				m2=pair2;
				while(l2<=u2){
					mid2=(l2+u2)/2;
					if(m2==array[i][mid2]){	
								//printf(" \t%d\n", +array[i][mid2]); 							
								ele2=1;
								break;
							     }
					else if(m2<array[i][mid2]){
							     u2=mid2-1;
							      }
					 else
							l2=mid2+1;
				            }
				
				if(ele1 == 1 && ele2 == 1)
					{
					//pair[noo][j][2]=pair[noo][j][2]+1;
					//printf("The both number is found.");
					clu1=clu1+1;
					}
					// long int max= pair[noo][0][2];
		               		
							   
				}
				if(l_max1<clu1)
					l_max1=clu1;

				
				cl1_p[clu1]=cl1_p[clu1]+1;



				//finding the pair in other cluster
				for(i=0;i<rows1;i++)
				{
				//printf("\nbinary search for cluster %lu",i);
 
				ele1=0,ele2=0;
				  //ele1 = binarySearch(a,l,u,m);	
				 long int mid1,l1,u1,m1;
				l1=0;
				u1=clust_d1[i];
				m1=pair1;
				while(l1<=u1){
					mid1=(l1+u1)/2;
					if(m1==array1[i][mid1]){	
								//printf("found ele %d", +array[i][mid1]); 							
								ele1=1;
								break;
							     }
					else if(m1<array1[i][mid1]){
							     u1=mid1-1;
							      }
					 else
							l1=mid1+1;
				            }

				//for second ele

				 long int mid2,l2,u2,m2;
				l2=0;
				u2=clust_d1[i];
				//printf("val of clissss %d\n\n ",clust_d[i]); 
				m2=pair2;
				while(l2<=u2){
					mid2=(l2+u2)/2;
					if(m2==array1[i][mid2]){	
								//printf(" \t%d\n", +array[i][mid2]); 							
								ele2=1;
								break;
							     }
					else if(m2<array1[i][mid2]){
							     u2=mid2-1;
							      }
					 else
							l2=mid2+1;
				            }
				
				if(ele1 == 1 && ele2 == 1)
					{
					//pair[noo][j][2]=pair[noo][j][2]+1;
					//printf("The both number is found.");
					clu2=clu2+1;
					}
					// long int max= pair[noo][0][2];
		               		
							   
				}				
				
				if(l_max2<clu2)
					l_max2=clu2;

				cl2_p[clu2]=cl2_p[clu2]+1;
	         if(clu1==clu2 && clu1>=1)
			{
			a++;
			}
		  else if(clu1>clu2)
			{
			b++;
			}
		 else if(clu1<clu2)
			{
			c++;

                        }
			else
			d++;
		





				
			    }
			}
			printf("found value of abcd");
      
		long int min_b;
		if(l_max2<l_max1)
			min_b=l_max2;
		else
			min_b=l_max1;

		long double   obs,exp,omega;
		long double   RI=0,ARI=0;
		RI = (a+d)/(a+b+c+d);
		printf("\n\n\nRand Index is: %Lf",RI);
		uni = ( uni * ( uni-1))/2;
		printf("\na b  c d  %Lf\t%Lf\t%Lf\t%Lf ",a,b,c,d);
			
		ARI = (long double  )((uni*(a+d))-((a+b)*(a+c)+(c+d)*(b+d)))/((uni*uni)-((a+b)*(a+c)+(c+d)*(b+d)));
		printf("\n\n\nAdj. Rand Index is: %Lf",ARI);
		long int product=0;
		for(i=0;i<=min_b;i++)
		{
			product = product + (cl1_p[i]*cl2_p[i]);
                }
				obs=RI;
		exp=(long double  )product/(uni*uni);
			omega=(obs-exp)/(1-exp);
			printf("\nObserved Index is: %Lf ",obs);
			printf(";\tExpected Index is: %Lf ",exp);
			printf("\n\n\nOmega Index is: %Lf ",omega);
		
		printf("\n");
		//for(i=0;i<uni1;i++)
		//	printf("\t%lu",uni1);
		free(array);
		free(array1);
		free(clust_d);
		


		//printf("\n%lu\t %lu\t %lu\t %lu \t %lu\t %lu\t %lu \t",l_max1,l_max2,min_b,a,b,c,d);


}
