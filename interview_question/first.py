"""
# Problem: CI Pipeline Usage Reporting

runs thousands of CI pipelines daily. To help optimize compute costs and infrastructure usage,
 our team needs reporting on pipeline execution windows.

Each CI pipeline run is represented as a time interval `[start, end]`, where `start` and `end` are integer timestamps (`start < end`).

---

### Step 1 — Base Task: Active Execution Windows

Given an unsorted list of pipeline execution intervals, find all non-overlapping time intervals during which 
**at least one** CI pipeline was actively running.

#### Example:

- **Input:** `[[2, 5], [12, 15], [4, 8]]`

- **Output:** `[[2, 8], [12, 15]]`

- **Explanation:** 

  - Pipelines running between `[2, 5]` and `[4, 8]` overlap, meaning compute was active continuously from `2` to `8`.

  - The pipeline running between `[12, 15]` does not overlap with any other job.


  1st -> 2, 3, 4, 5
  2nd --> 4, 5, 6, 7, 8
  3rd --> 12, 13, 14, 15

  o/p -- 2, 8 # overlapping start and end index

  i/p -> [[2, 5], [4, 8], [12, 15]]


 stack -> [2, 5]
    [12, 15]
  for start, end in input:
    if start in 



"""

def find_overlapping_intervals(intervals):

    output = []

    intervals.sort(key=lambda x: x[1])
    overlapped_interval = intervals[0]
    for i in range(1, len(intervals)):
        if overlapped_interval[1] > intervals[i][0]:
            overlapped_interval = [overlapped_interval[0], intervals[i][1]]
        else:
            output.append(overlapped_interval)
            overlapped_interval = intervals[i]
    output.append(overlapped_interval)
    return output




if __name__ == "__main__":
    intervals = [[2, 5], [12, 15], [4, 8]]
    print(find_overlapping_intervals(intervals))

    intervals = [[2, 5], [12, 15], [10, 13]] #[[2, 5], [10, 15]] 

    print(find_overlapping_intervals(intervals))
