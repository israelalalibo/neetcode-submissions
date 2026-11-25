public class Solution {
    public bool hasDuplicate(int[] nums) {

        HashSet<int> seen = new HashSet<int>(nums); //Make a hashset using the nums argument

        if (seen.Count < nums.Length)
        {
            return true;
        }
        else{
            return false;
        }

    }
}