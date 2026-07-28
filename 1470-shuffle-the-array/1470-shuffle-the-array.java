class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];

        for (int i = 0; i < n; i++) {
            // Place element from first half
            result[2 * i] = nums[i];
            // Place element from second half
            result[2 * i + 1] = nums[n + i];
        }

        return result;
    }
}