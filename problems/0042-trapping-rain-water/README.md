# 0042 — Trapping Rain Water

Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/

## Approach

* Put one pointer at each end of the array.
* Keep track of the tallest bar seen so far on the left and on the right.
* Always move the pointer on the shorter side.
* Water at that spot = tallest bar on that side minus the bar's height.
* Add it to the total and keep going until the pointers meet.

## Complexity

Time: O(n)
Space: O(1)

## Tags

Array, Two Pointers, Dynamic Programming, Stack
