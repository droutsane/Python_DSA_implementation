nums = [11,13,15,17]
N = len(nums)
start = 0
end = N - 1

while start <= end:
    mid = start + ((end-start)//2)
    nexte = (mid + 1) % N
    preve = (mid + N - 1) % N
    print("the mid now is", nums[mid])

    if nums[mid] < nums[nexte] and nums[mid] < nums[preve]:
        pivot = mid

    if nums[-1] >= nums[mid]:
        end = mid - 1
    elif nums[0] <= nums[mid]:
        start = mid + 1

st = 0
en = pivot-1

while st <= en:
    mi = st + (en-start)//2
    if nums[mi] == target:
        print("true")
    elif nums[mi] > target:
        en = mi -1
    else:
        st = mi +1

sta = pivot
enn = N -1

while sta <= enn:
    mii = sta + (enn-sta)//2
    if nums[mii] == target:
        print("true")
    elif nums[mii] > target:
        enn = mii -1
    else:
        st = mii +1





