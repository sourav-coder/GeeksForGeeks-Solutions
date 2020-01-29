


// coded by sourav sarkar---


#include <bits/stdc++.h>
using namespace std;
bool prime(long int n)
{	int i;
	if(n<2)return false;
	else if(n==2)return true;
	else if(n%2==0)return false;
	else
	{
		int m=sqrt(n)+1;
		for(i=2;i<=m;i++)
		{
			if(n%i==0)
				return false;
		}
	}
	return true;
}



int main() {
	//code
	int t;
	cin>>t;while(t--)
	{	
		long int l,r,i,j;cin>>l>>r;
		for(i=l;i<=r;i++)
		{
		
		if(prime(i))
		{
			cout<<i<<" ";
		}
		
		
		}cout<<endl;
		//for(auto x:a)cout<<x<<" ";
		}//cout<<"\n";
				
	
	
	
	return 0;
}
