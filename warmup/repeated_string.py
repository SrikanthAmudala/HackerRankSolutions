s = "a"
n = 1000000000000

# def repeat_str(s, n):
temp = s
count_a = s.count('a')
diff = n // len(s)
extra_term = (n - len(s)) % len(s)
total_a_count = diff * count_a + s[:extra_term].count('a')


# return total_a_count



