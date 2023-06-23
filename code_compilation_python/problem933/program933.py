def program933():
    #include <stdio.h>
    #include <algorithm>
    #include <iostream>
    
    using namespace std;
    
    int F(int *arr, int p_size){
        int res = 0;
        for (int i = 0; i < p_size; i++){
            int min_val = arr[i];
            res += min_val;
            for (int j = i + 1; j < p_size; j++)
                min_val = min(min_val, arr[j]), res += min_val;
        }
        return res;
    }
    
    bool NextPerm(int *arr, int p_size){
        for (int i = p_size - 2; i >= 0; i--)
            if (arr[i] < arr[i + 1]){
                int ind = i + 1;
                for (int j = i + 2; j < p_size; j++)
                    if (arr[j] > arr[i] && arr[j] < arr[ind])
                        ind = j;
                swap(arr[i], arr[ind]);
                sort(&arr[i + 1], &arr[p_size]);
                return 1;
            }
        return 0;
    }
    
    int MaxVal(int p_size){
        int arr[10];
        for (int i = 0; i < p_size; i++)
            arr[i] = i + 1;
        int res = F(arr, p_size);
        while (NextPerm(arr, p_size))
            res = max(res, F(arr, p_size));
        return res;
    }
    
    int main(){
        int n, k;
        scanf("%d%d", &n, &k);
    
        int max_val = MaxVal(n), cur_id = 0;
        int arr[10];
        for (int i = 0; i < n; i++)
            arr[i] = i + 1;
        if (F(arr, n) == max_val)
            cur_id++;
        while (cur_id < k)
            NextPerm(arr, n), cur_id += (F(arr, n) == max_val);
    
        for (int i = 0; i < n; i++)
            printf("%d ", arr[i]);
        return 0;
    }