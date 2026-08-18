class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        int compliment;

        for(int i = 0; i< nums.length; i++){
            compliment = target - nums[i];
            if(seen.containsKey(compliment)){
                return new int[]{seen.getOrDefault(compliment, 0), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}