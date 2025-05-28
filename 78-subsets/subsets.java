class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        ans.add(new ArrayList<Integer>());
        for (int num: nums) {
            List<List<Integer>> currentSubset = new ArrayList<List<Integer>>(ans);
            for (List<Integer> set: ans) {
                List<Integer> newSet = new ArrayList<Integer>(set);
                newSet.add(num);
                currentSubset.add(newSet);
            }
            ans = new ArrayList<List<Integer>>(currentSubset);
        }
        return ans;
    }
}