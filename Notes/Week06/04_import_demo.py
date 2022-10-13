import functions_params_return as fns
# nickname as fns

nums = [1, 2, 3, 4, 5]

print(fns.double_num(7))

doubled_nums = map(
    fns.double_num,
    nums
)
# map create a map object like zip

print(list(doubled_nums))

# we can iterate through doubled_nums only once
# nothing left in doubled_nums as a map object
for d in doubled_nums:
    print(d)

# Lambda functions are anonymous functions
# defined inline
num_plus_5 = map(
    lambda x: x+5,
    nums
)
print(list(num_plus_5))


def function_with_no_name(x):
    return x+5


num_plus_5_too = map(
    function_with_no_name,
    nums
)
print(list(num_plus_5_too))

# use lambda x: not fns.is_prime to filter False
# direct expression "not fns.is_prime" is a boolean object and not callable
primes = filter(
    fns.is_prime,
    [14, 2, 11, 15, 13, 16, 7, 12, 31, 10]
)
# predicate will filter each value of the sequence is true
print(list(primes))

# press shift ZZ
print(help(fns.is_prime))

print(help(filter))
