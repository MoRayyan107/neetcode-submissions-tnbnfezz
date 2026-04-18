class Solution {
    public int[] replaceElements(int[] arr) {
        
        int maxValue = -1;

        for (int i = arr.length-1; i >= 0; i--){
            int currentVal = arr[i];
            arr[i] = maxValue;
            maxValue = Math.max(currentVal, maxValue);
        }

        return arr;
    }
}