class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        ans.add(new ArrayList<Integer>());
        for (int num: nums) {
            List<List<Integer>> newSubsets = new ArrayList();
            for (List<Integer> set: ans) {
                List<Integer> newSet = new ArrayList(set);
                newSet.add(num);
                newSubsets.add(newSet);
            }
            ans.addAll(newSubsets);
        }
        return ans;
    }
}