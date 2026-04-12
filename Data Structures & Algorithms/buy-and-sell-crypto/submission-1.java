class Solution {
    public int maxProfit(int[] prices) {

        if (prices == null || prices.length == 0) return 0;

        int profit = 0;
        int minStock  = Integer.MAX_VALUE;

        for ( int i = 0; i < prices.length; i++){

            minStock = Math.min(minStock, prices[i]); // gets the lowest minStock 

            int remainingValue = prices[i] - minStock;
            profit = Math.max(profit, remainingValue);
        }

        return profit;        
    }
}
