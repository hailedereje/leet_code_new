class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int,int>>st; // Stack to store the next greatest element and their index
        vector<int>ans(temperatures.size(),0);// answer vector initialized if there is no greater element to right store 0 else store the difference of their index

        for(int i=temperatures.size()-1;i>=0;i--)
        {
           
            while(st.size()>0 && st.top().first<=temperatures[i]) // Pop the elements in stack till the elements in stack is smaller than the current element
                {   
                    st.pop();
                }

            if(st.size()!=0) 
            ans[i] = (st.top().second-i); // if there is greater element to right in array  it will be at the top of stack as we are traversing from back, & so we store the difference in index  
            
            st.push({temperatures[i],i}); // Push elements and their index in stack
        }
        return ans;
    }
};