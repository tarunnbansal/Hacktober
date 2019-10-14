#include<iostream>
using namespace std;


int smallest()
{
   	int size,k;
    int A[size];

	cout<<"enter the size of array";
	cin>>size;
	
	for(int i=0;i<size;i++)
	{
		cout<<"enter array elements";
		cin>>A[i];
		
	}
	cout<<"enter the kth smallest elment";
	cin>>k;
	if(k>size)
	{
	  cout<<"not eligible";
	  return 0;
    }
    else 
        return A[k];
        
}


int main()
{
	
	int result = smallest();
	
     cout<< result;
	
	
	
}
