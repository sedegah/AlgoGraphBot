def binary_search_ascii():
    return (
        \"Array: [1, 3, 5, 7, 9, 11, 13]\\n\"
        \"Target: 9\\n\"
        \"Start=0, End=6 → Mid=3 → arr[3]=7 < 9\\n\"
        \"Start=4, End=6 → Mid=5 → arr[5]=11 > 9\\n\"
        \"Start=4, End=4 → Mid=4 → arr[4]=9 ✓ Found\"
    )

def linear_search_ascii():
    return (
        \"Array: [4, 8, 2, 7, 5]\\n\"
        \"Looking for 7...\\n\"
        \"Index 0 → 4 ✗\\n\"
        \"Index 1 → 8 ✗\\n\"
        \"Index 2 → 2 ✗\\n\"
        \"Index 3 → 7 ✓ Found\"
    )
