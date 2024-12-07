from itertools import product

with open('7/input.txt') as file:
    lines = file.read().splitlines()

targets = {}

for line in lines:
    target, source = line.split(':')
    target = int(target.strip())
    sources = list(map(int, source.strip().split()))
    targets[target] = sources

def evaluate_expression(nums, ops):
    total = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            total += nums[i + 1]
        elif op == '*':
            total *= nums[i + 1]
    return total

def is_valid_target(target, nums):
    n = len(nums) - 1
    for ops in product(['+', '*'], repeat=n):
        if evaluate_expression(nums, ops) == target:
            return True
    return False

total = 0
for target, nums in targets.items():
    if is_valid_target(target, nums):
        total += target

print("Part 1:", total)


# Read the input file
with open('7/input.txt') as file:
    lines = file.read().splitlines()

targets = {}

# Parse the input
for line in lines:
    target, source = line.split(':')
    target = int(target.strip())
    sources = list(map(int, source.strip().split()))
    targets[target] = sources

def evaluate_expression_p2(nums, ops):
    total = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            total += nums[i + 1]
        elif op == '*':
            total *= nums[i + 1]
        elif op == '||':
            total = int(str(total) + str(nums[i + 1]))  # Concatenate digits
    return total

def is_valid_target_p2(target, nums):
    n = len(nums) - 1
    # Generate all combinations of operators
    for ops in product(['+', '*', '||'], repeat=n):
        if evaluate_expression_p2(nums, ops) == target:
            return True
    return False

# Calculate the total calibration result
total = 0
for target, nums in targets.items():
    if is_valid_target_p2(target, nums):
        total += target

print("Part 2:", total)