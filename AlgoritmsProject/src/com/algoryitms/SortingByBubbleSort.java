package com.algoryitms;

public class SortingByBubbleSort {

    private static void swapNumbers(int secondIndex, int[] arrayToBeSorted){

        //Comparing two indexes in array and swaping their positions if if array[i] > array[i+1]
        int temp = arrayToBeSorted[secondIndex];
        arrayToBeSorted[secondIndex] = arrayToBeSorted[secondIndex+1];
        arrayToBeSorted[secondIndex+1] = temp;

    }

    public static void sortAnArray(int[] arrayToBeSorted){
        int firstIndex;
        int secondIndex;
        for(firstIndex = arrayToBeSorted.length-1; firstIndex >= 1; firstIndex--){
            for(secondIndex = 0; secondIndex < firstIndex; secondIndex++){
                if(arrayToBeSorted[secondIndex] > arrayToBeSorted[secondIndex + 1]){
                    swapNumbers(secondIndex,arrayToBeSorted);
                }
            }

        }
    }

    public static void printArray(int[] arrayPassed){

        for(int oneElement : arrayPassed)
            System.out.print(oneElement + ", ");
    }

}
