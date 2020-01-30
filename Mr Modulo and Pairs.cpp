


//coded by sourav sarkar
//complexity-O(n^2)

#include <bits/stdc++.h>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	while(t--)
	{
	    int n,k,i,j;cin>>n>>k;
	    long int a[n],c=0;
	    for(i=0;i<n;i++)cin>>a[i];
	    for(i=0;i<n;i++)
	    {   
	        //cin>>a[i];
	        for(j=0;j<n;j++)
	        {
	            if (a[i]%a[j]==k)c++;
	        }
	    }
	    cout<<c<<"\n";
	    
	}
	
	return 0;
}
