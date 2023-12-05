# ID решения 85646145


def broken_search(nums=[], target=-1, left=0, right=None) -> int:
    if right is None:
        right = len(nums) - 1
    if right < left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:
        if nums[left] <= target and target <= nums[mid]:
            return broken_search(nums, target, left, mid - 1)
        return broken_search(nums, target, mid + 1, right)
    if nums[mid] <= target and target <= nums[right]:
        return broken_search(nums, target, mid + 1, right)
    return broken_search(nums, target, left, mid - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    postion = broken_search(arr, 5)
    print(postion)
    assert postion == 6
