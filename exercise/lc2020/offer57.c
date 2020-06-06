int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* result = malloc(sizeof(int) * 2);
    int left = 0;
    int right = numsSize - 1;
    int current_sum = nums[left] + nums[right];
    do {
        if (current_sum < target) {
            left++;
        } 
        else if (current_sum > target) {
            right--;
        }
        current_sum = nums[left] + nums[right];
    } while (current_sum != target);
    result[0] = nums[left];
    result[1] = nums[right];
    return result;
}