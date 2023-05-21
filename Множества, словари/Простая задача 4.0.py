nums = list(set(input().split('; ')))
coprime_dict = {}

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        a, b = int(nums[i]), int(nums[j])

        while b != 0:
            a, b = b, a % b

        if a == 1:
            coprime_dict[nums[i]] = coprime_dict.get(nums[i], []) + [nums[j]]
            coprime_dict[nums[j]] = coprime_dict.get(nums[j], []) + [nums[i]]

for key in sorted(coprime_dict.keys(), key=int):
    print(f'{key} - {", ".join(sorted(coprime_dict[key], key=int))}')