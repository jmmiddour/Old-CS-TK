"""
Input: an integer
Returns: an integer
"""


# ### Chaz's Code (2nd Evening Session)... ### #
# # First pass solution (refactored to work)
# from functools import cache
#
# t_cache = {0: 0, 1: 0, 2: 1}
#
# # This Tribonacci sequence uses a dictionary
# def trib_memorized(n):
#     if n not in t_cache:
#         t_cache[n] = trib_memorized(
#             n - 1) + trib_memorized(
#             n - 2) + trib_memorized(
#             n - 3)
#
#     return t_cache[n]
#
#
# # # This Tribonacci sequence uses a cache (not sure which is better)
# # @cache
# # def trib_cache(n):
# #     if n == 0 or n == 1:
# #         return 0
# #
# #     elif n == 2:
# #         return 1
# #
# #     return trib_cache(n - 1) + trib_cache(n - 2) + trib_cache(n - 3)
#
#
# def eating_cookies(n):
#     if n < 0:
#         return None  # Invalid input
#
#     if n < 2:  # If it is 0 or 1
#         return 1  # return 1
#
#     if n == 2:
#         return 2
#
#     # return trib_cache(n + 2)
#     return trib_memorized(n + 2)


# ### Doc's Solution ### #
# TIP from Doc --> to skip a test,
#                  go to test file,
#                  on the line above the test to skip,
#                  `@unittest.skip` will skip that test only,
#                  instead of having to comment it out.
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(
#             n - 1) + eating_cookies(
#             n - 2) + eating_cookies(
#             n - 3)


# ### Ava's Solution ### #
def eating_cookies(n, cache={}):
    if cache == {}:
        # Empty cache bucket! Dictionary Comprehension {1:0, 2:0, 3:0, etc}
        cache = {i: 0 for i in range(n + 1)}

    if n < 0:  # if negative cookies no way of eating them
        return 0

    elif n == 0:  # If 0 cookies only 1 way to eat them
        return 1

    # Check cache to see if answer is stored in there
    if cache and cache[n] > 0:
        return cache[n]

    else:  # Store answer in cache
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(
            n - 2, cache) + eating_cookies(
            n - 3, cache)
        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
