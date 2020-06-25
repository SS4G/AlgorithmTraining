func runningSum(nums []int) []int {
	res := make([]int, len(nums))
	for idx, n := range nums {
		if idx == 0 {
			res[0] = n
		} else {
			res[idx] = n + res[idx - 1]
		}
	} 
	return res
}