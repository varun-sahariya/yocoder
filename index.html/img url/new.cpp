// #include <iostream>

// using namespace std;

// int partition(int arr[], int str , int end) {
//     int pivot = arr[str];
    
//     int count = 0;
//     for(int i = str+1; i<=end ;i++) {
//         if(arr[i] <= pivot) {
//             count++;
//         }
//     }
    
//     int pivotIndex = str + count;
//     swap(arr[pivotIndex],arr[str]);
    
//     int i = str;
//     int j = end;
    
//     while(i < pivotIndex && j > pivotIndex) {
        
//         while(arr[i] <= pivot) {
//             i++;
//         }
//          while(arr[j] > pivot) {
//             j++;
//         }
        
//         if(i < pivotIndex && j > pivotIndex) {
//             swap(arr[i++],arr[j--]);
//         }
//     }
//     return pivotIndex;
// }

// void quickSort(int arr[] , int str , int end) {
    
//     if(str >= end) {
//         return;
        
//     }
//      int p = partition(arr,str,end);
     
//      quickSort(arr,str,p-1);
//      quickSort(arr,p+1,end);
    
// }

// int main()
// {
//    int arr[5] = {3,1,4,5,2};
//    int n = 5; 
  
//    quickSort(arr,0,n-1);
   
//    for(int i=0; i<n; i++) {
//        cout << arr[i] << " ";
//    } cout << endl;
  

//     return 0;
// }
// #include <iostream>

// using namespace std;

// void merge(int *arr, int str, int end)
// {     
//    int mid = str + (end - str)/2;

//      int len1 = mid - str + 1;
//      int len2 = end - mid;
     
//      int *first = new int[len1];
//      int *second = new int[len2];
     
//      int k = str;
//      int mainArrayIndex = str;
//      for(int i=0 ; i < len1 ; i++) {
//          first[i] = arr[mainArrayIndex++];
//      }
//       for(int i=0 ; i < len2 ; i++) {
//          second[i] = arr[mainArrayIndex++];
//      }
     
//      int index1=0;
//      int index2=0;
//      mainArrayIndex = str;
     
//      while(index1 < len1 && index2 < len2) {
//          if(first[index1] < second[index2]) {
//              arr[mainArrayIndex++] = first[index1++];
             
//          } else {
//                      arr[mainArrayIndex++] = second[index2++];
//          }
         
//          while(index1 < len1){
//                      arr[mainArrayIndex++] = first[index1++];
//          }
           
//          while(index2 < len2){
//                      arr[mainArrayIndex++] = second[index2++];
//          }
//      }
// }

// void mergeSort(int *arr, int str, int end)
// {

//   if (str >= end)
//     {
//       return;
//     }

//   int mid = str + (end - str)/2;

//   mergeSort (arr, str, mid );

//   mergeSort (arr, mid+1, end);

//   merge (arr, str, end);
// }

// int main ()
// {
//   int arr[5] = { 3, 1, 4, 2, 5 };
//   int n = 5;
  
//   mergeSort(arr , 0 , n-1);
  
//       for(int i=0; i<n; i++) {
//         cout << arr[i] << " ";
//     } cout << endl;
  

//   return 0;
// }
#include <iostream>

using namespace std;

void merge(int *arr, int str, int mid, int end) {
    int len1 = mid - str + 1;
    int len2 = end - mid;

    for (int i = 0; i < len1; i++) {
        int current = arr[str + i];
        int j = mid + 1 + i;

        // Find the correct position for the current element in the second half
        while (j <= end && arr[j] < current) {
            j++;
        }

        // Shift the elements in the second half to make space for the current element
        for (int k = end; k >= j; k--) {
            arr[k + 1] = arr[k];
        }

        // Place the current element in its correct position
        arr[j] = current;
    }
}

void mergeSort(int *arr, int str, int end) {
    if (str < end) {
        int mid = str + (end - str) / 2;

        // Sort first and second halves
        mergeSort(arr, str, mid);
        mergeSort(arr, mid + 1, end);

        // Merge the sorted halves
        merge(arr, str, mid, end);
    }
}

int main() {
    int arr[5] = {2, 5, 1, 6, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}


