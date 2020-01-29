

//---coded by sourav sarkar---


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
		for(i=3;i<=m;i++)
		{
			if(n%i==0)
				{
				return false;
			}
		}
	}
	return true;
}



int main() {
	//code
	int t,d,n,i,s;
	cin>>t;while(t--)
	{	
			cin>>n;
			for(i=2;i<=10000;i++)
			{
				if(prime(i)){
				
					d=(n-i);
					if(prime(d))
						{
						s=i;break;
						}
					}
					
			}
			cout<<s<<" "<<d<<endl;
			
	
	
	
}
}
